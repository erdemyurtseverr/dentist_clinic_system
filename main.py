import sqlite3

connection=sqlite3.connect("clinic.db")
cursor=connection.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS clinic (
               id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
               name TEXT NOT NULL,
               surname TEXT NOT NULL,
               address TEXT NOT NULL,
               age INTEGER NOT NULL,
               problem TEXT NOT NULL,
               phone_number TEXT NOT NULL UNIQUE
               )""")
connection.commit()

print("Diş hekimliği hasta sorgulama,kayıt ekranına hoşgeldiniz.")
print("""Lütfen işlem numarası giriniz
    1-Hasta kaydetme
    2-Hasta kayıt sorgulama
    3-Çıkış
      """)


def add_client(name,surname,address,age,problem,phone_number):
    if not phone_number.isdigit() or len(phone_number)!=11:
        print("Telefon numarası geçersiz!")
        return
    cursor.execute("""
    INSERT INTO clinic (name,surname,address,age,problem,phone_number)
    VALUES (?,?,?,?,?,?)
    """, (name,surname,address,age,problem,phone_number)
                   )

    connection.commit()
def find_client_by_phonenumber(phone_number):
    cursor.execute("""
    SELECT * FROM clinic
    WHERE phone_number=?
    """, (phone_number,))
    hasta=cursor.fetchone()
    if hasta:
        print("""Hasta bulundu:
        --------------------------
        id= {}
        isim= {}
        soyisim= {}
        adres= {}
        yaş= {}
        şikayet= {}
        telefon numarası= {}
        --------------------------
              """.format(
            hasta[0],hasta[1],hasta[2],hasta[3],
            hasta[4],hasta[5],hasta[6]
        ))
    else:
        print("Hasta bulunamadı")
while True:
    try:
        islem=int(input("Lütfen işlem numarasını giriniz:"))

    except ValueError:
        print("Lütfen tam sayı giriniz.")
        continue
    if  islem==1:
        name=input("İsim?")
        surname=input("Soyisim?")
        address=input("Adres?")
        try :
            yas=int(input("Age?"))
        except ValueError:
            print("Yaş tam sayı olmalıdır.")
            continue

        problem=input("Problem?")

        phone_number=input("Telefon?")

        add_client(name,surname,address,yas,problem,phone_number)
    elif islem==2:
        phone_number=input("Telefon numarası?")
        find_client_by_phonenumber(phone_number)


    elif islem==3:
        print("Çıkış yapılıyor...")
        break
    else:
        print("Geçersiz seçim")
        continue
connection.close()