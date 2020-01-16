import requests
import sys
import io
import bs4
import urllib3
#1、发送请求  http://xuexiao.51sxue.com/slist/?o=&t=3&areaCodeS=31
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
#url="https://www.baidu.com/"
for num in range(1,141):
    url='http://xuexiao.51sxue.com/slist/?t=3&areaCodeS=31&page='+str(num)
    #url='http://xuexiao.51sxue.com/slist/?t=2&areaCodeS=31'
    html=requests.get(url)
    html = html.text
    html = html.encode("ISO-8859-1")
    html = html.decode("gbk")

    #2、保存文件
    #所有的小学的元素id是dsadas
    fileOb = open('1.html', 'w', encoding='gbk')  # 打开一个文件，没有就新建一个
    fileOb.write(html)
    fileOb.close()
    #3、获取信息
    exampleFile = open('1.html')
    exampleSoup = bs4.BeautifulSoup(exampleFile.read(), 'html5lib')
    elems = exampleSoup.select('#dsadas')
    type(elems)
    for ele in elems:
        fileOb1 = open('result1.txt', 'a', encoding='utf-8')
        fileOb1.write(ele.getText())
        fileOb1.write("\n")
        fileOb1.close()