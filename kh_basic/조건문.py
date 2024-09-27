# 제어문이란? 조건문과 반복문의 의미
# num = int(input("정수값 입력 : "))
#
# if num > 100:
#     print(f"{num}은 100보다 커요")
# elif num < 100:
#     print(f"{num}은 100보다 작아요")
# else:
#     print(f"{num}은 100과 같아요.")

# 실습문제
# 성적을 입력 받아서 0 ~ 100사이가 아니면 성적을 잘못 입력 하였다고 표기
# 성적이 0 ~ 100이고,
# 90점 이상 이면 "A"
# 80점 이상 이면 "B"
# 70점 이상 이면 "C"
# 60점 이상 이면 "D"
# 나머지는 "F"

while True:
    score = int(input("성적 입력 : "))
    if 0 <= score <= 100:
        if score >= 90: print("A")
        elif score >= 80: print("B")
        elif score >= 70: print("C")
        elif score >= 60: print("D")
        else: print("F")
        break
    else:
        print("성적을 잘못 입력 하셨습니다.")

# 세자리 정수를 입력 받아 100의 자리, 10자리, 1자리로 나누어 담고
# 이 중 가장 큰 수 출력
# 몫과 나머지로 변수 할당
# if ~ else 값 비교
# 456 => a = 4, b = 5, c = 6
# num = int(input("정수 입력 : "))
# a = int(num[0])
# b = int(num[1])
# c = int(num[2])
# a = num // 100   # 456
# b = (num % 100) // 10
# c = num % 10
#
# if a > b:
#     if a > c: print(a)
#     else: print(c)
# else:
#     if b > c: print(b)
#     else: print(c)