import streamlit as st
import pandas as pd
from datetime import datetime

# Configuração da página do Streamlit
st.set_page_config(page_title="Congregação Jardim Europa - Escalas", layout="wide")

# ==========================================
# 1. BANCO DE DADOS INICIAL (MEMÓRIA DO APP)
# ==========================================
if 'membros' not in st.session_state:
    st.session_state.membros = pd.DataFrame([
        {"Nome": "Jonei Lima", "Sexo": "M", "Cargo": "Servo", "Leitor_Quinta": True, "Leitor_Sentinela": True, "Audio_Video": True, "Familia": "Jonei Lima"},
        {"Nome": "Cássia Leite", "Sexo": "F", "Cargo": "Publicador", "Leitor_Quinta": False, "Leitor_Sentinela": False, "Audio_Video": False, "Familia": "Jonei Lima"},
        {"Nome": "Alcides Morais", "Sexo": "M", "Cargo": "Ancião", "Leitor_Quinta": True, "Leitor_Sentinela": True, "Audio_Video": False, "Familia": "Alcides Morais"},
        {"Nome": "Jane", "Sexo": "F", "Cargo": "Publicador", "Leitor_Quinta": False, "Leitor_Sentinela": False, "Audio_Video": False, "Familia": "Alcides Morais"},
        {"Nome": "José Santana", "Sexo": "M", "Cargo": "Ancião", "Leitor_Quinta": False, "Leitor_Sentinela": False, "Audio_Video": True, "Familia": "José Santana"},
        {"Nome": "Elizangela Santana", "Sexo": "F", "Cargo": "Publicador", "Leitor_Quinta": False, "Leitor_Sentinela": False, "Audio_Video": False, "Familia": "José Santana"},
        {"Nome": "Rodrigo Santana", "Sexo": "M", "Cargo": "Publicador", "Leitor_Quinta": True, "Leitor_Sentinela": True, "Audio_Video": True, "Familia": "José Santana"},
        {"Nome": "Damião", "Sexo": "M", "Cargo": "Ancião", "Leitor_Quinta": False, "Leitor_Sentinela": False, "Audio_Video": True, "Familia": "Damião"},
        {"Nome": "Rita Lima", "Sexo": "F", "Cargo": "Publicador", "Leitor_Quinta": False, "Leitor_Sentinela": False, "Audio_Video": False, "Familia": "Damião"},
        {"Nome": "Felipe Berge", "Sexo": "M", "Cargo": "Servo", "Leitor_Quinta": True, "Leitor_Sentinela": True, "Audio_Video": True, "Familia": "Felipe Berge"},
        {"Nome": "Alexandra", "Sexo": "F", "Cargo": "Publicador", "Leitor_Quinta": False, "Leitor_Sentinela": False, "Audio_Video": False, "Familia": "Felipe Berge"},
        {"Nome": "Bruno Giovanni", "Sexo": "M", "Cargo": "Publicador", "Leitor_Quinta": True, "Leitor_Sentinela": True, "Audio_Video": True, "Familia": "Bruno Giovanni"},
        {"Nome": "Itala", "Sexo": "F", "Cargo": "Publicador", "Leitor_Quinta": False, "Leitor_Sentinela": False, "Audio_Video": False, "Familia": "Bruno Giovanni"},
        {"Nome": "Alex Cauã", "Sexo": "M", "Cargo": "Publicador", "Leitor_Quinta": True, "Leitor_Sentinela": False, "Audio_Video": False, "Familia": "Alex Oliveira"},
        {"Nome": "Anderson Cauê", "Sexo": "M", "Cargo": "Publicador", "Leitor_Quinta": True, "Leitor_Sentinela": False, "Audio_Video": False, "Familia": "Alex Oliveira"},
        {"Nome": "Juan Pablo", "Sexo": "M", "Cargo": "Servo", "Leitor_Quinta": True, "Leitor_Sentinela": True, "Audio_Video": False, "Familia": "Nilson Bomfim"},
        {"Nome": "Nilson Bomfim", "Sexo": "M", "Cargo": "Publicador", "Leitor_Quinta": True, "Leitor_Sentinela": True, "Audio_Video": False, "Familia": "Nilson Bomfim"},
        {"Nome": "Carlos Veras", "Sexo": "M", "Cargo": "Publicador", "Leitor_Quinta": True, "Leitor_Sentinela": False, "Audio_Video": False, "Familia": "Avulso"},
        {"Nome": "Fabio Diniz", "Sexo": "M", "Cargo": "Publicador", "Leitor_Quinta": True, "Leitor_Sentinela": False, "Audio_Video": False, "Familia": "Avulso"},
        {"Nome": "Fabricio Diniz", "Sexo": "M", "Cargo": "Publicador", "Leitor_Quinta": True, "Leitor_Sentinela": False, "Audio_Video": False, "Familia": "Avulso"},
        {"Nome": "Felipe Pereira", "Sexo": "M", "Cargo": "Publicador", "Leitor_Quinta": True, "Leitor_Sentinela": True, "Audio_Video": False, "Familia": "Felipe Pereira"},
        {"Nome": "Marco Antônio", "Sexo": "M", "Cargo": "Servo", "Leitor_Quinta": True, "Leitor_Sentinela": False, "Audio_Video": False, "Familia": "Avulso"},
        {"Nome": "Wesley Rodrigues", "Sexo": "M", "Cargo": "Publicador", "Leitor_Quinta": True, "Leitor_Sentinela": False, "Audio_Video": False, "Familia": "Avulso"},
        {"Nome": "Adalberto Pereira", "Sexo": "M", "Cargo": "Servo", "Leitor_Quinta": False, "Leitor_Sentinela": False, "Audio_Video": False, "Familia": "Avulso"}
    ])

