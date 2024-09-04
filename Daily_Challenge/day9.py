# 20240904 day9.py

# day9 문자열


'''
문자열 배열 intStrs와 정수 k, s, l가 주어집니다. intStrs의 원소는 숫자로 이루어져 있습니다.
배열 intStrs의 각 원소마다 s번 인덱스에서 시작하는 길이 l짜리 부분 문자열을 잘라내 정수로 변환합니다. 
이때 변환한 정수값이 k보다 큰 값들을 담은 배열을 return 하는 solution 함수를 완성해 주세요.

intStrs	                                    k	    s	l	result
["0123456789","9876543210","9999999999999"]	50000	5	5   [56789, 99999]
'''
def solution(intStrs, k, s, l):
    result = []
    for i in intStrs:
        if int(i[s:s + l]) > k:
            result.append(int(i[s:s + l]))
    return result
# print(solution(["0123456789","9876543210","9999999999999"], 50000, 5, 5))
## 다른 풀이
# def solution(intStrs, k, s, l):
#     return [int(intstr[s:s+l]) for intstr in intStrs if int(intstr[s:s+l]) > k]


'''
길이가 같은 문자열 배열 my_strings와 이차원 정수 배열 parts가 매개변수로 주어집니다. 
parts[i]는 [s, e] 형태로, my_string[i]의 인덱스 s부터 인덱스 e까지의 부분 문자열을 의미합니다. 
각 my_strings의 원소의 parts에 해당하는 부분 문자열을 순서대로 이어 붙인 문자열을 return 하는 solution 함수를 작성해 주세요.

my_strings	                                            parts	                            result
["progressive", "hamburger", "hammer", "ahocorasick"]	[[0, 4], [1, 2], [3, 5], [7, 7]]	"programmers"
'''
def solution(my_strings, parts):
    result = ''
    for part, my_string in zip(parts, my_strings):
        result += my_string[part[0]:part[1]+1]
    return result
# print(solution(["progressive", "hamburger", "hammer", "ahocorasick"], [[0, 4], [1, 2], [3, 5], [7, 7]]))
## 다른 풀이
# def solution(my_strings, parts):
#     result = ''
#     for i, (start, end) in enumerate(parts):
#         result += my_strings[i][start:end+1]
#     return result
# enumerate()를 사용하여 i(=index)로 my_strings 리스트를 반복해서 가져오고 parts의 리스트 값을 start, end로 가져와서 대입해서 값을 가져온다.


'''
문자열 my_string과 정수 n이 매개변수로 주어질 때, my_string의 뒤의 n글자로 이루어진 문자열을 return 하는 solution 함수를 작성해 주세요.

my_string	        n	result
"ProgrammerS123"	11	"grammerS123"
"He110W0r1d"	    5	"W0r1d"
'''
def solution(my_string, n):
    return my_string[-n:]
# print(solution("ProgrammerS123", 11))
# print(solution("He110W0r1d", 5))


'''
어떤 문자열에 대해서 접미사는 특정 인덱스부터 시작하는 문자열을 의미합니다. 예를 들어, "banana"의 모든 접미사는 "banana", "anana", "nana", "ana", "na", "a"입니다.
문자열 my_string이 매개변수로 주어질 때, my_string의 모든 접미사를 사전순으로 정렬한 문자열 배열을 return 하는 solution 함수를 작성해 주세요.

my_string	    result
"banana"	    ["a", "ana", "anana", "banana", "na", "nana"]
"programmers"	["ammers", "ers", "grammers", "mers", "mmers", "ogrammers", "programmers", "rammers", "rogrammers", "rs", "s"]
'''
def solution(my_string):
    result = [my_string[i:] for i in range(len(my_string))]
    result.sort()
    return result
# print(solution("banana"))
# print(solution("programmers"))
## 다른 풀이
# def solution(my_string):
#     return sorted(my_string[i:] for i in range(len(my_string)))
# sorted 함수를 사용하여 return 할 때 바로 정렬 할 수 있도록 작성한 풀이.


'''
어떤 문자열에 대해서 접미사는 특정 인덱스부터 시작하는 문자열을 의미합니다. 예를 들어, "banana"의 모든 접미사는 "banana", "anana", "nana", "ana", "na", "a"입니다.
문자열 my_string과 is_suffix가 주어질 때, is_suffix가 my_string의 접미사라면 1을, 아니면 0을 return 하는 solution 함수를 작성해 주세요.

my_string	is_suffix	result
"banana"	"ana"	    1
"banana"	"nan"	    0
"banana"	"wxyz"	    0
"banana"	"abanana"	0
'''
def solution(my_string, is_suffix):
    return int(is_suffix in [my_string[i:] for i in range(len(my_string))])
# print(solution("banana", "ana"))
# print(solution("banana", "nan"))
# print(solution("banana", "wxyz"))
# print(solution("banana", "abanana"))
## 다른 풀이1
# def solution(my_string, is_suffix):
#     if my_string[-len(is_suffix):] == is_suffix : return 1
#     return 0
# 특정 인덱스부터 시작하는 접미사 배열에서 [-len(is_suffix):]로 문자열을 출력해서 같으면 1 다르면 0을 반환
## 다른 풀이2
# def solution(my_string, is_suffix):
#     return int(my_string.endswith(is_suffix))
# endswith() : 문자열이 특정 접미사로 끝나는지 여부를 확인하는 메서드
#   ex) 문자열.endswith(suffix[, start[, end]])
#           suffix: 문자열이 끝나는지 확인할 접미사
#           start (선택): 검사할 문자열의 시작 인덱스로 기본값 0
#           end (선택): 검사할 문자열의 끝 인덱스로 기본값 문자열의 끝까지
# 예제1) 문자열에서 문자열 있는지 확인
# text = "hello world"
# print(text.endswith("world")) 출력: True
# print(text.endswith("hello")) 출력: False
# 예제2) 문자열의 특정부분만 확인
# text = "hello world"
# print(text.endswith("world", 6))  # 출력: True (인덱스 6부터 끝까지 검사)
# print(text.endswith("hello", 0, 5))  # 출력: True (인덱스 0부터 5까지 검사)
# 예제3) 튜플을 사용하여 여러 개의 접미사 확인
# text = "example.py"
# print(text.endswith((".py", ".txt")))  # 출력: True (".py"로 끝나기 때문에)