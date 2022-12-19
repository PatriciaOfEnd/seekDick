"""该模块为 seekDick 的主模块。
"""

from seekDick import seek_dick

while True:
    name = input("输入判定对象的姓名 >")
    gender = input("输入判定对象的性别（男性/女性/其他性别）>")
    if seek_dick(name, gender) is True:
        print(f"{name} hasDick")
    elif seek_dick(name, gender) is False:
        print(f"{name} noDick")
    else:
        print(f"{name} notSureHasOrNoDick")
