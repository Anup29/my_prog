#lambda function:

# multiply = lambda a,b : a*b
# print(multiply(4,5))

# recursion fibonacci of nth term
# def recur(n, dp):
#     if n <= 1:
#         return n
#     if dp[n] != -1:
#         return dp[n]
#
#     dp[n] = recur(n-2, dp) + recur(n-1, dp)
#     return dp[n]
#
# n = 8
# dp = [-1] * (n+1)
# print(recur(n,dp))

## Decorator
# def my_decor(func):
#     def wrapper():
#         print("Before func call..")
#         func()
#         print("After func call..")
#     return wrapper
#
# @my_decor
# def my_fucn():
#     print("Hello")
#
# my_fucn()

# *args and **kwargs
# def my_fun(*args, **kwargs):
#     for arg in args:
#         print(arg)
#     for k,v in kwargs.items():
#         print(f"key:{k}, value:{v}")
#
# my_fun(1,2,3,x=4,y=5)

# # Generator
# def fun(n):
#     count =1
#     while count<=n:
#         yield count
#         count += 1
# print(list(fun(5)))

# Threading
# import threading
# def fun1():
#     for i in range(1,6):
#         print(i,end="**")
# def fun2():
#     for i in 'abcde':
#         print(i,end="##")
#
# t1 = threading.Thread(target=fun1)
# t2 = threading.Thread(target=fun2)
# t1.start()
# t2.start()
# t1.join()
# t2.join()

# sort dict by values

# d = {'apple': 15,'cherry': 20, 'banana': 10 }
# sorted_d = dict(sorted(d.items(), key=lambda item: item[1]))
# print(sorted_d)

# magic function or dunder function
# allow developers to emulate built-in behavior or implement operator overloading
# class Books:
#     def __init__(self, pages):
#         self.pages = pages
#
#     def __add__(self, other):
#         return Books(self.pages + other.pages)
#
# book1 = Books(100)
# book2 = Books(200)
# book3 = book1 + book2
# print(book3.pages)

# merge dictionaries
# d1 = {'a': 1, 'b': 2}
# d2 = {'b': 3, 'c': 4}
# print({**d1, **d2})

# @property decorator: allows you yo define methods in a class that can be accessed like attributes
# without calling them as a method.
# class Circle:
#     def __init__(self, radius):
#         self.__radius = radius
#
#     @property
#     def diameter(self):
#         return self.__radius * 2
#
# c = Circle(5)
# print(c.diameter)

# filer out all strings which are palindrome
# def find_palindrome(words):
#     for w in words:
#         if w.lower() == w[::-1].lower():
#             print(w)
# words = ["radar", "python", "level", "world"]
# find_palindrome(words)

# def flatten(lst):
#     # Flatten a nested list
#     res = []
#     for i in lst:
#         if isinstance(i,list):
#             res.extend(flatten(i))
#         else:
#             res.append(i)
#     return res
#
# nested_list = [1, [2, 3, [4, 5]], 6]
# print(flatten(nested_list))

#Most repeated char in a string
def char_count(s):
    d = {}
    for i in s:
        if i not in d.keys():
            d[i] = 1
        else:
            d[i] += 1
    print(d)
    print(sorted(d.items(), key=lambda item: item[1],reverse=True))

s = "aavvvsssrrrrr"
char_count(s)

def find_ele(arr, target):
    n = len(arr)
    l = 0
    h = n-1
    while l <= h:
        mid = (l+h)//2
        if target == arr[mid]:
            return mid
        if arr[l] <= arr[mid]:
            if arr[l]<=target<=arr[mid]:
                h = mid - 1
            else:
                l = mid + 1
        else:
            if arr[mid]<=target<=arr[h]:
                l = mid + 1
            else:
                h = mid - 1


arr = [7, 8, 1, 2, 3, 4, 5, 6]
# arr.sort()
print(arr)
print(find_ele(arr,5))


def find_two_pair_sum(arr, target):
    n = len(arr)
    left = 0
    right = n - 1
    while left < right:
        s = arr[left] + arr[right]
        if s == target:
            print("Yes")
            break
        elif s < target:
            left += 1
        else:
            right -= 1
    else:
        print("No")
arr = [2,6,5,8,11]
target = 13
find_two_pair_sum(arr,target)


def fibo(k):
    prev2 = 0
    prev1 = 1
    # print(prev2)
    # print(prev1)
    for i in range(2,k):
        curr = prev2 + prev1
        print(curr)
        prev2 = prev1
        prev1 = curr
    # print(prev1)
# fibo(7)

"""
Input: a given file having some words -
       e.g.  cat cat dog cat hen hen
Output: a file - cat4 dog1 hen2
"""
with open("hosts.txt","r") as f_obj:
    ob = f_obj.readline()

print(type(ob))
r = ob.split()
d = {}
for i in r:
    d[i] = r.count(i)

print(d)

"""
Shift all 0 to right
Input: [5, 6, 0, 1, 0, 10, 0, 2, 0]
Output: [5, 6, 1, 10, 2, 0, 0, 0, 0]
"""
arr = [5, 6, 0, 1, 0, 10, 0, 2, 0]
r = []
z = arr.count(0)
print(z)
for i in arr:
    if i!=0:
        r.append(i)
s = r.extend([0] * z)
print(r)

"""
find the count of unique characters present in the string
Input: FUNNY
OUTPUT: 4
"""
arr = "FUNNY"
s = set(arr)
print(s,len(s))
"""
Now remove the characters till one character is left.
FUNNY -> FUNY -> FUY -> FU -> F
OUTPUT: F 
"""
n = len(arr)
for i in range(n-1,-2,-1):
    # arr.
    arr.replace(arr[i]," ")
print(arr)
