import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import random

# Configuracao da pagina
st.set_page_config(page_title="Gerenciador Jardim Europa", layout="wide")

# Lista oficial corrigida e atualizada
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
    
    # Homens com qualificacoes especificas (Felipe Berger corrigido)
    {"Nome": "Alcides Morais", "Cargo": "Publicador", "Sexo": "M", "Pres_Quinta": False, "Pres_Domingo": True, "Disc_Publico": True, "Leitor_Estudo": True, "Leitor_Sentinela": True, "Leitura_Biblia": True, "Disc_Estudante": True, "Audio_Video": False},
    {"Nome": "Felipe Berger", "Cargo": "Servo", "Sexo": "M", "Pres_Quinta": False, "Pres_Domingo": True, "Disc_Publico": True, "Leitor_Estudo": True, "Leitor_Sentinela": True, "Leitura_Biblia": True, "Disc_Estudante": True, "Audio_Video": True},
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
    
    # Irmas cadastradas (Nomes corrigidos aqui)
    {"Nome": "Cássia Leite", "Cargo": "Publicador", "Sexo": "F", "Pres_Quinta": False, "Pres_Domingo": False, "Disc_Publico": False, "Leitor_Estudo": False, "Leitor_Sentinela": False, "Leitura_Biblia": False, "Disc_Estudante": True, "Audio_Video": False},
    {"Nome": "Jane Morais", "Cargo": "Publicador", "Sexo": "F", "Pres_Quinta": False, "Pres_Domingo": False, "Disc_Publico": False, "Leitor_Estudo": False, "Leitor_Sentinela": False, "Leitura_Biblia": False, "Disc_Estudante": True, "Audio_Video": False},
    {"Nome": "Elizangela Santana", "Cargo": "Publicador", "Sexo": "F", "Pres_Quinta": False, "Pres_Domingo": False, "Disc_Publico": False, "Leitor_Estudo": False, "Leitor_Sentinela": False, "Leitura_Biblia": False, "Disc_Estudante": True, "Audio_Video": False},
    {"Nome": "Rita Lima", "Cargo": "Publicador", "Sexo": "F", "Pres_Quinta": False, "Pres_Domingo": False, "Disc_Publico": False, "Leitor_Estudo": False, "Leitor_Sentinela": False, "Leitura_Biblia": False, "Disc_Estudante": True, "Audio_Video": False},
    {"Nome": "Alessandra Cavalcante", "Cargo": "Publicador", "Sexo": "F", "Pres_Quinta": False, "Pres_Domingo": False, "Disc_Publico": False, "Leitor_Estudo": False, "Leitor_Sentinela": False, "Leitura_Biblia": False, "Disc_Estudante": True, "Audio_Video": False},
    {"Nome": "Itala Giovanni", "Cargo": "Publicador", "Sexo": "F", "Pres_Quinta": False, "Pres_Domingo": False, "Disc_Publico": False, "Leitor_Estudo": False, "Leitor_Sentinela": False, "Leitura_Biblia": False, "Disc_Estudante": True, "Audio_Video": False}
]

# Forcar reset se encontrar qualquer vestigio de dados antigos ou nomes errados na memoria
if 'membros' not in st.session_state or "Felipe Berger" not in st.session_state.membros["Nome"].values:
    st.session_state.membros = pd.DataFrame(lista_membros_oficial)

# Menu Lateral de Acesso
st.sidebar.header("Controle de Acesso")
usuario_atual = st.sidebar.selectbox("Operador do Sistema", ["Selecione...", "Jonei Lima", "José Santana", "Damião Sobrinho"])

tem_permissao_adm = usuario_atual in ["Jonei Lima", "José Santana", "Damião Sobrinho"]

aba1, aba2 = st.tabs(["Gerar Escala Semanal", "Listas de Habilitados"])

