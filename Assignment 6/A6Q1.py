class Password_Manager:
    def __init__(self):
            self.old_passwords=[]
    def get_password(self):
        if self.old_passwords:
            return self.old_passwords[-1]
        else:
            return None 
    def set_password(self, new_password):
        while new_password in self.old_passwords:
            print("This password has been used before. Choose a different one.")
        self.old_passwords.append(new_password)
        print("Password set successfully!")
    def is_correct(self, password_to_check):
        return self.get_password()==password_to_check
def menu():
    print("Enter 'set' to set a new password")
    print("Enter 'current' to see your current password")
    print("Enter 'verify' to verify your password")
    choice=input("Enter 'exit' to exit:")
    return choice
def main():
    pm=Password_Manager()
    password=input("Enter password:")
    pm.set_password(password)
    choice=menu()
    while choice!='exit':
        if choice=='set':
            password=input("Enter password:")
            pm.set_password(password)
        if choice=='current':
            print("Current password is:",pm.get_password())
        if choice=='verify':
            password=input("Enter password:")
            if pm.is_correct(password):
                print("Password is correct.")
            else:
                print("Password is incorrect.")
        choice=menu()
if __name__=='__main__':
    main()