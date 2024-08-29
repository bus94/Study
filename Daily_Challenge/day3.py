# 20240828 day3.py

# day3 연산


'''
길이가 같은 두 문자열 str1과 str2가 주어집니다. 두 문자열의 각 문자가 앞에서부터 서로 번갈아가면서 한 번씩 등장하는 문자열을 만들어 return 하는 solution 함수를 완성해 주세요.

str1          str2        result
"aaaaa"	    "bbbbb"	    "ababababab"
'''
def solution(str1, str2):
    answer = ''
    for i in range(len(str1)):
        answer += str1[i] + str2[i]
    return answer
## 다른 풀이
# def solution(str1, str2):
#    answer = ''.join(i+j for i,j in zip(str1, str2))
#    return answer
# zip(): 파이썬 내장함수. 순회 가능(iterable)한 객체를 인자로 받아 각 자료형의 요소를 나눈 후 인덱스끼리 잘라 리스트로 반환
#   위 코드의 경우 - str1, str2의 0번째 인덱스부터 하나씩 잘라 i+j의 형태로 출력


'''
문자들이 담겨있는 배열 arr가 주어집니다. arr의 원소들을 순서대로 이어 붙인 문자열을 return 하는 solution함수를 작성해 주세요.

arr	            result
["a","b","c"]	    "abc"
'''
def solution(arr):
    answer = ''
    for arr in arr:
        answer += arr
    return answer
## 다른 풀이
# def solution(arr):
#    return ''.join(arr)
# join(): ''.join(리스트) 또는 '구분자'.join(리스트) 형태로 쓰인다.
#          매개변수로 들어온 리스트에 있는 요소 하나씩 합쳐 하나의 문자열로 바꾸어 반환하는 함수


'''
문자열 my_string과 정수 k가 주어질 때, my_string을 k번 반복한 문자열을 return 하는 solution 함수를 작성해 주세요.

my_string	    k	    result
"string"	    3	    "stringstringstring"
"love"	    10	    "lovelovelovelovelovelovelovelovelovelove"
'''
def solution(my_string, k):
    answer = ''
    for k in range(k):
        answer += my_string
    return answer
## 다른 풀이
# def solution(my_string, k):
#     return my_string * k


'''
연산 ⊕는 두 정수에 대한 연산으로 두 정수를 붙여서 쓴 값을 반환합니다. 예를 들면 다음과 같습니다.
12 ⊕ 3 = 123
3 ⊕ 12 = 312
양의 정수 a와 b가 주어졌을 때, a ⊕ b와 b ⊕ a 중 더 큰 값을 return 하는 solution 함수를 완성해 주세요.
단, a ⊕ b와 b ⊕ a가 같다면 a ⊕ b를 return 합니다.

a	    b	    result
9	    91	    991
89	8	    898
'''
def solution(a, b):
    a, b = str(a), str(b)
    if a + b >= b + a:
        return int(a + b)
    elif a + b < b + a:
        return int(b + a)
## 다른 풀이
# def solution(a, b):
#     return int(max(f"{a}{b}", f"{b}{a}"))


'''
연산 ⊕는 두 정수에 대한 연산으로 두 정수를 붙여서 쓴 값을 반환합니다. 예를 들면 다음과 같습니다.
12 ⊕ 3 = 123
3 ⊕ 12 = 312
양의 정수 a와 b가 주어졌을 때, a ⊕ b와 2 * a * b 중 더 큰 값을 return하는 solution 함수를 완성해 주세요.
단, a ⊕ b와 2 * a * b가 같으면 a ⊕ b를 return 합니다.

a	    b	    result
2	    91	    364
91	2	    912
'''
def solution(a, b):
    return max(int(f"{a}{b}"), 2 * a * b)
print(solution(2, 91))
print(solution(91, 2))



