# 20240903 day8.py

# day8 조건문


'''
boolean 변수 x1, x2, x3, x4가 매개변수로 주어질 때, 다음의 식의 true/false를 return 하는 solution 함수를 작성해 주세요.
(x1 ∨ x2) ∧ (x3 ∨ x4)

x1	    x2	    x3	    x4	    result
false	true	true	true	true
true	false	false	false	false
'''
def solution(x1, x2, x3, x4):
    return (x1 or x2) and (x3 or x4)
x1 = False
x2 = True
x3 = True
x4 = True
# print(solution(x1, x2, x3, x4))
## 다른 풀이
# def solution(x1, x2, x3, x4):
#     return (x1 | x2) & (x3 | x4)


'''
1부터 6까지 숫자가 적힌 주사위가 네 개 있습니다. 네 주사위를 굴렸을 때 나온 숫자에 따라 다음과 같은 점수를 얻습니다.
네 주사위에서 나온 숫자가 모두 p로 같다면 1111 × p점을 얻습니다.
세 주사위에서 나온 숫자가 p로 같고 나머지 다른 주사위에서 나온 숫자가 q(p ≠ q)라면 (10 × p + q)**2 점을 얻습니다.
주사위가 두 개씩 같은 값이 나오고, 나온 숫자를 각각 p, q(p ≠ q)라고 한다면 (p + q) × |p - q|점을 얻습니다.
어느 두 주사위에서 나온 숫자가 p로 같고 나머지 두 주사위에서 나온 숫자가 각각 p와 다른 q, r(q ≠ r)이라면 q × r점을 얻습니다.
네 주사위에 적힌 숫자가 모두 다르다면 나온 숫자 중 가장 작은 숫자 만큼의 점수를 얻습니다.
네 주사위를 굴렸을 때 나온 숫자가 정수 매개변수 a, b, c, d로 주어질 때, 얻는 점수를 return 하는 solution 함수를 작성해 주세요.

a	b	c	d	result
2	2	2	2	2222
4	1	4	4	1681
6	3	3	6	27
2	5	2	6	30
6	4	2	5	2
'''
def solution(a, b, c, d):
    result = 0
    numList = [a, b, c, d]
    setList = set(numList)
    if len(setList) == 1:
        result += 1111 * a
    elif len(setList) == 2:
        for i in numList:
            x = list(setList - {i})[0]
            if numList.count(i) == 1:
                result += (10 * x + i) ** 2
                break
            elif numList.count(i) == 2:
                result += (x + i) * abs(x - i)
                break
    elif len(setList) == 3:
        for i in numList:
            y = list(setList - {i})
            if numList.count(i) == 2:
                result += y[0] * y[1]
                break
    elif len(setList) == 4:
        result += min(setList)
    return result
# print(solution(2, 2, 2, 2))
# print(solution(4, 1, 4, 4))
# print(solution(6, 3, 3, 6))
# print(solution(2, 5, 2, 6))
# print(solution(6, 4, 2, 5))
## 다른 풀이
# def solution(a, b, c, d):
#     l = [a,b,c,d]
#     c = [l.count(x) for x in l]
#     if max(c) == 4:
#         return 1111*a
#     elif max(c) == 3:
#         return (10*l[c.index(3)]+l[c.index(1)])**2
#     elif max(c) == 2:
#         if min(c) == 1:
#             return eval('*'.join([str(l[i]) for i, x in enumerate(c) if x == 1]))
#         else:
#             return (max(l) + min(l)) * abs(max(l) - min(l))
#     else:
#         return min(l)
# set()을 쓰지않고 count로 가장 많이 겹치는 수의 개수(max(c))를 구해서 각각의 수식으로 계산하고, 같은 수가 2개인 경우만 if문으로 min(c)를 통해 각각의 수식으로 계산하였다.
# ex) 같은 수 2개, 다른 수 2개이면 min(c) == 1이 되고(위의 코드에선 if 조건), 같은 수 2개 2쌍이면 min(c) == 2가 된다(위의 코드에선 else 조건).


'''
문자열 my_string과 정수 배열 index_list가 매개변수로 주어집니다. 
my_string의 index_list의 원소들에 해당하는 인덱스의 글자들을 순서대로 이어 붙인 문자열을 return 하는 solution 함수를 작성해 주세요.

my_string	            index_list	                                result
"cvsgiorszzzmrpaqpe"	[16, 6, 5, 3, 12, 14, 11, 11, 17, 12, 7]	"programmers"
"zpiaz"	                [1, 2, 0, 0, 3]	                            "pizza"
'''
def solution(my_string, index_list):
    result = ''
    for i in index_list:
        result += my_string[i]
    return result
# print(solution("cvsgiorszzzmrpaqpe", [16, 6, 5, 3, 12, 14, 11, 11, 17, 12, 7]))
# print(solution("zpiaz", [1, 2, 0, 0, 3]))
## 다른 풀이
# def solution(my_string, index_list):
#     return ''.join([my_string[idx] for idx in index_list])


'''
음이 아닌 정수를 9로 나눈 나머지는 그 정수의 각 자리 숫자의 합을 9로 나눈 나머지와 같은 것이 알려져 있습니다.
이 사실을 이용하여 음이 아닌 정수가 문자열 number로 주어질 때, 이 정수를 9로 나눈 나머지를 return 하는 solution 함수를 작성해주세요.

number	                result
"123"	                6
"78720646226947352489"	2
'''
def solution(number):
    return sum(int(n) for n in number) % 9
# print(solution("123"))
# print(solution("78720646226947352489"))


'''
문자열 my_string과 이차원 정수 배열 queries가 매개변수로 주어집니다. 
queries의 원소는 [s, e] 형태로, my_string의 인덱스 s부터 인덱스 e까지를 뒤집으라는 의미입니다.
my_string에 queries의 명령을 순서대로 처리한 후의 문자열을 return 하는 solution 함수를 작성해 주세요.

my_string	    queries	                            result
"rermgorpsam"	[[2, 3], [0, 7], [5, 9], [6, 10]]	"programmers"
'''
def solution(my_string, queries):
    s = list(my_string)
    for start, end in queries:
        s[start:end + 1] = s[start:end + 1][::-1]
    return ''.join(s)
print(solution("rermgorpsam", [[2, 3], [0, 7], [5, 9], [6, 10]]))
# 잘못된 풀이
# def solution(my_string, queries):
#     s = list(my_string)
#     for start, end in queries:
#         x = s[start:end + 1]
#         s = s.replace(x, x[::-1])
#     return my_string
# 이유: 해당 인덱스의 문자만 변경하는 것이 아니라 같은 문자 내용이 있는 곳이라면 모두 변경하게 된다.
#       ex) re 라는 문자를 찾아서 바꾸고 싶은데 re라는 문자가 다른 인덱스 범위에도 있다면 그곳도 변경하게 된다.