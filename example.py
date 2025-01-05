# 1. 基础数据类型和打印
name = "小明"
age = 25
height = 1.75
is_student = True

print(f"姓名：{name}")
print(f"年龄：{age}")

# 2. 简单的函数定义
def greet(name):
    return f"你好，{name}！"

# 3. 列表操作
fruits = ["苹果", "香蕉", "橙子"]
for fruit in fruits:
    print(f"我喜欢吃{fruit}")

# 4. 简单的条件判断
if age >= 18:
    print("已成年")
else:
    print("未成年")

# 5. while 循环示例
count = 0
while count < 3:
    print(f"当前计数：{count}")
    count += 1 