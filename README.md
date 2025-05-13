# Simple ETH Balance Checker

A lightweight Python script to check the ETH balance of any Ethereum address using Web3.py and Infura.

## 🧰 Features

- Connects to Ethereum mainnet using Infura
- Validates Ethereum address
- Retrieves ETH balance in real-time
- CLI-based usage

---

## 🚀 How to Use

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/eth-balance-checker.git
cd eth-balance-checker
```

### 2. Install Requirements
```bash
pip install -r requirements.txt
```

### 3. Set Your Infura URL
Open `main.py` and replace this line:
```python
INFURA_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"
```
with your actual Infura Project URL.

### 4. Run the Script
```bash
python main.py
```

---

## 🛑 Note

- Never share your Infura project ID publicly if it's tied to a paid plan.
- This script only works for the Ethereum **mainnet** by default. You can change the URL to use testnets.

## 📄 License

MIT © 2025
