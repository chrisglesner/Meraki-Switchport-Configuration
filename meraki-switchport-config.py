import meraki
import json

if __name__ == '__main__':
    api_key = 'YOUR API KEY'
    dashboard = meraki.DashboardAPI(api_key)
  
    for switchport in [*range(1,49)]: #Change Range Command for Your Desired Interfaces
        response = dashboard.switch.updateDeviceSwitchPort(serial='YOUR SERIAL NUMBER OF SWITCH', portId=switchport, name='Data', type='access', vlan=100)

        with open('DIRECTORY WHERE YOUR LOGGING FILE EXISTS', 'a') as my_file:
            data = json.dumps(response, indent=4)
            my_file.write(data)
