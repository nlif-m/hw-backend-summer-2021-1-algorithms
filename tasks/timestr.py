__all__ = (
    'seconds_to_str',
)


def seconds_to_str(seconds: int) -> str:
    """
    Функция должна вернуть текстовое представление времени
    20 -> 20s
    60 -> 01m00s
    65 -> 01m05s
    3700 -> 01h01m40s
    93600 -> 01d02h00m00s
    """
    assert(seconds >= 0)
    seconds_in_time = {
        "day": 86400,
        "hour": 3600,
        "minute": 60,
        "second": 1
    }
    result = ""
    amount_of_days = seconds // seconds_in_time["day"]
    if amount_of_days != 0:
        result += f"{amount_of_days:02}d"
        seconds %=seconds_in_time["day"]
        
    amount_of_hours = seconds // seconds_in_time["hour"]
    if amount_of_hours != 0 or result != "":
        result += f"{amount_of_hours:02}h"
        seconds %=seconds_in_time["hour"]

    amount_of_minutes = seconds // seconds_in_time["minute"]
    if amount_of_minutes != 0 or result != "":
        result += f"{amount_of_minutes:02}m"
        seconds %=seconds_in_time["minute"]

    amount_of_seconds = seconds // seconds_in_time["second"]
    result += f"{amount_of_seconds:02}s"
    seconds %=seconds_in_time["second"]

    return result



