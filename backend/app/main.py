from flask import Flask, jsonify
from models import User, FinancialData, db

from routes import dashboard, add_data, delete_data, get_financial_data, app



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)