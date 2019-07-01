# -*- coding: utf-8 -*-
# This is an example of a unit testing module

import unittest
import numpy.testing as npt
from lib import *


class TestLib(unittest.TestCase):

    def setUp(self):

        self.deg_values = [0, 30, 45, 60, 90]
        self.rad_values = [0, 0.5235987756, 0.7853981634, 1.0471975512,
                           1.5707963268]
        self.pos = [217.4292, -62.6794, 269.4500, 4.6933]
        self.dis = 77.94817894340369

    def tearDown(self):

        self.deg_values = None
        self.rad_values = None

    def testDeg2Rad(self):

        for deg, rad in zip(self.deg_values, self.rad_values):

            npt.assert_almost_equal(deg2rad(deg), rad,
                                    err_msg=('Failed conversion from'
                                    ' degrees to radians.'))

    def testRad2Deg(self):

        for deg, rad in zip(self.deg_values, self.rad_values):

            npt.assert_almost_equal(rad2deg(rad), deg,
                                    err_msg=('Failed conversion from'
                                    ' radians to degrees.'))

    def testCheckFloat(self):

        npt.assert_raises(ValueError, check_float, 1)

    def testCheckRA(self):

        npt.assert_raises(ValueError, check_ra, -1.)
        npt.assert_raises(ValueError, check_ra, 361.)

    def testCheckDEC(self):

        npt.assert_raises(ValueError, check_dec, -91.)
        npt.assert_raises(ValueError, check_dec, 91.)

    def testAngDis(self):

        npt.assert_almost_equal(angdis(*self.pos), self.dis,
                                err_msg=('Failed calculation of angular'
                                ' separation.'))


if __name__ == '__main__':
    unittest.main()
