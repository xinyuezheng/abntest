from flask import Flask
from flask_restful import Resource, Api
from flask_api import status
import sqlite3
import db_constants
import os


def _query_db(query_str):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    db_path = os.path.join(dir_path, db_constants.DB_NAME)
    with sqlite3.connect(db_path, timeout=10) as conn:
        # enables column access by name: row['column_name']
        conn.row_factory = sqlite3.Row
        rows = conn.execute(query_str).fetchall()
        query_result = [dict(i) for i in rows]

    return query_result


class StartCodingAge(Resource):
    def get(self, country_code):
        query_str = \
            f'select "Country Name", "Country Code", "Age1stCodeYoungest" from CountryStartCodingAge where "Country Code"= "{country_code}"'

        try:
            query_result = _query_db(query_str)
            status_code = status.HTTP_200_OK
        except sqlite3.Error as err:
            err_msg = f'SQLite error: {" ".join(err.args)}'
            query_result = {"err_msg": err_msg}
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

        return query_result, status_code


app = Flask(__name__)
api = Api(app)
api.add_resource(StartCodingAge, '/startcoding/<country_code>')

if __name__ == '__main__':
     app.run(port='8080')
