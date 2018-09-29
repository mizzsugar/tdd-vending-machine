## TDDBC 感想
コードレビューのタイミングでコミットログを順番にみていくの良い
逆にいうとコミットログ見ながら何をやったのか分かる粒度でちゃんとコミットしよう

testファイルの上に#TODO: hoge が全部のこってるの良い
コミットログはこれでどうでしょう？？？？
```
red: 200円でレッドブルが買える
green:
refactor: 変数名の変更

red: 100円だけならレッドブルが買えないようにする
green:
refactor: 関数名の変更
```
```
add: red: 200円でレッドブルが買える
add: green:
add: refactor: 変数名の変更

add: red: 100円だけならレッドブルが買えないようにする
add: green:
add: refactor: 関数名の変更
```
どっちがいいのか
けどred == add refactor == update になるような気がするので上で良い気がする
