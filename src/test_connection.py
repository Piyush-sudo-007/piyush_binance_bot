from src.client import BinanceFuturesClient

def main():
    client = BinanceFuturesClient()
    print("Pinging Binance Futures Testnet...")
    res = client.ping()
    print("Response:", res)

if __name__ == "__main__":
    main()
