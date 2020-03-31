
from ether_node import EtherNode
from eth_account.messages import encode_defunct
import web3

ETH_NODE_HTTP = "https://ropsten.infura.io/v3/99a79f80961b4db7aab7c9f54375eda7"

ymjson = "/home/henry/learning/git/yw/match-hydro/build/contracts/YouMatch.json"
hdjson = "/home/henry/learning/git/yw/match-hydro/build/contracts/HybridExchange.json"
proxyjson = "/home/henry/learning/git/yw/match-hydro/build/contracts/Proxy.json"
tptjson = "../build/contracts/TPToken.json"

qts = ["0x6C3118c39FAB22caF3f9910cd054F8ea435B5FFB",
       "0xe898663A2CbDf7a371bB4B6a5dd7aC93d4505C9a",
       "0xEAB3A69a992aeC845099717B148DC1995DD57685",
       "0x2e01154391F7dcBf215c77DBd7fF3026Ea7514ce"]

proxyaddr = "0x6BeE8B8a06F2Df4c3e3BE7E6ca8E489602378186"
hdaddr = "0xbc6B59f5a1e86F262Ae92A81aE1c44F401521577"
ymaddr = "0x950b5C568c46B1abcDC21F7348d9F29B7c64462a" 

ownerfile = "./keystore/UTC--2019-07-20T04-00-01.800933268Z--a9535b10ee96b4a03269d0e0def417af97477fd6"

# get ether node
enode = EtherNode(ETH_NODE_HTTP)

# decrype keystore file
acc = enode.decrypt_keystore(ownerfile, None)
print("acc address:", acc.address)
print("relayer address:", acc.address)

# get contract
proxy = enode.get_contract(proxyaddr, proxyjson)
hd = enode.get_contract(hdaddr, hdjson)
ym = enode.get_contract(ymaddr, ymjson)

APPROVE_VALUE =  10 ** 27

################### approve for proxy ##############start

#for qt in qts:
#    print("approve proxy for token:", qt)
#    qtoken = enode.get_contract(qt, tptjson)
#    enode.call_func(acc, qtoken.functions.approve(proxy.address, APPROVE_VALUE), True)

################### approve for proxy ##############end

################### get order depth   ##############start

btaddr = "0x6C3118c39FAB22caF3f9910cd054F8ea435B5FFB"
qtaddr = "0xe898663A2CbDf7a371bB4B6a5dd7aC93d4505C9a"

btoken = enode.get_contract(btaddr, tptjson)
qtoken = enode.get_contract(qtaddr, tptjson)

sqh, bqh = ym.functions.getBQHash(btaddr, qtaddr).call()
print(sqh.hex(), bqh.hex())
god = ym.functions.getOrderDepth(sqh, bqh)
print(god.buildTransaction())
sql, bql = ym.functions.getOrderDepth(sqh, bqh).call()
print(sql, bql)

################### get order depth   ##############end
