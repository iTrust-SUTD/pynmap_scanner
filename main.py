import nmap3
import json
import nmap
nmScan = nmap.PortScanner()
nm = nmap3.Nmap()
file1 = open('output.txt','w')
results = nm.nmap_os_detection("192.168.1.208")
osstats = results["192.168.1.208"]["osmatch"]
#print(json.dumps(osstats,indent=4))
for i in list(osstats):
    a = i["accuracy"]
    print(a)
    q=i["name"]
    print(q)
    if "cpe" in i:
        v = i["cpe"]
        print(v)
    else:
        v=[]
        print(v)
