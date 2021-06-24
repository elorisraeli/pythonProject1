# Copy machine: ---Copy text from file to another
file1 = open(r'C:\Users\Elor Israeli\Desktop\מבוא למחשבים\homework/fileWithText.txt', 'r')
file2_append = open(r'C:\Users\Elor Israeli\Desktop\מבוא למחשבים\homework/fileWithoutText.txt', 'a')
for line in file1:
    file2_append.write(line)
    print(f"File 1: {line}", end='')
file2_append.close()
print()
file2_r = open(r'C:\Users\Elor Israeli\Desktop\מבוא למחשבים\homework/fileWithoutText.txt', 'r')
for writen_line in file2_r:
    print(f"File 2: {writen_line}", end='')
