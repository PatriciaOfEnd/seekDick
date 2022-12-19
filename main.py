"""该模块为 seekDick 的主模块。
"""

def seek_dick(name: str, gender: str):
    """该函数根据给定的 name 和 gender 变量，判定此对象是否有 Dick。

    Args:
        name (str): 给定判定对象的姓名。
        gender (str): 给定判定对象的性别。
    """

    if name == "嘤嘤饭":
        return False
    elif gender == "男性":
        return True
    elif gender == "女性":
        return False
    else:
        return 2


while True:
    n, g = input("输入姓名和性别（男性/女性/其他性别），以空格隔开>").split()
    if seek_dick(n, g):
        print("hasDick")
    elif not seek_dick(n, g):
        print("noDick")
    else:
        print("notSureHasOrNoDick")
