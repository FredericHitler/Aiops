
a = 0
for i in range(11):
    a+=i
    print(a)


for i in range(1,11,2):
    print(i)


for i in range(1,11):
    if i%2 == 0:
        print(i)


a = 0
for i in range(1,11):
    if i%2 == 0:
        a -= i
    else:
        a += i
print(a)


num_list = []
for i in range(1,101,2):
    num_list.append(i)


for i in range(50):
    if i%3 == 0:
        num_list.append(i)


for i in list(range(1,100))[::-1]:
    # print(i)0
    pass


num3_list = []
num4_list = []
for i in range(1,30):
    if i%3 == 0:
        num3_list.append(i)
    elif i%4 == 0:
        num4_list.append(i)


li = ["pounds", "szk", "haoda", "barry", "devops"]
print(len(li))
print(li[1::2])
li.append("seven")
li.insert(0,"Tony")
li.insert(1,"Kelly")
li.remove("haoda")
li.pop(1)
for i in li[1:3]:
    li.remove(i)


li = [1, 3, 2, "a", 4, "b", 5,"c"]
print(li[0:3])
print(li[3:5])
print(li[0::2])
print(li[1::2])
print(li[-1::])
print(li[5::-2])


lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
lis[2] = lis[2].upper()
print(lis)


users = ["szk","pounds","波姐"]
for i,j in enumerate(users):
    print(i,j)


# googs = ['汽车','飞机','火箭']
# googs_num = input("googs_num:")
# print(googs[int(googs_num)])

li = "szk"
print("_".join(list(li)))


num8_list = [i+1 for i in range(0,100,2)]
print(num8_list)
num9_list=[ i for i in range(0,100) if i%3 == 0]
print(num9_list)


dic = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}
dic["k4"] = "v4"
dic["k1"] = "alex"
dic["k3"].append(44)
dic["k3"].insert(0,18)
print(dic)


dic1 = {
 'name':['pounds',2,3,5],
 'job':'teacher',
 '51devops':{'szk':['python1','python2',100]}
 }

dic1["name"].append('xxx')
dic1["name"][0] = dic1["name"][0].replace("p","P")
print(dic1)


info = {'k1':'v1','k2':'v2','k3':'v3'}
key_list = [i for i in info.keys()]
value_list = [i for i in info.values()]
print(key_list)
print(value_list)


dic = {'k1': 'v1', 'k2': 'v2', 'k3': [11,22,33]}
for value in dic.values():
    print(value)

for key in dic.keys():
    print(key)

for key,value in zip(dic.keys(),dic.values()):
    print(key,value)

dic.setdefault("k4","v4")
dic['k1'] = "szk"
dic["k3"].append(44)
dic["k3"].insert(1,18)


info = {
    'k1':'v1',
    'k2':[('pounds'),('szk'),('51devops')],
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

    for id,good_message in enumerate(goods):
            good_message.setdefault("id",id)
            good[id] = good_message
            print(good[id]["id"],good[id]["name"],good[id]["price"])

    print("退出请按q或Q")
    print("_________________________________")
    goods_id = input("请输入商品编号：")

    try:
        goods_id = int(goods_id)

        if goods_id<= len(good):
            print(good[goods_id]["id"], good[goods_id]["name"], good[goods_id]["price"])
        else:
            print("输入有误！")

    except:
        if goods_id == "q" or goods_id == "Q":
            break
        else:
           print("输入有误！")