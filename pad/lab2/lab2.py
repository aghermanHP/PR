from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from flask_mysqldb import MySQL


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})
app.config['CORS_HEADERS'] = 'Content-Type'

#database
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'gherman'
app.config['MYSQL_PASSWORD'] = '01092019'
app.config['MYSQL_DB'] = 'tests'
mysql = MySQL(app)

@app.route('/user', methods=['GET', 'POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def all_books():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        firstName = post_data.get('firstName')
        lastName = post_data.get('lastName')
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO MyUsers(firstName, lastName) VALUES (%s, %s)", (firstName, lastName))
        mysql.connection.commit()
        cur.close()
        response_object['message'] = 'USer succesfuly writed in db'
    else:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM MyUsers")
        allUsers = cur.fetchall()
        mysql.connection.commit()
        cur.close()
        return jsonify({
            'status': 'success',
            'mails': allUsers
        })
    return jsonify(response_object)

if __name__ == '__main__':
    app.run()
