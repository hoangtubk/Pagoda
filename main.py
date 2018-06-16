"""
 * Created by PyCharm.
 * User: tuhoangbk
 * Date: 13/06/2018
 * Time: 15:02
 * Have a nice day　:*)　:*)
"""
from crawl.getlink import getlink
from crawl.download_image import download_image_from_site

if __name__ == '__main__':
    # getlink('google-search-chua.html', 'link.txt')
    # getlink('google-search-temple.html', 'link2.txt')
    getlink('google-search-pagoda.html', 'link3.txt')
    file_links = open('link3.txt')
    while (True):
        try:
            link = file_links.readline()
            print('Downloading image from link \n' + link)
            download_image_from_site(link)
        except:
            break
