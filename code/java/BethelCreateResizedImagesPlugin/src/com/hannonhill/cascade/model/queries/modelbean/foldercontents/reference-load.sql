SELECT  e.id, e.name, e.cachePath, e.relativeOrder, e.permissionsId, 
    e.isWorkingCopy, e.isCurrentVersion, 
    e.workflowId,
    m.createdBy, m.creationDate, m.lastModifiedBy, m.lastModifiedDate
FROM cxml_reference e
LEFT JOIN cxml_entitymetadata m ON e.metadataId = m.id
WHERE
e.parentFolderId = 'FOLDERID'
AND
e.isCurrentVersion = 1
AND
e.isWorkingCopy = 0

