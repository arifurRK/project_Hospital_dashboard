from DBconnection.dbconf import PostgresConnection
import pandas as pd


class Query5:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = """SELECT store_dim.district as "district",time_dim.year,SUM(fact_table.total_price) "sales"
FROM star.fact_table
JOIN star.store_dim ON
store_dim.store_key=fact_table.store_key
JOIN star.time_dim ON
time_dim.time_key=fact_table.time_key
WHERE store_dim.district='BARISAL'AND
time_dim.year='2015'
GROUP BY time_dim.year,store_dim.district
"""

        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['district','Year', 'sales'])
        pd_data['sales'] = pd_data['sales'].astype('float64')
        pd_data = pd_data.dropna()
        # print(pd_data)
        return pd_data.to_dict(orient='records')


if __name__ == '__main__':
    query5 = Query5()
    data = query5.execute()
    print(data)
