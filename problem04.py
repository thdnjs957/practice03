# 문제4.
# 구구단 중에 특정 곱셈을 만들고 그 답을 선택하는 프로그램을 작성하는 문제입니다.
# 답을 포함하여 9개의 정수가 아래와 같은 형태로 출력되고 사용자는 답을 골라 입력하게 됩니다.
# 프로그램은 정답 여부를 다시 출력합니다.
import random

first = random.randrange(1,10)
second = random.randrange(1,10)
answer = first * second

print('{0} X {1}= ?'.format(first, second))

random_list = []

for i in range(1,10):
    for j in range(1,10):
        random_list.append(i*j)

get_random = set() # 빈 set 생성

get_random.add(answer)

while True:
    if len(get_random) == 9:
        break
    get_random.update((random.sample(random_list, 1)))

get_random = list(get_random)

random.shuffle(get_random)

for i in range(0, len(get_random)):
    if i % 3 == 0: print()
    print('{0} '.format(get_random[i]), end="\t\t")

print()

while True:
    user_input = input('answer')

    if int(user_input) == answer:
        print('정답')
        break

    print('오답')

