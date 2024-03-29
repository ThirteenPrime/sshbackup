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
    # except Exception as error:
    #    print(error)


def writetofile(inputtext='', hostname='CI', outputextension='txt'):
    '''
    writetofile(inputtext='inputstring', hostname='CI', outputextension='txt')
    '''
    datenow = datetime.datetime.now().strftime("%Y-%m-%d")
    outputfile = f'{hostname}-{datenow}.{outputextension}'
    text_file = open(outputfile, "wt")
    text_file.write(inputtext)
    text_file.close()
    print(f'writing file:{outputfile}')
    pass


# run command
command = 'show running-config'
#  username: admin
#  password: C1sco12345
#  secret: cisco


def getcredentials_todict():
    username = input('username: ')
    password = getpass.getpass('password: ')
    secretpass = getpass.getpass('secret password: ')
    result = {'username': username,
              'password': password, 'secret': secretpass}
    return result


credentialsdict = getcredentials_todict()
failed_devices = []
with open("devices.yaml") as f:
    devices = yaml.safe_load(f)
for device in devices:
    device = {**device, **credentialsdict}
    result = send_show_command(device, command)
    # result commands = {'command':'output'}
    if result:
        writetofile(result, device['host'])
    else:
        failed_devices.append(device)
print(f'failed devices:')
#print(x['host'] for x in failed_devices)
for x in failed_devices:
    print(x['host'])
