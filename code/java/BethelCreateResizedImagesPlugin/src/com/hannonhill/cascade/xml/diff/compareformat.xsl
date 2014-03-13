<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="html" indent="yes"/>
	<xsl:template match="/">
		<system-xml>
		<xsl:if test="count(//*[starts-with(@class, 'diff-')]) = 0">
			<xsl:comment><![CDATA[[if IE 6]>
			<style type="text/css">
				div.no-diff-notification { display: none;}
			</style>	
			<div style="position:absolute; top: 0; left: 0; background: #FFFF66 url(%%CONTEXT%PATH%%/css/icons/information.gif) no-repeat scroll 5px 50%; border: 1px solid gray; padding-top: 5px; padding-left: 25px; padding-bottom: 5px; width: 100%">%%NO%DIFF%%</div>
			<![endif]]]></xsl:comment>		
			<div class="no-diff-notification" style="position: fixed; top: 0; left: 0;background: #FFFF66 url(%%CONTEXT%PATH%%/css/icons/information.gif) no-repeat scroll 5px 50%; border: 1px solid gray; padding-top: 5px; padding-left: 25px; padding-bottom: 5px; width: 100%">%%NO%DIFF%%</div>

		</xsl:if>
		  <style type="text/css">
		  <![CDATA[
		      /*
			 * Styles for the Tag Diff
			 */
			span.diff-tag-html {
			  font-family: "Andale Mono" monospace;
			  font-size: 80%;
			}
			
			span.diff-tag-removed {
			  font-size: 100%;
			  text-decoration: line-through;
			  background-color: #fdc6c6; /* light red */
			}
			
			span.diff-tag-added {
			  font-size: 100%;
			  background-color: #ccffcc; /* light green */
			}
			
			/*
			 * Styles for the HTML Diff
			 */
			span.diff-html-added {
			  font-size: 100%;
			  background-color: #ccffcc; /* light green */
			  
			}
			
			span.diff-html-removed {
			  font-size: 100%;
			  text-decoration: line-through;
			  background-color: #fdc6c6; /* light red */
			}
			
			span.diff-html-changed {
			  background-color: #c6c6fd; /* light blue */
			  cursor: pointer;
			}
			
			span.diff-html-selected {
			  background-color: #FF8800; /* light orange */
			}
			
			span.diff-html-selected img{
			   border: 2px solid #FF8800; /* light orange */
			}
			
			span.diff-html-added img{
			 border: 2px solid #ccffcc;
			}
			
			span.diff-html-removed img{
			 border: 2px solid #fdc6c6;
			}
			
			span.diff-html-changed img{
			 border: 2px dotted #000099;
			 
			}
			
			div.diff-removed-image, div.diff-added-image{
			  height: 300px;
			  width: 200px;  
			  position: absolute;
			  opacity : 0.55;
			  filter: alpha(opacity=55);
			  -moz-opacity: 0.55;
			}
			
			div.diff-removed-image, div.diff-added-image {
			  margin-top: 2px;
			  margin-bottom: 2px;
			  margin-right: 2px;
			  margin-left: 2px;
			}
			
			div.diff-removed-image {
			  background-color: #fdc6c6;
			  background-image: url(../images/diffmin.gif);
			}
			div.diff-added-image {
			  background-color: #ccffcc;
			  background-image: url(../images/diffplus.gif);
			  background-repeat: no-repeat;
			}
			
			img.diff-icon {
			  background-color: #FF8800;
			  background-image: url(../images/bg_rounded.gif);
			  width: 16px;
			  height: 16px;
			  border: 0px none;
			}
			
			table.diff-tooltip-link, table.diff-tooltip-link-changed {
			   width: 100%;
			   text-align: center;
			   Vertical-align: middle;
			}
			
			table.diff-tooltip-link-changed {
			    border-top: thin dashed #000000; 
			    margin-top: 3px; 
			    padding-top: 3px
			}
			td.diff-tooltip-prev {
			   text-align: left;
			}
			
			td.diff-tooltip-next {
			   text-align: right;
			}
			
			table.diffpage-html-firstlast {
			  width: 100%;
			  Vertical-align: middle;
			}
			
			div.diff-topbar{
			 border-bottom: 2px solid #FF8800;
			 border-left: 1px solid #FF8800;
			 border-right: 1px solid #FF8800;
			 background-color: #FFF5F5;
			}
			
			a.diffpage-html-a, a.diffpage-html-a:hover, a.diffpage-html-a:link, a.diffpage-html-a:visited, a.diffpage-html-a:active {
			  text-decoration: none;
			  color: #FF8800;
			}
			
			.diffpage-html-firstlast a img, .dsydiff-prevnextnav a img {
			  vertical-align: middle;
			}
			
			ul.changelist {
			  padding-left: 15px;
			}
			
			body{
			  margin-top: 0px;
			}	
			
			
			]]>
		  </style>
		  
		  
		  
		  <xsl:apply-templates select="diffreport/diff/node()"/>
		</system-xml>
	</xsl:template>
	
	<xsl:template match="@*|node()">
		<xsl:copy>
		  <xsl:apply-templates select="@*|node()"/>
		</xsl:copy>
    </xsl:template>
    
    <xsl:template match="span[@class='diff-html-changed']">
<span>
  <xsl:copy-of select="@*"/>
  <xsl:attribute name="onclick">showDiffFormatChange(this, escape("<xsl:value-of select="@changes"/>")); return false;</xsl:attribute>
 
  <xsl:apply-templates select="node()"/>

</span>
</xsl:template>
</xsl:stylesheet>