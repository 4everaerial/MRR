import requests
import json

def get_rigs(type):
    rig_dict ={}
    url_rigs = f'https://www.miningrigrentals.com/api/v2/rig?type={type}&minhours.max=3&count=5'

    r = requests.get(url_rigs)
    rigs = json.loads(r.content)

    #with open('rigs1.txt', 'w') as outfile:
    #    json.dump(rigs, outfile, indent=4)

    #print(type(rigs['data']['records']))

    for records in rigs['data']['records']:
        rig_dict.update({(records['id']) : (records['price']['ETH']['price'])})
    return rig_dict


