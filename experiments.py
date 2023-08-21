from datetime import date, timedelta

today = date.today()
delta = timedelta(days=7)
weekLater = today + delta

query = ("SELECT * FROM Employees WHERE (MONTH(Birthday) BETWEEN {} AND {})"
         "and (DAY(Birthday) BETWEEN {} AND {});".
         format(today.month, weekLater.month,today.day, weekLater.day))
# select * from Employees where MONTH(Birthday)=1;
print(query)
