class Insta:
    def __init__(self,user_name,user_id,user_age,user_email,user_password):
        self.user_name = user_name
        self.user_id = user_id
        self.user_age = user_age
        self.user_emai = user_email
        self.user_password = user_password

    def update_username(self,new_username):
        user_name = new_username
        print("User name added successfully")


u1 = Insta("Prateek","cr7",18,"prateek53@gmail.com","PR7")
print(u1.__dict__)
Insta.update_username("Abhijeet",18)
print(u1.__dict__)