__author__ = 'ejc84332'


class AssetOperationHandlerService(object):

    def __init__(self, url, auth, t, p):
        self.url = url
        self.auth = auth
        self.message = ""
        self.success = ""
        self.createdAssetId = ""
        self.lastRequest = ""
        self.lastResponse = ""
        self.t = t
        self.p = p



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
        self.properties = [
            self.p.ASSETFACTORY,
            self.p.ASSETFACTORYCONTAINER,
            self.p.CONNECTORCONTAINER,
            self.p.CONTENTTYPE,
            self.p.CONTENTTYPECONTAINER,
            self.p.DATADEFINITION,
            self.p.DATADEFINITIONCONTAINER,
            self.p.DATABASETRANSPORT,
            self.p.DESTINATION,
            self.p.FACEBOOKCONNECTOR,
            self.p.FEEDBLOCK,
            self.p.FILE,
            self.p.FILESYSTEMTRANSPORT,
            self.p.FOLDER,
            self.p.FTPTRANSPORT,
            self.p.GOOGLEANALYTICSCONNECTOR,
            self.p.GROUP,
            self.p.INDEXBLOCK,
            self.p.METADATASET,
            self.p.METADATASETCONTAINER,
            self.p.PAGE,
            self.p.PAGECONFIGURATIONSET,
            self.p.PAGECONFIGURATIONSETCONTAINER,
            self.p.PUBLISHSET,
            self.p.PUBLISHSETCONTAINER,
            self.p.REFERENCE,
            self.p.ROLE,
            self.p.SCRIPTFORMAT,
            self.p.SITE,
            self.p.SITEDESTINATIONCONTAINER,
            self.p.SYMLINK,
            self.p.TARGET,
            self.p.TEMPLATE,
            self.p.TEXTBLOCK,
            self.p.TRANSPORTCONTAINER,
            self.p.USER,
            self.p.WORDPRESSCONNECTOR,
            self.p.WORKFLOWDEFINITION,
            self.p.WORKFLOWDEFINITIONCONTAINER,
            self.p.XHTMLDATADEFINITIONBLOCK,
            self.p.XMLBLOCK,
            self.p.XSLTFORMAT
        ]

        self.types = [
            self.t.ASSETFACTORY,
            self.t.ASSETFACTORYCONTAINER,
            self.t.CONNECTORCONTAINER,
            self.t.CONTENTTYPE,
            self.t.CONTENTTYPECONTAINER,
            self.t.DATADEFINITION,
            self.t.DATADEFINITIONCONTAINER,
            self.t.DESTINATION,
            self.t.FACEBOOKCONNECTOR,
            self.t.FEEDBLOCK,
            self.t.FILE,
            self.t.FOLDER,
            self.t.GOOGLEANALYTICSCONNECTOR,
            self.t.GROUP,
            self.t.INDEXBLOCK,
            self.t.MESSAGE,
            self.t.METADATASET,
            self.t.METADATASETCONTAINER,
            self.t.PAGE,
            self.t.PAGECONFIGURATION,
            self.t.PAGECONFIGURATIONSET,
            self.t.PAGECONFIGURATIONSETCONTAINER,
            self.t.PAGEREGION,
            self.t.PUBLISHSET,
            self.t.PUBLISHSETCONTAINER,
            self.t.REFERENCE,
            self.t.ROLE,
            self.t.SCRIPTFORMAT,
            self.t.SITE,
            self.t.SITEDESTINATIONCONTAINER,
            self.t.SYMLINK,
            self.t.TARGET,
            self.t.TEMPLATE,
            self.t.TEXTBLOCK,
            self.t.TRANSPORTDB,
            self.t.TRANSPORTFS,
            self.t.TRANSPORTFTP,
            self.t.TRANSPORTCONTAINER,
            self.t.USER,
            self.t.WORDPRESSCONNECTOR,
            self.t.WORKFLOW,
            self.t.WORKFLOWDEFINITION,
            self.t.WORKFLOWDEFINITIONCONTAINER,
            self.t.XHTMLDATADEFINITIONBLOCK,
            self.t.XMLBLOCK,
            self.t.XSLTFORMAT
        ]
        self.read_methods = []
        self.get_methods = []
        self.read_assets = []