import pyautogui
import os

# Path relatif dari file gambar
lokasi_simpan = os.path.join('Automation','assets','follow.png')

# Ambil tangkapan layar dan simpan ke file
pyautogui.locateOnScreen(lokasi_simpan,confidence=0.8)

if lokasi_simpan is not None:
    print("Lokasi Ditemukan")
else:
    print("Maaf kapten misi gagal location tidak ditemukan")
