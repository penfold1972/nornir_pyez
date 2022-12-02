import copy
from typing import Any, Dict, List, Optional
from nornir.core.task import Result, Task
from nornir_pyez.plugins.connections import CONNECTION_NAME
from lxml import etree
import xmltodict
import json


def pyez_chassis_inventory(
    task: Task,
    clei-models: str = False,
    detail: str = False,
    extensive: str = False,
    models: str = False
) -> Result:

    device = task.host.get_connection(CONNECTION_NAME, task.nornir.config)

    cmd_args = {}
    if clei-models is True:
        cmd_args["clei-models"]=clei-models
    if detail is True:
        cmd_args["detail"]=detail
    if extensive is True:
        cmd_args["extensive"]=extensive
    if models is True:
        cmd_args["models"]=models

    data = device.rpc.get_chassis_inventory(**cmd_args)
    data = etree.tostring(data, encoding='unicode', pretty_print=True)
    parsed = xmltodict.parse(data)
    clean_parse = json.loads(json.dumps(parsed))
    return Result(host=task.host, result=clean_parse)
