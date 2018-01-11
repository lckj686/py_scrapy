from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from xiaozhu.items import XiaozhuItem


class xiaozhu(CrawlSpider):
    name = 'xiaozhu'
    start_urls = ['http://bj.xiaozhu.com/fangzi/22317292103.html', 'http://bj.xiaozhu.com/fangzi/2803985763.html']

    def parse(self, responce):
        item = XiaozhuItem()
        selector = Selector(responce)
        title = selector.xpath('//h4/em/text()').extract()[0]
        address = selector.xpath('//*[@id="introducePart"]/div[3]/div[2]/div[1]/p/text()').extract()[0]

        traffic = selector.xpath('//*[@id="introducePart"]/div[3]/div[2]/div[1]/p/text()').extract()[0]

        item['title'] = title
        item['address'] = address
        item['traffic'] = traffic

        yield item
