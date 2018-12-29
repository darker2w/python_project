# coding:UTF-8
import urllib
import re
import os
import string

hosturl = 'https://www.woyaogexing.com'
def getHtmlCode(url):
    url = checkURL(url)
    if len(url) < 1:
        return ''

    netpage = urllib.urlopen(url)
    htmlcode = netpage.read()
    return htmlcode

def checkURL(url):
    if len(url) < 1 :
        return ''
    if string.find(url, '.com') == -1:
        if string.find(url, 'javascript') != -1:
            return ''
        if string.find(url, '.jpg') == -1:
            if string.find(url, '.html') == -1:
                return ''
            else:
                if string.find(url, '/') != -1:
                    return hosturl+url
                else:
                    return hosturl+'/'+url
        else:
            return "https:"+url
    else:
        if string.find(url,'https://') != -1:
            return url
        else:
            url = 'https:' + url
            return url

    return ''



#获取这个url里面的图片数据并下载下来
def getImage(imagelist):
    global index
    global jpg_path
    for img in imagelist:
        print '下载：' + img
        index = index + 1
        imgurl = checkURL(img)
        savepath = (jpg_path + '/%s.jpg' % index)
        print savepath
        urllib.urlretrieve(imgurl, savepath)


def retileHost(host):
    global jpg_path
    global png_path
    urls = getURL(hosturl)
    url_num = len(urls)
    idx = 0
    while idx < url_num:
        url = urls[idx]
        url = checkURL(url)
        if len(url) > 0:
            getImage(url, jpg_path, png_path)

        idx += 1

def getImageURL(url):
    reg_jpg = r'src="(.+?\.jpg)" width'
    # reg_png = r'src="(.+?\.png)" width'

    reg_img_jpg = re.compile(reg_jpg)
    # reg_img_png = re.compile(reg_png)

    htmlcode = getHtmlCode(url)

    print('开始爬虫...')
    jpglist = reg_img_jpg.findall(htmlcode)
    # pnglist = reg_img_png.findall(htmlcode)

    return jpglist

def getURL(host):
    htmlcode = getHtmlCode(host)
    reg_url = r'href="(.+?.html)" '
    reg_url_html = re.compile(reg_url)
    htmllist = reg_url_html.findall(htmlcode)

    return htmllist

def getURLData(url):
    urls = getURL(url)
    imgs = getImageURL(url)

    if len(imgs) > 0:
        getImage(imgs)
    else:
        return

    url_num = len(urls)
    url_index = 0
    while len(urls) > 0:
        url = urls[url_index]
        getURLData(url)
        urls.pop(url_index)
        url_index += 1

def main():
    global index
    index = 0
    global jpg_path
    jpg_path = './JPG'
    global png_path
    png_path = './PNG'

    if not os.path.exists(jpg_path):
        os.makedirs(jpg_path)
        print('创建JPG目录成功')
    if not os.path.exists(png_path):
        os.makedirs(png_path)
        print ('创建PNG目录成功')

    getURLData(hosturl)



main();