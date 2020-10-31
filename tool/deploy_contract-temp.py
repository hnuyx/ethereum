
from ether_node import EtherNode
from web3 import Web3

usdtfile   = "../build/contracts/USDT.json"
gusdfile   = "../build/contracts/GUSD.json"

ownerfile = "./keystore/UTC--2019-07-20T04-00-01.800933268Z--a9535b10ee96b4a03269d0e0def417af97477fd6"
MAGNITUDE = 10 ** 18


def bt_cstcb(cst, args):
    return cst(args[0])

if __name__ == "__main__":
    # get ether node
    enode = EtherNode()
    # decrype keystore file
    acc = enode.decrypt_keystore(ownerfile, None)

    # deploy contrct: USDT GUSD
    usdt = enode.create_contract(acc, usdtfile, bt_cstcb, [acc.address], True)
    print("usdt address:", usdt.address)
    gusd = enode.create_contract(acc, gusdfile, bt_cstcb, [acc.address], True)
    print("gusd address:", gusd.address)

    ## get contract: USDT, GUSD
    #qts = ["0x8e4d8D520f52B044e1E8B054D763B723B7C3E716",
    #       "0x60423Ebc63245631Ea71bdF58CF23A3949329cDb"]
    #usdt = enode.get_contract(qts[0], usdtfile)
    #gusd = enode.get_contract(qts[1], gusdfile)

    ## transfer token: BTA, BTB, BTC, BTD
    #TRANS_VALUE = 10000000 * MAGNITUDE
    ##accounts = ["0xfcff222a998b0cfa175d769663fb8d750c93b24f",
    ##            "0xab890808775d51e9bf9fa76f40ee5fff124dece5",
    ##            "0xFc2003889D3430A7D0931B5adE5c7A101356Efd7",
    ##           ]
    #accounts = ["0xFc2003889D3430A7D0931B5adE5c7A101356Efd7"]
    #for act in accounts:
    #    act = Web3.toChecksumAddress(act)
    #    print("transfer toke for acc", act)
    #    enode.call_func(acc, usdt.functions.transfer(act, TRANS_VALUE), False)
    #    enode.call_func(acc, gusd.functions.transfer(act, TRANS_VALUE), False)

