# -*- coding: utf-8 -*-

# Copyright (c) 2017-2018, Paul Wolf.
# All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:

# 1. Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.

# 2. Redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution.

# 3. Neither the name of Yewleaf Ltd. nor the names of its contributors
# may be used to endorse or promote products derived from this software
# without specific prior written permission.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# Original author: paul.wolf@yewleaf.com

import re
import time



__version__ = '0.1.0'
__author__ = 'Paul Wolf'
__license__ = 'BSD'


def pc1(pc_str, pc=None):
    """A9 9AA      L2 3SW"""
    if not pc:
        pc = PostCode()
    pc.area = pc_str[0]
    pc.district = pc_str[1]
    pc.sector = pc_str[3]
    pc.unit = pc_str[4:6]
    return pc

def pc2(pc_str, pc=None):
    """A99 9AA     M16 0RA"""
    if not pc:
        pc = PostCode()
    pc.area = pc_str[0]
    pc.district = pc_str[1:3]
    pc.sector = pc_str[4]
    pc.unit = pc_str[5:7]
    return pc

def pc3(pc_str, pc=None):
    """AA9 9AA     NW3 2RR"""
    if not pc:
        pc = PostCode()
    pc.area = pc_str[:2]
    pc.district = pc_str[2]
    pc.sector = pc_str[4]
    pc.unit = pc_str[5:7]
    return pc

def pc4(pc_str, pc=None):
    """AA99 9AA    EH12 9DN"""
    if not pc:
        pc = PostCode()
    pc.area = pc_str[:2]
    pc.district = pc_str[2:4]
    pc.sector = pc_str[5]
    pc.unit = pc_str[6:8]
    return pc

def pc5(pc_str, pc=None):
    """A9A 9AA     W1A 1HQ"""
    if not pc:
        pc = PostCode()
    pc.area = pc_str[0]
    pc.district = pc_str[1:3]
    pc.sector = pc_str[4]
    pc.unit = pc_str[5:7]
    return pc

def pc6(pc_str, pc=None):
    """AA9A 9AA    SW1A 2AA"""
    if not pc:
        pc = PostCode()
    pc.area = pc_str[:2]
    pc.district = pc_str[2:4]
    pc.sector = pc_str[5]
    pc.unit = pc_str[6:8]
    return pc

def pc7(pc_str, pc=None):
    # NPT 9ZB
    if not pc:
        pc = PostCode()
    pc.area = pc_str[:3]
    pc.district = ''
    pc.sector = pc_str[4]
    pc.unit = pc_str[5:7]
    return pc

def pc8(pc_str, pc=None):
    # GIR 0AA
    if not pc:
        pc = PostCode()
    pc.area = pc_str[1]
    pc.district = pc_str[1:3]
    pc.sector = pc_str[4]
    pc.unit = pc_str[5:7]
    return pc

def parse_pc(pc_str, pc=None, raise_error=True):
    """Return a PostCode() object.

    Postcode format specification: 

    https://www.mrs.org.uk/pdf/postcodeformat.pdf

    Pattern     Example
    A9 9AA      L2 3SW
    A99 9AA     M16 0RA
    AA9 9AA     NW3 2RR
    AA99 9AA    EH12 9DN
    A9A 9AA     W1A 1HQ
    AA9A 9AA    SW1A 2AA

    We don't change the input to make it more well-formed.  Input
    should already be upper case and with the space inbetween outward
    and inward parts.

    pc = parse_pc('L2 3SW')
    

    """

    PC1 = '[A-Z][0-9] [0-9][A-Z][A-Z]'
    PC2 = '[A-Z][0-9][0-9] [0-9][A-Z][A-Z]'
    PC3 = '[A-Z][A-Z][0-9] [0-9][A-Z][A-Z]'
    PC4 = '[A-Z][A-Z][0-9][0-9] [0-9][A-Z][A-Z]'
    PC5 = '[A-Z][0-9][A-Z] [0-9][A-Z][A-Z]'
    PC6 = '[A-Z][A-Z][0-9][A-Z] [0-9][A-Z][A-Z]'
    PC7 = 'NPT [0-9][A-Z][A-Z]'
    PC8 = 'GIR 0AA'
    patterns = {PC1: pc1,
                PC2: pc2,
                PC3: pc3,
                PC4: pc4,
                PC5: pc5,
                PC6: pc6,
                PC7: pc7,
                PC8: pc8,
    }
    for p, f in patterns.items():
        m = re.match(p, pc_str)
        if (m):
            return f(pc_str, pc)
    if raise_error:
        raise Exception("cannot match: {}".format(pc_str))

class PostCode(object):
    __slots__ = ('area', 'district', 'sector', 'unit')

    def __init__(self, pc_str=None):
        if pc_str:
            parse_pc(pc_str, pc=self)

    @property
    def farea(self):
        """Return area."""
        return self.area
    
    @property
    def fdistrict(self):
        """Return full district, like 'SW1A'."""
        return self.area+self.district

    @property
    def fsector(self):
        """Return full district, like 'SW1A 2'."""
        return "{}{} {}".format(self.area, self.district, self.sector)

    @property
    def funit(self):
        """Same as input string."""
        return "{}{} {}{}".format(self.area, self.district, self.sector, self.unit)

    @property
    def outward(self):
        return self.area + self.district

    @property
    def inward(self):
        return self.sector + self.unit

    def __str__(self):
        return "area={}, district={}, sector={}, unit={}".format(self.area,
                                                                 self.district,
                                                                 self.sector,
                                                                 self.unit)
