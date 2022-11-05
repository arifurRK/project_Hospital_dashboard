from DBconnection.dbconf import PostgresConnection
import pandas as pd


class Query2:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = """SELECT bill_info.MONTH,SUM(bill_info.CONSULT_FEE) 
FROM hospitals.bill_info 
GROUP BY (bill_info.MONTH) 
"""
        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['Month', 'Generated revenue'])
        pd_data['Generated revenue']= pd_data['Generated revenue'].astype('float64')
        pd_data = pd_data.dropna()
        # print(pd_data)
        return pd_data.to_dict(orient='records')


if __name__ == '__main__':
    query2 = Query2()
    data = query2.execute()
    print(data)
