# 20240830 day5.py

# day5 조건문

'''
문자열 code가 주어집니다.
code를 앞에서부터 읽으면서 만약 문자가 "1"이면 mode를 바꿉니다. mode에 따라 code를 읽어가면서 문자열 ret을 만들어냅니다.
mode는 0과 1이 있으며, idx를 0 부터 code의 길이 - 1 까지 1씩 키워나가면서 code[idx]의 값에 따라 다음과 같이 행동합니다.
mode가 0일 때
code[idx]가 "1"이 아니면 idx가 짝수일 때만 ret의 맨 뒤에 code[idx]를 추가합니다.
code[idx]가 "1"이면 mode를 0에서 1로 바꿉니다.
mode가 1일 때
code[idx]가 "1"이 아니면 idx가 홀수일 때만 ret의 맨 뒤에 code[idx]를 추가합니다.
code[idx]가 "1"이면 mode를 1에서 0으로 바꿉니다.
문자열 code를 통해 만들어진 문자열 ret를 return 하는 solution 함수를 완성해 주세요.
단, 시작할 때 mode는 0이며, return 하려는 ret가 만약 빈 문자열이라면 대신 "EMPTY"를 return 합니다.

code	        result
"abc1abc1abc"	"acbac"
'''
def solution(code):
    mode = 0
    ret = ''
    for index, char_code in enumerate(code):
        if char_code == "1":
            mode = int(mode != 1)
            continue
        elif (mode == 0 and index % 2 == 0) or (mode == 1 and index % 2 == 1):
            ret += char_code
    return ret if ret != '' else "EMPTY"
# print(solution("abc1abc1abc"))
## 다른 풀이
# def solution(code):
#     return "".join(code.split("1"))[::2] or "EMPTY"


'''
두 정수 a, d와 길이가 n인 boolean 배열 included가 주어집니다. 첫째항이 a, 공차가 d인 등차수열에서 included[i]가 i + 1항을 의미할 때, 이 등차수열의 1항부터 n항까지 included가 true인 항들만 더한 값을 return 하는 solution 함수를 작성해 주세요.

a	d	included	                                        result
3	4	[true, false, false, true, true]	                37
7	1	[false, false, false, true, false, false, false]	10
'''
def solution(a, d, included):
    arithmetic_sequence = []
    result = 0
    for i in range(len(included)):
        arithmetic_sequence.append(a + i * d)
    for inc, seq in zip(included, arithmetic_sequence):
        result += seq if inc else 0
    return result
## 다른 풀이
# def solution(a, d, included):
#     return sum(a + i * d for i, f in enumerate(included) if f)
# 불러오는 included가 True, False냐에 따라 등차수열을 확인하여 sum()을 적용하는 방법


'''
1부터 6까지 숫자가 적힌 주사위가 세 개 있습니다. 세 주사위를 굴렸을 때 나온 숫자를 각각 a, b, c라고 했을 때 얻는 점수는 다음과 같습니다.

세 숫자가 모두 다르다면 a + b + c 점을 얻습니다.
세 숫자 중 어느 두 숫자는 같고 나머지 다른 숫자는 다르다면 (a + b + c) x (a2 + b2 + c2 )점을 얻습니다.
세 숫자가 모두 같다면 (a + b + c) x (a2 + b2 + c2 ) x (a3 + b3 + c3 )점을 얻습니다.
세 정수 a, b, c가 매개변수로 주어질 때, 얻는 점수를 return 하는 solution 함수를 작성해 주세요.

a	b	c	result
2	6	1	9
5	3	3	473
4	4	4	110592
'''
def solution(a, b, c):
    count = (a == b) + (b == c) + (c == a)
    if count == 0:
        return (a + b + c)
    elif count == 1:
        return (a + b + c) * (a ** 2 + b ** 2 + c ** 2)
    elif count == 3:
        return (a + b + c) * (a ** 2 + b ** 2 + c ** 2) * (a ** 3 + b ** 3 + c ** 3)
print(solution(2, 6, 1))
print(solution(5, 3, 3))
print(solution(4, 4, 4))
## 다른 풀이
# def solution(a, b, c):
#     check=len(set([a,b,c]))
#     if check==1:
#         return 3*a*3*(a**2)*3*(a**3)
#     elif check==2:
#         return (a+b+c)*(a**2+b**2+c**2)
#     else:
#         return (a+b+c)
# set(): 


'''
정수가 담긴 리스트 num_list가 주어질 때, 모든 원소들의 곱이 모든 원소들의 합의 제곱보다 작으면 1을 크면 0을 return하도록 solution 함수를 완성해주세요.

num_list	        result
[3, 4, 5, 2, 1]	    1
[5, 7, 8, 3]	    0
'''
def solution(num_list):
    product = eval('*'.join(str(x) for x in num_list))
    square = sum(num_list) ** 2
    return int(product < square)
# * eval() : day4.py 참고


'''
정수가 담긴 리스트 num_list가 주어집니다. num_list의 홀수만 순서대로 이어 붙인 수와 짝수만 순서대로 이어 붙인 수의 합을 return하도록 solution 함수를 완성해주세요.

num_list	        result
[3, 4, 5, 2, 1]	    393
[5, 7, 8, 3]	    581
'''
def solution(num_list):
    odd = ''
    even = ''
    for n in num_list:
        if n % 2 != 0:
            odd += str(n)
        else:
            even += str(n)
    return eval(odd + "+" + even)
num_list = [3, 4, 5, 2, 1]
num_list1 = [5, 7, 8, 3]
print(solution(num_list))
print(solution(num_list1))
# 수정 풀이
# def solution(num_list):
#     odd = int(''.join([str(n) for n in num_list if not n % 2]))
#     even = int(''.join([str(n) for n in num_list if n % 2]))
#     return odd + even
# n % 2 의 값에 따라 if문의 조건이 결정될 수 있도록 코딩
