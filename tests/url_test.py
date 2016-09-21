import scrapy

class ScrapURL(scrapy.Spider):
    #NBA Catch and Shoot Stats
    name = 'URLscrap'
    url = ['http://stats.nba.com/stats/commonallplayers?IsOnlyCurrentSeason=0&LeagueID=00&Season=2016-17']

    def parse(self, response):
        filename = 'nba-' + response.url.split("/")[-2] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
