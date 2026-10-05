import streamlit as st
from core import TicketBlockchain

st.set_page_config(page_title="Ticket Traceability Blockchain", layout="wide")

# Inisialisasi session state agar data tersimpan saat ada aktivitas di UI
if 'ticketchain' not in st.session_state:
    st.session_state.ticketchain = TicketBlockchain()

st.title("🎟️ Traceability Tiket Konser Original")
st.write("Simulasi Verifikasi Keaslian & Riwayat Tiket Konser Menggunakan Hash Pointers")

st.divider()

# Mengambil data block paling baru
chain = st.session_state.ticketchain.chain
latest_block = chain[-1]

# Membagi layar menjadi 3 Kolom pas seperti layout tugas kamu (Input | Data Payload | Kriptografi)
col_input, col_payload, col_crypto = st.columns([1, 1.2, 1.2])

# --- KOLOM 1: INPUT DATA ---
with col_input:
    st.subheader("📥 Input Data Tiket")
    nama_pemilik = st.text_input("Nama Pemilik Tiket:")
    kategori_tiket = st.selectbox("Kategori Tiket:", ["VIP Direct Pass", "CAT 1 (Standing)", "CAT 2 (Seated)", "Tribune"])
    nomor_kursi = st.text_input("Nomor Kursi / Baris:", placeholder="Contoh: A-12")
    status_tiket = st.selectbox("Status Tiket:", [
        "Diterbitkan Promotor",
        "Telah Dibeli Pembeli Pertama",
        "Pindah Kepemilikan (Resell Resmi)",
        "Sudah Scanned / Used di Venue"
    ])

    if st.button("Tambah Block Tiket", use_container_width=True):
        if nama_pemilik and nomor_kursi:
            payload = {
                "nama_pemilik": nama_pemilik,
                "kategori_tiket": kategori_tiket,
                "nomor_kursi": nomor_kursi,
                "status_tiket": status_tiket
            }
            st.session_state.ticketchain.add_block(payload)
            st.success("Block Tiket Berhasil Ditambahkan!")
            st.rerun()
        else:
            st.error("Nama pemilik dan nomor kursi wajib diisi!")

# --- KOLOM 2: DATA PAYLOAD ---
with col_payload:
    st.subheader("📦 Data Payload")
    st.info(
        f"**Nama Pemilik:** {latest_block.data.get('nama_pemilik')}\n\n"
        f"**Kategori Tiket:** {latest_block.data.get('kategori_tiket')}\n\n"
        f"**Nomor Kursi:** {latest_block.data.get('nomor_kursi')}\n\n"
        f"**Status Tiket:** {latest_block.data.get('status_tiket')}\n\n"
        f"**Timestamp:** `{latest_block.timestamp}`"
    )

# --- KOLOM 3: KRIPTOGRAFI ---
with col_crypto:
    st.subheader("🔐 Kriptografi")
    st.text_input("Hash saat ini:", value=latest_block.hash, disabled=True, key=f"curr_{latest_block.index}")
    st.text_input("Hash sebelumnya (pointer):", value=latest_block.previous_hash, disabled=True, key=f"prev_{latest_block.index}")

st.divider()

# --- RIWAYAT KESELURUHAN BLOCK ---
st.subheader("📜 Riwayat Blok Kepemilikan Tiket")
for block in reversed(chain):
    with st.expander(f"🔗 Block #{block.index} - {block.data.get('nama_pemilik')} ({block.data.get('nomor_kursi')})"):
        c1, c2 = st.columns(2)
        with c1:
            st.write("**Detail Data Payload:**", block.data)
            st.write("**Waktu Didaftarkan:**", block.timestamp)
        with c2:
            st.code(f"Hash Saat Ini:\n{block.hash}")
            st.code(f"Hash Sebelumnya (Pointer):\n{block.previous_hash}")