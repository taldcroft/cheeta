#!/usr/bin/env python

import sys
import os
import optparse
import cPickle as pickle

def get_options():
    parser = optparse.OptionParser()
    parser.add_option("--root",
                      default='regr_vals',
                      help="Input prefix")
    return parser.parse_args()

opt, args = get_options()

flight = pickle.load(open(opt.root + '.flight'))
test = pickle.load(open(opt.root + '.test'))

msids = ('1crat', 'fptemp_11', 'orbitephem0_x', 'sim_z', 'tephin')
attrs = ('times', 'vals', 'quals', 'stds', 'mins', 'maxes', 'means',
         'p01s', 'p05s', 'p16s', 'p50s', 'p84s', 'p95s', 'p99s')

for msid in msids:
    for stat in ('dat', 'dat5', 'datd'):
        for attr in attrs:
            f = flight[msid][stat]
            t = test[msid][stat]
            if not hasattr(f, attr):
                continue
            print 'Checking', msid, stat, attr,
            if attr == 'quals':
                ok = f.quals == t.quals
            else:
                ok = np.max(np.abs(getattr(f, attr) - getattr(t, attr))) < 1e-6
            print ('OK' if ok else 'NOT OK')
                     
