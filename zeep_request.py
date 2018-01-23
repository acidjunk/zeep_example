import os

from lxml import etree
from zeep import Client

client = Client('wsdl/login.wsdl')
result = client.service.Login({"Username": os.getenv("USER"), "Password": os.getenv("PASS")})
token = result['LoginResult']

client = Client('wsdl/inventory.wsdl', strict=False)

array_of_filter_field = [{"FilterField": {"Name": "Name", "SelectedOperator": "OperationEquals", "Value": "LP"}}]
filter = {"Filters": array_of_filter_field}
pager = {"StartElement": 0, "Descending": False, "NumberOfElements": 10,
         "OrderByProperty": None}

node = client.create_message(client.service, 'GetAllProductsFiltered', pager=pager, filter=filter, sessionToken=token)
print("********")
print(etree.tostring(node, pretty_print=True))

"""
>>>
b'<soap-env:Envelope xmlns:soap-env="http://schemas.xmlsoap.org/soap/envelope/">\n  <soap-env:Header xmlns:wsa="http://www.w3.org/2005/08/addressing">\n    <wsa:Action>http://tempuri.org/IInventoryService/GetAllProductsFiltered</wsa:Action>\n    <wsa:MessageID>urn:uuid:561120a3-9d97-4556-afc4-55cff9be79d6</wsa:MessageID>\n    <wsa:To>http://ims.surfnet.nl:8095/Inventory/iInventoryHttp</wsa:To>\n  </soap-env:Header>\n  <soap-env:Body>\n    <ns0:GetAllProductsFiltered xmlns:ns0="http://tempuri.org/">\n      <ns0:pager>\n        <ns1:Descending xmlns:ns1="http://schemas.datacontract.org/2004/07/PresentationModel.DatabaseFilter">false</ns1:Descending>\n        <ns2:NumberOfElements xmlns:ns2="http://schemas.datacontract.org/2004/07/PresentationModel.DatabaseFilter">10</ns2:NumberOfElements>\n        <ns3:StartElement xmlns:ns3="http://schemas.datacontract.org/2004/07/PresentationModel.DatabaseFilter">0</ns3:StartElement>\n      </ns0:pager>\n      <ns0:filter>\n        <ns4:Filters xmlns:ns4="http://schemas.datacontract.org/2004/07/PresentationModel.DatabaseFilter">\n          <ns4:FilterField>\n            <ns4:Name>Name</ns4:Name>\n            <ns4:SelectedOperator>OperationEquals</ns4:SelectedOperator>\n            <ns4:Value>LP</ns4:Value>\n          </ns4:FilterField>\n        </ns4:Filters>\n      </ns0:filter>\n      <ns0:sessionToken>a9867af3-c0f5-46a9-99c3-c489fd208cf0</ns0:sessionToken>\n    </ns0:GetAllProductsFiltered>\n  </soap-env:Body>\n</soap-env:Envelope>\n'
"""