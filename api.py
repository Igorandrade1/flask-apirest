from flask import Flask, request

app = Flask(__name__)
# permitir caracters utf8
app.config['JSON_AS_ASCII'] = False

# fonte de dados
users_data = {
    1: {
        "id": 1,
        "name": "joão"
    },
    2: {
        "id": 2,
        "name:": "Ana"
    }

}


# resposta dos usuarios da fonte de dados
def response_users():
    return {"users": list(users_data.values())}


# rota
@app.route("/")
def root():
    return "<h1>API com Flask</h1>"


# retornar usuarios via api
@app.route('/users')
def list_users():
    return response_users()


@app.route('/users', methods=["POST"])
def create_user():
    body = request.json

    ids = list(users_data.keys())

    if ids:
        new_id = ids[-1] + 1
    else:
        new_id = 1

    users_data[new_id] = {
        "id": new_id,
        "name": body["name"]
    }

    return response_users()


@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete(user_id: int):
    user = users_data.get(user_id)

    if user:
        del users_data[user_id]

    return response_users()


@app.route("/users/<int:user_id>", methods=["PUT"])
def update(user_id: int):
    body = request.json
    name = body.get("name")

    if user_id in users_data:
        users_data[user_id]["name"] = name

    return response_users()


app.run(debug=True)
