from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from CrawlNodes.items import ClashItem


class ClashV2raySpider(CrawlSpider):
    name = 'clash_v2ray'
    allowed_domains = ['www.cfmem.com']
    # redis_key = 'clash_v2ray'
    start_urls = ['https://www.cfmem.com/search/label/free']
    # //*[@id="Blog1"]/div/article/div[1]/h2/a
    rules = (
        Rule(LinkExtractor(
            restrict_xpaths=('//*[@id="Blog1"]/div/article/div[1]/h2/a')), callback='parse_item', follow=True),
        Rule(LinkExtractor(
            restrict_xpaths=('//*[@id="starter-pro-load-more-link"]')), callback='parse_item', follow=True),)

    def parse_item(self, response):
        item = ClashItem()
        title = response.xpath(
            '//*[@id="Blog1"]/div/article/div/div[1]/h1/text()').get()
        nodes = response.xpath('//*[@id="post-body"]/div[4]/pre/span')
        node_list = []
        for node in nodes:
            node_list.append(node.xpath('string(.)').get())
        item['title'] = title
        item['nodes'] = node_list
        yield item
