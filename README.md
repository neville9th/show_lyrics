# show_lyrics

* ターミナル画面にいい感じに歌詞を表示するためのPythonプログラムです。

# Features

* MV作成時、テキストボックスを曲に合わせて切り替える作業があると思います。
* しかし、タイミングを合わせるのはかなり根気のいる作業かと思います。
* このプログラムはゲーム感覚(?)で用意しておいた歌詞を1行ずつ表示させることができます。

# Requirement
 
* Python3実行環境

# Usage

Terminalから以下のように実行します。
歌詞のファイルはプログラムと同じディレクトリにご用意ください。

```bash
python3 show_lyrics.py
Enter the path to the text file: "ここに任意のtxtファイル名を入力"
Enter the path to the text file: void.txt # ここではサンプルファイルとしてvoid.txtと入力
```

キー入力操作
* Enterキー
    * 1行目ずつ次々に歌詞を上書きしていきます。
* Spaceキー → Enterキー
    * 直前に表示した歌詞は消えずに次の行に表示します。

タイミング良く使いこなすと、キャプチャ動画がそのままMVになります。

# Note
 
活用楽曲
* https://www.nicovideo.jp/watch/sm43441444
 
# Author
 
作成情報を列挙する
* neville
 
# License
ライセンスを明示する
 
"hoge" is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).
