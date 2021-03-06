from txGoogle.googleService import GoogleService
from urllib import quote as urlibQuoteEncode
from txGoogle.googleResource import GoogleResource


class Tables(GoogleResource):
    def __init__(self, service, conn, *args, **kwargs):
        super(Tables, self).__init__(service, conn, *args, **kwargs)

    def insert(self, projectId, datasetId, tableId, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, expirationTime=None, description=None, friendlyName=None, schema_fields=None, query=None):
        '''Creates a new, empty table in the dataset.'''
        queryParams = {
            'url': 'https://www.googleapis.com/bigquery/v2/projects/{projectId}/datasets/{datasetId}/tables',
            'method': 'POST',
            'resultType': 'Table',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'projectId': urlibQuoteEncode(projectId, safe=''),
                'datasetId': urlibQuoteEncode(datasetId, safe=''),
            },
            'httpBodyParams': {
                'description': description,
                'friendlyName': friendlyName,
                'expirationTime': expirationTime,
                'schema': {
                    'fields': schema_fields,
                },
                'tableReference': {
                    'projectId': projectId,
                    'tableId': tableId,
                    'datasetId': datasetId,
                },
                'view': {
                    'query': query,
                },
            },
        }
        return self._request(queryParams)

    def get(self, projectId, tableId, datasetId, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None):
        '''Gets the specified table resource by table ID. This method does not return the data in the table, it only returns the table resource, which describes the structure of this table.'''
        queryParams = {
            'url': 'https://www.googleapis.com/bigquery/v2/projects/{projectId}/datasets/{datasetId}/tables/{tableId}',
            'method': 'GET',
            'resultType': 'Table',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'projectId': urlibQuoteEncode(projectId, safe=''),
                'tableId': urlibQuoteEncode(tableId, safe=''),
                'datasetId': urlibQuoteEncode(datasetId, safe=''),
            },
            'httpBodyParams': {
            },
        }
        return self._request(queryParams)

    def list(self, datasetId, projectId, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, pageToken=None, maxResults=None):
        '''Lists all tables in the specified dataset.'''
        queryParams = {
            'url': 'https://www.googleapis.com/bigquery/v2/projects/{projectId}/datasets/{datasetId}/tables',
            'method': 'GET',
            'resultType': 'TableList',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'pageToken': pageToken,
                'datasetId': urlibQuoteEncode(datasetId, safe=''),
                'maxResults': maxResults,
                'projectId': urlibQuoteEncode(projectId, safe=''),
            },
            'httpBodyParams': {
            },
        }
        return self._request(queryParams)

    def update(self, projectId, tableId, datasetId, projectId_, tableId_, datasetId_, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, expirationTime=None, description=None, friendlyName=None, schema_fields=None, query=None):
        '''Updates information in an existing table. The update method replaces the entire table resource, whereas the patch method only replaces fields that are provided in the submitted table resource.'''
        queryParams = {
            'url': 'https://www.googleapis.com/bigquery/v2/projects/{projectId}/datasets/{datasetId}/tables/{tableId}',
            'method': 'PUT',
            'resultType': 'Table',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'projectId': urlibQuoteEncode(projectId, safe=''),
                'tableId': urlibQuoteEncode(tableId, safe=''),
                'datasetId': urlibQuoteEncode(datasetId, safe=''),
            },
            'httpBodyParams': {
                'description': description,
                'friendlyName': friendlyName,
                'expirationTime': expirationTime,
                'schema': {
                    'fields': schema_fields,
                },
                'tableReference': {
                    'projectId': projectId_,
                    'tableId': tableId_,
                    'datasetId': datasetId_,
                },
                'view': {
                    'query': query,
                },
            },
        }
        return self._request(queryParams)

    def patch(self, projectId, tableId, datasetId, projectId_, tableId_, datasetId_, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, expirationTime=None, description=None, friendlyName=None, schema_fields=None, query=None):
        '''Updates information in an existing table. The update method replaces the entire table resource, whereas the patch method only replaces fields that are provided in the submitted table resource. This method supports patch semantics.'''
        queryParams = {
            'url': 'https://www.googleapis.com/bigquery/v2/projects/{projectId}/datasets/{datasetId}/tables/{tableId}',
            'method': 'PATCH',
            'resultType': 'Table',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'projectId': urlibQuoteEncode(projectId, safe=''),
                'tableId': urlibQuoteEncode(tableId, safe=''),
                'datasetId': urlibQuoteEncode(datasetId, safe=''),
            },
            'httpBodyParams': {
                'description': description,
                'friendlyName': friendlyName,
                'expirationTime': expirationTime,
                'schema': {
                    'fields': schema_fields,
                },
                'tableReference': {
                    'projectId': projectId_,
                    'tableId': tableId_,
                    'datasetId': datasetId_,
                },
                'view': {
                    'query': query,
                },
            },
        }
        return self._request(queryParams)

    def delete(self, projectId, tableId, datasetId, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None):
        '''Deletes the table specified by tableId from the dataset. If the table contains data, all the data will be deleted.'''
        queryParams = {
            'url': 'https://www.googleapis.com/bigquery/v2/projects/{projectId}/datasets/{datasetId}/tables/{tableId}',
            'method': 'DELETE',
            'resultType': 'empty',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'projectId': urlibQuoteEncode(projectId, safe=''),
                'tableId': urlibQuoteEncode(tableId, safe=''),
                'datasetId': urlibQuoteEncode(datasetId, safe=''),
            },
            'httpBodyParams': {
            },
        }
        return self._request(queryParams)


