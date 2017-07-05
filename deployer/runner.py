#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from six.moves.configparser import SafeConfigParser as ConfigParser
import filelock
from subprocess import Popen
import daemon

def main(config_path):
    flock = filelock.FileLock('{}.lock'.format(config_path))
    flock.timeout = 3*60
    with flock:
        with open(config_path, 'rt') as f:
            config = ConfigParser()
            config.readfp(f)

        command = config.get('deployment', 'command')
        logto = config.get('deployment', 'log')
        if logto:
            log = open(os.path.expanduser(logto), 'w')
            sys._stdout = sys.stdout
            sys._stderr = sys.stderr

            sys.stdout = log
            sys.stderr = log

            command = '({}) 2>&1 >> {}'.format(command, logto)

        print('parsing {}'.format(config_path))
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


def run_child(config_path):
    pid = os.fork()
    # parent, bye
    if pid != 0:
        print('created', pid)
        return
    print('running for', config_path)
    for fd in range(0, 3):
        try:
            os.close(fd)
        except:
            pass
    os.open("/dev/null", os.O_RDONLY)
    os.open("/dev/null", os.O_WRONLY)
    os.open("/dev/null", os.O_WRONLY)
    main(config_path)    

if __name__ == '__main__':
    config_path = sys.argv[-1]
    sys.exit(main(config_path))
