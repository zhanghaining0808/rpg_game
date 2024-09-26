class player:
    # CRT : 暴击率
    # HP:生命值 MP：法力值 AD：物理攻击 AP：法力攻击：AS:攻击速度 DEF：物理防御：MDEF：魔法防御
    def __init__(
        self,
        name: str,
        HP: int,
        MP: int,
        AD: int,
        AP: int,
        AS: int,
        CRT: int,
        DEF: int,
        MDEF: int,
    ):
        self.name = name
        self.HP = HP
        self.MP = MP
        self.AD = AD
        self.AP = AP
        self.AS = AS
        self.CRT = CRT
        self.DEF = DEF
        self.MDEF = MDEF
