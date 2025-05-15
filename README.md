# 🌿 Greenguard - Deteksi Penyakit Daun Cabai

Greenguard adalah aplikasi berbasis [Streamlit](https://streamlit.io) yang digunakan untuk mendeteksi jenis penyakit pada daun tanaman cabai dari gambar yang diunggah. Saat ini aplikasi menggunakan prediksi **dummy** untuk simulasi, dan cocok untuk pengembangan lebih lanjut dengan model AI sesungguhnya.

---

## 🚀 Fitur

- Upload gambar daun cabai (`.jpg`, `.jpeg`, `.png`)
- Klasifikasi dummy ke dalam 4 kategori penyakit:
  - ✅ Daun Sehat
  - ⚠️ Bercak Daun
  - ⚠️ Keriting
  - ❌ Busuk Daun
- Rekomendasi tindakan berdasarkan hasil prediksi
- Tampilan antarmuka interaktif menggunakan Streamlit

---

## 🛠️ Instalasi

1. **Clone repository ini** (jika belum):
   ```bash
   git clone https://github.com/username/greenguard.git
   cd greenguard
   ```

2. **Install dependensi**:
   ```bash
   pip install tensorflow
   pip install numpy
   pip install ttkbootsrap
   ```

3. **Jalankan aplikasi**:
   ```bash
   python main.py
   ```

---

## 📂 Struktur Proyek

```
greenguard/
├── greenguard.py      # Script utama aplikasi Streamlit
├── README.md          # Dokumentasi proyek
```

---

## 📌 Catatan

- Fungsi `predict()` saat ini menggunakan prediksi acak (random).
- Cocok untuk diintegrasikan dengan model CNN berbasis TensorFlow atau PyTorch di masa depan.

---

## 📃 Lisensi

Proyek ini bersifat open-source untuk keperluan edukasi dan penelitian.

---

## 🙌 Kontribusi

Pull request dan kontribusi sangat disambut! Silakan fork dan buat perbaikan sesuai kebutuhanmu.
