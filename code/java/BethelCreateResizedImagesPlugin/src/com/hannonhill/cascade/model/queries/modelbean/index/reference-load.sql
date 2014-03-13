SELECT  e.id, e.name, e.cachePath, e.relativeOrder, e.permissionsId, 
    e.isWorkingCopy, e.isCurrentVersion, 
    e.workflowId,
    m.createdBy, m.creationDate, m.lastModifiedBy, m.lastModifiedDate,
    e.parentFolderId,
    w.isInitialized, w.isCompleted,
    
    e.blockId,
    e.fileId,
    e.folderId,
    e.pageId,
    e.stylesheetId,
    e.symlinkId,
    e.templateId
    
FROM cxml_reference e
LEFT JOIN cxml_entitymetadata m ON e.metadataId = m.id
LEFT JOIN cxml_workflow w ON e.workflowId = w.id
WHERE
ASSETQUALIFIER
