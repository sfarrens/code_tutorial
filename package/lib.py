# -*- coding: utf-8 -*-
# This is an example of a library module

import math


def rad2deg(rad_value):

    return (180. / math.pi) * rad_value


def deg2rad(deg_value):

    return (math.pi / 180.) * deg_value


def check_float(value):

    if not isinstance(value, float):
        raise ValueError('Input must be of type float.')


def check_ra(ra_val):

    check_float(ra_val)

    if ra_val < 0. or ra_val > 360.:
        raise ValueError('{} is not a valid value for RA'.format(ra_val))


def check_dec(dec_val):

    check_float(dec_val)

    if dec_val < -90. or dec_val > 90.:
        raise ValueError('{} is not a valid value for Dec'.format(dec_val))


def angdis(ra1, dec1, ra2, dec2):

    [check_ra(ra_val) for ra_val in (ra1, ra2)]
    [check_dec(dec_val) for dec_val in (dec1, dec2)]

    ra1 = deg2rad(ra1)
    dec1 = deg2rad(dec1)
    ra2 = deg2rad(ra2)
    dec2 = deg2rad(dec2)

    return rad2deg(math.acos(math.sin(dec1) * math.sin(dec2) + math.cos(dec1) *
                   math.cos(dec2) * math.cos(ra1 - ra2)))
