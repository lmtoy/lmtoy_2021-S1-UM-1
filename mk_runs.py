#! /usr/bin/env python
#
#   script generator for project="2021-S1-UM-1"
#
#

import os
import sys
from lmtoy import runs

project="2021-S1-UM-1"

#        obsnums per source (make it negative if not added to the final combination)
on = {}
on['BKP7323_CO'] = [101704, 101705, 101711, 101712]

#        common parameters per source on the first dryrun (run1, run2)
pars1 = {}
pars1['BKP7323_CO'] = ""

#        common parameters per source on subsequent runs (run1a, run2a)
pars2 = {}
pars2['BKP7323_CO'] = "admit=0 srdp=1"


if __name__ == '__main__':    
    runs.mk_runs(project, on, pars1, pars2, sys.argv)
