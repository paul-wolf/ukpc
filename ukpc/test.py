# -*- coding: utf-8 -*-

import unittest
from __init__ import parse_pc


class TestUKPCParsing(unittest.TestCase):

    def test_parsing(self):

        pc1 = 'L2 3SW'
        pc2 = 'M16 0RA'
        pc3 = 'NW3 2RR'
        pc4 = 'EH12 9DN'
        pc5 = 'W1A 1HQ'
        pc6 = 'SW1A 2AA'
        pc7 = 'NPT 9ZB'

        pc = parse_pc(pc1)
        self.assertTrue(pc.area == 'L')
        self.assertTrue(pc.district == '2')
        self.assertTrue(pc.sector == '3')
        self.assertTrue(pc.unit == 'SW')

        pc = parse_pc(pc2)
        self.assertTrue(pc.area == 'M')
        self.assertTrue(pc.district == '16')
        self.assertTrue(pc.sector == '0')
        self.assertTrue(pc.unit == 'RA')

        pc = parse_pc(pc3)
        self.assertTrue(pc.area == 'NW')
        self.assertTrue(pc.district == '3')
        self.assertTrue(pc.sector == '2')
        self.assertTrue(pc.unit == 'RR')

        pc = parse_pc(pc4)
        self.assertTrue(pc.area == 'EH')
        self.assertTrue(pc.district == '12')
        self.assertTrue(pc.sector == '9')
        self.assertTrue(pc.unit == 'DN')

        pc = parse_pc(pc5)
        self.assertTrue(pc.area == 'W')
        self.assertTrue(pc.district == '1A')
        self.assertTrue(pc.sector == '1')
        self.assertTrue(pc.unit == 'HQ')

        pc = parse_pc(pc6)
        self.assertTrue(pc.area == 'SW')
        self.assertTrue(pc.district == '1A')
        self.assertTrue(pc.sector == '2')
        self.assertTrue(pc.unit == 'AA')

        pc = parse_pc(pc7)
        self.assertTrue(pc.area == 'NPT')
        self.assertTrue(pc.district == '')
        self.assertTrue(pc.sector == '9')
        self.assertTrue(pc.unit == 'ZB')

        
if __name__ == '__main__':
    unittest.main()
