import streamlit as st
import pandas as pd
from datetime import datetime
import random

# Configuração da página do Streamlit
st.set_page_config(page_title="Congregação Jardim Europa - Gestor", layout="wide")

# ==========================================
# 1. BANCO DE DADOS ATUALIZADO (REGRAS OFICIAIS)
# ==========================================
if 'membros' not in st.session_state:
    st.session_state.membros = pd.DataFrame([
        # Anciãos Oficiais (11)
        {"Nome": "Alanderson Carvalho", "Cargo": "Ancião", "Pres_Quinta": True, "Pres_Domingo": True, "Disc_Publico": True, "Leitor_Estudo": False, "Leitor_Sentinela": False, "Leitura_Biblia": False, "Disc_Estudante": False},
        {"Nome": "Alex Oliveira", "Cargo": "Ancião", "Pres_Quinta": True, "Pres_Domingo": True, "Disc_Publico": True, "Leitor_Estudo": False, "Leitor_Sentinela": False, "Leitura_Biblia": False, "Disc_Estudante": False},
        {"Nome": "Damião Sobrinho", "Cargo": "Ancião", "Pres_Quinta": True, "Pres_Domingo": True, "Disc_Publico": True, "Leitor_Estudo": False, "Leitor_Sentinela": False, "Leitura_Biblia": False, "Disc_Estudante": False},
        {"Nome": "Diassis Morais", "Cargo": "Ancião", "Pres_Quinta": True, "Pres_Domingo": True, "Disc_Publico": True, "Leitor_Estudo": False, "Leitor_Sentinela": False, "Leitura_Biblia": False, "Disc_Estudante": False},
        {"Nome": "Edilson Junior", "Cargo": "Ancião", "Pres_Quinta": True, "Pres_Domingo": True, "Disc_Publico": True, "Leitor_Estudo": False, "Leitor_Sentinela": False, "Leitura_Biblia": False, "Disc_Estudante": False},
        {"Nome": "Erivaldo Cavalcante", "Cargo": "Ancião", "Pres_Quinta": True, "Pres_Domingo": True, "Disc_Publico": True, "Leitor_Estudo": False, "Leitor_Sentinela": False, "Leitura_Biblia": False, "Disc_Estudante": False},
        {"Nome": "Gildênio Almeida", "Cargo": "Ancião", "Pres_Quinta": False, "Pres_Domingo": False, "Disc_Publico": True, "Leitor_Estudo": False, "Leitor_Sentinela": False, "Leitura_Biblia": False, "Disc_Estudante": False},
        {"Nome": "José Santana", "Cargo": "Ancião", "Pres_Quinta": True, "Pres_Domingo": True, "Disc_Publico": True, "Leitor_Estudo": False, "Leitor_Sentinela": False, "Leitura_Biblia": False, "Disc_Estudante": False},
        {"Nome": "Josevi Trindade", "Cargo": "Ancião", "Pres_Quinta": False, "Pres_Domingo": False, "Disc_Publico": True, "Leitor_Estudo": False, "Leitor_Sentinela": False, "Leitura_Biblia": False, "Disc_Estudante": False},
        {"Nome": "Ray Morais", "Cargo": "Ancião", "Pres_Quinta": True, "Pres_Domingo": True, "Disc_Publico": True, "Leitor_Estudo": False, "Leitor_Sentinela": False, "Leitura_Biblia": False, "Disc_Estudante": False},
        {"Nome": "Sidney Ramos", "Cargo": "Ancião", "Pres_Quinta": False, "Pres_Domingo": False, "Disc_Publico": True, "Leitor_Estudo": False, "Leitor_Sentinela": False, "Leitura_Biblia": False, "Disc_Estudante": False},
        
        # Outros irmãos com privilégios específicos de Ensino/Presidência
        {"Nome": "Alcides Morais", "Cargo": "Publicador", "Pres_Quinta": False, "Pres_Domingo": True, "Disc_Publico": True, "Leitor_Estudo": True, "Leitor_Sentinela": True, "Leitura_Biblia": True, "Disc_Estudante": True},
        {"Nome": "Felipe Berge", "Cargo": "Servo", "Pres_Quinta": False, "Pres_Domingo": True, "Disc_Publico": True, "Leitor_Estudo": True, "Leitor_Sentinela": True, "Leitura_Biblia": True, "Disc_Estudante": True},
        {"Nome": "Jonei Lima", "Cargo": "Servo", "Pres_Quinta": False, "Pres_Domingo": True, "Disc_Publico": True, "Leitor_Estudo": True, "Leitor_Sentinela": True, "Leitura_Biblia": True, "Disc_Estudante": True},
        {"Nome": "Juan Pablo", "Cargo": "Servo", "Pres_Quinta": False, "Pres_Domingo": False, "Disc_Publico": True, "Leitor_Estudo": True, "Leitor_Sentinela": True, "Leitura_Biblia": True, "Disc_Estudante": True},
        {"Nome": "Marcos Antônio", "Cargo": "Servo", "Pres_Quinta": False, "Pres_Domingo": True, "Disc_Publico": True, "Leitor_Estudo": True, "Leitor_Sentinela": False, "Leitura_Biblia": True, "Disc_Estudante": True},
        
        # Demais irmãos habilitados
        {"Nome": "Alex Cauã", "Cargo": "Publicador", "Pres_Quinta": False, "Pres_Domingo": False, "Disc_Publico": False, "Leitor_Estudo": True, "Leitor_Sentinela": False, "Leitura_Biblia": True, "Disc_Estudante": True},
        {"Nome": "Anderson Cauê", "Cargo": "Publicador", "Pres_Quinta": False, "Pres_Domingo": False, "Disc_Publico": False, "Leitor_Estudo": True, "Leitor_Sentinela": False, "Leitura_Biblia": True, "Disc_Estudante": True},
        {"Nome": "Bruno Giovanni", "Cargo": "Publicador", "Pres_Quinta": False, "Pres_Domingo": False, "Disc_Publico": False, "Leitor_Estudo": True, "Leitor_Sentinela": True, "Leitura_Biblia": True, "Disc_Estudante": True},
        {"Nome": "Carlos Veras", "Cargo": "Publicador", "Pres_Quinta": False, "Pres_Domingo": False, "Disc_Publico": False, "Leitor_Estudo": True, "Leitor_Sentinela": False, "Leitura_Biblia": True, "Disc_Estudante": True},
        {"Nome": "Fabio Diniz", "Cargo": "Publicador", "Pres_Quinta": False, "Pres_Domingo": False, "Disc_Publico": False, "Leitor_Estudo": True, "Leitor_Sentinela": False, "Leitura_Biblia": True, "Disc_Estudante": True},
        {"Nome": "Fabricio Diniz", "Cargo": "Publicador", "Pres_Quinta": False, "Pres_Domingo": False, "Disc_Publico": False, "Leitor_Estudo": True, "Leitor_Sentinela": False, "Leitura_Biblia": True, "Disc_Estudante": True},
        {"Nome": "Felipe Pereira", "Cargo": "Publicador", "Pres_Quinta": False, "Pres_Domingo": False, "Disc_Publico": False, "Leitor_Estudo": True, "Leitor_Sentinela": True, "Leitura_Biblia": True, "Disc_Estudante": True},
        {"Nome": "Geraldo Soares", "Cargo": "Publicador", "Pres_Quinta": False, "Pres_Domingo": False, "Disc_Publico": False, "Leitor_Estudo": True, "Leitor_Sentinela": False, "Leitura_Biblia": True, "Disc_Estudante": True},
        {"Nome": "Manoel Rodrigues", "Cargo": "Publicador", "Pres_Quinta": False, "Pres_Domingo": False, "Disc_Publico": False, "Leitor_Estudo": True, "Leitor_Sentinela": False, "Leitura_Biblia": True, "Disc_Estudante": True},
        {"Nome": "Nilson Bomfim", "Cargo": "Publicador", "Pres_Quinta": False, "Pres_Domingo": False, "Disc_Publico": False, "Leitor_Estudo": True, "Leitor_Sentinela": True, "Leitura_Biblia": True, "Disc_Estudante": True},
        {"Nome": "Roberto Rocha", "Cargo": "Publicador", "Pres_Quinta": False, "Pres_Domingo": False, "Disc_Publico": False, "Leitor_Estudo": True, "Leitor_Sentinela": False, "Leitura_Biblia": False, "Disc_Estudante": True},
        {"Nome": "Rodrigo Santana", "Cargo": "Publicador", "Pres_Quinta": False, "Pres_Domingo": False, "Disc_Publico": False, "Leitor_Estudo": True, "Leitor_Sentinela": True, "Leitura_Biblia": True, "Disc_Estudante": True},
        {"Nome": "Wesley Rodrigues", "Cargo": "Publicador", "Pres_Quinta": False, "Pres_Domingo": False, "Disc_Publico": False, "Leitor_Estudo": True, "Leitor_Sentinela": False, "Leitura_Biblia": False, "Disc_Estudante": True},
        
        # Exceção explícita
        {"Nome": "Adalberto Pereira", "Cargo": "Servo", "Pres_Quinta": False, "Pres_Domingo": False, "Disc_Publico": False, "Leitor_Estudo": False, "Leitor_Sentinela": False, "Leitura_Biblia": False, "Disc_Estudante": False}
    ])

