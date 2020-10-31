
from ether_node import EtherNode
from web3 import Web3

ETH_NODE_HTTP = "https://ropsten.infura.io/v3/99a79f80961b4db7aab7c9f54375eda7"
tptjson = "../build/contracts/TPToken.json"

# get ether node
enode = EtherNode(ETH_NODE_HTTP)

ownerfile = "./keystore/UTC--2019-07-20T04-00-01.800933268Z--a9535b10ee96b4a03269d0e0def417af97477fd6"
owner = enode.decrypt_keystore(ownerfile, "123456")

print('owner address', owner.address)
print('owner privatekey', owner.privateKey)

tokens = [
        '0xeD2D84d94Ab8f17ed26482910c8E586613ce9367',
        '0x3e1eb800c06faE1C1722eb3bda0840e28dd8ac28',
        ]

accounts = [
        #'0xdd025fbe7865aa4acbe44b405f5c1cda4c4e1c8b',
        #'0x8e4d8D520f52B044e1E8B054D763B723B7C3E716',
        #'0x45e110F81bBf89041A63Bc2403058743bc552bAF',
        #'0x7B29ed69368B0Ed0d3b21A857BaEeF788B13c626',
        #'0xfc2003889d3430a7d0931b5ade5c7a101356efd7',
        #'0x60423Ebc63245631Ea71bdF58CF23A3949329cDb',
        #'0xc64b9765085c43137a27c3506aeda67ab7112636',
        '0xfc2003889d3430a7d0931b5ade5c7a101356efd7',
        '0xab890808775d51e9bf9fa76f40ee5fff124dece5',
        ]

TRANSFER_VALUE = 10**25

for token in tokens:
    token = Web3.toChecksumAddress(token)
    tc = enode.get_contract(token, tptjson)
    bal = tc.functions.balanceOf(owner.address).call()
    print(bal // (10**18))
    for acc in accounts:
        acc = Web3.toChecksumAddress(acc)
        print('transfer to account', acc)
        enode.call_func(owner, tc.functions.transfer(acc, TRANSFER_VALUE), True)

