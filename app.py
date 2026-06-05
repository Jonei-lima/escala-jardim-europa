import streamlit as st

st.subheader("📝 Configuração do Bloco: Faça Seu Melhor")

# Mapeamento das regras de negócio (Atrás dos panos)
REGRAS_PARTES = {
    "Iniciando conversas": {
        "Casa em Casa": "Sorteia uma dupla (qualquer gênero ou casados).",
        "Testemunho Informal": "Sorteia uma dupla.",
        "Testemunho Público": "Sorteia uma dupla."
    },
    "Cultivando o interesse": {
        "Casa em Casa": "Sorteia uma dupla.",
        "Testemunho Informal": "Sorteia uma dupla (preferência para quem iniciou na semana anterior)."
    },
    "Discurso": {
        "Sem cenário": "Filtro estrito: Sorteia apenas homens (exclui anciãos)."
    },
    "Fazendo discípulos": {
        "Longo / Estudo": "Sorteia uma dupla."
    },
    "Explicando suas crenças": {
        "Demonstração": "Sorteia uma dupla ou participante solo, dependendo do pedido."
    }
}

# Pegando a quantidade de partes do slider que já está na sua tela
qtd_partes = st.slider("Quantidade de partes dinâmicas no Bloco 'Faça Seu Melhor'", 1, 3, 3)

# Dicionário para salvar o que o usuário escolheu em cada parte
configuracao_semana = {}

for i in range(1, qtd_partes + 1):
    st.markdown(f"#### Parte {i}")
    col1, col2 = st.columns(2)
    
    with col1:
        tipo_selecionado = st.selectbox(
            f"Tipo de Parte (Parte {i})",
            options=list(REGRAS_PARTES.keys()),
            key=f"tipo_{i}"
        )
        
    with col2:
        # Filtra as variantes baseadas no tipo de parte escolhido acima
        variantes_disponiveis = list(REGRAS_PARTES[tipo_selecionado].keys())
        variante_selecionada = st.selectbox(
            f"Cenário / Variante (Parte {i})",
            options=variantes_disponiveis,
            key=f"variante_{i}"
        )
    
    # Guarda a escolha e a regra que o algoritmo deve executar
    configuracao_semana[f"parte_{i}"] = {
        "tipo": tipo_selecionado,
        "variante": variante_selecionada,
        "regra_tratamento": REGRAS_PARTES[tipo_selecionado][variante_selecionada]
    }
    
    # Exibe discretamente a regra ativa para conferência durante os testes
    st.caption(f"🤖 *Regra ativa:* {REGRAS_PARTES[tipo_selecionado][variante_selecionada]}")
    st.write("---")
