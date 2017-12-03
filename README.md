# Humor Generator

## to do 
- 実験環境の作成
- 画像間類似度を計算する際のテーブルを修正
    + オブジェクト候補をどのように選定すべきか？
    + 主観である程度抽象度の高い対象をピックアップしてよいか？
- word2vecのtrainをsave__word2vec_format(fname, binary=~True)に変更
- resnetのfine tuning用スクリプト作成
- humor_generatorの修正
    + 使用するキャプションの個数はどうするか？
    + キャプションにはどの学習済みデータを利用するか？（要検討）
    + img_word_sim classの適用
    + 画像間類似度計算クラスの計算量削減のためcaption generatorの中間ベクトルの取得
- caption genertorの修正
    + CNNから中間ベクトルの取得
- make_hype_listの修正
    + optionで指定した上位レベルでのhype listの作成

- 各モジュールのpathの指定方法
    + ENVで指定するのではなく，引数指定したほうが良いのでは？
- img simの計算時に用いるNORM_LISTの中国語版NORM_LIST_CHの実装
- caption生成時，及びimg_simの計算時に用いるCNNモデルの追加 VGG16, AlexNetなど
- ENV.pyでパスを指定するのではなく，引数指定に変更
- word2vecの学習時に，humorcaptionを生成するときのクラス，キャプション生成時の固有名詞をdictに含める
    + wikiのデータを分かち書きするときにそれらのデータを含める
- img_simに用いられるclass tableを修正する必要がある
    + 上位クラスの利用 and 同日クラスが出力されないようにする
## 実験環境について
- 実験の種類
    + 普通のキャプションと提案手法でユーモアの受容性について差が見られるかどうか
    + img_sim, word_simの関係性によりユーモアの受容性がどのように変化するか？
        - 単に単語間類似度と画像間類似度を調整&ランダムの2要因分散分析で良い？
        - 画像間類似度と単語間類似度を考慮した最終的なスコアに基づいたものがユーモアの受容性が一番高いか？
            * final_score = img_sim * (1 - word_sim)
        - システムによって対話継続欲求が向上するかどうか

- 曖昧さ耐性の低い個人と高い個人の2群に分ける必要性

