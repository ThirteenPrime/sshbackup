import datetime
import yaml
import getpass
from netmiko import (
    ConnectHandler,
    NetmikoTimeoutException,
    NetmikoAuthenticationException,
)


def send_show_command(device, command):
    result = ''
    try:
        with ConnectHandler(**device) as ssh:
            ssh.enable()
            # for command in commands:
            result = ssh.send_command(command)
            #result[command] = output
        return result
    except (NetmikoTimeoutException, NetmikoAuthenticationException) as error:
        print(error)


def writetofile(inputtext='', hostname='CI', outputextension='txt'):
    '''
    writetofile(inputtext='inputstring', hostname='CI', outputextension='txt')
    '''
    datenow = datetime.datetime.now().strftime("%Y-%m-%d")
    outputfile = f'{hostname}-{datenow}.{outputextension}'
    text_file = open(outputfile, "wt")
    text_file.write(inputtext)
    text_file.close()
    pass


# run command
command = 'show running-config'
#  username: admin
#  password: C1sco12345
#  secret: cisco
username = input('username: ')
password = getpass.getpass('password: ')
secretpass = getpass.getpass('secret password: ')


with open("devices.yaml") as f:
    devices = yaml.safe_load(f)
for device in devices:
    device['username'] = username
    device['password'] = password
    device['secret'] = secretpass
    result = send_show_command(device, command)
    # result commands = {'command':'output'}
    writetofile(result, device['host'])
