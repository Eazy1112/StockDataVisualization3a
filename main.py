#import from other files
from userinput import (
    get_chart_type,
    get_stock_symbol,
    get_function,
    get_start_date,
    get_end_date,

)

from api_handling import fetch_stock_data
from chart_generation import generate_chart

def filter_data_by_date(time_series_data, start_date, end_date):
    """
    Filter the stock data based on the provided date range.
    """
    filtered = {}

    for x in time_series_data:
        if(x > start_date and x < end_date):
            filtered[x] = time_series_data[x]

    return filtered


def main():

    print("Stock Data Visualizer")
    print("---------------------")

    symbol = get_stock_symbol()
    chart_type = get_chart_type()
    function = get_function()
    start_date = get_start_date()
    end_date = get_end_date(start_date)

    data = fetch_stock_data(symbol, function)
    print("Data keys from API:", list(data.keys()))

    if data is None:
        print("Failed to fetch stock data. Please try again later.")
        return
    
    print("Successfully fetched stock data.\n")

    
    #manually input the key
    
    if function == "TIME_SERIES_INTRADAY":
        time_series_key = "Time Series (60min)"
    elif function == "TIME_SERIES_DAILY":
        time_series_key = "Time Series (Daily)"
    elif function == "TIME_SERIES_WEEKLY":
        time_series_key = "Weekly Time Series"
    elif function == "TIME_SERIES_MONTHLY":
        time_series_key = "Monthly Time Series"
    else:
        print("Invalid function type.")
        return

    time_series_data = data.get(time_series_key, {})

    if not time_series_data:
        print("No stock data available for the selected time series.")
        return
    
    filtered_data = filter_data_by_date(time_series_data, start_date, end_date)

    if not filtered_data:
        print("No stock data available for the selected date range. Try a different date.")
        return
    
    labels = sorted(filtered_data.keys())
    open = [float(filtered_data[date]["1. open"]) for date in labels]
    high = [float(filtered_data[date]["2. high"]) for date in labels]
    low = [float(filtered_data[date]["3. low"]) for date in labels]
    close = [float(filtered_data[date]["4. close"]) for date in labels]

    generate_chart(labels, open, high, low, close, chart_type, symbol, start_date,end_date)


if __name__ == "__main__":
    main()