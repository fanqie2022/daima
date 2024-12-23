def is_palindrome(number):
    return str(number) == str(number)[::-1]

def check_palindromes():
    number = int(input("Enter a 5-digit number: "))
    if len(str(number)) != 5:
        print("Please enter a 5-digit number.")
    else:
        if is_palindrome(number):
            print(f"{number} is a palindrome.")
        else:
            print(f"{number} is not a palindrome.")

# 检查输入的5位数字是否为回文数
check_palindromes()