import sys

from ciphey.basemods.Checkers.brandon import Brandon
from ciphey.Decryptor.Encoding.encodingParent import EncodingParent
from ciphey.__main__ import make_default_config
import unittest
from loguru import logger

config = make_default_config("")


class TestEncoding(unittest.TestCase):
    def test_english_yes(self):
        lc = Brandon(config)
        ep = EncodingParent(lc)
        result = ep.decrypt("eW91ciB0ZXh0")
        self.assertEqual(result["IsPlaintext?"], True)

    def test_base64_spaces_yes(self):
        lc = Brandon(config)
        ep = EncodingParent(lc)
        result = ep.decrypt("SGVsbG8gSSBsaWtlIGRvZ3MgYW5kIGNhdHM=")
        self.assertEqual(result["IsPlaintext?"], True)

    def test_binary_spaces_yes(self):
        lc = Brandon(config)
        ep = EncodingParent(lc)
        result = ep.decrypt(
            "01001000 01100101 01101100 01101100 01101111 00100000 01001001 00100000 01101100 01101001 01101011 01100101 00100000 01100100 01101111 01100111 01110011 00100000 01100001 01101110 01100100 00100000 01100011 01100001 01110100 01110011"
        )
        self.assertEqual(result["IsPlaintext?"], True)

    def test_hex_spaces_yes(self):
        lc = Brandon(config)
        ep = EncodingParent(lc)
        result = ep.decrypt(
            "68 65 6c 6c 6f 20 6f 6c 69 76 69 61 20 69 20 72 65 61 6c 6c 79 20 6c 69 6b 65 20 79 6f 75 72 20 64 6f 67"
        )
        self.assertEqual(result["IsPlaintext?"], True)

    def test_hex_mixed_spaces_yes(self):
        lc = Brandon(config)
        ep = EncodingParent(lc)
        a = "68656c6c6f206f 6c 69 76 69 61 20 69 20 72 65 61 6c 6c 79 20 6c 69 6b 65 20 79 6f 75 72 20 64 6f 67"
        a = a.replace(" ", "")
        result = ep.decrypt(a)
        self.assertEqual(result["IsPlaintext?"], True)

    def test_ascii(self):
        lc = Brandon(config)
        ep = EncodingParent(lc)
        a = "68 65 6C 6C 6F 20 64 6F 67"
        result = ep.decrypt(a)
        self.assertEqual(result["IsPlaintext?"], True)

    def test_morse(self):
        lc = Brandon(config)
        ep = EncodingParent(lc)
        a = ".... . .-.. .-.. --- / -- -.-- / -. .- -- . / .. ... / -... .-. .- -. -.. --- -."
        result = ep.decrypt(a)
        self.assertEqual(result["IsPlaintext?"], True)

    def test_morse(self):
        lc = Brandon(config)
        ep = EncodingParent(lc)
        logger.remove()
        logger.configure()
        logger.add(sink=sys.stderr, level="TRACE", colorize=True)
        logger.opt(colors=True)
        logger.error(f"""Debug level set to {config["debug"]}""")
        a = "| .... . .-.. .-.. ---/../.- --/.-/-.-. .... .. .-.. -../..-. .-. --- --/--- ..- -/... .--. .- -.-. ./.- -. -../../.-.. .. -.- ./-.-. -.-- -... . .-./.- -. -../-.-. .- -"
        result = ep.decrypt(a)
        logger.debug(result)
        logger.debug(result)
        self.assertEqual(result["IsPlaintext?"], True)

    def test_base32(self):

        # logger.configure()
        # logger.add(sink=sys.stderr, level="TRACE", colorize=True)
        # logger.opt(colors=True)
        # logger.error(f"""Debug level set to {config["debug"]}""")

        lc = Brandon(config)
        ep = EncodingParent(lc)
        a = "NBSWY3DPEBWXSIDOMFWWKIDJOMQGEZLF"
        result = ep.decrypt(a)
        self.assertEqual(result["IsPlaintext?"], True)
