# jutatus-examples

オンライン機械学習向け分散処理フレームワーク**Jubatus**のサンプルコードです。

## インストール(macOS)

JubatusをHomebrewでインストールする:

```
brew tap jubatus/jubatus
brew install jubatus --enable-mecab
```

mecabとmecab用辞書をインストールする:

```
brew install mecab mecab-ipadic
```

## 各種操作方法

各サンプルのディレクトリに`cd`した後、下記の各種操作が可能です。

* Jubatusサーバの起動: `make server`
* 学習させる: `make train`
* 学習に基づき問題を解決される: `make solve`

## 各種サンプル

* recommender-related-blog-posts: 関連するブログ記事を推薦します。特徴抽出はmecabによる名詞抽出、特徴量はtf-idfによる名詞頻出数。

