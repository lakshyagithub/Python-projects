from web3 import Web3
from web3.middleware import geth_poa_middleware

API_url = "https://mainnet.infura.io/v3/5159ef0311f84be386dea286d1719579"
web3 = Web3(Web3.HTTPProvider(API_url))

block_data = web3.eth.get_block(18463108)

transaction = web3.eth.get_transaction(0x7595c79b22f52e9e32d5ca91e0e0ab4618beeeb4042018189ea8e266a8899f4d)

print("Block hash:", transaction["blockHash"].hex())
print("Block number:", transaction["blockNumber"])
print("From:", transaction["from"])
print("gas:", transaction["gas"])
print("Gas price in ether:", transaction["gasPrice"])
print("Hash:", transaction["hash"].hex())
print("input:", transaction["input"])
print("nonce:", transaction["nonce"])
print("Signature:", transaction["s"].hex())
print("to:", transaction["to"])
print("value:", transaction["value"])