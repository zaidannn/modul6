# TODO 0: Import library lain yang dibutuhkan
from PIL import ImageDraw, ImageFont
from PIL import Image

# TODO 1: Lakukan load image pada variabel berikut
# hint: kalian bisa gunakan fungsi open()
gambarku = Image.open('C:\\Users\\acerc\\Downloads\\pre6\\assets\\hersummon 3.jpg')

# TODO 2: Ubah gambar menjadi hitam-putih
# hint: kalian bisa gunakan fungsi convert()
gambarBW = gambarku.convert('L')

# TODO 3: Tambahkan text dengan font Arial dan ukuran 24 sesuai kriteria
draw = ImageDraw.Draw(gambarBW)
font_path = 'C:\Users\\acerc\\Downloads\\pre6\\assets\\arial-font\\arial.ttf'  # Sesuaikan path dengan lokasi font Arial di komputer Anda
font = ImageFont.truetype(font_path, 45)
text = "gueh \n ayam"

# Menghitung ukuran teks menggunakan bounding box
text_bbox = draw.textbbox((0, 0), text, font=font)
text_width = text_bbox[2] - text_bbox[0]
text_height = text_bbox[3] - text_bbox[1]

text_x = (gambarBW.width - text_width) // 2
text_y = (gambarBW.height - text_height) // 2  # Letakkan teks di tengah gambar secara vertikal
draw.text((text_x, text_y), text, font=font, fill=255)

# TODO 4: Simpan gambar hasil edit menggunakan fungsi save()
imagenew = 'percobaan_satu.jpg'
gambarBW.save(imagenew)

# TODO 5: Tampilkan hasil akhir gambar
gambarBW.show()