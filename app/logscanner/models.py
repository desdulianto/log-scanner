from app import db


class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    timestamp = db.Column(db.DateTime)
    sip = db.Column(db.String(16))
    method = db.Column(db.String(10))
    uri = db.Column(db.String(4096))
    query = db.Column(db.String(4096))
    sport = db.Column(db.Integer)
    username = db.Column(db.String(256))
    cip = db.Column(db.String(16))
    useragent = db.Column(db.String(1024))
    referer = db.Column(db.String(4096))
    status = db.Column(db.Integer)
    substatus = db.Column(db.Integer)
    win32status = db.Column(db.Integer)
    timetaken = db.Column(db.Integer)
    country = db.Column(db.String(128))

    def __repr__(self):
        return '<Entry: {}>'.format(self.cip)


class Attack(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    entry_id = db.Column(db.Integer, db.ForeignKey('entry.id'))
    entry = db.relationship('Entry', backref=db.backref('attacks', lazy=True))
    ip = db.Column(db.String(16))
    type = db.Column(db.String(10))
    country = db.Column(db.String(128))

    def __repr__(self):
        return '<Attack: {} - {}>'.format(self.ip, self.type)
