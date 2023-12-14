import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Membaca dan menampilkan gambar
img = mpimg.imread('D:\\Kerja\\Kuliah\\WW\\SEM5\\PemrogramanFungsional\\Praktikum\\Week6\\pre6\\assets\\pakenanya.jpg') #Sesuaikan dengan direktori letak gambar tersimpan
plt.imshow(img)
plt.axis('off') # Tidak menampilkan sumbu koordinat
plt.show()
