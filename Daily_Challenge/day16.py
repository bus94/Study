# 20240913 day16.py

# day16 문자열


'''
알파벳으로 이루어진 문자열 myString이 주어집니다. 모든 알파벳을 대문자로 변환하여 return 하는 solution 함수를 완성해 주세요.

myString    result
"aBcDeFg"   "ABCDEFG"
"AAA"       "AAA"
'''
def solution(myString):
    return myString.upper()
# print(solution("aBcDeFg"))
# print(solution("AAA"))


'''
알파벳으로 이루어진 문자열 myString이 주어집니다. 모든 알파벳을 소문자로 변환하여 return 하는 solution 함수를 완성해 주세요.

myString    result
"aBcDeFg"   "abcdefg"
"aaa"       "aaa"
'''
def solution(myString):
    return myString.lower()
# print(solution("aBcDeFg"))
# print(solution("aaa"))


'''
문자열 배열 strArr가 주어집니다. 
모든 원소가 알파벳으로만 이루어져 있을 때, 
배열에서 홀수번째 인덱스의 문자열은 모든 문자를 대문자로, 짝수번째 인덱스의 문자열은 모든 문자를 소문자로 바꿔서 반환하는 solution 함수를 완성해 주세요.

strArr                      result
["AAA","BBB","CCC","DDD"]   ["aaa","BBB","ccc","DDD"]
["aBc","AbC"]               ["abc","ABC"]
'''
def solution(strArr):
    for i in range(len(strArr)):
        if not i % 2:
            strArr[i] = strArr[i].lower()
        else:
            strArr[i] = strArr[i].upper()
    return strArr
# print(solution(["AAA","BBB","CCC","DDD"]))
# print(solution(["aBc","AbC"]))
## 다른 풀이
# def solution(strArr):
#     return [s.lower() if i % 2 == 0 else s.upper() for i, s in enumerate(strArr)]
# 처음부터 리스트를 리턴하는 문장으로 반복하여 짝수이면 lower, 홀수이면 upper가 출력될 수 있도록 한다.


'''
문자열 myString이 주어집니다. 
myString에서 알파벳 "a"가 등장하면 전부 "A"로 변환하고, "A"가 아닌 모든 대문자 알파벳은 소문자 알파벳으로 변환하여 return 하는 solution 함수를 완성하세요.

myString                result
"abstract algebra"      "AbstrAct AlgebrA"
"PrOgRaMmErS"           "progrAmmers"
'''
def solution(myString):
    return ''.join(s.upper() if s == 'a' else s.lower() if s != 'A' and s.isupper() else s for s in myString)
# print(solution("abstract algebra"))
# print(solution("PrOgRaMmErS"))
## 다른 풀이
# def solution(myString):
#     return myString.lower().replace('a', 'A')
# 문제의 요점을 통해 a 대신 A로 변환, 소문자는 그대로, 대문자는 소문자로 출력하면 되므로 a 대신 A로 나머지는 모두 소문자로만 출력하면 된다.


'''
영소문자로 이루어진 문자열 my_string과 영소문자 1글자로 이루어진 문자열 alp가 매개변수로 주어질 때, 
my_string에서 alp에 해당하는 모든 글자를 대문자로 바꾼 문자열을 return 하는 solution 함수를 작성해 주세요.

my_string       alp     result
"programmers"   "p"     "Programmers"
"lowercase"     "x"     "lowercase"
'''
def solution(my_string, alp):
    return my_string.replace(alp, alp.upper())
# print(solution("programmers", "p"))
# print(solution("lowercase", "x"))