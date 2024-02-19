# -*- coding: utf-8 -*-
#!/usr/bin/env python3

from xmlrpc.server import SimpleXMLRPCServer

# "���� ������" � ����������� � ��������
client_data = {
    "1": {"inn": "1234567890", "name": "Bob"},
    "2": {"inn": "9876543210", "name": "Sagan"}
}
client2_data = {
     "1234567890":  {"name": "Bob"},
     "9876543210": {"name": "Sagan"}
}

def get_inn(deal_id):
    return client_data.get(deal_id, {}).get("inn", "Not found")

def get_name(inn):
    return client2_data.get(inn, {}).get("name", "Not found")

# ������� XML-RPC ������
server = SimpleXMLRPCServer(("localhost", 8001))

# ������������ �������, ��������� ��� ������ �� RPC
server.register_function(get_inn, "get_inn")
server.register_function(get_name, "get_name")

# ��������� ������
print("ClientInfo service started on localhost:8001")
server.serve_forever()
