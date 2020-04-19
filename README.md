# MailCrawler
Web crawler for finding Email addresses

Known Issues:
1. Searching recursively from the site's root isn't supported yet
2. Finding addresses through the response data. irrelevant email addresses may be returned (such as programmers)
3. Recursion crawling isn't supported yet
4. Wrong handling with duplicates in the mail addresses

TODO:
1. Recursion crawling
2. Implement scrapy crawling instead of requests
3. Logging
4. GET vs. POST research
5. HTTPS research
6. Not [200 OK] response research