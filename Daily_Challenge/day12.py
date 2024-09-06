# 20240907 day12.py

# day12 리스트(배열)


'''
정수 n과 정수 3개가 담긴 리스트 slicer 그리고 정수 여러 개가 담긴 리스트 num_list가 주어집니다. 
slicer에 담긴 정수를 차례대로 a, b, c라고 할 때, n에 따라 다음과 같이 num_list를 슬라이싱 하려고 합니다.
n = 1 : num_list의 0번 인덱스부터 b번 인덱스까지
n = 2 : num_list의 a번 인덱스부터 마지막 인덱스까지
n = 3 : num_list의 a번 인덱스부터 b번 인덱스까지
n = 4 : num_list의 a번 인덱스부터 b번 인덱스까지 c 간격으로
올바르게 슬라이싱한 리스트를 return하도록 solution 함수를 완성해주세요.

n	slicer	    num_list	                    result
3	[1, 5, 2]	[1, 2, 3, 4, 5, 6, 7, 8, 9]	    [2, 3, 4, 5, 6]
4	[1, 5, 2]	[1, 2, 3, 4, 5, 6, 7, 8, 9]	    [2, 4, 6]
'''
def solution(n, slicer, num_list):
    for i in range(len(num_list)):
        if i == slicer[1]:
            if n == 1:
                return num_list[:i+1]
            elif n == 2:
                return num_list[slicer[0]:]
            elif n == 3:
                return num_list[slicer[0]:i+1]
            elif n == 4:
                return num_list[slicer[0]:i+1:slicer[2]]
# print(solution(3, [1, 5, 2], [1, 2, 3, 4, 5, 6, 7, 8, 9]))
# print(solution(4, [1, 5, 2], [1, 2, 3, 4, 5, 6, 7, 8, 9]))
## 다른 풀이
# def solution(n, slicer, num_list):
#     a, b, c = slicer
#     return [num_list[:b + 1], num_list[a:], num_list[a:b + 1], num_list[a:b + 1:c]][n - 1]
# a, b, c 에 slicer의 각각 요소의 값들을 넣어준다. 4개의 종류 중에서 맨 뒤에 있는 [n-1]을 통해 n=1이면 0번째 인덱스의 num_list[:b + 1]이 반환될 수 있도록 작성했다.

'''
정수 리스트 num_list가 주어질 때, 첫 번째로 나오는 음수의 인덱스를 return하도록 solution 함수를 완성해주세요. 음수가 없다면 -1을 return합니다.

num_list	                    result
[12, 4, 15, 46, 38, -2, 15]	    5
[13, 22, 53, 24, 15, 6]	        -1
'''
def solution(num_list):
    for i in range(len(num_list)):
        if num_list[i] < 0:
            return i
    return -1
# print(solution([12, 4, 15, 46, 38, -2, 15]))
# print(solution([13, 22, 53, 24, 15, 6]))


'''
정수 배열 arr와 2개의 구간이 담긴 배열 intervals가 주어집니다.
intervals는 항상 [[a1, b1], [a2, b2]]의 꼴로 주어지며 각 구간은 닫힌 구간입니다. 닫힌 구간은 양 끝값과 그 사이의 값을 모두 포함하는 구간을 의미합니다.
이때 배열 arr의 첫 번째 구간에 해당하는 배열과 두 번째 구간에 해당하는 배열을 앞뒤로 붙여 새로운 배열을 만들어 return 하는 solution 함수를 완성해 주세요.

arr	                intervals	        result
[1, 2, 3, 4, 5]	    [[1, 3], [0, 4]]	[2, 3, 4, 1, 2, 3, 4, 5]
'''
def solution(arr, intervals):
    print(1)
    result = ''
    for i in intervals:
        print(2)
        print(arr[i[0]:i[1]+1])
        print(3)
        result += ','.join(arr[i[0]:i[1] + 1])
        print("result:", result)
    return result
print(solution([1, 2, 3, 4, 5], [[1, 3], [0, 4]]))


'''
정수 배열 arr가 주어집니다. 배열 안의 2가 모두 포함된 가장 작은 연속된 부분 배열을 return 하는 solution 함수를 완성해 주세요.
단, arr에 2가 없는 경우 [-1]을 return 합니다.

arr	                        result
[1, 2, 1, 4, 5, 2, 9]	    [2, 1, 4, 5, 2]
[1, 2, 1]	                [2]
[1, 1, 1]	                [-1]
[1, 2, 1, 2, 1, 10, 2, 1]	[2, 1, 2, 1, 10, 2]
'''
def solution(arr):
    answer = []
    return answer


'''
정수 배열 arr와 query가 주어집니다.
query를 순회하면서 다음 작업을 반복합니다.
짝수 인덱스에서는 arr에서 query[i]번 인덱스를 제외하고 배열의 query[i]번 인덱스 뒷부분을 잘라서 버립니다.
홀수 인덱스에서는 arr에서 query[i]번 인덱스는 제외하고 배열의 query[i]번 인덱스 앞부분을 잘라서 버립니다.
위 작업을 마친 후 남은 arr의 부분 배열을 return 하는 solution 함수를 완성해 주세요.

arr	                query	    result
[0, 1, 2, 3, 4, 5]	[4, 1, 2]	[1, 2, 3]
'''
def solution(arr, query):
    answer = []
    return answer



