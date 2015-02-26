
import assets.page


BR = "<br />\n"
HR = "<hr class='thin width100 text_lightgray bg_lightgray' />"
E_H2 = "</h2>\n"
S_H2 = "<h2>"
E_LI = "</li>\n"
S_LI = "<li>\n"
E_PRE = "</pre>\n"
S_PRE = "<pre>\n"
SPACE = "&nbsp&nbsp&nbsp&nbsp"
E_STRONG = "</strong>\n"
S_STRONG = "<strong>\n"
E_UL = "</ul>\n"
S_UL = "<ul>\n"
S_SPAN = "<span style='color:redfont-weight:bold'>"
E_SPAN = "</span>"


class F():

    ASSOCIATE_WITH_METADATA_SET = 'assetTreeAssociateWithMetadataSet'
    COUNT = 'assetTreeCount'
    DISPLAY = 'assetTreeDisplay'
    GET_ASSETS = 'assetTreeGetAssets'
    PUBLISH = 'assetTreePublish'
    REMOVE_ASSET = 'assetTreeRemoveAsset'
    REPORT_DATA_DEFINITION_FLAG = 'assetTreeReportDataDefinitionFlag'
    REPORT_FACTORY_GROUP = 'assetTreeReportAssetFactoryGroupAssignment'
    REPORT_METADATA_FLAG = 'assetTreeReportMetadataFlag'
    REPORT_PAGE_LEVEL = 'assetTreeReportPageWithPageLevelBlockFormat'
    REPORT_ORPHANS = 'assetTreeReportOrphans'
    SEARCH_BY_NAME = 'assetTreeSearchByName'
    STORE_ASSET_PATH = 'assetTreeStoreAssetPath'
    SKIP_ROOT_CONTAINER = 'skip-root-container'
    UNCONDITIONAL_REMOVAL = 'unconditional-removal'


class L:

    ACTION = "Action: "
    ASSET_TYPE = "Asset type: "
    BODY = "Body: "
    CREATED_BY = "Created by: "
    CREATED_DATE = "Created date: "
    DATA = "Data: "
    DATE = "Date: "
    EXPIRATION_FOLDER_ID = "Expiration folder ID: "
    EXPIRATION_FOLDER_PATH = "Expiration folder path: "
    FROM = "From: "
    ID = "ID: "
    LAST_MODIFIED_BY = "Last modified by: "
    LAST_MODIFIED_DATE = "Last modified date: "
    LAST_PUBLISHED_BY = "Last published by: "
    LAST_PUBLISHED_DATE = "Last published date: "
    MAINTAIN_ABSOLUTE_LINKS = "Maintain absolute links: "
    METADATA_SET_ID = "Metadata set ID: "
    METADATA_SET_PATH = "Metadata set path: "
    NAME = "Name: "
    PATH = "Path: "
    PARENT_CONTAINER_ID = "Parent container ID: "
    PARENT_CONTAINER_PATH = "Parent container path: "
    PARENT_FOLDER_ID = "Parent folder ID: "
    PARENT_FOLDER_PATH = "Parent folder path: "
    PROPERTY_NAME = "Property name: "
    READ_DUMP = "Read Dump"
    REWRITE_LINKS = "Rewrite links: "
    SHOULD_BE_INDEXED = "Should be indexed: "
    SHOULD_BE_PUBLISHED = "Should be published: "
    SITE_ID = "Site ID: "
    SITE_NAME = "Site name: "
    SUBJECT = "Subject: "
    TEXT = "Text: "
    TO = "To: "
    TYPE = "Type: "
    USER = "User: "