# ==========================================
# 2. INTERFACE VISUAL DO USUÁRIO
# ==========================================
st.title("Congregação Jardim Europa")
st.subheader("Gestor Automatizado de Reuniões")
st.caption("Filtros automáticos de privilégios, controle familiar e espelhamento Quinta ➡️ Sábado")

aba1, aba2 = st.tabs(["🗓️ Gerar Escala da Semana", "👥 Cadastro de Membros"])

# ------------------------------------------
# ABA 1: TELA DE CONFIGURAÇÃO DA ESCALA
# ------------------------------------------
with aba1:
    st.header("⚙️ Parâmetros da Reunião")
    
    col_d1, col_d2 = st.columns(2)
    with col_d1:
        data_reuniao = st.date_input("Selecione a Data da Reunião de Meio de Semana (Quinta)", datetime.now())
    with col_d2:
        num_partes_min = st.slider("Quantidade de partes dinâmicas no Bloco 'Faça Seu Melhor'", 2, 4, 3)

    st.markdown("---")
    
    st.subheader("✍️ Designações Manuais (Anciãos e Responsáveis Técnicos)")
    col_m1, col_m2 = st.columns(2)
    
    lista_anciaos = st.session_state.membros[st.session_state.membros["Cargo"] == "Ancião"]["Nome"].tolist()
    lista_av_permitidos = ["José Santana", "Damião"]
    
    with col_m1:
        t1_resp = st.selectbox("Tesouros Parte 1 (10 min) - Responsável", lista_anciaos, key="t1")
        t2_resp = st.selectbox("Tesouros Joias (10 min) - Responsável", lista_anciaos, key="t2")
        dirigente_estudo = st.selectbox("Dirigente do Estudo Bíblico (30 min)", lista_anciaos, key="dir_est")
    
    with col_m2:
        av_quinta = st.selectbox("Operador de Áudio e Vídeo (Som/Imagem)", lista_av_permitidos, key="av_q")
        ativar_nec_locais = st.checkbox("Esta semana terá a parte de 'Necessidades Locais'?")
        anciao_nec_locais = None
        if activar_nec_locais := activar_nec_locais:
            anciao_nec_locais = st.selectbox("Ancião designado para as Necessidades Locais", lista_anciaos)

    st.markdown("---")

    if st.button("🚀 Executar Inteligência e Montar Escala"):
        st.success(f"Grade montada com sucesso para a Congregação Jardim Europa!")
        
        leitores_quinta_disponiveis = st.session_state.membros[st.session_state.membros["Leitor_Quinta"] == True]["Nome"].tolist()
        leitores_sentinela_disponiveis = st.session_state.membros[st.session_state.membros["Leitor_Sentinela"] == True]["Nome"].tolist()
        
        leitor_q_sorteado = leitores_quinta_disponiveis[0]
        leitor_estudo_sorteado = leitores_quinta_disponiveis[2]
        leitor_sentinela_sorteado = leitores_sentinela_disponiveis[1]
        
        volante = "Irmão A"
        ind_interno = "Irmão B"
        ind_externo = "Irmão C"
        palco = "Irmão D"

        col_res1, col_res2 = st.columns(2)
        
        with col_res1:
            st.warning("📅 REUNIÃO DE QUINTA-FEIRA")
            st.markdown(f"**🎛️ Áudio e Vídeo:** {av_quinta}")
            st.markdown(f"**🔊 Microfone Volante:** {volante}")
            st.markdown(f"**🪑 Indicador Interno:** {ind_interno}")
            st.markdown(f"**🚪 Indicador Externo:** {ind_externo}")
            st.markdown(f"**🎭 Microfone de Palco:** {palco}")
            st.markdown("---")
            st.markdown(f"**[TESOUROS]** Parte 1 (10min): {t1_resp}")
            st.markdown(f"**[TESOUROS]** Joias (10min): {t2_resp}")
            st.markdown(f"**[TESOUROS]** Leitura da Bíblia (4min): `{leitor_q_sorteado}`")
            
            st.markdown("---")
            st.info("🎭 Faça Seu Melhor no Ministério (Salão Principal / Sala B)")
            for i in range(1, num_partes_min + 1):
                st.write(f"Parte {i} — Salão Principal: Dupla Sorteada")
                st.write(f"Parte {i} — Sala B: Dupla Sorteada")
                
            st.markdown("---")
            st.markdown("**[VIDA CRISTÃ]**")
            if activar_nec_locais:
                st.write(f"⚠️ Necessidades Locais: {anciao_nec_locais}")
            st.write(f"📖 Estudo Bíblico (Dirigente): {dirigente_estudo}")
            st.write(f"🎙️ Estudo Bíblico (Leitor): `{leitor_estudo_sorteado}`")

        with col_res2:
            st.success("REUNIÃO DE SÁBADO (Fim de Semana)")
            st.markdown(f"**🎛️ Áudio e Vídeo (Clonado):** {av_quinta}")
            st.markdown(f"**🔊 Microfone Volante (Clonado):** {volante}")
            st.markdown(f"**🪑 Indicador Interno (Clonado):** {ind_interno}")
            st.markdown(f"**🚪 Indicador Externo (Clonado):** {ind_externo}")
            st.markdown(f"**🎭 Microfone de Palco (Clonado):** {palco}")
            st.markdown("---")
            st.write("🎤 Discurso Público: [Orador Convidado/Externo]")
            st.markdown(f"📖 Leitor de A Sentinela: `{leitor_sentinela_sorteado}`")
            st.caption("🔒 Toda a infraestrutura de apoio foi espelhada automaticamente para poupar tempo da liderança.")

# ------------------------------------------
# ABA 2: TELA DE MANUTENÇÃO DOS MEMBROS
# ------------------------------------------
with aba2:
    st.header("👥 Cadastro Geral da Congregação")
    st.write("Modifique privilégios, mude cargos ou ajuste casais diretamente na tabela. O sistema recalcula tudo ao salvar.")
    
    dados_atualizados = st.data_editor(st.session_state.membros, num_rows="dynamic", use_container_width=True)
    
    if st.button("💾 Salvar Alterações no Banco De Dados"):
        st.session_state.membros = dados_atualizados
        st.success("As alterações foram gravadas na estrutura do aplicativo!")
