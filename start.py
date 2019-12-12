import os
import fnmatch
import logging


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
            file_juedui_lujing = os.path.join(os.path.abspath(dangqianmulu), file)
            # 判定文件名是否满足需要搜索的格式,如果符合则绝对路径放入生成器
            if is_file_math(file, guizes):
                logging.info(("{}  符合文件格式").format(file_juedui_lujing))
                yield file_juedui_lujing
            else:
                logging.info(("{} 不符合文件格式").format(file_juedui_lujing))
        for d in liwaimulus:
            if d in mulus:
                logging.debug(("{} 目录需要排除").format(os.path.join(dangqianmulu, d)))
                mulus.remove(d)


def get_logger():
    rdir = os.path.dirname(os.path.abspath(__file__))  # 获取上级目录的绝对路径
    log_dir = os.path.join(rdir, "record.log")  # 构建日志位置绝对路径
    fh = logging.FileHandler(log_dir, "w", encoding='utf-8')  # 创建一个文件流并设置编码utf8
    logger = logging.getLogger()  # 获得一个logger对象，默认是root
    logger.setLevel(logging.DEBUG)  # 设置最低等级debug
    fm = logging.Formatter("%(asctime)s --- %(message)s")  # 设置日志格式
    logger.addHandler(fh)  # 把文件流添加进来，流向写入到文件
    fh.setFormatter(fm)  # 把文件流添加写入格式


def main():
    get_logger()
    # 指定目录
    mulu_1 = r"D:\Clear cache\project_test\win10_main_p3\find_files\Test_case"
    # 指定文件格式
    geshi_1 = ["*.txt"]
    liwaimulu_1 = ["bin", "conf"]
    # 获取满足条件的文件生成器
    result_files = is_special_file(mulu_1, geshi_1, liwaimulu_1)
    for i in result_files:
        print(i)


if __name__ == '__main__':
    main()
