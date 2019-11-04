
from ether_node import EtherNode

ETH_NODE_HTTP = "https://mainnet.infura.io/v3/99a79f80961b4db7aab7c9f54375eda7"
ddexfile = "../build/contracts/HybridExchange.json"

if __name__ == "__main__":
    # get ether node
    enode = EtherNode(ETH_NODE_HTTP)
    # get ddex contract: hybrid exchange
    ddex = enode.get_contract("0xE2a0BFe759e2A4444442Da5064ec549616FFF101", ddexfile)

    # get proxy
    proxy = ddex.functions.proxyAddress().call()
    print("proxy address:", proxy)

