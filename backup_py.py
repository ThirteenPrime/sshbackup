# from netmiko import exceptions
import argparse
import errorfunc
import csv
import mscfunc
from netmiko import ConnectHandler
from getpass import getpass
# import json
import csvfunc
# initialize venv
# windows venv\bin\activate.ps1
# linux source venv/bin/activate
"""
Requires
commands.txt
fsmparser.py
main.py
#"""

parser = argparse.ArgumentParser()
parser.add_argument("-f", required=True, help="devices file .csv format")
parser.add_argument("-d", required=False,
                    help="devices type\ncisco_ios\njuniper_junos", default="cisco_ios")
parser.add_argument("-c", required=False,
                    help="command file list default: show run")
args = parser.parse_args()
# password = getpass()
username = input("username: ")
# username = "admin"
password = getpass()
# password = "C1sco12345"

# devtype = "juniper_junos"
devtype = args.d

# device = {
#    "device_type":"juniper_junos",
#    "host": "junos.google.comasdf",
#    "username": username,
#    "password": password,
#    }


def connect(hostname="junos.google.comasdf", device_type="juniper_junos"):
    # print("*****"+hostname)
    device = {
        "device_type": device_type,
        "host": hostname,
        "username": username,
        "password": password
    }
    try:
        print(f"\nconnecting to {hostname}")
        net_connect = ConnectHandler(**device)
        print(f"{hostname} - connect")
    except:
        print(f"\nconnecting to {hostname}-failed")
        return False
    return net_connect


def sendcommands(net_connect, commands=["show version"]):
    output_data = []
    pipecommands = ""
    # pipecommands=""
    for command in commands:
        try:
            net_connect.send_command("\n")
            output_data.append(net_connect.send_command(
                command+pipecommands+"\n"))
        except:
            print(f"send commands error:sendcommands() - {command}")
    return output_data


def sendcommand(net_connect, command="show version"):
    output_data = ""
    pipecommands = ""
    # pipecommands=""
    try:
        net_connect.send_command("\r")
        print(command+pipecommands)
        output_data = net_connect.send_command(command+pipecommands)
    except:
        print("send commands error:sendcommands()")
    return output_data


# Get list of devices from hostfile
'''
with open('hostfile.txt', 'r') as f:
    hostlist = f.read().splitlines()
# '''


# hostlist
hostlist = []
filename = args.f
# filename = 'devices.csv'
try:
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            hostlist.append(row)
except:
    errorfunc.devicescsv_error(filename)
# connect to device
data = {}
# Command list to run 0-2 list static

filename = args.c
try:
    with open(filename, newline='') as f:
        commandlist = f.read().splitlines()
except:
    commandlist = ["show run"]
# connect to device

outputdata_arptable = {}
for host in hostlist:
    # hostname="sandbox-iosxe-latest-1.cisco.com"
    netconn = connect(host['hostname'], devtype)
    # send commands
    if (netconn):
        outputdata = sendcommand(netconn, f"{commandlist[0]}")
        mscfunc.writestringtofile(host['device_name']+".txt", [outputdata])
        # Disconnect
        netconn.disconnect()
