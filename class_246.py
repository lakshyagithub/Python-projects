from web3 import Web3
import json
import requests

infura_url = 'https://mainnet.infura.io/v3/5159ef0311f84be386dea286d1719579'
web3 = Web3(Web3.HTTPProvider(infura_url)) #establish the connection

req_ethgas_data = requests.get('https://ethgasstation.info/json/ethgasAPI.json') #get the data from the API in json format.
latest_block_info = json.loads(req_ethgas_data.content)

#access various costs of transactions depending upon the speed.
print('safeLow', latest_block_info['safeLow'])
print('average', latest_block_info['average'])
print('fast', latest_block_info['fast'])
print('fastest', latest_block_info['fastest'])
print('Block number:', latest_block_info['blockNum'])

gas_price = web3.eth.gasPrice
gas_price_in_ether = gas_price/10**8
print("Gas price in ether:", gas_price_in_ether)
gas_price_in_dollar = gas_price_in_ether * 1797.54
print("Gas price in dollar:", gas_price_in_dollar)
Block_data = web3.eth.get_block(18491725)
print("Block data:", Block_data)
latest_transaction = Block_data["transactions"][-1].hex()
print("Latest transaction:", latest_transaction)
transaction_details = web3.eth.get_transaction(latest_transaction)
gas_estimate = web3.eth.estimateGas({"to": transaction_details["to"], "from":transaction_details["from"]})
print("Gas used by this transaction:", gas_estimate)
print("Gas limit:", transaction_details["gas"])