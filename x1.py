import xml.etree.ElementTree as ET
# mytree = ET.parse('xml_sample.xml')
# myroot = mytree.getroot()
# # print(myroot)
# #
# # print(myroot.tag, myroot.attrib)
# # print(myroot[0].tag)
# #
# # # trying to access the first food record
# # for x in myroot[0]:
# #     print(x.tag, x.attrib)
# #
# # for x in myroot[0]:
# #     print(x.text)
#
# for x in myroot.findall('food'):
#     item = x.find('item').text
#     price = x.find('price').text
#     description = x.find('description').text
#     calories = x.find('calories').text
#     print(item, price)
#
# # getting the "description" attribute text from the
# # first food record
# print(myroot[0].findtext('description'))

XMLexample_stored_in_a_string ='''<?xml version ="1.0"?>
<States>
    <state name ="TELANGANA">
        <rank>1</rank>
        <neighbor name ="ANDHRA" language ="Telugu"/>
        <neighbor name ="KARNATAKA" language ="Kannada"/>
    </state>
    <state name ="GUJARAT">
        <rank>2</rank>
        <neighbor name ="RAJASTHAN" direction ="N"/>
        <neighbor name ="MADHYA PRADESH" direction ="E"/>
    </state>
    <state name ="KERALA">
        <rank>3</rank>
        <neighbor name ="TAMILNADU" direction ="S" language ="Tamil"/>
    </state>
</States>
'''

root = ET.fromstring(XMLexample_stored_in_a_string)
for neighbor in root.iter('neighbor'):
    print(neighbor.attrib)

for state in root.findall('state'):
    rank = state.find('rank').text
    name = state.get('name')

    print(rank, name)