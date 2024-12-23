import random


def guess_number_game():
    number_to_guess = random.randint(0, 9)
    attempts = 0

    while True:
        try:
            user_guess = int(input("请输入你猜测的数字（0-9）："))
            attempts += 1

            if user_guess < number_to_guess:
                print("太小了!")
            elif user_guess > number_to_guess:
                print("太大了!")
            else:
                print(f"恭喜你，猜对了!你总共猜了{attempts}次。")
                break
        except ValueError:
            print("请输入一个有效的数字!")


if __name__ == "__main__":
    guess_number_game()