import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "examples"))
from representation import decode, encode


class RepresentationTests(unittest.TestCase):
    def test_round_trip_preserves_empty_and_leading_zero_bytes(self):
        for data in (b"", b"\x00", b"\x00\x0a", b"\x00\x00", b"\xff", b"\x00\xff\x00"):
            self.assertEqual(decode(*encode(data)), data)

    def test_all_single_byte_values(self):
        for value in range(256):
            self.assertEqual(decode(*encode(bytes([value]))), bytes([value]))

    def test_same_integer_needs_original_length(self):
        self.assertEqual(encode(b"\x0a")[0], encode(b"\x00\x0a")[0])
        self.assertNotEqual(encode(b"\x0a"), encode(b"\x00\x0a"))

    def test_invalid_inputs(self):
        for value, length in ((-1, 1), (256, 1), (1, 0), (0, -1)):
            with self.assertRaises(ValueError):
                decode(value, length)
        for value, length in ((True, 1), (1, 1.0), ("1", 1)):
            with self.assertRaises(TypeError):
                decode(value, length)
        with self.assertRaises(TypeError):
            encode("secret")


if __name__ == "__main__":
    unittest.main()
