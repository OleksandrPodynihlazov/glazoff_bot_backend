from flask import Flask, request, jsonify
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

DB_PATH ="business.db"


@app.route("/services",methods=["GET"])
def get_services():
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM pages")
        rows = cursor.fetchall()

        services=[
            {
                "service_id":row[0],
                "service_url":row[1],
                "service_name":row[2],
                "service_p":row[3],
                "service_price":row[4],
                "service_image_url":row[5]
            }
            for row in rows
        ]

        conn.close()


        return jsonify(services)
    except Exception as e:
        return jsonify({"error":str(e)}),500
    
    
@app.route('/order', methods=['POST'])
def create_order():
    data = request.json
    service_id = data.get('service_id')
    name = data.get('name')
    email = data.get('email')
    phone = data.get('phone')
    details = data.get('details')

    # Підключення до бази даних
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO orders (service_id, name, email, phone, details)
        VALUES (?, ?, ?, ?, ?)
    ''', (service_id, name, email, phone, details))

    conn.commit()
    conn.close()

    return jsonify({"message": "Order successfully created"}), 200
if __name__ == "__main__":
    app.run(debug=True)
