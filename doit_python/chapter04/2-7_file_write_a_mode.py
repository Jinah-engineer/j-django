'''
    파일에 새로운 내용 추가하기
        - 쓰기모드(w) 로 파일을 열 때 이미 존재하는 파일을 열면 그 파일의 내용이 모두 사라지게 된다.
        - 하지만 추가모드(a)로 열면 원래 있던 값을 유지하면서 새로운 값만 추가하는 것이 가능하다
'''
f = open('새파일.txt', 'a', encoding='utf-8')
for i in range(11, 20):
    data = "%d 번째 줄입니다. \n" % i
    f.write(data)
f.close()

