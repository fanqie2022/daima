def count_characters():
    text = input("请输入一行字符: ")
    counts = {'字母': 0, '数字': 0, '空格': 0, '其他': 0}
    for char in text:
        if char.isalpha():
            counts['字母'] += 1
        elif char.isdigit():
            counts['数字'] += 1
        elif char.isspace():
            counts['空格'] += 1
        else:
            counts['其他'] += 1
    print(counts)

count_characters()