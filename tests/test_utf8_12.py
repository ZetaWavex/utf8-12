import pytest

from utf8_12 import utf8_decode_raw, utf8_encode_raw


def test_encode_ascii():
    assert utf8_encode_raw("ABC") == "41 42 43"


def test_encode_multibyte():
    assert utf8_encode_raw("中") == "E4 B8 AD"
    assert utf8_encode_raw("😀") == "F0 9F 98 80"


def test_decode_roundtrip():
    text = "Hello, 世界! 😀"
    encoded = utf8_encode_raw(text)
    assert utf8_decode_raw(encoded) == text


def test_decode_rejects_invalid_hex():
    with pytest.raises(ValueError, match="长度必须为偶数|非法十六进制数据"):
        utf8_decode_raw("0A0")


def test_decode_rejects_invalid_utf8():
    with pytest.raises(ValueError, match="UTF-8|解码失败"):
        utf8_decode_raw("FF")
