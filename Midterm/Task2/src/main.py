# 学生管理系统

# PS: 可以仅以 “姓名” / “学号” 来代指学生信息
import json
STU_LIST = []
STU_FILE = "P-2024-plan\Midterm\Task2\src\students.json"

def stu_init():
    global STU_LIST
    """此函数用于, 从文件中, 初始化学生信息"""
    try:
        with open(STU_FILE,'r',encoding='utf-8') as file:
            STU_LIST = json.load(file)
    except FileNotFoundError:
        print("文件未找到，将创建新文件。")
        with open(STU_FILE,'w',encoding='utf-8')as file:
            json.dump([],file)
    pass


def get_choice() -> int:
    """此函数用于, 在命令行里, 获取用户输入的选项"""
    choice = input("请选择一个操作： ")
    return int(choice)
    pass


def menu():
    """此函数用于, 在命令行里, 打印出菜单"""
    print("学生信息管理系统")
    print("1.添加学生")
    print("2.删除学生")
    print("3.修改学生信息")
    print("4.查询学生信息")
    print("0.退出系统")
    pass


def exec(user_choice: int):
    """此函数用于, 根据用户输入的选项, 执行相应的功能"""
    if user_choice == 1:
        stu_add()
    elif user_choice == 2:
        stu_del()
    elif user_choice == 3:
        stu_mod()
    elif user_choice == 4:
        stu_sel()
    else:
        print("无效选择，请重新输入")
    pass


def stu_add():

    """此函数用于, 添加学生信息"""
    name = input("请输入学生姓名：")
    id = input("请输入学生学号: ")
    phone = input("请输入学生电话： ")
    STU_LIST.append({'name':name,'id':id,'phone':phone})
    stu_save()
    print(f"学生{name}已添加。")
    pass


def stu_del():
    """此函数用于, 删除学生信息"""
    name = input("请输入学生姓名：")
    for student in STU_LIST:
        if student['name'] == name:
            STU_LIST.remove(student)
            stu_save()
            print(f"学生{name}已删除。")
    pass


def stu_mod():
    """此函数用于, 修改学生信息"""
    name = input("请输入学生姓名：")
    for student in STU_LIST:
        if student['name'] == name:
            newname = input("请输入学生姓名：")
            newid = input("请输入学生学号: ")
            newphone = input("请输入学生电话： ")
            student['name']=newname
            student['id']=newid
            student['phone']=newphone
            stu_save()
            print(f"学生{name}已更新")
    pass


def stu_sel():
    """此函数用于, 查询学生信息"""
    name = input("请输入学生姓名：")
    for student in STU_LIST:
        if student['name'] == name:
            print(f"学生姓名:{student['name']}\n学号:{student['id']}\n电话:{student['phone']}")
    pass


def stu_save():
    """此函数用于, 将学生信息保存到文件中"""
    with open(STU_FILE,'w',encoding='utf-8') as file:
        json.dump(STU_LIST,file,ensure_ascii=False,indent=4)
    pass

def main():
    """尽量不要修改此函数的代码, 此函数用于全局调用"""
    stu_init()
    menu()
    user_choice = get_choice()
    while user_choice != 0:
        exec(user_choice)
        menu()
        user_choice = get_choice()
    pass


if __name__ == '__main__':
    main()
