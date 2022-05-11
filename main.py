from http import client
import os
from art import logo
print(logo)
clients_bids = {}

opt = True
while opt:
    name = input("enter your name: ")
    bid = int(input("enter your bid: $"))
    clients_bids[name] = bid
    other_bid = input("anyone else wants to bid?: ")
    if other_bid == "yes":
        #clear the console
        os.system("cls")
    elif other_bid == "no":     
        opt = False

price = 0
winer = ""
for k in clients_bids:
    if clients_bids[k] > price:
        price = clients_bids[k]
        winer = k
print(f"the winer is {winer} with the bid of {price}$")



