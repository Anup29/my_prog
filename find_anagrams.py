str = ["god","plum","sun","dog","lump"]
dic = {}

for each in str:
    s = "".join(sorted(each))
    # print(s)
    if s in dic:
        dic[s].append(each)
    else:
        dic[s] = [each]


print(dic)