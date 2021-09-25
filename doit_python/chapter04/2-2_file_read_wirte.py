'''
    파일 생성하기

    파일 객체 = open(파일 이름, 파일 열기 모드)

        r : 읽기 모드 (파일을 읽기만 할 때 사용)
        w : 쓰기 모드 (파일에 내용을 쓸 때 사용)
        a : 추가 모드 (파일의 마지막에 새로운 내용을 추가할 때 사용)
'''
f = open("새파일.txt", 'w')
f.close()

'''
    파일을 쓰기모드로 열면 해당 파일이 이미 존재할 경우, 원래 있던 내용이 모두 사라지고,
    해당 파일이 존재하지 않으면, 새로운 파일이 생성된다
'''
