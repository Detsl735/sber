# -*- coding: utf-8 -*-
#!/usr/bin/env python3

from xmlrpc.server import SimpleXMLRPCServer

# "База данных" с информацией о кредитной истории клиентов
risks_data = {
    "1234567890": "good",
    "9876543210": "bad"
}

def get_credit_history(inn):
    return risks_data.get(inn, "Unknown")

# Создаем XML-RPC сервер
server = SimpleXMLRPCServer(("localhost", 8002))

# Регистрируем функцию, доступную для вызова по RPC
server.register_function(get_credit_history, "get_credit_history")

# Запускаем сервер
print("RisksInfo service started on localhost:8002")
server.serve_forever()
