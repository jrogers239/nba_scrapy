import scrapy

class QuotesSpider(scrapy.Spider):
    name = "nba"
    start_urls = [
        'http://stats.nba.com/player/#1/893/career/'
    ]

    def parse(self, response):
        filename = 'nba-' + response.url.split("/")[-2] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
