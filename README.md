# 🚀 Binance Futures Order Bot (Testnet)

A **CLI + Web UI based Trading Bot** for **Binance USDT-M Futures Testnet**, built with Python.  
Supports **Market and Limit** orders, structured logging, and an optional **Flask dashboard** for managing trades visually.

---

## 🧠 Overview

This bot allows you to:

- ✅ Place **Market** and **Limit** orders from CLI or UI
- ⚙️ Validate inputs and handle errors gracefully
- 🪵 Log all actions in structured JSON format
- 🌐 (Optional) Use a clean Flask-based **Web Dashboard**

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/piyush-binance-bot.git
cd piyush-binance-bot
```

### 2️⃣ Create and Activate Virtual Environment

```bash
python -m venv myenv
# Activate it:
# Windows
myenv\Scripts\activate
# macOS/Linux
source myenv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables

Create a `.env` file in the project root and fill it with your Binance Testnet credentials:

```env
API_KEY=your_testnet_api_key
API_SECRET=your_testnet_api_secret
BASE_URL=https://testnet.binancefuture.com
RECV_WINDOW=5000
```

### 5️⃣ Test API Connection

```bash
python -m src.test_connection
```

✅ Expected Output:

```
Pinging Binance Futures Testnet...
Response: {}
```

---

## 💹 Run the Bot

### CLI Mode

```bash
# Market Order
python src/orders/market_orders.py BTCUSDT BUY 0.001

# Limit Order
python src/orders/limit_orders.py BTCUSDT SELL 0.001 75000
```

### Web UI Mode

```bash
python src/webapp/app.py
```

Then open: **http://127.0.0.1:5000** in your browser.

---

## 📊 Logging

All actions are logged in **bot.log** with timestamps and structured JSON for easy tracking.

Example:

```json
{
  "timestamp": "2025-10-29 12:56:29",
  "level": "INFO",
  "message": "Market BUY order executed for BTCUSDT"
}
```

---

## 🧪 Testing

Run unit tests with:

```bash
pytest tests/ -v
```

---

## 📘 Report

A detailed PDF report (`report.pdf`) is included, covering:

- Architecture overview
- API integration
- Error handling & logging
- Future improvements

---

## 🧠 Future Enhancements

- Add OCO / Grid trading strategies
- Integrate WebSocket streams for live prices
- Add portfolio tracking and PnL reporting
- Dockerize for deployment

---

## 🧑‍💻 Author

**Piyush**  
Built with ❤️ using Python and Binance Futures Testnet API.

---

## ⚠️ Disclaimer

> This bot is for **educational purposes** only.  
> It uses Binance **Testnet**, not real funds.  
> Always test carefully before using any trading automation in production.
