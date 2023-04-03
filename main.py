#Code uses python language, by Lucas, email: lucas.yeo69@gmail.com
#This code scans the network is 3 different modes,the 4th option is using all 3 modes at once.
import nmap3
import nmap
import datetime
nmScan = nmap.PortScanner()
nm = nmap3.Nmap()
now = datetime.datetime.now()
x = input("Enter network/device you want to scan for: ")
def istrue(x): #checks if input is a valid ip address
    """_summary_

    Args:
        x (): ip address of device/network
    """
    try:
        ip_object = ipaddress.ip_address(x)
    except ValueError:
        print("Not valid ip address")
        x = input("Pls input again: ")
        istrue(x)
istrue(x)
time = (now.strftime("%Y-%m-%d %H%M"))
bdict={
    
}
o = ("-------------------------------------------------------------------\n")
separate=("---------------------\n")
nmScan.scan(x)
results = nm.nmap_os_detection(x) #output of os scan of network/device
def os(scantype,writingtype): # scans network and returns os name and cpe with device name
    """_summary_

    Args:
        scantype (): type of scan (e.g. ping, os or all)
        writingtype (): 'w' or 'a' to write to a file
    """
    filename = scantype+'_'+time+'.txt'
    file1 = open(filename, writingtype)
    for host in nmScan.all_hosts(): 
        L=('Device :'+host+'\n') 
        file1.writelines(o)
        file1.writelines(L)
        file1.writelines(separate)
        osstart = ("--OS Matches--\n")
        file1.writelines(osstart)
        osstats = results[host]["osmatch"]
        for i in list(osstats):
            a = i["accuracy"]
            q=i["name"]
            if "cpe" in i:
                v = i["cpe"]
            else:
                v="cpe:[NONE]"
            file1.writelines("os name:"+q+"   (accuracy:"+a+")\n")
            file1.writelines(v+"\n")
    print("The output is in "+filename)
def ports(scantype, writingtype): #scans network and returns ports with device name
    """_summary_

    Args:
        scantype (): type of scan(os,ports or all)
        writingtype (   ): 'w' or 'a' to write to file
    """
    filename = scantype+'_'+time+'.txt'
    print(filename)
    file1 = open(filename, writingtype)
    for host in nmScan.all_hosts():
        file1.writelines(o)
        d=("Service:Port")
        L=('Device :'+host+'\n') 
        file1.writelines(L)
        file1.writelines(separate)
        file1.writelines(d+"\n")
        file1.writelines(separate)
        for proto in nmScan[host].all_protocols():
            lport = nmScan[host][proto].keys()
            nport = nmScan[host][proto]
            for i in nport:
                a=nport[i]['name']
                bdict[i]=a
            for port in lport:
                p=(bdict[port]+':'+ str(port)+'\n' )
                file1.writelines(p)
            file1.writelines(separate)
    print("The output is in "+filename)
def choice():
    y = input("Ping,scan OS, scan ports, or all: ")
    if y == "os" or y== "OS" or y == "scan os" or y == "scan OS":
        os("OS",'w')
    elif y == "ports" or y == "Port" or y== "scan port" or y== "Scan Port":
        ports("Ports",'w')
    elif y == "all" or y == "All":
        ports("All",'a')
        os("All",'a')
    elif y == "ping" or y == "Ping":
        scantype = "Ping"
        filename = scantype+'_'+time+'.txt'
        file1 = open(filename, 'w')
        for host in nmScan.all_hosts():
            L=('Device :'+host+'\n') 
            file1.writelines(L)
        print("The output is in "+filename)
    else:
        print("-Please input again-")
        choice()
choice()
print("--DONE--")




