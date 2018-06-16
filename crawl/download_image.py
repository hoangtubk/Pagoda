"""
 * Created by PyCharm.
 * User: tuhoangbk
 * Date: 13/06/2018
 * Time: 16:20
 * Have a nice day　:*)　:*)
"""

import re
import requests
from bs4 import BeautifulSoup
import urllib.request

website = 'http://vovworld.vn/vi-VN/viet-nam-dat-nuoc-con-nguoi/mai-chua-hue-net-kien-truc-dac-trung-cua-chua-viet-363410.vov'

def download_image_from_site(website):
    response = requests.get(website)

    soup = BeautifulSoup(response.text, 'html.parser')
    img_tags = soup.find_all('img')
    # link_images = img_tags.find_all('src')
    for tag in img_tags:
        link_img = tag['src']
        if not (link_img.endswith(".png")) and not (link_img.endswith('.jpg')):
            continue
        name_img = link_img.split('/')[-1]
        try:
            urllib.request.urlretrieve(link_img, '../image/' + name_img)
        except:
            pass

if __name__ == '__main__':
    download_image_from_site('http://thuexemaydanang.com.vn/choang-ngop-ve-dep-ngoi-chua-nam-o-ngoai-o-da-nang.html')
