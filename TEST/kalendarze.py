import calendar
import sys
import time

def main(args):
    GMT = time.gmtime() 
    text_calendar = calendar.TextCalendar()
    text_calendar.prmonth(2025, 10)
    print(f"Czy rok {GMT.tm_year} jest przystępny? ", calendar.isleap(2025))
  

if __name__=="__main__":
    sys.exit(main(sys.argv))
