
from ether_node import EtherNode
import sys
from web3 import Web3

if __name__ == "__main__":
    # get ether node
    enode = EtherNode()
    # get balance
    ret = enode.get_balance(sys.argv[1])
    print(ret, "Wei --->", Web3.fromWei(ret, 'ether'), "ether")

