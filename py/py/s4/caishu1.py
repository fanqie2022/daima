import random

def guess_number_v2():
    number = random.randint(0, 100)
    attempts = 0
    while True:
        user_guess = int(input("请输入一个0-100之间的整数: "))
        attempts += 1
        if user_guess > number:
            print("遗憾，太大了")
        elif user_guess < number:
            print("遗憾，太小了")
        else:
            print(f"预测{attempts}次，你猜中了!")
            break

guess_number_v2()