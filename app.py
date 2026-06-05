import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import random

# Configuracao da pagina
st.set_page_config(page_title="Gerenciador Jardim Europa", layout="wide")

# Lista oficial para restaurar a estrutura correta se houver quebra de cache
lista_membros_oficial = [
    # Os 11 Anciaos
    {"Nome": "Alanderson Carvalho", "Cargo": "Anciao", "Sexo": "M", "Pres_Quinta": True, "Pres_Domingo": True, "Disc_Publico": True, "Leitor_Estudo": False, "Leitor_Sentinela": False, "Leitura_Biblia": False, "Disc_Estudante": False, "Audio_Video": False},
    {"Nome": "Alex Oliveira", "Cargo": "Anciao", "Sexo": "M", "Pres_Quinta": True, "Pres_Domingo": True, "Disc_Publico": True, "Leitor_Estudo": False, "Leitor_Sentinela": False, "Leitura_Biblia": False, "Disc_Estudante": False, "Audio_Video": False},
    {"Nome": "Damião Sobrinho", "Cargo": "Anciao", "Sexo": "M", "Pres_Quinta": True, "Pres_Domingo": True, "Disc_Publico": True, "Leitor_Estudo": False, "Leitor_Sentinela": False, "Leitura_Biblia": False, "Disc_Estudante": False, "Audio_Video": True},
    {"Nome": "Diassis Morais", "Cargo": "Anciao", "Sexo": "M", "Pres_Quinta": True, "Pres_Domingo": True, "Disc_Publico": True, "Leitor_Estudo": False, "Leitor_Sentinela": False, "Leitura_Biblia": False, "Disc_Estudante": False, "Audio_Video": False},
    {"Nome": "Edilson Junior", "Cargo": "Anciao", "Sexo": "M", "Pres_Quinta": True, "Pres_Domingo": True, "Disc_Publico": True, "Leitor_Estudo": False, "Leitor_Sentinela": False, "Leitura_Biblia": False, "Disc_Estudante": False, "Audio_Video": False},
    {"Nome": "Erivaldo Cavalcante", "Cargo": "Anciao", "Sexo": "M", "Pres_Quinta": True, "Pres_Domingo": True, "Disc_Publico": True, "Leitor_Estudo": False, "Leitor_Sentinela": False, "Leitura_Biblia": False, "Disc_Estudante": False, "Audio_Video": False},
    {"Nome": "Gildênio Almeida", "Cargo": "Anciao", "Sexo": "M", "Pres_Quinta": False, "Pres_Domingo": False, "Disc_Publico": True, "Leitor_Estudo": False, "Leitor_Sentinela": False, "Leitura_Biblia": False, "Disc_Estudante": False, "Audio_Video": False},
    {"Nome": "José Santana", "Cargo": "Anciao", "Sexo": "M", "Pres_Quinta": True, "Pres_Domingo": True, "Disc_Publico": True, "Leitor_Estudo": False, "Leitor_Sentinela": False, "Leitura_Biblia": False, "Disc_Estudante": False, "Audio_Video": False},
    {"Nome": "Josevi Trindade", "Cargo": "Anciao", "Sexo": "M", "Pres_Quinta": False, "Pres_Domingo": False, "Disc_Publico": True, "Leitor_Estudo": False, "Leitor_Sentinela": False, "Leitura_Biblia": False, "Disc_Estudante": False, "Audio_Video": False},
    {"Nome": "Ray Morais", "Cargo": "Anciao", "Sexo": "M", "Pres_Quinta": True, "Pres_Domingo": True, "Disc_Publico": True, "Leitor_Estudo": False, "Leitor_Sentinela": False, "Leitura_Biblia": False, "Disc_Estudante": False, "Audio_Video": False},
    {"Nome": "Sidney Ramos", "Cargo": "Anciao", "Sexo": "M", "Pres_Quinta": False, "Pres_Domingo": False, "Disc_Publico": True, "Leitor_Estudo": False, "Leitor_Sentinela": False, "Leitura_Biblia": False, "Disc_Estudante": False, "Audio_Video": False},
    
    # Homens com qualificacoes especificas
    {"Nome": "Alcides Morais", "Cargo": "Publicador", "Sexo": "M", "Pres_Quinta": False, "Pres_Domingo": True, "Disc_Publico": True, "Leitor_Estudo": True, "Leitor_Sentinela": True, "Leitura_Biblia": True, "Disc_Estudante": True, "Audio_Video": False},
    {"Nome": "Felipe Berge", "Cargo": "Servo", "Sexo": "M", "Pres_Quinta": False, "Pres_Domingo": True, "Disc_Publico": True, "Leitor_Estudo": True, "Leitor_Sentinela": True, "Leitura_Biblia": True, "Disc_Estudante": True, "Audio_Video": True},
    {"Nome": "Jonei Lima", "Cargo": "Servo", "Sexo": "M", "Pres_Quinta": False, "Pres_Domingo": True, "Disc_Publico": True, "Leitor_Estudo": True, "Leitor_Sentinela": True, "Leitura_Biblia": True, "Disc_Estudante": True, "Audio_Video": True},
    {"Nome": "Juan Pablo", "Cargo": "Servo", "Sexo": "M", "Pres_Quinta": False, "Pres_Domingo": False, "Disc_Publico": True, "Leitor_Estudo": True, "Leitor_Sentinela": True, "Leitura_Biblia": True, "Disc_Estudante": True, "Audio_Video": False},
    {"Nome": "Marco Antônio", "Cargo": "Servo", "Sexo": "M", "Pres_Quinta": False, "Pres_Domingo": False, "Disc_Publico": False, "Leitor_Estudo": True, "Leitor_Sentinela": False, "Leitura_Biblia": True, "Disc_Estudante": True, "Audio_Video": False},
    {"Nome": "Marcos Antônio", "Cargo": "Servo", "Sexo": "M", "Pres_Quinta": False, "Pres_Domingo": True, "Disc_Publico": True, "Leitor_Estudo": True, "Leitor_Sentinela": False, "Leitura_Biblia": False, "Disc_Estudante": False, "Audio_Video": False},
    
    # Demais homens habilitados
    {"Nome": "Alex Cauã", "Cargo": "Publicador", "Sexo": "M", "Pres_Quinta": False, "Pres_Domingo": False, "Disc_Publico": False, "Leitor_Estudo": True, "Leitor_Sentinela": False, "Leitura_Biblia": True, "Disc_Estudante": True, "Audio_Video": False},
    {"Nome": "Anderson Cauê", "Cargo": "Publicador", "Sexo": "M", "Pres_Quinta": False, "Pres_Domingo": False, "Disc_Publico": False, "Leitor_Estudo": True, "Leitor_Sentinela": False, "Leitura_Biblia": True, "Disc_Estudante": True, "Audio_Video": False},
    {"Nome": "Bruno Giovanni", "Cargo": "Publicador", "Sexo": "M", "Pres_Quinta": False, "Pres_Domingo": False, "Disc_Publico": False, "Leitor_Estudo": True, "Leitor_Sentinela": True, "Leitura_Biblia": True, "Disc_Estudante": True, "Audio_Video": True},
    {"Nome": "Carlos Veras", "Cargo": "Publicador", "Sexo": "M", "Pres_Quinta": False, "Pres_Domingo": False, "Disc_Publico": False, "Leitor_Estudo": True, "Leitor_Sentinela": False, "Leitura_Biblia": True, "Disc_Estudante": True, "Audio_Video": False},
    {"Nome": "Fabio Diniz", "Cargo": "Publicador", "Sexo": "M", "Pres_Quinta": False, "Pres_Domingo": False, "Disc_Publico": False, "Leitor_Estudo": True, "Leitor_Sentinela": False, "Leitura_Biblia": True, "Disc_Estudante": True, "Audio_Video": False},
    {"Nome": "Fabricio Diniz", "Cargo": "Publicador", "Sexo": "M", "Pres_Quinta": False, "Pres_Domingo": False, "Disc_Publico": False, "Leitor_Estudo": True, "Leitor_Sentinela": False, "Leitura_Biblia": True, "Disc_Estudante": True, "Audio_Video": False},
    {"Nome": "Felipe Pereira", "Cargo": "Publicador", "Sexo": "M", "Pres_Quinta": False, "Pres_Domingo": False, "Disc_Publico": False, "Leitor_Estudo": True, "Leitor_Sentinela": True, "Leitura_Biblia": True, "Disc_Estudante": True, "Audio_Video": False},
    {"Nome": "Geraldo Soares", "Cargo": "Publicador", "Sexo": "M", "Pres_Quinta": False, "Pres_Domingo": False, "Disc_Publico": False, "Leitor_Estudo": True, "Leitor_Sentinela": False, "Leitura_Biblia": True, "Disc_Estudante": True, "Audio_Video": False},
    {"Nome": "Manoel Rodrigues", "Cargo": "Publicador", "Sexo": "M", "Pres_Quinta": False, "Pres_Domingo": False, "Disc_Publico": False, "Leitor_Estudo": True, "Leitor_Sentinela": False, "Leitura_Biblia": True, "Disc_Estudante": True, "Audio_Video": False},
    {"Nome": "Nilson Bomfim", "Cargo": "Publicador", "Sexo": "M", "Pres_Quinta": False, "Pres_Domingo": False, "Disc_Publico": False, "Leitor_Estudo": True, "Leitor_Sentinela": True, "Leitura_Biblia": True, "Disc_Estudante": True, "Audio_Video": False},
    {"Nome": "Roberto Rocha", "Cargo": "Publicador", "Sexo": "M", "Pres_Quinta": False, "Pres_Domingo": False, "Disc_Publico": False, "Leitor_Estudo": True, "Leitor_Sentinela": False, "Leitura_Biblia": False, "Disc_Estudante": True, "Audio_Video": False},
    {"Nome": "Rodrigo Santana", "Cargo": "Publicador", "Sexo": "M", "Pres_Quinta": False, "Pres_Domingo": False, "Disc_Publico": False, "Leitor_Estudo": True, "Leitor_Sentinela": True, "Leitura_Biblia": True, "Disc_Estudante": True, "Audio_Video": True},
    {"Nome": "Wesley Rodrigues", "Cargo": "Publicador", "Sexo": "M", "Pres_Quinta": False, "Pres_Domingo": False, "Disc_Publico": False, "Leitor_Estudo": True, "Leitor_Sentinela": False, "Leitura_Biblia": False, "Disc_Estudante": True, "Audio_Video": False},
    {"Nome": "Adalberto Pereira", "Cargo": "Servo", "Sexo": "M", "Pres_Quinta": False, "Pres_Domingo": False, "Disc_Publico": False, "Leitor_Estudo": False, "Leitor_Sentinela": False, "Leitura_Biblia": False, "Disc_Estudante": False, "Audio_Video": False},
    
    # Irmas cadastradas para o bloco de treinamento (Faça Seu Melhor)
    {"Nome": "Cássia Leite", "Cargo": "Publicador", "Sexo": "F", "Pres_Quinta": False, "Pres_Domingo": False, "Disc_Publico": False, "Leitor_Estudo": False, "Leitor_Sentinela": False, "Leitura_Biblia": False, "Disc_Estudante": True, "Audio_Video": False},
    {"Nome": "Jane Morais", "Cargo": "Publicador", "Sexo": "F", "Pres_Quinta": False, "Pres_Domingo": False, "Disc_Publico": False, "Leitor_Estudo": False, "Leitor_Sentinela": False, "Leitura_Biblia": False, "Disc_Estudante": True, "Audio_Video": False},
    {"Nome": "Elizangela Santana", "Cargo": "Publicador", "Sexo": "F", "Pres_Quinta": False, "Pres_Domingo": False, "Disc_Publico": False, "Leitor_Estudo": False, "Leitor_Sentinela": False, "Leitura_Biblia": False, "Disc_Estudante": True, "Audio_Video": False},
    {"Nome": "Rita Lima", "Cargo": "Publicador", "Sexo": "F", "Pres_Quinta": False, "Pres_Domingo": False, "Disc_Publico": False, "Leitor_Estudo": False, "Leitor_Sentinela": False, "Leitura_Biblia": False, "Disc_Estudante": True, "Audio_Video": False},
    {"Nome": "Alexandra Berge", "Cargo": "Publicador", "Sexo": "F", "Pres_Quinta": False, "Pres_Domingo": False, "Disc_Publico": False, "Leitor_Estudo": False, "Leitor_Sentinela": False, "Leitura_Biblia": False, "Disc_Estudante": True, "Audio_Video": False},
    {"Nome": "Itala Giovanni", "Cargo": "Publicador", "Sexo": "F", "Pres_Quinta": False, "Pres_Domingo": False, "Disc_Publico": False, "Leitor_Estudo": False, "Leitor_Sentinela": False, "Leitura_Biblia": False, "Disc_Estudante": True, "Audio_Video": False}
]

