"""
 * Created by PyCharm.
 * User: tuhoangbk
 * Date: 13/06/2018
 * Time: 16:30
 * Have a nice day　:*)　:*)
"""
from io import open

def getlink(file_html, file_link):
    html_file = open(file_html, 'r')
    line_html =  html_file.readline()
    link_file = open(file_link, 'w')
    #get link image from google search
    for i in range (0, len(line_html)):
        if line_html[i:i+6] == '\"ru":\"':
            for j in range (i+6, len(line_html)):
                if line_html[j] == '\"':
                    print(line_html[i+6:j])
                    link_file.write(line_html[i+6:j] + '\n')
                    break
    link_file.close()
    html_file.close()