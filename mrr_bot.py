import eth_mrr, etc_mrr, rental
import threading

x = int(input("Select 1 for ETH, 2 for ETC, or 3 for Both: "))
coin = 'ETH'
value = True
while (value):
    acct_balance = rental.get_balance(coin)
    print(print(coin, " = ",acct_balance))
    rental_hash = rental.get_rental_hash()
    print("Rented Hash : " + str(rental_hash[0]))
    if rental_hash[0] > 0:
        avg_rent_price = rental_hash[1] / rental_hash[0] * 8
        print("AVG Rental Price : " + str('%f10' % avg_rent_price))
    elif x == 1:
       eth_mrr.eth_bot()
    elif x == 2:
        etc_mrr.etc_bot()
    elif x == 3:
        if __name__ == '__main__':
            t1 = threading.Thread(target=eth_mrr.eth_bot)
            t2 = threading.Thread(target=etc_mrr.etc_bot)
            t1.start()
            t2.start()
            t1.join()
            t2.join()
    else:
        Print("Invalid selection....please restart!")
        break