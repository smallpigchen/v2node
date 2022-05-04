cd CrawlNodes/datas/node/ && rm -r nodes.csv

touch nodes.csv
cd ../../.
scrapy crawl clash_v2ray
#git add .
#git commit -am "爬取v2ray节点"
#git push