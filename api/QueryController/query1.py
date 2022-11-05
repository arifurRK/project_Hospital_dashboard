from DBconnection.dbconf import PostgresConnection
import pandas as pd


class Query1:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = """SELECT patient_info.gender as "gender", COUNT(bill_info.appoint_no) "Visited patient" 
FROM hospitals.bill_info 
JOIN hospitals.patient_info ON patient_info.appoint_no = bill_info.appoint_no
GROUP BY (patient_info.gender) """

        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['gender', 'Visited patient'])
        pd_data = pd_data.dropna()
        # print(pd_data)
        return pd_data.to_dict(orient='records')


if __name__ == '__main__':
    query1 = Query1()
    data = query1.execute()
    print(data)
