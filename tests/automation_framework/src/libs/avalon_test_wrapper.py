import env
import os
import json
import logging
import re
from src.libs.avalon_libs import AvalonImpl
from src.utilities.submit_request_utility import \
    submit_request_listener, worker_lookup_sdk, \
    worker_retrieve_sdk, workorder_receiptcreate_sdk, \
    workorder_submit_sdk, worker_register_sdk, \
    worker_setstatus_sdk, workorder_receiptretrieve_sdk, \
    worker_update_sdk, workorder_getresult_sdk, workorder_receiptlookup_sdk
from src.utilities.worker_utilities import configure_data
from src.libs.avalon_request import AvalonRequest

TCFHOME = os.environ.get("TCF_HOME", "../../")
logger = logging.getLogger(__name__)
avalon_lib_instance = AvalonImpl()


def build_request_obj(input_json_obj,
                        pre_test_response=None, method_name=""):
    """
    This function is used after the pre_test_env and for the
    actual request method passed in the test JSON file. Depending on the
    test mode and the request method, it will call the corresponding
    configure_data function.

    Output: request obj which is the final JSON object in case of the
    listener mode, for SDK mode it is the parameter required by the SDK
    function of the request method
    action_obj is the object of the request method class.

    For ex:
    worker_lookup SDK function requires worker_type parameter
    worker_retrieve SDK function requires worker_id parameter.
    """
    action_obj = AvalonRequest()
    request_obj = configure_data(action_obj, input_json_obj, pre_test_response)
    return request_obj, action_obj


def submit_request(uri_client, output_obj, output_file, input_file):
    """
    Single function that is called from the test with the relevant
    input parameters. For listener, output_obj is the JSON obj, for
    SDK it is the parameter that is received
    as an output from build_request_obj function.
    """
    request_method = input_file.get("method")
    if env.test_mode == "listener":
        submit_response = submit_request_listener(
            uri_client, output_obj, output_file)
    else:
        work_type = (re.findall('WorkOrder|Worker', request_method))[0]
        work_func = re.split(work_type, request_method)[1]
        calling_function = "{}_{}_sdk".format(work_type, work_func).lower()
        submit_response = eval(calling_function)(output_obj, input_file)
    return submit_response


def pre_test_worker_env(input_file):
    """
    This function sets up the environment required by work order submit, 
    work order get result and receipt API's. and pass that as the output.
    """
    response = None
    request_method = input_file.get("method")

    response = avalon_lib_instance.worker_lookup()
    logger.info("******Received WorkerLookUp Response******\n%s\n", response)

    if request_method not in ["WorkerRetrieve", "WorkerUpdate",
                              "WorkerSetStatus"]:
        response = avalon_lib_instance.worker_retrieve(response)
    return response


def pre_test_workorder_env(input_file, output):
    """
        This function sets up the environment required to run the test for
        submit function or receipt and result function
        For ex: Work Order Submit test requires worker_lookup, retrieve
        the worker details and pass that as the output.
        """
    request_method = input_file["method"]
    wo_submit = avalon_lib_instance.work_order_submit(output)

    if request_method in [
        "WorkOrderReceiptRetrieve",
            "WorkOrderReceiptLookUp"]:
        avalon_lib_instance.work_order_create_receipt(wo_submit)
    return wo_submit
