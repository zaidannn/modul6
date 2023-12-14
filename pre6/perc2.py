# TODO 0: Import beberapa library lain yang dibutuhkan
from PIL import Image

# TODO 1: Buka gambar latar belakang (background) dan gambar yang ingin
# disisipkan (overlay)
background_image = Image.open("D:\\Kerja\\Kuliah\\WW\\SEM5\\PemrogramanFungsional\\Praktikum\\Week6\\pre6\\assets\\pakenanya.jpg")
overlay_image = Image.open("D:\\Kerja\\Kuliah\\WW\\SEM5\\PemrogramanFungsional\\Praktikum\\Week6\\pre6\\assets\\KPSC.jpg")

# TODO 2: Konversi overlay image ke mode RGB (menghilangkan alpha channel)
overlay_image = overlay_image.convert("RGBA")

# TODO 3: (optional) Perkecil ukuran gambar overlay menggunakan method resize()
# Optional: Uncomment the line below if you want to resize the overlay image
#overlay_image = overlay_image.resize((new_width, new_height))

# Tentukan/Hitung koordinat tengah untuk menempatkan overlay
x_center = (background_image.width - overlay_image.width) // 2
y_center = (background_image.height - overlay_image.height) // 2

# TODO 4: Sisipkan gambar overlay ke dalam gambar background menggunakan
# method paste()
background_image.paste(overlay_image, (x_center, y_center), overlay_image)

# TODO 5: Simpan gambar hasil edit
background_image.save("hasil_edit.jpg")

# TODO 6: Tampilkan
background_image.show()
