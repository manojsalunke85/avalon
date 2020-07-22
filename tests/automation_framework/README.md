# Automation test framework 

This is a test framework client intended to execute automated tests. 
The intention is to run tests in direct/ proxy invocation models. 
This is to validate the response of worker, work order and work 
order receipts APIs as per Enterprise Ethereum Alliance Off-Chain 
Trusted Compute Specification v1.1.

Steps to execute automation test framework:

1. Build Avalon: Refer to Build.md from the link below.
     https://github.com/hyperledger/avalon/blob/master/BUILD.md
2. Open a Docker container shell using following command. 
     docker exec -it avalon-shell bash
4. Running automation tests in Listener/SDK/Proxy Mode(Ethereum/Fabric) using markers.
   Listener Mode:
   cd $TCF_HOME/tests/automation_framework
   Edit env.py and change the test_mode to "listener"
   Command: pytest -m listener
   
   SDK Mode:
   Edit env.py and change the test_mode to "sdk"
   Command: pytest -m sdk
   
   Proxy(Ethereum) Mode:
   Edit env.py and change the blockchain_type to "ethereum", test_mode to "sdk", proxy_mode to "True"
   Command: pytest -m ethereum
   
   Proxy(Fabric) Mode:
   Edit env.py and change the blockchain_type to "fabric", test_mode to "sdk", proxy_mode to "True"
   Command: pytest -m fabric
5. To run single test
	cd $TCF_HOME/tests/automation_framework
	e.g pytest -k "test_workordersumit_success"
6. To run all the tests from specific APIs (e.g Worker Setstatus/Worker Register/Workorder Submit)
    e.g 1. pytest tests/worker_tests/test_set_status.py
    e.g 2. pytest tests/worker_tests/test_registry.py
    e.g 3. pytest tests/work_order_tests/test_submit.py
