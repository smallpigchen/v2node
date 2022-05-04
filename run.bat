cd CrawlNodes/datas/node/ rm -r nodes.csv
cd ../../.
scrapy crawl clash_v2ray
git add .
git commit -m "爬取v2ray节点"
git push
