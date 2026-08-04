<?xml version="1.0" encoding="UTF-8"?>
<!-- Browser-side pretty-print for feed.xml. When someone opens the RSS feed in
     a browser instead of a feed reader, this transforms the raw XML into a
     readable, on-brand headline list. Feed readers ignore it. -->
<xsl:stylesheet version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
  xmlns:content="http://purl.org/rss/1.0/modules/content/">
<xsl:output method="html" encoding="UTF-8" indent="yes"
  doctype-system="about:legacy-compat"/>

<xsl:template match="/rss/channel">
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<script src="/theme-init.js"></script>
<title><xsl:value-of select="title"/> — RSS feed</title>
<link rel="icon" type="image/png" href="/favicon.png"/>
<link rel="apple-touch-icon" href="/apple-touch-icon.png"/>
<link rel="stylesheet" href="/style.css"/>
</head>
<body>
<header class="site">
  <a class="brand" href="/"><img class="brand-shark" src="/shark.png" alt="" width="20" height="20"/><xsl:text> </xsl:text><xsl:value-of select="title"/></a>
</header>
<div class="layout">
  <main>
    <section class="intro">
      <h1>RSS feed</h1>
      <p>This is the <xsl:value-of select="title"/> feed. Paste this page's URL
      into a feed reader to subscribe, or browse the latest posts below.</p>
    </section>
    <ul class="entries">
      <xsl:for-each select="item">
        <li class="entry">
          <a class="entry-title" href="{link}"><xsl:value-of select="title"/></a>
          <time><xsl:value-of select="substring(pubDate, 1, 16)"/></time>
          <p class="hook"><xsl:value-of select="description"/></p>
          <a class="read-more" href="{link}">Read more →</a>
        </li>
      </xsl:for-each>
    </ul>
  </main>
</div>
<footer class="site">
  <span><xsl:value-of select="title"/> — <xsl:value-of select="description"/></span>
</footer>
</body>
</html>
</xsl:template>
</xsl:stylesheet>
