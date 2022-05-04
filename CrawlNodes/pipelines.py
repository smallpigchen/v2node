# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pandas as pd
from CrawlNodes.items import ClashItem


class CrawlnodesPipeline:

    def process_item(self, item, spider):
        if isinstance(item, ClashItem):
            # print(item)
            pd.DataFrame(item['nodes']).to_csv(
                'nodes.csv', mode='a', header=False, index=False)
        return item

    def close_spider(self, spider):
        print("-" * 30, "\n完成！\n", "-" * 30)
