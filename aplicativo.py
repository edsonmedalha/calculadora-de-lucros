import streamlit as st

# Configuração da página
st.set_page_config(page_title="Cálculo de Lucros", page_icon="🧮")

# Título do aplicativo
st.title("🧮 Cálculo de Lucros")
st.subheader("Calculadora de Arbitragem para 3 Resultados")

st.markdown("---")

# Entradas do usuário na barra lateral
with st.sidebar:
    st.header("Insira os Dados")
    odd_a = st.number_input("Odd Time A Vence", min_value=1.0, value=2.5, step=0.01, format="%.2f")
    odd_empate = st.number_input("Odd Empate", min_value=1.0, value=3.0, step=0.01, format="%.2f")
    odd_b = st.number_input("Odd Time B Vence", min_value=1.0, value=4.0, step=0.01, format="%.2f")
    total_aposta = st.number_input("Valor Total a Apostar (R$)", min_value=1.0, value=100.0, step=1.0, format="%.2f")

# --- Lógica do Cálculo ---

# 1. Calcular a probabilidade implícita e a soma
try:
    prob_a = (1 / odd_a)
    prob_empate = (1 / odd_empate)
    prob_b = (1 / odd_b)
    soma_probs = prob_a + prob_empate + prob_b
except ZeroDivisionError:
    st.error("As odds devem ser maiores que zero.")
    st.stop()

# 2. Verificar se existe arbitragem
if soma_probs < 1:
    st.success(f"✅ Oportunidade de Arbitragem Encontrada!")
    
    # 3. Calcular os valores a serem apostados em cada resultado
    aposta_a = (prob_a / soma_probs) * total_aposta
    aposta_empate = (prob_empate / soma_probs) * total_aposta
    aposta_b = (prob_b / soma_probs) * total_aposta
    
    # 4. Calcular o lucro
    retorno_garantido = aposta_a * odd_a
    lucro_liquido = retorno_garantido - total_aposta
    percentual_lucro = (lucro_liquido / total_aposta) * 100
    
    st.markdown("### Resumo da Aposta")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Lucro Garantido", value=f"R$ {lucro_liquido:.2f}")
    with col2:
        st.metric(label="Retorno Percentual", value=f"{percentual_lucro:.2f}%")
        
    st.markdown("#### Quanto apostar em cada resultado:")
    
    st.info(f"**Aposte no Time A:** R$ {aposta_a:.2f}")
    st.info(f"**Aposte no Empate:** R$ {aposta_empate:.2f}")
    st.info(f"**Aposte no Time B:** R$ {aposta_b:.2f}")
    
    st.markdown("---")
    st.write(f"Ao fazer essas apostas, seu retorno será de **R$ {retorno_garantido:.2f}** independentemente do resultado final, garantindo seu lucro.")

else:
    percentual_acima = (soma_probs - 1) * 100
    st.error(f"❌ Não há oportunidade de arbitragem com essas odds.")
    st.warning(f"A soma das probabilidades é {soma_probs*100:.2f}%, o que representa uma perda garantida de aproximadamente {percentual_acima:.2f}%.")

st.markdown("---")
st.caption("Este aplicativo é uma ferramenta de cálculo e não garante resultados. Verifique sempre as odds nas casas de apostas antes de realizar qualquer operação.")
