import streamlit as st
import pandas as pd
from data.collector import DataCollector
from data.processor import DataProcessor
from visualization.charts import ChartBuilder

def main():
    st.set_page_config(
        page_title="Análise de Turismo - Nordeste",
        page_icon="🇧🇷",
        layout="wide"
    )
    
    st.title("🏖️ Análise de Dados de Turismo - Região Nordeste")
    st.markdown("""
    ### Estudo de caso sobre fluxo de turistas internacionais no Nordeste brasileiro
    
    **💡 Esta é uma demonstração com dados simulados** que replicam os padrões reais do turismo na região.
    """)
    
    # Inicialização dos módulos
    collector = DataCollector()
    processor = DataProcessor()
    charts = ChartBuilder()
    
    # Sidebar
    st.sidebar.title("🎯 Configurações")
    
    st.sidebar.markdown("""
    **Opções de Dados:**
    - ⚡ **Rápido**: Dados básicos (instantâneo)
    - 📊 **Completo**: Dados detalhados (alguns segundos)
    """)
    
    col1, col2 = st.sidebar.columns(2)
    
    with col1:
        if st.button("⚡ Dados Rápidos", use_container_width=True):
            with st.spinner("Gerando dados de exemplo..."):
                datasets = collector.get_sample_data_quick()
                st.session_state.datasets = datasets
                consolidated_data = processor.consolidate_data(datasets)
                st.session_state.consolidated_data = consolidated_data
                st.success("✅ Dados rápidos carregados!")
    
    with col2:
        if st.button("📊 Dados Completos", use_container_width=True):
            with st.spinner("Gerando dados detalhados... (isso pode levar alguns segundos)"):
                datasets = collector.generate_sample_data(years=5)
                st.session_state.datasets = datasets
                consolidated_data = processor.consolidate_data(datasets)
                st.session_state.consolidated_data = consolidated_data
                st.success("✅ Dados completos carregados!")
    
    st.sidebar.markdown("---")
    st.sidebar.info("""
    **Sobre os dados:**
    - 📅 Período: 2019-2023
    - 🗺️ Estados do Nordeste
    - ✈️ Dados de chegadas internacionais
    - 🎲 Dados simulados com padrões realistas
    """)
    
    # Verifica se os dados estão carregados
    if 'consolidated_data' not in st.session_state:
        st.info("""
        ## 👋 Bem-vindo à Análise de Turismo do Nordeste!
        
        **Para começar, escolha uma opção na sidebar:**
        
        - **⚡ Dados Rápidos**: Ideal para teste rápido
        - **📊 Dados Completos**: Para análise mais detalhada
        
        ---
        
        **📈 O que você pode analisar:**
        - Evolução temporal do turismo
        - Distribuição por estados
        - Principais países de origem
        - Vias de acesso preferenciais
        - Sazonalidade mensal
        """)
        
        # Mostrar preview dos dados
        st.subheader("📋 Preview da Estrutura de Dados")
        sample_preview = pd.DataFrame({
            'Ano': [2023, 2023, 2022, 2022],
            'Mês': ['janeiro', 'julho', 'dezembro', 'junho'],
            'UF': ['Bahia', 'Pernambuco', 'Ceará', 'Rio Grande do Norte'],
            'País': ['Argentina', 'Portugal', 'Estados Unidos', 'França'],
            'Continente': ['América', 'Europa', 'América', 'Europa'],
            'Via de acesso': ['Aérea', 'Aérea', 'Terrestre', 'Marítima'],
            'Chegadas': [150, 280, 90, 45]
        })
        st.dataframe(sample_preview, use_container_width=True)
        
        return
    
    # Dados carregados - mostrar análise
    data = st.session_state.consolidated_data
    
    # Métricas rápidas no topo
    st.subheader("📈 Métricas Principais")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        total_tourists = data['Chegadas'].sum()
        st.metric("Total de Turistas", f"{total_tourists:,.0f}")
    
    with col2:
        years_covered = f"{data['Ano'].min()} - {data['Ano'].max()}"
        st.metric("Período", years_covered)
    
    with col3:
        states_covered = data['UF'].nunique()
        st.metric("Estados", states_covered)
    
    with col4:
        avg_per_year = int(data.groupby('Ano')['Chegadas'].sum().mean())
        st.metric("Média/Ano", f"{avg_per_year:,.0f}")
    
    # Abas para organização
    tab1, tab2, tab3, tab4 = st.tabs([
        "📊 Visão Geral", 
        "🗺️ Análise Geográfica", 
        "📈 Tendências Temporais", 
        "🔍 Dados Detalhados"
    ])
    
    with tab1:
        st.header("Visão Geral do Turismo no Nordeste")
        
        # Gráfico de tendência
        trend_chart = charts.create_trend_chart(data)
        if trend_chart:
            st.plotly_chart(trend_chart, use_container_width=True)
        
        # Distribuição por continente
        col1, col2 = st.columns(2)
        
        with col1:
            continent_chart = charts.create_continent_chart(data)
            if continent_chart:
                st.plotly_chart(continent_chart, use_container_width=True)
        
        with col2:
            via_chart = charts.create_transport_chart(data)
            if via_chart:
                st.plotly_chart(via_chart, use_container_width=True)
    
    with tab2:
        st.header("Análise Geográfica")
        
        states_chart = charts.create_top_states_chart(data)
        if states_chart:
            st.plotly_chart(states_chart, use_container_width=True)
        
        # Mapa de calor por mês e estado
        heatmap_chart = charts.create_heatmap_chart(data)
        if heatmap_chart:
            st.plotly_chart(heatmap_chart, use_container_width=True)
    
    with tab3:
        st.header("Tendências Temporais")
        
        # Filtro por ano
        year_range = st.slider(
            "Selecione o intervalo de anos:",
            min_value=int(data['Ano'].min()),
            max_value=int(data['Ano'].max()),
            value=(int(data['Ano'].min()), int(data['Ano'].max()))
        )
        
        filtered_data = data[(data['Ano'] >= year_range[0]) & (data['Ano'] <= year_range[1])]
        
        if not filtered_data.empty:
            st.write(f"**Dados de {year_range[0]} a {year_range[1]}:** {filtered_data['Chegadas'].sum():,} chegadas no período")
            
            # Análise mensal
            monthly_chart = charts.create_monthly_trend_chart(filtered_data)
            if monthly_chart:
                st.plotly_chart(monthly_chart, use_container_width=True)
    
    with tab4:
        st.header("Dados Detalhados")
        
        st.dataframe(data, use_container_width=True)
        
        # Estatísticas
        st.subheader("📋 Estatísticas Descritivas")
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Chegadas por Ano:**")
            yearly_stats = data.groupby('Ano')['Chegadas'].sum()
            st.dataframe(yearly_stats)
        
        with col2:
            st.write("**Chegadas por Estado:**")
            state_stats = data.groupby('UF')['Chegadas'].sum().sort_values(ascending=False)
            st.dataframe(state_stats)
        
        # Download
        st.subheader("📥 Exportar Dados")
        csv = data.to_csv(index=False)
        st.download_button(
            label="💾 Download CSV",
            data=csv,
            file_name=f"turismo_nordeste_{datetime.now().strftime('%Y%m%d')}.csv",
            mime="text/csv"
        )

if __name__ == "__main__":
    main()