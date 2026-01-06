PYTHON_LESSONS = [
    {
        "title": "Variabel & Tipe Data",
        "content": """
Di Python, variabel digunakan untuk menyimpan data.
Contoh:
nama = "Manus"  # String
umur = 25       # Integer
pi = 3.14       # Float

Python adalah bahasa 'dynamically typed', artinya Anda tidak perlu 
mendeklarasikan tipe data secara eksplisit.
        """,
        "quiz": {
            "question": "Manakah cara penulisan variabel string yang benar?",
            "options": ["A. x = 5", "B. x = 'Halo'", "C. x = True"],
            "answer": "B"
        }
    },
    {
        "title": "Struktur Kontrol (If-Else)",
        "content": """
If-Else digunakan untuk mengambil keputusan.
Contoh:
if umur >= 18:
    print("Dewasa")
else:
    print("Anak-anak")

Penting: Python menggunakan indentasi (spasi) untuk menentukan blok kode!
        """,
        "quiz": {
            "question": "Apa yang digunakan Python untuk menentukan blok kode?",
            "options": ["A. Kurung kurawal {}", "B. Titik koma ;", "C. Indentasi (Spasi)"],
            "answer": "C"
        }
    },
    {
        "title": "Perulangan (Loops)",
        "content": """
For loop digunakan untuk mengulang sesuatu.
Contoh:
for i in range(5):
    print(i)

Ini akan mencetak angka 0 sampai 4.
        """,
        "quiz": {
            "question": "Apa hasil dari range(3)?",
            "options": ["A. 0, 1, 2", "B. 1, 2, 3", "C. 0, 1, 2, 3"],
            "answer": "A"
        }
    }
]

TYPING_TEXTS = [
    "print('Hello World')",
    "for i in range(10): print(i)",
    "def hitung_luas(p, l): return p * l",
    "if x > 0: print('Positif') else: print('Negatif')",
    "my_list = [1, 2, 3, 4, 5]",
    "class Mobil: def __init__(self): pass"
]
