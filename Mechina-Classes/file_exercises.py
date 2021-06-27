# # Exercise 'Copy machine': ---Copy text from file to another---
# file1 = open(r'C:\Users\Elor Israeli\Desktop\מבוא למחשבים\homework/fileWithText.txt', 'r')
# file2_append = open(r'C:\Users\Elor Israeli\Desktop\מבוא למחשבים\homework/fileWithoutText.txt', 'a')
# for line in file1:
#     file2_append.write(line)
#     print(f"File 1: {line}", end='')
# file2_append.close()
# print()
# file2_r = open(r'C:\Users\Elor Israeli\Desktop\מבוא למחשבים\homework/fileWithoutText.txt', 'r')
# for writen_line in file2_r:
#     print(f"File 2: {writen_line}", end='')


# Exercise 'Lazy student': ---Questions in file and questions with answers to another file---

# # internet boy attempt (if the questions with '=' in the end (not our case))
# with open(r'C:\Users\Elor Israeli\Desktop\מבוא למחשבים\homework/questions.txt') as fp:
#     qs = fp.readlines()  # reading the qustion file
#     # writing the text file by the name fp
# with open(r'C:\Users\Elor Israeli\Desktop\מבוא למחשבים\homework/answers.txt',  'w') as fp:
#     for q in qs:
#         Deleteequal = q.split('=')
#         a = eval(Deleteequal[0])  # always going to be line 0 because I am reading a line by line
#         f = q + str(a)
#         f = f.replace("\n",  "")
#         fp.write(f)
#         fp.write('\n')
# # str(a) to write the final answer

# my attempt
def solve(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    elif operator == "-":
        return num1 - num2
    else:
        return "NOT VALID OPERATOR"


solved_text = ""
with open(r'C:\Users\Elor Israeli\Desktop\מבוא למחשבים\homework/mathQuestions.txt', 'r') as file_questions:
    for line in file_questions:
        line_values = line.split(" ")
        line_values[2] = line_values[2].replace("\n", "")
        # check if it is a valid math problem
        if line_values[0].isdigit() and line_values[2].isdigit():
            line_values.append("=")
            line_values.append(str(solve(int(line_values[0]), line_values[1], int(line_values[2]))))
            print(line_values)
            sentence_join = " ".join(line_values)
            print(sentence_join)
            solved_text = f"{solved_text} \n {sentence_join}"
        else:
            MESSAGE = "NOT A REAL MATH PROBLEM"
            solved_text = f"{solved_text} \n {line} = {MESSAGE}"


with open(r'C:\Users\Elor Israeli\Desktop\מבוא למחשבים\homework/mathSolutions.txt', 'w') as file_answers:
    file_answers.write(solved_text)
