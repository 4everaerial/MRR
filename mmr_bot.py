import eth_mrr, etc_mrr

x = int(input("Select 1 for ETH, 2 for ETC, or 3 for Both: "))

value = True
while (value):
    if x == 1:
       eth_mrr.eth_bot()
    elif x == 2:
        etc_mrr.etc_bot()
    elif x == 3:
        #this is not yet working...need to parallel
        eth_mrr.eth_bot()
        etc_mrr.etc_bot()
    else:
        Print("Invalid selection....please restart!")
        break