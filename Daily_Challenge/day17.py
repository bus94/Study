# 20240918 day17.py

# day17 문자열


'''
문자열 myString과 pat가 주어집니다. myString의 부분 문자열중 pat로 끝나는 가장 긴 부분 문자열을 찾아서 return 하는 solution 함수를 완성해 주세요.

myString	pat	    result
"AbCdEFG"	"dE"	"AbCdE"
"AAAAaaaa"	"a"	    "AAAAaaaa"
'''
def solution(myString, pat):
    for i in range(len(myString)):
        if len(pat) == 1 and myString[-i-1] == pat[0]:
            return myString[:len(myString)-i]
        elif myString[i:i + len(pat)] == pat:
                return myString[:i + len(pat)]
# print(solution("AbCdEFG", "dE"))
# print(solution("AAAAaaaa", "a"))


'''
문자열 myString과 pat이 주어집니다. myString에서 pat이 등장하는 횟수를 return 하는 solution 함수를 완성해 주세요.

myString	pat	    result
"banana"	"ana"	2
"aaaa"	    "aa"	3
'''
def solution(myString, pat):
    result = 0
    for i in range(len(myString)):
        if myString[i:i + len(pat)] == pat:
            result += 1
    return result
# print(solution("banana", "ana"))
# print(solution("aaaa", "aa"))


'''
문자열 배열 strArr가 주어집니다. 
배열 내의 문자열 중 "ad"라는 부분 문자열을 포함하고 있는 모든 문자열을 제거하고 남은 문자열을 순서를 유지하여 배열로 return 하는 solution 함수를 완성해 주세요.

strArr	                        result
["and","notad","abcd"]	        ["and","abcd"]
["there","are","no","a","ds"]	["there","are","no","a","ds"]
'''
def solution(strArr):
    return [s for s in strArr if "ad" not in s]
# print(solution(["and","notad","abcd"]))
# print(solution(["there","are","no","a","ds"]))


'''
단어가 공백 한 개로 구분되어 있는 문자열 my_string이 매개변수로 주어질 때, 
my_string에 나온 단어를 앞에서부터 순서대로 담은 문자열 배열을 return 하는 solution 함수를 작성해 주세요.

my_string	    result
"i love you"	["i", "love", "you"]
"programmers"	["programmers"]
'''
def solution(my_string):
    return my_string.split(" ")
# print(solution("i love you"))
# print(solution("programmers"))


'''
단어가 공백 한 개 이상으로 구분되어 있는 문자열 my_string이 매개변수로 주어질 때, 
my_string에 나온 단어를 앞에서부터 순서대로 담은 문자열 배열을 return 하는 solution 함수를 작성해 주세요.

my_string	            result
" i    love  you"	    ["i", "love", "you"]
"    programmers  "	    ["programmers"]
'''
def solution(my_string):
    return my_string.strip().split()
# print(solution(" i    love  you"))
# print(solution("    programmers  "))