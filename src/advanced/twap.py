from src.client import BinanceFuturesClient
from src.logging_setup import get_logger

logger = get_logger(__name__)

class TWAPStrategy:
    def __init__(self, client: BinanceFuturesClient):
        self.client = client

    def execute(self, symbol: str, side: str, total_qty: float, slices: int=5, duration_secs: int=60):
        if slices < 1:
            raise ValueError('slices must be >= 1')
        slice_qty = float(total_qty) / slices
        interval = duration_secs / slices
        results = []
        for i in range(slices):
            logger.info('TWAP slice %d/%d qty=%s', i+1, slices, slice_qty)
            res = self.client.create_order(symbol, side, 'MARKET', slice_qty)
            results.append(res)
            import time; time.sleep(interval)
        return results
