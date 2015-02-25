__author__ = 'ejc84332'

from constants import types, properties

class AssetOperationHandlerService():

    def __init__(self, url, auth):
        self.url = url
        self.auth = auth
        self.message = ""
        self.success = ""
        self.createdAssetId = ""
        self.lastRequest = ""
        self.lastResponse = ""



    #     foreach( $this->properties as $property )
    #     {
    #         // turn a property name like 'publishSet' to 'PublishSet'
    #         $property = ucwords( $property );
    #         // populate the two arrays for dynamic generation of methods
    #         // attach the prefixes 'read' and 'get'
    #         $this->read_methods[] = 'read' . $property;
    #         $this->get_methods[]  = 'get'  . $property;
    #     }
    #
    #     try
    #     {
    #         $this->soapClient = new SoapClient( $this->url, array( 'trace' => 1 ) );
    #     }
    #     catch( Exception $e )
    #     {
    #         throw new ServerException( S_SPAN . $e->getMessage() . E_SPAN );
    #     }
    # }


    # 42 properties
    # property array to generate methods
    properties = [
        properties.P.ASSETFACTORY,
        properties.P.ASSETFACTORYCONTAINER,
        properties.P.CONNECTORCONTAINER,
        properties.P.CONTENTTYPE,
        properties.P.CONTENTTYPECONTAINER,
        properties.P.DATADEFINITION,
        properties.P.DATADEFINITIONCONTAINER,
        properties.P.DATABASETRANSPORT,
        properties.P.DESTINATION,
        properties.P.FACEBOOKCONNECTOR,
        properties.P.FEEDBLOCK,
        properties.P.FILE,
        properties.P.FILESYSTEMTRANSPORT,
        properties.P.FOLDER,
        properties.P.FTPTRANSPORT,
        properties.P.GOOGLEANALYTICSCONNECTOR,
        properties.P.GROUP,
        properties.P.INDEXBLOCK,
        properties.P.METADATASET,
        properties.P.METADATASETCONTAINER,
        properties.P.PAGE,
        properties.P.PAGECONFIGURATIONSET,
        properties.P.PAGECONFIGURATIONSETCONTAINER,
        properties.P.PUBLISHSET,
        properties.P.PUBLISHSETCONTAINER,
        properties.P.REFERENCE,
        properties.P.ROLE,
        properties.P.SCRIPTFORMAT,
        properties.P.SITE,
        properties.P.SITEDESTINATIONCONTAINER,
        properties.P.SYMLINK,
        properties.P.TARGET,
        properties.P.TEMPLATE,
        properties.P.TEXTBLOCK,
        properties.P.TRANSPORTCONTAINER,
        properties.P.USER,
        properties.P.WORDPRESSCONNECTOR,
        properties.P.WORKFLOWDEFINITION,
        properties.P.WORKFLOWDEFINITIONCONTAINER,
        properties.P.XHTMLDATADEFINITIONBLOCK,
        properties.P.XMLBLOCK,
        properties.P.XSLTFORMAT
    ]

    types = [
        types.T.ASSETFACTORY,
        types.T.ASSETFACTORYCONTAINER,
        types.T.CONNECTORCONTAINER,
        types.T.CONTENTTYPE,
        types.T.CONTENTTYPECONTAINER,
        types.T.DATADEFINITION,
        types.T.DATADEFINITIONCONTAINER,
        types.T.DESTINATION,
        types.T.FACEBOOKCONNECTOR,
        types.T.FEEDBLOCK,
        types.T.FILE,
        types.T.FOLDER,
        types.T.GOOGLEANALYTICSCONNECTOR,
        types.T.GROUP,
        types.T.INDEXBLOCK,
        types.T.MESSAGE,
        types.T.METADATASET,
        types.T.METADATASETCONTAINER,
        types.T.PAGE,
        types.T.PAGECONFIGURATION,
        types.T.PAGECONFIGURATIONSET,
        types.T.PAGECONFIGURATIONSETCONTAINER,
        types.T.PAGEREGION,
        types.T.PUBLISHSET,
        types.T.PUBLISHSETCONTAINER,
        types.T.REFERENCE,
        types.T.ROLE,
        types.T.SCRIPTFORMAT,
        types.T.SITE,
        types.T.SITEDESTINATIONCONTAINER,
        types.T.SYMLINK,
        types.T.TARGET,
        types.T.TEMPLATE,
        types.T.TEXTBLOCK,
        types.T.TRANSPORTDB,
        types.T.TRANSPORTFS,
        types.T.TRANSPORTFTP,
        types.T.TRANSPORTCONTAINER,
        types.T.USER,
        types.T.WORDPRESSCONNECTOR,
        types.T.WORKFLOW,
        types.T.WORKFLOWDEFINITION,
        types.T.WORKFLOWDEFINITIONCONTAINER,
        types.T.XHTMLDATADEFINITIONBLOCK,
        types.T.XMLBLOCK,
        types.T.XSLTFORMAT
    ]
    read_methods = []
    get_methods = []
    read_assets = []