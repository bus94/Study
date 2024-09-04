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
    answer = []
    return answer



'''
정수 n과 k가 주어졌을 때, 1 이상 n이하의 정수 중에서 k의 배수를 오름차순으로 저장한 배열을 return 하는 solution 함수를 완성해 주세요.

n	k	result
10	3	[3, 6, 9]
15	5	[5, 10, 15]
'''
def solution(n, k):
    answer = []
    return answer


'''
문자열 my_string과 정수 배열 indices가 주어질 때, 
my_string에서 indices의 원소에 해당하는 인덱스의 글자를 지우고 이어 붙인 문자열을 return 하는 solution 함수를 작성해 주세요.

my_string	            indices	                        result
"apporoograpemmemprs"	[1, 16, 6, 15, 0, 10, 11, 3]	"programmers"
'''
def solution(my_string, indices):
    answer = ''
    return answer


'''
정수 start_num와 end_num가 주어질 때, start_num에서 end_num까지 1씩 감소하는 수들을 차례로 담은 리스트를 return하도록 solution 함수를 완성해주세요.

start_num	end_num	result
10	3	    [10, 9, 8, 7, 6, 5, 4, 3]
'''
def solution(start_num, end_num):
    answer = []
    return answer


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
    answer = 0
    return answer