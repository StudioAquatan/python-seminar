# Python講座

スクリプト言語は世界共通語．

## 環境構築

---

目次

1. [各種ツールのバージョン](#各種ツールのバージョン)
2. [Windowsでの環境構築](#windowsでの環境構築)
3. [Ubuntuでの環境構築](#ubuntuでの環境構築)
4. [パッケージのインストール](#パッケージのインストール)
   1. [pip](#pip)
   2. [conda](#conda)
5. [IDE](#ide)

---

### 各種ツールのバージョン

2017/12/8現在のものを記載しています．

#### Windows

* Windows 10 バージョン1709


* [Miniconda3](https://conda.io/miniconda.html)
  * `conda` 4.3.30
* Python > 3.5

#### Ubuntu

* Ubuntu 16.04 LTS (or Windows Subsystem for Linux on Windows 10 バージョン1709)


* [anyenv](https://github.com/riywo/anyenv)
* [pyenv](https://github.com/yyuu/pyenv)

### Windowsでの環境構築

Windows 10にあらずんばWIndowsにあらず．

#### 1. Python実行環境のインストール

[miniconda](https://conda.io/miniconda.html)を使用．

上記リンクよりPython3.*のWindows 64bit向けインストーラを取得，インストール．

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

#### 2. 仮想環境の作成

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


### Ubuntuでの環境構築

Ubuntu/MacではAnacondaやMinicondaを直接インストールするのはリスクが高すぎるため，これらを使用するにせよ`pyenv`を通して使用することを推奨する．

#### 1. anyenvのインストール

`anyenv`は`**env`系のツールを統括して扱えるツール．

* `pyenv` - Python
* `rbenv` - Ruby
* `ndenv` - Node.js
* `phpenv` - PHP

など，様々な言語のバージョン管理が出来る．

`.bash_profile`派の人，`zsh`など別のシェルを使っている人は`.basrhc`を適宜読み替えること．

```bash
$ git clone https://github.com/riywo/anyenv ~/.anyenv
```

`.bashrc`に下記を追記

```bash
if [ -d $HOME/.anyenv ] ; then
    export PATH="$HOME/.anyenv/bin:$PATH"
    eval "$(anyenv init -)"
fi
```

再読み込みしてanyenvコマンドが使えることを確認

```bash
$ source ~/.bashrc
$ anyenv -h
anyenv
Usage: anyenv <command> [<args>]

Some useful anyenv commands are:
   commands            List all available anyenv commands
   local               Show the local application-specific Any version
   global              Show the global Any version
   install             Install a **env
   uninstall           Uninstall a specific **anv
   version             Show the current Any version and its origin
   versions            List all Any versions available to **env

See `anyenv help <command>' for information on a specific command.
For full documentation, see: https://github.com/riywo/anyenv#readme
```

#### 2. pythonのインストール

まずpyenvをインストールする．

```bash
$ anyenv install pyenv
$ source ~/.bashrc
$ pyenv -v
```

依存ライブラリのインストールをし，pythonをインストール．

```bash
$ sudo apt-get install -y gcc make openssl libssl-dev libbz2-dev libreadline-dev libsqlite3-dev zlib1g-dev
$ pyenv install 3.6.3
$ pyenv install 2.7.14
```

他に`pyenv install --list`からインストール可能なバージョン一覧を取得できる．通常のpythonの他に，AnacondaやMinicondaのインストールも可能である．

#### 3. pyenv-virtualenvのインストール

pyenvのみではバージョン変更はできても，仮想環境切り替えを行うことが出来ない．そこで`pyenv-virtualenv`というプラグインを導入する．

```bash
$ git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
```

#### 4. 仮想環境の作成

`pyenv virtualenv {pythonバージョン} {仮想環境名}`で仮想環境を作成することが出来る．

```bash
$ pyenv virtualenv 3.6.3 seminar
```

この仮想環境は`~/.anyenv/envs/pyenv/versions/seminar`以下に存在する．

pyenvにはglobalとlocalという考え方がある．global，つまりシステムのどこでも呼び出すpythonのバージョンを指定する，また，local，つまりあるディレクトリ直下において呼び出すpythonバージョンを指定することができる．localはglobalを常にオーバーライドするため，特定ディレクトリ直下では自動的にpython3を呼ぶようにする，などが可能である．このときバージョンだけでなく，作成した仮想環境名を指定することも可能である．

```bash
$ pyenv global 2.7.14 3.6.3
$ pyenv global
2.7.14
3.6.3
$ python -V
2.7.14
$ python3 -V
3.6.3
$ pyenv local seminar
$ python -V
3.6.3
```

これらpythonまたはpython3コマンドは`~/.anyenv/envs/pyenv/shims/python（またはpython3）`というシンボリックリンクを叩いているに過ぎないので，`which python`しても仮想環境のインタプリタを直接表示するわけでは無いことに注意．

### パッケージのインストール

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

また，`pip`でインストールできない依存関係にあるライブラリなどは自動でインストールしてくれるわけではない．そのため，必要なライブラリは`apt-get`や`brew`などを用いて自分で導入する必要がある．

##### conda

`conda`コマンドはAnacondaとMiniconda専用のパッケージ管理システム，及び環境管理ツール．pythonのパッケージではよく依存関係にある他のCなどのライブラリをコンパイルするためにgccを要求したり，その他UNIX系特有のライブラリを必要とすることがある．しかしWindowsではそれらを用意するために紆余曲折を経た後挫折する道しかなく，人々はWindowsを捨てMacBookを手に取ることとなる．

AnacondaとMinicondaはコンパイル済みのパッケージを配布してくれるため，Windowsでも高速なCのライブラリを活用した計算ライブラリなどを容易に使用することが出来るようになる．

```cmd
> conda install {入れたいパッケージ}
```

### IDE

Pythonを書くこと自体はちょっとしたテキストエディタで可能である．最近であればAtom，VS Code，SublimeTextなどがある．が，仮想環境に対応させ，それに応じた補完候補を表示したりすることは面倒でありIDEの使用を推奨する．

あくあたん工房ではJetbrains製のIDEをスタンダードとしている．Python向けのIDE製品はPyCharmと呼ばれ，学生はProfessional版を無料で使用可能である．

##### 学生登録

無料で利用するためには学生アカウントを作成する必要がある．

1. [Free individual licenses for students and faculty members](https://www.jetbrains.com/student/)にアクセスし，`Apply Now`をクリック
2. 必要事項を記入
   - メールアドレスには`.ac.jp`のものを使用すること
3. 送信されてきたメールからアクティベート

##### インストール

1. [PyCharm](https://www.jetbrains.com/pycharm/)からProfessional版をダウンロード
2. 基本`Next`連打で構わない
3. PyCharmを起動後，アカウントを用いた認証を選択し，学生登録時のメールアドレス等で認証する

##### インタプリタの指定

以下，パスは適宜読み替えること．

* Windows
  * 仮想環境のインタプリタへのパス: `C:\Users\{ユーザ名}\.conda\envs\seminar\python.exe`
* Ubuntu
  - 仮想環境のインタプリタへのパス: `~/.anyenv/envs/pyenv/versions/seminar/bin/python`

以下，PyCharm 2017.3（build on Nov 29, 2017）を対象として説明する．

1. `Create new project`から新しいプロジェクトを作成
2. プロジェクト名（デフォルトは`untitled`）を`seminar`とする
3. pythonインタプリタまでのパスを指定する．`…`をクリックし，`Add local`を選択，`Conda Environment`から`Existing environment`を選択し，`Interpreter`から`seminar`のものを選択する．表示されない場合`…`から`C:\Users\{ユーザ名}\.conda\envs\seminar\python.exe`を指定．
4. `OK`
5. 設定を開く
6. `Project: seminar`から`Project Interpreter`を選択．`C:\Users\{ユーザ名}\.conda\envs\seminar\python.exe`が指定されていることを確認する

初期はインデクシングにより操作が重くなる可能性がある．

