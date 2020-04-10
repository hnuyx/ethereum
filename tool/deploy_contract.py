
from ether_node import EtherNode
from web3 import Web3

tptfile   = "../build/contracts/TPToken.json"
randfile   = "../build/contracts/Random.json"
btafile   = "../build/contracts/BTAToken.json"
btbfile   = "../build/contracts/BTBToken.json"
btcfile   = "../build/contracts/BTCToken.json"
btdfile   = "../build/contracts/BTDToken.json"

ownerfile = "./keystore/UTC--2019-07-20T04-00-01.800933268Z--a9535b10ee96b4a03269d0e0def417af97477fd6"
MAGNITUDE = 10 ** 18


def tpt_cstcb(cst, args):
    return cst()

def rand_cstcb(cst, args):
    return cst()

def bt_cstcb(cst, args):
    return cst(args[0])

if __name__ == "__main__":
    # get ether node
    enode = EtherNode()
    # decrype keystore file
    acc = enode.decrypt_keystore(ownerfile, None)

    # deploy contract: TPT
    #tpt = enode.create_contract(acc, tptfile, tpt_cstcb, None, True)
    #print("tpt address:", tpt.address)
    #tpt = enode.create_contract(acc, tptfile, tpt_cstcb, None, True)
    #print("tpt address:", tpt.address)
    #tpt = enode.create_contract(acc, tptfile, tpt_cstcb, None, True)
    #print("tpt address:", tpt.address)
    #tpt = enode.create_contract(acc, tptfile, tpt_cstcb, None, True)
    #print("tpt address:", tpt.address)

    # deploy contract: random
    #random = enode.create_contract(acc, randfile, rand_cstcb, None, True)
    #print("random address:", random.address)

    # deploy contrct: BTA, BTB, BTC, BTD
    #bta = enode.create_contract(acc, btafile, bt_cstcb, [acc.address], True);
    #print("bta address:", bta.address)
    #btb = enode.create_contract(acc, btbfile, bt_cstcb, [acc.address], True);
    #print("btb address:", btb.address)
    #btc = enode.create_contract(acc, btcfile, bt_cstcb, [acc.address], True);
    #print("btc address:", btc.address)
    #btd = enode.create_contract(acc, btdfile, bt_cstcb, [acc.address], True);
    #print("btd address:", btd.address)

    # get contract: BTA, BTB, BTC, BTD
    qts = ["0x8e4d8D520f52B044e1E8B054D763B723B7C3E716",
           "0x45e110F81bBf89041A63Bc2403058743bc552bAF",
           "0x7B29ed69368B0Ed0d3b21A857BaEeF788B13c626",
           "0x60423Ebc63245631Ea71bdF58CF23A3949329cDb"]
    bta = enode.get_contract(qts[0], btafile)
    btb = enode.get_contract(qts[1], btbfile)
    btc = enode.get_contract(qts[2], btcfile)
    btd = enode.get_contract(qts[3], btdfile)

    # transfer token: BTA, BTB, BTC, BTD
    TRANS_VALUE = 1000000 * MAGNITUDE
    #accounts = ["0xfcff222a998b0cfa175d769663fb8d750c93b24f",
    #            "0xab890808775d51e9bf9fa76f40ee5fff124dece5",
    #            "0xFc2003889D3430A7D0931B5adE5c7A101356Efd7",
    #           ]
    accounts = ["0xFc2003889D3430A7D0931B5adE5c7A101356Efd7"]
    for act in accounts:
        act = Web3.toChecksumAddress(act)
        print("transfer toke for acc", act)
        enode.call_func(acc, bta.functions.transfer(act, TRANS_VALUE), False)
        enode.call_func(acc, btb.functions.transfer(act, TRANS_VALUE), False)
        enode.call_func(acc, btc.functions.transfer(act, TRANS_VALUE), False)
        enode.call_func(acc, btd.functions.transfer(act, TRANS_VALUE), False)

