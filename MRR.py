import requests
import json
import time
import rigs, rental


rental_cap = 4000
type = "hashimotos"
coin = "eth"
url_ms = f'https://api.minerstat.com/v2/coins?list={coin}'

value = True
while (value):
    try:
        r = requests.get(url_ms)
        minerstat = json.loads(r.content)
        minerstat_reward = float(minerstat[0]['reward'] * 24 * 1000000)
#        print("Rewards per 1mh/day = " + str('%f10' % minerstat_reward))

        rig_dict = rigs.get_rigs(type)

        diff = minerstat_reward - float(rig_dict['Price'])
#        print("Difference = " + str('%f10' % diff))

        profit = diff / float(rig_dict['Price'])

        rental_hash = rental.get_rental_hash()

        if minerstat_reward > rig_dict['Price'] * 1.03 and rental_hash < rental_cap:
            print("Good time to rent ETH!")
            print("Potential Profit = " + str(int(profit * 100)) + "%")
            rent_id = rig_dict["ID"]
            rent_price = rig_dict['Price'] + 0.00000001
            rental.rent_rig(rent_id, rent_price)
            print("Rig " + str(rent_id) + " Rented")
            time.sleep(240)
        else:
            print("Bad time to rent ETH!")
            print("Potential Profit = " + str(int(profit * 100)) + "%")
#            etc_mrr.etc_bot()

        print("Rented Hash : " + str(rental_hash))
        time.sleep(60)
    except:
        print("Error detected")
        time.sleep(300)