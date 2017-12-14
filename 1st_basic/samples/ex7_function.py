
def hello(user, time='morning'):
    if time == 'morning':
        return "Good morning {}".format(user)

    elif time == 'night':
        return "Good night ", user

    else:
        return "Hello {}".format(user)


if __name__ == '__main__':

    print(hello('aquatan'))

    # キーワード指定
    print(hello(user='aquatan'))

    # 複数返り値
    a, b = hello('aquatan', time='night')
    print(a, b)
