# 第二章Python基础入门
# 1.	gbk，utf-8，ascii，unicode
#
# 2.	1.>print变为内置函数需要加括号
#     2.>isinstance判断变化
#     3.>增加了新式类
#     4.>range和xrange合并为range（生成器）
#     5.>编码统一使用utf-8
#
# 3.	1.str，int，

value = """51devops"niubi"""

print("""
    ⽂能提笔安天下,
    武能上⻢定乾坤.
    ⼼存谋略何⼈胜,
    古今英雄唯是君。
    """)

# 数字，字母下滑下划线组合而成，不能以数字开头，不要以关键字命名。命名要有意义，尽量使用驼峰命名法或者小驼峰还有下划线命名法
#
# name = '51devops'
# _ = 'echo'
#
# if 条件语句：
#         满足条件执行的语句
#     elif 条件语句：
#         满足条件执行的语句
#     else：
#         满足条件执行的语句

num = int(input("输入所猜数字："))
if num > 66:
    print("猜大了")
elif num < 66 :
    print("猜小了")
else:
    print("猜对了")

achivement = int(input("请输入成绩："))
if achivement > 0:
    print('E')
elif achivement >39:
    print('D')
elif achivement >59:
    print('C')
elif achivement > 79:
    print('B')
elif 89 < achivement <= 100:
    print('A')


while 1:
    print(
    '''
    菜单：
        1：固网业务
        2：查话费
        3：话费充值
        *：退出
    ''')
    num = input("请选择：")
    if num == '1':
                print('''
                1.xxxxx
                2.yyyyyyy
            ''')
    elif num == '2':
                print('您的话费余额为：999999999999')
    elif num == '3':
                input("请输入充值金额：")
                print("充值成功")
    elif num == '*':
        print('结束')
        break
# 第三章Python条件语句和运算符
# 1.猜数字，设定一个理想数字比如：66，让用户输入数字，如果比66大，则显示猜测的结果大了；如果比66小，则显示猜测的结果小了;只有等于66，显示猜测结果正确，然后退出循环。
while 1:
    num = int(input("输入所猜数字："))
    if num > 66:
        print("猜大了")
    elif num < 66 :
        print("猜小了")
    else:
        print("猜对了")
        break
# # 2.在上一题的基础，设置：给用户三次猜测机会，如果三次之内猜测对了，则显示猜测正确，退出循环，如果三次之内没有猜测正确，则自动退出循环，并显示‘大笨蛋’。
count = 0
while count < 3:
    num = int(input("输入所猜数字："))
    count += 1
    if num > 66:
        print("猜大了")
    elif num < 66:
        print("猜小了")
    else:
        print("猜对了")
        break
else:
    print("笨蛋")

# 3.使用两种方法实现输出 1 2 3 4 5 6 8 9 10 。
for i in range(1, 11):
    print(i)
i = 0
while i < 10:
    i += 1
    print(i)

# 4.求1-100的所有数的和
print(sum(range(11)))
# 5.输出 1-100 内的所有奇数
for i in range(1,101,2):
    print(i)
# 6.输出 1-100 内的所有偶数
for i in range(1,101,2):
    print(i)
# 7.求1-2+3-4+5 … 99的所有数的和
n = 0
for i in range(1,100):
    if i%2 ==0:
        n += i
    else:
        n -= i
print(n)
# 8.⽤户登陆（三次输错机会）且每次输错误时显示剩余错误次数（提示：使⽤字符串格式化）
i = 0
while i < 3:
    i += 1
    pwd = input("请输入密码：")
    if pwd == "123":
        print("三号技师为您服务")
    else:
        print("密码错误，您还有{}次服务".format(3 - i))
else:
    print("暗号错误，不接待")

# 9.猜年龄游戏
# 要求：允许用户最多尝试3次，3次都没猜对的话，就直接退出，如果猜对了，打印恭喜信息并退出。
while 1:
    num = int(input("输入所猜年龄："))
    if num > 66:
        print("猜大了")
    elif num < 66 :
        print("猜小了")
    else:
        print("猜对了")
        break

