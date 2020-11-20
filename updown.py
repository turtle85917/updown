import random

try:
    count = 5
    choice_number = random.randint(1, 51)
    while count != 0:
        print("1~50 사이에 숫자를 입력해주세요(기회: 5번):")
        number = int(input())
        if number > choice_number:
            print("입력한 숫자보다 작습니다!")
            count -= 1
        if number < choice_number:
            print("입력한 숫자보다 큽니다!")
            count -= 1
        if number == choice_number:
            print("정답입니다!")
            break
    if count == 0:
        print(f"기회 안에 다 맞추지 못 했네요..\n답은 {choice_number}!")
except: pass
