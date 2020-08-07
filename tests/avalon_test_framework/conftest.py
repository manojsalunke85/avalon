import utility.logger as plogger
import env
import toml
import pytest
import json
import os
import sys
import logging
import config.config as pconfig
from http_client.http_jrpc_client import HttpJrpcClient

logger = logging.getLogger(__name__)
sys.path.append(os.getcwd())

# Config File Path
TCFHOME = os.environ.get("TCF_HOME", "../../")
config_path = TCFHOME + '/tests/avalon_test_framework/config.toml'
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
env['tcs_config_conffiles'] = [env['tcs_config_conffiles']]
env['confpaths'] = [env['confpaths']]


@pytest.fixture(scope="session", autouse=True)
def setup_config(args=None):
    """ Fixture to setup initial config for pytest session. """

    # parse out the configuration file first
    try:
        config = pconfig.parse_configuration_files(
            env["tcs_config_conffiles"], env["confpaths"])
        config_json_str = json.dumps(config, indent=4)
    except pconfig.ConfigurationException as e:       
        logger.error(str(e))
        sys.exit(-1)

    plogger.setup_loggers(config.get("Logging", {}))
    sys.stdout = plogger.stream_to_logger((logging.getLogger("STDOUT"),
                                           logging.DEBUG))
    sys.stderr = plogger.stream_to_logger((logging.getLogger("STDERR"),
                                           logging.WARN))

    logger.info("configuration for the session: %s", config)
