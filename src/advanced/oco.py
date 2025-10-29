from src.client import BinanceFuturesClient
from src.logging_setup import get_logger

logger = get_logger(__name__)

class SimpleOCO:
    def __init__(self, client: BinanceFuturesClient):
        self.client = client

    def place_oco(self, symbol: str, side: str, quantity: float, take_profit: float, stop_price: float, stop_limit_price: float):
        tp_side = 'SELL' if side.upper() == 'BUY' else 'BUY'
        tp = self.client.create_order(symbol, tp_side, 'LIMIT', quantity, price=take_profit, timeInForce='GTC')
        sl = self.client.create_order(symbol, tp_side, 'STOP_MARKET', quantity, stopPrice=stop_price)
        logger.info('Placed TP and SL (simplified): %s %s', tp, sl)
        return {'take_profit': tp, 'stop_loss': sl}
