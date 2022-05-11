# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import base64
from itemadapter import ItemAdapter
import pandas as pd
from CrawlNodes.items import ClashItem


class CrawlnodesPipeline:

    def process_item(self, item, spider):
        if isinstance(item, ClashItem):
            # print(item)
            pd.DataFrame(item['nodes']).to_csv(
                './CrawlNodes/datas/node/nodes.csv', header=False, index=False)
        return item

    def close_spider(self, spider):
        print("-" * 30, "\n完成！\n", "-" * 30)
        f = open('./CrawlNodes/datas/node/nodes.csv', encoding='utf-8')  # 读取文件
        a = f.read()  # 读取文件内容
        a = base64.b64encode(str(a).encode('utf-8'))  # 转换为base64
        # print(a.decode('utf-8'))  # 输出base64编码
        p = open('./CrawlNodes/datas/node/nodes.txt', 'w')
        p.write(a.decode('utf-8'))
        p.close()
        f.close()
