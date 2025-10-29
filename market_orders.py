import argparse, sys
from src.client import BinanceFuturesClient
from src.validation import validate_symbol, validate_positive_number
from src.logging_setup import get_logger

logger = get_logger(__name__)

def main(argv=None):
    parser = argparse.ArgumentParser(prog='market_order', description='Place a MARKET order (Futures Testnet)')
    parser.add_argument('symbol', type=str)
    parser.add_argument('side', choices=['BUY','SELL','buy','sell'])
    parser.add_argument('quantity', type=str)
    parser.add_argument('--api_key', type=str, default=None)
    parser.add_argument('--api_secret', type=str, default=None)
    args = parser.parse_args(argv)

    symbol = validate_symbol(args.symbol)
    side = args.side.upper()
    qty = validate_positive_number(args.quantity)

    client = BinanceFuturesClient(api_key=args.api_key, api_secret=args.api_secret)
    try:
        res = client.create_order(symbol, side, 'MARKET', qty)
        print(res)
        logger.info('Market order executed: %s', res)
    except Exception as e:
        logger.exception('Market order failed')
        print('Error:', e)
        sys.exit(1)

if __name__ == '__main__':
    main()
