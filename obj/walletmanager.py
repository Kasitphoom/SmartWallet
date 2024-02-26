from obj.account import Account
class WalletManager():
    def __init__(self, account: Account):
        self.account = account
    
    def get_account_number_non_visible(self):
        return f"XXX-X-{str(self.get_account_number())[4:8]}-X"
    
    def get_account_number(self):
        return self.account.getID()
    
    def get_account_number_visible(self):
        return f"{str(self.get_account_number())[:3]}-{str(self.get_account_number())[3]}-{str(self.get_account_number())[4:8]}-{str(self.get_account_number())[8:]}"