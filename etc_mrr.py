import requests
import json
import time
import rigs, rental, config


def etc_bot():
    type = "hashimotos"
    coin = "etc"
    rental_cap = 4000
    url_ms = f'https://api.minerstat.com/v2/coins?list={coin}'
    url_binance = f'https://api.binance.com/api/v3/avgPrice?symbol=ETCETH'
    profile = config.pool_profile['ETC']

    try:
        r = requests.get(url_ms)
        minerstat = json.loads(r.content)
        minerstat_reward_etc = float(minerstat[0]['reward'] * 24 * 1000000)

        r = requests.get(url_binance)
        binance_etc = json.loads(r.content)
        etc_eth_price = float(binance_etc['price'])
        eth_rewards = minerstat_reward_etc * etc_eth_price

        rig_dict = rigs.get_rigs(type)

        diff = eth_rewards - float(rig_dict['Price'])

        profit = diff / float(rig_dict['Price'])

        rental_hash = rental.get_rental_hash()

        if eth_rewards > rig_dict['Price'] * 1.02 and rental_hash < rental_cap:
            print("Good time to rent ETC!")
            print("Potential Profit = " + str(int(profit * 100)) + "%")
            rent_id = rig_dict["ID"]
            rent_price = rig_dict['Price'] + 0.00000001
            rental.rent_rig(rent_id, rent_price, profile)
            print("Rig " + str(rent_id) + " Rented")
            time.sleep(240)
        else:
            print("Bad time to rent ETC!")
            print("Potential Profit = " + str(int(profit * 100)) + "%")

        print("Rented Hash : " + str(rental_hash))
        time.sleep(60)
    except:
        print("Error detected")
        time.sleep(300)



