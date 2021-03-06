from txGoogle.googleService import GoogleService
from urllib import quote as urlibQuoteEncode
from txGoogle.googleResource import GoogleResource


class TimeseriesDescriptors(GoogleResource):
    def __init__(self, service, conn, *args, **kwargs):
        super(TimeseriesDescriptors, self).__init__(service, conn, *args, **kwargs)

    def list(self, project, metric, youngest, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, count=None, timespan=None, labels=None, pageToken=None, oldest=None, kind=None):
        '''List the descriptors of the time series that match the metric and labels values and that have data points in the interval. Large responses are paginated; use the nextPageToken returned in the response to request subsequent pages of results by setting the pageToken query parameter to the value of the nextPageToken.'''
        queryParams = {
            'url': 'https://www.googleapis.com/cloudmonitoring/v2beta1/projects/{project}/timeseriesDescriptors/{metric}',
            'method': 'GET',
            'resultType': 'ListTimeseriesDescriptorsResponse',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'count': count,
                'project': urlibQuoteEncode(project, safe=''),
                'timespan': timespan,
                'metric': urlibQuoteEncode(metric, safe=''),
                'labels': labels,
                'youngest': youngest,
                'pageToken': pageToken,
                'oldest': oldest,
            },
            'httpBodyParams': {
                'kind': kind,
            },
        }
        return self._request(queryParams)


class Timeseries(GoogleResource):
    def __init__(self, service, conn, *args, **kwargs):
        super(Timeseries, self).__init__(service, conn, *args, **kwargs)

    def list(self, project, metric, youngest, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, count=None, timespan=None, labels=None, pageToken=None, oldest=None, kind=None):
        '''List the data points of the time series that match the metric and labels values and that have data points in the interval. Large responses are paginated; use the nextPageToken returned in the response to request subsequent pages of results by setting the pageToken query parameter to the value of the nextPageToken.'''
        queryParams = {
            'url': 'https://www.googleapis.com/cloudmonitoring/v2beta1/projects/{project}/timeseries/{metric}',
            'method': 'GET',
            'resultType': 'ListTimeseriesResponse',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'count': count,
                'project': urlibQuoteEncode(project, safe=''),
                'timespan': timespan,
                'metric': urlibQuoteEncode(metric, safe=''),
                'labels': labels,
                'youngest': youngest,
                'pageToken': pageToken,
                'oldest': oldest,
            },
            'httpBodyParams': {
                'kind': kind,
            },
        }
        return self._request(queryParams)


class MetricDescriptors(GoogleResource):
    def __init__(self, service, conn, *args, **kwargs):
        super(MetricDescriptors, self).__init__(service, conn, *args, **kwargs)

    def list(self, project, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, count=None, pageToken=None, query=None, kind=None):
        '''List metric descriptors that match the query. If the query is not set, then all of the metric descriptors will be returned. Large responses will be paginated, use the nextPageToken returned in the response to request subsequent pages of results by setting the pageToken query parameter to the value of the nextPageToken.'''
        queryParams = {
            'url': 'https://www.googleapis.com/cloudmonitoring/v2beta1/projects/{project}/metricDescriptors',
            'method': 'GET',
            'resultType': 'ListMetricDescriptorsResponse',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'count': count,
                'pageToken': pageToken,
                'project': urlibQuoteEncode(project, safe=''),
                'query': query,
            },
            'httpBodyParams': {
                'kind': kind,
            },
        }
        return self._request(queryParams)


class Cloudmonitoring(GoogleService):
    '''API for accessing Google Cloud and API monitoring data.'''
    _DEFAULT_SCOPES = [u'https://www.googleapis.com/auth/monitoring.readonly']

    def __init__(self, conn=None, scopes=None, *args, **kwargs):
        if scopes is not None:
            self._scopes = scopes
        else:
            self._scopes = self._DEFAULT_SCOPES
        conn.registerScopes(self._scopes)
        super(Cloudmonitoring, self).__init__(conn, *args, **kwargs)
        self.timeseriesDescriptors = TimeseriesDescriptors(self, conn, *args, **kwargs)
        self.timeseries = Timeseries(self, conn, *args, **kwargs)
        self.metricDescriptors = MetricDescriptors(self, conn, *args, **kwargs)
