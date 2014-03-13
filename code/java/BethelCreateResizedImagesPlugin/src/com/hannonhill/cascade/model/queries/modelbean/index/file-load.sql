SELECT  e.id, e.name, e.cachePath, e.relativeOrder, e.permissionsId, 
    e.displayName, e.title, e.summary, e.author, e.teaser, e.keywords, e.metaDescription, e.startDate, e.endDate,
    e.isWorkingCopy, e.isCurrentVersion, 
    e.workflowId,
    e.shouldBePublished, e.shouldBeIndexed, e.lastDatePublished, e.lastPublishedBy,
    m.createdBy, m.creationDate, m.lastModifiedBy, m.lastModifiedDate,
    e.parentFolderId,
    b.byteLength,
    w.isInitialized, w.isCompleted,
    df.definitionId, df.metadataValue,
    dfd.name, dfd.metadataType, dfd.required, dfd.configuration, e.metadataSetId, dfd.visibility
FROM cxml_file e
LEFT JOIN cxml_entitymetadata m ON e.metadataId = m.id
LEFT JOIN cxml_blob b ON e.blobId = b.id
LEFT JOIN cxml_workflow w ON e.workflowId = w.id
LEFT JOIN cxml_dynamicmetadatafield df on e.id = df.fileId
LEFT JOIN cxml_dynamicmetadatafielddef dfd on df.definitionId = dfd.id
WHERE
ASSETQUALIFIER

