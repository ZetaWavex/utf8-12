import argparse

def utf8_encode_raw(text: str) -> str:
    data = b""
    for ch in text:
        code = ord(ch)
        if code <= 0x7F:
            data += bytes([code])
        elif code <= 0x7FF:
            b1 = 0xC0 | (code >> 6)
            b2 = 0x80 | (code & 0x3F)
            data += bytes([b1, b2])
        elif code <= 0xFFFF:
            b1 = 0xE0 | (code >> 12)
            b2 = 0x80 | ((code >> 6) & 0x3F)
            b3 = 0x80 | (code & 0x3F)
            data += bytes([b1, b2, b3])
        elif code <= 0x10FFFF:
            b1 = 0xF0 | (code >> 18)
            b2 = 0x80 | ((code >> 12) & 0x3F)
            b3 = 0x80 | ((code >> 6) & 0x3F)
            b4 = 0x80 | (code & 0x3F)
            data += bytes([b1, b2, b3, b4])
        else:
            raise ValueError(f"不支持字符：{ch}，码点超出 Unicode 范围")
    return data.hex(" ").upper()

def utf8_decode_raw(hex_str: str) -> str:
    clean_hex = hex_str.replace(" ", "").replace("\n", "")
    if len(clean_hex) % 2 != 0:
        raise ValueError("十六进制字符长度必须为偶数")
    try:
        byte_data = bytes.fromhex(clean_hex)
        return byte_data.decode("utf-8")
    except ValueError as e:
        raise ValueError(f"非法十六进制数据：{str(e)}")
    except UnicodeDecodeError:
        raise ValueError("不是合法的 UTF-8 字节流，解码失败")

def main():
    parser = argparse.ArgumentParser(prog="BM.py", description="BM UTF8 编解码工具 --tout编码 / --tin解码")
    parser.add_argument("input", help="输入文本(编码) / 空格分隔十六进制(解码)")
    parser.add_argument("--tout", action="store_true", help="编码模式：文本转UTF8十六进制")
    parser.add_argument("--tin", action="store_true", help="解码模式：十六进制转原始文本")
    arg = parser.parse_args()

    if arg.tout and arg.tin:
        print("错误：--tout 和 --tin 不能同时使用！")
        return
    if not arg.tout and not arg.tin:
        print("错误：必须指定 --tout（编码）或 --tin（解码）")
        return

    try:
        if arg.tout:
            res = utf8_encode_raw(arg.input)
            print(res)
        else:
            res = utf8_decode_raw(arg.input)
            print(res)
    except Exception as err:
        print(f"运行错误：{err}")

if __name__ == "__main__":
    main()
