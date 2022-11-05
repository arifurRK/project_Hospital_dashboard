from DBconnection.dbconf import PostgresConnection
import pandas as pd


class Query9:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query9 = "SELECT i.item_name, s.division, sum(ft.total_price) "\
            "FROM star.fact_table ft "\
            "JOIN star.item_dim i on i.item_key=ft.item_key "\
            "JOIN star.store_dim s on s.store_key = ft.store_key "\
            "GROUP BY CUBE(i.item_name, s.division) "\
            "ORDER BY i.item_name,s.division "
        cur.execute(query9)
        itemsdiv = cur.fetchall()
        idiv = pd.DataFrame(list(itemsdiv), columns=['Item', 'Division', 'Sales'])
        idiv = idiv.dropna()
        # pd_data.set_index("Division", inplace = True)
        # pd_data['Sales'] = pd_data['Sales'].astype('float64')
        idiv.head(30)
        # pd_data.plot.pie(y='Sales', figsize=(15,10))
        return idiv.to_dict(orient='records')


if __name__ == '__main__':
    q9 = Query9()
    data = q9.execute()
    print(data)