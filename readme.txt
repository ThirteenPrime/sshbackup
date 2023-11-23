install python3
pip3 install netmiko

#run script
python3 backup_py.py -f devices.csv -c commands.txt -d cisco_ios
Optional:
-c commands.txt
-d cisco_ios

devices.csv format:
hostname,device_name
a.b.c.d,output_filename
