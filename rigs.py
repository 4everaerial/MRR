import requests
import json

def get_rigs(type):
    rig_dict ={"ID":[], "Price":[]}
    url_rigs = f'https://www.miningrigrentals.com/api/v2/rig?type={type}&minhours.max=3&count=25'
    r = requests.get(url_rigs)
    rigs = json.loads(r.content)

    for records in rigs['data']['records']:
        if float(records['price']['ETH']['price']) > 0 and int(records['device_ram']) > 4:
            rig_dict['ID'] = (records['id'])
            rig_dict['Price'] = (float(records['price']['ETH']['price']))
            break
    return rig_dict


