
from ether_node import EtherNode

randaddr = "0x53bf75a6948ce0B0A7680d87881008972c7CcBcB"
randfile   = "../build/contracts/Random.json"
ownerfile = "./keystore/UTC--2019-07-20T04-00-01.800933268Z--a9535b10ee96b4a03269d0e0def417af97477fd6"


if __name__ == "__main__":
    # get ether node
    enode = EtherNode()
    # decrype keystore file
    acc = enode.decrypt_keystore(ownerfile)
    random = enode.get_contract(randaddr, randfile)

    rnum = enode.call_func(acc, random.functions.random(1), True)
    print("random number:", rnum)

