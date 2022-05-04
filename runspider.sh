cd CrawlNodes/datas/node && rm -r nodes.csv,nodes.txt
touch nodes.csv
cd ../../..
scrapy crawl clash_v2ray
cd CrawlNodes/datas/node && python tobase64.py
git add .
git commit -am "爬取v2ray节点"
git push -f
