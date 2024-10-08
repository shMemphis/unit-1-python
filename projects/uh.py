from datetime import datetime
my_string ="07/22/2000"
my_date = datetime.strptime(my_string, "%m/%d%y")
print(my_date)