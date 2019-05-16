import unittest

from py8583 import *


class ParserISOMessageTest(unittest.TestCase):

    def test_parser_iso_message(self):
        data = '0200f0000000000000000000000000000000' \
            '101234567890400000123456123456'

        iso_packet = py8583.Iso8583(
            data.encode(),
            IsoSpec=py8583spec.IsoSpec1987ASCII()
        )

        self.assertEqual(iso_packet.FieldData(2), 1234567890)
        self.assertEqual(iso_packet.FieldData(3), 400000)
        self.assertEqual(iso_packet.FieldData(4), 123456123456)


if __name__ == '__main__':
    unittest.main()

