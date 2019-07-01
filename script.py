#! /usr/bin/env python
# -*- coding: utf-8 -*-
# This is an example of a script

from package.lib import angdis


def main():
    proxima_centauri = (217.4292, -62.6794)
    barnards_star = (269.4500, 4.6933)

    res = angdis(*proxima_centauri, *barnards_star)

    print("The angular separation between Proxima Centauri and Barnard's star "
          "is {:.3} degrees.".format(res))


if __name__ == "__main__":
    main()
