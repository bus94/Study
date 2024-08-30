# 20240829 day4.py

# day4 연산, 조건문

'''
정수 num과 n이 매개 변수로 주어질 때, num이 n의 배수이면 1을 return n의 배수가 아니라면 0을 return하도록 solution 함수를 완성해주세요.

num	n	result
98	2	1
34	3	0
'''
def solution(num, n):
    return 1 if num % n == 0 else 0
## 다른 풀이
# def solution(num, n):
#     return int(num % n == 0)
# 위 코드에서 num % n == 0이 참이면 배수라는 뜻으로 1(True)을 리턴받고, 거짓이면 배수가 아니라는 뜻으로 0(False)을 리턴받는다.


'''
정수 number와 n, m이 주어집니다. number가 n의 배수이면서 m의 배수이면 1을 아니라면 0을 return하도록 solution 함수를 완성해주세요.

number	n	m	result
60	    2	3	1
55	    10	5	0
'''
def solution(number, n, m):
    return int(number % n == 0 and number % m == 0)


'''
양의 정수 n이 매개변수로 주어질 때, n이 홀수라면 n 이하의 홀수인 모든 양의 정수의 합을 return 하고 n이 짝수라면 n 이하의 짝수인 모든 양의 정수의 제곱의 합을 return 하는 solution 함수를 작성해 주세요.

n	    result
7	    16
10	220
'''
def solution(n):
    sum = 0
    start = 1 if n % 2 != 0 else 2
    for i in range(start, n + 1, 2):
        sum += (i if start == 1 else i ** 2)
    return sum
# 처음 풀이:
# def solution(n):
#     sum = 0
#     if n % 2 != 0:
#         for i in range(1, n + 1, 2):
#             sum += i
#     else :
#         for i in range(2, n + 1, 2):
#             sum += i ** 2
#     return sum
## 다른 풀이
# def solution(n):
#     if n % 2:
#         return sum(range(1,n+1,2))
#     return sum([i*i for i in range(2,n+1,2)])
# n % 2 가 0 또는 1로 False와 True를 구분해준 뒤 sum()을 이용해서 리턴한다.


'''
문자열에 따라 다음과 같이 두 수의 크기를 비교하려고 합니다.
두 수가 n과 m이라면
">", "=" : n >= m
"<", "=" : n <= m
">", "!" : n > m
"<", "!" : n < m
두 문자열 ineq와 eq가 주어집니다. ineq는 "<"와 ">"중 하나고, eq는 "="와 "!"중 하나입니다. 그리고 두 정수 n과 m이 주어질 때, n과 m이 ineq와 eq의 조건에 맞으면 1을 아니면 0을 return하도록 solution 함수를 완성해주세요.

ineq	eq	    n	m	result
"<"	    "="	    20	50	1
">"	    "!"	    41	78	0
'''
def solution(ineq, eq, n, m):
    if ineq == "<":
        if eq == "=":
           return int(n <= m)
        elif eq == "!":
            return int(n < m)
    elif ineq == ">":
        if eq == "=":
           return int(n >= m)
        elif eq == "!":
            return int(n > m)
# print(solution("<", "=", 20, 50))
# print(solution(">", "!", 41, 78))
## 다른 풀이
def solution(ineq, eq, n, m):
    return int(eval(str(n)+ineq+eq.replace('!', '')+str(m)))
# 'eval(expression)' 함수는 매개변수로 받은 expression(=식)을 문자열로 받아 그대로 실행한다. 단, 실행 가능한 문자열이 들어와야한다.
# 따라서 매개변수로 받은 문자를 그대로 넣고 eq에서는 "="은 그대로, "!"는 ""로 바꿔서 eval()을 실행한다.


'''
두 정수 a, b와 boolean 변수 flag가 매개변수로 주어질 때, flag가 true면 a + b를 false면 a - b를 return 하는 solution 함수를 작성해 주세요.

a	b	flag	result
-4	7	True	3
-4	7	False	-11
'''
def solution(a, b, flag):
    return (a + b if flag else a - b)
# print(solution(-4, 7, True))
# print(solution(-4, 7, False))
## 다른 풀이
# solution=lambda a,b,f:[a-b,a+b][f]
# lambda 함수 : 익명함수를 정의하는데 사용한다.
# 표현 : lambda 매개변수1, 매개변수2, ... : 표현식       (표현식: 반환값이나 계산 결과를 포함한 표현식)
# ex1) add = lambda x, y: x + y
# ex2) select_operation = lambda x, y, choice: [x * y, x / y, x + y, x - y][choice] => choice가 0, 1, 2, 3 일 때 표현식(곱하기, 나누기, 더하기, 빼기)을 기준으로 계산해준다.