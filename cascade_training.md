# Cascade Training

## In context editing

* Apply to the page after everything else is complete
* Properties &rarr; Content Type &rarr; Edit &rarr; Editable Fields

## Metadata & Data Definitions

* When to use Metadata vs. Data Definitions
    * Metadata sets are reusable on other pages and content types
    * If there is already an existing metadata set, don't reinvent the wheel with data definitions
    * Metadata fields are strictly text-only. If you want to use HTML or similar, you should use a data definition
    * Data definitions allow the use of **help text** which explain the usage of the data. Metadata sets do not allow this.
    * You have an XML view available when you create a new data definition, which makes it more flexible
        * Smart fields, allows you to dynamically populate new data inputs in a data definition based on a previous option
    * Common metadata sets *will* effect publishing, unlike data definitions
        * Start date & end date
            * If you fill in a start date, the page that this metadata set is configured for will not be indexed in the XML until the start date.
            * i.e. we're delaying publishing until the start date.
            * End date will expire the page at a given time.
        * Expiration folder
            * The location that an item will go once it hits the end date.
            * i.e. an archive
        * Review date
            * Date where a page will be brought up for review by an editor.

## Blocks

#### Feed Block

* YouTube/Flickr etc. RSS feeds

#### Navigation Block ([KB article](http://www.hannonhill.com/kb/Index-Block/))

* Descriptively name your index blocks so you know what it's indexing
    * e.g. "three level with parent" instead of "left-nav"
* Depth of index
    * Nothing much over 3, like not 100. Not even close to 100.
    * Limiting the depth makes sense to avoid a super ugly nav.
    * Not really going to hurt performance.
* Stuff you don't need to index for navigation blocks
    * "Other indexed information"
        * User information
        * Workflow navigation
        * Calling page data
            * Adds all information about the current page using this index block
            * `<calling-page>`
            * Contains all information about the current page in a `<system-page>` element.
            * Only needed when you're using a content-type index
            
---
#### Setup Block

* These blocks override more general blocks
    * For instance a department can have customization, such as their own logo, without changing the rest of the layout.
    * Michael thinks we should never use these.