class M:

    ACCESS_TO_USERS_GROUPS = "Access can only be granted to users and groups."
    COMMENT_NOT_STRING = "The comment should be a string. "
    COPY_ASSET_FAILURE = "Failed to copy the asset. "
    COPY_BASE_FOLDER = "Cannot copy the Base Folder. "
    CREATE_ASSET_FAILURE = "Cannot create the asset. "
    DELETE_ASSET_FAILURE = "Cannot delete the asset. "
    DIFFERENT_DATA_DEFINITIONS = "The two data definitions are different. "
    EDIT_ASSET_FAILURE = "Failed to edit the asset. "
    EDIT_WORKFLOW_SETTINGS_FAILURE = "Failed to edit the workflow settings. "
    EMPTY_ASSET_CONTENT = "The asset content cannot be empty. "
    EMPTY_ASSET_FACTORY_NAME = "The asset factory name cannot be empty. "
    EMPTY_ASSET_FACTORY_CONTAINER_NAME = "The asset factory container name cannot be empty. "
    EMPTY_ASSET_METADATA = "The asset metadata cannot be empty. "
    EMPTY_ASSET_NAME = "The asset name cannot be empty. "
    EMPTY_AUDIT = "The audit cannot be empty. "
    EMPTY_BLOCK_NAME = "The block name cannot be empty. "
    EMPTY_COMMENT = "The comment cannot be empty. "
    EMPTY_CONFIGURATION_NAME = "The configuration name cannot be empty. "
    EMPTY_CONNECTOR_NAME = "The connector name cannot be empty. "
    EMPTY_CONNECTOR_CONTAINER_NAME = "The connector container name cannot be empty. "
    EMPTY_CONTENT_TYPE_NAME = "The content type name cannot be empty. "
    EMPTY_CONTENT_TYPE_CONTAINER_NAME = "The content type container name cannot be empty. "
    EMPTY_DATABASE_NAME = "The database name cannot be empty. "
    EMPTY_DATA_DEFINITION_NAME = "The data definition name cannot be empty. "
    EMPTY_DATA_DEFINITION_CONTAINER_NAME = "The data definition container name cannot be empty. "
    EMPTY_DESTINATION_NAME = "The destination name cannot be empty. "
    EMPTY_DESTINATION_CONTAINER_NAME = "The destination container name cannot be empty. "
    EMPTY_DIRECTORY = "The directory cannot be empty. "
    EMPTY_FILE_NAME = "The file name cannot be empty. "
    EMPTY_FILE_EXTENSION = "The file extension cannot be empty. "
    EMPTY_FOLDER_NAME = "The folder name cannot be empty. "
    EMPTY_FORMAT_NAME = "The format name cannot be empty. "
    EMPTY_GROUP_NAME = "The group name cannot be empty. "
    EMPTY_HASH_TAG = "The hash tag cannot be empty. "
    EMPTY_IDENTIFIER = "The identifier cannot be empty. "
    EMPTY_METADATA_SET_NAME = "The metadata set name cannot be empty. "
    EMPTY_METADATA_SET_CONTAINER_NAME = "The metadata set container name cannot be empty. "
    EMPTY_NAME = "The name cannot be empty. "
    EMPTY_PAGE_NAME = "The page name cannot be empty. "
    EMPTY_PAGE_CONFIGURATION_NAME = "The page configuration name cannot be empty. "
    EMPTY_PAGE_CONFIGURATION_SET_NAME = "The configuration set name cannot be empty. "
    EMPTY_PAGE_CONFIGURATION_SET_CONTAINER_NAME = "The configuration set container name cannot be empty. "
    EMPTY_PASSWORD = "The password cannot be empty. "
    EMPTY_POSSIBLE_VALUES = "The possible value cannot be empty. "
    EMPTY_PREFIX = "The prefix cannot be empty. "
    EMPTY_PROFILE_ID = "The profile ID cannot be empty. "
    EMPTY_PUBLISH_SET_NAME = "The publish set name cannot be empty. "
    EMPTY_PUBLISH_SET_CONTAINER_NAME = "The publish set container name cannot be empty. "
    EMPTY_REFERENCE_NAME = "The reference name cannot be empty. "
    EMPTY_RECYCLE_BIN_EXPIRATION = "The recycle bin expiration cannot be empty. "
    EMPTY_ROLE_NAME = "The role name cannot be empty. "
    EMPTY_SCRIPT = "The script cannot be empty. "
    EMPTY_SERVER_NAME = "The server name cannot be empty. "
    EMPTY_SERVER_PORT = "The server port cannot be empty. "
    EMPTY_SITE_NAME = "The site name cannot be empty. "
    EMPTY_SITE_DESTINATION_CONTAINER_NAME = "The site destination container name cannot be empty. "
    EMPTY_SYMLINK_NAME = "The symlink name cannot be empty. "
    EMPTY_TEMPLATE_NAME = "The template name cannot be empty. "
    EMPTY_TEXT = "The text is required. "
    EMPTY_TEXT_DATA = "Either one of text, data is required. "
    EMPTY_TRANSPORT_NAME = "The transport name cannot be empty. "
    EMPTY_TRANSPORT_SITE_ID = "The transport site ID cannot be empty. "
    EMPTY_TRANSPORT_CONTAINER_NAME = "The transport container name cannot be empty. "
    EMPTY_URL = "The URL cannot be empty. "
    EMPTY_USER_NAME = "The username cannot be empty. "
    EMPTY_WORKFLOW_NAME = "The workflow name cannot be empty. "
    EMPTY_WORKFLOW_DEFINITION_CONTAINER_NAME = "The workflow definition container name cannot be empty. "
    EMPTY_XML = "The xml cannot be empty. "
    EXCEPTION_THROWN_NOT_SET = "The exception thrown value is not set. "
    GOOGLE_CONNECTOR_NO_CT = "A google analytics connector does not have content type. "
    MOVE_ASSET_FAILURE = "Failed to move/rename the asset. "
    NOT_ARRAY = "The parameter is not an array. "
    NOT_DATA_BLOCK = "The block is not a data definition block. "
    NOT_XHTML_BLOCK = "The block is not an xhmtl block. "
    NOT_DATA_DEFINITION_PAGE = "The page is not associated with a data definition. "
    NOT_XHTML_PAGE = "The page is associated with a data definition. "
    NULL_ASSET = "The asset cannot be NULL. "
    NULL_CACHE = "The cache cannot be NULL. "
    NULL_CONTAINER = "The container cannot be NULL. "
    NULL_CONTENT_TYPE = "The content type cannot be NULL. "
    NULL_FOLDER = "The folder cannot be NULL. "
    NULL_GROUP = "The group cannot be NULL. "
    NULL_IDENTIFIER = "The identifier cannot be NULL. "
    NULL_SERVICE = "The service object cannot be NULL. "
    NULL_WORKFLOW_DEFINITION = "The workflow definition cannot be NULL. "
    READ_WORKFLOW_FAILURE = "Failed to read the workflow. "
    RENAME_ASSET_FAILURE = "Failed to move/rename the asset. "
    ROOT_FOLDER_NOT_SET = "The root folder has not been set. "
    SITE_NOT_SET = "The site has not been set. "
    SOURCE_CASCADE_NOT_SET = "The source Cascade object is not set. "
    SOURCE_SITE_NOT_SET = "The source site is not set. "
    SITE_CREATION_FAILURE = "Failed to create the site. "
    SITE_NO_PARENT_CONTAINER = "Sites do not have parent containers and cannot be moved/renamed. "
    SMALLER_END_TIME = "The end time cannot be smaller than the start time. "
    TARGET_CASCADE_NOT_SET = "The target Cascade object is not set. "
    TARGET_SITE_NOT_SET = "The target site is not set. "
    TEXT_NO_POSSIBLE_VALUE = "Text field cannot have possible value. "
    WRONG_ASSET_TYPE = "The operation is not possible for this asset type. "
    WRONG_AUDIT_TYPE = "The audit type does not exists. "
    WRONG_ROLE = "The role does not exists. "


