from web3 import Web3
from time import sleep
import json

import config as cfg
import getpass


class EtherNode():
    def __init__(self, nodeurl = cfg.ETH_NODE_HTTP):
        # nonce flag and value
        self.nonce_value = {}
        #  connect to node
        while True:
            self.w3 = Web3(Web3.HTTPProvider(nodeurl, {"timeout": 30}))
            if self.w3.isConnected() == False:
                print("node is not connected, wait " + str(5) + " second")
                sleep(5)
            else:
                print("connect to node by http: " + nodeurl)
                break

    # wait confirmed
    # tx_hash: transaction hash
    def wait_tx_confirm(self, tx_hash):
        logs = self.w3.eth.waitForTransactionReceipt(tx_hash)
        return logs

    # decrypt keystore file
    # _kf: keystore file
    # _pwd: password for keystore file
    # return accout obj: {address, privateKey, signTransaction, encrypt, signHash} for success, None for failed
    def decrypt_keystore(self, _kf, _pwd):
        if _pwd is None:
            _pwd = getpass.getpass("password:")
        # open keystore file
        with open(_kf, 'r') as fp:
            # load json file
            fj = json.load(fp)
            # decrypt
            private_key = self.w3.eth.account.decrypt(fj, _pwd)
            #print("private key:", private_key.hex())
            return self.w3.eth.account.privateKeyToAccount(private_key)
        return None

    # get nonce
    # address: address of ordinary account
    # return nonce value
    def get_nonce(self, address):
        # get nonce from dict
        nonce = self.nonce_value.get(address)
        if nonce is None:
            # get nonce from node
            nonce = self.w3.eth.getTransactionCount(address);

        #update nonce
        self.nonce_value[address] = nonce + 1
        return nonce

    # create contract
    # acc_owner: owner who creates the contract
    # build_file: build file from `truffle compile`
    # cstcb: construct callback, deal constructor with args
    # args: arguments for cstcb
    # wait: true for wait until response of ether node, false for otherwise
    # return: eth.contract / None
    def create_contract(self, acc_owner, build_file, cstcb, args, wait=False):
        with open(build_file, 'r') as fp:
            # load json file
            fj = json.load(fp)
            # get bytecode, deployedBytecode, abi
            bc = fj['bytecode']
            dbc = fj["deployedBytecode"]
            abi = fj["abi"]
            # get contract
            contr = self.w3.eth.contract(abi=abi, bytecode=bc, bytecode_runtime=dbc)
            # build transaction
            cst = cstcb(contr.constructor, args)
            contx = cst.buildTransaction({
                "from": acc_owner.address,
                "gas": cfg.ETH_TX_GAS,
                "gasPrice": cfg.ETH_TX_GAS_PRICE,
                "nonce": self.get_nonce(acc_owner.address)
                })
            # sign transaction
            raw_tx = acc_owner.signTransaction(contx)
            # send raw transaction
            tx_hash = self.w3.eth.sendRawTransaction(raw_tx["rawTransaction"])
            print("tx hash:", str(self.w3.toHex(tx_hash)))
            # wait tx confirmed
            if wait is True:
                ret = self.wait_tx_confirm(tx_hash)
                print("deploy contract", build_file, "successed, gas used:", ret["gasUsed"])
                return self.w3.eth.contract(address=ret["contractAddress"], abi=fj["abi"])
        return None

    # transfer ether
    # acc_from: account who sends ether
    # to: address of account who receives ether
    # value: amount of ether
    # wait: true for wait until response of ether node, false for otherwise
    # return None for failed, value for success
    def transfer_ether(self, acc_from, to, value, wait=False):
        # get signed tx
        stx = acc_from.signTransaction({
            "to": to,
            "value": value,
            "gas": cfg.ETH_TX_GAS,
            "gasPrice": cfg.ETH_TX_GAS_PRICE,
            "nonce": self.get_nonce(acc_from.address)
            })

        # send raw transaction
        tx_hash = self.w3.eth.sendRawTransaction(stx["rawTransaction"])
        print("tx hash:", str(self.w3.toHex(tx_hash)))
        # wait tx confirmed
        if wait is True:
            ret = self.wait_tx_confirm(tx_hash)
            print("trasfer ether from", acc_from.address, "to", to, "value", value, "success")
        return value

    # get contract 
    # addr: address of contract
    # build_file: build file from `truffle compile`
    # return None for failed, contract obj for success
    def get_contract(self, addr, build_file):
        with open(build_file, 'r') as fp:
            fj = json.load(fp)
            abi = fj['abi']
            return self.w3.eth.contract(address=addr, abi=abi)

    # transfer token
    # token: contract obj of token, created from get_contract or create_contract
    # acc_from: account who sends token
    # to: address of account who receives token
    # value: amount of token
    # wait: true for wait until response of ether node, false for otherwise
    # return None for failed, value for success
    def transfer_token(self, token, acc_from, to, value, wait=False):
        # get tx
        tx = token.functions.transfer(to, 100).buildTransaction({
            "gas": cfg.ETH_TX_GAS,
            "gasPrice": cfg.ETH_TX_GAS_PRICE,
            "nonce": self.get_nonce(acc_from.address)
            })
        # get signed tx
        stx = acc_from.signTransaction(tx)

        # send raw transaction
        tx_hash = self.w3.eth.sendRawTransaction(stx["rawTransaction"])
        print("tx hash:", str(self.w3.toHex(tx_hash)))
        # wait tx confirmed
        if wait is True:
            ret = self.wait_tx_confirm(tx_hash)
            print("trasfer token", token.functions.name().call(), "from", acc_from.address, "to", to, "value", value, "success")
        return value

    # call function
    # acc: account who calls the function
    # cst: contract function with args
    # wait: true for wait until response of ether node, false for otherwise
    # return tx-hash
    def call_func(self, acc, cst, wait = False):
        # get tx
        tx = cst.buildTransaction({
            "gas": cfg.ETH_TX_GAS,
            "gasPrice": cfg.ETH_TX_GAS_PRICE,
            "nonce": self.get_nonce(acc.address)
            })
        # get signed tx
        stx = acc.signTransaction(tx)

        # send raw transaction
        tx_hash = self.w3.eth.sendRawTransaction(stx["rawTransaction"])
        print("tx hash:", str(self.w3.toHex(tx_hash)))
        # wait tx confirmed
        if wait is True:
            ret = self.wait_tx_confirm(tx_hash)

        return str(self.w3.toHex(tx_hash))

