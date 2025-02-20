# Using data file sample-data.json, create output that resembles the following by parsing the included JSON file.

# Interface Status
# ================================================================================
# DN                                                 Description           Speed    MTU  
# -------------------------------------------------- --------------------  ------  ------
# topology/pod-1/node-201/sys/phys-[eth1/33]                              inherit   9150 
# topology/pod-1/node-201/sys/phys-[eth1/34]                              inherit   9150 
# topology/pod-1/node-201/sys/phys-[eth1/35]                              inherit   9150 


import json

with open('sample-data.json', 'r') as file:
    data = json.load(file)

print("Interface Status")
print("=" * 80)

print("DN", " " * 47, "Description", " " * 9,"Speed", " " * 2, "MTU")
print("-" * 50, "-" * 20 ,"", "-" * 6 ,"","-" * 6)

for imdata in data["imdata"]:
    for i in imdata:
        for j in imdata[i]:
            print(imdata[i][j]["dn"],"\t\t\t\t", imdata[i][j]["speed"],'', imdata[i][j]["mtu"])
            
    