class P:

    ASSET_FACTORY = "assetFactory"
    ASSETFACTORY = "assetFactory"
    ASSET_FACTORY_CONTAINER = "assetFactoryContainer"
    ASSETFACTORYCONTAINER = "assetFactoryContainer"
    CONFIGURATION_SET = "pageConfigurationSet"
    CONFIGURATIONSET = "pageConfigurationSet"
    CONFIGURATION_SET_CONTAINER = "pageConfigurationSetContainer"
    CONFIGURATIONSETCONTAINER = "pageConfigurationSetContainer"
    CONNECTOR_CONTAINER = "connectorContainer"
    CONNECTORCONTAINER = "connectorContainer"
    CONTENT_TYPE = "contentType"
    CONTENTTYPE = "contentType"
    CONTENT_TYPE_CONTAINER = "contentTypeContainer"
    CONTENTTYPECONTAINER = "contentTypeContainer"
    DATA_DEFINITION = "dataDefinition"
    DATADEFINITION = "dataDefinition"
    DATA_DEFINITION_BLOCK = "xhtmlDataDefinitionBlock"
    DATADEFINITIONBLOCK = "xhtmlDataDefinitionBlock"
    DATA_DEFINITION_CONTAINER = "dataDefinitionContainer"
    DATADEFINITIONCONTAINER = "dataDefinitionContainer"
    DATABASE_TRANSPORT = "databaseTransport"
    DATABASETRANSPORT = "databaseTransport"
    DATA_BLOCK = "xhtmlDataDefinitionBlock"
    DATABLOCK = "xhtmlDataDefinitionBlock"
    DESTINATION = "destination"
    FACEBOOK_CONNECTOR = "facebookConnector"
    FACEBOOKCONNECTOR = "facebookConnector"
    FEED_BLOCK = "feedBlock"
    FEEDBLOCK = "feedBlock"
    FILE = "file"
    FILE_SYSTEM_TRANSPORT = "fileSystemTransport"
    FILESYSTEMTRANSPORT = "fileSystemTransport"
    FOLDER = "folder"
    FTP_TRANSPORT = "ftpTransport"
    FTPTRANSPORT = "ftpTransport"
    GOOGLE_ANALYTICS_CONNECTOR = "googleAnalyticsConnector"
    GOOGLEANALYTICSCONNECTOR = "googleAnalyticsConnector"
    GROUP = "group"
    INDEX_BLOCK = "indexBlock"
    INDEXBLOCK = "indexBlock"
    METADATA_SET = "metadataSet"
    METADATASET = "metadataSet"
    METADATA_SET_CONTAINER = "metadataSetContainer"
    METADATASETCONTAINER = "metadataSetContainer"
    PAGE = "page"
    PAGE_CONFIGURATION_SET = "pageConfigurationSet"
    PAGECONFIGURATIONSET = "pageConfigurationSet"
    PAGE_CONFIGURATION_SET_CONTAINER = "pageConfigurationSetContainer"
    PAGECONFIGURATIONSETCONTAINER = "pageConfigurationSetContainer"
    PUBLISH_SET = "publishSet"
    PUBLISHSET = "publishSet"
    PUBLISH_SET_CONTAINER = "publishSetContainer"
    PUBLISHSETCONTAINER = "publishSetContainer"
    REFERENCE = "reference"
    ROLE = "role"
    SCRIPT_FORMAT = "scriptFormat"
    SCRIPTFORMAT = "scriptFormat"
    SITE = "site"
    SITE_DESTINATION_CONTAINER = "siteDestinationContainer"
    SITEDESTINATIONCONTAINER = "siteDestinationContainer"
    SYMLINK = "symlink"
    TARGET = "target"
    TEMPLATE = "template"
    TEXT_BLOCK = "textBlock"
    TEXTBLOCK = "textBlock"
    TRANSPORT_CONTAINER = "transportContainer"
    TRANSPORTCONTAINER = "transportContainer"
    TWITTER_CONNECTOR = "twitterConnector"
    TWITTERCONNECTOR = "twitterConnector"
    USER = "user"
    VELOCITY_FORMAT = "scriptFormat"
    VELOCITYFORMAT = "scriptFormat"
    WORDPRESS_CONNECTOR = "wordPressConnector"
    WORDPRESSCONNECTOR = "wordPressConnector"
    WORKFLOW_DEFINITION = "workflowDefinition"
    WORKFLOWDEFINITION = "workflowDefinition"
    WORKFLOW_DEFINITION_CONTAINER = "workflowDefinitionContainer"
    WORKFLOWDEFINITIONCONTAINER = "workflowDefinitionContainer"
    XHTML_DATA_DEFINITION_BLOCK = "xhtmlDataDefinitionBlock"
    XHTMLDATADEFINITIONBLOCK = "xhtmlDataDefinitionBlock"
    XML_BLOCK = "xmlBlock"
    XMLBLOCK = "xmlBlock"
    XSLT_FORMAT = "xsltFormat"
    XSLTFORMAT = "xsltFormat"


