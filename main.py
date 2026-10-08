ismlar=("asadbek","diyor","ali","vali","sanjar")
takrorlanishlar_soni=1

for ism in ismlar:
    print(f"oshga kel {ism}")
    takrorlanishlar_soni += 1
    print(f"Kod {takrorlanishlar_soni} marta takrorlandi")

toq_sonlar =  list(range(11, 100, 2))

for son in toq_sonlar:
    kubi=son**3
    print(kubi)
cars=['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
    if car != ('gm'):
        print(car.title())
    else:
        print(car.upper())
login=input("Login ismingizni kiriting: ")
if login.lower() == "admin":
    print("Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?")
else:
    print(f"Xush kelibsiz, {login}!")

son1 = float(input("Birinchi sonni kiriting: "))
son2 = float(input("Ikkinchi sonni kiriting: "))
if son1 == son2:
    print("Sonlar teng")
son = float(input("Istalgan son kiriting: "))

if son < 0:
    print("Manfiy son")
else:
    print("Musbat son")
son = float(input("Son kiriting: "))

if son >= 0:
    ildiz = son ** 0.5
    print(f"Sonning ildizi: {ildiz}")
else:
    print("Musbat son kiritimg")