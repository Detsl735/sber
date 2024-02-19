# -*- coding: utf-8 -*-
#!/usr/bin/env python3

from xmlrpc.server import SimpleXMLRPCServer

# "���� ������" � ����������� � ��������� ������� ��������
risks_data = {
    "1234567890": "good",
    "9876543210": "bad"
}

def get_credit_history(inn):
    return risks_data.get(inn, "Unknown")

# ������� XML-RPC ������
server = SimpleXMLRPCServer(("localhost", 8002))

# ������������ �������, ��������� ��� ������ �� RPC
server.register_function(get_credit_history, "get_credit_history")

# ��������� ������
print("RisksInfo service started on localhost:8002")
server.serve_forever()
