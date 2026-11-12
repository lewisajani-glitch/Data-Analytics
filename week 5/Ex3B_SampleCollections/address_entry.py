# Create a dictionary with the contact's mailing information.
contact_info = {
    "name": "Taylor Reed",
    "address": "123 Example Street",
    "city": "Philadelphia",
    "state": "PA",
    "zip": "19103"
}

# Print the original mailing address using one multi-line f-string.
print(f"""{contact_info['name']}
{contact_info['address']}
{contact_info['city']}, {contact_info['state']} {contact_info['zip']}""")

# Remove the original name entry from contact_info.
del contact_info["name"]

# Store the first and last name in a separate dictionary.
full_name = {
    "first name": "Taylor",
    "last name": "Reed"
}

# Add an honorific to the full_name dictionary.
full_name.update({"honorific": "Dr."})

# Add the full_name dictionary to contact_info.
contact_info.update({"full_name": full_name})

# Print the updated mailing address, including the honorific and full name.
print(f"""{contact_info['full_name']['honorific']} {contact_info['full_name']['first name']} {contact_info['full_name']['last name']}
{contact_info['address']}
{contact_info['city']}, {contact_info['state']} {contact_info['zip']}""")
