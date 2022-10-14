'''
1. Напишите программу, удаляющую из текста все слова, содержащие "абв". 
В тексте используется разделитель пробел.
in
Number of words: 10

out
авб абв бав абв вба бав вба абв абв абв
авб бав вба бав вба

in
Number of words: 6

out
ваб вба абв ваб бва абв
ваб вба ваб бва

in
Number of words: -1

out
The data is incorrect
'''
from random import choices

def word_list(count, val = "абв"):
    result = []
    for i in range(count):
        temp = choices(val, k=3)
        result.append("".join(temp))
    return result

count = int(input("Введите количество: "))
text = word_list(count)
print(text)
new_text = ' '.join(list(filter(lambda w: "абв" not in w, text)))
print(new_text)
