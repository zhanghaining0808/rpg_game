from inventory import Inventory


class Equipment(Inventory):
    def __init__(self, name: str) -> None:
        self.name = name


# AD:物理攻击 AP:魔法攻击 AS:攻击速度  CRT:暴击率
class Weapon(Equipment):
    def __init__(
        self,
        name,
        AD: int,
        AP: int,
        AS: int,
        CRT: int,
    ) -> None:
        super().__init__(name)
        self.AD = AD
        self.AP = AP
        self.AS = AS
        self.CRT = CRT


# Armor：防具 DEF:物理防御 MDEF:魔法防御
class Armor(Equipment):
    def __init__(
        self,
        name: str,
        DEF: int,
        MDEF: int,
    ) -> None:
        super().__init__(name)
        self.DEF = DEF
        self.MDEF = MDEF


# Potion:药水 HP:回血 MP：回蓝
class Potion(Equipment):
    def __init__(self, name: str, HP: int, MP: int) -> None:
        super().__init__(name)
        self.HP = HP
        self.MP = MP