class S:

    SEARCH_ASSET_FACTORIES = 'searchAssetFactories'
    SEARCHASSETFACTORIES = 'searchAssetFactories'
    SEARCH_BLOCKS = 'searchBlocks'
    SEARCHBLOCKS = 'searchBlocks'
    SEARCH_CONNECTORS = 'searchConnectors'
    SEARCHCONNECTORS = 'searchConnectors'
    SEARCH_CONTENT_TYPES = 'searchContentTypes'
    SEARCHCONTENTTYPES = 'searchContentTypes'
    SEARCH_DATA_DEFINITIONS = 'searchDataDefinitions'
    SEARCHDATADEFINITIONS = 'searchStructuredDataDefinitions'
    SEARCH_DESTINATIONS = 'searchStructuredDataDefinitions'
    SEARCHDESTINATIONS = 'searchDestinations'
    SEARCH_FILES = 'searchFiles'
    SEARCHFILES = 'searchFiles'
    SEARCH_FOLDERS = 'searchFolders'
    SEARCHFOLDERS = 'searchFolders'
    SEARCH_FORMATS = 'searchFormats'
    SEARCHFORMATS = 'searchFormats'
    SEARCH_GROUPS = 'searchGroups'
    SEARCHGROUPS = 'searchGroups'
    SEARCH_METADATA_SETS = 'searchMetadataSets'
    SEARCHMETADATASETS = 'searchMetadataSets'
    SEARCH_PAGE_CONFIGURATION_SETS = 'searchPageConfigurationSets'
    SEARCHPAGECONFIGURATIONSETS = 'searchPageConfigurationSets'
    SEARCH_PAGES = 'searchPages'
    SEARCHPAGES = 'searchPages'
    SEARCH_PUBLISH_SETS = 'searchPublishSets'
    SEARCHPUBLISHSETS = 'searchPublishSets'
    SEARCH_ROLES = 'searchRoles'
    SEARCHROLES = 'searchRoles'
    SEARCH_SITES = 'searchSites'
    SEARCHSITES = 'searchSites'
    SEARCH_SYMLINKS = 'searchSymlinks'
    SEARCHSYMLINKS = 'searchSymlinks'
    SEARCH_TARGETS = 'searchTargets'
    SEARCHTARGETS = 'searchTargets'
    SEARCH_TEMPLATES = 'searchTemplates'
    SEARCHTEMPLATES = 'searchTemplates'
    SEARCH_TRANSPORTS = 'searchTransports'
    SEARCHTRANSPORTS = 'searchTransports'
    SEARCH_USERS = 'searchUsers'
    SEARCHUSERS = 'searchUsers'
    SEARCH_WORKFLOW_DEFINITIONS = 'searchWorkflowDefinitions'
    SEARCHWORKFLOWDEFINITIONS = 'searchWorkflowDefinitions'


