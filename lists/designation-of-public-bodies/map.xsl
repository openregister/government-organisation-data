<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:leg="http://www.legislation.gov.uk/namespaces/legislation">
<xsl:output method="text" encoding="UTF-8"/>

<xsl:template match="/">
  <xsl:apply-templates select="//leg:ListItem"/>
</xsl:template>

<xsl:template match="leg:ListItem">
  <!-- name --><xsl:value-of select="leg:Para/leg:Text"/><xsl:text>
</xsl:text>
</xsl:template>

</xsl:stylesheet>
