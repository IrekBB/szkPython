import sys
from datetime import timedelta
from datetime import datetime

def main(args):
    # create a timedelta object representing 3 hours and 15 minutes
    event_duration = timedelta(hours=3, minutes=15)

    # get the total duration in seconds
    event_duration_seconds = event_duration.total_seconds()

    # add the duration to a start time to get an end time
    event_start_time = datetime(2023, 3, 1, 18, 15)
    event_end_time = event_start_time + event_duration
    print (f"Poczatek wydatzenia: {event_start_time}")
    print (f"Koniec wydarzenia: {event_end_time}")
    print (f"Czas wydarzenia w sekundach: {event_duration_seconds}")

if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))