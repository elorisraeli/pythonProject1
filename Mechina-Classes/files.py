# # Open a file in my computer
# #  --> DON'T MIX OPTIONS <--
# input_file = open(r'C:\Users\Elor Israeli\Desktop\מבוא למחשבים/textFile1.txt', 'r')
# print(type(input_file))
# # Option 1: read all data in the file
# lyrics = input_file.read()
# print(lyrics)
# # Option 2: read line by line the data in the file
# lyrics2 = None
# while lyrics2 != '':
#     lyrics2 = input_file.readline()
#     print(lyrics2, end='')
# # Option 3: read data simply line by line from file
# for line in input_file:
#     print(line, end='')


# # Write into file
# file_append = open(r'C:\Users\Elor Israeli\Desktop\מבוא למחשבים/textFile1.txt', 'a')
# file_read = open(r'C:\Users\Elor Israeli\Desktop\מבוא למחשבים/textFile1.txt', 'r')
# text_to_add = input("Enter what you want to add to the file:")
# file_append.write('\n' + str(text_to_add))
# file_append.close()
# for line in file_read:
#     print(line, end='')


# # Create function to append text to text file
# def append_text(file_dir, text):
#     file_a = open(r'{}'.format(str(file_dir)), 'a')
#     file_a.write('\n' + str(text))
#     file_a.close()
#     file_r = open(r'{}'.format(str(file_dir)), 'r')
#     for txt_line in file_r:
#         print(txt_line, end='')
#
#
# append_text(r'C:\Users\Elor Israeli\Desktop\מבוא למחשבים/textFile1.txt', "add from function!!!")


# # Open file without closing him, its automatically
# with open(r'C:\Users\Elor Israeli\Desktop\מבוא למחשבים/textFile1.txt', 'r') as my_file:
#     for line in my_file:
#         print(line, end='')