class Datasets(GoogleResource):
    def __init__(self, service, conn, *args, **kwargs):
        super(Datasets, self).__init__(service, conn, *args, **kwargs)

    def insert(self, projectId, datasetId, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, description=None, projectId_=None, access=None, friendlyName=None):
        '''Creates a new empty dataset.'''
        queryParams = {
            'url': 'https://www.googleapis.com/bigquery/v2/projects/{projectId}/datasets',
            'method': 'POST',
            'resultType': 'Dataset',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'projectId': urlibQuoteEncode(projectId, safe=''),
            },
            'httpBodyParams': {
                'access': access,
                'friendlyName': friendlyName,
                'description': description,
                'datasetReference': {
                    'projectId': projectId_,
                    'datasetId': datasetId,
                },
            },
        }
        return self._request(queryParams)

    def get(self, projectId, datasetId, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None):
        '''Returns the dataset specified by datasetID.'''
        queryParams = {
            'url': 'https://www.googleapis.com/bigquery/v2/projects/{projectId}/datasets/{datasetId}',
            'method': 'GET',
            'resultType': 'Dataset',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'projectId': urlibQuoteEncode(projectId, safe=''),
                'datasetId': urlibQuoteEncode(datasetId, safe=''),
            },
            'httpBodyParams': {
            },
        }
        return self._request(queryParams)

    def list(self, projectId, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, pageToken=None, all=None, maxResults=None):
        '''Lists all the datasets in the specified project to which the caller has read access; however, a project owner can list (but not necessarily get) all datasets in his project.'''
        queryParams = {
            'url': 'https://www.googleapis.com/bigquery/v2/projects/{projectId}/datasets',
            'method': 'GET',
            'resultType': 'DatasetList',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'pageToken': pageToken,
                'all': all,
                'maxResults': maxResults,
                'projectId': urlibQuoteEncode(projectId, safe=''),
            },
            'httpBodyParams': {
            },
        }
        return self._request(queryParams)

    def update(self, projectId, datasetId, datasetId_, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, description=None, projectId_=None, access=None, friendlyName=None):
        '''Updates information in an existing dataset. The update method replaces the entire dataset resource, whereas the patch method only replaces fields that are provided in the submitted dataset resource.'''
        queryParams = {
            'url': 'https://www.googleapis.com/bigquery/v2/projects/{projectId}/datasets/{datasetId}',
            'method': 'PUT',
            'resultType': 'Dataset',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'projectId': urlibQuoteEncode(projectId, safe=''),
                'datasetId': urlibQuoteEncode(datasetId, safe=''),
            },
            'httpBodyParams': {
                'access': access,
                'friendlyName': friendlyName,
                'description': description,
                'datasetReference': {
                    'projectId': projectId_,
                    'datasetId': datasetId_,
                },
            },
        }
        return self._request(queryParams)

    def patch(self, projectId, datasetId, datasetId_, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, description=None, projectId_=None, access=None, friendlyName=None):
        '''Updates information in an existing dataset. The update method replaces the entire dataset resource, whereas the patch method only replaces fields that are provided in the submitted dataset resource. This method supports patch semantics.'''
        queryParams = {
            'url': 'https://www.googleapis.com/bigquery/v2/projects/{projectId}/datasets/{datasetId}',
            'method': 'PATCH',
            'resultType': 'Dataset',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'projectId': urlibQuoteEncode(projectId, safe=''),
                'datasetId': urlibQuoteEncode(datasetId, safe=''),
            },
            'httpBodyParams': {
                'access': access,
                'friendlyName': friendlyName,
                'description': description,
                'datasetReference': {
                    'projectId': projectId_,
                    'datasetId': datasetId_,
                },
            },
        }
        return self._request(queryParams)

    def delete(self, datasetId, projectId, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, deleteContents=None):
        '''Deletes the dataset specified by the datasetId value. Before you can delete a dataset, you must delete all its tables, either manually or by specifying deleteContents. Immediately after deletion, you can create another dataset with the same name.'''
        queryParams = {
            'url': 'https://www.googleapis.com/bigquery/v2/projects/{projectId}/datasets/{datasetId}',
            'method': 'DELETE',
            'resultType': 'empty',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'deleteContents': deleteContents,
                'datasetId': urlibQuoteEncode(datasetId, safe=''),
                'projectId': urlibQuoteEncode(projectId, safe=''),
            },
            'httpBodyParams': {
            },
        }
        return self._request(queryParams)


