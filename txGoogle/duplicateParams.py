'''
Created on 20 aug. 2014

@author: koos
'''
duplicateDict = {
    'bigquery:v2:bigquery.tables.insert:schema_fields': 'schema_fields',
    'bigquery:v2:bigquery.tables.insert:tableReference_projectId': 'projectId',
    #'bigquery:v2:bigquery.tables.insert:tableReference_datasetId': 'datasetId_',
    'bigquery:v2:bigquery.tables.update:schema_fields': 'schema_fields',
    'bigquery:v2:bigquery.tables.update:tableReference_projectId': 'projectId_',
    'bigquery:v2:bigquery.tables.update:tableReference_tableId': 'tableId_',
    'bigquery:v2:bigquery.tables.update:tableReference_datasetId': 'datasetId_',
    'bigquery:v2:bigquery.tables.patch:schema_fields': 'schema_fields',
    'bigquery:v2:bigquery.tables.patch:tableReference_projectId': 'projectId_',
    'bigquery:v2:bigquery.tables.patch:tableReference_tableId': 'tableId_',
    'bigquery:v2:bigquery.tables.patch:tableReference_datasetId': 'datasetId_',
    'bigquery:v2:bigquery.datasets.insert:datasetReference_projectId': 'projectId_',
    'bigquery:v2:bigquery.datasets.update:datasetReference_projectId': 'projectId_',
    'bigquery:v2:bigquery.datasets.update:datasetReference_datasetId': 'datasetId_',
    'bigquery:v2:bigquery.datasets.patch:datasetReference_projectId': 'projectId_',
    'bigquery:v2:bigquery.datasets.patch:datasetReference_datasetId': 'datasetId_',
    'bigquery:v2:bigquery.jobs.insert:statistics_query_totalBytesProcessed': 'totalBytesProcessed_',
    'bigquery:v2:bigquery.jobs.insert:jobReference_projectId': 'projectId_',
    'bigquery:v2:bigquery.jobs.insert:configuration_load_destinationTable_projectId': 'load_destinationTable_projectId',
    'bigquery:v2:bigquery.jobs.insert:configuration_load_schema_fields': 'schema_fields',
    'bigquery:v2:bigquery.jobs.insert:configuration_link_createDisposition': 'createDisposition_',
    'bigquery:v2:bigquery.jobs.insert:configuration_link_writeDisposition': 'writeDisposition_',
    'bigquery:v2:bigquery.jobs.insert:configuration_link_destinationTable_projectId': 'link_destinationTable_projectId',
    'bigquery:v2:bigquery.jobs.insert:configuration_link_destinationTable_tableId': 'link_destinationTable_tableId',
    'bigquery:v2:bigquery.jobs.insert:configuration_link_destinationTable_datasetId': 'link_destinationTable_datasetId',
    'bigquery:v2:bigquery.jobs.insert:configuration_query_defaultDataset_projectId': 'projectIdQuery',
    'bigquery:v2:bigquery.jobs.insert:configuration_query_defaultDataset_datasetId': 'datasetIdQuery',
    'bigquery:v2:bigquery.jobs.insert:configuration_query_destinationTable_projectId': 'query_destinationTable_projectId',
    'bigquery:v2:bigquery.jobs.insert:configuration_query_destinationTable_tableId': 'query_destinationTable_tableId',
    'bigquery:v2:bigquery.jobs.insert:configuration_query_destinationTable_datasetId': 'query_destinationTable_datasetId',
    'bigquery:v2:bigquery.jobs.insert:configuration_query_writeDisposition': 'query_writeDisposition',
    'bigquery:v2:bigquery.jobs.insert:configuration_query_createDisposition': 'query_createDisposition',
    'bigquery:v2:bigquery.jobs.insert:configuration_copy_createDisposition': 'copy_createDisposition',
    'bigquery:v2:bigquery.jobs.insert:configuration_copy_writeDisposition': 'copy_writeDisposition',
    'bigquery:v2:bigquery.jobs.insert:configuration_copy_destinationTable_projectId': 'copy_destinationTable_projectId',
    'bigquery:v2:bigquery.jobs.insert:configuration_copy_destinationTable_tableId': 'copy_destinationTable_tableId',
    'bigquery:v2:bigquery.jobs.insert:configuration_copy_destinationTable_datasetId': 'copy_destinationTable_datasetId',
    'bigquery:v2:bigquery.jobs.insert:configuration_copy_sourceTable_projectId': 'copy_sourceTable_projectId',
    'bigquery:v2:bigquery.jobs.insert:configuration_copy_sourceTable_tableId': 'copy_sourceTable_tableId',
    'bigquery:v2:bigquery.jobs.insert:configuration_copy_sourceTable_datasetId': 'copy_sourceTable_datasetId',
    'bigquery:v2:bigquery.jobs.insert:configuration_extract_fieldDelimiter': 'fieldDelimiter_',
    'bigquery:v2:bigquery.jobs.insert:configuration_extract_sourceTable_projectId': 'extract_sourceTable_projectId',
    'bigquery:v2:bigquery.jobs.insert:configuration_extract_sourceTable_tableId': 'extract_sourceTable_tableId',
    'bigquery:v2:bigquery.jobs.insert:configuration_extract_sourceTable_datasetId': 'extract_sourceTable_datasetId',
    'bigquery:v2:bigquery.jobs.query:defaultDataset_projectId': 'projectId_',
    'datastore:v1beta2:datastore.datasets.runQuery:query_filter_propertyFilter_operator': 'operator_',
    'datastore:v1beta2:datastore.datasets.runQuery:query_filter_propertyFilter_value_entityValue_key': 'key_',
    'datastore:v1beta2:datastore.datasets.runQuery:query_filter_propertyFilter_value_entityValue_key_partitionId_datasetId': 'key_partitionId_datasetId',
    'datastore:v1beta2:datastore.datasets.runQuery:query_filter_propertyFilter_value_keyValue_path': 'path_',
    'datastore:v1beta2:datastore.datasets.runQuery:query_filter_propertyFilter_value_keyValue_partitionId_namespace': 'partitionId_namespace',
    'datastore:v1beta2:datastore.datasets.runQuery:query_filter_propertyFilter_value_keyValue_partitionId_datasetId': 'partitionId_datasetId',
    'datastore:v1beta2:datastore.datasets.runQuery:partitionId_namespace': 'namespace_',
    'datastore:v1beta2:datastore.datasets.runQuery:partitionId_datasetId': 'datasetId_',
    'gmail:v1:gmail.users.labels.update:id': 'id_',
    'gmail:v1:gmail.users.labels.patch:id': 'id_',
    'gmail:v1:gmail.users.drafts.create:id': 'id_',
    'gmail:v1:gmail.users.drafts.update:message_id': 'id_',
    'gmail:v1:gmail.users.drafts.update:id': 'updateId',
    'gmail:v1:gmail.users.drafts.send:id': 'id_',
    'storage:v1:storage.defaultObjectAccessControls.insert:bucket': 'bucket',
    'storage:v1:storage.defaultObjectAccessControls.update:bucket': 'bucket',
    'storage:v1:storage.defaultObjectAccessControls.update:entity': 'entity',
    'storage:v1:storage.defaultObjectAccessControls.patch:bucket': 'bucket',
    'storage:v1:storage.defaultObjectAccessControls.patch:entity': 'entity',
    'storage:v1:storage.bucketAccessControls.insert:bucket': 'bucket',
    'storage:v1:storage.bucketAccessControls.update:bucket': 'bucket',
    'storage:v1:storage.bucketAccessControls.update:entity': 'entity',
    'storage:v1:storage.bucketAccessControls.patch:bucket': 'bucket',
    'storage:v1:storage.bucketAccessControls.patch:entity': 'entity',
    'storage:v1:storage.objects.insert:name': 'name',
    'storage:v1:storage.objects.insert:bucket': 'bucket',
    'storage:v1:storage.objects.insert:contentEncoding': 'contentEncoding',
    'storage:v1:storage.objects.compose:destination_kind': 'destination_kind',
    'storage:v1:storage.objects.update:generation': 'generation',
    'storage:v1:storage.objects.update:bucket': 'bucket',
    'storage:v1:storage.objects.patch:generation': 'generation',
    'storage:v1:storage.objects.patch:bucket': 'bucket',
    'storage:v1:storage.objectAccessControls.insert:generation': 'generation',
    'storage:v1:storage.objectAccessControls.insert:object': 'object',
    'storage:v1:storage.objectAccessControls.insert:bucket': 'bucket',
    'storage:v1:storage.objectAccessControls.update:generation': 'generation',
    'storage:v1:storage.objectAccessControls.update:object': 'object',
    'storage:v1:storage.objectAccessControls.update:bucket': 'bucket',
    'storage:v1:storage.objectAccessControls.update:entity': 'entity',
    'storage:v1:storage.objectAccessControls.patch:generation': 'generation',
    'storage:v1:storage.objectAccessControls.patch:object': 'object',
    'storage:v1:storage.objectAccessControls.patch:bucket': 'bucket',
    'storage:v1:storage.objectAccessControls.patch:entity': 'entity',
}