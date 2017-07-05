#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys
import subprocess

from flask import Flask, Response, request

app = Flask('deployer')

@app.route('/incoming/<deployment_name>/', methods=["POST"])
def incoming(deployment_name):
    r = request
    config_path = os.environ.get('DEPLOYER_CONFIG')
    if not config_path:
        return Response(response='no deployment config path', status=500)
    final_path = os.path.join(config_path, '{}.conf'.format(deployment_name))
    if not os.path.exists(final_path):
        return Response(response='no deployment config', status=404)
    command = '({} -m deployer.runner {}) & '.format(sys.executable, final_path)
    subprocess.call(command, shell=True)
    response = 'ok'
    status = 200
    r = Response(response=response, status=status)
    return r


if __name__ == '__main__':
    app.run()
