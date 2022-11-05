from DBconnection.dbconf import PostgresConnection
import pandas as pd


class Query3:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = """SELECT bill_info.DAY as "day of week",sum(bill_info.CONSULT_FEE) as "total income"
FROM hospitals.bill_info 
GROUP BY (bill_info.DAY)
ORDER BY bill_info.DAY """


        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['Day', 'total_income'])
        pd_data['total_income'] = pd_data['total_income'].astype('float64')
        pd_data = pd_data.dropna()
        # print(pd_data)
        return pd_data.to_dict(orient='records')


if __name__ == '__main__':
    query3 = Query3()
    data = query3.execute()
    print(data)
