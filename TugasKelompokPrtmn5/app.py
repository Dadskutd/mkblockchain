import streamlit as st  # cite: 2
from core import Block, Blockchain  # cite: 2

st.set_page_config(page_title="Supply Chain Kopi", page_icon="☕")  # cite: 2
st.title("☕ Sistem Pelacakan Rantai Pasok Kopi")  # cite: 2

if "kopi_chain" not in st.session_state:  # cite: 2
    st.session_state.kopi_chain = Blockchain()  # cite: 2

data_kopi = st.text_input(
    "Masukkan Data Pengiriman (Misal: '100kg - Petani A'):"
)  # cite: 2
if st.button("⛏️ Mine Block (Tambah Data)"):  # cite: 2
    if data_kopi:  # cite: 2
        new_index = len(st.session_state.kopi_chain.chain)  # cite: 2
        new_block = Block(new_index, data_kopi, "")  # cite: 2

        # Streamlit Spinner untuk efek loading saat proses PoW berlangsung  # cite: 2
        with st.spinner("Sedang mencari Hash yang tepat (Mining)..."):  # cite: 2
            st.session_state.kopi_chain.add_block(new_block)  # cite: 2

        st.success(
            "Blok berhasil ditambang dan diamankan ke dalam rantai!"
        )  # cite: 2

# --- FITUR BARU: Validasi Rantai ---  # cite: 2
st.markdown("---")  # cite: 2
if st.button("🛡️ Cek Integritas Rantai"):  # cite: 2
    if st.session_state.kopi_chain.is_chain_valid():  # cite: 2
        st.success("Status Jaringan: AMAN (Rantai Valid)")  # cite: 2
    else:  # cite: 2
        st.error(
            "Status Jaringan: BAHAYA (Data telah dimanipulasi!)"
        )  # cite: 2
st.markdown("---")  # cite: 2

st.subheader("📜 Buku Besar (Ledger)")  # cite: 2
for block in st.session_state.kopi_chain.chain:  # cite: 2
    with st.expander(
        f"Blok #{block.index} - Hash: {block.hash[:15]}..."
    ):  # cite: 2
        st.write(f"**Waktu:** {block.timestamp}")  # cite: 2
        st.write(f"**Data:** {block.data}")  # cite: 2
        # FITUR BARU: Menampilkan Nonce  # cite: 2
        st.write(f"**Nonce (Tebakan):** {block.nonce}")  # cite: 2
        st.write(f"**Prev Hash:** {block.previous_hash}")  # cite: 2
        # FITUR BARU: Menyoroti Hash yang sudah sesuai Difficulty  # cite: 2
        st.info(f"**Hash:** {block.hash}")  # cite: 2