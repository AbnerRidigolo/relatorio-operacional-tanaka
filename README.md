📊 Relatório Operacional – Tanaka

Dashboard interativo desenvolvido em Python com Streamlit para análise operacional baseada em dados de planilha Excel. O sistema gera KPIs, gráficos e insights de produtividade, ocorrências, uso de veículos e atividades por setor.

🚀 Funcionalidades
📥 Upload de planilha .xlsx com dados operacionais

📊 Exibição de indicadores chave:

Total de pedidos

Média de colaboradores

Peso total movimentado

Ocorrências e avarias

Produtividade por colaborador

📈 Gráficos:

Uso de veículos por tipo

Total por setor (recebimento, expedição, organização, embalamento)

Evolução de pedidos por data

🔍 Visualização completa do DataFrame original carregado

🛠️ Tecnologias Utilizadas
Python 3.10+

Streamlit

Pandas

Matplotlib

Seaborn

openpyxl (para leitura de arquivos .xlsx)

📂 Estrutura esperada da planilha
A aba da planilha (Página1 por padrão) deve conter, ao menos, as seguintes colunas:

DATA

QTD PEDIDOS

QTD.COLABORADORES

PESO TOTAL

OCORRÊNCIAS

AVARIAS

QTD VUC, QTD DUCATO, QTD HR, QTD FIORINO, QTD MONTANA, QTD SAVEIRO

RECEBIMENTOS, EXPEDIÇÃO, ORGANIZAÇÃO INTERNA, EMBALAMENTO

▶️ Como executar
Clone o repositório:

bash
Copiar
Editar
git clone https://github.com/seu-usuario/relatorio-operacional-tanaka.git
cd relatorio-operacional-tanaka
Crie e ative um ambiente virtual (opcional, mas recomendado):

bash
Copiar
Editar
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
Instale as dependências:

bash
Copiar
Editar
pip install -r requirements.txt
Execute o app:

bash
Copiar
Editar
streamlit run app.py
📎 Exemplo de uso

Interface do dashboard com KPIs e gráficos interativos.

📌 Observações
Um arquivo de exemplo chamado pythonlog.xlsx pode ser usado como base para os dados.

O app pode ser usado com upload manual ou com o arquivo padrão presente na raiz do projeto.

Todas as transformações e agregações estão cacheadas para desempenho com @st.cache_data.
