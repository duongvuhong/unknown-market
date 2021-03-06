import scrapy

from scraper.items import ArticleItem


class VnexpressSpider(scrapy.Spider):
    name = 'VNExpress'
    allowed_domains = ['vnexpress.net']
    start_urls = [
        'https://vnexpress.net/kinh-doanh/quoc-te',
        'https://vnexpress.net/kinh-doanh/chung-khoan',
        'https://vnexpress.net/kinh-doanh/doanh-nghiep'
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for article in self.parse_page(response):
            yield article

    def parse_page(self, response):
        data_campaign = response.xpath('//div[normalize-space(@class)="container flexbox"]/div[@data-campaign]')

        headline = data_campaign.xpath('./div[1]')
        yield self.parse_article(headline.xpath('./article'))

        news = data_campaign.xpath('./div[last()]')
        for article in news.xpath('./article'):
            yield self.parse_article(article)

    def parse_article(self, article):
        picture = article.xpath('.//picture/source/img')
        title_link = article.xpath('./h2[@class="title-news"]/a')
        description = article.xpath('./p[@class="description"]/a')

        item = ArticleItem()

        item['thumbnail']   = picture.xpath('./@data-src').get()
        item['title']       = title_link.xpath('./text()').get()
        item['url']         = title_link.xpath('./@href').get()
        item['description'] = ' '.join(description.xpath('./text()').getall())

        return item
