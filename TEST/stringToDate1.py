"""
Python datetime Modul:
Class/Method	     Purpose	                                                             Common use cases
____________________________________________________________________________________________________________________________________________________________
datetime.date	     Represents a date (year, month, day).	                                    Calculating differences between dates, formatting dates as strings, extracting date components.

datetime.time	     Represents a time of day (hour, minute, second, microsecond).	            Comparing times, formatting times as strings, extracting time components.

datetime.datetime	 Represents a date and time. Combines date and time functionalities.	    Working with time-series data, extracting date and time components, formatting as strings.

datetime.timedelta	 Represents the difference between two dates or times (duration).	        Adding/subtracting durations to/from dates or times, calculating time intervals.

datetime.strptime()	 Parses a string into a datetime object based on a specified format.	    Converting strings to datetime objects for further manipulation and analysis.

datetime.strftime()	 Formats a datetime object into a string based on a specified format.	    Converting datetime objects to human-readable strings for display or reporting.

"""
from datetime import date

def main(args):
    tyg = ['poniedziałek','wtorek', 'środa', 'czwartek','piątek','sobota', 'niedziela']
    # create a date object representing February 2, 2025
    start_date = date(2026, 2, 2)

    # extract information such as the year, month, and day
    year = start_date.year
    month = start_date.month
    day = start_date.day


    # get the day of the week (Note: Monday is coded as 0, and Sunday as 6)
    weekday = start_date.weekday()

    # the date can be formatted as a string if needed
    date_str = start_date.strftime('%Y-%m-%d')
    
    print(date_str)
    print (f" {day} {month} {year}")
    print (tyg[weekday])

if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))
