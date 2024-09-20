# 20240921 day20.py

# day20 함수(메서드)


'''
정수 배열 arr이 매개변수로 주어집니다. arr의 길이가 2의 정수 거듭제곱이 되도록 arr 뒤에 정수 0을 추가하려고 합니다. 
arr에 최소한의 개수로 0을 추가한 배열을 return 하는 solution 함수를 작성해 주세요.

arr	                result
[1, 2, 3, 4, 5, 6]	[1, 2, 3, 4, 5, 6, 0, 0]
[58, 172, 746, 89]	[58, 172, 746, 89]
'''
def solution(arr):
    answer = []
    return answer
print(solution([1, 2, 3, 4, 5, 6]))
print(solution([58, 172, 746, 89]))


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
    answer = 0
    return answer


'''
문자열 배열 strArr이 주어집니다. 
strArr의 원소들을 길이가 같은 문자열들끼리 그룹으로 묶었을 때 가장 개수가 많은 그룹의 크기를 return 하는 solution 함수를 완성해 주세요.

strArr	                    result
["a","bc","d","efg","hi"]	2
'''
def solution(strArr):
    answer = 0
    return answer


'''
정수 배열 arr과 정수 n이 매개변수로 주어집니다. 
arr의 길이가 홀수라면 arr의 모든 짝수 인덱스 위치에 n을 더한 배열을, 
arr의 길이가 짝수라면 arr의 모든 홀수 인덱스 위치에 n을 더한 배열을 return 하는 solution 함수를 작성해 주세요.

arr	                    n	result
[49, 12, 100, 276, 33]	27	[76, 12, 127, 276, 60]
[444, 555, 666, 777]	100	[444, 655, 666, 877]
'''
def solution(arr, n):
    answer = []
    return answer


'''
정수로 이루어진 리스트 num_list가 주어집니다. 
num_list에서 가장 작은 5개의 수를 오름차순으로 담은 리스트를 return하도록 solution 함수를 완성해주세요.

num_list	                result
[12, 4, 15, 46, 38, 1, 14]	[1, 4, 12, 14, 15]
'''
def solution(num_list):
    answer = []
    return answer