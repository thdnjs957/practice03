# 문제5.
# 선택정렬(제자리 정렬 알고리즘)을 적용하는 코드를 완성하세요.
# 문제에 주어진 배열 [ 5, 9, 3, 8, 60, 20, 1 ] 를 크기 순서대로 정렬하여 다음과 같은 출력이 되도록 완성하는 문제입니다.
def sel_sort(a):
    n = len(a)
    for i in range(0, n - 1):
        max_idx = i
        for j in range(i + 1, n):
            if a[j] > a[max_idx]:
                max_idx = j
        a[i], a[max_idx] = a[max_idx], a[i] # 파이썬 swap

list1 = [5, 9, 3, 8, 60, 20, 1]

print('Before sort\n {0}'.format(list1))
sel_sort(list1)
print('After sort\n {0}'.format(list1))

