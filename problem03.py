# 문제 3
# 중첩 루프를 이용해 신문 배달을 하는 프로그램을 작성하세요.
# 단, 아래에서 arrears 리스트는 신문 구독료가 미납된 세대에 대한 정보를 포함하고 있는데,
# 해당 세대에는 신문을 배달하지 않아야 합니다.
#
apart = [[101, 102, 103, 104],[201, 202, 203, 204],[301, 302, 303, 304], [401, 402, 403, 404]]
arrears = [101, 203, 301, 404]

# for i in range(len(apart)):
#     for j in range(len(apart[i])):
#         if apart[i][j] in arrears:
#             continue
#         print('Newspaper delivery : {0}'.format(apart[i][j]))

for floor in apart:
    for home in floor:
        if home not in arrears:
            print('Newspaper delivery : {0}'.format(home))
            # print(f'Newspaper delivery : {home}')
            # print('Newspaper delivery : %d' % home)

