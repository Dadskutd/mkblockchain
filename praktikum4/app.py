import streamlit as st
from core import Block, Blockchain

st.set_page_config(page_title="Supply Chain Perikanan", page_icon="🐟")
st.title("🐟 Sistem Pelacakan Rantai Pasok Seafood")

if "seafood_chain" not in st.session_state:
    st.session_state.seafood_chain = Blockchain()

data_tangkapan = st.text_input("Masukkan Data Tangkapan (Misal: '50kg Ikan Tuna - Nelayan A'):")

if st.button("⛏️ Mine Block (Tambah Data)"):
    if data_tangkapan:
        new_index = len(st.session_state.seafood_chain.chain)
        new_block = Block(new_index, data_tangkapan, "")
        
        with st.spinner("Sedang mencari Hash yang tepat (Mining)..."):
            st.session_state.seafood_chain.add_block(new_block)
            
        st.success("Blok berhasil ditambang dan diamankan ke dalam rantai!")

st.markdown("---")
if st.button("🛡️ Cek Integritas Rantai"):
    if st.session_state.seafood_chain.is_chain_valid():
        st.success("Status Jaringan: AMAN (Rantai Valid)")
    else:
        st.error("Status Jaringan: BAHAYA (Data telah dimanipulasi!)")
st.markdown("---")

st.subheader("📜 Buku Besar (Ledger)")
for block in st.session_state.seafood_chain.chain:
    with st.expander(f"Blok #{block.index} - Hash: {block.hash[:15]}..."):
        st.write(f"**Waktu:** {block.timestamp}")
        st.write(f"**Data:** {block.data}")
        st.write(f"**Nonce (Tebakan):** {block.nonce}")
        st.write(f"**Prev Hash:** {block.previous_hash}")
        st.info(f"**Hash:** {block.hash}")