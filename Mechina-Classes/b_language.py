# get sentence from user, translate to b language
# b language = after "aeiou" chars adding 'b' and the char again

# Option 1 (simple way)
sentence = input("Enter a sentence in english:")
if 'a' in sentence:
    sentence = sentence.replace("a", "aba")
if 'e' in sentence:
    sentence = sentence.replace("e", "ebe")
if 'i' in sentence:
    sentence = sentence.replace("i", "ibi")
if 'o' in sentence:
    sentence = sentence.replace("o", "obo")
if 'u' in sentence:
    sentence = sentence.replace("u", "ubu")
print(sentence)


# Option 2 (with function)
def myFun(str):
    result = ""
    charList = ["a", "e", "i", "o", "u"]
    for c in str:
        if c in charList:
            result += c + 'b' + c
        else:
            result += c
    return result


print(myFun("ani ohev otach"))

# Option 3 (with "re" class and "sub" method)
import re


def myFun(str):
    return re.sub(r'([aeiou])', r'\1b\1', str)


print(myFun("ani ohev otach"))

# Option 4: Teacher way :)
str1 = 'ani ohev otach'
str2 = 'aeiou'
str3 = ''

for i in str1:
    str3 += i
    for j in str2:
        if i == j:
            str3 += 'b' + i
            break

print(str3)

# Option 5: Teacher way :)
str1 = 'ani ohev otach'
str2 = 'aeiou'
str3 = ''

for i in str1:
    str3 += i
    if i in str2:
        str3 += 'b' + i


print(str3)

