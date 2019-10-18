import re
import time
ori = input('请输入提取共有单词的第一个文件名：')
com = input('请输入提取共有单词的第二个文件名：')
print('数据正在处理中...Loading...')
duplicate_list = []
first_list = []
second_list = []
sequence = []
final_list = []
with open(ori + '.txt', 'r', encoding='UTF-8') as original_txt:
    ori = original_txt.readlines()
    for each in ori:
        split_list_ori =  re.split(' |/', each)
        # split_list_ori = each.split(' ')
        for each in split_list_ori:
            first_list.append(each)
    for i in range(len(first_list)):
        first_list[i] = first_list[i].replace('#', '').replace('\n', '').replace('(', '').replace(')', '').replace(',', '').replace('.', '')
# print(first_list)
# print(first_list[0])
# print(first_list[1])
# print(first_list[2])

    # invalid code
    # for i in first_list:
    #     i = i.replace('#', '')    

with open(com + '.txt', 'r', encoding='UTF-8') as compare_txt:
    com = compare_txt.readlines()
    for each in com:
        split_list_com = each.split(' ')
        for each in split_list_com:
            second_list.append(each)
    for i in range(len(second_list)):
        second_list[i] = second_list[i].replace('.\n', '').replace('!\n', '').replace('?\n', '').replace(',', '').replace('.', '')
# print(second_list)
# print(second_list[0])
# print(second_list[1])
# print(second_list[2])

    # print(second_list)
for each in first_list:
    if each in second_list:
        duplicate_list.append(each)
duplicate_list = list(set(duplicate_list))
duplicate_list.sort()

# print(duplicate_list[0])
# print(duplicate_list[1])
# print(duplicate_list[2])
# print(duplicate_list[3])
# print(duplicate_list[4])
# print(duplicate_list[5])
# print(duplicate_list[6])
# print(duplicate_list[7])
# print(duplicate_list[100])
# print(duplicate_list[200])
# print(duplicate_list[300])
# print(duplicate_list[400])
# print(duplicate_list[500])
# print(duplicate_list[1000])
# print(duplicate_list[1500])
# print(duplicate_list[2000])


# for each in duplicate_list:
    # print(each)
for i in range(len(duplicate_list)):
    print(i, duplicate_list[i])


# print(duplicate_list)
# print(len(duplicate_list))
        
# with open('coca60000.txt', 'r') as coca:
#     coca_list = coca.readlines()
#     for i in range(len(coca_list)):
#         split_list = coca_list[i].split()
#         sequence.append(split_list)
        # print(sequence)


# for i in range(len(sequence)):
    # print(sequence[i])


# print(sequence)
# print(len(sequence))

# for each in duplicate_list:
    # print(each)
    # for i in range(len(sequence)):
        # print(i)
        # if each in sequence[i]:
            # print(each)
            # final_list.append(each)

# final_list = list(set(final_list))
# print(final_list)     
# print(len(final_list))
print('查找已完成！文件共同单词如上，累计 %d 个共同单词。' % len(duplicate_list))
time.sleep(600)

