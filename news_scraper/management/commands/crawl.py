from django.core.management.base import BaseCommand
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from news_scraper.spiders.vnexpress import VnexpressSpider

from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from news_scraper import settings as my_settings



class Command(BaseCommand):
    help = "Release the spiders"

    def handle(self, *args, **options):
        crawler_settings = Settings()
        crawler_settings.setmodule(my_settings)
        process = CrawlerProcess(settings=crawler_settings)

        process.crawl(VnexpressSpider)
        process.start()
