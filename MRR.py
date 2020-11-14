import requests
import json
import time
import rigs


type = "hashimotos"
coin = "eth"
url_ms = f'https://api.minerstat.com/v2/coins?list={coin}'
url_mmr = f'https://www.miningrigrentals.com/api/v2/info/algos/hashimotos?currency={coin}'
value = True
while (value):

    r = requests.get(url_ms)
    minerstat = json.loads(r.content)
    minerstat_reward = float(minerstat[0]['reward'] * 24 * 1000000)
    print("Rewards per 1mh/day = " + str('%f10' % minerstat_reward))
#    print('%f10' % minerstat_reward)

    r = requests.get(url_mmr)
    mmr = json.loads(r.content)
    mmr_reward = float(mmr['data']['stats']['prices']['last_10']['amount'])
    print(f"MRR avg cost in {coin} = " + str('%f10' % mmr_reward))
#    print('%f10' % mmr_reward)

    diff = minerstat_reward - mmr_reward
    print("Difference = " + str('%f10' % diff))

    profit = diff / mmr_reward
    print("Potential Profit = " + str(int(profit *100)) + "%" )


    if minerstat_reward > mmr_reward:
        print("Good time to rent!")
    else:
        print("Bad time to rent!")

    rig_dict = rigs.get_rigs(type)
    print(rig_dict)

    time.sleep(300)
