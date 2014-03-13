SELECT  e.id, e.name, e.cachePath, e.relativeOrder, e.permissionsId, 
    e.displayName, e.title, e.summary, e.author, e.teaser, e.keywords, e.metaDescription, e.startDate, e.endDate,
    e.isWorkingCopy, e.isCurrentVersion, 
    e.workflowId,
    e.shouldBePublished, e.shouldBeIndexed, e.lastDatePublished, e.lastPublishedBy,
    m.createdBy, m.creationDate, m.lastModifiedBy, m.lastModifiedDate,
    e.parentFolderId,
    w.isInitialized, w.isCompleted,
    e.usesStructuredData, x.xmlData,
    df.definitionId, df.metadataValue,
    dfd.name, dfd.metadataType, dfd.required, dfd.configuration, e.metadataSetId, dfd.visibility,
    e.workingCopyId
FROM cxml_page e
LEFT JOIN cxml_entitymetadata m ON e.metadataId = m.id
LEFT JOIN cxml_xml x ON e.xmlId = x.id
LEFT JOIN cxml_workflow w ON e.workflowId = w.id
LEFT JOIN cxml_dynamicmetadatafield df ON e.id = df.pageId
LEFT JOIN cxml_dynamicmetadatafielddef dfd ON df.definitionId = dfd.id
WHERE
ASSETQUALIFIER

