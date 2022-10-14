'''
2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.Входные и выходные данные хранятся в отдельных текстовых файлах.
Алгоритм RLE

in
Enter the name of the file with the text:
'text_words.txt'
Enter the file name to record:
'text_code_words.txt'
Enter the name of the file to decode:
'text_code_words.txt'

out
aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
vvvvvvvvvvvbbwwPPuuuTTYyWWQQ

out in file
'text_words.txt'
aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
vbbwwPPuuuTTYyWWQQ

'text_code_words.txt'
5a29v4s3D3d2F4g2O3i2a1
1v2b2w2P3u2T1Y1y2W2Q
'''

from itertools import groupby , starmap

def rle_encode(origin, encd):
    with open(origin, "r", encoding = "utf-8") as file, \
        open(encd, "w", encoding = "utf-8") as file_encode:
        for i in file:
            file_encode.write("".join([f"{len(list(v))}{ch}" for ch,v in groupby(i)]))

def rle_decode(file_name):
    with open(file_name, "r", encoding = "utf-8") as file:
        n = ""
        for i in file:
            word_list = []
            for k in i.strip():
                if k.isdigit():
                    n+=k
                else:
                    word_list.append([int(n),k])
                    n = ""
            print("".join(starmap(lambda x,y: x*y, word_list)))


rle_encode("task_3_text.txt", "task_3_encode.txt")
rle_decode("task_3_encode.txt")