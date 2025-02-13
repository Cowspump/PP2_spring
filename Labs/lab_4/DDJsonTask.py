import json


print("""Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------      --------  ------""")

with open("DEsimpData.json", "r") as file:

    data = json.load(file)

    for i in data['imdata']:

        dn = i['l1PhysIf']['attributes']['dn']
        descr = i['l1PhysIf']['attributes']['descr']
        speed = i['l1PhysIf']['attributes']['speed']
        mtu = i['l1PhysIf']['attributes']['mtu']


        print(dn,'\t' ,descr, '   ' * 8, speed,"  ", mtu)


