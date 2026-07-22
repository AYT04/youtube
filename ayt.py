import xml.etree.ElementTree as ET

tree = ET.parse('subscriptions.opml')
for node in tree.findall('.//outline'):
    url = node.attrib.get('xmlUrl')
    if url:
        print(url)