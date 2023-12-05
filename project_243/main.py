# Import the required module and establish a connection with Infura API
from web3 import Web3

# URL of the Infura API
URL = 'https://mainnet.infura.io/v3/cded6e6690d04259b05137dd10b170c3'

# Establish a connection to the specified URL
web3 = Web3(Web3.HTTPProvider(URL))

# Task 02: Get the latest block of the blockchain
latest_block = web3.eth.get_block('latest')

# Print the latest block information
print("Latest Block of Ethereum blockchain:")
print(latest_block)

# Task 03: Get block transaction count
block_number = latest_block['number']
block_transaction_count = web3.eth.get_block_transaction_count(block_number)

# Print the number of transactions in the block
print("Number of transactions happened in the block:", block_transaction_count)

# Task 04: Get transaction fee history
block_count = 10  # You can change this to the desired number of blocks
newest_block = 'latest'
reward_percentiles = None

# Get transaction fee history
Transaction_fee = web3.eth.fee_history(block_count, newest_block, reward_percentiles)

# Print the transaction fee history
print("Transaction fee history:")
print(Transaction_fee)
