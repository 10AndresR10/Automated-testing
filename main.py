import random

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        """If username and password are valid, user can login successfully """
        if self.username == "admin" and self.password == "ABCD1234":
            return "Login successful"
        else:
            return "Invalid credentials"

class AdminUser(User):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    def __init__(self, username, password):
        super().__init__(username, password)
        self.admin_privileges = ["add_user", "delete_user", "view_users"]

    def reset_password(self):
        """When user need to reset password"""
        new_password = ""
        for _ in range(5):
            new_password += random.choice(self.letters)

        for _ in range(2):
            new_password += random.choice(self.numbers)

        for _ in range(2):
            new_password += random.choice(self.symbols)

        print(f"🔄 New password is: {new_password} for user '{self.username}'")

        self.password = new_password

class LoginTest:


    def test_login(self):
        """"Test for valid login functionality """
        user = User("admin", "ABCD1234")
        assert user.login() == "Login successful"
        print(f"✅ {user.username} - {user.login()}")

    def test_failed_login(self):
        """Test for valid login failed functionality"""
        user = User("admin", "ZXCVB0987")
        assert user.login() == "Invalid credentials"
        print(f"❌ {user.username} - {user.login()}")

    def test_reset_password(self):
        """Test for valid login failed functionality"""
        admin = AdminUser("admin_user", "somepass")
        admin.reset_password()



# Run test cases
test = LoginTest()
test.test_login()
test.test_failed_login()
test.test_reset_password()
