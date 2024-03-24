# Python code to read a list of emails from a file and save only the names to another file

# Open the file with the list of emails
with open('listaEmails.txt', 'r') as emails_file:
    # Read all lines from the file
    emails = emails_file.readlines()

# Open the file to write the names
with open('listaNomes.txt', 'w') as names_file:
    # Iterate over each email
    for email in emails:
        # Split the email by '@' and get the first part (the name)
        name = email.split('@')[0]
        # Write the name to the file, followed by a newline
        names_file.write(name + '\n')

# Print a success message
print("Os nomes foram extraídos e salvos no arquivo listaNomes.txt com sucesso.")
