# 20240831 day6.py

# day6 조건문, 반복문


'''
정수 리스트 num_list가 주어질 때, 마지막 원소가 그전 원소보다 크면 마지막 원소에서 그전 원소를 뺀 값을 마지막 원소가 그전 원소보다 크지 않다면 마지막 원소를 두 배한 값을 추가하여 return하도록 solution 함수를 완성해주세요.

num_list            result
[2, 1, 6]           [2, 1, 6, 5]
[5, 2, 1, 7, 5]     [5, 2, 1, 7, 5, 10]
'''
def solution(num_list):
    num_list.append(num_list[-1] - num_list[-2] if num_list[-1] > num_list[-2] else num_list[-1] * 2)
    return num_list
# num_list = [2, 1, 6]
# num_list1 = [5, 2, 1, 7, 5]
# print(solution(num_list))
# print(solution(num_list1))


'''
정수 n과 문자열 control이 주어집니다. control은 "w", "a", "s", "d"의 4개의 문자로 이루어져 있으며, control의 앞에서부터 순서대로 문자에 따라 n의 값을 바꿉니다.
"w" : n이 1 커집니다.
"s" : n이 1 작아집니다.
"d" : n이 10 커집니다.
"a" : n이 10 작아집니다.
위 규칙에 따라 n을 바꿨을 때 가장 마지막에 나오는 n의 값을 return 하는 solution 함수를 완성해 주세요.

n   control         result
0   "wsdawsdassw"   -1

입출력 예 설명
입출력 예 #1

수 n은 control에 따라 다음과 같은 순서로 변하게 됩니다.
0 → 1 → 0 → 10 → 0 → 1 → 0 → 10 → 0 → -1 → -2 → -1
따라서 -1을 return 합니다.
'''
def solution(n, c):
    for c in c:
        if c == "w":
            n += 1
        elif c == "s":
            n -= 1
        elif c == "d":
            n += 10
        elif c == "a":
            n -= 10
    return n
# n = 0
# control = "wsdawsdassw"
# print(solution(n, control))
## 다른 풀이
# def solution(n, control):
#     key = dict(zip(['w','s','d','a'], [1,-1,10,-10]))
#     return n + sum([key[c] for c in control])
# dict 딕셔너리를 이용해서 각 문자가 나왔을 때 해당하는 값들을 리스트에 저장하고 모두 더해서 n에 적용하고 리턴


'''
정수 배열 numLog가 주어집니다. 처음에 numLog[0]에서 부터 시작해 "w", "a", "s", "d"로 이루어진 문자열을 입력으로 받아 순서대로 다음과 같은 조작을 했다고 합시다.
"w" : 수에 1을 더한다.
"s" : 수에 1을 뺀다.
"d" : 수에 10을 더한다.
"a" : 수에 10을 뺀다.
그리고 매번 조작을 할 때마다 결괏값을 기록한 정수 배열이 numLog입니다. 즉, numLog[i]는 numLog[0]로부터 총 i번의 조작을 가한 결과가 저장되어 있습니다.
주어진 정수 배열 numLog에 대해 조작을 위해 입력받은 문자열을 return 하는 solution 함수를 완성해 주세요.

numLog                                      result
[0, 1, 0, 10, 0, 1, 0, 10, 0, -1, -2, -1]   "wsdawsdassw"
'''
# 0에서 1로 가면 w, 1에서 0으로 가면 s, 0에서 10으로 가면 d, 10에서 0으로 가면 a
def solution(numLog):
    result = ''
    for i in range(len(numLog)):
        if i >= 1:
            check = numLog[i] - numLog[i - 1]
            if check == 1:
                result += "w"
            elif check == -1:
                result += "s"
            elif check == 10:
                result += "d"
            elif check == -10:
                result += "a"
    return result
# numLog = [0, 1, 0, 10, 0, 1, 0, 10, 0, -1, -2, -1]
# print(solution(numLog))
## 다른 풀이
# def solution(log):
#     result = ''
#     joystick = dict(zip([1,-1,10,-10], ['w','s','d','a']))
#     for i in range(1, len(log)):
#         result += joystick[log[i] - log[i-1]]
#     return result


'''
정수 배열 arr와 2차원 정수 배열 queries이 주어집니다. queries의 원소는 각각 하나의 query를 나타내며, [i, j] 꼴입니다.
각 query마다 순서대로 arr[i]의 값과 arr[j]의 값을 서로 바꿉니다.
위 규칙에 따라 queries를 처리한 이후의 arr를 return 하는 solution 함수를 완성해 주세요.

arr	            queries	                result
[0, 1, 2, 3, 4]	[[0, 3],[1, 2],[1, 4]]	[3, 4, 1, 0, 2]
'''
def solution(arr, queries):
    for q in queries:
        arr[q[0]], arr[q[1]] = arr[q[1]], arr[q[0]]
    return arr
# arr = [0, 1, 2, 3, 4]
# queries = [[0, 3],[1, 2],[1, 4]]
# print(solution(arr, queries))
## 다른 풀이
# def solution(arr, queries):
#     for a,b in queries:
#         arr[a],arr[b]=arr[b],arr[a]
#     return arr
# a, b는 queries 리스트의 각 튜플에서 가져온 두 개의 인덱스 값


'''
정수 배열 arr와 2차원 정수 배열 queries이 주어집니다. queries의 원소는 각각 하나의 query를 나타내며, [s, e, k] 꼴입니다.
각 query마다 순서대로 s ≤ i ≤ e인 모든 i에 대해 k보다 크면서 가장 작은 arr[i]를 찾습니다.
각 쿼리의 순서에 맞게 답을 저장한 배열을 반환하는 solution 함수를 완성해 주세요.
단, 특정 쿼리의 답이 존재하지 않으면 -1을 저장합니다.

arr	            queries	                        result
[0, 1, 2, 4, 3]	[[0, 4, 2],[0, 3, 2],[0, 2, 2]]	[3, 4, -1]
'''
def solution(arr, queries):
    result = []
    for q in queries:
        arrList = arr[q[0]:q[1] + 1]
        min_value = min((i for i in arrList if i > q[2]), default = -1)
        result.append(min_value)
    return result
arr = [0, 1, 2, 4, 3]
queries = [[0, 4, 2],[0, 3, 2],[0, 2, 2]]
print(solution(arr, queries))
# default = -1은 min() 함수에 대한 값이 없을 경우 -1을 반환한다는 것!