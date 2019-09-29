"""
题目
任意给出一个字符串，例如”dfdWIUdfadfIkadfPPP”，求出这个字符串中大写字母和小写字母的数量。
"""

String = "dfdWIUdfadfIkadfPPP"

NumLower = 0        # 小写字母数量
NumCapital = 0      # 大写字母数量

for Char in String:
    if 'a' <= Char <= 'z':
        NumLower += 1
    elif 'A' <= Char <= "Z":
        NumCapital += 1
    else:
        print(Char, "不是英文字母.")
else:
    print("在", String, "中:")
    print("大写字母:", NumCapital, "个")
    print("小写字母:", NumLower, "个")
