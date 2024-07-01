def fun(str):
    res = []
    n = len(str)
    for i in str:
        if i == "(" or i == "[" or i == "{":
            res.append(i)
        else:
            if len(res) == 0:
                return False
            ch = res[-1]
            res.pop()
            if (i == "}" and ch == "{") or (i == "]" and ch == "[") or (i == ")" and ch == "("):
                continue
            else:
                return False
    return len(res) == 0

str = "()[{}()]"
print(fun(str))