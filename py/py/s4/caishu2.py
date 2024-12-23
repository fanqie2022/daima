import random

def guess_number_v3():
    number = random.randint(0, 100)
    attempts = 0
    while True:
        try:
            user_guess = int(input("请输入一个0-100之间的整数: "))
            attempts += 1
            if user_guess > number:
                print("遗憾，太大了")
            elif user_guess < number:
                print("遗憾，太小了")
            else:
                print(f"预测{attempts}次，你猜中了!")
                break
        except ValueError:
            print("输入内容必须为整数!")

guess_number_v3()