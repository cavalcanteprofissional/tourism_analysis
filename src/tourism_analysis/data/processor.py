import pandas as pd
import streamlit as st

class DataProcessor:
    def __init__(self):
        self.nordeste_ufs = [
            'Alagoas', 'Bahia', 'Ceará', 'Maranhão', 
            'Paraíba', 'Pernambuco', 'Piauí', 
            'Rio Grande do Norte', 'Sergipe'
        ]
    
    def unify_column_names(self, df, year):
        """Padroniza nomes de colunas entre diferentes anos"""
        column_mapping = {
            'cod continente': 'Ordem continente',
            'cod pais': 'Ordem país', 
            'cod uf': 'Ordem UF',
            'cod via': 'Ordem via de acesso',
            'cod mes': 'Ordem mês',
            'ano': 'Ano',
            'Via': 'Via de acesso'
        }
        
        df = df.rename(columns=column_mapping)
        
        # Garante que a coluna Ano existe
        if 'Ano' not in df.columns:
            df['Ano'] = year
            
        return df
    
    def filter_northeast_data(self, df):
        """Filtra dados apenas para estados do Nordeste"""
        if 'UF' not in df.columns:
            st.warning("Dataset não contém coluna UF")
            return df
            
        nordeste_df = df[df['UF'].isin(self.nordeste_ufs)].copy()
        return nordeste_df
    
    def consolidate_data(self, datasets):
        """Consolida todos os datasets em um único DataFrame"""
        consolidated_data = []
        
        for name, df in datasets.items():
            # Para dados de exemplo, usar anos do próprio DataFrame
            if 'SAMPLE' in name or 'DATA' in name:
                # Se já tem coluna Ano, usar ela
                if 'Ano' in df.columns:
                    df_processed = df.copy()
                else:
                    # Se não tem, criar anos aleatórios
                    df_processed = self.unify_column_names(df, 2023)
            else:
                # Para dados reais, tentar extrair o ano do nome
                try:
                    year = int(name.split('_')[1])
                    df_processed = self.unify_column_names(df, year)
                except (ValueError, IndexError):
                    # Se não conseguir extrair o ano, usar um padrão
                    st.warning(f"Não foi possível extrair ano do dataset {name}, usando 2023 como padrão")
                    df_processed = self.unify_column_names(df, 2023)
            
            df_nordeste = self.filter_northeast_data(df_processed)
            
            if not df_nordeste.empty:
                consolidated_data.append(df_nordeste)
        
        if consolidated_data:
            return pd.concat(consolidated_data, ignore_index=True)
        else:
            st.error("Nenhum dado foi consolidado. Verifique a estrutura dos dados.")
            return pd.DataFrame()