# Copyright 2019 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pytest
import logging
import os
import globals
from src.libs.avalon_test_wrapper \
    import read_json, submit_request
from src.libs.test_base import TestBase
from src.utilities.verification_utils \
    import verify_test, check_negative_test_responses
from src.utilities.generic_utils import TestStep
logger = logging.getLogger(__name__)


class TestClass():
    test_obj = TestBase()

    @pytest.mark.workordersubmit
    @pytest.mark.test_workordersubmit_success
    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.p1
    def test_workordersubmit_success(self):
        test_id = '18697'
        request_file = os.path.join(
            globals.work_order_input_file,
            "work_order_success.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.wo_submit_output_json_file_name,
            read_json(request_file))

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'])

        assert (
            verify_test(
                result_response, 0,
                self.test_obj.build_request_output['pre_test_output'],
                self.test_obj.build_request_output['action_obj'])
            is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.test_workordersubmit_inDataDataEncryptionKey_hyphenecho
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_workordersubmit_inDataDataEncryptionKey_hyphenecho(self):
        test_id = '18783'
        request_file = os.path.join(
            globals.work_order_input_file,
            "work_order_inData_DataEncryptionKey_hyphen_echo.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.wo_submit_output_json_file_name,
            read_json(request_file))

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'])

        assert (
                verify_test(
                    result_response, 0,
                    self.test_obj.build_request_output['pre_test_output'],
                    self.test_obj.build_request_output['action_obj'])
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.test_workordersubmit_datahash_null
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_workordersubmit_datahash_null(self):
        test_id = '18713'
        request_file = os.path.join(
            globals.work_order_input_file,
            "work_order_data_datahash_null.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.wo_submit_output_json_file_name,
            read_json(request_file))

        assert (
                check_negative_test_responses(
                    submit_response,
                    "Invalid data format for data hash of in data")
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.test_workordersubmit_requesterId_null
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_workordersubmit_requesterId_null(self):
        test_id = '18739'
        request_file = os.path.join(
            globals.work_order_input_file,
            "work_order_requester_id_null.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.wo_submit_output_json_file_name,
            read_json(request_file))

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'])

        assert (
                verify_test(
                    result_response, 0,
                    self.test_obj.build_request_output['pre_test_output'],
                    self.test_obj.build_request_output['action_obj'])
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.test_workordersubmit_sessionkeyivInDataIv_hexstring
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_workordersubmit_sessionkeyivInDataIv_hexstring(
            self):
        test_id = '18738'
        request_file = os.path.join(
            globals.work_order_input_file,
            "work_order_iv_indata_hex_string.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.wo_submit_output_json_file_name,
            read_json(request_file))

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'])

        assert (
                verify_test(
                    result_response, 0,
                    self.test_obj.build_request_output['pre_test_output'],
                    self.test_obj.build_request_output['action_obj'])
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.test_workordersubmit_verifysignature
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_workordersubmit_verifysignature(self):
        test_id = '18450'
        request_file = os.path.join(
            globals.work_order_input_file,
            "work_order_verify_signature.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.wo_submit_output_json_file_name,
            read_json(request_file))

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'])

        assert (
                verify_test(
                    result_response, 0,
                    self.test_obj.build_request_output['pre_test_output'],
                    self.test_obj.build_request_output['action_obj'])
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.test_workordersubmit_requesternonce_specialcharacters
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_workordersubmit_requesternonce_specialcharacters(
            self):
        test_id = '18736'
        request_file = os.path.join(
            globals.work_order_input_file,
            "work_order_submit_requesterNonce_all_special_characters.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.wo_submit_output_json_file_name,
            read_json(request_file))

        assert (
                check_negative_test_responses(
                    submit_response,
                    "Invalid data format for requesterNonce")
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.test_workordersubmit_signingalgorithm_alternate
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_workordersubmit_signingalgorithm_alternate(self):
        test_id = '18614'
        request_file = os.path.join(
            globals.work_order_input_file,
            "work_order_with_alternate_worker_signing_algorithm.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.wo_submit_output_json_file_name,
            read_json(request_file))

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'])

        assert (
                verify_test(
                    result_response, 0,
                    self.test_obj.build_request_output['pre_test_output'],
                    self.test_obj.build_request_output['action_obj'])
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.test_workordersubmit_hashingalgorithm_alternate
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_workordersubmit_hashingalgorithm_alternate(self):
        test_id = '18704'
        request_file = os.path.join(
            globals.work_order_input_file,
            "work_order_with_alternate_hashing_algorithm.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.wo_submit_output_json_file_name,
            read_json(request_file))

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'])

        assert (
                verify_test(
                    result_response, 0,
                    self.test_obj.build_request_output['pre_test_output'],
                    self.test_obj.build_request_output['action_obj'])
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.test_workordersubmit_requesterprivatekey_no
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_workordersubmit_requesterprivatekey_no(self):
        test_id = '18612'
        request_file = os.path.join(
            globals.work_order_input_file,
            "work_order_without_requester_private_key.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.wo_submit_output_json_file_name,
            read_json(request_file))

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'])

        assert (
                verify_test(
                    result_response, 0,
                    self.test_obj.build_request_output['pre_test_output'],
                    self.test_obj.build_request_output['action_obj'])
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.test_workordersubmit_params_twiceheartdisease
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_workordersubmit_params_twiceheartdisease(self):
        test_id = '18811'
        request_file = os.path.join(
            globals.work_order_input_file,
            "work_order_submit_twice_params.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.wo_submit_output_json_file_name,
            read_json(request_file))

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'])

        assert (
                verify_test(
                    result_response, 0,
                    self.test_obj.build_request_output['pre_test_output'],
                    self.test_obj.build_request_output['action_obj'])
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.test_workordersubmit_workloadid_invalid
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_workordersubmit_workloadid_invalid(self):
        test_id = '18807'
        request_file = os.path.join(
            globals.work_order_input_file,
            "work_order_Submit_invalid_parameter_Workloadid.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.wo_submit_output_json_file_name,
            read_json(request_file))

        assert (
                check_negative_test_responses(
                    submit_response,
                    "Invalid workload id")
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.test_workordersubmit_methodname_list
    @pytest.mark.listener
    def test_workordersubmit_methodname_list(self):
        test_id = '18797'
        request_file = os.path.join(
            globals.work_order_input_file,
            "work_order_methodename_list.json")

        # err_cd = \
        #    self.test_obj.setup_and_build_request_wo_submit(
        #        read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            read_json(request_file),
            globals.wo_submit_output_json_file_name,
            read_json(request_file))

        # result_response = self.test_obj.getresult(
        #     self.test_obj.build_request_output['request_obj'])

        assert (
                check_negative_test_responses(
                    submit_response,
                    "Invalid Request")
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.test_workordersubmit_workerencryptionkey_specialcharacter
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_workordersubmit_workerencryptionkey_specialcharacter(self):
        test_id = '18732'
        request_file = os.path.join(
            globals.work_order_input_file,
            "work_order_workerEncryptionKey_special_character.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.wo_submit_output_json_file_name,
            read_json(request_file))

        assert (
                check_negative_test_responses(
                    submit_response,
                    "Invalid data format for worker encryption key")
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')


    @pytest.mark.workordersubmit
    @pytest.mark.test_workordersubmit_workerencryptionkey_empty
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_workordersubmit_workerencryptionkey_empty(self):
        test_id = '18705'
        request_file = os.path.join(
            globals.work_order_input_file,
            "work_order_worker_encryption_key.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.wo_submit_output_json_file_name,
            read_json(request_file))

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'])

        assert (
                verify_test(
                    result_response, 0,
                    self.test_obj.build_request_output['pre_test_output'],
                    self.test_obj.build_request_output['action_obj'])
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')


    @pytest.mark.workordersubmit
    @pytest.mark.test_workordersubmit_dataencryptionalgorithm_alternate
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_workordersubmit_dataencryptionalgorithm_alternate(self):
        test_id = '18706'
        request_file = os.path.join(
            globals.work_order_input_file,
            "work_order_with_alternate_dataEncryption_algorithm.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.wo_submit_output_json_file_name,
            read_json(request_file))

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'])

        assert (
                check_negative_test_responses(
                    result_response,
                    "Unsupported dataEncryptionAlgorithm found in the request")
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')


    @pytest.mark.workordersubmit
    @pytest.mark.test_workordersubmit_indexindata_50
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_workordersubmit_indexindata_50(self):
        test_id = '18707'
        request_file = os.path.join(
            globals.work_order_input_file,
            "work_order_with_50_index_indata.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.wo_submit_output_json_file_name,
            read_json(request_file))

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'])

        assert (
                verify_test(
                    result_response, 0,
                    self.test_obj.build_request_output['pre_test_output'],
                    self.test_obj.build_request_output['action_obj'])
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')


    @pytest.mark.workordersubmit
    @pytest.mark.test_workordersubmit_index_orderchange
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_workordersubmit_index_orderchange(self):
        test_id = '18708'
        request_file = os.path.join(
            globals.work_order_input_file,
            "work_order_with_changing_order_index.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.wo_submit_output_json_file_name,
            read_json(request_file))

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'])

        assert (
                verify_test(
                    result_response, 0,
                    self.test_obj.build_request_output['pre_test_output'],
                    self.test_obj.build_request_output['action_obj'])
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.test_workordersubmit_indata_empty
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_workordersubmit_indata_empty(self):
        test_id = '18765'
        request_file = os.path.join(
            globals.work_order_input_file,
            "work_order_with_empty_indata.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.wo_submit_output_json_file_name,
            read_json(request_file))

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'])

        assert (
                check_negative_test_responses(
                    result_response,
                    "Indata is empty")
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')


    @pytest.mark.workordersubmit
    @pytest.mark.test_workordersubmit_indata_remove
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_workordersubmit_indata_remove(self):
        test_id = '18766'
        request_file = os.path.join(
            globals.work_order_input_file,
            "work_order_with_no_indata.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.wo_submit_output_json_file_name,
            read_json(request_file))

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'])

        assert (
                check_negative_test_responses(
                    submit_response,
                    "Missing parameter inData")
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')


    @pytest.mark.workordersubmit
    @pytest.mark.test_workordersubmit_indataoutdata_empty
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_workordersubmit_indataoutdata_empty(self):
        test_id = '18711'
        request_file = os.path.join(
            globals.work_order_input_file,
            "work_order_with_empty_indata_outdata.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.wo_submit_output_json_file_name,
            read_json(request_file))

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'])

        assert (
                check_negative_test_responses(
                    result_response,
                    "Indata is empty")
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')



    @pytest.mark.workordersubmit
    @pytest.mark.test_workordersubmit_indata_unknownparametervalue
    @pytest.mark.listener
    # @pytest.mark.sdk (AttributeError: 'dict' object has no attribute 'to_jrpc_string)
    def test_workordersubmit_indata_unknownparametervalue(self):
        test_id = '18768'
        request_file = os.path.join(
            globals.work_order_input_file,
            "work_order_with_indata_unknown_parameter_value.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.wo_submit_output_json_file_name,
            read_json(request_file))

        assert (
                check_negative_test_responses(
                    submit_response,
                    "Invalid data format for in/out data")
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')


    @pytest.mark.workordersubmit
    @pytest.mark.test_workordersubmit_index_negative
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_workordersubmit_index_negative(self):
        test_id = '18769'
        request_file = os.path.join(
            globals.work_order_input_file,
            "work_order_negative_index.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.wo_submit_output_json_file_name,
            read_json(request_file))

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'])

        assert (
                verify_test(
                    result_response, 0,
                    self.test_obj.build_request_output['pre_test_output'],
                    self.test_obj.build_request_output['action_obj'])
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')


    @pytest.mark.workordersubmit
    @pytest.mark.test_workordersubmit_indatahash_empty
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_workordersubmit_indatahash_empty(self):
        test_id = '18712'
        request_file = os.path.join(
            globals.work_order_input_file,
            "work_order_with_empty_indata_hash.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.wo_submit_output_json_file_name,
            read_json(request_file))

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'])

        assert (
                verify_test(
                    result_response, 0,
                    self.test_obj.build_request_output['pre_test_output'],
                    self.test_obj.build_request_output['action_obj'])
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.test_workordersubmit_datahash_randomstr
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_workordersubmit_datahash_randomstr(self):
        test_id = '18772'
        request_file = os.path.join(
            globals.work_order_input_file,
            "work_order_datahash_random_str.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.wo_submit_output_json_file_name,
            read_json(request_file))

        assert (
                check_negative_test_responses(
                    submit_response,
                    "Invalid data format for data hash of in data")
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')


    @pytest.mark.workordersubmit
    @pytest.mark.test_workordersubmit_data_multipleechoresult
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_workordersubmit_data_multipleechoresult(self):
        test_id = '18774'
        request_file = os.path.join(
            globals.work_order_input_file,
            "work_order_multiple_data_echoresult.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.wo_submit_output_json_file_name,
            read_json(request_file))

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'])

        assert (
                verify_test(
                    result_response, 0,
                    self.test_obj.build_request_output['pre_test_output'],
                    self.test_obj.build_request_output['action_obj'])
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')


    @pytest.mark.workordersubmit
    @pytest.mark.test_workordersubmit_echoclient
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_workordersubmit_echoclient(self):
        test_id = '18808'
        request_file = os.path.join(
            globals.work_order_input_file,
            "work_order_echoclient.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.wo_submit_output_json_file_name,
            read_json(request_file))

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'])

        assert (
                verify_test(
                    result_response, 0,
                    self.test_obj.build_request_output['pre_test_output'],
                    self.test_obj.build_request_output['action_obj'])
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.test_workordersubmit_indata_alternatetextechoclient
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_workordersubmit_indata_alternatetextechoclient(self):
        test_id = '18809'
        request_file = os.path.join(
            globals.work_order_input_file,
            "work_order_diff_text_data_indata_echoClient.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.wo_submit_output_json_file_name,
            read_json(request_file))

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'])

        assert (
                verify_test(
                    result_response, 0,
                    self.test_obj.build_request_output['pre_test_output'],
                    self.test_obj.build_request_output['action_obj'])
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')


    @pytest.mark.workordersubmit
    @pytest.mark.test_workordersubmit_indata_specialcharacter
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_workordersubmit_indata_specialcharacter(self):
        test_id = '18810'
        request_file = os.path.join(
            globals.work_order_input_file,
            "work_order_specialcharacter_data_single_index_indata.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.wo_submit_output_json_file_name,
            read_json(request_file))

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'])

        assert (
                verify_test(
                    result_response, 0,
                    self.test_obj.build_request_output['pre_test_output'],
                    self.test_obj.build_request_output['action_obj'])
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')


    @pytest.mark.workordersubmit
    @pytest.mark.test_workordersubmit_iv_specialcharacterechoclient
    @pytest.mark.listener
    # @pytest.mark.sdk
    def test_workordersubmit_iv_specialcharacterechoclient(self):
        test_id = '18786'
        request_file = os.path.join(
            globals.work_order_input_file,
            "work_order_special_char_iv_echoresult.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.wo_submit_output_json_file_name,
            read_json(request_file))

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'])

        assert (
                check_negative_test_responses(
                    submit_response,
                    "Invalid data format for initialization vector of in data")
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')


    @pytest.mark.workordersubmit
    @pytest.mark.test_workordersubmit_requesterId_paramremove
    @pytest.mark.listener
    def test_workordersubmit_requesterId_paramremove(self):
        test_id = '18733'
        request_file = os.path.join(
            globals.work_order_input_file,
            "work_order_submit_requesterId_param_remove.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.wo_submit_output_json_file_name,
            read_json(request_file))

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'])

        assert (
                check_negative_test_responses(
                    submit_response,
                    "Missing parameter requesterId")
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')


    @pytest.mark.workordersubmit
    @pytest.mark.test_workordersubmit_responsetimeout_string
    @pytest.mark.listener
    def test_workordersubmit_responsetimeout_string(self):
        test_id = '18798'
        request_file = os.path.join(
            globals.work_order_input_file,
            "work_order_with_response_timeout_str.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.wo_submit_output_json_file_name,
            read_json(request_file))

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'])

        assert (
                check_negative_test_responses(
                    submit_response,
                    "Invalid data format for responseTimeoutMSecs")
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.test_workordersubmit_dataencryptionalgorithm_list
    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.set1
    def test_workordersubmit_dataencryptionalgorithm_list(self):
        test_id = '18793'
        request_file = os.path.join(
            globals.work_order_input_file,
            "work_order_multiple_dataEncryptionAlgorithm.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.wo_submit_output_json_file_name,
            read_json(request_file))

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'])

        assert (
                verify_test(
                    result_response, 0,
                    self.test_obj.build_request_output['pre_test_output'],
                    self.test_obj.build_request_output['action_obj'])
                is TestStep.FAILURE.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.test_workordersubmit_workloadId_twoworkload
    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.set1
    def test_workordersubmit_workloadId_twoworkload(self):
        test_id = '18805'
        request_file = os.path.join(
            globals.work_order_input_file,
            "work_order_two_workloadid.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.wo_submit_output_json_file_name,
            read_json(request_file))

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'])

        assert (
                verify_test(
                    result_response, 0,
                    self.test_obj.build_request_output['pre_test_output'],
                    self.test_obj.build_request_output['action_obj'])
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.test_workordersubmit_workorderId_null
    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.p1
    @pytest.mark.set1
    def test_workordersubmit_workorderId_null(self):
        test_id = '18717'
        request_file = os.path.join(
            globals.work_order_input_file,
            "work_order_submit_WorkOrderId_null.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.wo_submit_output_json_file_name,
            read_json(request_file))

        assert (
                check_negative_test_responses(
                    submit_response,
                    "Invalid data format for work order id")
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.test_workordersubmit_workerId_nullstring
    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.set1
    def test_workordersubmit_workerId_nullstring(self):
        test_id = '18718'
        request_file = os.path.join(
            globals.work_order_input_file,
            "workorder_workerId_null_number_randomString.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.wo_submit_output_json_file_name,
            read_json(request_file))

        assert (
                check_negative_test_responses(
                    submit_response,
                    "Invalid data format for Worker id")
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.test_workordersubmit_workloadId_specialcharacters
    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.set1
    def test_workordersubmit_workloadId_specialcharacters(self):
        test_id = '18730'
        request_file = os.path.join(
            globals.work_order_input_file,
            "work_order_workloadId_specialcharacters.json")
        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.wo_submit_output_json_file_name,
            read_json(request_file))

        assert (
                check_negative_test_responses(
                    submit_response,
                    "Invalid workload id")
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.test_workordersubmit_encrypteddataencryptionkey_nullechoclient
    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.set1
    def test_workordersubmit_encrypteddataencryptionkey_nullechoclient(self):
        test_id = '18785'
        request_file = os.path.join(
            globals.work_order_input_file,
            "work_order_both_in_out_Data_EncryptionKey_null_echo.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.wo_submit_output_json_file_name,
            read_json(request_file))

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'])

        assert (
                verify_test(
                    result_response, 0,
                    self.test_obj.build_request_output['pre_test_output'],
                    self.test_obj.build_request_output['action_obj'])
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.test_workordersubmit_dataencryptionalgorithm_listsamealgotwice
    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.set1
    def test_workordersubmit_dataencryptionalgorithm_listsamealgotwice(self):
        test_id = '18788'
        request_file = os.path.join(
            globals.work_order_input_file,
            "work_order_submit_dataEncryptionAlgorithm_list_same_algo_twice.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.wo_submit_output_json_file_name,
            read_json(request_file))

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'])

        assert (
                verify_test(
                    result_response, 0,
                    self.test_obj.build_request_output['pre_test_output'],
                    self.test_obj.build_request_output['action_obj'])
                is TestStep.FAILURE.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.test_workordersubmit_encrypteddataencryptionkey_hyphenechoclient
    @pytest.mark.listener
    @pytest.mark.set1
    def test_workordersubmit_encrypteddataencryptionkey_hyphenechoclient(self):
        test_id = '18711'
        request_file = os.path.join(
            globals.work_order_input_file,
            "work_order_submit_inData_outData_encryptedDataEncryptionKey_hyphen_echoClient.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.wo_submit_output_json_file_name,
            read_json(request_file))

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'])
        assert (
                verify_test(
                    result_response, 0,
                    self.test_obj.build_request_output['pre_test_output'],
                    self.test_obj.build_request_output['action_obj'])
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.test_workordersubmit_encrypteddataencryptionkey_remove
    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.set1
    def test_workordersubmit_encrypteddataencryptionkey_remove(self):
        test_id = '18754'
        request_file = os.path.join(
            globals.work_order_input_file,
            "work_order_submit_encryptedDataEncryptionKey_not_set_echoClient.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.wo_submit_output_json_file_name,
            read_json(request_file))

        assert (
                check_negative_test_responses(
                    submit_response,
                    "Invalid data format for data hash of in data")
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.test_workordersubmit_encrypteddataencryptionkey_emptyechoclient
    @pytest.mark.listener
    @pytest.mark.sdk
    @pytest.mark.set1
    def test_workordersubmit_encrypteddataencryptionkey_emptyechoclient(self):
        test_id = '18806'
        request_file = os.path.join(
            globals.work_order_input_file,
            "work_order_submit_encryptedDataEncryptionKey_empty_echoClient.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.wo_submit_output_json_file_name,
            read_json(request_file))

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'])
        assert (
                verify_test(
                    result_response, 0,
                    self.test_obj.build_request_output['pre_test_output'],
                    self.test_obj.build_request_output['action_obj'])
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.test_workordersubmit_outdata_success
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_workordersubmit_outdata_success(self):
        test_id = '18710'
        request_file = os.path.join(
            globals.work_order_input_file,
            "work_order_submit_with_outdata.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.wo_submit_output_json_file_name,
            read_json(request_file))

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'])

        assert (
                verify_test(
                    result_response, 0,
                    self.test_obj.build_request_output['pre_test_output'],
                    self.test_obj.build_request_output['action_obj'])
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.test_workordersubmit_indata_bothindexremoveDataDatahash
    @pytest.mark.listener
    def test_workordersubmit_indata_bothindexremoveDataDatahash(self):
        test_id = '18714'
        request_file = os.path.join(
            globals.work_order_input_file,
            "work_order_submit_remove_both_data_datahash_in_inData.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.wo_submit_output_json_file_name,
            read_json(request_file))

        assert (
                check_negative_test_responses(
                    submit_response,
                    "Missing in data parameter data")
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')


    @pytest.mark.workordersubmit
    @pytest.mark.test_workordersubmit_indata_oneValidOtherEmptDataDatahash
    @pytest.mark.listener
    def test_workordersubmit_indata_oneValidOtherEmptDataDatahash(self):
        test_id = '18715'
        request_file = os.path.join(
            globals.work_order_input_file,
            "work_order_submit_with_one_valid_and_other_empty_data_and_datahash_in_indata.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.wo_submit_output_json_file_name,
            read_json(request_file))

        assert (
                check_negative_test_responses(
                    submit_response,
                    "Invalid data format for data hash of in data")
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')


    @pytest.mark.workordersubmit
    @pytest.mark.test_workordersubmit_indata_singleindexremoveDataDatahash
    @pytest.mark.listener
    def test_workordersubmit_indata_singleindexremoveDataDatahash(self):
        test_id = '18716'
        request_file = os.path.join(
            globals.work_order_input_file,
            "work_order_submit_remove_both_data_datahash_Single_index_in_inData.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.wo_submit_output_json_file_name,
            read_json(request_file))

        assert (
                check_negative_test_responses(
                    submit_response,
                    "Missing in data parameter data")
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.test_workordersubmit_indata_index2randomstr
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_workordersubmit_indata_index2randomstr(self):
        test_id = '18719'
        request_file = os.path.join(
            globals.work_order_input_file,
            "work_order_submit_indata_data_index2_random_str.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.wo_submit_output_json_file_name,
            read_json(request_file))

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'])
        assert (
               check_negative_test_responses(
                   result_response,
                   "Invalid Request")
                is TestStep.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.test_workordersubmit_indata_index1randomstr
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_workordersubmit_indata_index1randomstr(self):
        test_id = '18720'
        request_file = os.path.join(
            globals.work_order_input_file,
            "work_order_submit_indata_data_index1_random_str.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.wo_submit_output_json_file_name,
            read_json(request_file))

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'])
        assert (
               check_negative_test_responses(
                   result_response,
                   "Invalid Request")
                is TestStep.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.test_workordersubmit_workloadid_emptystring
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_workordersubmit_workloadid_emptystring(self):
        test_id = '18722'
        request_file = os.path.join(
            globals.work_order_input_file,
            "work_order_submit_workload_id_empty_string.json")
        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.wo_submit_output_json_file_name,
            read_json(request_file))

        assert (
                check_negative_test_responses(
                    submit_response,
                    "Invalid data format for work load id")
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.test_workordersubmit_workloadid_hexstring
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_workordersubmit_workloadid_hexstring(self):
        test_id = '18723'
        request_file = os.path.join(
            globals.work_order_input_file,
            "work_order_submit_workload_id_hex_string.json")
        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.wo_submit_output_json_file_name,
            read_json(request_file))

        assert (
                check_negative_test_responses(
                    submit_response,
                    "Invalid workload id")
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.test_workordersubmit_workload_nullstring
    @pytest.mark.listener
    def test_workordersubmit_workload_nullstring(self):
        test_id = '18726'
        request_file = os.path.join(
            globals.work_order_input_file,
            "work_order_submit_workLoad_null_string.json")
        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.wo_submit_output_json_file_name,
            read_json(request_file))

        assert (
                check_negative_test_responses(
                    submit_response,
                    "Invalid workload id")
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.test_workordersubmit_workorderid_increasedhexlength
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_workordersubmit_workorderid_increasedhexlength(self):
        test_id = '18727'
        request_file = os.path.join(
            globals.work_order_input_file,
            "work_order_submit_WorkOrder_increased_hexlength.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.wo_submit_output_json_file_name,
            read_json(request_file))

        assert (
                check_negative_test_responses(
                    submit_response,
                    "Invalid data format for work order id")
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')


    @pytest.mark.workordersubmit
    @pytest.mark.test_workordersubmit_workorderidworkloadid_same
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_workordersubmit_workorderidworkloadid_same(self):
        test_id = '18728'
        request_file = os.path.join(
            globals.work_order_input_file,
            "work_order_submit_same_WorkOrderID_WorkloadId.json")


        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.wo_submit_output_json_file_name,
            read_json(request_file))

        assert (
                check_negative_test_responses(
                    submit_response,
                    "Invalid data format for work order id")
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.test_workordersubmit_data_differentdataheartdisease
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_workordersubmit_data_differentdataheartdisease(self):
        test_id = '18731'
        request_file = os.path.join(
            globals.work_order_input_file,
            "work_order_submit_indata_index1_data_different_hexlength.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.wo_submit_output_json_file_name,
            read_json(request_file))

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'])

        assert (
                verify_test(
                    result_response, 0,
                    self.test_obj.build_request_output['pre_test_output'],
                    self.test_obj.build_request_output['action_obj'])
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')


    @pytest.mark.workordersubmit
    @pytest.mark.test_workordersubmit_requesterId_specialcharacter
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_workordersubmit_requesterId_specialcharacter(self):
        test_id = '18734'
        request_file = os.path.join(
            globals.work_order_input_file,
            "work_order_submit_requesterId_som_special_characters.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.wo_submit_output_json_file_name,
            read_json(request_file))

        assert (
               check_negative_test_responses(
                   submit_response,
                   "Invalid data format for requester id")
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.test_work_order_submit_requesterNonce_param_empty
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_work_order_submit_requesterNonce_param_empty(self):
        test_id = '18735'
        request_file = os.path.join(
            globals.work_order_input_file,
            "work_order_submit_requesterNonce_param_empty.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.wo_submit_output_json_file_name,
            read_json(request_file))

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'])
        assert (
               check_negative_test_responses(
                   result_response,
                   "Invalid Request")
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')


    @pytest.mark.workordersubmit
    @pytest.mark.test_workordersubmit_requestersignature_differentlength
    @pytest.mark.listener
    def test_workordersubmit_requestersignature_differentlength(self):
        test_id = '18492'
        request_file = os.path.join(
            globals.work_order_input_file,
            "work_order_verify_requesterSignature_diff_length.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.wo_submit_output_json_file_name,
            read_json(request_file))

        assert (
               check_negative_test_responses(
                   submit_response,
                   "Invalid data format for requesterSignature")
                is TestStep.SUCCESS.value)
        
        logger.info('\t\t!!! Test completed !!!\n\n')


    @pytest.mark.workordersubmit
    @pytest.mark.test_workordersubmit_verifyingkey_nullstr
    @pytest.mark.listener
    def test_workordersubmit_verifyingkey_nullstr(self):
        test_id = '18501'
        request_file = os.path.join(
            globals.work_order_input_file,
            "work_order_submit_verifyingkey_null_str.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.wo_submit_output_json_file_name,
            read_json(request_file))
        assert (
               check_negative_test_responses(
                   submit_response,
                   "Crypto Error (deserializeECDSAPublicKey): Could not deserialize public ECDSA key")
                is TestStep.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')


    @pytest.mark.workordersubmit
    @pytest.mark.test_workordersubmit_indataoutdata_success
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_workordersubmit_indataoutdata_success(self):
        test_id = '18703'
        request_file = os.path.join(
            globals.work_order_input_file,
            "workordersubmit_indata_outdata.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.wo_submit_output_json_file_name,
            read_json(request_file))

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'])
        assert (
                verify_test(
                    result_response, 0,
                    self.test_obj.build_request_output['pre_test_output'],
                    self.test_obj.build_request_output['action_obj'])
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.test_workordersubmit_workorderId_remove
    @pytest.mark.sdk
    @pytest.mark.listener
    def test_workordersubmit_workorderId_remove(self):
        test_id = '18725'
        request_file = os.path.join(
            globals.work_order_input_file,
            "workordersubmit_workorderId_remove.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.wo_submit_output_json_file_name,
            read_json(request_file))        
        assert (
                  check_negative_test_responses(
                   submit_response,
                   "Invalid data format for work order id")
                  is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')


    @pytest.mark.workordersubmit
    @pytest.mark.test_workordersubmit_sessionkeyiv_allspecial_characters
    @pytest.mark.listener
    def test_workordersubmit_sessionkeyiv_allspecial_characters(self):
        test_id = '18737'
        request_file = os.path.join(
            globals.work_order_input_file,
            "workordersubmit_sessionkeyiv_allspecialchar.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.wo_submit_output_json_file_name,
            read_json(request_file))

        assert (
                  check_negative_test_responses(
                   submit_response,
                   "Invalid data format for session key iv")
                  is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.test_workordersubmit_requesterId_differenthexlength
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_workordersubmit_requesterId_differenthexlength(self):
        test_id = '18742'
        request_file = os.path.join(
            globals.work_order_input_file,
            "workordersubmit_requesterId_variouslengthhex.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.wo_submit_output_json_file_name,
            read_json(request_file))

        assert (
                check_negative_test_responses(
                    submit_response,
                    "Invalid parameter requesterId")
                is TestStep.SUCCESS.value)        
        logger.info('\t\t!!! Test completed !!!\n\n')


    @pytest.mark.workordersubmit
    @pytest.mark.test_workordersubmit_workerEncryptionKey_notdefaulthex
    @pytest.mark.sdk
    @pytest.mark.listener
    def test_workordersubmit_workerEncryptionKey_notdefaulthex(self):
        test_id = '18743'
        request_file = os.path.join(
            globals.work_order_input_file,
            "workordersubmit_workerEncryptionKey_notdefaulthex.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.wo_submit_output_json_file_name,
            read_json(request_file))
        assert (
                check_negative_test_responses(
                    submit_response,
                    "Invalid parameter workerEncryptionKey")
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')


    @pytest.mark.workordersubmit
    @pytest.mark.test_workordersubmit_requesterNonce_notdefaultlength
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_workordersubmit_requesterNonce_notdefaultlength(self):
        test_id = '18745'
        request_file = os.path.join(
            globals.work_order_input_file,
            "workordersubmit_requesterNonce_notdefaultlength.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.wo_submit_output_json_file_name,
            read_json(request_file))
        assert (
                check_negative_test_responses(
                    submit_response,
                    "Invalid parameter requesterNonce")
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')


    @pytest.mark.workordersubmit
    @pytest.mark.test_workordersubmit_requesterSignature_no
    @pytest.mark.listener
    def test_workordersubmit_requesterSignature_no(self):
        test_id = '18613'
        request_file = os.path.join(
            globals.work_order_input_file,
            "workordersubmit_encryptedRequestHash_norequesterSignature.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.wo_submit_output_json_file_name,
            read_json(request_file))

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'])
        assert (
                verify_test(
                    result_response, 0,
                    self.test_obj.build_request_output['pre_test_output'],
                    self.test_obj.build_request_output['action_obj'])
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')


    @pytest.mark.workordersubmit
    @pytest.mark.test_workordersubmit_encryptedRequestHash_no
    @pytest.mark.listener
    def test_workordersubmit_encryptedRequestHash_no(self):
        test_id = '18777'
        request_file = os.path.join(
            globals.work_order_input_file,
            "workordersubmit_requesterSignature_noencryptedRequestHash.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.wo_submit_output_json_file_name,
            read_json(request_file))
        assert (
                  check_negative_test_responses(
                   submit_response,
                   "Missing parameter encryptedRequestHash")
                  is TestStep.SUCCESS.value)

        logger.info('\t\t!!! Test completed !!!\n\n')


    @pytest.mark.workordersubmit
    @pytest.mark.test_workordersubmit_mandatoryfields_remove
    def test_workordersubmit_mandatoryfields_remove(self):
        test_id = '18781'
        request_file = os.path.join(
            globals.work_order_input_file,
            "workordersubmit_mandatoryfields_remove.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.wo_submit_output_json_file_name,
            read_json(request_file))
        assert (
                  check_negative_test_responses(
                   submit_response,
                   "Invalid params")
                  is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.test_workordersubmit_id_remove
    @pytest.mark.listener
    def test_workordersubmit_id_remove(self):
        test_id = '18787'
        request_file = os.path.join(
            globals.work_order_input_file,
            "workordersubmit_id_remove.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.wo_submit_output_json_file_name,
            read_json(request_file))
        assert (
                  check_negative_test_responses(
                   submit_response,
                   "Server error")
                  is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')

    @pytest.mark.workordersubmit
    @pytest.mark.test_workordersubmit_workeridworkloadid_same
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_workordersubmit_workeridworkloadid_same(self):
        test_id = '18794'
        request_file = os.path.join(
            globals.work_order_input_file,
            "workordersubmit_workeridworkloadid_same.json")
        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.wo_submit_output_json_file_name,
            read_json(request_file))
        assert (
                  check_negative_test_responses(
                   submit_response,
                   "Invalid workload id")
                  is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')


    @pytest.mark.workordersubmit
    @pytest.mark.test_workordersubmit_indata_firstinparams
    @pytest.mark.listener
    @pytest.mark.sdk
    def test_workordersubmit_indata_firstinparams(self):
        test_id = '18796'
        request_file = os.path.join(
            globals.work_order_input_file,
            "workordersubmit_indata_firstinparams.json")

        err_cd = \
            self.test_obj.setup_and_build_request_wo_submit(
                read_json(request_file))

        submit_response = submit_request(
            self.test_obj.uri_client,
            self.test_obj.build_request_output['request_obj'],
            globals.wo_submit_output_json_file_name,
            read_json(request_file))

        result_response = self.test_obj.getresult(
            self.test_obj.build_request_output['request_obj'])
        assert (
                verify_test(
                    result_response, 0,
                    self.test_obj.build_request_output['pre_test_output'],
                    self.test_obj.build_request_output['action_obj'])
                is TestStep.SUCCESS.value)
        logger.info('\t\t!!! Test completed !!!\n\n')