from rpg.equipment import Weapon, Armor, Potion

# 用来放装备资源 具体的装备等
# 武器
pj = Weapon("破军", AD=100)
wjzr = Weapon("无尽之刃", AD=50, CRT=40)
sdbs = Weapon("闪电匕首", AD=30, AS=15)
sxc = Weapon("碎星锤", AD=30)
hxzz = Weapon("回响之杖", AP=30, CRT=20)
tkmj = Weapon("痛苦面具", AP=40, CRT=20)
# 防具
bxzz = Armor("不祥征兆", DEF=50, HP=100)
fscj = Armor("反伤刺甲", DEF=80)
jhfb = Armor("极寒风暴", DEF=30, MDEF=30)
mndp = Armor("魔女斗篷", MDEF=80)
bsnzy = Armor("不死鸟之眼", MDEF=50, HP=40)
# 药水
xb = Potion("血包", HP=60)
fb = Potion("法包", HP=60)
