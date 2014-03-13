SELECT  e.id, e.name, e.cachePath, e.relativeOrder, e.permissionsId, 
    e.displayName, e.title, e.summary, e.author, e.teaser, e.keywords, e.metaDescription, e.startDate, e.endDate,
    e.isWorkingCopy, e.isCurrentVersion, 
    e.workflowId,
    m.createdBy, m.creationDate, m.lastModifiedBy, m.lastModifiedDate,
    e.parentFolderId,
    e.link,
    w.isInitialized, w.isCompleted,
    df.definitionId, df.metadataValue,
    dfd.name, dfd.metadataType, dfd.required, dfd.configuration, e.metadataSetId, dfd.visibility
FROM cxml_symlink e
LEFT JOIN cxml_entitymetadata m ON e.metadataId = m.id
LEFT JOIN cxml_workflow w ON e.workflowId = w.id
LEFT JOIN cxml_dynamicmetadatafield df on e.id = df.symlinkId
LEFT JOIN cxml_dynamicmetadatafielddef dfd on df.definitionId = dfd.id
WHERE
ASSETQUALIFIER
