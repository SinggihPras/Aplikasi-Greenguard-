import streamlit as st
import numpy as np
from PIL import Image

# --- Konfigurasi halaman ---
st.set_page_config(page_title="Greenguard - Deteksi Penyakit Daun Cabai", layout="centered")

# --- Judul Aplikasi ---
st.title("🌿 Greenguard")
st.subheader("Deteksi Penyakit Daun Tanaman Cabai dari Gambar")

# --- Label Kelas (Dummy) ---
CLASS_NAMES = ["Daun Sehat", "Bercak Daun", "Keriting", "Busuk Daun"]

# --- Fungsi Prediksi Dummy ---
def predict(image):
    image = image.resize((224, 224))  # Resize ke ukuran model
    img_array = np.array(image) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    # Prediksi acak (simulasi, ganti dengan model asli jika sudah ada)
    predicted_class = np.random.choice(CLASS_NAMES)
    return predicted_class

# --- Upload Gambar ---
uploaded_file = st.file_uploader("📤 Unggah gambar daun cabai", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Tampilkan gambar
    image = Image.open(uploaded_file)
    st.image(image, caption="🖼️ Gambar yang Diunggah", use_column_width=True)

    # Proses prediksi
    with st.spinner("🔎 Mendeteksi penyakit..."):
        prediction = predict(image)
        st.success(f"🩺 Hasil Deteksi: **{prediction}**")

        # --- Rekomendasi berdasarkan hasil ---
        if prediction == "Daun Sehat":
            st.info("✅ Daun tampak sehat, tidak ditemukan gejala penyakit.")
        elif prediction == "Bercak Daun":
            st.warning("⚠️ Bercak daun terdeteksi. Periksa kelembaban dan semprot fungisida alami.")
        elif prediction == "Keriting":
            st.warning("⚠️ Gejala keriting terdeteksi. Cek kemungkinan serangan hama seperti thrips.")
        elif prediction == "Busuk Daun":
            st.error("❌ Busuk daun terdeteksi. Pangkas bagian yang terinfeksi dan gunakan fungisida.")
else:
    st.info("Silakan unggah gambar daun cabai untuk dideteksi.")
