
from ether_node import EtherNode

tptfile   = "../build/contracts/TPToken.json"
randfile   = "../build/contracts/Random.json"

ownerfile = "./keystore/UTC--2019-07-20T04-00-01.800933268Z--a9535b10ee96b4a03269d0e0def417af97477fd6"


def tpt_cstcb(cst, args):
    return cst()

def rand_cstcb(cst, args):
    return cst()

if __name__ == "__main__":
    # get ether node
    enode = EtherNode()
    # decrype keystore file
    acc = enode.decrypt_keystore(ownerfile, None)

    '''
    # deploy contract: TPT
    tpt = enode.create_contract(acc, tptfile, tpt_cstcb, None, True)
    print("tpt address:", tpt.address)
    '''

    # deploy contract: TPT
    random = enode.create_contract(acc, randfile, rand_cstcb, None, True)
    print("random address:", random.address)

