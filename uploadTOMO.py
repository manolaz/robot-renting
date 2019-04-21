from web3 import Web3, HTTPProvider, IPCProvider, WebsocketProvider
import json

with open(
        'Certify.json'
) as f:
    abi = json.load(f)

w3 = Web3(HTTPProvider('https://testnet.tomochain.com'))

contract_address = '0x2249e974842d14ae8e5283960f5072faa070f350308b118b4bc03f179b699bbc'
contract_address = Web3.toChecksumAddress(contract_address)
wallet_private_key = ''

contract = w3.eth.contract(address=contract_address, abi=abi)


def store_results(_name, _address, _course, _status, _symbolIssued, _grade):
    wallet_address = ''
    wallet_address = Web3.toChecksumAddress(wallet_address)

    nonce = w3.eth.getTransactionCount(wallet_address)

    txn_dict = contract.functions.chatsave(_name, _symbol,
                                           _decimal).buildTransaction({
                                               'chainId':
                                               89,
                                               'gas':
                                               340000,
                                               'gasPrice':
                                               w3.toWei('40', 'gwei'),
                                               'nonce':
                                               nonce,
                                           })

    signed_txn = w3.eth.account.signTransaction(txn_dict,
                                                private_key=wallet_private_key)

    result = w3.eth.sendRawTransaction(signed_txn.rawTransaction)

    tx_receipt = w3.eth.getTransactionReceipt(result)

    count = 0
    while tx_receipt is None and (count < 30):

        time.sleep(10)

        tx_receipt = w3.eth.getTransactionReceipt(result)

    return (tx_receipt)

    if tx_receipt is None:
        tx_receipt = "Failed"
        return (tx_receipt)


def check_hash(sessionId):
    tx_receipt = contract.functions.checkhash(sessionId).call()
    return (tx_receipt)


def tsend(name, symbol, decimal):
    _username = str(name)
    _symbol = int(symbol)
    _decimal = str(decimal)
    _status = str(status)
    tx_receipt = store_results(_username, _symbol, _decimal)
    return tx_receipt


def hashcheck(sessionId):
    sessionId = int(sessionId)
    tx_receipt = check_hash(sessionId)
    return tx_receipt


# examples:
hashcheck(0)
tsend(an, 190420, 0x0e670075ee255b54dbe55c1aca90a52946962deb)
