import datetime as dt


#
# 1 task
#
def substruct_five() -> dt.datetime:
    return dt.datetime.now() - dt.timedelta(days=5)


#
# 2 task
#
def print_days() -> None:
    print(f"Today is {dt.datetime.now()}")
    print(f"Tommorow is {dt.datetime.now() + dt.timedelta(days=1)}")
    print(f"Yesterday is {dt.datetime.now() - dt.timedelta(days=1)}")


#
# 3 task
#
def print_days_without_microseconds() -> None:
    print(dt.datetime.now().replace(microsecond=0))


#
# 4 task
#
def diff_seconds_between_dates(a: dt.datetime, b: dt.datetime) -> float:
    return (a - b).total_seconds()


print_days_without_microseconds()
res = diff_seconds_between_dates(dt.datetime.now(), dt.datetime(1970, 1, 1))
print(res)
