import streamlit as st
import pandas as pd
from datetime import datetime
import random

# Configuracao da pagina
st.set_page_config(page_title="Gerenciador Jardim Europa", layout="wide")

# Lista oficial de membros para checagem e reinicializacao
lista_membros_oficial = [
    # Os 11 Anciaos
    {"Nome": "Alanderson Carvalho", "Cargo": "Anciao", "Pres_Quinta": True, "Pres_Domingo": True, "Disc_Publico": True, "Leitor_Estudo": False, "Leitor_Sentinela": False, "Leitura_Biblia": False, "Disc_Estudante": False, "Audio_Video": False},
    {"Nome": "Alex Oliveira", "Cargo": "Anciao", "Pres_Quinta": True, "Pres_Domingo": True, "Disc_Publico": True, "Leitor_Estudo": False, "Leitor_Sentinela": False, "Leitura_Biblia": False, "Disc_Estudante": False, "Audio_Video": False},
    {"Nome": "Damião Sobrinho", "Cargo": "Anciao", "Pres_Quinta": True, "Pres_Domingo": True, "Disc_Publico": True, "Leitor_Estudo": False, "Leitor_Sentinela": False, "Leitura_Biblia": False, "Disc_Estudante": False, "Audio_Video": True},
    {"Nome": "Diassis Morais", "Cargo": "Anciao", "Pres_Quinta": True, "Pres_Domingo": True, "Disc_Publico": True, "Leitor_Estudo": False, "Leitor_Sentinela": False, "Leitura_Biblia": False, "Disc_Estudante": False, "Audio_Video": False},
    {"Nome": "Edilson Junior", "Cargo": "Anciao", "Pres_Quinta": True, "Pres_Domingo": True, "Disc_Publico": True, "Leitor_Estudo": False, "Leitor_Sentinela": False, "Leitura_Biblia": False, "Disc_Estudante": False, "Audio_Video": False},
    {"Nome": "Erivaldo Cavalcante", "Cargo": "Anciao", "Pres_Quinta": True, "Pres_Domingo": True, "Disc_Publico": True, "Leitor_Estudo": False, "Leitor_Sentinela": False, "Leitura_Biblia": False, "Disc_Estudante": False, "Audio_Video": False},
    {"Nome": "Gildênio Almeida", "Cargo": "Anciao", "Pres_Quinta": False, "Pres_Domingo": False, "Disc_Publico": True, "Leitor_Estudo": False, "Leitor_Sentinela": False, "Leitura_Biblia": False, "Disc_Estudante": False, "Audio_Video": False},
    {"Nome": "José Santana", "Cargo": "Anciao", "Pres_Quinta": True, "Pres_Domingo": True, "Disc_Publico": True, "Leitor_Estudo": False, "Leitor_Sentinela": False, "Leitura_Biblia": False, "Disc_Estudante": False, "Audio_Video": False},
    {"Nome": "Josevi Trindade", "Cargo": "Anciao", "Pres_Quinta": False, "Pres_Domingo": False, "Disc_Publico": True, "Leitor_Estudo": False, "Leitor_Sentinela": False, "Leitura_Biblia": False, "Disc_Estudante": False, "Audio_Video": False},
    {"Nome": "Ray Morais", "Cargo": "Anciao", "Pres_Quinta": True, "Pres_Domingo": True, "Disc_Publico": True, "Leitor_Estudo": False, "Leitor_Sentinela": False, "Leitura_Biblia": False, "Disc_Estudante": False, "Audio_Video": False},
    {"Nome": "Sidney Ramos", "Cargo": "Anciao", "Pres_Quinta": False, "Pres_Domingo": False, "Disc_Publico": True, "Leitor_Estudo": False, "Leitor_Sentinela": False, "Leitura_Biblia": False, "Disc_Estudante": False, "Audio_Video": False},
    
    # Outros homens e qualificacoes especificas
    {"Nome": "Alcides Morais", "Cargo": "Publicador", "Pres_Quinta": False, "Pres_Domingo": True, "Disc_Publico": True, "Leitor_Estudo": True, "Leitor_Sentinela": True, "Leitura_Biblia": True, "Disc_Estudante": True, "Audio_Video": False},
    {"Nome": "Felipe Berge", "Cargo": "Servo", "Pres_Quinta": False, "Pres_Domingo": True, "Disc_Publico": True, "Leitor_Estudo": True, "Leitor_Sentinela": True, "Leitura_Biblia": True, "Disc_Estudante": True, "Audio_Video": True},
    {"Nome": "Jonei Lima", "Cargo": "Servo", "Pres_Quinta": False, "Pres_Domingo": True, "Disc_Publico": True, "Leitor_Estudo": True, "Leitor_Sentinela": True, "Leitura_Biblia": True, "Disc_Estudante": True, "Audio_Video": True},
    {"Nome": "Juan Pablo", "Cargo": "Servo", "Pres_Quinta": False, "Pres_Domingo": False, "Disc_Publico": True, "Leitor_Estudo": True, "Leitor_Sentinela": True, "Leitura_Biblia": True, "Disc_Estudante": True, "Audio_Video": False},
    {"Nome": "Marco Antônio", "Cargo": "Servo", "Pres_Quinta": False, "Pres_Domingo": False, "Disc_Publico": False, "Leitor_Estudo": True, "Leitor_Sentinela": False, "Leitura_Biblia": True, "Disc_Estudante": True, "Audio_Video": False},
    {"Nome": "Marcos Antônio", "Cargo": "Servo", "Pres_Quinta": False, "Pres_Domingo": True, "Disc_Publico": True, "Leitor_Estudo": True, "Leitor_Sentinela": False, "Leitura_Biblia": False, "Disc_Estudante": False, "Audio_Video": False},
    
    # Demais habilitados das listas
    {"Nome": "Alex Cauã", "Cargo": "Publicador", "Pres_Quinta": False, "Pres_Domingo": False, "Disc_Publico": False, "Leitor_Estudo": True, "Leitor_Sentinela": False, "Leitura_Biblia": True, "Disc_Estudante": True, "Audio_Video": False},
    {"Nome": "Anderson Cauê", "Cargo": "Publicador", "Pres_Quinta": False, "Pres_Domingo": False, "Disc_Publico": False, "Leitor_Estudo": True, "Leitor_Sentinela": False, "Leitura_Biblia": True, "Disc_Estudante": True, "Audio_Video": False},
    {"Nome": "Bruno Giovanni", "Cargo": "Publicador", "Pres_Quinta": False, "Pres_Domingo": False, "Disc_Publico": False, "Leitor_Estudo": True, "Leitor_Sentinela": True, "Leitura_Biblia": True, "Disc_Estudante": True, "Audio_Video": True},
    {"Nome": "Carlos Veras", "Cargo": "Publicador", "Pres_Quinta": False, "Pres_Domingo": False, "Disc_Publico": False, "Leitor_Estudo": True, "Leitor_Sentinela": False, "Leitura_Biblia": True, "Disc_Estudante": True, "Audio_Video": False},
    {"Nome": "Fabio Diniz", "Cargo": "Publicador", "Pres_Quinta": False, "Pres_Domingo": False, "Disc_Publico": False, "Leitor_Estudo": True, "Leitor_Sentinela": False, "Leitura_Biblia": True, "Disc_Estudante": True, "Audio_Video": False},
    {"Nome": "Fabricio Diniz", "Cargo": "Publicador", "Pres_Quinta": False, "Pres_Domingo": False, "Disc_Publico": False, "Leitor_Estudo": True, "Leitor_Sentinela": False, "Leitura_Biblia": True, "Disc_Estudante": True, "Audio_Video": False},
    {"Nome": "Felipe Pereira", "Cargo": "Publicador", "Pres_Quinta": False, "Pres_Domingo": False, "Disc_Publico": False, "Leitor_Estudo": True, "Leitor_Sentinela": True, "Leitura_Biblia": True, "Disc_Estudante": True, "Audio_Video": False},
    {"Nome": "Geraldo Soares", "Cargo": "Publicador", "Pres_Quinta": False, "Pres_Domingo": False, "Disc_Publico": False, "Leitor_Estudo": True, "Leitor_Sentinela": False, "Leitura_Biblia": True, "Disc_Estudante": True, "Audio_Video": False},
    {"Nome": "Manoel Rodrigues", "Cargo": "Publicador", "Pres_Quinta": False, "Pres_Domingo": False, "Disc_Publico": False, "Leitor_Estudo": True, "Leitor_Sentinela": False, "Leitura_Biblia": True, "Disc_Estudante": True, "Audio_Video": False},
    {"Nome": "Nilson Bomfim", "Cargo": "Publicador", "Pres_Quinta": False, "Pres_Domingo": False, "Disc_Publico": False, "Leitor_Estudo": True, "Leitor_Sentinela": True, "Leitura_Biblia": True, "Disc_Estudante": True, "Audio_Video": False},
    {"Nome": "Roberto Rocha", "Cargo": "Publicador", "Pres_Quinta": False, "Pres_Domingo": False, "Disc_Publico": False, "Leitor_Estudo": True, "Leitor_Sentinela": False, "Leitura_Biblia": False, "Disc_Estudante": True, "Audio_Video": False},
    {"Nome": "Rodrigo Santana", "Cargo": "Publicador", "Pres_Quinta": False, "Pres_Domingo": False, "Disc_Publico": False, "Leitor_Estudo": True, "Leitor_Sentinela": True, "Leitura_Biblia": True, "Disc_Estudante": True, "Audio_Video": True},
    {"Nome": "Wesley Rodrigues", "Cargo": "Publicador", "Pres_Quinta": False, "Pres_Domingo": False, "Disc_Publico": False, "Leitor_Estudo": True, "Leitor_Sentinela": False, "Leitura_Biblia": False, "Disc_Estudante": True, "Audio_Video": False},
    
    # Excecoes de designacao
    {"Nome": "Adalberto Pereira", "Cargo": "Servo", "Pres_Quinta": False, "Pres_Domingo": False, "Disc_Publico": False, "Leitor_Estudo": False, "Leitor_Sentinela": False, "Leitura_Biblia": False, "Disc_Estudante": False, "Audio_Video": False}
]

