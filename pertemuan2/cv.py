import streamlit as st
#pembuatan title halaman
st.set_page_config(page_title="CV digital Mahasiswa")

#pembuatan sidebar
st.sidebar.title ("pengaturan profile")
st.sidebar.write("Masukkan data diri Anda di bawah ini:")

#ketikan
nama = st.sidebar.text_input("Nama Lengkap", "")
nim = st.sidebar.text_input("NIM", "")
jurusan = st.sidebar.text_input("Jurusan", "")
foto_profil = st.sidebar.file_uploader("Unggah Foto Profil (Opsional)", type=['png', 'jpg'])
deskripsi = st.sidebar.text_area("Deskripsi Singkat (Bio)", "")
pengalaman = st.sidebar.text_area("Pengalaman organisasi", "")

sertifikat = st.sidebar.checkbox("apakah kamu punya sertifikat")
if sertifikat:
    st.success("Sertifikat berhasil ditambahkan")
    sertifikat = st.sidebar.text_area("masukkan sertifikat", "")
else:
    st.markdown("")



#area utama
st.title("Curiculum Vitae")
st.markdown("---------")

kolom_kiri, kolom_kanan = st.columns([4, 1])
with kolom_kiri :
    st.header(nama)
    st.markdown(f"{jurusan} | NIM: {nim} ")
    st.markdown("##### Pengalaman Organisasi")
    st.markdown(pengalaman.replace("\n", "  \n"))
    if sertifikat:
        st.markdown("### sertifikat")
    if sertifikat:
        st.markdown(sertifikat.replace("\n", " \n"))
    


with kolom_kanan:
    if foto_profil is not None:
        st.image(foto_profil, width=200, caption="Foto Profil")
    else:
        st.info("Belum ada foto yang diunggah.")

    st.write(f"tentang saya : {deskripsi}")

# - BAGIAN KEAHLIAN (SKILLS) -
st.markdown("### Keahlian Teknis")
# Sidebar slider untuk mengatur level skill
st.sidebar.markdown(" -------")
st.sidebar.subheader("Atur Kemahiran Skill")
skill_python = st.sidebar.slider("Python", 0, 100, 80)
skill_web = st.sidebar.slider("Web Development", 0, 100, 60)
skill_db = st.sidebar.slider("Database", 0, 100, 70)

# Menampilkan indikator visual (Progress Bar) di halaman utama
st.write(" *Python *")
st.progress(skill_python)
st.write(" *Web Development (HTML/CSS) *")
st.progress(skill_web)
st.write(" *Database (SQL) *")
st.progress(skill_db)

# - BAGIAN KONTAK -
st.markdown("### 🪪 Hubungi Saya")

with st.expander("Klik untuk melihat detail kontak"):
    st.write(f"📧 Email: raishakim847@gmail.com")
    st.write("🐙 GitHub: https://github.com/Putrarais")


data_cv = f"Nama: {nama}\nNIM: {nim}\nJurusan: {jurusan}"
st.download_button(label="📥 Download Data CV", data=data_cv, file_name="cv_app.txt")