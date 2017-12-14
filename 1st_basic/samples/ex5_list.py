if __name__ == '__main__':

    a = [2, 4, 1, 3]
    print(a)

    # ソート
    a.sort()
    print(a)

    # 追加
    a.append(4)
    print(a)

    # 削除
    a.remove(4)
    print(a)

    # 長さ
    print(len(a))

    # アクセス
    print(a[1])
    print(a[-2])

    # 要素があるかどうか
    print(1 in a)


    # forと併用できる優れもの
    names = ['hoge', 'huga', 'foo', 'bar', 'piyo']
    for name in names:
        print(name)

    for idx, name in enumerate(names):
        print(idx, name)