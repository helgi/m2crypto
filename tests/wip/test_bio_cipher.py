#!/usr/bin/env python

"""Unit tests for M2Crypto.BIO.CipherStream.

Copyright (c) 1999-2001 Ng Pheng Siong. All rights reserved."""

RCS_id='$Id: test_bio_cipher.py,v 1.1 2002/12/23 06:14:02 ngps Exp $'

import unittest
import M2Crypto
from M2Crypto.BIO import CipherStream

class CipherStreamTestCase(unittest.TestCase):

    data = 'abcdef' * 64

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def check_init_empty(self):
        pass


def suite():
    return unittest.makeSuite(CipherStreamTestCase, 'check_')
    

if __name__ == '__main__':
    unittest.TextTestRunner().run(suite())

