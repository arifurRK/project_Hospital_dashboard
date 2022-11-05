from DBconnection.dbconf import PostgresConnection
import pandas as pd


class Query8:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = """SELECT item_dim.item_name, quarter, SUM(quantity)
FROM star.fact_table
JOIN star.item_dim ON item_dim.item_key = fact_table.item_key
JOIN star.time_dim ON time_dim.time_key = fact_table.time_key
GROUP BY CUBE(item_name, time_dim.quarter)
ORDER BY item_name, SUM(quantity)"""
        cur.execute(query)
        sq = cur.fetchall()
        quarter_info = pd.DataFrame(list(sq), columns=['item', 'quarter', 'sales'])
        quarter_info = quarter_info.dropna()
        # quarter_info = quarter_info.groupby('quarter').head(10)
        quarter_info

        return quarter_info.to_dict(orient='records')




if __name__ == '__main__':
    q8 = Query8()
    data = q8.execute()
    print(data)