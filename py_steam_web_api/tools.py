import datetime


def date_transformer(timestamp: int):
    dt = datetime.datetime.fromtimestamp(timestamp)

    formatted_datetime = dt.strftime('%Y-%m-%d %H:%M:%S')

    return formatted_datetime
