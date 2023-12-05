from web3 import Web3

infura_url = "https://mainnet.infura.io/v3/5159ef0311f84be386dea286d1719579"
web3 = Web3(Web3.HTTPProvider(infura_url))
gas_prices = web3.eth.gas_price

safe_low_gas_price = int(gas_prices * 0.9) # 90%
average_gas_price = int(gas_prices * 1.0) # Same as current gas price
fast_gas_price = int(gas_prices * 1.1) # 110%
fastest_gas_price = int(gas_prices * 1.2) # 120%

safe_low_gas_price_gwei = web3.from_wei(safe_low_gas_price, "gwei")
average_gas_price_gwei = web3.from_wei(average_gas_price, "gwei")
fast_gas_price_gwei = web3.from_wei(fast_gas_price, "gwei")
fastest_gas_price_gwei = web3.from_wei(fastest_gas_price, "gwei")

print("Safe low gas price:", safe_low_gas_price_gwei)
print("average gas price:", average_gas_price_gwei)
print("Fast gas price:", fast_gas_price_gwei)
print("Fastest gas price:", fastest_gas_price_gwei)

print("Gas price in gwei:", web3.from_wei(gas_prices, "gwei"))