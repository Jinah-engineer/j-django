try:
    print('나누기 전용 계산기 입니다.')

    nums = []
    # num1 = int(input('첫 번째 숫자를 입력하세요 : '))
    # num2 = int(input('두 번째 숫자를 입력하세요 : '))
    nums.append(int(input('첫 번째 숫자를 입력하세요 : ')))
    nums.append(int(input('두 번째 숫자를 입력하세요 : ')))
    nums.append(int(nums[0] / nums[1]))
    print('{0} / {1} = {2}'.format(nums[0], nums[1], nums[2]))

    # print('{0} / {1} = {2}'.format(num1, num2, int(num1/num2)))

except ValueError:
    print('Error evoked!')

except ZeroDivisionError as err:
    # 발생하는 에러문장을 그대로 출력한다.
    print(err)

except Exception as err:
    print('알 수 없는 에러가 발생하였다.')
    print(err)
