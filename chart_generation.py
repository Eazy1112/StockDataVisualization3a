import pygal

def generate_chart(labels, open_, high, low, close, chart_type, symbol, start_date, end_date):
    title = f"{symbol} Stock Data ({start_date} to {end_date})"

    chart = pygal.Bar(x_label_rotation=20, height=400) if chart_type == "1" else pygal.Line(x_label_rotation=20, height=400)
    chart.title = title
    chart.x_labels = labels
    chart.add("Open", open_)
    chart.add("High", high)
    chart.add("Low", low)
    chart.add("Close", close)

    return chart.render(is_unicode=True)