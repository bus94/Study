# 20240905 day10.py

# day10 문자열


'''
문자열 my_string과 정수 n이 매개변수로 주어질 때, my_string의 앞의 n글자로 이루어진 문자열을 return 하는 solution 함수를 작성해 주세요.

my_string	        n	result
"ProgrammerS123"	11	"ProgrammerS"
"He110W0r1d"	    5	"He110"
'''
def solution(my_string, n):
    return my_string[:n]
# print(solution("ProgrammerS123", 11))
# print(solution("He110W0r1d", 5))


'''
어떤 문자열에 대해서 접두사는 특정 인덱스까지의 문자열을 의미합니다. 예를 들어, "banana"의 모든 접두사는 "b", "ba", "ban", "bana", "banan", "banana"입니다.
문자열 my_string과 is_prefix가 주어질 때, is_prefix가 my_string의 접두사라면 1을, 아니면 0을 return 하는 solution 함수를 작성해 주세요.

my_string	is_prefix	result
"banana"	"ban"	    1
"banana"	"nan"	    0
"banana"	"abcd"	    0
"banana"	"bananan"	0
'''
def solution(my_string, is_prefix):
    return int(my_string.startswith(is_prefix))
# print(solution("banana", "ban"))
# print(solution("banana", "nan"))
# print(solution("banana", "abcd"))
# print(solution("banana", "bananan"))


'''
문자열 my_string과 정수 s, e가 매개변수로 주어질 때, my_string에서 인덱스 s부터 인덱스 e까지를 뒤집은 문자열을 return 하는 solution 함수를 작성해 주세요.

my_string	        s	e	result
"Progra21Sremm3"	6	12	"ProgrammerS123"
"Stanley1yelnatS"	4	10	"Stanley1yelnatS"
'''
def solution(my_string, s, e):
    return my_string.replace(my_string[s:e+1], my_string[s:e+1][::-1])
# print(solution("Progra21Sremm3", 6, 12))
# print(solution("Stanley1yelnatS", 4, 10))


'''
문자열 my_string과 두 정수 m, c가 주어집니다. 
my_string을 한 줄에 m 글자씩 가로로 적었을 때 왼쪽부터 세로로 c번째 열에 적힌 글자들을 문자열로 return 하는 solution 함수를 작성해 주세요.

my_string	            m	c	result
"ihrhbakrfpndopljhygc"	4	2	"happy"
"programmers"	        1	1	"programmers"
'''
def solution(my_string, m, c):
    leng = len(my_string) // m + (1 if len(my_string) % m != 0 else 0)
    result = ''
    for i in range(leng):
        result += my_string[m*i+c-1]
    return result
# print(solution("ihrhbakrfpndopljhygc", 4, 2))
# print(solution("programmers", 1, 1))
## 다른 풀이
# def solution(my_string, m, c):
#     return my_string[c-1::m]
# c-1로 시작 인덱스를 정하고 m의 배수만큼 더해서 출력 될 수 있도록 설정한다.
# ex) c = 2, m = 4 라면 my_string[1::4]가 되고, 이렇게 되면 my_string[1], [5], [9], ... 가 된다.
# 좀 더 쉽게 이해해볼 수 있도록 인덱스 기준으로 문자를 정리한다면 (문자열의 길이가 20이라고 가정했을 때)
# 0  1  2  3
# 4  5  6  7
# 8  9  10 11
# 12 13 14 15
# 16 17 18 19
# 이렇게 되며, 왼쪽에서 2번째(c=2)를 뽑아와야하므로 1, 5, 9, 13, 17을 뽑아오면 된다. 따라서 위의 코드로 간단하게 정의할 수 있다.


'''
두 정수 q, r과 문자열 code가 주어질 때, 
code의 각 인덱스를 q로 나누었을 때 나머지가 r인 위치의 문자를 앞에서부터 순서대로 이어 붙인 문자열을 return 하는 solution 함수를 작성해 주세요.

q	r	code	            result
3	1	"qjnwezgrpirldywt"	"jerry"
1	0	"programmers"	    "programmers"
'''
def solution(q, r, code):
    return ''.join(code[i] for i in range(len(code)) if i % q == r)
# print(solution(3, 1, "qjnwezgrpirldywt"))
# print(solution(1, 0, "programmers"))
## 다른 풀이
# def solution(q, r, code):
#     return code[r::q]
# q로 나누었을 때 나머지가 r인 것은 q * 0 + r = r, q * 1 + r = q + r, q * 2 + r = 2q + r, ... 의 꼴이므로 시작 인덱스를 r로 잡고 q씩 증가시켜서 출력시키면 된다.
