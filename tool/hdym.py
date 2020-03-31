
from ether_node import EtherNode
from eth_account.messages import encode_defunct
import web3

ETH_NODE_HTTP = "https://ropsten.infura.io/v3/99a79f80961b4db7aab7c9f54375eda7"

tmjson = "/home/henry/learning/git/yw/match-hydro/build/contracts/YouMatch.json"
hdjson = "/home/henry/learning/git/yw/match-hydro/build/contracts/HybridExchange.json"
proxyjson = "/home/henry/learning/git/yw/match-hydro/build/contracts/Proxy.json"
tptjson = "../build/contracts/TPToken.json"

#tmaddr = "0x597d1B683AA9b54ac9F137Dc6420aED213d7FdB4" 
#btaddr = "0x5c70C92c52B1072F4dDCe647C2590333946e46f3"
#qtaddr = "0xf5b328881db39a497e3a5937F3fE44709069796e"
#relayer = "0xef7bd13F0Cc305A907E1e75B16bc4A7c2F28f073"

proxyaddr = "0x6BeE8B8a06F2Df4c3e3BE7E6ca8E489602378186"
tmaddr = "0x3762fF9389feaE5C7C00aC765C1f0056f9B53eCB" 
hdaddr = "0xC34528755ACBcf1872FeE04c5Cf4BbE112cdafA2"
btaddr = "0x6C3118c39FAB22caF3f9910cd054F8ea435B5FFB"
qtaddr = "0xe898663A2CbDf7a371bB4B6a5dd7aC93d4505C9a"

#relayer = web3.Web3.toChecksumAddress("0x3d9c6c5a7b2b2744870166eac237bd6e366fa3ef")
#relayer = web3.Web3.toChecksumAddress("0xA9535b10EE96b4A03269D0e0DEf417aF97477FD6")


ownerfile = "./keystore/UTC--2019-07-20T04-00-01.800933268Z--a9535b10ee96b4a03269d0e0def417af97477fd6"

# get ether node
enode = EtherNode(ETH_NODE_HTTP)

# decrype keystore file
relayer = enode.decrypt_keystore(ownerfile, "123456")
print("relayer address:", relayer.address)
acc = web3.eth.Eth.account.privateKeyToAccount("279EFAC43AAE9405DCD9A470B9228C1A3C0F2DEFC930AD1D9B764E78D28DB1DF")
print("acc address:", acc.address)

# get contract
tm = enode.get_contract(tmaddr, tmjson)
hd = enode.get_contract(hdaddr, hdjson)
proxy = enode.get_contract(proxyaddr, proxyjson)


# get btaddr, qtaddr
btoken = enode.get_contract(btaddr, tptjson)
qtoken = enode.get_contract(qtaddr, tptjson)

'''
# get configure data
#data = tm.functions.getConfigData(False).call()
data = 0x020000005ffb17bc000000000000000000000000000000000000000000000000
data = data.to_bytes(32, 'big')
print("data:", data.hex())

signature = [data, data, data]
# order param
odparam = [acc.address, 1, 1, 0, data, signature]
# order set
odset = [btaddr, qtaddr, relayer] 

#print(odparam, odset)
# get bqod hash
bqhash, odhash = tm.functions.getBQODHash(odparam, odset).call()
print("bq-od:", bqhash.hex(), odhash.hex())

msghash = encode_defunct(hexstr=odhash.hex())
stx = acc.sign_message(msghash)
v = stx['v']
r = stx['r']
s = stx['s']
print("vrs", hex(v), hex(r), hex(s))

bv = v.to_bytes(1, 'big')
br = r.to_bytes(32, 'big')
bs = s.to_bytes(32, 'big')

osig = tm.functions.getConfigSignature(bv, br, bs, 0).call()
print("signature", osig[0].hex(), osig[1].hex(), osig[2].hex())

odparam = [acc.address, 1, 1, 0, data, osig]

#enode.call_func(acc, tm.functions.takeOrder(odparam, odset), True)
'''


#bqhash, odhash = tm.functions.getOrderQueueInfo(btaddr, qtaddr, False).call()
#print(bqhash.hex(), odhash.hex())
#
#goi = tm.functions.getOrderInfo(bqhash, odhash, False)
#print(goi.buildTransaction())
#
#ret = goi.call()
#print(ret)

#enode.call_func(acc, hd.functions.approveDelegate(tm.address), True)

APPROVE_VALUE =  10 ** 27
#print("relayer:", relayer.address)
#enode.call_func(relayer, btoken.functions.approve(proxy.address, APPROVE_VALUE), True)
#enode.call_func(relayer, qtoken.functions.approve(proxy.address, APPROVE_VALUE), True)

print("realyer:", relayer.address);
print("proxy:", proxy.address);
print("btoken:", btoken.address);
ab = btoken.functions.allowance(relayer.address, proxy.address).call()
print("relayer base  token appove", ab)

print("qtoken:", qtoken.address);
aq = qtoken.functions.allowance(relayer.address, proxy.address).call()
print("relayer quote token appove", aq)

afi = btoken.functions.approve(proxy.address, APPROVE_VALUE).buildTransaction()
#print(afi)

bb = btoken.functions.balanceOf(acc.address).call()
bq = qtoken.functions.balanceOf(acc.address).call()
print("base  token amount", bb)
print("quote token amount", bq)

ab = btoken.functions.allowance(acc.address, proxy.address).call()
aq = qtoken.functions.allowance(acc.address, proxy.address).call()
print("base  token appove", ab)
print("quote token appove", aq)

