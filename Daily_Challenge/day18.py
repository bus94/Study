# 20240919 day18.py

# day18 문자열


'''
문자열 myString이 주어집니다. 
myString을 문자 "x"를 기준으로 나눴을 때 나눠진 문자열 각각의 길이를 순서대로 저장한 배열을 return 하는 solution 함수를 완성해 주세요.

myString	    result
"oxooxoxxox"	[1, 2, 1, 0, 1, 0]
"xabcxdefxghi"	[0, 3, 3, 3]
'''
def solution(myString):
    count = 0
    result = []
    for i in range(len(myString)):
        if myString[i] == "x":
            result.append(count)
            count = 0
        else:
            count += 1
    result.append(count)
    return result
# print(solution("oxooxoxxox"))
# print(solution("xabcxdefxghi"))
## 다른 풀이
# def solution(myString):
#     return [len(w) for w in myString.split('x')]
# x로 슬라이싱해서 그 때 나오는 값들의 길이를 리스트에 추가하는 방법을 사용했다.


'''
문자열 myString이 주어집니다. 
"x"를 기준으로 해당 문자열을 잘라내 배열을 만든 후 사전순으로 정렬한 배열을 return 하는 solution 함수를 완성해 주세요.
단, 빈 문자열은 반환할 배열에 넣지 않습니다.

myString	    result
"axbxcxdx"	    ["a","b","c","d"]
"dxccxbbbxaaaa"	["aaaa","bbb","cc","d"]
'''
def solution(myString):
    result = [s for s in myString.split("x") if not s == ""]
    result.sort()
    return result
# print(solution("axbxcxdx"))
# print(solution("dxccxbbbxaaaa"))
## 다른 풀이
# def solution(myString):
#     return sorted(s for s in myString.split('x') if s)
# boolean 타입을 기준으로 s가 빈 문자열이면 false 인 것을 이용하여 리스트 값을 반환하고, sorted로 정렬하였다.


'''
문자열 binomial이 매개변수로 주어집니다. 
binomial은 "a op b" 형태의 이항식이고 a와 b는 음이 아닌 정수, op는 '+', '-', '*' 중 하나입니다. 
주어진 식을 계산한 정수를 return 하는 solution 함수를 작성해 주세요.

binomial	        result
"43 + 12"	        55
"0 - 7777"	        -7777
"40000 * 40000"	    1600000000
'''
def solution(binomial):
    return eval(binomial)
# print(solution("43 + 12"))
# print(solution("0 - 7777"))
# print(solution("40000 * 40000"))


'''
문자 "A"와 "B"로 이루어진 문자열 myString과 pat가 주어집니다. 
myString의 "A"를 "B"로, "B"를 "A"로 바꾼 문자열의 연속하는 부분 문자열 중 pat이 있으면 1을 아니면 0을 return 하는 solution 함수를 완성하세요.

myString	pat	        result
"ABBAA"	    "AABB"	    1
"ABAB"	    "ABAB"	    0
'''
def solution(myString, pat):
    reString = ""
    for i in range(len(myString)):
        if myString[i] == "A":
            reString += "B"
        elif myString[i] == "B":
            reString += "A"
    if pat in reString:
        return 1
    return 0
print(solution("ABBAA", "AABB"))
print(solution("ABAB", "ABAB"))
## 다른 풀이
# def solution(myString, pat):
#     return int(pat in myString.replace('A', 'C').replace('B', 'A').replace('C', 'B'))
# replace를 하게 되면 모든 문자열에 적용이 되므로 이미 변경된 문자열들이 다시 바뀌는 경우가 발생한다. 
# 그래서 임의로 다른 문자로 변경한 후 두 번째 문자를 변경하고 마지막으로 첫 번째 임의로 변경한 문자를 다시 원하는 문자로 변경하는 방법을 사용했다.


'''
'm'과 "rn"이 모양이 비슷하게 생긴 점을 활용해 문자열에 장난을 하려고 합니다. 
문자열 rny_string이 주어질 때, rny_string의 모든 'm'을 "rn"으로 바꾼 문자열을 return 하는 solution 함수를 작성해 주세요.

rny_string	    result
"masterpiece"	"rnasterpiece"
"programmers"	"prograrnrners"
"jerry"	        "jerry"
"burn"	        "burn"
'''
def solution(rny_string):
    return rny_string.replace("m", "rn")
# print(solution("masterpiece"))
# print(solution("programmers"))
# print(solution("jerry"))
# print(solution("burn"))