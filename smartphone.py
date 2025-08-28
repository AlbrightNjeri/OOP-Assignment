# Parent class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def device_info(self):
        return f"{self.brand} {self.model}"


# Child class inheriting from Device
class Smartphone(Device):
    def __init__(self, brand, model, storage, camera):
        super().__init__(brand, model)  # Call parent constructor
        self.storage = storage
        self.camera = camera

    # Method
    def take_photo(self):
        return f"📸 Taking a photo with {self.camera}MP camera"

    # Encapsulation example (private variable)
    def __secret_feature(self):
        return "Hidden Developer Mode 🔒"

    def reveal_secret(self):
        return self.__secret_feature()


# Create objects
phone1 = Smartphone("Samsung", "S24 Ultra", "512GB", 200)
phone2 = Smartphone("Apple", "iPhone 15 Pro", "256GB", 48)

print(phone1.device_info())
print(phone1.take_photo())
print(phone2.device_info())
print(phone2.reveal_secret())
