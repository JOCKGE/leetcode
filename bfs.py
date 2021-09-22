#广度优先遍历打印目录结构，队列实现
import os
def get_all_dir(path):
    quene = []
    quene.append(path)
    while len(quene) > 0:
        dir_path = quene.pop(0)
        print(dir_path)
        for file in os.listdir(dir_path):
            file_abs_path = os.path.join(dir_path,file)
            if os.path.isdir(file_abs_path):
                quene.append(file_abs_path)
get_all_dir('/Users/gezhiguo/Downloads')

        