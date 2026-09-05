import argparse

from .core import utf8_decode_raw, utf8_encode_raw


def main() -> int:
    parser = argparse.ArgumentParser(
        prog="utf8_12",
        description="UTF-8 编解码工具 --tout 编码 / --tin 解码",
    )
    parser.add_argument("input", help="输入文本(编码) / 空格分隔十六进制(解码)")
    parser.add_argument("--tout", action="store_true", help="编码模式：文本转 UTF-8 十六进制")
    parser.add_argument("--tin", action="store_true", help="解码模式：十六进制转原始文本")
    args = parser.parse_args()

    if args.tout and args.tin:
        print("错误：--tout 和 --tin 不能同时使用！")
        return 2
    if not args.tout and not args.tin:
        print("错误：必须指定 --tout（编码）或 --tin（解码）")
        return 2

    try:
        if args.tout:
            print(utf8_encode_raw(args.input))
        else:
            print(utf8_decode_raw(args.input))
        return 0
    except Exception as err:
        print(f"运行错误：{err}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
