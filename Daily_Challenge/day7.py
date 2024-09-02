# 20240902 day7.py

# day7 반복문


'''
정수 배열 arr와 2차원 정수 배열 queries이 주어집니다. queries의 원소는 각각 하나의 query를 나타내며, [s, e, k] 꼴입니다.
각 query마다 순서대로 s ≤ i ≤ e인 모든 i에 대해 i가 k의 배수이면 arr[i]에 1을 더합니다.
위 규칙에 따라 queries를 처리한 이후의 arr를 return 하는 solution 함수를 완성해 주세요.

arr	            queries	                        result
[0, 1, 2, 4, 3]	[[0, 4, 1],[0, 3, 2],[0, 3, 3]]	[3, 2, 4, 6, 4]
'''
def solution(arr, queries):
    for s, e, k in queries:
        for i in range(s, e + 1):
            if i % k == 0 and k != 0:
                arr[i] += 1
    return arr
# arr = [0, 1, 2, 4, 3]
# queries = [[0, 4, 1],[0, 3, 2],[0, 3, 3]]
# print(solution(arr, queries))
# 처음 풀이 (채점 x)
# def solution(arr, queries):
#     for q in queries:
#         arrList = arr[q[0]:q[1] + 1]
#         for i in range(len(arrList)):
#             if i % q[2] == 0:
#                 arr[i] += 1
#     return arr


'''
정수 l과 r이 주어졌을 때, l 이상 r이하의 정수 중에서 숫자 "0"과 "5"로만 이루어진 모든 정수를 오름차순으로 저장한 배열을 return 하는 solution 함수를 완성해 주세요.
만약 그러한 정수가 없다면, -1이 담긴 배열을 return 합니다.

l	r	result
5	555	[5, 50, 55, 500, 505, 550, 555]
10	20	[-1]
'''
def solution(l, r):
    result = []
    for i in range(l, r + 1):
        if set(str(i)) <= {'0', '5'}:
            result.append(i)
    return result if result else [-1]
# l = 5
# r = 555
# l1 = 10
# r1 = 20
# print(solution(l, r))
# print(solution(l1, r1))
# set() : 주어지는 문자들을 집합 형태로 저장(중복 허용x)


'''
정수 start_num와 end_num가 주어질 때, start_num부터 end_num까지의 숫자를 차례로 담은 리스트를 return하도록 solution 함수를 완성해주세요.

start_num	end_num	    result
3	        10	        [3, 4, 5, 6, 7, 8, 9, 10]
'''
def solution(start_num, end_num):
    result = []
    for i in range(start_num, end_num + 1):
        result.append(i)
    return result
# print(solution(3, 10))
## 다른 풀이
# def solution(start_num, end_num):
#     return list(range(start_num, end_num + 1))


'''
모든 자연수 x에 대해서 현재 값이 x이면 x가 짝수일 때는 2로 나누고, x가 홀수일 때는 3 * x + 1로 바꾸는 계산을 계속해서 반복하면 언젠가는 반드시 x가 1이 되는지 묻는 문제를 콜라츠 문제라고 부릅니다.
그리고 위 과정에서 거쳐간 모든 수를 기록한 수열을 콜라츠 수열이라고 부릅니다.
계산 결과 1,000 보다 작거나 같은 수에 대해서는 전부 언젠가 1에 도달한다는 것이 알려져 있습니다.
임의의 1,000 보다 작거나 같은 양의 정수 n이 주어질 때 초기값이 n인 콜라츠 수열을 return 하는 solution 함수를 완성해 주세요.

n	result
10	[10, 5, 16, 8, 4, 2, 1]
'''
def solution(n):
    result = [n]
    while n != 1:
        n = n // 2 if not n % 2 else 3 * n + 1
        result.append(n)
    return result
print(solution(10))


'''
정수 배열 arr가 주어집니다. arr를 이용해 새로운 배열 stk를 만드려고 합니다.
변수 i를 만들어 초기값을 0으로 설정한 후 i가 arr의 길이보다 작으면 다음 작업을 반복합니다.
만약 stk가 빈 배열이라면 arr[i]를 stk에 추가하고 i에 1을 더합니다.
stk에 원소가 있고, stk의 마지막 원소가 arr[i]보다 작으면 arr[i]를 stk의 뒤에 추가하고 i에 1을 더합니다.
stk에 원소가 있는데 stk의 마지막 원소가 arr[i]보다 크거나 같으면 stk의 마지막 원소를 stk에서 제거합니다.
위 작업을 마친 후 만들어진 stk를 return 하는 solution 함수를 완성해 주세요.

arr	            result
[1, 4, 2, 5, 3]	[1, 2, 3]
'''
def solution(arr):
    i = 0
    stk = []
    while i < len(arr):
        if not stk:
            stk.append(arr[i])
            i += 1
        else:
            if stk[-1] < arr[i]:
                stk.append(arr[i])
                i += 1
            else:
                stk.remove(stk[-1])
    return stk
arr = [1, 4, 2, 5, 3]
print(solution(arr))
# stk.remove(stk[-1]) 대신 stk.pop() 사용해도 된다.