# Python講座

スクリプト言語は世界共通語．

## 環境構築

### Windows

Windows 10 64bitでない人に人権はない．  

ここでは以下の様に4つのセクションに分けて説明する．

1. Python実行環境のインストール
2. パッケージのインストール
3. 仮想環境の作成
4. IDE

#### 1. Python実行環境のインストール

[miniconda](https://conda.io/miniconda.html)を使用．

上記リンクよりPython3.*のWindows 64bit向けインストーラを取得，インストールします．

1. Install for `All Users`を選択して`Next`
   + パスが`C:\ProgramData\`以下になりわかりやすい
2. `Destination Folder`が`C:\ProgramData\Miniconda3`になっていることを確認して`Next`
3. `Add Anaconda to the system PATH environment variable`には**チェックを入れず**に`Register Anaconda as the system Python 3.*`のみにチェックを入れて`Install`
4. 終了したら`Next`
5. `Learn more ~`のチェックを全て外し終了

環境変数にパスを設定する．

1. `システムの詳細設定` > `詳細設定`  > `環境変数…` > `{ユーザ名}のユーザ環境変数`を開き，変数`Path`をダブルクリック
2. `新規…`から`C:\ProgramData\Miniconda3\Scripts`および`C:\ProgramData\Miniconda3`を追加
3. ウィンドウを閉じる
4. コマンドプロンプトを開いて`where conda`コマンドおよび`where python`コマンドを実行してそれぞれ`C:\ProgramData\Miniconda3\Scripts\conda.exe`と`C:\ProgramData\Miniconda3\python.exe`が表示されたら終了

##### conda, pythonコマンドが見つからない

環境変数の設定が間違っていないか確認し，再起動して再度実行する．

##### python.exeへのパスが異なる，複数のpython.exeが表示される

`MinGW`などでpythonをインストールしている場合，先にそちらのpythonが呼ばれてしまうことがある．Minicondaのpythonへのパスが一番上に表示されていれば問題ない．一番上にない場合，環境変数から読み込むパスの順番を変更する必要がある．このとき，ユーザの環境変数とシステムの環境変数の二つが存在することに注意して変更すること．通常システムの環境変数を読み込んでからユーザの環境変数を読み込むため，ユーザの環境変数で最も上に設定しても改善しない可能性がある．

#### 2. パッケージのインストール

pythonでは標準ライブラリの他に，有志らが作成した便利なライブラリを使用することが出来る．インストールする方法はいくつか存在するが，ここでは2つの方法のみを紹介する．

以下のどちらを用いても良いが，`conda`でインストールできるものとできないものがある（ビルド済みかどうかに依存する．低レイヤーのAPIを要求するメジャーなライブラリの場合，`conda`の方が上手くいく可能性が高い．）

##### pip

`pip`コマンドはpythonでは今やデファクトスタンダードとなったパッケージ管理システム．使用方法は単純で，`pip install {入れたいパッケージ}`として使用することが出来る．通常インストールされたパッケージはインストールされたpythonのディレクトリ以下に置かれる．

```cmd
> pip install requests
> python
>>> import requests
>>> # googleからwebページを取得
>>> body = requests.get('https://www.google.com/')
>>> # htmlのコードが表示される
>>> print(body.text)
>>> exit()
> pip uninstall requests
```

依存関係で一緒に入ってきたパッケージはアンインストールされない．

##### conda

`conda`コマンドはAnacondaとMiniconda専用のパッケージ管理システム，及び環境管理ツール．pythonのパッケージではよく依存関係にある他のCなどのライブラリをコンパイルするためにgccを要求したり，その他UNIX系特有のライブラリを必要とすることがある．しかしWindowsではそれらを用意するために紆余曲折を経た後挫折する道しかなく，人々はWindowsを捨てMacBookを手に取ることとなる．

AnacondaとMinicondaはコンパイル済みのパッケージを配布してくれるため，Windowsでも高速なCのライブラリを活用した計算ライブラリなどを容易に使用することが出来るようになる．

```cmd
> conda install {入れたいパッケージ}
```

#### 3. 仮想環境の作成

パッケージを複数インストールし続けていくと，プロジェクトをまたがってバージョンの変更が必要になることがある．また，ただ単に現在のプロジェクトにおけるパッケージの依存関係を明らかにするため，できる限り必要最低限のパッケージインストールで済ませることが望ましい．

今回の講座において使用する環境をセットアップする．

まず仮想環境を作成するパスを検討する．Python仮想環境はインタプリタなど実行環境をほぼ丸々コピーして作成され，それら個別の環境をコマンドを用いて切替えることができる．後にIDEで指定するとき楽にするため，作成されるディレクトリを予め定義しておく．

1. `conda config --add envs_dirs C:\Users\{ユーザ名}\.conda\envs`を実行すると，ユーザのホームディレクトリ（`C:\Users\{ユーザ名}`）以下に`.condarc`ファイルが作成される
2. `conda info`を実行し，`config file`に`C:\Users\{ユーザ名}\.condarc`が指定されているか確認
3. `conda info --show-sources`を実行し，`C:\Users\{ユーザ名}\.condarc`の中身が読み取れているか確認

仮想環境を作成する．`conda create -n {仮想環境名} {インストールするパッケージ（指定無しの場合pythonと入力）}`で作成できる．また`python=x.x`と入力することでそのバージョンの環境を作成できる．ここでは，バージョン3.6，仮想環境名を`seminar`とする

1. `conda create -n seminar python=3.6`を実行（`Package plan for installation in environment C:\Users\{ユーザ名}\.conda\envs\seminar:`となっているか確認すること）
2. `Proceed ([y]/n)?`に`y`と答えEnter
3. `activate seminar`を実行し，プロンプトの表示が`(seminar) C:\Users\{User}>`となっていれば成功．`where python`コマンドを実行し，`seminar`以下のpythonを呼べているか確認する．
4. `deactivate`で環境から抜ける


#### 4. IDE

Pythonを書くこと自体はちょっとしたテキストエディタで可能である．最近であればAtom，VS Code，SublimeTextなどがある．が，仮想環境に対応させ，それに応じた補完候補を表示したりすることは面倒でありIDEの使用を推奨する．

あくあたん工房ではJetbrains製のIDEをスタンダードとしている．Python向けのIDE製品はPyCharmと呼ばれ，学生はProfessional版を無料で使用可能である．

##### 学生登録

無料で利用するためには学生アカウントを作成する必要がある．

1. [Free individual licenses for students and faculty members](https://www.jetbrains.com/student/)にアクセスし，`Apply Now`をクリック
2. 必要事項を記入
   + メールアドレスには`.ac.jp`のものを使用すること
3. 送信されてきたメールからアクティベート

##### インストール

1. [PyCharm](https://www.jetbrains.com/pycharm/)からProfessional版をダウンロード
2. 基本`Next`連打で構わない
3. PyCharmを起動後，アカウントを用いた認証を選択し，学生登録時のメールアドレス等で認証する

##### インタプリタの指定

以下，PyCharm 2017.3（build on Nov 29, 2017）を対象として説明する．

1. `Create new project`から新しいプロジェクトを作成
2. プロジェクト名（デフォルトは`untitled`）を`seminar`とする
3. pythonインタプリタまでのパスを指定する．`…`をクリックし，`Add local`を選択，`Conda Environment`から`Existing environment`を選択し，`Interpreter`から`seminar`のものを選択する．表示されない場合`…`から`C:\Users\{ユーザ名}\.conda\envs\seminar\python.exe`を指定．
4. `OK`
5. `Ctrl + Alt + s`を押して設定を開く
6. `Project: seminar`から`Project Interpreter`を選択．`C:\Users\{ユーザ名}\.conda\envs\seminar\python.exe`が指定されていることを確認する

初期はインデクシングにより操作が重くなる可能性がある．

### Ubuntu

これから書く



