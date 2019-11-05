
from ether_node import EtherNode

ETH_NODE_HTTP = "https://mainnet.infura.io/v3/99a79f80961b4db7aab7c9f54375eda7"
idexfile = "../build/contracts/Exchange.json"

if __name__ == "__main__":
    # get ether node
    enode = EtherNode(ETH_NODE_HTTP)
    # get idex contract: exchange
    idex = enode.get_contract("0x2a0c0DBEcC7E4D658f48E01e3fA353F44050c208", idexfile)

    # get period 
    period = idex.functions.inactivityReleasePeriod().call()
    print("period :", period)

