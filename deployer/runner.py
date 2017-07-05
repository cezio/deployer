#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from configparser import SafeConfigParser as ConfigParser
import filelock
from subprocess import Popen

def main():
    config_path = sys.argv[-1]
    flock = filelock.FileLock('{}.lock'.format(config_path))
    flock.timeout = 3*60
    with flock:
        print('parsing {}'.format(config_path))
        with open(config_path, 'rt') as f:
            config = ConfigParser()
            config.readfp(f)

        if config is None:
            print('no deployment config in {}'.format(config_path))
            return 1
        
        command = config.get('deployment', 'command')
        
        env = {}
        if config.has_section('environment'):
            for k, v in config.items('environment'):
                env[k] = v
        nenv = os.environ.copy()
        nenv.update(env)

        p = Popen(command, shell=True, env=nenv)
        ret = p.wait()

        return ret


if __name__ == '__main__':
    sys.exit(main())
