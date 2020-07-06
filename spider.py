# https://www.meituan.com/changecity/
from pyquery import PyQuery as pq
import requests
def citynames():
    url = "https://www.meituan.com/changecity/"
    doc = pq(requests.get(url).text)
    name = doc('.cities a').items()
    name_dict = dict()
    for i in name:
        name_dict[i.text()] = 'https:'+i.attr.href+'/meishi/'
    return name_dict
name_dict = citynames()
# print(name_dict)


def get_html(url):
    '''
    下载 html 页面
    :return:
    '''
    doc = pq(requests.get(url).text)
    print(doc('li').text())
get_html(name_dict['金昌'])