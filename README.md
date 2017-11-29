# Humor Generator

## to do 
- 実験環境の作成
- 画像間類似度を計算する際のテーブルを修正
    + オブジェクト候補をどのように選定すべきか？
    + 主観である程度抽象度の高い対象をピックアップしてよいか？
- 単語間類似度の計算時に，-の値を考慮せず，昇順にソートしているため，絶対値に変換する．
- word2vecの学習
    + 日本語wikipediaデータの前処理
    + gensimでの学習
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

## 実験環境について
- 実験の種類
    + 普通のキャプションと提案手法でユーモアの受容性について差が見られるかどうか
    + img_sim, word_simの関係性によりユーモアの受容性がどのように変化するか？
        - 単に単語間類似度と画像間類似度を調整&ランダムの2要因分散分析で良い？
        - 画像間類似度と単語間類似度を考慮した最終的なスコアに基づいたものがユーモアの受容性が一番高いか？
            * final_score = img_sim * (1 - word_sim)
        - システムによって対話継続欲求が向上するかどうか

# done

- 画像間類似度を計算する際，上位n個の対象を除外
