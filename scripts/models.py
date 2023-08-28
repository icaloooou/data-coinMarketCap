from extract_n_load import db

class History(db.Model):
    __tablename__ = "history"

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float, nullable=False)
    time = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(100), nullable=False)

    def __init__(self, price, time, date):
        self.price = price
        self.time = time
        self.date = date

class Candles(db.Model):
    __tablename__ = 'candles'

    id = db.Column(db.Integer, primary_key=True)
    high = db.Column(db.Float, nullable=False)
    low = db.Column(db.Float, nullable=False)
    open = db.Column(db.Float, nullable=False)
    close = db.Column(db.Float, nullable=False)
    volume = db.Column(db.Float, nullable=False)
    marketCap = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    month = db.Column(db.Integer, nullable=False)
    day = db.Column(db.Integer, nullable=False)

    def __init__(self, high, low, open, close, volume, marketCap, year, month, day):
        self.high = high
        self.low = low
        self.open = open
        self.close = close
        self.volume = volume
        self.marketCap = marketCap
        self.year = year
        self.month = month
        self.day = day