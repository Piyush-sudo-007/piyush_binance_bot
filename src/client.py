from typing import Optional, Dict, Any
import time, hmac, hashlib
from urllib.parse import urlencode
import requests
from .config import API_KEY, API_SECRET, BASE_URL, RECV_WINDOW
from .logging_setup import get_logger

logger = get_logger(__name__)

class BinanceFuturesClient:
    def __init__(self, api_key: Optional[str]=None, api_secret: Optional[str]=None, base_url: Optional[str]=None):
        self.api_key = api_key or API_KEY
        self.api_secret = api_secret or API_SECRET
        self.base_url = (base_url or BASE_URL).rstrip('/')

    def _sign(self, payload: dict) -> str:
        payload = dict(payload)
        payload['timestamp'] = int(time.time() * 1000)
        payload['recvWindow'] = RECV_WINDOW
        qs = urlencode(payload, doseq=True)
        signature = hmac.new(self.api_secret.encode('utf-8'), qs.encode('utf-8'), hashlib.sha256).hexdigest()
        return qs + '&signature=' + signature

    def _headers(self) -> dict:
        return {'X-MBX-APIKEY': self.api_key}

    def ping(self) -> Dict[str, Any]:
        url = f"{self.base_url}/fapi/v1/ping"
        r = requests.get(url, headers=self._headers(), timeout=10)
        r.raise_for_status()
        return r.json()

    def create_order(self, symbol: str, side: str, order_type: str, quantity: float, price: Optional[float]=None, timeInForce: str='GTC', **extra) -> Dict[str, Any]:
        path = '/fapi/v1/order'
        payload = {
            'symbol': symbol.upper(),
            'side': side.upper(),
            'type': order_type.upper(),
            'quantity': quantity,
        }
        if price is not None:
            payload['price'] = price
            payload['timeInForce'] = timeInForce
        payload.update(extra or {})
        qs = self._sign({k:v for k,v in payload.items() if v is not None})
        url = self.base_url + path + '?' + qs
        logger.info('POST %s', url)
        r = requests.post(url, headers=self._headers(), timeout=10)
        try:
            data = r.json()
        except Exception:
            r.raise_for_status()
        if not r.ok:
            logger.error('Order error: %s %s', r.status_code, data)
            r.raise_for_status()
        logger.info('Order response: %s', data)
        return data