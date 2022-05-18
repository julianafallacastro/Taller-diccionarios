usuarios = {
        "iperurena": {
            "nombre": "Iñaki",
            "apellido": "Perurena",
            "password": "123123"
    },
        "fmuguruza": {
            "nombre": "Fermín",
            "apellido": "Muguruza",
            "password": "654321"
    },
        "aolaizola": {
            "nombre": "Aimar",
            "apellido": "Olaizola",
            "password": "123456"
    }
 }
User = input("Escriba su usuario: ")    
Pass = input("Escriba su password: ") 
intentos = 3

while(User not in usuarios.keys() or Pass != usuarios[User]["password"]):
    intentos = intentos - 1
    print(f"Acceso fallido, te quedan {intentos} intentos")

    User = input("Escriba su usuario: ") 
    Pass = input("Escriba su password: ")

    if intentos == 0:
        print("Acceso fallido, te quedaste sin intentos")
        break 

if User in usuarios.keys() and Pass == usuarios[User]["password"]:
    print({"nombre", "apellido"}) 