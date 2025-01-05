# 1. 基础数据类型和打印
name = "小明"
age = 25
height = 1.75
is_student = True

# 使用更规范的打印方式
def print_info():
    print(f"姓名：{name}")
    print(f"年龄：{age}")
    print(f"身高：{height}米")

# 2. 改进的函数定义
def greet(name: str) -> str:
    """
    向指定的人打招呼
    Args:
        name: 人名
    Returns:
        打招呼的字符串
    """
    return f"你好，{name}！"
    return f"你好，{name}！"
    return f"你好，{name}！"
    return f"你好，{name}！"
    return f"你好，{name}！"
    return f"你好，{name}！"
    return f"你好，{name}！"
    return f"你好，{name}！"
    return f"你好，{name}！"
    return f"你好，{name}！"

# 3. 列表操作
fruits = ["苹果", "香蕉", "橙子"]
def print_fruits():
    for fruit in fruits:
        print(f"我喜欢吃{fruit}")

# 4. 简单的条件判断
def check_age(age: int) -> None:
    if age >= 18:
        print("已成年")
    else:
        print("未成年")

# 5. while 循环示例
def count_numbers(limit: int = 3):
    count = 0
    while count < limit:
        print(f"当前计数：{count}")
        count += 1

if __name__ == "__main__":
    print_info()
    print(greet(name))
    print_fruits()
    check_age(age)
    count_numbers() 