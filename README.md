# Impressora Zebra - Impressão de Etiquetas ZPL

Este projeto permite a impressão de etiquetas ZPL usando uma impressora Zebra. A interface gráfica foi criada com Tkinter e permite a importação de arquivos CSV para gerar e imprimir etiquetas.

## Requisitos

- Python 3.10 ou superior
- Dependências listadas em `requirements.txt`

## Instalação

1. Clone o repositório:
   ```sh
   git clone https://github.com/seu-usuario/impressora-zebra.git
   cd impressora-zebra
   ```

2. Crie um ambiente virtual e ative-o:
   ```sh
   python -m venv venv
   venv\Scripts\activate  # No Windows
   source venv/bin/activate  # No Linux/Mac
   ```

3. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```

## Uso

1. Execute o script principal:
   ```sh
   python main.py
   ```

2. Na interface gráfica:
   - Clique em "Importar CSV" para selecionar um arquivo CSV.
   - Insira o nome da impressora Zebra.
   - Clique em "Imprimir" para gerar e imprimir as etiquetas.

## Empacotamento

Para criar um executável do projeto, use o PyInstaller:

1. Instale o PyInstaller:
   ```sh
   pip install pyinstaller
   ```

2. Crie o executável:
   ```sh
   pyinstaller --onefile --windowed --add-data "csvFile/tonner.csv;csvFile" main.py
   ```

3. O executável será gerado na pasta `dist`.

## Estrutura do Projeto

```
impressora-zebra/
├── csvFile/
│   └── tonner.csv
├── models/
│   └── modelZpl.py
├── zpl/
│   └── zpl.py
├── main.py
├── requirements.txt
└── README.md
```

## Dependências

As dependências do projeto estão listadas no arquivo `requirements.txt`:

```
altgraph==0.17.4
annotated-types==0.7.0
packaging==24.2
pefile==2023.2.7
pydantic==2.10.5
pydantic_core==2.27.2
pyinstaller==6.11.1
pyinstaller-hooks-contrib==2025.0
pywin32==308
pywin32-ctypes==0.2.3
setuptools==75.8.0
typing_extensions==4.12.2
zebra==0.1.0
```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
