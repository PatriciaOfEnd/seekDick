"""该模块用来判断传入的判定对象是否有 Dick。
"""

def seek_dick(name_: str, gender_: str):
    """该函数根据给定的 name 和 gender 变量，判定此对象是否有 Dick。

    Args:
        name_ (str): 给定判定对象的姓名。
        gender_ (str): 给定判定对象的性别。
    """

    if name_ == "嘤嘤饭":
        return False

    if gender_ == "男性":
        return True
    elif gender_ == "女性":
        return False
    else:
        return 2
