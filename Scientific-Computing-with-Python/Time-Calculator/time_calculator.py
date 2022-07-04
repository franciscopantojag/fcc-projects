def add_time(start: str, duration: str, day_of_week: str = None):
    DAYS_OF_WEEK = ['monday', 'tuesday', 'wednesday',
                    'thursday', 'friday', 'saturday', 'sunday']
    week_day = None
    result_week_day = None

    if day_of_week:
        week_day = day_of_week.lower()

    [start_number, start_am_pm] = start.split(' ')
    [start_hour, start_minutes] = list(
        map(lambda x: int(x), start_number.split(':')))
    [duration_hour, duration_minutes] = list(
        map(lambda x: int(x), duration.split(':')))

    start_hour_24 = start_hour if start_am_pm == 'AM' else int(start_hour) + 12

    raw_result_hours = start_hour_24 + duration_hour
    raw_result_minutes = start_minutes + duration_minutes

    result_minutes = raw_result_minutes % 60

    result_plus = (raw_result_hours % 24) + (int(raw_result_minutes/60))

    result_days = int(raw_result_hours / 24) + int(result_plus / 24)

    result_hours = result_plus % 24

    final_result_am = result_hours < 12
    final_result_am_pm = 'AM' if final_result_am else 'PM'
    final_result_hours = result_hours if final_result_am else result_hours - 12
    if final_result_hours == 0:
        final_result_hours = 12

    n_zero_minutes = '0' if len(str(result_minutes)) < 2 else ''
    final_result = f'{final_result_hours}:{n_zero_minutes}{result_minutes} {final_result_am_pm}'

    parens = None
    if result_days == 1:
        parens = '(next day)'
    elif result_days > 1:
        parens = f'({result_days} days later)'

    if week_day:
        index = DAYS_OF_WEEK.index(week_day)
        final_index = (index + result_days) % 7
        result_week_day = DAYS_OF_WEEK[final_index].capitalize()

    if result_week_day:
        final_result = f'{final_result}, {result_week_day}'

    if parens:
        final_result = f'{final_result} {parens}'

    return final_result


print(add_time("3:00 PM", "3:10"))
# Returns: 6:10 PM

print(add_time("11:30 AM", "2:32", "Monday"))
# Returns: 2:02 PM, Monday

print(add_time("11:43 AM", "00:20"))
# Returns: 12:03 PM

print(add_time("10:10 PM", "3:30"))
# Returns: 1:40 AM (next day)

print(add_time("11:43 PM", "24:20", "tueSday"))
# Returns: 12:03 AM, Thursday (2 days later)

print(add_time("6:30 PM", "205:12", 'tuesday'))
# Returns: 7:42 AM (9 days later)

print(add_time("11:40 AM", "0:25"))
