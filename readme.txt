install python3
pip3 install netmiko

devices.yaml
- device_type: cisco_xr
  host: sandbox-iosxr-1.cisco.com
  username: admin
  password: C1sco12345
  secret: cisco
  timeout: 10
  #fast_cli: true