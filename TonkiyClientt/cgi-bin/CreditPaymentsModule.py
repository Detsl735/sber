import sqlite3
import time
from datetime import date

class CreditPayments:

    def __init__(self):
        # connect to DB
        # save cursor object to self property
        conn = sqlite3.connect("./mydatabase.db")
        self.cursor = conn.cursor()
        pass
        
    #method convert date from MM.yyyy in unix format
    def get_timestamp(self, x):
        # Calc date in unix format
        date_arr = x.split(".")
        d = date(int(date_arr[1]), int(date_arr[0]), 1)
        unixtime = time.mktime(d.timetuple())
        return unixtime
    
    #method getRestOfCredit
    def getRestOfCredit(self, id, date):
        # get summ of credit
        # query payments from DB where deal_id=id AND pdate<=date
        # calculate rest of credit and return it
        summ = self.getSummOfCredit(id)
        sql = "SELECT sum(summ) FROM payment WHERE deal_id=? AND pdate<=?"
        self.cursor.execute(sql, [(id), (self.get_timestamp(date))])
        payed=self.cursor.fetchone()[0]
        return summ-payed

    #method getSummOfCredit
    def getSummOfCredit(self, id):
        # query summ of credit from DB where id=id
        # return it
        sql = "SELECT summ FROM credit WHERE id=?"
        self.cursor.execute(sql, [id])
        summ = self.cursor.fetchone()[0]
        return summ
        