class T(object):

    def __init__(self):
        pass

    ROOT_PATH = "/"
    CA = "bu_cascade-admin"
    ACTIVATE_VERSION = "activate_version"
    ACTIVATEVERSION = "activate_version"
    ADVANCE_WORKFLOW = "advance_workflow"
    ADVANCEWORKFLOW = "advance_workflow"
    ALL_DESTINATIONS = "all-destinations"
    ALLDESTINATIONS = "all-destinations"
    ALPHABETICAL = "alphabetical"
    ASCENDING = "ascending"
    ASSET = "asset"
    ASSET_FACTORY = "assetfactory"
    ASSETFACTORY = "assetfactory"
    ASSET_FACTORY_CONTAINER = "assetfactorycontainer"
    ASSETFACTORYCONTAINER = "assetfactorycontainer"
    AUTO_NAME = "auto-name"
    AUTONAME = "auto-name"
    BACKWARD = "backward"
    BLOCK = "block"
    BLOCK_FEED = "block_FEED"
    BLOCKFEED = "block_FEED"
    BLOCK_INDEX = "block_INDEX"
    BLOCKINDEX = "block_INDEX"
    BLOCK_TEXT = "block_TEXT"
    BLOCKTEXT = "block_TEXT"
    BLOCK_XHTML_DATADEFINITION = "block_XHTML_DATADEFINITION"
    BLOCK_XHTML_DATA_DEFINITION = "block_XHTML_DATADEFINITION"
    BLOCKXHTMLDATADEFINITION = "block_XHTML_DATADEFINITION"
    BLOCK_XML = "block_XML"
    BLOCKXML = "block_XML"
    BLOCK_TWITTER_FEED = "block_TWITTER_FEED"
    BLOCKTWITTERFEED = "block_TWITTER_FEED"
    CHECKBOX = "checkbox"
    CHECK_IN = "check_in"
    CHECKIN = "check_in"
    CHECK_OUT = "check_out"
    CHECKOUT = "check_out"
    CONFIGURATION = "pageconfiguration"
    CONFIGURATION_SET = "pageconfigurationset"
    CONFIGURATIONSET = "pageconfigurationset"
    CONFIGURATION_SET_CONTAINER = "pageconfigurationsetcontainer"
    CONFIGURATIONSETCONTAINER = "pageconfigurationsetcontainer"
    CONNECTOR_CONTAINER = "connectorcontainer"
    CONNECTORCONTAINER = "connectorcontainer"
    CONTENT_TYPE = "contenttype"
    CONTENT_TYPE_ASSET = "contenttype"
    CONTENTTYPE = "contenttype"
    CONTENTTYPEASSET = "contenttype"
    CONTENT_TYPE_INDEX = "content-type"
    CONTENTTYPEINDEX = "content-type"
    CONTENT_TYPE_CONTAINER = "contenttypecontainer"
    CONTENTTYPECONTAINER = "contenttypecontainer"
    COPY = "copy"
    CREATE = "create"
    CREATED_DATE = "created-date"
    CREATEDDATE = "created-date"
    CSS = "CSS"
    CUSTOM = "custom"
    DATA_BLOCK = "block_XHTML_DATADEFINITION"
    DATABLOCK = "block_XHTML_DATADEFINITION"
    DATADEFINITION = "datadefinition"
    DATA_DEFINITION = "datadefinition"
    DATA_DEFINITION_INLINE = "data-definition"
    DATADEFINITIONINLINE = "data-definition"
    DATA_DEFINITION_BLOCK = "block_XHTML_DATADEFINITION"
    DATADEFINITIONBLOCK = "block_XHTML_DATADEFINITION"
    DATADEFINITION_CONTAINER = "datadefinitioncontainer"
    DATA_DEFINITION_CONTAINER = "datadefinitioncontainer"
    DATADEFINITIONCONTAINER = "datadefinitioncontainer"
    DATABASE_TRANSPORT = "transport_db"
    DATABASETRANSPORT = "transport_db"
    DB_TRANSPORT = "transport_db"
    DBTRANSPORT = "transport_db"
    DELETE = "delete"
    DELETE_UNPUBLISH = "delete_unpublish"
    DELETEUNPUBLISH = "delete_unpublish"
    DESCENDING = "descending"
    DESTINATION = "destination"
    DO_NOT_PUBLISH = "do-not-publish"
    DONOTPUBLISH = "do-not-publish"
    DROP_DOWN = "dropdown"
    DROPDOWN = "dropdown"
    DYNAMIC_METADATA = "dynamic-metadata"
    DYNAMICMETADATA = "dynamic-metadata"
    EDIT = "edit"
    EMPTY = "empty"
    EXTERNAL = "symlink"
    EXTERNAL_LINK = "symlink"
    EXTERNALLINK = "symlink"
    FACEBOOK_CONNECTOR = "facebookconnector"
    FACEBOOKCONNECTOR = "facebookconnector"
    FACTORY_CONTROLLED = "factory-controlled"
    FACTORYCONTROLLED = "factory-controlled"
    FEED_BLOCK = "block_FEED"
    FEEDBLOCK = "block_FEED"
    FILE = "file"
    FIFTEEN = "15"
    FOLDER = "folder"
    FOLDER_CONTROLLED = "folder-controlled"
    FOLDERCONTROLLED = "folder-controlled"
    FOLDER_ORDER = "folder-order"
    FOLDERORDER = "folder-order"
    FORMAT = "format"
    FORMAT_XSLT = "format_XSLT"
    FORMATXSLT = "format_XSLT"
    FORMAT_SCRIPT = "format_SCRIPT"
    FORMATSCRIPT = "format_SCRIPT"
    FORWARD = "forward"
    FRIDAY = "Friday"
    FS_TRANSPORT = "transport_fs"
    FSTRANSPORT = "transport_fs"
    FTP_TRANSPORT = "transport_ftp"
    FTPTRANSPORT = "transport_ftp"
    GLOBAL = "global"
    GOOGLE_ANALYTICS_CONNECTOR = "googleanalyticsconnector"
    GOOGLEANALYTICSCONNECTOR = "googleanalyticsconnector"
    GROUP = "group"
    HIDDEN = "hidden"
    HIERARCHY = "hierarchy"
    HIERARCHY_WITH_SIBLINGS = "hierarchy-with-siblings"
    HIERARCHYWITHSIBLINGS = "hierarchy-with-siblings"
    HIERARCHY_SIBLINGS_FORWARD = "hierarchy-siblings_forward"
    HIERARCHYSIBLINGSFORWARD = "hierarchy-siblings_forward"
    HTML = "HTML"
    INDEX_BLOCK = "block_INDEX"
    INDEXBLOCK = "block_INDEX"
    INLINE = "inline"
    INLINE_DATA_DEFINITION = "data-definition"
    INLINEDATADEFINITION = "data-definition"
    JS = "JS"
    JSON = "JSON"
    LAST_MODIFIED_DATE = "last-modified-date"
    LASTMODIFIEDDATE = "last-modified-date"
    LDAP = "ldap"
    LINKABLE = "page,file,symlink"
    LOG_IN = "login"
    LOGIN = "login"
    LOGIN_FAILED = "login_failed"
    LOGINFAILED = "login_failed"
    LOG_OUT = "logout"
    LOGOUT = "logout"
    MATCH_ALL = "match-all"
    MATCHALL = "match-all"
    MATCH_ANY = "match-any"
    MATCHANY = "match-any"
    MESSAGE = "message"
    METADATA_SET = "metadataset"
    METADATASET = "metadataset"
    METADATASET_CONTAINER = "metadatasetcontainer"
    METADATA_SET_CONTAINER = "metadatasetcontainer"
    METADATASETCONTAINER = "metadatasetcontainer"
    MONDAY = "Monday"
    MOVE = "move"
    MULTI_SELECT = "multiselect"
    MULTISELECT = "multiselect"
    NAME_OF_DEFINITION = "name-of-definition"
    NAMEOFDEFINITION = "name-of-definition"
    NEVER = "never"
    NO_RENDER = "no-render"
    NORENDER = "no-render"
    NONE = "none"
    NORMAL = "normal"
    ONE = "1"
    PAGE = "page"
    PAGE_CONFIGURATION = "pageconfiguration"
    PAGECONFIGURATION = "pageconfiguration"
    PAGE_CONFIGURATION_SET = "pageconfigurationset"
    PAGECONFIGURATIONSET = "pageconfigurationset"
    PAGE_CONFIGURATION_SET_CONTAINER = "pageconfigurationsetcontainer"
    PAGECONFIGURATIONSETCONTAINER = "pageconfigurationsetcontainer"
    PAGE_FILE_SYMLINK = "page,file,symlink"
    PAGEFILESYMLINK = "page,file,symlink"
    PAGE_REGION = "pageregion"
    PAGEREGION = "pageregion"
    PDF = "PDF"
    PFS = "page,file,symlink"
    PUBLISH = "publish"
    PUBLISH_SET = "publishset"
    PUBLISHSET = "publishset"
    PUBLISH_SET_CONTAINER = "publishsetcontainer"
    PUBLISHSETCONTAINER = "publishsetcontainer"
    RADIO = "radio"
    READ = "read"
    RECYCLE = "recycle"
    REFERENCE = "reference"
    RENDER = "render"
    RENDER_CURRENT_PAGE_ONLY = "render-current-page-only"
    RENDERCURRENTPAGEONLY = "render-current-page-only"
    RENDER_NORMALLY = "render-normally"
    RENDERNORMALLY = "render-normally"
    RESTORE = "restore"
    ROLE = "role"
    RTF = "RTF"
    SATURDAY = "Saturday"
    SEARCH_TERMS = "search-terms"
    SEARCHTERMS = "search-terms"
    SCRIPT_FORMAT = "format_SCRIPT"
    SCRIPTFORMAT = "format_SCRIPT"
    SELECTED_DESTINATIONS = "selected-destinations"
    SELECTEDDESTINATIONS = "selected-destinations"
    SITE = "site"
    SITE_DESTINATION_CONTAINER = "sitedestinationcontainer"
    SITEDESTINATIONCONTAINER = "sitedestinationcontainer"
    SOURCE = "source"
    START_WORKFLOW = "start_workflow"
    STARTWORKFLOW = "start_workflow"
    SUNDAY = "Sunday"
    SYMLINK = "symlink"
    TARGET = "target"
    TEMPLATE = "template"
    TEXT_BLOCK = "block_TEXT"
    TEXTBLOCK = "block_TEXT"
    TEXT = "text"
    THIRTY = "30"
    THURSDAY = "Thursday"
    TRANSPORT = "transport"
    TRANSPORT_DB = "transport_db"
    TRANSPORTDB = "transport_db"
    TRANSPORT_FS = "transport_fs"
    TRANSPORTFS = "transport_fs"
    TRANSPORT_FTP = "transport_ftp"
    TRANSPORTFTP = "transport_ftp"
    TRANSPORT_CONTAINER = "transportcontainer"
    TRANSPORTCONTAINER = "transportcontainer"
    TUESDAY = "Tuesday"
    TWITTER_CONNECTOR = 'twitterconnector'
    TWITTERCONNECTOR = 'twitterconnector'
    UN_PUBLISH = "unpublish"
    UNPUBLISH = "unpublish"
    UN_READ = "unread"
    UNREAD = "unread"
    USER = "user"
    USER_AND_MENTIONS = "user-and-mentions"
    USERANDMENTIONS = "user-and-mentions"
    USER_ONLY = "user-only"
    USERONLY = "user-only"
    VELOCITY_FORMAT = "format_SCRIPT"
    VELOCITYFORMAT = "format_SCRIPT"
    VISIBLE = "visible"
    WEDNESDAY = "Wednesday"
    WIRED_METADATA = "wired-metadata"
    WIREDMETADATA = "wired-metadata"
    WML = "WML"
    WORDPRESS_CONNECTOR = "wordpressconnector"
    WORDPRESSCONNECTOR = "wordpressconnector"
    WORKFLOW = 'workflow'
    WORKFLOW_DEFINITION = "workflowdefinition"
    WORKFLOWDEFINITION = "workflowdefinition"
    WORKFLOW_DEFINITION_CONTAINER = "workflowdefinitioncontainer"
    WORKFLOWDEFINITIONCONTAINER = "workflowdefinitioncontainer"
    WRITE = "write"
    XHTML = "xhtml"
    XHTML_DATA_DEFINITION_BLOCK = "block_XHTML_DATADEFINITION"
    XHTMLDATADEFINITION_BLOCK = "block_XHTML_DATADEFINITION"
    XHTMLDATADEFINITIONBLOCK = "block_XHTML_DATADEFINITION"
    XML = "XML"
    XML_BLOCK = "block_XML"
    XMLBLOCK = "block_XML"
    XSLT_FORMAT = "format_XSLT"
    XSLTFORMAT = "format_XSLT"

    # take a constant and return a
    type_class_name_map = {
        ASSETFACTORY: 'AssetFactory',
        ASSETFACTORYCONTAINER: 'AssetFactoryContainer',
        CONNECTORCONTAINER: 'ConnectorContainer',
        CONTENTTYPE: 'ContentType',
        CONTENTTYPECONTAINER: 'ContentTypeContainer',
        DATADEFINITION: 'DataDefinition',
        DATADEFINITIONCONTAINER: 'DataDefinitionContainer',
        DESTINATION: 'Destination',
        FACEBOOKCONNECTOR: 'FacebookConnector',
        FEEDBLOCK: 'FeedBlock',
        FILE: 'File',
        FOLDER: 'Folder',
        GOOGLEANALYTICSCONNECTOR: 'GoogleAnalyticsConnector',
        GROUP: 'Group',
        INDEXBLOCK: 'IndexBlock',
        METADATASET: 'MetadataSet',
        METADATASETCONTAINER: 'MetadataSetContainer',
        PAGE: assets.page.P,
        PAGECONFIGURATIONSET: 'PageConfigurationSet',
        PAGECONFIGURATIONSETCONTAINER: 'PageConfigurationSetContainer',
        PUBLISHSET: 'PublishSet',
        PUBLISHSETCONTAINER: 'PublishSetContainer',
        REFERENCE: 'Reference',
        ROLE: 'Role',
        SCRIPTFORMAT: 'ScriptFormat',
        SITE: 'Site',
        SITEDESTINATIONCONTAINER: 'SiteDestinationContainer',
        SYMLINK: 'Symlink',
        TEMPLATE: 'Template',
        TEXTBLOCK: 'TextBlock',
        TRANSPORTDB: 'DatabaseTransport',
        TRANSPORTFS: 'FileSystemTransport',
        TRANSPORTFTP: 'FtpTransport',
        TRANSPORTCONTAINER: 'TransportContainer',
        TWITTERCONNECTOR: 'TwitterConnector',
        USER: 'User',
        WORDPRESSCONNECTOR: 'WordPressConnector',
        WORKFLOWDEFINITION: 'WorkflowDefinition',
        WORKFLOWDEFINITIONCONTAINER: 'WorkflowDefinitionContainer',
        XHTMLDATADEFINITIONBLOCK: 'DataDefinitionBlock',
        XMLBLOCK: 'XmlBlock',
        XSLTFORMAT: 'XsltFormat'
    }

    type_parent_type_map = {
        ASSETFACTORY: ASSETFACTORYCONTAINER,
        ASSETFACTORYCONTAINER: ASSETFACTORYCONTAINER,
        CONNECTORCONTAINER: CONNECTORCONTAINER,
        CONTENTTYPE: CONTENTTYPECONTAINER,
        CONTENTTYPECONTAINER: CONTENTTYPECONTAINER,
        DATADEFINITION: DATADEFINITIONCONTAINER,
        DATADEFINITIONCONTAINER: DATADEFINITIONCONTAINER,
        DESTINATION: SITEDESTINATIONCONTAINER,
        FACEBOOKCONNECTOR: CONNECTORCONTAINER,
        FEEDBLOCK: FOLDER,
        FILE: FOLDER,
        FOLDER: FOLDER,
        GOOGLEANALYTICSCONNECTOR: CONNECTORCONTAINER,
        INDEXBLOCK: FOLDER,
        METADATASET: METADATASETCONTAINER,
        METADATASETCONTAINER: METADATASETCONTAINER,
        PAGE: FOLDER,
        PAGECONFIGURATIONSET: PAGECONFIGURATIONSETCONTAINER,
        PAGECONFIGURATIONSETCONTAINER: PAGECONFIGURATIONSETCONTAINER,
        PUBLISHSET: PUBLISHSETCONTAINER,
        PUBLISHSETCONTAINER: PUBLISHSETCONTAINER,
        REFERENCE: FOLDER,
        SCRIPTFORMAT: FOLDER,
        SITEDESTINATIONCONTAINER: SITEDESTINATIONCONTAINER,
        SYMLINK: FOLDER,
        TEMPLATE: FOLDER,
        TEXTBLOCK: FOLDER,
        TRANSPORTDB: TRANSPORTCONTAINER,
        TRANSPORTFS: TRANSPORTCONTAINER,
        TRANSPORTFTP: TRANSPORTCONTAINER,
        TRANSPORTCONTAINER: TRANSPORTCONTAINER,
        TWITTERCONNECTOR: CONNECTORCONTAINER,
        WORDPRESSCONNECTOR: CONNECTORCONTAINER,
        WORKFLOWDEFINITION: WORKFLOWDEFINITIONCONTAINER,
        WORKFLOWDEFINITIONCONTAINER: WORKFLOWDEFINITIONCONTAINER,
        XHTMLDATADEFINITIONBLOCK: FOLDER,
        XMLBLOCK: FOLDER,
        XSLTFORMAT: FOLDER
    }

    type_property_name_map = {
        ASSETFACTORY: P.ASSETFACTORY,
        ASSETFACTORYCONTAINER: P.ASSETFACTORYCONTAINER,
        CONNECTORCONTAINER: P.CONNECTORCONTAINER,
        CONTENTTYPE: P.CONTENTTYPE,
        CONTENTTYPECONTAINER: P.CONTENTTYPECONTAINER,
        DATADEFINITION: P.DATADEFINITION,
        DATADEFINITIONCONTAINER: P.DATADEFINITIONCONTAINER,
        DESTINATION: P.DESTINATION,
        FACEBOOKCONNECTOR: P.FACEBOOKCONNECTOR,
        FEEDBLOCK: P.FEEDBLOCK,
        FILE: P.FILE,
        FOLDER: P.FOLDER,
        GOOGLEANALYTICSCONNECTOR: P.GOOGLEANALYTICSCONNECTOR,
        GROUP: P.GROUP,
        INDEXBLOCK: P.INDEXBLOCK,
        METADATASET: P.METADATASET,
        METADATASETCONTAINER: P.METADATASETCONTAINER,
        PAGE: P.PAGE,
        PAGECONFIGURATIONSET: P.PAGECONFIGURATIONSET,
        PAGECONFIGURATIONSETCONTAINER: P.PAGECONFIGURATIONSETCONTAINER,
        PUBLISHSET: P.PUBLISHSET,
        PUBLISHSETCONTAINER: P.PUBLISHSETCONTAINER,
        REFERENCE: P.REFERENCE,
        ROLE: P.ROLE,
        SCRIPTFORMAT: P.SCRIPTFORMAT,
        SITE: P.SITE,
        SITEDESTINATIONCONTAINER: P.SITEDESTINATIONCONTAINER,
        SYMLINK: P.SYMLINK,
        TEMPLATE: P.TEMPLATE,
        TEXTBLOCK: P.TEXTBLOCK,
        TRANSPORTDB: P.DATABASETRANSPORT,
        TRANSPORTFS: P.FILESYSTEMTRANSPORT,
        TRANSPORTFTP: P.FTPTRANSPORT,
        TRANSPORTCONTAINER: P.TRANSPORTCONTAINER,
        TWITTERCONNECTOR: P.TWITTERCONNECTOR,
        USER: P.USER,
        WORDPRESSCONNECTOR: P.WORDPRESSCONNECTOR,
        WORKFLOWDEFINITION: P.WORKFLOWDEFINITION,
        WORKFLOWDEFINITIONCONTAINER: P.WORKFLOWDEFINITIONCONTAINER,
        XHTMLDATADEFINITIONBLOCK: P.XHTMLDATADEFINITIONBLOCK,
        XMLBLOCK: P.XMLBLOCK,
        XSLTFORMAT: P.XSLTFORMAT
    }

    @staticmethod
    def get_type_array():
        return T.type_class_name_map.keys()

    @staticmethod
    def get_class_name_by_type(type):

        if type in T.type_class_name_map.keys():
            return T.type_class_name_map[type]

        return None

    @staticmethod
    def get_parent_type(type):

        if type in T.type_parent_type_map.keys():
            return T.type_parent_type_map[type]
        return None