class Jobs(GoogleResource):
    def __init__(self, service, conn, *args, **kwargs):
        super(Jobs, self).__init__(service, conn, *args, **kwargs)

    def insert(self, projectId, load_destinationTable_projectId, tableId, datasetId, link_destinationTable_projectId, link_destinationTable_tableId, link_destinationTable_datasetId, copy_destinationTable_projectId, copy_destinationTable_tableId, copy_destinationTable_datasetId, extract_sourceTable_projectId, extract_sourceTable_tableId, extract_sourceTable_datasetId, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, projectId_=None, jobId=None, quote=None, encoding=None, fieldDelimiter=None, sourceFormat=None, maxBadRecords=None, allowJaggedRows=None, writeDisposition=None, sourceUris=None, skipLeadingRows=None, createDisposition=None, schemaInlineFormat=None, schemaInline=None, allowQuotedNewlines=None, ignoreUnknownValues=None, schema_fields=None, dryRun=None, createDisposition_=None, writeDisposition_=None, sourceUri=None, flattenResults=None, useQueryCache=None, projectIdQuery=None, datasetIdQuery=None, query_destinationTable_projectId=None, query_destinationTable_tableId=None, query_destinationTable_datasetId=None, priority=None, query_writeDisposition=None, allowLargeResults=None, query_createDisposition=None, query=None, preserveNulls=None, copy_createDisposition=None, sourceTables=None, copy_writeDisposition=None, copy_sourceTable_projectId=None, copy_sourceTable_tableId=None, copy_sourceTable_datasetId=None, destinationUri=None, compression=None, fieldDelimiter_=None, destinationFormat=None, printHeader=None, destinationUris=None):
        '''Starts a new asynchronous job.'''
        queryParams = {
            'url': 'https://www.googleapis.com/bigquery/v2/projects/{projectId}/jobs',
            'method': 'POST',
            'resultType': 'Job',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'projectId': urlibQuoteEncode(projectId, safe=''),
            },
            'httpBodyParams': {
                'configuration': {
                    'load': {
                        'encoding': encoding,
                        'skipLeadingRows': skipLeadingRows,
                        'quote': quote,
                        'sourceFormat': sourceFormat,
                        'destinationTable': {
                            'projectId': load_destinationTable_projectId,
                            'tableId': tableId,
                            'datasetId': datasetId,
                        },
                        'maxBadRecords': maxBadRecords,
                        'allowJaggedRows': allowJaggedRows,
                        'writeDisposition': writeDisposition,
                        'sourceUris': sourceUris,
                        'fieldDelimiter': fieldDelimiter,
                        'createDisposition': createDisposition,
                        'schemaInlineFormat': schemaInlineFormat,
                        'schemaInline': schemaInline,
                        'allowQuotedNewlines': allowQuotedNewlines,
                        'ignoreUnknownValues': ignoreUnknownValues,
                        'schema': {
                            'fields': schema_fields,
                        },
                    },
                    'dryRun': dryRun,
                    'link': {
                        'createDisposition': createDisposition_,
                        'writeDisposition': writeDisposition_,
                        'destinationTable': {
                            'projectId': link_destinationTable_projectId,
                            'tableId': link_destinationTable_tableId,
                            'datasetId': link_destinationTable_datasetId,
                        },
                        'sourceUri': sourceUri,
                    },
                    'query': {
                        'flattenResults': flattenResults,
                        'useQueryCache': useQueryCache,
                        'defaultDataset': {
                            'projectId': projectIdQuery,
                            'datasetId': datasetIdQuery,
                        },
                        'destinationTable': {
                            'projectId': query_destinationTable_projectId,
                            'tableId': query_destinationTable_tableId,
                            'datasetId': query_destinationTable_datasetId,
                        },
                        'priority': priority,
                        'writeDisposition': query_writeDisposition,
                        'allowLargeResults': allowLargeResults,
                        'createDisposition': query_createDisposition,
                        'query': query,
                        'preserveNulls': preserveNulls,
                    },
                    'copy': {
                        'createDisposition': copy_createDisposition,
                        'sourceTables': sourceTables,
                        'writeDisposition': copy_writeDisposition,
                        'destinationTable': {
                            'projectId': copy_destinationTable_projectId,
                            'tableId': copy_destinationTable_tableId,
                            'datasetId': copy_destinationTable_datasetId,
                        },
                        'sourceTable': {
                            'projectId': copy_sourceTable_projectId,
                            'tableId': copy_sourceTable_tableId,
                            'datasetId': copy_sourceTable_datasetId,
                        },
                    },
                    'extract': {
                        'destinationUri': destinationUri,
                        'compression': compression,
                        'fieldDelimiter': fieldDelimiter_,
                        'destinationFormat': destinationFormat,
                        'printHeader': printHeader,
                        'destinationUris': destinationUris,
                        'sourceTable': {
                            'projectId': extract_sourceTable_projectId,
                            'tableId': extract_sourceTable_tableId,
                            'datasetId': extract_sourceTable_datasetId,
                        },
                    },
                },
                'jobReference': {
                    'projectId': projectId_,
                    'jobId': jobId,
                },
            },
        }
        return self._request(queryParams)

    def query(self, projectId, query, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, timeoutMs=None, kind=None, dryRun=None, useQueryCache=None, projectId_=None, datasetId=None, maxResults=None, preserveNulls=None):
        '''Runs a BigQuery SQL query synchronously and returns query results if the query completes within a specified timeout.'''
        queryParams = {
            'url': 'https://www.googleapis.com/bigquery/v2/projects/{projectId}/queries',
            'method': 'POST',
            'resultType': 'QueryResponse',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'projectId': urlibQuoteEncode(projectId, safe=''),
            },
            'httpBodyParams': {
                'timeoutMs': timeoutMs,
                'kind': kind,
                'dryRun': dryRun,
                'useQueryCache': useQueryCache,
                'defaultDataset': {
                    'projectId': projectId_,
                    'datasetId': datasetId,
                },
                'maxResults': maxResults,
                'query': query,
                'preserveNulls': preserveNulls,
            },
        }
        return self._request(queryParams)

    def list(self, projectId, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, projection=None, stateFilter=None, allUsers=None, maxResults=None, pageToken=None):
        '''Lists all the Jobs in the specified project that were started by the user. The job list returns in reverse chronological order of when the jobs were created, starting with the most recent job created.'''
        queryParams = {
            'url': 'https://www.googleapis.com/bigquery/v2/projects/{projectId}/jobs',
            'method': 'GET',
            'resultType': 'JobList',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'projection': projection,
                'stateFilter': stateFilter,
                'projectId': urlibQuoteEncode(projectId, safe=''),
                'allUsers': allUsers,
                'maxResults': maxResults,
                'pageToken': pageToken,
            },
            'httpBodyParams': {
            },
        }
        return self._request(queryParams)

    def getQueryResults(self, projectId, jobId, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, timeoutMs=None, maxResults=None, pageToken=None, startIndex=None):
        '''Retrieves the results of a query job.'''
        queryParams = {
            'url': 'https://www.googleapis.com/bigquery/v2/projects/{projectId}/queries/{jobId}',
            'method': 'GET',
            'resultType': 'GetQueryResultsResponse',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'timeoutMs': timeoutMs,
                'projectId': urlibQuoteEncode(projectId, safe=''),
                'maxResults': maxResults,
                'jobId': urlibQuoteEncode(jobId, safe=''),
                'pageToken': pageToken,
                'startIndex': startIndex,
            },
            'httpBodyParams': {
            },
        }
        return self._request(queryParams)

    def get(self, projectId, jobId, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None):
        '''Retrieves the specified job by ID.'''
        queryParams = {
            'url': 'https://www.googleapis.com/bigquery/v2/projects/{projectId}/jobs/{jobId}',
            'method': 'GET',
            'resultType': 'Job',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'projectId': urlibQuoteEncode(projectId, safe=''),
                'jobId': urlibQuoteEncode(jobId, safe=''),
            },
            'httpBodyParams': {
            },
        }
        return self._request(queryParams)


