def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

a = int(input("请输入第一个整数: "))
b = int(input("请输入第二个整数: "))

print(f"最大公约数: {gcd(a, b)}")
print(f"最小公倍数: {lcm(a, b)}")