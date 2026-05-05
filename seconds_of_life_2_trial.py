from datetime import datetime as dt
now=dt.now()
dob=dt.strptime(input("Enter your date of birth DD/MM/YYYY: "),"%d/%m/%Y")
diff=now-dob
print(f"The number of seconds since your date of birth is {diff.total_seconds() :.2f}.")

"""
- First of all is .strptime() which parses stringes. It converts the string input into a datetime object that could be worked with.
- The %d/%m/%Y is the formmat of datetime that gets us DD/MM/YYYY 
"""
