from flask import Flask, render_template, request, redirect, url_for, flash
from src.client import BinanceFuturesClient
from src.logging_setup import get_logger
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = "supersecretkey"

logger = get_logger("webapp")
client = BinanceFuturesClient(
    os.getenv("API_KEY"),
    os.getenv("API_SECRET"),
    base_url=os.getenv("BASE_URL")
)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        symbol = request.form.get("symbol").upper()
        side = request.form.get("side").upper()
        qty = float(request.form.get("quantity"))
        order_type = request.form.get("order_type")
        price = request.form.get("price")

        try:
            if order_type == "MARKET":
                res = client.create_order(symbol, side, "MARKET", qty)
            elif order_type == "LIMIT":
                res = client.create_order(symbol, side, "LIMIT", qty, price=float(price))
            else:
                flash("Unsupported order type", "error")
                return redirect(url_for("index"))

            flash(f"Order successful! ID: {res.get('orderId', 'N/A')}", "success")
            logger.info(f"Order placed via UI: {res}")
        except Exception as e:
            logger.error(f"UI order error: {e}")
            flash(f"Error: {e}", "error")

        return redirect(url_for("index"))

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000)