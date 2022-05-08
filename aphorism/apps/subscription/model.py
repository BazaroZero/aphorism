from aphorism import db


subscriptions = db.Table(
    "subscriptions",
    db.Column("subscriber_id", db.Integer, db.ForeignKey("user.id", ondelete='CASCADE'), primary_key=True),
    db.Column("publisher_id", db.Integer, db.ForeignKey("user.id", ondelete='CASCADE'), primary_key=True),
)
