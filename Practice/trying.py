a = ['foo', 'bar', 'baz', 'qux']

# all the list
print(a)
# first element
print(a[0])
# last element
print(a[-1])
# from element 2 to 3 (not included last(element 4))
print(a[1:3])
# from element 1 to end
print(a[1:])
# until element 3 (not included)
print(a[:2])
# upside down
print(a[::-1])

# add 2 elements
a += ['one', 'two']
print(a)
# print twice the list
print(a * 2)
# list's lenght
print(len(a))
# minimum string by chars (a<b<c...)
print(min(a))
# maximun string by chars (a<b<c...)
print(max(a))
# Boolian question if the string exist in the list
print('two' in a)
# change an element
a[3] = 10
print(a)

s = 'elorisraeli'
# Boolian question if the char exist in the string
print('a' in s)
# delete specific element
del a[3]
print(a)

b = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight']
# delete from element 2 to 3 (not included last(element 4))
del b[1:3]
print(b)

# All str functions option - using dir
str1 = 'This is a lovely day'
print(dir(str1))
