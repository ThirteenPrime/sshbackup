import csv


def csvwriteheader(outputfile, headerlist=["Hostname", "Interface", "Interface Description", "Interface Status", "VLAN", "MAC Address", "IP address", "DNS"]):
    with open(f"{outputfile}.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headerlist)
        print(f"creating report file: {outputfile}")


def writetocsv(outputfile, inputlist):
    # hostname=""
    # interface=""
    # intdesc=""
    # intstat=""
    # vlan=""
    # mac=""
    # ipadd=""
    # dnsname=""
    print(f"writing file: {outputfile}")
    with open(f"{outputfile}.csv", 'a', newline='') as file:
        writer = csv.writer(file)
        for x in inputlist:
            writer.writerow(x)
    print(f"writing file: {outputfile} - completed")
    return