class Tabledata(GoogleResource):
    def __init__(self, service, conn, *args, **kwargs):
        super(Tabledata, self).__init__(service, conn, *args, **kwargs)

    def list(self, projectId, tableId, datasetId, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, maxResults=None, pageToken=None, startIndex=None):
        '''Retrieves table data from a specified set of rows.'''
        queryParams = {
            'url': 'https://www.googleapis.com/bigquery/v2/projects/{projectId}/datasets/{datasetId}/tables/{tableId}/data',
            'method': 'GET',
            'resultType': 'TableDataList',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'projectId': urlibQuoteEncode(projectId, safe=''),
                'maxResults': maxResults,
                'pageToken': pageToken,
                'startIndex': startIndex,
                'tableId': urlibQuoteEncode(tableId, safe=''),
                'datasetId': urlibQuoteEncode(datasetId, safe=''),
            },
            'httpBodyParams': {
            },
        }
        return self._request(queryParams)

    def insertAll(self, projectId, tableId, datasetId, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, kind=None, rows=None):
        '''Streams data into BigQuery one record at a time without needing to run a load job.'''
        queryParams = {
            'url': 'https://www.googleapis.com/bigquery/v2/projects/{projectId}/datasets/{datasetId}/tables/{tableId}/insertAll',
            'method': 'POST',
            'resultType': 'TableDataInsertAllResponse',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'projectId': urlibQuoteEncode(projectId, safe=''),
                'tableId': urlibQuoteEncode(tableId, safe=''),
                'datasetId': urlibQuoteEncode(datasetId, safe=''),
            },
            'httpBodyParams': {
                'kind': kind,
                'rows': rows,
            },
        }
        return self._request(queryParams)


