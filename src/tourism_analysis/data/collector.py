import pandas as pd
import streamlit as st
import numpy as np
from datetime import datetime

class DataCollector:
    def __init__(self):
        self.nordeste_ufs = [
            'Alagoas', 'Bahia', 'Ceará', 'Maranhão', 
            'Paraíba', 'Pernambuco', 'Piauí', 
            'Rio Grande do Norte', 'Sergipe'
        ]
        
        self.paises = ['Argentina', 'Estados Unidos', 'Portugal', 'França', 'Alemanha', 
                      'Itália', 'Espanha', 'Reino Unido', 'Chile', 'Uruguai']
        
        self.continentes = ['América', 'Europa', 'Ásia', 'Oceania', 'África']
        
        self.vias_acesso = ['Aérea', 'Terrestre', 'Marítima']
        
        self.meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
                     'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

    def generate_sample_data(self, years=5):
        """Gera dados de exemplo realistas para demonstração"""
        st.info("🎲 Gerando dados de exemplo realistas...")
        
        records_per_year = 5000
        total_records = records_per_year * years
        
        data = []
        
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        for i in range(total_records):
            year = 2019 + (i // records_per_year) % years
            uf = np.random.choice(self.nordeste_ufs)
            pais = np.random.choice(self.paises)
            continente = 'Europa' if pais in ['Portugal', 'França', 'Alemanha', 'Itália', 'Espanha', 'Reino Unido'] else \
                        'América' if pais in ['Argentina', 'Estados Unidos', 'Chile', 'Uruguai'] else 'Ásia'
            via = np.random.choice(self.vias_acesso)
            mes = np.random.choice(self.meses)
            
            # Gerar chegadas realistas baseadas em padrões
            base_arrivals = np.random.poisson(10)  # Base de chegadas
            
            # Ajustar por fatores sazonais
            if mes in ['janeiro', 'julho', 'dezembro']:  # Alta temporada
                base_arrivals *= 2
            elif mes in ['fevereiro', 'março', 'abril']:  # Baixa temporada
                base_arrivals *= 0.7
            
            # Ajustar por UF (Bahia e Pernambuco têm mais turistas)
            if uf in ['Bahia', 'Pernambuco']:
                base_arrivals *= 1.5
            elif uf in ['Alagoas', 'Piauí']:
                base_arrivals *= 0.8
            
            # Ajustar por ano (crescimento simulado)
            year_factor = 1 + (year - 2019) * 0.1  # 10% de crescimento ao ano
            base_arrivals *= year_factor
            
            chegadas = max(1, int(base_arrivals))
            
            data.append({
                'Continente': continente,
                'País': pais,
                'UF': uf,
                'Via de acesso': via,
                'Ano': year,
                'Mês': mes,
                'Chegadas': chegadas
            })
            
            if i % 500 == 0:
                progress = (i + 1) / total_records
                progress_bar.progress(progress)
                status_text.text(f"Gerando dados... {i+1}/{total_records}")
        
        progress_bar.progress(1.0)
        status_text.text("✅ Dados gerados com sucesso!")
        
        df = pd.DataFrame(data)
        
        # Adicionar colunas de ordem para compatibilidade
        df['Ordem continente'] = df['Continente'].map({'América': 1, 'Europa': 2, 'Ásia': 3, 'Oceania': 4, 'África': 5})
        df['Ordem país'] = range(1, len(df) + 1)
        df['Ordem UF'] = df['UF'].map({uf: i+1 for i, uf in enumerate(self.nordeste_ufs)})
        df['Ordem via de acesso'] = df['Via de acesso'].map({'Aérea': 1, 'Terrestre': 2, 'Marítima': 3})
        df['Ordem mês'] = df['Mês'].map({mes: i+1 for i, mes in enumerate(self.meses)})
        
        return {'SAMPLE_DATA': df}

    def get_sample_data_quick(self):
        """Gera dados de exemplo mais rapidamente"""
        st.info("⚡ Gerando dados de exemplo...")
        
        # Dados mais compactos mas ainda realistas
        np.random.seed(42)  # Para reproducibilidade
        
        records = 10000
        
        data = {
            'Continente': np.random.choice(self.continentes, records, p=[0.4, 0.3, 0.15, 0.1, 0.05]),
            'País': np.random.choice(self.paises, records),
            'UF': np.random.choice(self.nordeste_ufs, records, p=[0.2, 0.18, 0.15, 0.1, 0.09, 0.12, 0.06, 0.05, 0.05]),
            'Via de acesso': np.random.choice(self.vias_acesso, records, p=[0.7, 0.2, 0.1]),
            'Ano': np.random.choice([2019, 2020, 2021, 2022, 2023], records, p=[0.15, 0.1, 0.2, 0.25, 0.3]),
            'Mês': np.random.choice(self.meses, records),
        }
        
        df = pd.DataFrame(data)
        
        # Gerar chegadas realistas - corrigir o dtype
        chegadas = np.random.poisson(15, records)
        df['Chegadas'] = chegadas.astype(int)
        
        # Ajustar por fatores sazonais e regionais - CORRIGIDO
        high_season_mask = df['Mês'].isin(['janeiro', 'julho', 'dezembro'])
        df.loc[high_season_mask, 'Chegadas'] = (df.loc[high_season_mask, 'Chegadas'] * 2).astype(int)
        
        popular_states_mask = df['UF'].isin(['Bahia', 'Pernambuco'])
        df.loc[popular_states_mask, 'Chegadas'] = (df.loc[popular_states_mask, 'Chegadas'] * 1.5).astype(int)
        
        # Adicionar colunas de ordem
        df['Ordem continente'] = df['Continente'].map({cont: i+1 for i, cont in enumerate(self.continentes)})
        df['Ordem país'] = range(1, len(df) + 1)
        df['Ordem UF'] = df['UF'].map({uf: i+1 for i, uf in enumerate(self.nordeste_ufs)})
        df['Ordem via de acesso'] = df['Via de acesso'].map({'Aérea': 1, 'Terrestre': 2, 'Marítima': 3})
        df['Ordem mês'] = df['Mês'].map({mes: i+1 for i, mes in enumerate(self.meses)})
        
        st.success(f"✅ Gerados {len(df)} registros de exemplo")
        
        return {'SAMPLE_DATA': df}