# suumo-get-propterty-list


## PCにpython言語をインストールする手順
https://www.python.jp/install/windows/install.html

## ライブラリのインストール
●コマンドプロンプト上で以下のコマンドを実行<br>
pip install pandas openpyxl requests beautifulsoup4 argparse

●上記のコマンド実行時に、パスが通ってないという旨のエラーが出た場合は以下のコマンドを実行<br>
py -m pip install pandas openpyxl requests beautifulsoup4 argparse

## スクリプトの実行
ファイルのある場所まで移動
cd の後ろに実行したいファイルのあるフォルダーをドラック＆ドロップ
例）
get-property-listのフォルダーをドラック＆ドロップするとcd [ファイルの住所]というコマンドになるから、enterで実行⇒現在地が指定したフォルダーの住所へ移動する<br>
### コマンドプロンプトを開いた際の初期地
<img width="726" alt="image" src="https://github.com/taiga32/suumo-get-propterty-list/assets/69178111/9e726c08-72e9-43cb-9064-c258bcbe42d3"><br>
### pythonファイルの場所を確認
<img width="321" alt="image" src="https://github.com/taiga32/suumo-get-propterty-list/assets/69178111/410d8c06-0e79-4c2c-a226-54b1e0f79d4c"><br>
### ドラック＆ドロップ後のイメージ
<img width="408" alt="image" src="https://github.com/taiga32/suumo-get-propterty-list/assets/69178111/413068b9-8f78-4d1d-b7a1-2e379ed6964e"><br>

## ファイル直上のフォルダーに現在地が変わったら
以下のコマンドをEnterして、ファイルを実行する
Python3 ./get-property-abst.py --url "https://suumo.jp//jj/bukken/ichiran/JJ012FC002/?ar=030&bs=011&cn=9999999&cnb=0&ekTjCd=&ekTjNm=&kb=1&kt=9999999&mb=0&mt=9999999&sc=13113&ta=13&tj=0&bknlistmodeflg=2&pc=30&pn=1" --max_pages 2

### 実行時の注意点
上記のコマンドには、２つのユーザー指定の値を設定する必要がある。<br>
１つは--url の後ろについているurl。これは物件一覧のページリンクをコピペする。<br>
※""の中にコピペすることを忘れずに！

２つは--max_pages についている数字。何ページ分の物件一覧を取得するかを設定する。