class AuditTypes():
    pass
    # types = [
    #     LOGIN, LOGIN_FAILED, LOGOUT, START_WORKFLOW, ADVANCE_WORKFLOW,
    #     EDIT, COPY, CREATE, REFERENCE, DELETE, DELETE_UNPUBLISH,
    #     CHECK_IN, CHECK_OUT, ACTIVATE_VERSION, PUBLISH, UNPUBLISH,
    #     RECYCLE, RESTORE, MOVE, ""
    # ]

    # def isAuditType( $value )
    # {
    #     return in_array( trim( $value ), self.$types )
    # }


class BooleanValues():
    pass
    # def isBoolean( $value )
    # {
    #     return $value === true || $value === false
    # }


class LevelValues():
    pass
    # def isLevel( $level )
    # {
    #     return $level == READ || $level == WRITE || $level == NONE
    # }


class NamingBehaviorValues():
    pass
    # def isNamingBehaviorValue( $value )
    # {
    #     return $value == WorkflowDefinition.NAMING_BEHAVIOR_AUTO ||
    #     	$value == WorkflowDefinition.NAMING_BEHAVIOR_DEFINITION ||
    #     	$value == WorkflowDefinition.NAMING_BEHAVIOR_BLANK
    # }


class RecycleBinExpirationValues():
    pass
    # def isRecycleBinExpirationValue( $value )
    # {
    #     return $value == NEVER || $value == ONE || $value == FIFTEEN || $value == THIRTY
    # }


