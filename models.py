from app import db

class Task(db.Model): # we create our Task model which inherits from db instance model
    id = db.Column(db.Integer, primary_key=True) #auto managed
    title = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False)

    def __repr__(self): # overwrite the print
        return f'{self.title} created on {self.date}'
