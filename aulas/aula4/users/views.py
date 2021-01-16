from flask import jsonify

users_database = [{"name": "Matheus", "email": "matheusgiga123@gmail.com"}]


def users_app(users):
    @users.route("/")
    def index():
        return jsonify(users_database)