with aba1:
    if not tem_permissao_adm:
        st.warning("Acesso Restrito: Selecione um operador autorizado no menu lateral para gerenciar as escalas.")
    else:
        st.header("Parâmetros da Escala Semanal")
        
        col_d1, col_d2 = st.columns(2)
        with col_d1:
            data_escolhida = st.date_input("Selecione o dia da Reunião", datetime.now())
            segunda_feira = data_escolhida - timedelta(days=data_escolhida.weekday())
            st.info(f"**Semana de {segunda_feira.strftime('%d/%m/%Y')}**")
        with col_d2:
            orador_domingo = st.text_input("Orador do Discurso Público (Domingo)", "Orador Local/Convidado")

        st.markdown("---")
        st.subheader("Designações Manuais (Presidência e Som)")
        col_m1, col_m2 = st.columns(2)
        
        df_membros = st.session_state.membros
        lista_pres_quinta = df_membros[df_membros["Pres_Quinta"] == True]["Nome"].tolist()
        lista_av = df_membros[df_membros["Audio_Video"] == True]["Nome"].tolist()
        
        with col_m1:
            presidente_q = st.selectbox("Presidente da Reunião", lista_pres_quinta)
            av_operador = st.selectbox("Operador de Áudio e Vídeo", lista_av)
            
        with col_m2:
            lista_anciaos_filtrada = df_membros[(df_membros["Cargo"] == "Anciao") & (df_membros["Nome"] != presidente_q)]["Nome"].tolist()
            dirigente_estudo = st.selectbox("Dirigente do Estudo Bíblico", lista_anciaos_filtrada)
            necessidades_locais = st.checkbox("Esta semana terá a parte de 'Necessidades Locais'?")
            
            anciao_nec_locais = "Não se aplica"
            if necessidades_locais:
                anciao_nec_locais = st.selectbox("Ancião para Necessidades Locais", [a for a in lista_anciaos_filtrada if a != dirigente_estudo])

        st.markdown("---")

        if st.button("Executar Inteligência e Montar Escala"):
            seed_data = int(segunda_feira.strftime("%Y%m%d"))
            random.seed(seed_data)
            
            # Bloqueio total de duplicidade com quem já está fixo nas funções principais
            indisponiveis_total = [presidente_q, dirigente_estudo, av_operador]
            if necessidades_locais:
                indisponiveis_total.append(anciao_nec_locais)
            
            # Sorteio dos Leitores sem conflito
            lista_leitura_biblia = df_membros[(df_membros["Leitura_Biblia"] == True) & (~df_membros["Nome"].isin(indisponiveis_total))]["Nome"].tolist()
            lista_leitor_estudo = df_membros[(df_membros["Leitor_Estudo"] == True) & (~df_membros["Nome"].isin(indisponiveis_total))]["Nome"].tolist()
            lista_leitor_sentinela = df_membros[(df_membros["Leitor_Sentinela"] == True) & (~df_membros["Nome"].isin(indisponiveis_total))]["Nome"].tolist()
            
            random.shuffle(lista_leitura_biblia)
            random.shuffle(lista_leitor_estudo)
            random.shuffle(lista_leitor_sentinela)
            
            leitor_b_fim = lista_leitura_biblia[0] if lista_leitura_biblia else "Disponível"
            
            leitor_e_fim = [i for i in lista_leitor_estudo if i != leitor_b_fim]
            leitor_e_fim = leitor_e_fim[0] if leitor_e_fim else "Disponível"
            
            leitor_s_fim = [i for i in lista_leitor_sentinela if i not in [leitor_b_fim, leitor_e_fim]]
            leitor_s_fim = leitor_s_fim[0] if leitor_s_fim else "Disponível"

            # Preparação da Fila do Bloco "Faça Seu Melhor" (Separação por gênero e remoção dos ocupados)
            estudantes_f = df_membros[(df_membros["Disc_Estudante"] == True) & (df_membros["Sexo"] == "F")]["Nome"].tolist()
            estudantes_m = df_membros[(df_membros["Disc_Estudante"] == True) & (df_membros["Sexo"] == "M") & (~df_membros["Nome"].isin(indisponiveis_total))]["Nome"].tolist()
            
            random.shuffle(estudantes_f)
            random.shuffle(estudantes_m)
            
            # Sorteio dos Auxiliares de Apoio
            todos_homens = df_membros[(df_membros["Cargo"] != "Anciao") & (df_membros["Nome"] != "Adalberto Pereira") & (df_membros["Sexo"] == "M")]["Nome"].tolist()
            homens_apoio = [i for i in todos_homens if i not in [leitor_b_fim, leitor_e_fim, leitor_s_fim] and i not in indisponiveis_total]
            random.shuffle(homens_apoio)
            
            volante = homens_apoio[0] if len(homens_apoio) > 0 else "Disponível"
            interno = homens_apoio[1] if len(homens_apoio) > 1 else "Disponível"
            externo = homens_apoio[2] if len(homens_apoio) > 2 else "Disponível"
            palco = homens_apoio[3] if len(homens_apoio) > 3 else "Disponível"

            col_res1, col_res2 = st.columns(2)
            with col_res1:
                st.success("### 🗓️ REUNIÃO DE MEIO DE SEMANA")
                st.markdown(f"**Presidente:** {presidente_q}")
                st.markdown(f"**Áudio e Vídeo:** {av_operador}")
                st.markdown(f"**Microfone Volante:** {volante}")
                st.markdown(f"**Indicador Interno:** {interno}")
                st.markdown(f"**Indicador Externo:** {externo}")
                st.markdown(f"**Microfone de Palco:** {palco}")
                st.markdown("---")
                st.markdown(f"**Leitura da Bíblia (4min):** {leitor_b_fim}")
                
                st.markdown("---")
                st.markdown("#### 🏫 Bloco: Faça Seu Melhor No Ministério")
                
                # Divisão visual limpa e explícita para Sala Principal e Sala B
                st.info("🏛️ **SALA PRINCIPAL**")
                st.write(f"**Designado:** {estudantes_f[0] if len(estudantes_f) > 0 else 'Disponível'}")
                st.write(f"**Ajudante:** {estudantes_f[1] if len(estudantes_f) > 1 else 'Disponível'}")
                
                st.warning("🚪 **SALA B**")
                st.write(f"**Designado:** {estudantes_m[0] if len(estudantes_m) > 0 else 'Disponível'}")
                st.write(f"**Ajudante:** {estudantes_m[1] if len(estudantes_m) > 1 else 'Disponível'}")
                
                st.markdown("---")
                if necessidades_locais:
                    st.write(f"**Necessidades Locais:** {anciao_nec_locais}")
                st.write(f"**Dirigente do Estudo Bíblico:** {dirigente_estudo}")
                st.write(f"**Leitor do Estudo Bíblico:** {leitor_e_fim}")

            with col_res2:
                st.success("### REUNIÃO DE FIM DE SEMANA")
                st.markdown(f"**Áudio e Vídeo (Espelhado):** {av_operador}")
                st.markdown(f"**Microfone Volante (Espelhado):** {volante}")
                st.markdown(f"**Indicador Interno (Espelhado):** {interno}")
                st.markdown(f"**Indicador Externo (Espelhado):** {externo}")
                st.markdown(f"**Microfone de Palco (Espelhado):** {palco}")
                st.markdown("---")
                st.write(f"**Discurso Público:** {orador_domingo}")
                st.write(f"**Leitor de A Sentinela:** {leitor_s_fim}")

with aba2:
    st.header("Verificação de Habilitados por Categoria")
    col_l1, col_l2 = st.columns(2)
    with col_l1:
        st.subheader("Irmãs Cadastradas (Treinamento)")
        st.dataframe(st.session_state.membros[(st.session_state.membros["Disc_Estudante"] == True) & (st.session_state.membros["Sexo"] == "F")][["Nome"]], hide_index=True)
    with col_l2:
        st.subheader("Operadores de Som Autorizados")
        st.dataframe(st.session_state.membros[st.session_state.membros["Audio_Video"] == True][["Nome"]], hide_index=True)
