# contacts.py

# We will store contacts in a simple list (temporary in-memory database)
contacts = []

def add_contact(name, phone, email):
    contact = {
        "id": len(contacts) + 1,
        "name": name,
        "phone": phone,
        "email": email
    }
    contacts.append(contact)
    return contact

def get_all_contacts():
    return contacts

def get_contact(contact_id):
    for contact in contacts:
        if contact["id"] == contact_id:
            return contact
    return None

def update_contact(contact_id, name=None, phone=None, email=None):
    contact = get_contact(contact_id)
    if contact:
        if name: contact["name"] = name
        if phone: contact["phone"] = phone
        if email: contact["email"] = email
        return contact
    return None

def delete_contact(contact_id):
    global contacts
    new_list = [c for c in contacts if c["id"] != contact_id]
    deleted = len(contacts) != len(new_list)
    contacts = new_list
    return deleted
