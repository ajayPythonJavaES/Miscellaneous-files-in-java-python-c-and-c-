import xml.dom.minidom as xml

def readXML():
    xmlStr = open('F://xmltest.xml','r').read()
    doc = xml.parseString(xmlStr)
    print(doc.getElementsByTagName('book')[0].getAttribute('id'))

