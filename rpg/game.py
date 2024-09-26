class equip:
    def __init__(
        self,
        name: str,
        AD: int,
        AP: int,
        AS: int,
        MP: int,
        CRT: int,
        DEF: int,
        MDEF: int,
        HP: int,
    ) -> None:
        {
            "破军": {AD: 100},
            "无尽之刃": {AD: 50, CRT: 40},
            "闪电匕首": {AD: 30.0, AS: 15},
            "碎星锤": {AD: 30},
            "回响之杖": {AP: 30, CRT: 20},
            "不祥征兆": {DEF: 50, HP: 100},
            "反伤刺甲": {DEF: 80},
            "极寒风暴": {DEF: 30, MDEF: 30},
            "魔女斗篷": {MDEF: 80},
            "不死鸟之眼": {MDEF: 50, HP: 40},
            "血包": {HP: 60},
            "法包": {MP: 60},
        }
