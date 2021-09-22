import os
#深度优先遍历目录层级结构,堆栈实现
def get_all_dir(path):
    stack = []
    stack.append(path)
    while len(stack) != 0:
        dir_path = stack.pop()
        print(dir_path)
        for file in os.listdir(dir_path):
            file_abs_path = os.path.join(dir_path,file)
            if os.path.isdir(file_abs_path):
                stack.append(file_abs_path)
get_all_dir('/Users/gezhiguo/Downloads')