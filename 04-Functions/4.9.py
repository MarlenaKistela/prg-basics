
def time_string(hours, minutes, time_format):
    if time_format == '12':
        if hours == 0:
            hours = 12
            period = 'AM'
        elif hours < 12:
            period = 'AM'
        elif hours == 12:
            period = 'PM'
        else:
            hours -= 12
            period = 'PM'
        return f"{hours}:{minutes:02d} {period}"
    elif time_format == '24':
        return f"{hours}:{minutes:02d}"
    else:
        raise ValueError("Invalid time format. Use '12' or '24'.")