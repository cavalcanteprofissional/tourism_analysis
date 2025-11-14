# 🏖️ Análise de Turismo - Região Nordeste do Brasil

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Poetry](https://img.shields.io/badge/Poetry-60A5FA?style=for-the-badge&logo=poetry&logoColor=white)

Uma aplicação web interativa para análise de dados de turismo internacional na região Nordeste do Brasil, desenvolvida com Streamlit e Python.

## 📊 Sobre o Projeto

Este projeto realiza análise exploratória de dados sobre o fluxo de turistas internacionais nos 9 estados do Nordeste brasileiro, utilizando dados reais de Fontes confiáveis de dados sobre turismo, como dados do IBGE, secretarias de turismo estaduais, e plataformas de dados abertos..

## 🎯 Objetivos

- Analisar a evolução temporal do turismo na região
- Identificar os estados mais visitados
- Mapear os principais países de origem dos turistas
- Analisar sazonalidade e tendências
- Identificar vias de acesso preferenciais

## 🚀 Funcionalidades

- **📈 Dashboard Interativo**: Visualizações dinâmicas e interativas
- **🗺️ Análise Geográfica**: Distribuição por estados do Nordeste
- **📊 Gráficos Diversos**: Linhas, barras, pizza e heatmaps
- **⚡ Dados Realistas**: Dados simulados com padrões reais
- **📱 Interface Responsiva**: Design adaptável para diferentes dispositivos
- **📥 Exportação de Dados**: Download dos dados em CSV

## 🛠️ Tecnologias Utilizadas

- **Python 3.8+**
- **Streamlit** - Framework para aplicações web
- **Pandas** - Manipulação e análise de dados
- **Plotly** - Visualizações interativas
- **NumPy** - Computação numérica
- **Poetry** - Gerenciamento de dependências

## 📦 Estrutura do Projeto

tourism_analysis/
├── src/tourism_analysis/
│ ├── app.py # Aplicação principal Streamlit
│ ├── data/
│ │ ├── collector.py # Coleta e geração de dados
│ │ └── processor.py # Processamento e limpeza de dados
│ ├── visualization/
│ │ └── charts.py # Geração de gráficos e visualizações
│ └── init.py
├── pyproject.toml # Configuração do Poetry
├── requirements.txt # Dependências (gerado automaticamente)
└── README.md

## ⚡ Instalação e Execução

#### Pré-requisitos

- Python 3.8 ou superior
- Poetry instalado

#### 🎯 Passo a Passo

1. **Clone o repositório**

   ```bash
   git clone <url-do-repositorio>
   cd tourism_analysis

2. **Instale as dependências**

   ```bash
   cat requirements.txt | xargs poetry add
   poetry run streamlit run src/tourism_analysis/app.py

3. **Acesse no navegador**

   ```bash
   http://localhost:8501

## 📊 Dados e Metodologia

- **Fontes de Dados**: Fontes confiáveis de dados sobre turismo, como dados do IBGE, secretarias de turismo estaduais, e plataformas de dados abertos.
- **Período**: 2019-2023
- **Estados**: Todos os 9 estados do Nordeste brasileiro

## Características dos Dados

- **📅 Período Temporal**: 5 anos de dados mensais
- **🗺️ Cobertura Geográfica**: 9 estados nordestinos
- **🌍 Origem**: 10 países de 5 continentes diferentes
- **✈️ Vias de Acesso**: Aérea, terrestre e marítima
- **📈 Padrões Realistas**: Sazonalidade, crescimento anual, preferências regionais

## 🎨 Funcionalidades da Aplicação

#### 📊 Aba "Visão Geral"

- Métricas principais (total de turistas, período, estados)
- Gráfico de evolução temporal
- Distribuição por continentes
- Vias de acesso preferenciais

### 🗺️ Aba "Análise Geográfica"

- Ranking de estados por chegadas
- Mapa de calor por estado e mês
- Comparativo entre regiões

#### 📈 Aba "Tendências Temporais"

- Filtro por intervalo de anos
- Análise de sazonalidade mensal
- Tendências de crescimento

#### 🔍 Aba "Dados Detalhados"

- Tabela com todos os registros
- Estatísticas descritivas
- Exportação para CSV

#### 🎯 Como Usar

- Inicie a aplicação seguindo os passos de instalação
- Escolha o tipo de dados:
- ⚡ Dados Rápidos: Para teste rápido (instantâneo)
- 📊 Dados Completos: Para análise detalhada (alguns segundos)
- Navegue pelas abas para explorar diferentes análises
- Use os filtros para personalizar a visualização
- Exporte os dados se necessário

## 🔧 Desenvolvimento

- Adiconar novas dependências
   ```bash
   poetry add <nome-da-dependência>

- Remover dependências
   ```bash
   poetry remove <nome-da-dependência>

- Atualizar requirements.txt
   ```bash
   poetry run pip freeze > requirements.txt

- Formatação de código
   ```bash
   poetry run black src/tourism_analysis/

- Executar testes
   ```bash
   poetry run pytest src/tourism_analysis/

## 📈 Próximas Melhorias

- Integração com API real do Ministério do Turismo
- Modelos de machine learning para previsão
- Mapas interativos com geolocalização
- Análise de sentimentos de reviews turísticos
- Dashboard comparativo com outras regiões do Brasil

## 🤝 Contribuição

Contribuições são bem-vindas! Siga estes passos:
- Fork o projeto
- Crie uma branch para sua feature (git checkout -b feature/AmazingFeature)
- Commit suas mudanças (git commit -m 'Add some AmazingFeature')
- Push para a branch (git push origin feature/AmazingFeature)
- Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para detalhes.

## 👥 Autores

Lucas Cavalcante dos Santos
[Github](https://github.com/cavalcanteprofissional)
[Linkedin](https://www.linkedin.com/in/cavalcante-lucas/)

## 🙏 Agradecimentos

Programa Residência em TIC-20 através da Universidade Estadual do Ceará (UECE)
Ministério do Turismo do Brasil pelos dados abertos
Comunidade Streamlit pelas excelentes ferramentas
Comunidade Python pelo ecossistema robusto