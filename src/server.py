from __future__ import print_function

import time
import grpc

from generated import employee_pb2_grpc
from concurrent import futures
import employee_orm

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class EmployeeServicer(employee_pb2_grpc.EmployeeServicer):
    def __init__(self):
        self.__emp_orm = employee_orm.EmployeeORM()

    def Read(self, request, context):
        print("Read employee service called...")
        return self.__emp_orm.select(request)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    employee_pb2_grpc.add_EmployeeServicer_to_server(EmployeeServicer(), server)
    server.add_insecure_port('[::]:40084')
    server.start()
    print("Employee server running on 40084...")
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except:
        server.stop(0)

if __name__ == '__main__':
    serve()
