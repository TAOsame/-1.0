import os
import re
import requests


def url_open(url):
    # 以字典的形式添加请求头
    header = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0"
    }
    # 使用get方法发送请求获取网页源码
    response = requests.get(url, headers=header)
    return response


def find_imgs(url):
    html = url_open(url).text
    p = r'<img src="([^"]+\.jpg)"'

    img_addrs = re.findall(p, html)

    return img_addrs


def download_Meizi(dirName="meizi"):
    os.mkdir(dirName)
    os.chdir(dirName)

    pageNumber = 1
    x = 0
    img_address = []

    while pageNumber < 2 :
        page_url = url + '/a/sexy_'+str(pageNumber)+'.html'
        addrs = find_imgs(page_url)
        print(len(addrs))

        for i in addrs:
            if i in img_address:
                continue
            else:
                img_address.append(i)
            print(len(img_address))

        for each in img_address:
            print(each)
            pageNumber += 1

    for each in img_address:
        filename = str(x) + ".jpg"
        x+=1
        with open(filename,'wb') as f:
            img = url_open(each).content
            f.write(img)


if __name__ == '__main__':
    url = "http://www.meizitu.com"
    download_Meizi()


