class player:
    # HP:生命值 MP：法力值 AD：物理攻击 AP：法力攻击：DEF 物理防御：MDEF：魔法防御
    def __init__(
        self, name: str, HP: int, MP: int, AD: int, AP: int, DEF: int, MDEF: int
    ):
        self.name = name
        self.HP = 100
        self.MP = 100
        self.AD = 0
        self.AP = 0
        self.DEF = 0
        self.MDEF = 0
