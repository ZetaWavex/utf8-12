def utf8_encode_raw(text: str) -> str:
    """Return UTF-8 bytes as uppercase hexadecimal bytes separated by spaces."""
    data = bytearray()
    for ch in text:
        code = ord(ch)
        if code <= 0x7F:
            data.append(code)
        elif code <= 0x7FF:
            data.extend((0xC0 | (code >> 6), 0x80 | (code & 0x3F)))
        elif code <= 0xFFFF:
            data.extend((
                0xE0 | (code >> 12),
                0x80 | ((code >> 6) & 0x3F),
                0x80 | (code & 0x3F),
            ))
        elif code <= 0x10FFFF:
            data.extend((
                0xF0 | (code >> 18),
                0x80 | ((code >> 12) & 0x3F),
                0x80 | ((code >> 6) & 0x3F),
                0x80 | (code & 0x3F),
            ))
        else:
            raise ValueError(f"不支持字符：{ch}，码点超出 Unicode 范围")
    return data.hex(" ").upper()


def utf8_decode_raw(hex_str: str) -> str:
    """Decode a UTF-8 byte stream represented as hexadecimal text."""
    clean_hex = hex_str.replace(" ", "").replace("\n", "").replace("\r", "")
    if len(clean_hex) % 2 != 0:
        raise ValueError("十六进制字符长度必须为偶数")
    try:
        byte_data = bytes.fromhex(clean_hex)
        return byte_data.decode("utf-8")
    except UnicodeDecodeError as e:
        raise ValueError("不是合法的 UTF-8 字节流，解码失败") from e
    except ValueError as e:
        raise ValueError(f"非法十六进制数据：{str(e)}")
