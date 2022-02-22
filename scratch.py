import os

def TestMiniDom(path):
    from xml.dom import minidom

    xmls = os.listdir(path)
    print(xmls)

    for x in xmls:
        if x.endswith('.xml'):
            # print(x)
            doc = minidom.parse(path + x)
            # contract = doc.documentElement
            # print(contract)
            # header = contract.getElementByName("HEADER")
            contract = doc.documentElement
            headers = contract.getElementsByTagName("HEADER")



            for header in headers:
                print(header.nodeName)
                list1=[]
                for n in header.childNodes:
                    node = n.childNodes
                    print(n.toxml())
                    print(n.nodeName)
                    print (n.tagName, "has value:", n.nodeValue, "and is child of:", n.parentNode.tagName)

                    list1.append(node)

                print(list1)







                list = []
                CONTRACT_NO = header.childNodes[0].childNodes[0].nodeValue
                list.append(CONTRACT_NO)
                CURRENCY_HEAD = header.childNodes[1].childNodes[0].nodeValue
                list.append(CURRENCY_HEAD)
                SUPPLIER = header.childNodes[2].childNodes[0].nodeValue
                list.append(SUPPLIER)
                SUPPLIER_NAME = header.childNodes[3].childNodes[0].nodeValue
                list.append(SUPPLIER_NAME)
                ORDER_DATE = header.childNodes[4].childNodes[0].nodeValue
                list.append(ORDER_DATE)
                # AMENDMENT_DATE = header.childNodes[5].childNodes[0].nodeValue
                # list.append(AMENDMENT_DATE)
                # print(list)
                PRINT_DATE = header.childNodes[6].childNodes[0].nodeValue
                list.append(PRINT_DATE)
                VER_NO = header.childNodes[7].childNodes[0].nodeValue
                list.append(VER_NO)
                ACTIVITY_TEXT = header.childNodes[8].childNodes[0].nodeValue
                list.append(ACTIVITY_TEXT)
                print(list)





    # doc = minidom.parse(path+"test.xml")
    #
    # # get root element: <employees/>
    # root = doc.documentElement
    # print(root)
    #
    # # get all children elements: <employee/> <employee/>
    # headers = root.getElementsByTagName("HEADER")
    #
    # for header in headers:
    #     print(header.nodeName)
    #     CONTRACT_NO = root.getElementsByTagName("CONTRACT_NO")
    #     print(CONTRACT_NO)



path = '/Users/mac_mini_007/Desktop/xml/'
TestMiniDom(path)

