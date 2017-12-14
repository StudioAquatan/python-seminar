
def hello(user: str, time='morning') -> str:
    if time == 'morning':
        return "Good morning {}".format(user)

    elif time == 'night':
        # 返り値の型ヒントはstrなのでWarningが出るはず
        return "Good night ", user

    else:
        return "Hello {}".format(user)


if __name__ == '__main__':

    print(hello('aquatan'))

    # PycharmならWarningが出るはず
    print(hello(user=123))
