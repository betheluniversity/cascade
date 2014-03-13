select
	e.id, 
	e.name, 
	e.structuredDatatype, 
	e.ownerEntityId,
	
	e.structuredDataId,
	e.groupStructuredDataId,
	
	e.textData, 
	e.textVersion, 
	
	e.blockId, 
	b.cachePath,
	
	e.fileId, 
	f.cachePath,
	
	e.pageId,
	p.cachePath,
	
	e.symlinkId, 
	s.cachePath,
	
	e.assetType
	
from cxml_structureddata e

left join cxml_block b on e.blockId = b.id
left join cxml_file f on e.fileId = f.id
left join cxml_page p on e.pageId = p.id
left join cxml_symlink s on e.symlinkId = s.id

where e.ownerEntityId = ?
