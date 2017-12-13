if __name__ == '__main__':

    print('Hello World!!')
    print('Hello', 'World', '!!')

    # 改行削除もできる
    print('Hello'+'World'+'!!', end='')
    print('hoge')

    # 全て文字列(str)で取得される
    line = input()
    print(type(line), line)

    # キャスト
    line_int = int(line)
    line_float = float(line)