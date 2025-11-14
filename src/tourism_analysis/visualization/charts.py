import plotly.express as px
import pandas as pd
import streamlit as st

class ChartBuilder:
    def create_trend_chart(self, data):
        """Cria gráfico de tendência temporal"""
        yearly_data = data.groupby('Ano')['Chegadas'].sum().reset_index()
        
        fig = px.line(
            yearly_data, 
            x='Ano', 
            y='Chegadas',
            title='📈 Evolução das Chegadas de Turistas no Nordeste',
            markers=True
        )
        fig.update_layout(
            xaxis_title='Ano',
            yaxis_title='Número de Chegadas',
            hovermode='x unified'
        )
        return fig
    
    def create_top_states_chart(self, data):
        """Cria gráfico dos estados mais visitados"""
        state_data = data.groupby('UF')['Chegadas'].sum().reset_index()
        state_data = state_data.sort_values('Chegadas', ascending=True)  # Para barras horizontais
        
        fig = px.bar(
            state_data,
            y='UF',
            x='Chegadas',
            title='🗺️ Chegadas por Estado do Nordeste',
            color='Chegadas',
            color_continuous_scale='viridis',
            orientation='h'
        )
        fig.update_layout(yaxis_title='Estado', xaxis_title='Chegadas')
        return fig
    
    def create_continent_chart(self, data):
        """Cria gráfico por continente de origem"""
        continent_data = data.groupby('Continente')['Chegadas'].sum().reset_index()
        
        fig = px.pie(
            continent_data,
            values='Chegadas',
            names='Continente',
            title='🌍 Distribuição por Continente de Origem'
        )
        return fig
    
    def create_transport_chart(self, data):
        """Cria gráfico por via de acesso"""
        via_data = data.groupby('Via de acesso')['Chegadas'].sum().reset_index()
        
        fig = px.bar(
            via_data,
            x='Via de acesso',
            y='Chegadas',
            title='✈️ Chegadas por Via de Acesso',
            color='Via de acesso'
        )
        return fig
    
    def create_heatmap_chart(self, data):
        """Cria mapa de calor por mês e estado"""
        heatmap_data = data.groupby(['UF', 'Mês'])['Chegadas'].sum().reset_index()
        
        # Ordenar meses corretamente
        meses_order = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
                      'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
        heatmap_data['Mês'] = pd.Categorical(heatmap_data['Mês'], categories=meses_order, ordered=True)
        
        fig = px.density_heatmap(
            heatmap_data,
            x='Mês',
            y='UF',
            z='Chegadas',
            title='🔥 Mapa de Calor: Chegadas por Estado e Mês',
            color_continuous_scale='viridis'
        )
        return fig
    
    def create_monthly_trend_chart(self, data):
        """Cria gráfico de tendência mensal"""
        monthly_data = data.groupby(['Ano', 'Mês'])['Chegadas'].sum().reset_index()
        
        # Ordenar meses
        meses_order = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
                      'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
        monthly_data['Mês'] = pd.Categorical(monthly_data['Mês'], categories=meses_order, ordered=True)
        monthly_data = monthly_data.sort_values(['Ano', 'Mês'])
        
        monthly_data['Ano-Mês'] = monthly_data['Ano'].astype(str) + '-' + monthly_data['Mês']
        
        fig = px.line(
            monthly_data,
            x='Ano-Mês',
            y='Chegadas',
            title='📅 Tendência Mensal de Chegadas',
            markers=True
        )
        fig.update_layout(xaxis_title='Ano-Mês', yaxis_title='Chegadas')
        fig.update_xaxes(tickangle=45)
        return fig