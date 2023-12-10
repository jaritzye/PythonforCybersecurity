import random
import string
import requests
import hashlib

# Function to generate a password
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

# Function to check password security using HaveIBeenPwned API
def check_password_security(password):
    sha1_hash = hashlib.sha1(password.encode()).hexdigest().upper()
    prefix, suffix = sha1_hash[:5], sha1_hash[5:]
    url = f"https://api.pwnedpasswords.com/range/{prefix}"

    try:
        response = requests.get(url)
        hashes = response.text.splitlines()
        return suffix not in hashes
    except requests.exceptions.RequestException as e:
        print(f"Error checking password against HaveIBeenPwned API: {e}")
        return False

# Main function
def main():
    password_length = 12
    generated_password = generate_password(length=password_length)

    if generated_password:
        print(f"Generated Password: {generated_password}")

        if check_password_security(generated_password):
            print("Password is secure!")
        else:
            print("Password is compromised. Please generate a new one.")
    else:
        print("Password generation failed.")

# Run the main function
if __name__ == "__main__":
    main()
