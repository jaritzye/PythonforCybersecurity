message = input ("Type message ")
for letter in message:
    letter_num = ord(letter)
    if letter_num < 110 and letter_num > 96:
        letter_num = letter_num + 13
    else:
        letter_num = letter_num - 13

    print(chr(letter_num), end = "")