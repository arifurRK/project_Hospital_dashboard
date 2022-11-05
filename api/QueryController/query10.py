from DBconnection.dbconf import PostgresConnection
import pandas as pd


class Query10:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = """SELECT store_dim.store_key as "STORE", month as "MONTH", SUM(total_price)/30 as "Average sales"
FROM star.fact_table
JOIN star.store_dim ON store_dim.store_key = fact_table.store_key
JOIN star.time_dim ON time_dim.time_key = fact_table.time_key
GROUP BY CUBE(store_dim.store_key, time_dim."month")
ORDER By store_dim.store_key, month"""

        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['item_name','month', 'sales'])
        pd_data['sales'] = pd_data['sales'].astype('float64')
        pd_data = pd_data.dropna()
        # print(pd_data)
        return pd_data.to_dict(orient='records')


if __name__ == '__main__':
    query10 = Query10()
    data = query10.execute()
    print(data)
