使うモデルファイルは nn/network/dual_net.py のフィルタ、ブロック数に合わせる。
使用モデル: sl-01 または rl-elmo
多分前者の方が強い。

sl- :教師あり学習
rl- :強化学習

sl-default.bin: デフォルト。64, 6
sl-00.bin: NN のフィルタ数 128, ブロック数 10
sl-01.bin: NN のフィルタ数 192, ブロック数 15

rl-default.bin: 強化学習デフォルト。64, 6
rl-elmo.bin: 数手先の value と勝敗をミックスして学習させたモデル。 192, 15
rl-model.bin: 不明。だけど強化学習の時にこのファイル名で出力される。
