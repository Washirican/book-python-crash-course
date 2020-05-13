# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-05-13
# --------------------------------------------------------------------------- #

from admin import Admin
from user import User

admin_1 = Admin('daniel', 'rodriguez', 'washirican', 'kirkland')
admin_1.greet_user()
admin_1.describe_user()
admin_1.privileges.show_privileges()

print("\nAdding admin privileges...")
admin_1.privileges.privileges = ['can add post', 'can delete post', 'can ban user']

admin_1.privileges.show_privileges()


print()
user_1 = User('andres', 'iniesta', 'el_mago', 'madrid')
user_1.greet_user()
user_1.describe_user()
