"""Byte/integer representation only; this is not the historical NAM transform."""


def encode(data: bytes) -> tuple[int, int]:
    if not isinstance(data, bytes):
        raise TypeError("data must be bytes")
    return int.from_bytes(data, "big"), len(data)


def decode(value: int, length: int) -> bytes:
    if type(value) is not int or type(length) is not int:
        raise TypeError("value and length must be integers")
    if value < 0 or length < 0 or value >= 1 << (8 * length):
        raise ValueError("value does not fit the specified non-negative byte length")
    return value.to_bytes(length, "big")


if __name__ == "__main__":
    print(f"bits 1010 -> decimal {int('1010', 2)}")
    sample = bytes.fromhex("000a")
    value, length = encode(sample)
    print(f"bytes {sample.hex()} -> integer {value}, length {length} -> bytes {decode(value, length).hex()}")
