from DBconnection.dbconf import PostgresConnection
import pandas as pd


class Query6:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = """SELECT store_dim.store_key as store_key, item_dim.item_name as item_name, sum(fact_table.quantity) as quantity_of_sales 
FROM star.fact_table  
JOIN star.store_dim ON
store_dim.store_key = fact_table.store_key 
JOIN star.item_dim ON 
item_dim.item_key = fact_table.item_key 
GROUP BY CUBE(store_dim.store_key, item_dim.item_name)
ORDER BY store_dim.store_key, sum(fact_table.quantity) desc"""

        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['district','Year', 'sales'])
        pd_data['sales'] = pd_data['sales'].astype('float64')
        pd_data = pd_data.dropna()
        # print(pd_data)
        return pd_data.to_dict(orient='records')


if __name__ == '__main__':
    query6 = Query6()
    data = query6.execute()
    print(data)