# Forca limpeza total do cache estrutural antigo
if 'membros' not in st.session_state or "Sexo" not in st.session_state.membros.columns:
    st.session_state.membros = pd.DataFrame(lista_membros_oficial)

# Menu Lateral de Acesso
st.sidebar.header("Controle de Acesso")
usuario_atual = st.sidebar.selectbox("Operador do Sistema", ["Selecione...", "Jonei Lima", "José Santana", "Damião Sobrinho", "Outro"])

tem_permissao_adm = usuario_atual in ["Jonei Lima", "José Santana", "Damião Sobrinho"]

aba1, aba2 = st.tabs(["Gerar Escala", "Listas de Habilitados"])

with aba1:
    if not tem_permissao_adm:
        st.warning("Acesso Restrito: Apenas operadores autorizados podem gerenciar os parametros estruturais.")
    else:
        st.header("Parametros da Escala Semanal")
        
        col_d1, col_d2 = st.columns(2)
        with col_d1:
            data_escolhida = st.date_input("Selecione um dia da semana", datetime.now())
            segunda_feira = data_escolhida - timedelta(days=data_escolhida.weekday())
            st.info(f"**Semana de {segunda_feira.strftime('%d/%m/%Y')}** (Baseada na segunda-feira)")
        with col_d2:
            num_partes_min = st.slider("Numero de secoes de treinamento", 1, 3, 2)

        st.markdown("---")
        st.subheader("Designacoes Manuais de Ensino")
        col_m1, col_m2 = st.columns(2)
        
        lista_pres_quinta = st.session_state.membros[st.session_state.membros["Pres_Quinta"] == True]["Nome"].tolist()
        lista_av = st.session_state.membros[st.session_state.membros["Audio_Video"] == True]["Nome"].tolist()
        
        with col_m1:
            presidente_q = st.selectbox("Presidente da Reuniao", lista_pres_quinta)
            
            # Filtro limpo removendo o Presidente
            lista_anciaos_filtrada = st.session_state.membros[(st.session_state.membros["Cargo"] == "Anciao") & (st.session_state.membros["Nome"] != presidente_q)]["Nome"].tolist()
            
            dirigente_estudo = st.selectbox("Dirigente do Estudo", lista_anciaos_filtrada)
            av_operador = st.selectbox("Operador de Audio e Video", lista_av)
            
        with col_m2:
            necessidades_locais = st.checkbox("Incluir secao de Necessidades Locais?")
            anciao_nec_locais = "Nao se aplica"
            if necessidades_locais:
                lista_nec_locais = [a for a in lista_anciaos_filtrada]
                anciao_nec_locais = st.selectbox("Anciao designado para Necessidades Locais", lista_nec_locais)

        st.markdown("---")

        if st.button("Executar Algoritmo e Gerar Grade"):
            seed_data = int(segunda_feira.strftime("%Y%m%d"))
            random.seed(seed_data)
            
            # Damião ou qualquer outro operador fixado no som entra aqui para blindagem absoluta
            indisponiveis_total = [presidente_q, dirigente_estudo, anciao_nec_locais, av_operador]
            
            # Filtro com sintaxe explicita corrigida
            df_membros = st.session_state.membros
            
            lista_leitura_biblia = df_membros[(df_membros["Leitura_Biblia"] == True) & (~df_membros["Nome"].isin(indisponiveis_total))]["Nome"].tolist()
            lista_leitor_estudo = df_membros[(df_membros["Leitor_Estudo"] == True) & (~df_membros["Nome"].isin(indisponiveis_total))]["Nome"].tolist()
            lista_leitor_sentinela = df_membros[(df_membros["Leitor_Sentinela"] == True) & (~df_membros["Nome"].isin(indisponiveis_total))]["Nome"].tolist()
            
            random.shuffle(lista_leitura_biblia)
            random.shuffle(lista_leitor_estudo)
            random.shuffle(lista_leitor_sentinela)
            
            leitor_b_fim = lista_leitura_biblia[0] if lista_leitura_biblia else "Disponivel"
            leitor_e_fim = [i for i in lista_leitor_estudo if i != leitor_b_fim][0] if len([i for i in lista_leitor_estudo if i != leitor_b_fim]) > 0 else "Disponivel"
            leitor_s_fim = [i for i in lista_leitor_sentinela if i not in [leitor_b_fim, leitor_e_fim]][0] if lista_leitor_sentinela else "Disponivel"

            # Corrigida a linha 127 com a sintaxe direta do Pandas sem duplicacao de escopo
            estudantes_f = df_membros[(df_membros["Disc_Estudante"] == True) & (df_membros["Sexo"] == "F")]["Nome"].tolist()
            estudantes_m = df_membros[(df_membros["Disc_Estudante"] == True) & (df_membros["Sexo"] == "M") & (~df_membros["Nome"].isin(indisponiveis_total))]["Nome"].tolist()
            
            random.shuffle(estudantes_f)
            random.shuffle(estudantes_m)
            
            fila_treinamento = estudantes_f + estudantes_m

            # Auxiliares de apoio estrutural masculino sem choques
            todos_homens = df_membros[(df_membros["Cargo"] != "Anciao") & (df_membros["Nome"] != "Adalberto Pereira") & (df_membros["Sexo"] == "M")]["Nome"].tolist()
            homens_apoio = [i for i in todos_homens if i not in [leitor_b_fim, leitor_e_fim] and i not in indisponiveis_total]
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
                st.markdown("**Treinamento Designado (Faça Seu Melhor)**")
                
                idx_t = 0
                for i in range(1, num_partes_min + 1):
                    p1 = fila_treinamento[idx_t % len(fila_treinamento)]
                    p2 = fila_treinamento[(idx_t + 1) % len(fila_treinamento)]
                    st.write(f"Parte {i} - **Sala Principal**: {p1} / {p2}")
                    idx_t += 2
                    
                    p3 = fila_treinamento[idx_t % len(fila_treinamento)]
                    p4 = fila_treinamento[(idx_t + 1) % len(fila_treinamento)]
                    st.write(f"Parte {i} - **Sala B**: {p3} / {p4}")
                    idx_t += 2
                
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
    col_l1, col_l2 = st.columns(2)
    with col_l1:
        st.subheader("Irmas no Treinamento")
        st.dataframe(st.session_state.membros[(st.session_state.membros["Disc_Estudante"] == True) & (st.session_state.membros["Sexo"] == "F")][["Nome"]], hide_index=True)
    with col_l2:
        st.subheader("Operadores de Som Cadastrados")
        st.dataframe(st.session_state.membros[st.session_state.membros["Audio_Video"] == True][["Nome"]], hide_index=True)
