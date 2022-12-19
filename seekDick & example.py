def seekDick(name,gender):
    if name == "嘤嘤饭":
        return (False)
    elif gender == "男性":
        return (True)
    elif gender == "女性":
        return (False)
    else:
        return (2)

while (True):
    n,g=input ("输入姓名和性别（男性/女性/其他性别），以空格隔开>").split()
    if seekDick(n,g) == True:
        print ("hasDick")
    elif seekDick(n,g) == False:
        print ("noDick")
    else:
        print ("notSureHasOrNoDick")
