def read_file():
    count_chars = 0
    count_the = 0
    count_end_e = 0
    count_less_4 = 0
    count_upper = 0
    file = open(r'C:\Users\Elor Israeli\Desktop\מבוא למחשבים\homework/poem.txt', 'r', encoding='utf-8')
    for line in file:
        print(line, end='')
        words_regular = line.split()
        for original_word in words_regular:
            for char in original_word:
                if 64 < ord(char) < 91:  # (Upper case)
                    count_upper += 1

        words_lower = line.lower().split()
        for word in words_lower:
            count_chars += len(word)
            if word == 'the':
                count_the += 1
            if word[-1] == 'e':
                count_end_e += 1
            if len(word) < 4:
                count_less_4 += 1
    print(f"\n\nThe number of chars in file: {count_chars}", end='')
    print(f"\nThe number of the word 'the' in file: {count_the}", end='')
    print(f"\nThe number of words end with 'e' in file: {count_end_e}", end='')
    print(f"\nThe number of words less then 4 chars in file: {count_less_4}", end='')
    print(f"\nThe number of upper chars in file: {count_upper}", end='')
    file.close()


read_file()