* Creating setup blocks ([Index Block](http://www.hannonhill.com/kb/Index-Block/))
    1. Create a setup block in the base folder (e.g. www/)
    2. Create a setup block in the sub folder (e.g. admissions/)
    3. Create your format
    4. Create an index block to find your setup blocks
    5. Select that index block from your format
        * This will give you a dump of the XML from all blocks indexed
        * You can alternatively use the [LocatorTool](http://www.hannonhill.com/kb/Script-Formats/#locator-tool)
    6. Use the [XPathTool](http://www.hannonhill.com/kb/Script-Formats/#xpath-tool) command `$_XPathTool.selectSingleNode` to find the default setup block, as well as the current setup block if it exists (using `"/system-index-block/system-folder[@current]/system-block[name='setup']"`)
        * perform the `selectSingleNode` action on the `$contentRoot`, which is a [predefined variable](http://www.hannonhill.com/kb/Script-Formats/#velocity-context).
    7. You can then get the node that you need within that block, and then whatever values you need.
* Creating setup blocks ([LocatorTool](http://www.hannonhill.com/kb/Script-Formats/#locator-tool))
    1. Set the current page
        * `#set($page = $_.locatePage($currentPagePath, $currentPageSiteName))`
    2. Set the parent directory
        * `#set($folder = $page.parentFolder)`
        * You can user the [PropertyTool](http://www.hannonhill.com/kb/Script-Formats/#property-tool) to display all the properties of a selected node `$_PropertyTool.outputProperties($page)`
    3. Find the setup block
        * `#for($child in $folder.children)` etc.
* All blocks use the "Default" metadata set unless you explicitly change it
    * Because of this, you want to make the "Default" set very generic
        * e.g. don't require any fields unless you're sure every single piece of content you create will require that

---
#### Basic Navigation

* Basic navigation (XPathTool)
    1. Get the base data that you're going to be dealing with
        * `#set($data = $_XPathTool.selectSingleNode($contentRoot, "/system-index-block"))`
    2. Get the parent folder
        * `#set($folder = $_XPathTool.selectSingleNode($data, "//system-folder[@current])"))`
    3. Get the items within that folder (i.e. current page siblings)
        * `#set($items = $_XPathTool.selectNodes($folder, "system-page[name='index'][dynamic-metadata[name='include-nav' and value='Yes']] | system-folder"))`
        * Note that `dynamic-metadata` values are case sensitive
    4. Check for items, and if there is at least one loop through and create a list of links ([see here](#1))
    5. Use a macro to get the link for each item in the list ([see here](#2))
    6. Use a macro to get the title for each item in the list ([see here](#3))
* Basic navigation (LocatorTool)
    1. Set the current page
        * `#set($page = $_.locatePage($currentPagePath, $currentPageSiteName))`
        * You could also potentially get the parent folder directly `#set($folder = $_.locateFolder('/'))`
    2. Get the parent folder
        * `#set($folder = $page.parentFolder)`
    3. Get the parent children (aka siblings)
        * `#set($children = $folder.children)`
    4. Do your nav loop ([see here](#4))
    5. Use a printTitle macro ([see here](#5))

##### Implementation Details

* If you want to get a high level of specificity when selecting navigation directories, you can create a data definition or metadata field on directories to allow you to select those directories.
    * e.g. Navigation Level metadata option with a `top-level` value for the root directory
    
##### Footnotes
    
<a name="1"></a>Navigation Loop:

    #if($items.size > 0)
        <ul>
            #getLink($folder)
            <li><a href="${link}">#printTitle($folder)</a></li>
        #foreach($item in $items)
            #if ($item.name == 'folder')
                #set ($children = $_XPathTool.selectNode($item, "system-page[name != 'index'][dynamic-metadata[name='include-nav' and value='Yes']]"))
                #foreach($child in $children)
                    $getLink($child)
                    <li><a href="${link}">#printTitle($item)</a></li>
                #end
            #end
            #getLink($item)
            <li><a href="${link}">#printTitle($item)</a></li>
        #end
        </ul>
    #end
    
<a name="2"></a>getLink Macro:

    #macro(getLink $node)
        #if($node.getChild("link"))
            #set ($link = $_EscapeTool.xml($node.getChild("link").value))
        #end
    #end

<a name="3"></a>printTitle Macro:

    #macro(printTitle $i)
        #if($i.getChild("display-name"))
            $_EscapeTool.xml($i.getChild("display-name").value)
        #elseif($i.getChild("title"))
            $_EscapeTool.xml($i.getChild("title").value)
        #else
            $_EscapeTool.xml($i.getChild("name").value)
        #end
    #end

<a name="4"></a>Locator Tool Navigation Loop

    #foreach($child in $children)
        #if($item.identifier.type == 'folder')
            #set($folderContent = $child.children)
            #foreach($grandChild in $folderContent)
                <li><a href="${grandChild.link}">#printTitle($grandChild)</a></li>
            #end
        #elseif($item.identifier.type == 'page')
            #if($child.metadata.getDynamicField('include-nav).value)
                <li><a href="${child.link}">#printTitle($child)</a></li>
            #end
        #end
    #end

<a name="5"></a>Locator Tool printTitle Macro

    #macro (printTitle $i)
        #if($_PropertyTool.isNull($i.metadata.displayName))
            $_EscapeTool.xml($i.metadata.dynamicField.displayName)
        #elseif(!$i.metadata.title.empty)
            $_EscapeTool.xml($i.metadata.title)
        #end
    #end

---
#### Format Imports
* There are some format elements that you will want to share across the site
    * We can create a format to contain these, and then import it into other formats
    * Create format file called `_shared`, for example
        * Underscore lets it float to the top when navigating the file tree
    * `import('_cascade/formats/_shared')`

---
#### Content Reuse

* Base template
    * `<system-page-meta-keywords/>` pulls in metadata content
    * `<system-page-title/>` tag pulls in the title of the current page
* Text content
    * If there is text that you know will be re-used across the site, you can create a text block containing that text and include it in your [configuration set](http://www.hannonhill.com/kb/Configuration-Set/) or template.
* Limit templates
    * If you need customization in just a few areas, use configuration sets or [content types](http://www.hannonhill.com/kb/Content-Type/) instead.

---
#### Calendar

* [Sample implementation](https://github.com/hannonhill/Calendar)
