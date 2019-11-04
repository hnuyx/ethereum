
from ether_node import EtherNode

tptfile   = "../build/contracts/TPToken.json"

def tpt_cstcb(cst, args):
    return cst()

if __name__ == "__main__":
    # get ether node
    enode = EtherNode()
    # decrype keystore file
    acc = enode.decrypt_keystore(ownerfile, None)
    # deploy contract
    tpt = enode.create_contract(acc, tptfile, tpt_cstcb, None, True)
    print("tpt address:", tpt.address)

