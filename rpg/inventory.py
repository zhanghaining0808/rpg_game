class inventory:
    def weapon(
        self,
        name: str,
        AD: int,
        AP: int,
    ):
        self.name = name
        self.AD = 0
        self.AP = 0

    def armor(self, name: str, DEF: int, MDEF: int):
        self.name = name
        self.DEF = 0
        self.MDEF = 0

    def Potion(self, name: str, HP: int, MP: int):
        self.name = name
        self.HP = 0
        self.MP = 0
