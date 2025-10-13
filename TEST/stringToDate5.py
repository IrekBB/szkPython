#  Convert a String to a datetime Object in Python Using datetime.strptime()
# Step 01: Analyze the date-time string that can be converted for patterns that match the formatting codes.
# Step 02: Create the date-time format from the strptime()directives.
# Step 03: Pass the string and format to the function and receive the object as output.

import sys
from datetime import datetime
from dateutil.parser import parse

def main(args):
   from datetime import datetime

   # Example with the standard date and time format
   date_str = '2023-02-28 14:30:00'
   date_format = '%Y-%m-%d %H:%M:%S'

   date_obj = datetime.strptime(date_str, date_format)
   print(date_obj)

    # Example with a different format

   date_str = '02/28/2023 02:30 PM'
   date_format = '%m/%d/%Y %I:%M %p'

   date_obj = datetime.strptime(date_str, date_format)
   print(date_obj)

   # Another flexible option is the dateutil library, particularly the parser.parse() function.
   # It automatically detects date formats, allowing you to parse strings without specifying 
   # a format string.

   

    # Automatically infers the format
   date_obj = parse("March 1, 2023 9:30 AM")
   print(date_obj)

   # Formatting datetime Objects to Strings with strftime()
   now = datetime.now()
   formatted = now.strftime('%Y-%m-%d %H:%M:%S')
   print(formatted)

if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))