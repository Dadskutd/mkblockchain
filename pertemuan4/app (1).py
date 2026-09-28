import streamlit as st
from core import Blockchain

st.set_page_config(page_title="film", page_icon="🎬", layout="wide")
st.title("Hipelem 🎞️")

if 'my_blockchain' not in st.session_state:
    st.session_state.my_blockchain = Blockchain()

st.sidebar.header("Tambahkan data Film")

genre = st.sidebar.selectbox("Genre Film:", ["Action", "Comedy", "Drama", "Horror", "Romance", "Sci-Fi", "Thriller", "Documentary"])
film = st.sidebar.text_input("Nama Film:")
sutradara = st.sidebar.text_input("Sutradara:")
durasi = st.sidebar.text_input("Durasi (jam):")
sinopsis = st.sidebar.text_area("Sinopsis:")

if st.sidebar.button("Tambah Data"):
    if film and sutradara and durasi:
        data_transaksi = f"Nama film: {film}, Sutradara: {sutradara}, Durasi: {durasi}, Sinopsis: {sinopsis}, Genre: {genre}"
        st.session_state.my_blockchain.add_block(data_transaksi)
        st.sidebar.success("Film berhasil ditambahkan ke data")
    else:
        st.sidebar.error("Harap isi semua field sebelum menambahkan data")

st.subheader("Data Film di Hipelem")

is_valid = st.session_state.my_blockchain.is_chain_valid()
if is_valid:
    st.success("✅ film berhasil ditambahkan ke data")
else:
    st.error("❌ film tidak valid")

for block in st.session_state.my_blockchain.chain:
    with st.expander(f"Block {block.index} | Hash {block.hash[:15]}..."):
        col1, col2 = st.columns(2)
        with col1:
            st.write("**Data Payload**")
            st.info(block.data)
            st.write(f"**Timestamp:** {block.timestamp_readable}")

        with col2:
            st.write("**Kriptografi:**")
            st.write("**Hash saat ini:**")
            st.code(block.hash, language='python')
            st.write("**Hash sebelumnya (pointer):**")
            st.code(block.prev_hash, language='python')