from DBconnection.dbconf import PostgresConnection
import pandas as pd


class Query5:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = """SELECT bill_info.DAY,COUNT(bill_info.APPOINT_NO) AS patient_count
        FROM hospitals.bill_info 
        GROUP BY (bill_info.DAY)
        ORDER BY patient_count DESC
"""

        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['DAY', 'patient_count'])
        pd_data['patient_count'] = pd_data['patient_count'].astype('float64')
        pd_data = pd_data.dropna()
        # print(pd_data)
        return pd_data.to_dict(orient='records')


if __name__ == '__main__':
    query5 = Query5()
    data = query5.execute()
    print(data)
