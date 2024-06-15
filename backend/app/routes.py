from flask import render_template, request, redirect, url_for, session, Blueprint, jsonify, Flask
from flask_login import login_required

from models import FinancialData, User, db
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.innit_app(app)

CORS(app)
@app.route('/dashboard')
@login_required
def dashboard():
    user_id = session.get('user_id')
    financial_data = FinancialData.query.filter_by(user_id=user_id).all()
    return render_template('dashboard.html', financial_data=financial_data)

@app.route('/add_data', methods=['GET', 'POST'])
@login_required
def add_data():
    if request.method == 'POST':
        new_data = FinancialData(
            revenue=request.form['revenue'],
            gross_profit=request.form['gross_profit'],
            net_income=request.form['net_income'],
            user_id=session['user_id']
        )
        db.session.add(new_data)
        db.session.commit()
        return redirect(url_for('dashboard'))
    return render_template('add_data.html')

@app.route('/delete_data/<int:data_id>', methods=['POST'])
@login_required
def delete_data(data_id):
    data = FinancialData.query.get_or_404(data_id)
    db.session.delete(data)
    db.session.commit()
    return redirect(url_for('dashboard'))

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/financial-data', methods=['GET'])
def get_financial_data():
    try:
        financial_data = FinancialData.query.all()
   
        financial_data_list = [
            {
                'id': data.id,
                'revenue': data.revenue,
                'gross_profit': data.gross_profit,
                'net_income': data.net_income,
                'user_id': data.user_id
            }
            for data in financial_data
        ]
        return jsonify(financial_data_list)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