# ==========================================
# 2. INTERFACE VISUAL DO APP
# ==========================================
st.title("Congregação Jardim Europa")
st.caption("Filtros de privilégios baseados estritamente na listagem da congregação.")

# TRAVA DE SEGURANÇA EXIGIDA
st.sidebar.header("🔐 Controle de Acesso")
usuario_atual = st.sidebar.selectbox("Quem está operando o sistema?", ["Selecione...", "José Santana", "Damião Sobrinho", "Outro Irmão"])

# Validação do Operador
tem_permissao_adm = usuario_atual in ["José Santana", "Damião Sobrinho"]

aba1, aba2 = st.tabs(["🗓️ Gerar Escala da Semana", "👥 Listas de Habilitados"])

with aba1:
    if not tem_permissao_adm:
        st.warning("⚠️ **Acesso Bloqueado:** Apenas os anciãos coordenadores (José Santana ou Damião Sobrinho) podem definir parâmetros e gerenciar os anciãos da escala.")
    else:
        st.success(f"🔓 Modo Supervisor Ativo: Bem-vindo, irmão {usuario_atual}.")
        
        st.header("⚙️ Parâmetros da Reunião")
        col_d1, col_d2 = st.columns(2)
        with col_d1:
            data_reuniao = st.date_input("Selecione a Data da Reunião (Quinta)", datetime.now())
        with col_d2:
            num_partes_min = st.slider("Quantidade de partes no bloco 'Faça Seu Melhor'", 2, 4, 3)

        st.markdown("---")
        st.subheader("✍️ Designações Estruturais de Ensino")
        
        col_m1, col_m2 = st.columns(2)
        
        # Extração das listas baseadas estritamente nas regras enviadas
        lista_pres_quinta = st.session_state.membros[st.session_state.membros["Pres_Quinta"] == True]["Nome"].tolist()
        lista_anciaos_locais = st.session_state.membros[st.session_state.membros["Cargo"] == "Ancião"]["Nome"].tolist()
        
        with col_m1:
            presidente_q = st.selectbox("Presidente da Reunião de Quinta-Feira", lista_pres_quinta)
            dirigente_estudo = st.selectbox("Dirigente do Estudo Bíblico (Ancião)", lista_anciaos_locais)
        
        with col_m2:
            necessidades_locais = st.checkbox("Esta semana terá a parte de 'Necessidades Locais'?")
            anciao_nec_locais = "Não terá"
            if necessidades_locais:
                anciao_nec_locais = st.selectbox("Ancião para as Necessidades Locais", lista_anciaos_locais)

        st.markdown("---")

        if st.button("🚀 Gerar Grade de Designações"):
            seed_data = int(data_reuniao.strftime("%Y%m%d"))
            random.seed(seed_data)
            
            # Filtro rigoroso de Leitores coletando direto do banco de dados configurado
            lista_leitura_biblia = st.session_state.membros[st.session_state.membros["Leitura_Biblia"] == True]["Nome"].tolist()
            lista_leitor_estudo = st.session_state.membros[st.session_state.membros["Leitor_Estudo"] == True]["Nome"].tolist()
            lista_leitor_sentinela = st.session_state.membros[st.session_state.membros["Leitor_Sentinela"] == True]["Nome"].tolist()
            lista_estudantes = st.session_state.membros[st.session_state.membros["Disc_Estudante"] == True]["Nome"].tolist()
            
            # Evitar repetições imediatas tirando quem já está em partes grandes fixas
            ocupados = [presidente_q, dirigente_estudo, anciao_nec_locais]
            
            leitores_b_filtrados = [i for i in lista_leitura_biblia if i not in ocupados]
            leitores_e_filtrados = [i for i in lista_leitor_estudo if i not in ocupados]
            
            random.shuffle(leitores_b_filtrados)
            random.shuffle(leitores_e_filtrados)
            random.shuffle(lista_leitor_sentinela)
            random.shuffle(lista_estudantes)
            
            leitor_b_escolhido = leitores_b_filtrados[0] if leitores_b_filtrados else "Disponível"
            leitor_e_escolhido = [i for i in leitores_e_filtrados if i != leitor_b_escolhido][0] if len([i for i in leitores_e_filtrados if i != leitor_b_escolhido]) > 0 else "Disponível"
            leitor_s_escolhido = [i for i in lista_leitor_sentinela if i not in [leitor_b_escolhido, leitor_e_escolhido]][0] if lista_leitor_sentinela else "Disponível"

            st.balloons()
            
            col_res1, col_res2 = st.columns(2)
            with col_res1:
                st.warning("📅 DESIGNADOS DE QUINTA-FEIRA")
                st.markdown(f"**👑 Presidente da Reunião:** {presidente_q}")
                st.markdown(f"**📖 Leitura da Bíblia (4min):** `{leitor_b_escolhido}`")
                st.markdown("---")
                st.info("🎭 Bloco Faça Seu Melhor")
                
                idx_est = 0
                for i in range(1, num_partes_min + 1):
                    est1 = lista_estudantes[idx_est % len(lista_estudantes)]
                    est2 = lista_estudantes[(idx_est + 1) % len(lista_estudantes)]
                    st.write(f"Parte {i} — Salão Principal: **{est1}** e **{est2}**")
                    idx_est += 2
                
                st.markdown("---")
                st.markdown("**[VIDA CRISTÃ]**")
                if necessidades_locais:
                    st.write(f"⚠️ Necessidades Locais: **{anciao_nec_locais}**")
                st.write(f"📖 Estudo Bíblico (Dirigente): **{dirigente_estudo}**")
                st.write(f"🎙️ Estudo Bíblico (Leitor): `{leitor_e_escolhido}`")

            with col_res2:
                st.success("DESIGNADOS DE DOMINGO")
                st.markdown("**🎤 Discurso Público:** [Orador Convidado]")
                st.markdown(f"**📖 Leitor de A Sentinela:** `{leitor_s_escolhido}`")

with aba2:
    st.header("📊 Listas de Controle Interno")
    st.write("Aqui você confere como o motor do aplicativo está enxergando os privilégios baseado nas listas enviadas:")
    
    col_l1, col_l2, col_l3 = st.columns(3)
    with col_l1:
        st.subheader("Anciãos Disponíveis")
        st.dataframe(st.session_state.membros[st.session_state.membros["Cargo"] == "Ancião"][["Nome"]], hide_index=True)
    with col_l2:
        st.subheader("Habilitados Leitura Bíblia")
        st.dataframe(st.session_state.membros[st.session_state.membros["Leitura_Biblia"] == True][["Nome"]], hide_index=True)
    with col_l3:
        st.subheader("Habilitados Sentinela")
        st.dataframe(st.session_state.membros[st.session_state.membros["Leitor_Sentinela"] == True][["Nome"]], hide_index=True)
