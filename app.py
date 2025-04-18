from flask import Flask, render_template, request
from api_handling import fetch_stock_data
from chart_generation import generate_chart

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    chart_svg = None

    if request.method == "POST":
        symbol = request.form.get("symbol").upper()
        chart_type = request.form.get("chart_type")
        function = request.form.get("function")
        start_date = request.form.get("start_date")
        end_date = request.form.get("end_date")

        if not all([symbol, chart_type, function, start_date, end_date]):
            message = "All fields are required."
        elif end_date < start_date:
            message = "End date must be after start date."
        else:
            data = fetch_stock_data(symbol, function)
            key_map = {
                "TIME_SERIES_INTRADAY": "Time Series (60min)",
                "TIME_SERIES_DAILY": "Time Series (Daily)",
                "TIME_SERIES_WEEKLY": "Weekly Time Series",
                "TIME_SERIES_MONTHLY": "Monthly Time Series",
            }
            time_series_data = data.get(key_map.get(function), {})
            filtered = {date: d for date, d in time_series_data.items() if start_date <= date <= end_date}

            if not filtered:
                message = "No data found for that date range."
            else:
                labels = sorted(filtered)
                open_ = [float(filtered[d]["1. open"]) for d in labels]
                high = [float(filtered[d]["2. high"]) for d in labels]
                low = [float(filtered[d]["3. low"]) for d in labels]
                close = [float(filtered[d]["4. close"]) for d in labels]

                chart_svg = generate_chart(labels, open_, high, low, close, chart_type, symbol, start_date, end_date)

    return render_template("index.html", message=message, chart_svg=chart_svg)

if __name__ == "__main__":
    print(" App running at: http://localhost:5017")
    app.run(host="0.0.0.0", port=5000, debug=True)
