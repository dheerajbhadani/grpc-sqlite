from __future__ import print_function

import grpc
from generated import employee_pb2, employee_pb2_grpc

class EmployeeClient(object):

    def get_employee(self, stub):
        read_request = employee_pb2.readRequestPB()
        read_request.first_name = "Pauli"
        #read_request.gender = "Female"
        return stub.Read(read_request)

def run():
    channel = grpc.insecure_channel('localhost:40084')
    stub = employee_pb2_grpc.EmployeeStub(channel)

    emp_client = EmployeeClient()
    print(emp_client.get_employee(stub))

if __name__ == '__main__':
    run()