# 10.猜年龄游戏升级版
# 要求：允许用户最多尝试3次，每尝试3次后，如果还没猜对，就问用户是否还想继续玩，如果回答Y，就继续让其猜3次，以此往复，如果回答N，就退出程序，如何猜对了，就直接退出。

while 1:
    i = 0
    while i < 3:
        i += 1
        num = int(input("输入所猜数字："))
        if num > 66:
            print("猜大了")
        elif num < 66 :
            print("猜小了")
        else:
            print("猜对了")
            break
    else:
        ans = input("还想要么？")
        if ans == "Y":
            continue
        else:
            break





# 第四章Python的数据类型之字符串和整型
name = "szk zeNb "
# 移除 name 变量对应的值两边的空格,并输出处理结果
print(name.strip())
# 判断 name 变量是否以 “sz” 开头,并输出结果（用切片）
name.startswith("sz")
print(name[0:3] == "sz")
# 判断name变量是否以”Nb”结尾,并输出结果（用切片）
print(name[-1:-3] == "Nb")
# 将 name 变量对应的值中的 所有的”z” 替换为 “p”,并输出结果
print(name.replace("z", "p"))
# 将name变量对应的值中的第一个”z”替换成”p”,并输出结果
print(name.replace("z", "p", 1))
# 将 name 变量对应的值根据 所有的”z” 分割,并输出结果
a = name.split("z")
print(a)
# 将name变量对应的值根据第一个”z”分割,并输出结果
print(name.split("z", 1))
# 将 name 变量对应的值变大写,并输出结果
print(name.upper())
# 将 name 变量对应的值变小写,并输出结果
print(name.lower())
# 请输出 name 变量对应的值的第 2 个字符?
print(name[1])
# 请输出 name 变量对应的值的前 3 个字符?
print(name[0:3])
# 请输出 name 变量对应的值的后 2 个字符?
print(name[-3:])

s = "123a4b5c"
# 通过对s切片形成新的字符串 “123”
new_s = s[0:3]
print(new_s)
# 通过对s切片形成新的字符串 “a4b”
new_s = s[3:6]
print(new_s)
# 通过对s切片形成字符串s5,s5 = “c”
new_s = s[-1]
print(new_s)
# 通过对s切片形成字符串s6,s6 = “ba2”
new_s = s[::-1][2::2]
print(new_s)

s = "asdfer"
# 使用while和for循环字符串 s=”asdfer” 中每个元素。
index = 0

while index < len(s):
    print(s[index])
    index += 1
print("_____________")
for i in s:
    print(i)

# 使用while和for循环分别对字符串 message = “伤情最是晚凉天，憔悴厮人不堪言。” 进行打印。
message = "伤情最是晚凉天，憔悴厮人不堪言。"
index = 0

while index < len(message):
    print(message[index])
    index += 1


for i in message:
    print(i)
