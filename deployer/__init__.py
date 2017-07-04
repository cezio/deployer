#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
from subprocess import Popen

from flask import Flask, Response, request

app = Flask('deployer')



@app.route('/incoming/', methods=["POST"])
def incoming():
    r = request
    config_path = os.environ.get('DEPLOYER_CONFIG')
    if not config_path:
        return Response(response='no deployment config', status=500)
    response = 'ok'
    code = 200
    with open(config_path, 'rt') as f:
        config = json.load(f)

        command = config['command']
        env = config['environment']
        nenv = os.environment.copy()
        nenv.update(env)
        p = Popen(command, shell=True, env=nenv)
        ret = p.wait()
        if ret:
            code=500
            response='error during execution: {}'.format(ret)

    r = Response(response=response, status=code)
    return r


if __name__ == '__main__':
    app.run()