class RoleTypeValues:
    pass
    # def isRoleTypeValue( $value )
    # {
    #     return $value == SITE || $value == "global"
    # }


class SerializationTypeValues:
    pass
    # def isSerializationTypeValue( $value )
    # {
    #     return $value == HTML || $value == PDF || $value == XML || $value == RTF
    # }


class SearchTypes():
    types = [
        S.SEARCHASSETFACTORIES,
        S.SEARCHBLOCKS,
        S.SEARCHCONNECTORS,
        S.SEARCHCONTENTTYPES,
        S.SEARCHDATADEFINITIONS,
        S.SEARCHDESTINATIONS,
        S.SEARCHFILES,
        S.SEARCHFOLDERS,
        S.SEARCHFORMATS,
        S.SEARCHGROUPS,
        S.SEARCHMETADATASETS,
        S.SEARCHPAGECONFIGURATIONSETS,
        S.SEARCHPAGES,
        S.SEARCHPUBLISHSETS,
        S.SEARCHROLES,
        S.SEARCHSITES,
        S.SEARCHSYMLINKS,
        S.SEARCHTARGETS,
        S.SEARCHTEMPLATES,
        S.SEARCHTRANSPORTS,
        S.SEARCHUSERS,
        S.SEARCHWORKFLOWDEFINITIONS
    ]

    def is_search_type(self, value):
        return value.strip() in self.types


class VisibilityValues():

    def is_visibility(self, value):
        return value == T.VISIBLE or value == T.INLINE or value == T.HIDDEN


class WorkflowModeValues():

    def is_workflow_mode(self, value):
        return value == T.NONE or value == T.FACTORY_CONTROLLED or value == T.FOLDER_CONTROLLED
