SELECT  e.id, e.name, e.cachePath, e.relativeOrder, e.permissionsId, 
    e.displayName, e.title, e.summary, e.author, e.teaser, e.keywords, e.metaDescription, e.startDate, e.endDate,
    e.isWorkingCopy, e.isCurrentVersion, 
    e.workflowId,
    e.shouldBePublished, e.shouldBeIndexed, e.lastDatePublished, e.lastPublishedBy,
    m.createdBy, m.creationDate, m.lastModifiedBy, m.lastModifiedDate
FROM cxml_folder e
LEFT JOIN cxml_entitymetadata m ON e.metadataId = m.id
WHERE
e.parentFolderId = 'FOLDERID'
AND
e.isCurrentVersion = 1
AND
e.isWorkingCopy = 0

