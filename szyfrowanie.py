import base64

def szyfrowanie():
    wiadomosc_do_szyfr = input("wprowadz tekst: ")
    szyfrowanie_ascii = wiadomosc_do_szyfr.encode('ascii')
    szyfrowanie_base64 = base64.b64encode(szyfrowanie_ascii)
    zaszyfrowana_wiad = szyfrowanie_base64.decode('ascii')
    
    print(zaszyfrowana_wiad)
    
szyfrowanie()
