# # Before Exam Mechina: ---Sort a list---
# lst = ["ab", "cde", "fghi", "jklmn"]
# print(f"List: {lst}")
# lst.sort(reverse=True)
# print(f"List reverse: {lst}")
#
#
# # sort by key, this time is length of string in list
# def sort_len(e):
#     return len(e)
#
#
# lst2 = ["cde", "ab", "jklmn", "fghi", ]
# lst2.sort(key=sort_len)
# print(lst2)

# sort by key, this time is first date in list
from datetime import datetime

values = ['8-Nov-19', '21-Jun-16', '1-Nov-18', '7-Apr-19']
values.sort(key=lambda d: datetime.strptime(d, "%d-%b-%y"))
print(values)
