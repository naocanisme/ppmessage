# -*- coding: utf-8 -*-
#
# Copyright (C) 2010-2016 PPMessage.
# Guijin Ding, dingguijin@gmail.com.
# All rights are reserved.
#
# ppkefu/min/config.py
#

import os
import json
import scss
import logging
import hashlib

def _cur_dir():
    return os.path.dirname(__file__)

def _replace(_d):
    _api_uuid = _d.get("api_uuid")
    _app_uuid = _d.get("app_uuid")
    _api_key = _d.get("api_key")
    _api_secret = _d.get("api_secret")
    
    TEMPLATE_MIN_JS = "../../resource/assets/ppconsole/static/dist/ppconsole-template.min.js"
    MIN_JS = "../../resource/assets/ppconsole/static/dist/ppconsole.min.js"
    
    _js_path = os.path.join(_cur_dir(), TEMPLATE_MIN_JS)
    _js_n_path = os.path.join(_cur_dir(), MIN_JS)

    if not os.path.exists(_js_path):
        logging.error("no such file: %s" % _js_path)
        return

    with open(_js_path, "r") as _f:
        _js_str = _f.read()
        _js_str = _js_str.replace('{ppconsole_api_uuid}', _api_uuid)\
                         .replace('{ppconsole_api_key}', _api_key)\
                         .replace('{ppconsole_api_secret}', _api_secret)\
                         .replace('{ppmessage_app_uuid}', _app_uuid)
                
        with open(_js_n_path, "w") as _of:
            _of.write(_js_str)

    return

def config(_d):
    _replace(_d)
    return

if __name__ == "__main__":
    import sys
    reload(sys)
    sys.setdefaultencoding('utf-8')
    _d = {
        "app_uuid": "NGY3YjM2MGM1ZDExNTRlOGRiNDcxNjhjNjA2Y2ExMDE1YmNiOTVkNA==",
        "api_uuid": "NGY3YjM2MGM1ZDExNTRlOGRiNDcxNjhjNjA2Y2ExMDE1YmNiOTVkNA==",
        "api_key": "NGY3YjM2MGM1ZDExNTRlOGRiNDcxNjhjNjA2Y2ExMDE1YmNiOTVkNA==",
        "api_secret": "NGY3YjM2MGM1ZDExNTRlOGRiNDcxNjhjNjA2Y2ExMDE1YmNiOTVkNA=="
    }
    config(_d)

        
