import requests
import json
import time
import rigs, rental



type = "hashimotos"
coin = "eth"
url_ms = f'https://api.minerstat.com/v2/coins?list={coin}'

value = True
while (value):

    r = requests.get(url_ms)
    minerstat = json.loads(r.content)
    minerstat_reward = float(minerstat[0]['reward'] * 24 * 1000000)
    print("Rewards per 1mh/day = " + str('%f10' % minerstat_reward))

    rig_dict = rigs.get_rigs(type)

    diff = minerstat_reward - float(rig_dict['Price'])
    print("Difference = " + str('%f10' % diff))

    profit = diff / float(rig_dict['Price'])



    if minerstat_reward > rig_dict['Price']:
        print("Good time to rent!")
        print("Potential Profit = " + str(int(profit * 100)) + "%")
        rent_id = rig_dict["ID"]
        rent_price = rig_dict['Price']
        rental.rent_rig(rent_id, rent_price)
        print("Rig " + str(rent_id) + "Rented")
#        time.sleep(36000)
    else:
        print("Bad time to rent!")
 #       print(rig_dict)

    time.sleep(300)
