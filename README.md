# GraphPlot

学習曲線などのグラフをプロットしてくれるchainerのTrainer向けExtensionです。

## 使用例

#### 学習曲線を描く

```python

# setup trainer

trainer.extend(GlaphPlot(('main/accuracy', 'validation/main/accuracy'), 
                         ylim=(0, 1),
                         trigger=(100, 'iteration'), file_name='accuracy.png'))

```

複数使用することもできます。

```python

# setup trainer

trainer.extend(GlaphPlot(('main/accuracy', 'validation/main/accuracy'), 
                         ylim=(0, 1),
                         trigger=(100, 'iteration'), file_name='accuracy.png'))
trainer.extend(GlaphPlot(('main/loss', 'validation/main/loss'), 
                         ylim=(0, 10),
                         trigger=(100, 'iteration'), file_name='loss.png'))

```

## 引数

```python
GraphPlot(y_keys, x_key='iteration', trigger=(1, 'epoch'), xlim=None, ylim=None, file_name='graph.png')
```

- `y_keys`

    y軸にプロットする値。str、またはstrのタプルで複数指定も可能
    
- `x_key`

    x軸にプロットする値。デフォルトは `iteration`
    
- `xlim`

    x軸の値の範囲。未指定の場合はデータに応じて自動的に設定される。
    
- `ylim`

    y軸の値の範囲。未指定の場合はデータに応じて自動的に設定される。
    
- `file_name`

    出力ファイル名。 `trainer` の `out` ディレクトリ内部に出力されます。