# Inicializacao forçada para evitar colunas corrompidas no cache antigo
if 'membros' not in st.session_state or "Pres_Quinta" not in st.session_state.membros.columns:
    st.session_state.membros = pd.DataFrame(lista_membros_oficial)

# Menu Lateral de Acesso
st.sidebar.header("Controle de Acesso")
usuario_atual = st.sidebar.selectbox("Operador do Sistema", ["Selecione...", "Jonei Lima", "José Santana", "Damião Sobrinho", "Outro"])

# Trava de seguranca estrutural
tem_permissao_adm = usuario_atual in ["Jonei Lima", "José Santana", "Damião Sobrinho"]

aba1, aba2 = st.tabs(["Gerar Escala", "Listas de Habilitados"])

with aba1:
    if not tem_permissao_adm:
        st.warning("Acesso Restrito: Apenas operadores autorizados podem gerenciar os parametros estruturais.")
    else:
        st.header("Parametros da Escala Semanal")
        
        col_d1, col_d2 = st.columns(2)
        with col_d1:
            data_reuniao = st.date_input("Data da Reuniao de Meio de Semana", datetime.now())
        with col_d2:
            num_partes_min = st.slider("Numero de partes de treinamento", 2, 4, 3)

        st.markdown("---")
        st.subheader("Designacoes Manuais de Ensino")
        col_m1, col_m2 = st.columns(2)
        
        # Filtros corrigidos e estritos usando sintaxe direta do pandas
        lista_pres_quinta = st.session_state.membros[st.session_state.membros["Pres_Quinta"] == True]["Nome"].tolist()
        lista_anciaos_geral = st.session_state.membros[st.session_state.membros["Cargo"] == "Anciao"]["Nome"].tolist()
        lista_av = st.session_state.membros[st.session_state.membros["Audio_Video"] == True]["Nome"].tolist()
        
        with col_m1:
            presidente_q = st.selectbox("Presidente da Reuniao", lista_pres_quinta)
            dirigente_estudo = st.selectbox("Dirigente do Estudo", lista_anciaos_geral)
            av_operador = st.selectbox("Operador de Audio e Video", lista_av)
            
        with col_m2:
            necessidades_locais = st.checkbox("Incluir secao de Necessidades Locais?")
            anciao_nec_locais = "Nao se aplica"
            if necessidades_locais:
                anciao_nec_locais = st.selectbox("Anciao designado para Necessidades Locais", lista_anciaos_geral)

        st.markdown("---")

        if st.button("Executar Algoritmo e Gerar Grade"):
            seed_data = int(data_reuniao.strftime("%Y%m%d"))
            random.seed(seed_data)
            
            # Filtro das listas dinamicas diretas do DataFrame
            lista_leitura_biblia = st.session_state.membros[st.session_state.membros["Leitura_Biblia"] == True]["Nome"].tolist()
            lista_leitor_estudo = st.session_state.membros[st.session_state.membros["Leitor_Estudo"] == True]["Nome"].tolist()
            lista_leitor_sentinela = st.session_state.membros[st.session_state.membros["Leitor_Sentinela"] == True]["Nome"].tolist()
            lista_estudantes = st.session_state.membros[st.session_state.membros["Disc_Estudante"] == True]["Nome"].tolist()
            
            # Evitar acumulo de quem ja esta em partes fixas de ensino
            indisponiveis = [presidente_q, dirigente_estudo, anciao_nec_locais]
            
            leitura_b_disponiveis = [i for i in lista_leitura_biblia if i not in indisponiveis]
            leitura_e_disponiveis = [i for i in lista_leitor_estudo if i not in indisponiveis]
            
            random.shuffle(leitura_b_disponiveis)
            random.shuffle(leitura_e_disponiveis)
            random.shuffle(lista_leitor_sentinela)
            random.shuffle(lista_estudantes)
            
            leitor_b_fim = leitura_b_disponiveis[0] if leitura_b_disponiveis else "Disponivel"
            leitor_e_fim = [i for i in leitura_e_disponiveis if i != leitor_b_fim][0] if len([i for i in leitura_e_disponiveis if i != leitor_b_fim]) > 0 else "Disponivel"
            leitor_s_fim = [i for i in lista_leitor_sentinela if i not in [leitor_b_fim, leitor_e_fim]][0] if lista_leitor_sentinela else "Disponivel"

            # Indicadores de apoio estrutural (Sorteio limpo sem repeticao)
            todos_homens = st.session_state.membros[(st.session_state.membros["Cargo"] != "Anciao") & (st.session_state.membros["Nome"] != "Adalberto Pereira")]["Nome"].tolist()
            homens_apoio = [i for i in todos_homens if i not in [leitor_b_fim, leitor_e_fim, av_operador]]
            random.shuffle(homens_apoio)
            
            volante = homens_apoio[0] if len(homens_apoio) > 0 else "Disponivel"
            interno = homens_apoio[1] if len(homens_apoio) > 1 else "Disponivel"
            externo = homens_apoio[2] if len(homens_apoio) > 2 else "Disponivel"
            palco = homens_apoio[3] if len(homens_apoio) > 3 else "Disponivel"

            col_res1, col_res2 = st.columns(2)
            with col_res1:
                st.subheader("Grade de Meio de Semana")
                st.markdown(f"**Presidente:** {presidente_q}")
                st.markdown(f"**Audio e Video:** {av_operador}")
                st.markdown(f"**Microfone Volante:** {volante}")
                st.markdown(f"**Indicador Interno:** {interno}")
                st.markdown(f"**Indicador Externo:** {externo}")
                st.markdown(f"**Microfone de Palco:** {palco}")
                st.markdown("---")
                st.markdown(f"**Leitura da Biblia (4min):** {leitor_b_fim}")
                
                st.markdown("---")
                st.markdown("**Designacoes de Treinamento**")
                idx_est = 0
                for i in range(1, num_partes_min + 1):
                    est1 = lista_estudantes[idx_est % len(lista_estudantes)]
                    est2 = lista_estudantes[(idx_est + 1) % len(lista_estudantes)]
                    st.write(f"Parte {i} - Principal: **{est1}** / **{est2}**")
                    idx_est += 2
                
                st.markdown("---")
                if necessidades_locais:
                    st.write(f"**Necessidades Locais:** {anciao_nec_locais}")
                st.write(f"**Dirigente do Estudo:** {dirigente_estudo}")
                st.write(f"**Leitor do Estudo:** {leitor_e_fim}")

            with col_res2:
                st.subheader("Grade de Fim de Semana")
                st.markdown(f"**Audio e Video (Espelhado):** {av_operador}")
                st.markdown(f"**Microfone Volante (Espelhado):** {volante}")
                st.markdown(f"**Indicador Interno (Espelhado):** {interno}")
                st.markdown(f"**Indicador Externo (Espelhado):** {externo}")
                st.markdown(f"**Microfone de Palco (Espelhado):** {palco}")
                st.markdown("---")
                st.write("**Discurso Publico:** [Orador Convidado]")
                st.write(f"**Leitor de Secao:** {leitor_s_fim}")

with aba2:
    st.header("Verificacao de Habilitados por Categoria")
    
    col_l1, col_l2, col_l3 = st.columns(3)
    with col_l1:
        st.subheader("Lista Geral de Anciaos")
        st.dataframe(st.session_state.membros[st.session_state.membros["Cargo"] == "Anciao"][["Nome"]], hide_index=True)
    with col_l2:
        st.subheader("Habilitados Leitura Biblia")
        st.dataframe(st.session_state.membros[st.session_state.membros["Leitura_Biblia"] == True][["Nome"]], hide_index=True)
    with col_l3:
        st.subheader("Habilitados Sentinela")
        st.dataframe(st.session_state.membros[st.session_state.membros["Leitor_Sentinela"] == True][["Nome"]], hide_index=True)
