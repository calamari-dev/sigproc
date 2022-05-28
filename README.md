# 信号解析の数理

この本は書きかけであり，内容の正しさについては一切保証できません．

## PDFのダウンロード方法

ベータ版を<https://github.com/calamari-dev/sigproc/releases>で配布する予定です．なお，各ブランチにあるLaTeXソースは下書きやメモを含むため，誤りを含む可能性が多分にあります．そのため，内容に関するご指摘は最新のリリースに対してお願い致します．

## ライセンス

+ `src/`以下のファイルは[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.ja)の下で配布しています
+ `fonts/`以下のファイルは各フォントのライセンスの下で再配布しています

## ビルド方法

```
$ docker compose build
$ docker compose run sigproc
$ pipenv sync --dev # 初回のみ
$ pipenv run publish
```
