<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE peclo[
<!ENTITY new-line "&#60081;">
<!ENTITY bold-open "&#60082;">
<!ENTITY bold-close "&#60083;">
]>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:output method="text" encoding="utf-8"/>

<xsl:template match="dict">
	<xsl:apply-templates select="*|comment()"/>
</xsl:template>

<xsl:template match="comment()">
	<xsl:text>//</xsl:text>
	<xsl:value-of select="normalize-space(.)"/>
	<xsl:text>&#xa;</xsl:text>
</xsl:template>

<xsl:template match="entry">
	<xsl:value-of select="@simplified"/>
	<xsl:if test="@traditional">
		<xsl:text>[</xsl:text>
		<xsl:value-of select="@traditional"/>
		<xsl:text>]</xsl:text>
	</xsl:if>
	<xsl:text>&#x9;</xsl:text>
	<xsl:value-of select="@pinyin"/>
	<xsl:text>&#x9;</xsl:text>
	<xsl:apply-templates select="def"/>
	<xsl:text>&#xa;</xsl:text>
</xsl:template>

<xsl:template match="def">
	<xsl:text>&bold-open;</xsl:text>
	<xsl:value-of select="@type"/>
	<xsl:text>&bold-close; </xsl:text>
	<xsl:value-of select="normalize-space(.)"/>
	<xsl:text>&new-line;</xsl:text>
	</xsl:template>
</xsl:stylesheet>
