from dotenv import load_dotenv
import os

load_dotenv()
app_name = os.getenv("APP_NAME", "Flask App")



from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
from contact_api.contacts import(
    add_contact, get_all_contacts, get_contact,
    update_contact, delete_contact
)

# Load environment variables
load_dotenv()

app = Flask(app_name)

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")


@app.route("/")
def home():
    return jsonify({"message": "Contact API is running"})


# CREATE a new contact
@app.route("/contacts", methods=["POST"])
def create_contact():
    data = request.json
    name = data.get("name")
    phone = data.get("phone")
    email = data.get("email")

    contact = add_contact(name, phone, email)
    return jsonify(contact), 201


# READ all contacts
@app.route("/contacts", methods=["GET"])
def read_contacts():
    return jsonify(get_all_contacts())


# READ a single contact
@app.route("/contacts/<int:contact_id>", methods=["GET"])
def read_contact(contact_id):
    contact = get_contact(contact_id)
    if not contact:
        return jsonify({"error": "Contact not found"}), 404
    return jsonify(contact)


# UPDATE a contact
@app.route("/contacts/<int:contact_id>", methods=["PUT"])
def update_contact_route(contact_id):
    data = request.json
    updated = update_contact(
        contact_id,
        name=data.get("name"),
        phone=data.get("phone"),
        email=data.get("email")
    )
    if not updated:
        return jsonify({"error": "Contact not found"}), 404
    return jsonify(updated)


# DELETE a contact
@app.route("/contacts/<int:contact_id>", methods=["DELETE"])
def delete_contact_route(contact_id):
    deleted = delete_contact(contact_id)
    if not deleted:
        return jsonify({"error": "Contact not found"}), 404
    return jsonify({"message": "Contact deleted"})


if __name__ == "__main__":
    app.run(debug=True)


