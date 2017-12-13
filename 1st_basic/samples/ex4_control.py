import random

if __name__ == '__main__':

    # xに1~10の乱数を入れる
    x = random.randint(1, 10)
    if x < 5:
        print('LOW')
    else:
        print('HIGH')

    # こんな書き方もできる
    if 4 < x < 6:
        print('x is 5!!')


    for i in range(10):
        print(i)

    while x > 0:
        print(x)
        x -= 1