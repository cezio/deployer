#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from six.moves.configparser import SafeConfigParser as ConfigParser
import filelock
from subprocess import Popen

def main(config_path):
    flock = filelock.FileLock('{}.lock'.format(config_path))
    flock.timeout = 3*60
    with flock:
        print('parsing {}'.format(config_path))
        with open(config_path, 'rt') as f:
            config = ConfigParser()
            config.readfp(f)

        command = config.get('deployment', 'command')
        logto = config.get('deployment', 'log')
        if logto:
            command = '({}) 2>&1 >> {}'.format(command, logto)
        env = {}
        if config.has_section('environment'):
            for k, v in config.items('environment'):
                env[k] = v
        nenv = os.environ.copy()
        nenv.update(env)
        print('running command', command)
        p = Popen(command, shell=True, env=nenv)
        ret = p.wait()

        return ret


if __name__ == '__main__':
    config_path = sys.argv[-1]
    sys.exit(main(config_path))
