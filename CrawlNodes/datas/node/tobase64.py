import base64

if __name__ == '__main__':
    f = open('CrawlNodes/datas/node/nodes.csv', encoding='utf-8')  # 读取文件
    a = f.read()  # 读取文件内容
    a = base64.b64encode(str(a).encode('utf-8'))  # 转换为base64
    print(a.decode('utf-8'))  # 输出base64编码
    p = open('nodes.txt', 'w')
    p.write(a.decode('utf-8'))
    p.close()
    f.close()
