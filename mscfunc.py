import platform    # For getting the operating system name
import subprocess  # For executing a shell command
import socket  # DNS function


def iptodns(ipaddstr="8.8.8.8"):
    try:
        return (socket.gethostbyaddr(ipaddstr)[0])
    except:
        return (False)


def writestringtofile(filename, inputdata=[]):
    if inputdata:
        print(f"{filename} - writing")
        with open(f'{filename}', 'w', encoding="utf-8") as f:
            for output in inputdata:
                f.write(output)
            print(f"{filename} - complete")


def ping(host):
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """
    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    # Building the command. Ex: "ping -c 2 google.com"
    command = ['ping', f"{param}", '2', str(host)]
    try:
        subprocess.check_call(
            command, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
        return (host)
    except:
        return False
