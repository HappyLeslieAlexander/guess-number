# 导入random和tkinter模块
import random
import tkinter as tk

# 定义一个函数，用于生成一个1到100之间的随机整数
def generate_number():
    # 生成一个1到100之间的随机整数，并赋值给全局变量number
    global number
    number = random.randint(1, 100)
    # 打印提示信息
    print("我已经想好了一个1到100之间的数字，你能猜出来吗？")

# 定义一个函数，用于检查用户的输入是否正确
def check_guess():
    # 获取用户在输入框中输入的内容，并转换为整数
    guess = int(entry.get())
    # 如果用户的猜测等于随机数，显示恭喜信息，并重新生成一个随机数
    if guess == number:
        label.config(text="恭喜你，你猜对了！")
        generate_number()
    # 如果用户的猜测小于随机数，显示提示信息
    elif guess < number:
        label.config(text="你猜的太小了，再试试吧！")
    # 如果用户的猜测大于随机数，显示提示信息
    else:
        label.config(text="你猜的太大了，再试试吧！")

# 创建一个窗口对象
window = tk.Tk()
# 设置窗口的标题为猜数字小游戏
window.title("猜数字小游戏")
# 设置窗口的大小为300x100
window.geometry("300x100")
# 创建一个标签对象，用于显示提示信息
label = tk.Label(window, text="欢迎来到猜数字小游戏！")
# 将标签放置在窗口的上方
label.pack()
# 创建一个输入框对象，用于接收用户的输入
entry = tk.Entry(window)
# 将输入框放置在窗口的中间
entry.pack()
# 创建一个按钮对象，用于触发检查用户的输入的函数
button = tk.Button(window, text="猜一猜", command=check_guess)
# 将按钮放置在窗口的下方
button.pack()
# 调用生成随机数的函数
generate_number()
# 进入窗口的主循环
window.mainloop()