# 管理玩家的装备栏
equipment = ["金铲铲", "金锅锅"]


def inventory():
    # 查看装备栏
    while True:
        print("当前你拥有的装备是:一个金铲铲和一个金锅锅 ")
        print("⭐1.返回主菜单")
        print("⭐2.金铲铲能合成的转职")
        print("⭐3.金锅锅能合成的转职")
        choices = input("请选择下一步操作：")
        if choices == "1":
            from menu import choice
        elif choices == "2":
            print("金铲铲+暴风大剑=咖啡甜心")
            print("金铲铲+反曲弓=炎魔")
            print("金铲铲+锁子甲=冰霜")
            print("金铲铲+负极斗篷=诅咒女巫")
            print("金铲铲+大棒=次元术士")
            print("金铲铲+眼泪=花仙子")
            print("金铲铲+巨人腰带=魔神使者")
            print("金铲铲+拳套=小蜜蜂")
            print("金铲铲+金铲铲=金铲铲冠冕")
            print("金铲铲+金锅锅=金锅铲冠冕")
            print("⭐1.返回上一次操作")
            print("⭐2.返回主菜单")
            choices = input("请选择进行下一步操作：")

            if choices == "1":
                inventory()
            elif choices == "2":
                from menu import choice
            else:
                print("🔴🔴🔴请重新输入🔴🔴🔴")
                return

        elif choices == "3":
            print("金锅锅+暴风大剑=猎手")
            print("金锅锅+反曲弓=魔战士")
            print("金锅锅+锁子甲=堡垒卫士")
            print("金锅锅+负极斗篷=复苏者")
            print("金锅锅+大棒=法师")
            print("金锅锅+眼泪=学者")
            print("金锅锅+巨人腰带=换型师")
            print("金锅锅+拳套=狂暴战士")
            print("金锅锅+金铲铲=金锅铲冠冕")
            print("金锅锅+金锅锅=金锅锅冠冕")
            print("⭐1.返回上一次操作")
            print("⭐2.返回主菜单")
            choices = input("请选择进行下一步操作：")

            if choices == "1":
                inventory()
            elif choices == "2":
                from menu import choice
            else:
                print("🔴🔴🔴请重新输入🔴🔴🔴")
                return
        else:
            print("🔴🔴🔴请重新输入🔴🔴🔴")
            return
        break
    exit
