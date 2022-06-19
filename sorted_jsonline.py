import os.path
import jsonlines
import sys

args = sys.argv
print(args)

if len(args) != 4:
    print('Введите 3 аргумента:\n путь первого файла,\n путь второго файла,\n путь для сохранений нового файла')
else:
    if os.path.exists(args[2]) or os.path.exists(args[3]):
        pass
    else:
        print('Введите существующий путь')

    path1 = os.path.normpath(args[1])
    path2 = os.path.normpath(args[2])
    path3 = os.path.normpath(args[3])

    print('generation', str(path3) + '....')

    with jsonlines.open(path1, mode='r') as file1, jsonlines.open(path2, mode='r') as file2, jsonlines.open(
        path3, mode='w') as file_write:
        iter1 = file1.__iter__()
        iter2 = file2.__iter__()
        elem1 = iter1.__next__()
        elem2 = iter2.__next__()
        while True:
            try:
                if elem1['timestamp'] > elem2['timestamp']:
                    file_write.write(elem2)
                    elem2 = iter2.__next__()
                    continue
            except Exception:
                iteration = iter1
                elem = iter1
                break
            try:
                if elem1['timestamp'] <= elem2['timestamp']:
                    file_write.write(elem1)
                    elem1 = iter1.__next__()
            except Exception:
                iteration = iter2
                elem = iter2
                break

        while True:
            try:
                file_write.write(elem)
                elem = iteration.__next__()
            except Exception:
                break

    file_write.close()

# with jsonlines.open('union.jsonl', mode='w') as file3:
# file3.write(*new_lst)

# file3.close()

# print(path1)
# print(path2)

# with open(path1, 'r') as file1, open(path2, 'r') as file2:
# read1 = file1.readline()
# read2 = file2.readlines()
# read1.extend(read2)
# new_lst = sorted(read1, key=lambda x: json.loads(x)["timestamp"])
# new_lst1 = ''.join(list(new_lst))
# with open('union.jsonl', 'w') as file3:
# file3.write(new_lst)
