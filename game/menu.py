from view import inventory
from add import Add_equipment
from move import Remove_equipment


# 选项栏的框架
def choice():
    while True:
        print("🌙1.查看装备栏")
        print("🌙2.添加装备")
        print("🌙3.移除装备")
        print("🌙4.查看玩家状态")
        print("🌙5.开始战斗")
        print("🌙6.退出游戏")

        choice = input("请输入数字选项: ")
        if choice == "1":
            inventory()

        elif choice == "2":
            Add_equipment()

        elif choice == "3":
            Remove_equipment()
            break
        elif choice == "4":
            None
        elif choice == "5":
            print("战斗开始")
        elif choice == "6":
            print("退出游戏")
        else:
            print("🔴🔴🔴请重新输入🔴🔴🔴")
    return
