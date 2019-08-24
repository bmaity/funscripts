'''Program to parse xml '''

'''Program to parse xml '''

import xml.etree.ElementTree as ET
data = '''<person>
    <name>Bisu</name>
    <phone type = "intl">
    +1 xxx xxx xxxx
    </phone>
    <email hide = "yes"/>
    </person>'''

tree = ET.fromstring(data)
print("Name:", tree.find('name').text)
print("Attr:", tree.find('email').get('hide'))
