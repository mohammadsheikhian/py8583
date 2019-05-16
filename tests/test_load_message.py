import unittest

from py8583 import *


class DumpISOMessageTest(unittest.TestCase):

    def test_dump_iso_message(self):
        expected_iso_message = '0210f0000000000000000000000002000000' \
            '10123456789040000012345612345603abc'

        iso_packet = py8583.Iso8583(IsoSpec=py8583spec.IsoSpec1987ASCII())
        iso_packet.MTI('0210')

        iso_packet.Field(2, 1)
        iso_packet.FieldData(2, 1234567890)

        iso_packet.Field(3, 1)
        iso_packet.FieldData(3, 400000)

        iso_packet.Field(4, 1)
        iso_packet.FieldData(4, 123456123456)

        iso_packet.Field(103, 1)
        iso_packet.FieldData(103, 'abc')

        self.assertEqual(iso_packet.BuildIso().decode(), expected_iso_message)


if __name__ == '__main__':
    unittest.main()

