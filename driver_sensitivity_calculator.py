#!/usr/bin/env python
from __future__ import print_function
import sys
from scipy.stats import binom

if __name__ == "__main__":

    dep = float(sys.argv[1])
    purity = float(sys.argv[2])
    print (1 - binom.cdf(3, dep, 0.5 * purity))


