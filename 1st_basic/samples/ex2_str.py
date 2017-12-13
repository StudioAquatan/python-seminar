if __name__ == '__main__':

    # 連結
    a = 'hoge'
    b = 'foo'
    c = a + b
    print(c)

    a = 'hogehogefoobar'
    # 分割
    print(a.split('foo'))

    # 検索
    print(a.find('foo'))

    # 置換
    print(a.replace('foo', 'piyo'))

    # 埋め込み
    a = 'pi'
    b = 3.14
    print('{} is {}'.format(a, b))

    # 指定区切り文字で結合
    a = ['a', 'b', 'c', 'd']
    print(','.join(a))
