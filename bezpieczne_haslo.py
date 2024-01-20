import secrets  
import string

def bezpieczne_haslo():
    dlugosc = 10
    zestaw = string.ascii_letters + string.digits + string.punctuation
    haslo = "".join(secrets.choice(zestaw) for i in range(dlugosc))
    
    print(haslo)
    
bezpieczne_haslo()
