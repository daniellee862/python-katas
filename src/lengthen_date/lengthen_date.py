from datetime import datetime


def lengthen_date(date_string):
    # Parse input to datetime object
    date_obj = datetime.strptime(date_string, '%d.%m.%Y')

    # day
    day_name = date_obj.strftime("%A")

    # day number
    day_num = date_obj.strftime("%-d")

    # suffix
    # key-value pairs for nums 1, 2, 3 and suffix
    # last digit day_num[-1] passed to get() method returns value or "th".
    day_num += {"1": "st", "2": "nd", "3": "rd"}.get(day_num[-1], "th")

    # month
    month_name = date_obj.strftime("%B")

    # year
    year = date_obj.year

    # final
    lengthened_date = f"{day_name} {day_num} {month_name} {year}"
    return lengthened_date
