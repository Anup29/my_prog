def insertion_sort(arr):
    n = len(arr)
    for i in range(n):
        j = i
        while(j>0 and arr[j-1] > arr[j]):
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1
    return arr

arr = [11,2,4,1,5]
# print(insertion_sort(arr))


def palind(str):
    n = len(str)
    str1 = ""
    for i in range(n-1,-1,-1):
        str1 += str[i]
    print(str1)
    if str == str1:
        print("Palindrome")
    else:
        print("not")

str = "aba"
palind(str)

def merge_dict(d1, d2):
    for k,v in d2.items():
        d1[k] = v
    print(d1)

d1 = {"a":1, "b":2,"c":3}
d2 = {"d":4}
# merge_dict(d1,d2)
print(d1.update(d2))
print(d1)

def count_fre():
    with open("hosts.txt","r") as f_ob:
        s = f_ob.read()
        d = {}
        l = ' '.join(s.splitlines()).split()
        for i in l:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1

    print(d)
count_fre()


def add_upto(arr,t):
    n = len(arr)
    s = 0
    start = -1
    startInd,endInd = 0,0
    for i in range(n):
        if s == 0:
            start = i
        s += arr[i]

        if s == t:
            print("found")
            startInd= start
            endInd = i
            print(startInd, endInd)
            break
        if s > t:
            s = 0
        if s < t :
            continue
arr = [2, 11, 7, 17]
t = 9
add_upto(arr,t)