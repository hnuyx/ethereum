
from ether_node import EtherNode
from eth_account.messages import encode_defunct
import web3

ETH_NODE_HTTP = "https://ropsten.infura.io/v3/99a79f80961b4db7aab7c9f54375eda7"

tmjson = "/home/henry/learning/git/yw/match-hydro/build/contracts/YouMatch.json"
hdjson = "/home/henry/learning/git/yw/match-hydro/build/contracts/HybridExchange.json"
proxyjson = "/home/henry/learning/git/yw/match-hydro/build/contracts/Proxy.json"
tptjson = "../build/contracts/TPToken.json"

#qts = ["0x6C3118c39FAB22caF3f9910cd054F8ea435B5FFB",
#       "0xe898663A2CbDf7a371bB4B6a5dd7aC93d4505C9a",
#       "0xEAB3A69a992aeC845099717B148DC1995DD57685",
#       "0x2e01154391F7dcBf215c77DBd7fF3026Ea7514ce"]

#qts = ["0xa6E566f17aDB55861cd06E57c1Be8F5853EE16BE",
#       "0x2e9372C90c4646Ef04cF4a63A7D0685b0aA6d889",
#       "0x5fe84E79b54266F1B6BB66cfADAB4c79532b9F98",
#       "0x1ad0011C7EEC14590603BFcb17f0a3C9F517DB46"]

qts = ["0x8e4d8D520f52B044e1E8B054D763B723B7C3E716",
       "0x45e110F81bBf89041A63Bc2403058743bc552bAF",
       "0x7B29ed69368B0Ed0d3b21A857BaEeF788B13c626",
       "0x60423Ebc63245631Ea71bdF58CF23A3949329cDb"]

proxyaddr = "0x6BeE8B8a06F2Df4c3e3BE7E6ca8E489602378186"
hdaddr = "0xbc6B59f5a1e86F262Ae92A81aE1c44F401521577"
ymaddr = "0x950b5C568c46B1abcDC21F7348d9F29B7c64462a" 

ownerfile = "./keystore/UTC--2019-07-20T04-00-01.800933268Z--a9535b10ee96b4a03269d0e0def417af97477fd6"

# get ether node
enode = EtherNode(ETH_NODE_HTTP)

# decrype keystore file
acc = enode.decrypt_keystore(ownerfile, "123456")
print("acc address:", acc.address)
relayer = acc
print("relayer address:", relayer.address)

# get contract
proxy = enode.get_contract(proxyaddr, proxyjson)
hd = enode.get_contract(hdaddr, hdjson)
tm = enode.get_contract(ymaddr, tmjson)

APPROVE_VALUE =  10 ** 27

# approve
for qt in qts:
    print("approve proxy for token:", qt)
    qtoken = enode.get_contract(qt, tptjson)
    enode.call_func(acc, qtoken.functions.approve(proxy.address, APPROVE_VALUE), True)

# check approve
for qt in qts:
    print("check approve proxy for token:", qt)
    qtoken = enode.get_contract(qt, tptjson)
    aq = qtoken.functions.allowance(relayer.address, proxy.address).call()
    print("relayer quote token appove:", aq)


