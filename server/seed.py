#!/usr/bin/env python3

from config import app, db
from models import User
from faker import Faker

faker = Faker()

if __name__ == '__main__':
    with app.app_context():
        print("Seeding database...")

        User.query.delete()

        u1 = User(username="Chett")
        u2 = User(username="Sakib")
        u3 = User(username="Ricardo")
        u4 = User(username="Ben")

        db.session.add_all([u1, u2, u3, u4])
        db.session.commit()

        print("NOTE -- YOU MAY NEED TO ADJUST THE SEED DATA WHEN YOU ADD VALIDATIONS....")

        print("Seeding complete!")