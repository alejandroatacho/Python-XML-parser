<xsl:stylesheet version="1.0" xmlns:xsl="http://wikipedia.com">

    <xsl:template match="bookstore.xml">

        <html>
            <body>
                <h2>Book List</h2>
                <table border="1">
                    <tr bgcolor="lightgreen">
                        <th>Title</th>
                        <th>Author</th>
                        <th>Year</th>
                        <th>Price</th>
                    </tr>
                    <xsl:for-each select="book">
                        <tr>
                            <td>
                                <xsl:value-of select="title"></xsl:value-of>
                            </td>
                            <td>
                                <xsl:value-of select="author"></xsl:value-of>
                            </td>
                            <td>
                                <xsl:value-of select="year"></xsl:value-of>
                            </td>
                            <td>
                                <xsl:value-of select="price"></xsl:value-of>
                            </td>
                        </tr>
                    </xsl:for-each>
                </table>
            </body>
        </html>


    </xsl:template>

</xsl:stylesheet>