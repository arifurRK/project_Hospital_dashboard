

from flask import Blueprint
from QueryServices.query1service import Query1API
from QueryServices.query2service import Query2API
from QueryServices.query3services import Query3API
from QueryServices.query4services import Query4API


query_api = Blueprint('queryapi', __name__)

query_api.add_url_rule('/query1', view_func=Query1API.as_view("Get Division-wise Sales"))
query_api.add_url_rule('/query2', view_func=Query2API.as_view("Customer wise total_sale_price"))
query_api.add_url_rule('/query3', view_func=Query3API.as_view("a"))
query_api.add_url_rule('/query4', view_func=Query4API.as_view("Customer wise a"))
