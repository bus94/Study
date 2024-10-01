# 20240923 day20.py

# day20 함수(메서드)


'''
정수 배열 arr이 매개변수로 주어집니다. arr의 길이가 2의 정수 거듭제곱이 되도록 arr 뒤에 정수 0을 추가하려고 합니다. 
arr에 최소한의 개수로 0을 추가한 배열을 return 하는 solution 함수를 작성해 주세요.

arr	                result
[1, 2, 3, 4, 5, 6]	[1, 2, 3, 4, 5, 6, 0, 0]
[58, 172, 746, 89]	[58, 172, 746, 89]
'''
def solution(arr):
    i = 0
    while True:
        if len(arr) < 2 ** i:
            arr = arr + [0] * (2 ** i - len(arr))
        if len(arr) == 2 ** i:
            break
        i += 1
    return arr
# print(solution([1, 2, 3, 4, 5, 6]))
# print(solution([58, 172, 746, 89]))
## 다른 풀이
# def solution(arr):
#     a = 1
#     b = len(arr)
#     while a < b :
#         a *= 2
#     return arr + [0] * (a - b)
# 기본적으로 arr의 길이가 2의 거듭제곱 형태가 나오면 while문이 끝나게 된다. 그 전까지는 a가 거듭제곱을 반복하게 된다.
# 만약 arr의 길이가 2의 거듭제곱 형태가 된다면 arr만 반환되고, 남은 공간이 있다면 그 개수만큼 리스트에 0을 추가한다.


'''
이 문제에서 두 정수 배열의 대소관계를 다음과 같이 정의합니다.
두 배열의 길이가 다르다면, 배열의 길이가 긴 쪽이 더 큽니다.
배열의 길이가 같다면 각 배열에 있는 모든 원소의 합을 비교하여 다르다면 더 큰 쪽이 크고, 같다면 같습니다.
두 정수 배열 arr1과 arr2가 주어질 때, 
위에서 정의한 배열의 대소관계에 대하여 arr2가 크다면 -1, arr1이 크다면 1, 두 배열이 같다면 0을 return 하는 solution 함수를 작성해 주세요.

arr1	            arr2	            result
[49, 13]	        [70, 11, 2]	        -1
[100, 17, 84, 1]	[55, 12, 65, 36]	1
[1, 2, 3, 4, 5]	    [3, 3, 3, 3, 3]	    0
'''
def solution(arr1, arr2):
    if len(arr1) != len(arr2):
        if len(arr1) > len(arr2):
            return 1
        else:
            return -1
    else:
        if sum(arr1) > sum(arr2):
            return 1
        elif sum(arr1) < sum(arr2):
            return -1
        else:
            return 0
# print(solution([49, 13], [70, 11, 2]))
# print(solution([100, 17, 84, 1], [55, 12, 65, 36]))
# print(solution([1, 2, 3, 4, 5], [3, 3, 3, 3, 3]))
## 다른 풀이
# def solution(arr1, arr2):
#     return (len(arr1) > len(arr2)) - (len(arr2) > len(arr1)) or (sum(arr1) > sum(arr2)) - (sum(arr2) > sum(arr1))
# 1. len(arr1) > len(arr2) : 참 1, 거짓 0 반환
# 2. (len(arr1) > len(arr2)) - (len(arr2) > len(arr1)) 기준으로 arr1이 더 길면 1, arr2가 더 길면 -1, 같으면 0을 반환
# 3. 2번의 첫 번째 조건의 값으로 0이 아닌 값 즉 길이가 다르다면 그대로 반환하게 된다. (or는 첫 번째 조건이 True이면 두 번째 조건을 실행하지 않는다)
# 4. 2번의 첫 번째 조건의 값으로 0 즉 길이가 같다면 두 번째 조건을 실행하게 되는데,
#    마찬가지로 arr1의 합이 더 크다면 1, arr2의 합이 더 크다면 -1, 두 리스트의 각각의 합이 서로 같다면 0을 반환하게 된다.

'''
문자열 배열 strArr이 주어집니다. 
strArr의 원소들을 길이가 같은 문자열들끼리 그룹으로 묶었을 때 가장 개수가 많은 그룹의 크기를 return 하는 solution 함수를 완성해 주세요.

strArr	                    result
["a","bc","d","efg","hi"]	2
'''
def solution(strArr):
    countDict = {}
    for s in strArr:
        l = len(s)
        if l in countDict:
            countDict[l] += 1
        else:
            countDict[l] = 1
    return max(countDict.values(), default=0)
# print(solution(["a","bc","d","efg","hi"]))
## 다른 풀이
# def solution(strArr):
#     a=[0]*31
#     for x in strArr: 
#         a[len(x)] += 1
#     return max(a)
# 문제에 주어진 조건으로 strArr의 원소의 길이가 1이상 30 이하이므로 인덱스는 0번부터 시작하므로 총 31개(인덱스 기준 0번~30번)의 리스트 요소 갯수를 설정해서 카운트 될 때마다 1씩 더해서 최종 리스트에서 max로 구하는 방법이다.

'''
정수 배열 arr과 정수 n이 매개변수로 주어집니다. 
arr의 길이가 홀수라면 arr의 모든 짝수 인덱스 위치에 n을 더한 배열을, 
arr의 길이가 짝수라면 arr의 모든 홀수 인덱스 위치에 n을 더한 배열을 return 하는 solution 함수를 작성해 주세요.

arr	                    n	result
[49, 12, 100, 276, 33]	27	[76, 12, 127, 276, 60]
[444, 555, 666, 777]	100	[444, 655, 666, 877]
'''
def solution(arr, n):
    l = len(arr)
    if l % 2:
        for i in range(l):
            if not i % 2:
                arr[i] += n
    else:
        for i in range(l):
            if i % 2:
                arr[i] += n
    return arr
# print(solution([49, 12, 100, 276, 33], 27))
# print(solution([444, 555, 666, 777], 100))
## 다른 풀이
def solution(arr, n):
    N = len(arr)
    if N % 2:
        for i in range(0, N, 2): 
            arr[i] += n
    else:
        for i in range(1, N, 2): 
            arr[i] += n
    return arr
# 같은 알고리즘의 코드
# 홀수와 짝수를 짝수의 시작은 0부터 증감값으로 2, 홀수의 시작은 1부터 증감값으로 2로 설정해서 코드를 줄일 수 있다.


'''
정수로 이루어진 리스트 num_list가 주어집니다. 
num_list에서 가장 작은 5개의 수를 오름차순으로 담은 리스트를 return하도록 solution 함수를 완성해주세요.

num_list	                result
[12, 4, 15, 46, 38, 1, 14]	[1, 4, 12, 14, 15]
'''
def solution(num_list):
    num_list.sort()
    return num_list[:5]
# print(solution([12, 4, 15, 46, 38, 1, 14]))
## 다른 풀이
# def solution(num_list):
#     return sorted(num_list)[:5]
# 좀 더 간단한 코드로 작성했다.