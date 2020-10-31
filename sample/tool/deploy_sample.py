#!/usr/bin/python3

import json

# miner node
from web3 import Web3
w3 = Web3(Web3.HTTPProvider("https://ropsten.infura.io/v3/99a79f80961b4db7aab7c9f54375eda7", {"timeout": 30}))


# account
fp = open('../../keystore/UTC--2019-07-20T04-00-01.800933268Z--a9535b10ee96b4a03269d0e0def417af97477fd6', 'r')
fj  = json.load(fp)
pk  = w3.eth.account.decrypt(fj, '123456')
acc = w3.eth.account.privateKeyToAccount(pk)


# building file info
fp = open("../build/contracts/Sample.json", 'r')
fj = json.load(fp)
bc = fj['bytecode']
dbc = fj["deployedBytecode"]
abi = fj["abi"]

# transaction
contr = w3.eth.contract(abi=abi, bytecode=bc, bytecode_runtime=dbc)
cst = contr.constructor()
contx = cst.buildTransaction({
    "from": acc.address,
    "gas": 1000000,
    "gasPrice": 10000000000,
    "nonce": w3.eth.getTransactionCount(acc.address)
    })

# sign and send transaction
raw_tx = acc.signTransaction(contx)
tx_hash = w3.eth.sendRawTransaction(raw_tx["rawTransaction"])

print(str(w3.toHex(tx_hash)))
