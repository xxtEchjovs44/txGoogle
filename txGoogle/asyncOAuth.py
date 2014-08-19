'''
Created on 14 jul. 2014

@author: sjuul
'''
from asyncUtils import ignoreFirstArg
from asyncHttp import AsyncHttp
from twisted.internet.defer import Deferred
from twisted.internet.defer import succeed
from twisted.internet.defer import fail
import simplejson as json
from twisted.python import log
from urllib import urlencode
import webbrowser
import logging
import time
import os


'''
Currently implemented as installed app. This doesn't require us to run a web server.
The difference between "installed app" and webserver is that now we need to copy-paste the oauth token into our console,
when running a webserver the oauth endpoint will send the token to the webserver.
The rest of the grant process is the same.

Reference: https://developers.google.com/accounts/docs/OAuth2InstalledApp
Playground: https://developers.google.com/oauthplayground/

If you want to understand the "flow" of oauth the playground will take you through the steps
'''


class AsyncOAuthConnectionHandler(AsyncHttp):

    def __init__(self, authUrl, tokenUrl, scope, clientId=None, clientSecret=None, credentialsFileName=None, redirect_uri='urn:ietf:wg:oauth:2.0:oob', jsonHandleFun=None, **grantKwargs):
        super(AsyncOAuthConnectionHandler, self).__init__(jsonHandleFun)
        self._grantUrl = authUrl
        self._tokenUrl = tokenUrl
        self._clientId = clientId
        self._clientSecret = clientSecret
        self._redirectUri = redirect_uri
        self._grantKwargs = grantKwargs
        self._grantKwargs['redirect_uri'] = redirect_uri
        self._grantKwargs['client_id'] = clientId
        self._grantKwargs['scope'] = scope
        self._credentialsFileName = credentialsFileName
        if credentialsFileName is None:
            raise Exception('No credentialsFileName is specified')
        self._getAccessCredsDfd = None
        self._credentialsDct = None
        self._loadCredentials()

    def _getAccessCredentials(self, authCode=None, refreshToken=None):
        if self._getAccessCredsDfd is None:
            self._getAccessCredsDfd = Deferred()
        else:
            return self._getAccessCredsDfd
        if refreshToken:
            tokenParams = {
                'client_id': self._clientId,
                'client_secret': self._clientSecret,
                'grant_type': 'refresh_token',
                'refresh_token': refreshToken
            }
        else:
            if authCode is None:
                url = self._grantUrl + '?' + urlencode(self._grantKwargs)
                print url
                webbrowser.open(url)
                authCode = raw_input('\nCODE:')
            tokenParams = {
                'code': authCode,
                'redirect_uri': self._redirectUri,
                'client_id': self._clientId,
                'client_secret': self._clientSecret,
                'grant_type': 'authorization_code'
            }

        dfd = super(AsyncOAuthConnectionHandler, self).httpRequest(self._tokenUrl, urlParams=tokenParams, method='POST', formEncode=True)
        dfd.addCallback(self.loadTokenDict, refreshToken=refreshToken)
        return self._getAccessCredsDfd

    def loadTokenDict(self, tokenDct, refreshToken):
        log.msg('Received token dict', logLevel=logging.INFO)
        self._credentialsDct = tokenDct
        self._credentialsDct['expirationTimestamp'] = int(time.time()) + self._credentialsDct['expires_in']
        if refreshToken and 'refresh_token' not in self._credentialsDct:
            self._credentialsDct['refresh_token'] = refreshToken
        parentFolder = os.path.dirname(self._credentialsFileName)
        if parentFolder and not os.path.exists(parentFolder):
            os.makedirs(parentFolder)
        fl = open(self._credentialsFileName, 'w')
        json.dump(self._credentialsDct, fl)
        self._getAccessCredsDfd.callback('Ok')
        fl.close()
        return 'Ok'

    def _checkCredentialsDct(self):
        if 'expirationTimestamp' not in self._credentialsDct or 'refresh_token' not in self._credentialsDct:
            log.msg('Missing expirationTimestamp or refresh_token', logLevel=logging.INFO)
            return self._getAccessCredentials()
        elif self._credentialsDct['expirationTimestamp'] < int(time.time() - 10):
            log.msg('Grant expired, refreshing', logLevel=logging.INFO)
            return self._getAccessCredentials(refreshToken=self._credentialsDct['refresh_token'])
        else:
            return succeed('grant still valid')

    def _loadCredentials(self):
        if self._credentialsDct:
            return self._checkCredentialsDct()
        elif self._getAccessCredsDfd:
            return self._getAccessCredsDfd
        elif os.path.exists(self._credentialsFileName):
                credsFile = open(self._credentialsFileName, 'r')
                creds = json.load(credsFile)
                credsFile.close()
                self._credentialsDct = creds
                return self._checkCredentialsDct()
        else:
            return self._getAccessCredentials()

    def httpRequest(self, url, urlParams=None, bodyParams=None, headers=None, method='POST', formEncode=False):
        dfd = self._loadCredentials()
        if not urlParams:
            urlParams = {}

        @dfd.addCallback
        def injectAccesToken(dummy):
            urlParams['access_token'] = self._credentialsDct['access_token']

        dfd.addCallback(ignoreFirstArg, super(AsyncOAuthConnectionHandler, self).httpRequest, url, urlParams=urlParams, bodyParams=bodyParams, headers=headers, method=method, formEncode=formEncode)
        return dfd