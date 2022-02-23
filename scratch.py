import os
import pandas as pd

def TestMiniDom(path):
    from xml.dom import minidom

    xmls = os.listdir(path)
    print(xmls)
    list = []

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
                # list1=[]
                # for n in header.childNodes:
                #     node = n.childNodes
                #     print(n.toxml())
                #     print(n.nodeName)
                #     print (n.tagName, "has value:", n.nodeValue, "and is child of:", n.parentNode.tagName)
                #
                #     list1.append(node)
                #
                # print(list1)







                # list = []
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



            purchasers = contract.getElementsByTagName("PURCHASER")

            for purchaser in purchasers:
                print(purchaser.nodeName)


                # list = []
                PURCHASER_NAME = purchaser.childNodes[0].childNodes[0].nodeValue
                list.append(PURCHASER_NAME)
                DEPARTMENT = purchaser.childNodes[1].childNodes[0].nodeValue
                list.append(DEPARTMENT)
                TELEPHONE = purchaser.childNodes[2].childNodes[0].nodeValue
                list.append(TELEPHONE)
                # FAX = purchaser.childNodes[3].childNodes[0].nodeValue
                # list.append(FAX)
                EMAIL = purchaser.childNodes[4].childNodes[0].nodeValue
                list.append(EMAIL)

                print(list)



            items = contract.getElementsByTagName("ITEM")

            for item in items:
                print(purchaser.nodeName)

                # list = []
                PRODUCT = item.childNodes[0].childNodes[0].nodeValue
                list.append(PRODUCT)
                DESCRIPTION = item.childNodes[1].childNodes[0].nodeValue
                list.append(DESCRIPTION)
                PRICE_TYPE = item.childNodes[2].childNodes[0].nodeValue
                list.append(PRICE_TYPE)
                PRICE_UNIT_ITEM = item.childNodes[3].childNodes[0].nodeValue
                list.append(PRICE_UNIT_ITEM)
                PRICE_UOM = item.childNodes[4].childNodes[0].nodeValue
                list.append(PRICE_UOM)
                NET_PRICE = item.childNodes[5].childNodes[0].nodeValue
                list.append(NET_PRICE)
                ITEM_CURRENCY = item.childNodes[6].childNodes[0].nodeValue
                list.append(ITEM_CURRENCY)

                print(item.childNodes[7].nodeName)
                TYPE = item.childNodes[7].childNodes[0].childNodes[0].nodeValue
                list.append(TYPE)
                VALIDITY_START = item.childNodes[7].childNodes[1].childNodes[0].nodeValue
                list.append(VALIDITY_START)
                VALIDITY_END = item.childNodes[7].childNodes[2].childNodes[0].nodeValue
                list.append(VALIDITY_END)
                VALUE = item.childNodes[7].childNodes[3].childNodes[0].nodeValue
                list.append(VALUE)
                CURRENCY_COND = item.childNodes[7].childNodes[4].childNodes[0].nodeValue
                list.append(CURRENCY_COND)
                PRICE_UNIT_COND = item.childNodes[7].childNodes[5].childNodes[0].nodeValue
                list.append(PRICE_UNIT_COND)
                PRICE_UOM_COND = item.childNodes[7].childNodes[6].childNodes[0].nodeValue
                list.append(PRICE_UOM_COND)

                # LOCATION_NAME = item.childNodes[7].childNodes[7].childNodes[0].nodeValue
                # list.append(LOCATION_NAME)

                DOC_CURR = item.childNodes[7].childNodes[8].childNodes[0].nodeValue
                list.append(DOC_CURR)
                CONVERTED_PRICE = item.childNodes[7].childNodes[9].childNodes[0].nodeValue
                list.append(CONVERTED_PRICE)

                # FRML_WEIGHT = item.childNodes[7].childNodes[10].childNodes[0].nodeValue
                # list.append(FRML_WEIGHT)

                FRML_NOTATION = item.childNodes[7].childNodes[11].childNodes[0].nodeValue
                list.append(FRML_NOTATION)

                # FRML_PER = item.childNodes[19].childNodes[0].nodeValue
                # list.append(FRML_PER)
                # FRML_UM = item.childNodes[20].childNodes[0].nodeValue
                # list.append(FRML_UM)
                # FRML_BTQ = item.childNodes[21].childNodes[0].nodeValue
                # list.append(FRML_BTQ)
                # FRML_SURCHRG = item.childNodes[22].childNodes[0].nodeValue
                # list.append(FRML_SURCHRG)

                print(item.childNodes[8].nodeName)
                DEMAND_LOCATION = item.childNodes[8].childNodes[0].childNodes[0].nodeValue
                list.append(DEMAND_LOCATION)
                DEMAND_LOCATION_DESC = item.childNodes[8].childNodes[1].childNodes[0].nodeValue
                list.append(DEMAND_LOCATION_DESC)
                DEMAND_LOC_STATUS = item.childNodes[8].childNodes[2].childNodes[0].nodeValue
                list.append(DEMAND_LOC_STATUS)
                # QUANTITY = item.childNodes[8].childNodes[3].childNodes[0].nodeValue
                # list.append(QUANTITY)
                DELIVERY_LOCATION = item.childNodes[8].childNodes[4].childNodes[0].nodeValue
                list.append(DELIVERY_LOCATION)
                DELIVERY_LOCATION_DESC = item.childNodes[8].childNodes[5].childNodes[0].nodeValue
                list.append(DELIVERY_LOCATION_DESC)
                DELIVERY_TERMS = item.childNodes[8].childNodes[6].childNodes[0].nodeValue
                list.append(DELIVERY_TERMS)
                PRODUCT_LOCATION = item.childNodes[8].childNodes[7].childNodes[0].nodeValue
                list.append(PRODUCT_LOCATION)
                PRODUCT_LOCATION_DESC = item.childNodes[8].childNodes[8].childNodes[0].nodeValue
                list.append(PRODUCT_LOCATION_DESC)
                INCOTERM = item.childNodes[8].childNodes[9].childNodes[0].nodeValue
                list.append(INCOTERM)
                INCOTERM_LOCATION = item.childNodes[8].childNodes[10].childNodes[0].nodeValue
                list.append(INCOTERM_LOCATION)
                # PACKAGING_TYPE = item.childNodes[8].childNodes[11].childNodes[0].nodeValue
                # list.append(PACKAGING_TYPE)
                DISPATCH_TYPE = item.childNodes[8].childNodes[12].childNodes[0].nodeValue
                list.append(DISPATCH_TYPE)
                PAYMENT_TERMS = item.childNodes[8].childNodes[13].childNodes[0].nodeValue
                list.append(PAYMENT_TERMS)
                INVOICING_PARTY = item.childNodes[8].childNodes[14].childNodes[0].nodeValue
                list.append(INVOICING_PARTY)
                INVOICING_PARTY_DESCR = item.childNodes[8].childNodes[15].childNodes[0].nodeValue
                list.append(INVOICING_PARTY_DESCR)
                QUOTA = item.childNodes[8].childNodes[16].childNodes[0].nodeValue
                list.append(QUOTA)

                print(list)
                column_name = ['CONTRACT_NO', 'CURRENCY_HEAD', 'SUPPLIER', 'SUPPLIER_NAME', 'ORDER_DATE', 'PRINT_DATE',
                               'VER_NO',
                               'ACTIVITY_TEXT', 'PURCHASER_NAME', 'DEPARTMENT', 'TELEPHONE', 'EMAIL', 'PRODUCT',
                               'DESCRIPTION',
                               'PRICE_TYPE', 'PRICE_UNIT_ITEM', 'PRICE_UOM', 'NET_PRICE', 'ITEM_CURRENCY', 'TYPE',
                               'VALIDITY_START',
                               'VALIDITY_END', 'VALUE', 'CURRENCY_COND', 'PRICE_UNIT_COND', 'PRICE_UOM_COND',
                               'DOC_CURR',
                               'CONVERTED_PRICE', 'FRML_NOTATION', 'DEMAND_LOCATION', 'DEMAND_LOCATION_DESC',
                               'DEMAND_LOC_STATUS',
                               'DELIVERY_LOCATION', 'DELIVERY_LOCATION_DESC', 'DELIVERY_TERMS', 'PRODUCT_LOCATION',
                               'PRODUCT_LOCATION_DESC', 'INCOTERM', 'INCOTERM_LOCATION', 'DISPATCH_TYPE',
                               'PAYMENT_TERMS',
                               'INVOICING_PARTY', 'INVOICING_PARTY_DESCR', 'QUOTA']
                xml_df = pd.DataFrame([list], columns=column_name)
                print(xml_df)
                xml_df.to_csv(path+'data.csv', mode='a', header=True, index=None)





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

