# 定义一个对象数组，每个元素包括name和salary两个属性
# 遍历数组，输出每个元素的name和salary属性
# 输出格式为：name好，瓦特合作办学项目绩效salary元（税前)，已随年终绩效发放，董部长委托我通知您，请查收。祝假期愉快[庆祝][庆祝]
# name和salary之间没有空格，salary和元之间没有空格，元和（税前)之间没有空格
# 输出完一个元素后换行，输出完所有元素后换行
# 代码如下：

class Pay:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

pays = [Pay('张三', 10000), Pay('李四', 20000), Pay('王五', 30000)]
for pay in pays:
    print(pay.name + '好，瓦特合作办学项目绩效' + str(pay.salary) + '元（税前)，已随年终绩效发放，董部长委托我通知您，请查收。祝假期愉快[庆祝][庆祝]')
print()
# 输出结果为：
# 张三好，瓦特合作办学项目绩效10000元（税前)，已随年终绩效发放，董部长委托我通知您，请查收。祝假期愉快[庆祝][庆祝]


# pay2023 = [
#     {'name': "洪老师", 'salary': 10080},
#     {'name': "曲老师", 'salary': 21360},
#     {'name': "夏老师", 'salary': 2000},
#     {'name': "董老师", 'salary': 2000},
#     {'name': "顾部长", 'salary': 4000},
#     {'name': "宋书记", 'salary': 4000},
#     {'name': "黄书记", 'salary': 4000},
#     {'name': "王主任", 'salary': 4000}
# ]
# for person in pay2023:
#     print(person['name'], "好，瓦特合作办学项目绩效", person['salary'], "元（税前)，已随年终绩效发放，董部长委托我通知您，请查收。祝假期愉快[庆祝][庆祝]", sep="")
#     print()




