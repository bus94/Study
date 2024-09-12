# 20240906 day11.py

# day11 리스트(배열)


'''
알파벳 대소문자로만 이루어진 문자열 my_string이 주어질 때, 
my_string에서 'A'의 개수, my_string에서 'B'의 개수,..., my_string에서 'Z'의 개수, my_string에서 'a'의 개수, my_string에서 'b'의 개수,..., my_string에서 
'z'의 개수를 순서대로 담은 길이 52의 정수 배열을 return 하는 solution 함수를 작성해 주세요.

my_string	    result
"Programmers"	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 2, 0, 1, 0, 0, 3, 1, 0, 0, 0, 0, 0, 0, 0]
'''
def solution(my_string):
    al = "abcdefghijklmnopqrstuvwxyz"
    alph = al.upper() + al
    result = []
    for i in range(len(alph)):
        result.append(my_string.count(alph[i]))
    return result
# print(solution("Programmers"))
## 다른 풀이
# def solution(my_string):
#     answer=[0] * 52
#     for x in my_string:
#         if x.isupper():
#             answer[ord(x)-65] += 1
#         else:
#             answer[ord(x)-71] += 1
#     return answer
# answer리스트에 52개의 0이라는 값을 넣어 선언한 후 my_string 문자를 하나씩 반복해서 유니코드로 변환 후 - 65를 하면 대문자 기준, - 71을 하면 소문자 기준으로 0번부터의 인덱스와 같게 된다.
# 따라서 my_string의 문자가 대문자인지 소문자인지 확인 후 그 문자를 유니코드로 변환하여 65 또는 71을 빼면 그 문자에 해당하는 인덱스의 값이 1 증가하도록 코딩을 하였다.
# 아스키 코드 (ASCII - American Standard Code for Information Interchange) : 영문 알파벳과 키보드에 있는 문자들을 정리한 대표적인 문자 인코딩 방식
#       0 ~ 127 개의 문자 표현 가능
# 유니코드 (Unicode) : 전 세계의 모든 문자를 컴퓨터에서 일관되게 나타내고 처리하기 위한 국제적인 표준 문자 전산 처리법
#       특정 글자를 표기할 때 U+(4자리의 16자리숫자)
# ord('문자') : 하나의 문자를 인자로 받고 해당 문자에 해당하는 유니코드 정수를 반환
#   ex) ord('a') => 97
# chr(정수) : 하나의 정수를 인자로 받고 해당 정수에 해당하는 유니코드 문자를 반환
#   ex) chr(97) => 'a'


'''
정수 n과 k가 주어졌을 때, 1 이상 n이하의 정수 중에서 k의 배수를 오름차순으로 저장한 배열을 return 하는 solution 함수를 완성해 주세요.

n	k	result
10	3	[3, 6, 9]
15	5	[5, 10, 15]
'''
def solution(n, k):
    return [k * i for i in range(1, n+1) if k * i <= n]
# print(solution(10, 3))
# print(solution(15, 5))
## 다른 풀이
# def solution(n, k):
#     return [i for i in range(k, n+1, k)]
# k의 배수이므로 k부터 인덱스가 시작할 수 있도록 하고 증감값으로 k로 잡아 k의 배수들이 출력될 수 있도록 한다.


'''
문자열 my_string과 정수 배열 indices가 주어질 때, 
my_string에서 indices의 원소에 해당하는 인덱스의 글자를 지우고 이어 붙인 문자열을 return 하는 solution 함수를 작성해 주세요.

my_string	            indices	                        result
"apporoograpemmemprs"	[1, 16, 6, 15, 0, 10, 11, 3]	"programmers"
'''
def solution(my_string, indices):
    l = list(my_string)
    for i in range(len(indices)):
        l[indices[i]] = ''
    return ''.join(l)
# print(solution("apporoograpemmemprs", [1, 16, 6, 15, 0, 10, 11, 3]))
## 다른 풀이
# def solution(my_string, indices):
#     result = ''
#     for i in range(len(my_string)):
#         if i not in indices:
#           result += my_string[i]
#     return result
# my_string의 문자를 하나씩 검사하는 방법으로, indices 배열에 my_string의 인덱스와 비교하여 indices 배열에 있는 인덱스의 값을 제외하고 result에 문자열을 계속 추가하여 출력한다.


'''
정수 start_num와 end_num가 주어질 때, start_num에서 end_num까지 1씩 감소하는 수들을 차례로 담은 리스트를 return하도록 solution 함수를 완성해주세요.

start_num	end_num	    result
10	        3	        [10, 9, 8, 7, 6, 5, 4, 3]
'''
def solution(start_num, end_num):
    return [i for i in range(start_num, end_num - 1, -1)]
# print(solution(10, 3))


'''
정수 배열 arr가 주어집니다. 이때 arr의 원소는 1 또는 0입니다. 
정수 idx가 주어졌을 때, idx보다 크면서 배열의 값이 1인 가장 작은 인덱스를 찾아서 반환하는 solution 함수를 완성해 주세요.
단, 만약 그러한 인덱스가 없다면 -1을 반환합니다.

arr	                idx	    result
[0, 0, 0, 1]	    1	    3
[1, 0, 0, 1, 0, 0]	4	    -1
[1, 1, 1, 1, 0]	    3	    3
'''
def solution(arr, idx):
    for a in range(idx, len(arr)):
        if arr[a] == 1:
            return a
    return -1
# print(solution([0, 0, 0, 1], 1))
# print(solution([1, 0, 0, 1, 0, 0], 4))
# print(solution([1, 1, 1, 1, 0], 3))