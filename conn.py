from abc import ABC
#abc = abstract base class

class Data(ABC):

    def __init__(self):
        conn = mysql.connector.connect(host="localhost",port=3306,user="root",password="",database="pbo2_toko")
        curs = conn.cursor()

    def execute(self,query):
        return self.connection.execute(query)

    def commit(self):
        return self.connection.commit()
        
