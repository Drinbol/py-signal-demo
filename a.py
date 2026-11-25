import signal  # 信号处理模块，用于处理各种系统信号，如中断、终止等
import time    # 时间模块，提供了各种时间相关的函数，如暂停、延迟等
import sys     # 系统模块，提供了与 Python 解释器和系统交互的函数和变量

# 定义一个无限循环的函数
def run_program():
    while True:
        time.sleep(1)  # 暂停 1 秒钟
        print("a")     # 输出 "a"

# 如果当前脚本被直接执行，那么执行 run_program 函数
if __name__ == "__main__":
    try:
        run_program()  # 运行 run_program 函数
    except KeyboardInterrupt:
        print("\nApplication exit!")  # 捕获 KeyboardInterrupt 异常，输出提示信息