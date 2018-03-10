__author__ = 'Dheeraj Bhadani'

import sqlite3
from generated import employee_pb2

class EmployeeORM(object):
    def __init__(self):
        pass

    def run_query(self, query):
        conn = sqlite3.connect('G:/RnD/grpc-sqlite/resource/employees.db')
        curs = conn.cursor()
        curs.execute(query)
        return curs

    def select(self, requestPB):
        base_query = 'select * from EMPLOYEE'

        if requestPB.ListFields():
            where_clause = " WHERE "
        condition_count = 0
        for f in requestPB.ListFields():
            if condition_count == 0:
                where_clause += ' {0} = "{1}"'.format(f[0].name, f[1])
            else:
                where_clause += ' AND {0} = "{1}"'.format(f[0].name, f[1])
            condition_count += 1

        query = base_query + where_clause

        query_result = self.run_query(query)

        result = []
        for cur in query_result:
            response = employee_pb2.readResponsePB()
            response.first_name = str(cur[1])
            response.last_name = str(cur[2])
            response.email = str(cur[3])
            response.gender = str(cur[4])
            response.ip_address = str(cur[5])
            response.country = str(cur[6])
            response.postcode = str(cur[7])
            response.id = int(cur[0])
            result.append(response)

        response_list = employee_pb2.readResponseListPB()
        response_list.employee.extend(result)
        return response_list
