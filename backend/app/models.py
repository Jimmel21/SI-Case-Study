from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def serialize(self):
        return{
            'id':self.id,
            'username':self.username,
            'password':self.password
        }

class FinancialData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    revenue = db.Column(db.Float, nullable=False)
    gross_profit = db.Column(db.Float, nullable=False)
    net_income = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('financial_data', lazy=True))

    def serialize(self):
        return{
            'id':self.id,
            'revenue':self.revenue,
            'gross_profit':self.gross_profit,
            'net_income':self.net_income,
            'user_id':self.user_id,
            'user':self.user
        }
