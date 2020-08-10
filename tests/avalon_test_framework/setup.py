import os
import toml
import pytest
from http_client.http_jrpc_client import HttpJrpcClient

"""
Read the config file for setting up the automation environment.
"""
TCFHOME = os.environ.get("TCF_HOME", "../../")
config_path = TCFHOME + '/tests/avalon_test_framework/config/config.toml'
with open(config_path) as fd:
    env = toml.load(fd)

# For worker_register, worker_setstatus and worker_update API's
# avalon currently doesn't allow access when running in direct mode
# but allows access when running in Proxy mode. Hence the expected
# error codes are different for proxy mode vs. direct mode.
if env['proxy_mode']:
    env['expected_error_code'] = 0
else:
    env['expected_error_code'] = -32601

env['uri_client'] = HttpJrpcClient("http://avalon-listener:1947")
