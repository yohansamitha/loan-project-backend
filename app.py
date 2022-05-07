from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


def saveUser():
    user = request.json
    userName = user['name']
    userAmount = user['amount']
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='bank_loan',
                                             user='root',
                                             password='1234')

        query = """INSERT INTO shareholder(Name, Amount) values (%s,%s)"""
        data = (userName, userAmount)
        cursor = connection.cursor()
        cursor.execute(query, data)
        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into shareholder table")
        cursor.close()

    except mysql.connector.Error as error:
        print("Failed to insert record into shareholder table {}".format(error))

    finally:
        if connection.is_connected():
            connection.close()
            print("MySQL connection is closed")

    return jsonify(request.json)


@app.route('/registration', methods=['POST'])
def registerUser():
    return saveUser()


if __name__ == '__main__':
    app.run(debug=True)
