import random

target = random.randint(1, 100)
print("猜数字游戏：我想了一个 1-100 之间的数字")

while True:
    guess = int(input("请输入你的猜测: "))
    if guess < target:
        print("太小了")
    elif guess > target:
        print("太大了")
    else:
        print("恭喜你，猜对了！")
        break

