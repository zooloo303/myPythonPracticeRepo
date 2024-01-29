customer = {
    "name": "Neil Ward",
    "age": 50,
    "marriage_status": True
}

print(customer["name"])
print(customer.get("name"))
#create a key/valu pair in te dictionary with a default value
print(customer.get("birthdate", "Jan 27 1974"))

# change a value in a "dictionary"
customer["name"] = "Debbie Ward"
print(customer)