from dash_package import db
class Listing(db.Model):
    __tablename__ = 'listings'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.Text)
    housing = db.Column(db.Text)
    neighborhood = db.Column(db.Text)
    price = db.Column(db.Integer)

    @classmethod
    def most_expensive(cls):
        pass


# session.query(Listing).all()
# Listing.query.all()
# Listing.query.filter_by()
