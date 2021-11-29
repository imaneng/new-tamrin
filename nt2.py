import uuid
class MainUser:
    type = None
    file_name = None
    file_path = None


    def __init__(self, username, tel, address):
        self.username = username
        self.tel = tel
        self.address = address
        self.purchase_history = []
        self.status = False  # ordinary user


class UserAdmin(MainUser):
    type = "admin"
    file_name = "admins.db"
    file_path = settings.USER_DATA_PATH / file_name

    def __init__(self, username, tel, passw):
        super().__init__(username, tel)
        self.status = True
        self.passw = passw

    def add_user(self):
        pass

class Users(MainUser):

    type = "user"
    file_name = "users.db"
    file_path = settings.USER_DATA_PATH / file_name

    def __init__(self, username, tel, address):
        super().__init__(username, tel, address)


    def add_user(self):
        pass


class Product:
    _id = 100

    _category = ['Food', 'Drink', 'Service', 'Zarf']

    def __init__(self, name, price, category):
        self.id = Product.id_gen()
        self.serial_num = uuid.uuid4()
        self.name = name
        self.price = price
        self.category = category

    
    @staticmethod
    def id_gen():
        Product._id += 1
        return Product._id
