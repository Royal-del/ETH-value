# main.py
from web3 import Web3

# Connect to Ethereum (via Infura)
INFURA_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"
w3 = Web3(Web3.HTTPProvider(INFURA_URL))

if not w3.isConnected():
    print("❌ Failed to connect to Ethereum node.")
    exit()

# Ask for Ethereum address
address = input("🔍 Enter Ethereum address: ")

# Validate address
if not w3.isAddress(address):
    print("⚠️ Invalid Ethereum address.")
    exit()

# #####Get balance
balance_wei = w3.eth.get_balance(address)
balance_eth = w3.fromWei(balance_wei, 'ether')

print(f"💰 Balance of {address}: {balance_eth} ETH")
