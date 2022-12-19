"""该模块为 seekDick 的主模块。
"""

def seek_dick(name_: str, gender_: str):
    """该函数根据给定的 name 和 gender 变量，判定此对象是否有 Dick。

    Args:
        name_ (str): 给定判定对象的姓名。
        gender_ (str): 给定判定对象的性别。
    """

    if name_ == "嘤嘤饭":
        return False
    elif gender_ == "男性":
        return True
    elif gender_ == "女性":
        return False
    else:
        return 2


while True:
    name = input("输入判定对象的姓名 >")
    gender = input("输入判定对象的性别（男性/女性/其他性别）>")
    if seek_dick(name, gender):
        print(f"{name} hasDick")
    elif not seek_dick(name, gender):
        print(f"{name} noDick")
    else:
        print(f"{name} notSureHasOrNoDick")
