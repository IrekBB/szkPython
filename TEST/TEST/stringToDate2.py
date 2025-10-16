import sys
from datetime import time

def main(args):
    # create a time object with the microsecond granularity
    end_time = time(15, 45, 30, 500000)    # (hour, minute, second, and microsecond)

    # get the hour and minute
    hour = end_time.hour
    minute = end_time.minute
    second = end_time.second
    microsecond = end_time.microsecond

    print(f" godziny: {hour}\n minuty:  {minute}\n sekundy: {second}\n mikrosekundy: {microsecond}")

if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))