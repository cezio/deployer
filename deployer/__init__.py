#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json

from flask import Flask, Response, request

app = Flask('deployer')



@app.route('/incoming/')
def incoming():
    r = request
    config_path = os.environ.get('DEPLOYER_CONFIG')
    if not config_path:
        return Response(response='no deployment config', status_code=500)
    response = 'ok'
    code = 200
    with open(confi_path, 'rt') as f:
        config = json.load(f)

        command = config['command']
        env = config['env']

        p = Popen(command, shell=True, env=env)
        ret = p.wait()
        if ret:
            code=500
            response='error during execution: {}'.format(ret)

    r = Response(response=response, status_code=code)
    return resp
