# Open a file in my computer
input_file = open(r'C:\Users\Elor Israeli\Desktop\מבוא למחשבים/textFile1.txt', 'r')
print(type(input_file))
# # Option 1: read all data in the file
# lyrics = input_file.read()
# print(lyrics)
# Option 2: read line by line the data in the file
lyrics2 = None
while lyrics2 != '':
    lyrics2 = input_file.readline()
    print(lyrics2, end='')
