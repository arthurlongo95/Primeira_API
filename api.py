import requests
import streamlit as st

st.image("https://images.ctfassets.net/em6l9zw4tzag/oVfiswjNH7DuCb7qGEBPK/b391db3a1d0d3290b96ce7f6aacb32b0/python.png") 
st.title("Encontre a Letra da Música (v.1.0.0)")

def pesquisar_letra(banda, musica):
    endpoint = f"https://api.lyrics.ovh/v1/{banda}/{musica}"
    response = requests.get(endpoint)
    print(response.status_code)
    letra = response.json()["lyrics"] if response.status_code == 200 else ""
    return letra  


banda = st.text_input("Digite o nome da banda: ", key="banda")
musica = st.text_input("Digite o nome da música: ", key="musica")
pesquisar = st.button("Pesquisar")


if pesquisar:
    letra = pesquisar_letra(banda, musica)
    if letra:
        st.success("Música encontrada com sucesso!")
        st.text(letra)
    else:
        st.error("Letra não encontrada!")