# 获取用户输入的内容，并计算前四位”l”出现几次,并输出结果。
content = input("请输入内容")
print(content.count("a"))
# 获取用户两次输入的内容，并将所有的数据获取并进行相加，如：
text1 = input("请输入内容:")
text2 = input("请输入第二次内容:")
print("{}{}".format(text1,text2))
# 写代码实现判断用户输入的值否以 "al"开头,如果是则输出 "是的" 否则 输出 "不是的"
str1 = "alqqq"
print("是的") if str1.startswith("cc") else print("不是")
# 写代码实现判断用户输入的值否以"Nb"结尾,如果是则输出 "是的" 否则 输出 "不是的"
print("是的") if str1.endswith("Nb") else print("不是")
# 将 name 变量对应的值中的 所有的"l"替换为 "p",并输出结果
name = "lpsdfafa"
print(name.replace("l","p"))
# 写代码实现对用户输入的值判断，是否为十进制小数（isdecimal），如果是则转换为整型并输入，否则直接输出"请输入数字"
in_text = input("请输入内容：")
print(int(in_text)//0) if in_text.isdecimal() else print("请输入数字")
# 对用户输入的数据使用"+"切割，判断输入的值是否都是数字？	提示：用户输入的格式必须是以+连接，如 5+9 、devops+999
num = input("请输入内容：（请用+连接）")
for i in num.split("+"):
    print(i.isalnum())

# 写代码实现一个整数加法计算器(两个数相加)
num = input("请输入内容：（数字+数字）")
num_sum = 0
for i in num.split("+"):
    if i.isalnum():
        i = int(i)
        num_sum += i
print(num_sum)

# 需求：提示用户输入：5+9或5+9或5+9，计算出两个值的和（提示：先分割再转换为整型，再相加）


a = 0
for i in range(11):
    a += i
    print(a)

for i in range(1, 11, 2):
    print(i)

for i in range(1, 11):
    if i % 2 == 0:
        print(i)

a = 0
for i in range(1, 11):
    if i % 2 == 0:
        a -= i
    else:
        a += i
print(a)

num_list = []
for i in range(1, 101, 2):
    num_list.append(i)

for i in range(50):
    if i % 3 == 0:
        num_list.append(i)

for i in list(range(1, 100))[::-1]:
    # print(i)0
    pass

num3_list = []
num4_list = []
for i in range(1, 30):
    if i % 3 == 0:
        num3_list.append(i)
    elif i % 4 == 0:
        num4_list.append(i)

li = ["pounds", "szk", "haoda", "barry", "devops"]
print(len(li))
print(li[1::2])
li.append("seven")
li.insert(0, "Tony")
li.insert(1, "Kelly")
li.remove("haoda")
li.pop(1)
for i in li[1:3]:
    li.remove(i)

li = [1, 3, 2, "a", 4, "b", 5, "c"]
print(li[0:3])
print(li[3:5])
print(li[0::2])
print(li[1::2])
print(li[-1::])
print(li[5::-2])

lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
lis[2] = lis[2].upper()
print(lis)

users = ["szk", "pounds", "波姐"]
for i, j in enumerate(users):
    print(i, j)

# googs = ['汽车','飞机','火箭']
# googs_num = input("googs_num:")
# print(googs[int(googs_num)])

li = "szk"
print("_".join(list(li)))

num8_list = [i + 1 for i in range(0, 100, 2)]
print(num8_list)
num9_list = [i for i in range(0, 100) if i % 3 == 0]
print(num9_list)

dic = {
    'k1': "v1",
    "k2": "v2",
    "k3": [11, 22, 33]
}

dic["k4"] = "v4"
dic["k1"] = "alex"
dic["k3"].append(44)
dic["k3"].insert(0, 18)
print(dic)

dic1 = {
    'name': ['pounds', 2, 3, 5],
    'job': 'teacher',
    '51devops': {'szk': ['python1', 'python2', 100]}
}

dic1["name"].append('xxx')
dic1["name"][0] = dic1["name"][0].replace("p", "P")
print(dic1)

info = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
key_list = [i for i in info.keys()]
value_list = [i for i in info.values()]
print(key_list)
print(value_list)

dic = {'k1': 'v1', 'k2': 'v2', 'k3': [11, 22, 33]}
for value in dic.values():
    print(value)

for key in dic.keys():
    print(key)

for key, value in zip(dic.keys(), dic.values()):
    print(key, value)

dic.setdefault("k4", "v4")
dic['k1'] = "szk"
dic["k3"].append(44)
dic["k3"].insert(1, 18)

info = {
    'k1': 'v1',
    'k2': [('pounds'), ('szk'), ('51devops')],
}
for value in info['k2']:
    print(value)

goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998}
]

while 1:
    good = {}

    for id, good_message in enumerate(goods):
        good_message.setdefault("id", id)
        good[id] = good_message
        print(good[id]["id"], good[id]["name"], good[id]["price"])

    print("退出请按q或Q")
    print("_________________________________")
    goods_id = input("请输入商品编号：")

    try:
        goods_id = int(goods_id)

        if goods_id <= len(good):
            print(good[goods_id]["id"], good[goods_id]["name"], good[goods_id]["price"])
        else:
            print("输入有误！")

    except:
        if goods_id == "q" or goods_id == "Q":
            break
        else:
            print("输入有误！")
