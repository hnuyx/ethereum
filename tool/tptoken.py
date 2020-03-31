
from ether_node import EtherNode
from eth_account.messages import encode_defunct
import web3

ETH_NODE_HTTP = "https://ropsten.infura.io/v3/99a79f80961b4db7aab7c9f54375eda7"

tptjson = "../build/contracts/TPToken.json"

btaddr = "0x2e01154391F7dcBf215c77DBd7fF3026Ea7514ce"
qtaddr = "0x2e01154391F7dcBf215c77DBd7fF3026Ea7514ce"

proxy = "0x141A60c20026d88385a5339191C3950285e41072"
owner = web3.Web3.toChecksumAddress("0xab890808775d51e9bf9fa76f40ee5fff124dece5")

# get ether node
enode = EtherNode(ETH_NODE_HTTP)

# get btaddr, qtaddr
btoken = enode.get_contract(btaddr, tptjson)
qtoken = enode.get_contract(qtaddr, tptjson)

bb = btoken.functions.balanceOf(owner).call()
bq = qtoken.functions.balanceOf(owner).call()
print("base  token amount", bb)
print("quote token amount", bq)

ab = btoken.functions.allowance(owner, proxy).call()
aq = qtoken.functions.allowance(owner, proxy).call()
print("base  token appove", ab)
print("quote token appove", aq)

a =  btoken.functions.allowance(owner, proxy);
print(a.buildTransaction())

