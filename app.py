from flask import Flask, request, jsonify
import sqlite3
from flask_cors import CORS
from database import save_order 
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

        
@app.route('/api/orders', methods=['POST'])
def create_order():
    try:
        data = request.get_json()  # Отримуємо дані з запиту
        print("Отримані дані:", data)
        service_name = data['service_name']
        user_name = data['user_name']
        email = data['email']
        phone = data['phone']
        details = data.get('details',None)

        # Зберігаємо замовлення в базі даних
        print(f"Saving order: {service_name}, {user_name}, {email}, {phone}, {details}")
        save_order(service_name, user_name, email, phone, details)

        return jsonify({'message': 'Order successfully created'}), 200
    except Exception as e:
        print("Помилка:", e)
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
