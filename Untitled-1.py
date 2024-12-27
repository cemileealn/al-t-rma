
from abc import ABC, abstractmethod # python içerisinde bulunan abstract modülü import ediyoruz

class UlasimAraci(ABC):  # Soyut sınıf
    @abstractmethod
    def calis(self):
        pass  

    @abstractmethod
    def durdur(self):
        pass


class Araba(UlasimAraci):
    def calis(self):
        print("Arabayı anahtarla çalıştırdım.")

    def durdur(self):
        print("Arabayı durdurdum.")

class Bisiklet(UlasimAraci):
    def calis(self):
        print("Bisikleti pedal çevirerek çalıştırdım.")

    def durdur(self):
        print("Bisikleti durdurdum.")


araba = Araba()
araba.calis()  
araba.durdur()    

bisiklet = Bisiklet()
bisiklet.calis()  
bisiklet.durdur()    
