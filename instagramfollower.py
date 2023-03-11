from InstagramAPI import InstagramAPI

# List of accounts to use for following
accounts = [
    {"username": "account1", "password": "password1"},
    {"username": "account2", "password": "password2"},
    {"username": "account3", "password": "password3"},
    # Add more accounts as needed
]

# User ID of the person to follow
user_id = "123456789" # Replace with the user ID of the person you want to follow

# Loop through the accounts and follow the user
for account in accounts:
    # Initialize the InstagramAPI object with the current account's username and password
    api = InstagramAPI(account["username"], account["password"])
    api.login()

    # Follow the user with the specified ID
    api.follow(user_id)

    # Check if the follow was successful
    result = api.LastJson
    if result['status'] == 'ok':
        print(f"{account['username']} followed user successfully!")
    else:
        print(f"Error following user with {account['username']}.")
