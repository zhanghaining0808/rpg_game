from rpg.player import Player
from rpg.equipment_resources import pj


class Game:
    def __init__(self) -> None:
        # 这里编写一个游戏的开始逻辑

        # 比如新建角色进行游戏等。。。

        # 后续你自己写全属性，这里暂时这样
        zhn = Player(
            name="张海宁", HP=100, MP=100, AD=50, AP=50, AS=20, CRT=20, DEF=50, MDEF=50
        )

        # 给这个玩家装备 装备
        # 比如添加破军
        zhn.add_equipment(pj)

        # 查看装备属性有没有应用到玩家身上
        # 结果应该是150
        print(f"玩家{zhn.name}的攻击力有{zhn.AD}")
