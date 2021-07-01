# Exercise Excel: ---Read specific data from the specific column from a csv file---
from csv import reader
opened_file = open(r'C:\Users\Elor Israeli\Desktop\מבוא למחשבים\homework/AppleStore.csv', encoding="utf8")
read_file = reader(opened_file)
apps_data = list(read_file)
# print(apps_data[1][11])

# get only column number 11 with the values into an array
column = [rec[11] for rec in apps_data]
# print(column)
content_ratings = {
    '4+': column.count('4+'),
    '9+': column.count('9+'),
    '12+': column.count('12+'),
    '17+': column.count('17+'),
}
print(content_ratings)
