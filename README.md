# utf8-12

一个轻量的 UTF-8 编码/解码 Python 库，保留了原始 `BM.py` 的核心能力：

- 文本转 UTF-8 十六进制字符串
- UTF-8 十六进制字符串转原始文本
- 可作为 CLI 使用

## 安装

```bash
pip install .
```

## 用法

```python
from utf8_12 import utf8_encode_raw, utf8_decode_raw

text = "Hello, 世界!"
encoded = utf8_encode_raw(text)
print(encoded)
print(utf8_decode_raw(encoded))
```

## CLI

```bash
python -m utf8_12 --tout "Hello"
python -m utf8_12 --tin "48 65 6C 6C 6F"
```
