# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import cgi
import json
from CreditPaymentsModule import CreditPayments
import xmlrpc.client

# ��������� ������ �� ���������� �������
form = cgi.FieldStorage()
deal_id = form.getfirst("deal_id", "none")
pay_date = form.getfirst("pay_date", "none")
obj = CreditPayments()
res_rest = obj.getRestOfCredit(deal_id, pay_date)
res_sum = obj.getSummOfCredit(deal_id)

# ������� XML-RPC ������� ��� �������� ClientInfo � RisksInfo
clientinfo_client = xmlrpc.client.ServerProxy("http://localhost:8001")
risksinfo_client = xmlrpc.client.ServerProxy("http://localhost:8002")

# ��������� ���������� � ������� � ��� ��������� �������
inn = clientinfo_client.get_inn(deal_id)
name = clientinfo_client.get_name(inn)
credit_history = risksinfo_client.get_credit_history(inn)

# ����� ����������� � ���� JSON
print("Content-type: application/json\n")
result = {
    "deal_id": deal_id,
    "pay_date": pay_date,
    "res_rest": res_rest,
    "res_sum": res_sum,
    "inn": inn,
    "name": name,
    "credit_history": credit_history
}
print(json.dumps(result))
