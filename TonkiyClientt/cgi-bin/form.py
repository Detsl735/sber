# -*- coding: utf-8 -*-
import cgi
import json
from CreditPaymentsModule import CreditPayments

form = cgi.FieldStorage()
deal_id = form.getfirst("deal_id", "none")
pay_date = form.getfirst("pay_date", "none")


obj=CreditPayments()
res_rest=obj.getRestOfCredit(deal_id, pay_date)
res_sum=obj.getSummOfCredit(deal_id)


print("Content-type: application/json\n")
print(json.dumps({"result_rest": res_rest}))
print(json.dumps({"result_sum": res_sum}))