📊 Relatório Operacional – Tanaka
Este projeto é uma aplicação desenvolvida em Python utilizando Streamlit para gerar relatórios operacionais a partir de uma planilha Excel. A ferramenta é voltada para o acompanhamento de indicadores logísticos, produtividade da equipe e uso de veículos.

🚀 Funcionalidades
Upload de planilha .xlsx com os dados operacionais.

Cálculo automático de KPIs:

Total de Pedidos

Média de Colaboradores

Total de Peso

Total de Ocorrências e Avarias

Produtividade por Colaborador

Visualização gráfica:

Uso de veículos

Total por setor

Pedidos por dia

Exibição da base de dados original (com opção de expandir ou ocultar).

🛠️ Tecnologias Utilizadas
Python 3.10+

Streamlit

Pandas

Seaborn

Matplotlib

OpenPyXL (para leitura de arquivos Excel)

📂 Estrutura de Arquivos
bash
Copiar
Editar
.
├── app.py                  # Código principal do Streamlit
├── pythonlog.xlsx          # Planilha de exemplo com os dados operacionais
└── README.md               # Documentação do projeto
🧾 Requisitos
Certifique-se de ter o Python instalado e depois instale as dependências com:

bash
Copiar
Editar
pip install -r requirements.txt
Exemplo de requirements.txt:

nginx
Copiar
Editar
streamlit
pandas
openpyxl
matplotlib
seaborn
▶️ Como Executar
Coloque o arquivo pythonlog.xlsx na mesma pasta do app.py ou use o upload via interface.

Execute o Streamlit com o comando:

bash
Copiar
Editar
streamlit run app.py
Acesse no navegador: http://localhost:8501

📌 Observações
O arquivo padrão é pythonlog.xlsx com a aba chamada Página1.

Caso deseje utilizar outro arquivo ou aba, utilize as opções na barra lateral esquerda da aplicação.