class Projects(GoogleResource):
    def __init__(self, service, conn, *args, **kwargs):
        super(Projects, self).__init__(service, conn, *args, **kwargs)

    def list(self, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, pageToken=None, maxResults=None):
        '''Lists the projects to which you have at least read access.'''
        queryParams = {
            'url': 'https://www.googleapis.com/bigquery/v2/projects',
            'method': 'GET',
            'resultType': 'ProjectList',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'pageToken': pageToken,
                'maxResults': maxResults,
            },
            'httpBodyParams': {
            },
        }
        return self._request(queryParams)


class Bigquery(GoogleService):
    '''A data platform for customers to create, manage, share and query data.'''
    _DEFAULT_SCOPES = [u'https://www.googleapis.com/auth/devstorage.full_control', u'https://www.googleapis.com/auth/devstorage.read_only', u'https://www.googleapis.com/auth/devstorage.read_write', u'https://www.googleapis.com/auth/cloud-platform', u'https://www.googleapis.com/auth/bigquery.insertdata', u'https://www.googleapis.com/auth/bigquery']

    def __init__(self, conn=None, scopes=None, *args, **kwargs):
        if scopes is not None:
            self._scopes = scopes
        else:
            self._scopes = self._DEFAULT_SCOPES
        conn.registerScopes(self._scopes)
        super(Bigquery, self).__init__(conn, *args, **kwargs)
        self.tables = Tables(self, conn, *args, **kwargs)
        self.datasets = Datasets(self, conn, *args, **kwargs)
        self.jobs = Jobs(self, conn, *args, **kwargs)
        self.tabledata = Tabledata(self, conn, *args, **kwargs)
        self.projects = Projects(self, conn, *args, **kwargs)
