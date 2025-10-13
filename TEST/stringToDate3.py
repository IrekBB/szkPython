import sys
from datetime import datetime

def main(args):
    # create a datetime object representing March 1, 2023 at 9:30 AM
    start_datetime = datetime(2023, 3, 1, 9, 30)

    # get the year, month, day, hour, and minute
    year = start_datetime.year
    month = start_datetime.month
    day = start_datetime.day
    hour = start_datetime.hour
    minute = start_datetime.minute
    print (f" rok: {year}\n miesiąc: {month}\n dzień: {day}\n godzina: {hour}\n minuta: {minute}\n")

if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))