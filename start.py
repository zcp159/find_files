import os
import fnmatch


# 确定文件是否符合责规则
def is_file_math(file, guizes):
    # 遍历规则，如果文件符合任何一条规则则返回真
    for guize in guizes:
        if fnmatch.fnmatch(file, guize):
            return True
    # 遍历完成后，返回假
    # 如果前面已经返回真了，由于只能返回一个值，则这个返回假就没用了
    return False


# 获取目录及规则，返回生成器，生成器内容为
# 目录下所有满足规则的文件的绝对路径
def is_special_file(root, guizes=["*"], liwaimulus=[]):
    # 遍历根目录
    for dangqianmulu, mulus, files in os.walk(os.path.abspath(root)):
        # 遍历返回的文件名
        for file in files:
            # 判定文件名是否满足需要搜索的格式,如果符合则绝对路径放入生成器
            if is_file_math(file, guizes):
                yield os.path.join(os.path.abspath(dangqianmulu), file)
        for d in liwaimulus:
            if d in mulus:
                mulus.remove(d)


def main():
    # 指定目录
    mulu_1 = r"C:\Users\33011\Desktop\新建文件夹"
    # 指定文件格式
    geshi_1 = ["*.txt"]
    liwaimulu_1 = ["bin", "conf"]
    # 获取满足条件的文件生成器
    result_files = is_special_file(mulu_1, geshi_1, liwaimulu_1)
    for i in result_files:
        print(i)


if __name__ == '__main__':
    main()
