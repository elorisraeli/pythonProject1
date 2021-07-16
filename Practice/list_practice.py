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

# # sort by key, this time is first date in list
# from datetime import datetime
#
# values = ['8-Nov-19', '21-Jun-16', '1-Nov-18', '7-Apr-19']
# values.sort(key=lambda d: datetime.strptime(d, "%d-%b-%y"))
# print(values)


# function return how much of each type is in the list
def type_count(lst):
    new_lst = [["int", 0], ["float", 0], ["string", 0], ["boolean", 0]]
    if isinstance(lst, list):
        for element in lst:
            if type(element) == int:
                new_lst[0][1] += 1
            elif type(element) == float:
                new_lst[1][1] += 1
            elif type(element) == str:
                new_lst[2][1] += 1
            elif type(element) == bool:
                new_lst[3][1] += 1
    return new_lst


combined_list = [1, "ertgb", 34.343, True, 54, "ewptbw", False, 21.98]
print(type_count(combined_list))
