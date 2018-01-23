import os
import pretend  # pip install pretend

from zeep import Client
from zeep.transports import Transport

client = Client('wsdl/login.wsdl')
result = client.service.Login({"Username": os.getenv("USER"), "Password": os.getenv("PASS")})
token = result['LoginResult']

# Replace YOUR-WSDL and OPERATION_NAME with the wsdl url
# and the method name you are calling. The response
# needs to be set in the content=""" """ var.

client = Client('wsdl/inventory.wsdl', strict=False)
response = pretend.stub(
    status_code=200,
    headers={},
    content="""
        <s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">
    <s:Body>
        <GetAllProductsFilteredResponse xmlns="http://tempuri.org/">
            <GetAllProductsFilteredResult xmlns:a="http://schemas.datacontract.org/2004/07/PresentationModel.Circuits"
                                          xmlns:i="http://www.w3.org/2001/XMLSchema-instance">
                <a:Product z:Id="i1" xmlns:z="http://schemas.microsoft.com/2003/10/Serialization/">
                    <Errors i:nil="true" xmlns="http://schemas.datacontract.org/2004/07/PresentationModel"/>
                    <HasErrors xmlns="http://schemas.datacontract.org/2004/07/PresentationModel">false</HasErrors>
                    <Id xmlns="http://schemas.datacontract.org/2004/07/PresentationModel">2001</Id>
                    <RowVersion xmlns="http://schemas.datacontract.org/2004/07/PresentationModel">2016-06-08T15:46:27</RowVersion>
                    <a:AliasProduct/>
                    <a:Circuits i:nil="true"/>
                    <a:ColorValue xmlns:b="http://schemas.datacontract.org/2004/07/System.Drawing">
                        <b:knownColor>0</b:knownColor>
                        <b:name i:nil="true"/>
                        <b:state>0</b:state>
                        <b:value>0</b:value>
                    </a:ColorValue>
                    <a:ContId/>
                    <a:CreateSubCircuits/>
                    <a:Description>LP</a:Description>
                    <a:Domain i:nil="true" xmlns:b="http://schemas.datacontract.org/2004/07/PresentationModel.Domain"/>
                    <a:DomainId i:nil="true"/>
                    <a:FiberLossPerMeter i:nil="true"/>
                    <a:GroupId/>
                    <a:MaterialTypes i:nil="true"
                                     xmlns:b="http://schemas.datacontract.org/2004/07/PresentationModel.Warehouse"/>
                    <a:Name>LP</a:Name>
                    <a:ProductLines>INFRA</a:ProductLines>
                    <a:Report>NO</a:Report>
                    <a:Speed i:nil="true"/>
                    <a:SpeedId i:nil="true"/>
                </a:Product>
            </GetAllProductsFilteredResult>
            <pager xmlns:a="http://schemas.datacontract.org/2004/07/PresentationModel.DatabaseFilter"
                   xmlns:i="http://www.w3.org/2001/XMLSchema-instance">
                <a:Descending>false</a:Descending>
                <a:ElementsRead>1</a:ElementsRead>
                <a:NumberOfElements>100</a:NumberOfElements>
                <a:OrderByProperty i:nil="true"/>
                <a:StartElement>0</a:StartElement>
            </pager>
        </GetAllProductsFilteredResponse>
    </s:Body>
</s:Envelope>
    """)

operation = client.service._binding._operations['GetAllProductsFiltered']
result = client.service._binding.process_reply(
    client, operation, response)
print("***")
print(result)

"""
>>>
{
    'GetAllProductsFilteredResult': {
        'Product': [
            {
                'AliasProduct': None,
                'Circuits': None,
                'ColorValue': None,
                'ContId': None,
                'CreateSubCircuits': None,
                'Description': None,
                'Domain': None,
                'DomainId': None,
                'FiberLossPerMeter': None,
                'GroupId': None,
                'MaterialTypes': None,
                'Name': None,
                'ProductLines': None,
                'Report': None,
                'Speed': None,
                'SpeedId': None,
                '_raw_elements': deque([<Element {http://schemas.datacontract.org/2004/07/PresentationModel}Errors at 0x1061f5708>, <Element {http://schemas.datacontract.org/2004/07/PresentationModel}HasErrors at 0x1061f5808>, <Element {http://schemas.datacontract.org/2004/07/PresentationModel}Id at 0x1061f5888>, <Element {http://schemas.datacontract.org/2004/07/PresentationModel}RowVersion at 0x1061f58c8>, <Element {http://schemas.datacontract.org/2004/07/PresentationModel.Circuits}AliasProduct at 0x1061f5908>, <Element {http://schemas.datacontract.org/2004/07/PresentationModel.Circuits}Circuits at 0x1061f5948>, <Element {http://schemas.datacontract.org/2004/07/PresentationModel.Circuits}ColorValue at 0x1061f5988>, <Element {http://schemas.datacontract.org/2004/07/PresentationModel.Circuits}ContId at 0x1061f59c8>, <Element {http://schemas.datacontract.org/2004/07/PresentationModel.Circuits}CreateSubCircuits at 0x1061f5a08>, <Element {http://schemas.datacontract.org/2004/07/PresentationModel.Circuits}Description at 0x1061f5a48>, <Element {http://schemas.datacontract.org/2004/07/PresentationModel.Circuits}Domain at 0x1061f5a88>, <Element {http://schemas.datacontract.org/2004/07/PresentationModel.Circuits}DomainId at 0x1061f5ac8>, <Element {http://schemas.datacontract.org/2004/07/PresentationModel.Circuits}FiberLossPerMeter at 0x1061f5b08>, <Element {http://schemas.datacontract.org/2004/07/PresentationModel.Circuits}GroupId at 0x1061f5b48>, <Element {http://schemas.datacontract.org/2004/07/PresentationModel.Circuits}MaterialTypes at 0x1061f5b88>, <Element {http://schemas.datacontract.org/2004/07/PresentationModel.Circuits}Name at 0x1061f5bc8>, <Element {http://schemas.datacontract.org/2004/07/PresentationModel.Circuits}ProductLines at 0x1061f5c08>, <Element {http://schemas.datacontract.org/2004/07/PresentationModel.Circuits}Report at 0x1061f5c48>, <Element {http://schemas.datacontract.org/2004/07/PresentationModel.Circuits}Speed at 0x1061f5c88>, <Element {http://schemas.datacontract.org/2004/07/PresentationModel.Circuits}SpeedId at 0x1061f5cc8>])
            }
        ]
    },
    'pager': {
        'Descending': False,
        'ElementsRead': 1,
        'NumberOfElements': 100,
        'OrderByProperty': None,
        'StartElement': 0
    }
}
"""