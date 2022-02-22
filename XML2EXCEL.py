#coding=utf-8
import xml.dom.minidom
import xlsxwriter
import pandas as pd
import glob
import os
import os.path


path = 'C://Users//lli//Desktop//XML//'
xmls = os.listdir(path)
print(xmls)

for x in xmls:
    list = []
    print(x)
    dom = xml.dom.minidom.parse(x)
    doc_contract = xml.dom.minidom.parseString(dom)
    doc_contract.getElementsByTagName("CONTRACT")

    CONTRACT_NO = [p.firstChild.wholeText for p in doc_contract.getElementsByTagName("CONTRACT_NO") if
                   p.firstChild.nodeType == p.TEXT_NODE]
    for x in CONTRACT_NO:
        list.append(x)
    CURRENCY_HEAD = [p.firstChild.wholeText for p in doc_contract.getElementsByTagName("CURRENCY_HEAD") if
                     p.firstChild.nodeType == p.TEXT_NODE]
    for x in CURRENCY_HEAD:
        list.append(x)
    SUPPLIER = [p.firstChild.wholeText for p in doc_contract.getElementsByTagName("SUPPLIER") if
                p.firstChild.nodeType == p.TEXT_NODE]
    for x in SUPPLIER:
        list.append(x)
    SUPPLIER_NAME = [p.firstChild.wholeText for p in doc_contract.getElementsByTagName("SUPPLIER_NAME") if
                     p.firstChild.nodeType == p.TEXT_NODE]
    for x in SUPPLIER_NAME:
        list.append(x)
    ORDER_DATE = [p.firstChild.wholeText for p in doc_contract.getElementsByTagName("ORDER_DATE") if
                  p.firstChild.nodeType == p.TEXT_NODE]
    for x in ORDER_DATE:
        list.append(x)
    PRINT_DATE = [p.firstChild.wholeText for p in doc_contract.getElementsByTagName("PRINT_DATE") if
                  p.firstChild.nodeType == p.TEXT_NODE]
    for x in PRINT_DATE:
        list.append(x)
    VER_NO = [p.firstChild.wholeText for p in doc_contract.getElementsByTagName("VER_NO") if
              p.firstChild.nodeType == p.TEXT_NODE]
    for x in VER_NO:
        list.append(x)
    ACTIVITY_TEXT = [p.firstChild.wholeText for p in doc_contract.getElementsByTagName("ACTIVITY_TEXT") if
                     p.firstChild.nodeType == p.TEXT_NODE]
    for x in ACTIVITY_TEXT:
        list.append(x)

    PURCHASER_NAME = [p.firstChild.wholeText for p in doc_contract.getElementsByTagName("PURCHASER_NAME") if
                      p.firstChild.nodeType == p.TEXT_NODE]
    for x in PURCHASER_NAME:
        list.append(x)
    DEPARTMENT = [p.firstChild.wholeText for p in doc_contract.getElementsByTagName("DEPARTMENT") if
                  p.firstChild.nodeType == p.TEXT_NODE]
    for x in DEPARTMENT:
        list.append(x)
    TELEPHONE = [p.firstChild.wholeText for p in doc_contract.getElementsByTagName("TELEPHONE") if
                 p.firstChild.nodeType == p.TEXT_NODE]
    for x in TELEPHONE:
        list.append(x)
    EMAIL = [p.firstChild.wholeText for p in doc_contract.getElementsByTagName("EMAIL") if
             p.firstChild.nodeType == p.TEXT_NODE]
    for x in EMAIL:
        list.append(x)

    PRODUCT = [p.firstChild.wholeText for p in doc_contract.getElementsByTagName("PRODUCT") if
               p.firstChild.nodeType == p.TEXT_NODE]
    for x in PRODUCT:
        list.append(x)
    DESCRIPTION = [p.firstChild.wholeText for p in doc_contract.getElementsByTagName("DESCRIPTION") if
                   p.firstChild.nodeType == p.TEXT_NODE]
    for x in DESCRIPTION:
        list.append(x)
    PRICE_TYPE = [p.firstChild.wholeText for p in doc_contract.getElementsByTagName("PRICE_TYPE") if
                  p.firstChild.nodeType == p.TEXT_NODE]
    for x in PRICE_TYPE:
        list.append(x)
    PRICE_UNIT_ITEM = [p.firstChild.wholeText for p in doc_contract.getElementsByTagName("PRICE_UNIT_ITEM") if
                       p.firstChild.nodeType == p.TEXT_NODE]
    for x in PRICE_UNIT_ITEM:
        list.append(x)
    PRICE_UOM = [p.firstChild.wholeText for p in doc_contract.getElementsByTagName("PRICE_UOM") if
                 p.firstChild.nodeType == p.TEXT_NODE]
    for x in PRICE_UOM:
        list.append(x)
    NET_PRICE = [p.firstChild.wholeText for p in doc_contract.getElementsByTagName("NET_PRICE") if
                 p.firstChild.nodeType == p.TEXT_NODE]
    for x in NET_PRICE:
        list.append(x)
    ITEM_CURRENCY = [p.firstChild.wholeText for p in doc_contract.getElementsByTagName("ITEM_CURRENCY") if
                     p.firstChild.nodeType == p.TEXT_NODE]
    for x in ITEM_CURRENCY:
        list.append(x)
    TYPE = [p.firstChild.wholeText for p in doc_contract.getElementsByTagName("TYPE") if
            p.firstChild.nodeType == p.TEXT_NODE]
    for x in TYPE:
        list.append(x)
    VALIDITY_START = [p.firstChild.wholeText for p in doc_contract.getElementsByTagName("VALIDITY_START") if
                      p.firstChild.nodeType == p.TEXT_NODE]
    for x in VALIDITY_START:
        list.append(x)
    VALIDITY_END = [p.firstChild.wholeText for p in doc_contract.getElementsByTagName("VALIDITY_END") if
                    p.firstChild.nodeType == p.TEXT_NODE]
    for x in VALIDITY_END:
        list.append(x)
    VALUE = [p.firstChild.wholeText for p in doc_contract.getElementsByTagName("VALUE") if
             p.firstChild.nodeType == p.TEXT_NODE]
    for x in VALUE:
        list.append(x)
    CURRENCY_COND = [p.firstChild.wholeText for p in doc_contract.getElementsByTagName("CURRENCY_COND") if
                     p.firstChild.nodeType == p.TEXT_NODE]
    for x in CURRENCY_COND:
        list.append(x)
    PRICE_UNIT_COND = [p.firstChild.wholeText for p in doc_contract.getElementsByTagName("PRICE_UNIT_COND") if
                       p.firstChild.nodeType == p.TEXT_NODE]
    for x in PRICE_UNIT_COND:
        list.append(x)
    PRICE_UOM_COND = [p.firstChild.wholeText for p in doc_contract.getElementsByTagName("PRICE_UOM_COND") if
                      p.firstChild.nodeType == p.TEXT_NODE]
    for x in PRICE_UOM_COND:
        list.append(x)
    DOC_CURR = [p.firstChild.wholeText for p in doc_contract.getElementsByTagName("DOC_CURR") if
                p.firstChild.nodeType == p.TEXT_NODE]
    for x in DOC_CURR:
        list.append(x)
    CONVERTED_PRICE = [p.firstChild.wholeText for p in doc_contract.getElementsByTagName("CONVERTED_PRICE") if
                       p.firstChild.nodeType == p.TEXT_NODE]
    for x in CONVERTED_PRICE:
        list.append(x)
    FRML_NOTATION = [p.firstChild.wholeText for p in doc_contract.getElementsByTagName("FRML_NOTATION") if
                     p.firstChild.nodeType == p.TEXT_NODE]
    for x in FRML_NOTATION:
        list.append(x)
    DEMAND_LOCATION = [p.firstChild.wholeText for p in doc_contract.getElementsByTagName("DEMAND_LOCATION") if
                       p.firstChild.nodeType == p.TEXT_NODE]
    for x in DEMAND_LOCATION:
        list.append(x)
    DEMAND_LOCATION_DESC = [p.firstChild.wholeText for p in
                            doc_contract.getElementsByTagName("DEMAND_LOCATION_DESC") if
                            p.firstChild.nodeType == p.TEXT_NODE]
    for x in DEMAND_LOCATION_DESC:
        list.append(x)
    DEMAND_LOC_STATUS = [p.firstChild.wholeText for p in doc_contract.getElementsByTagName("DEMAND_LOC_STATUS") if
                         p.firstChild.nodeType == p.TEXT_NODE]
    for x in DEMAND_LOC_STATUS:
        list.append(x)
    DELIVERY_LOCATION = [p.firstChild.wholeText for p in doc_contract.getElementsByTagName("DELIVERY_LOCATION") if
                         p.firstChild.nodeType == p.TEXT_NODE]
    for x in DELIVERY_LOCATION:
        list.append(x)
    DELIVERY_LOCATION_DESC = [p.firstChild.wholeText for p in
                              doc_contract.getElementsByTagName("DELIVERY_LOCATION_DESC") if
                              p.firstChild.nodeType == p.TEXT_NODE]
    for x in DELIVERY_LOCATION_DESC:
        list.append(x)
    DELIVERY_TERMS = [p.firstChild.wholeText for p in doc_contract.getElementsByTagName("DELIVERY_TERMS") if
                      p.firstChild.nodeType == p.TEXT_NODE]
    for x in DELIVERY_TERMS:
        list.append(x)
    PRODUCT_LOCATION = [p.firstChild.wholeText for p in doc_contract.getElementsByTagName("PRODUCT_LOCATION") if
                        p.firstChild.nodeType == p.TEXT_NODE]
    for x in PRODUCT_LOCATION:
        list.append(x)
    PRODUCT_LOCATION_DESC = [p.firstChild.wholeText for p in
                             doc_contract.getElementsByTagName("PRODUCT_LOCATION_DESC") if
                             p.firstChild.nodeType == p.TEXT_NODE]
    for x in PRODUCT_LOCATION_DESC:
        list.append(x)
    INCOTERM = [p.firstChild.wholeText for p in doc_contract.getElementsByTagName("INCOTERM") if
                p.firstChild.nodeType == p.TEXT_NODE]
    for x in INCOTERM:
        list.append(x)
    INCOTERM_LOCATION = [p.firstChild.wholeText for p in doc_contract.getElementsByTagName("INCOTERM_LOCATION") if
                         p.firstChild.nodeType == p.TEXT_NODE]
    for x in INCOTERM_LOCATION:
        list.append(x)
    DISPATCH_TYPE = [p.firstChild.wholeText for p in doc_contract.getElementsByTagName("DISPATCH_TYPE") if
                     p.firstChild.nodeType == p.TEXT_NODE]
    for x in DISPATCH_TYPE:
        list.append(x)
    PAYMENT_TERMS = [p.firstChild.wholeText for p in doc_contract.getElementsByTagName("PAYMENT_TERMS") if
                     p.firstChild.nodeType == p.TEXT_NODE]
    for x in PAYMENT_TERMS:
        list.append(x)
    INVOICING_PARTY = [p.firstChild.wholeText for p in doc_contract.getElementsByTagName("INVOICING_PARTY") if
                       p.firstChild.nodeType == p.TEXT_NODE]
    for x in INVOICING_PARTY:
        list.append(x)
    INVOICING_PARTY_DESCR = [p.firstChild.wholeText for p in
                             doc_contract.getElementsByTagName("INVOICING_PARTY_DESCR") if
                             p.firstChild.nodeType == p.TEXT_NODE]
    for x in INVOICING_PARTY_DESCR:
        list.append(x)
    QUOTA = [p.firstChild.wholeText for p in doc_contract.getElementsByTagName("QUOTA") if
             p.firstChild.nodeType == p.TEXT_NODE]
    for x in QUOTA:
        list.append(x)

    print(list)

    column_name = ['CONTRACT_NO', 'CURRENCY_HEAD', 'SUPPLIER', 'SUPPLIER_NAME', 'ORDER_DATE', 'PRINT_DATE', 'VER_NO',
                   'ACTIVITY_TEXT', 'PURCHASER_NAME', 'DEPARTMENT', 'TELEPHONE', 'EMAIL', 'PRODUCT', 'DESCRIPTION',
                   'PRICE_TYPE', 'PRICE_UNIT_ITEM', 'PRICE_UOM', 'NET_PRICE', 'ITEM_CURRENCY', 'TYPE', 'VALIDITY_START',
                   'VALIDITY_END', 'VALUE', 'CURRENCY_COND', 'PRICE_UNIT_COND', 'PRICE_UOM_COND', 'DOC_CURR',
                   'CONVERTED_PRICE', 'FRML_NOTATION', 'DEMAND_LOCATION', 'DEMAND_LOCATION_DESC', 'DEMAND_LOC_STATUS',
                   'DELIVERY_LOCATION', 'DELIVERY_LOCATION_DESC', 'DELIVERY_TERMS', 'PRODUCT_LOCATION',
                   'PRODUCT_LOCATION_DESC', 'INCOTERM', 'INCOTERM_LOCATION', 'DISPATCH_TYPE', 'PAYMENT_TERMS',
                   'INVOICING_PARTY', 'INVOICING_PARTY_DESCR', 'QUOTA']
    xml_df = pd.DataFrame(list, columns=column_name)
    xml_df.to_excel(path+"output.xlsx", sheet_name="")
    print(xml_df)



# if __name__ == "__main__":
#     xml_path = 'C://Users//lli//Desktop//XML'  # 改为自己的xml路径
#     xml_df = xml_to_excel(xml_path)
#     print(xml_df)
#     xml_df.to_csv('C://Users//lli//Desktop//XML//labels.csv', index=None)  # 改为自己csv存储路径
#     print('Successfully converted xml to csv.')

