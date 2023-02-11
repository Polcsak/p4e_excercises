# Import libraries

import urllib.request
import urllib.parse
import urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Connect xml from web to python
# open comments_42.xml & comments_170....

link = input('Enter location: ')
data = urllib.request.urlopen(link).read().decode()
print('Retrieving', link)
print('Retrieved', len(data), 'characters')

# Data calculations

count = 0
sum = 0
tree = ET.fromstring(data)
tags = tree.findall('comments/comment')
#tags = tree.findall('.//count')

# For loop

for item in tags:
    sum = sum + int(item.find('count').text)
    count = count + 1

print('Count:', count)
print('Sum:', sum)