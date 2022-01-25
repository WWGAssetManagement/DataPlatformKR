from daeshin.tr.minute_price import MinutePrice


def get_minute_price(code, start, end):
    return MinutePrice(code, start, end)
