# 당신은 cocoa 서비스를 이용하는 택시 기사입니다.
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

# 조건 1 : 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
# 조건 2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.

from random import *


# 총 탑승 승객 수
cnt = 0

for i in range(1, 51):
    time = randrange(5, 51) # 5~50 분 사이의 소요 시간
    if 5 <= time <= 15: # 5분~15분 이내의 손님, 탑승 승객 수 증가 처리
        print("[0] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
        cnt += 1
    else: # 매칭 실패한 경우
        print("[] {0}번째 손님 (소요시간 : {1}분)".format(i, time))

print('총 탑승 승객: {0}분' .format(cnt))