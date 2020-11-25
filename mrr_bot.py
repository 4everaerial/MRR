import eth_mrr, etc_mrr
import threading

x = int(input("Select 1 for ETH, 2 for ETC, or 3 for Both: "))

value = True
while (value):
    if x == 1:
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