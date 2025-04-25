# Transcrição de Áudio - Fase de Testes

Este projeto é um script que utiliza o modelo Whisper para transcrever áudios de vários formatos. O código está em fase de testes e pode sofrer alterações significativas.

## Funcionalidades:
- Descompacta arquivos `.zip` e `.rar` (caso o módulo `rarfile` esteja disponível).
- Busca por arquivos de áudio em diretórios e subdiretórios.
- Transcreve os áudios encontrados utilizando o modelo Whisper.
- Gera relatórios em formato JSON com metadados e transcrições.

## Requisitos:
- Python 3.x
- Bibliotecas: `whisper`, `pydub`, `tqdm`, `rarfile` (opcional)

## Status do projeto:
- 🚧 **Em fase de testes.**
- ⚠️ Pode conter bugs ou falhas inesperadas.

## Como usar:
1. Clone este repositório.
2. Instale as dependências com `pip install -r requirements.txt`.
3. Execute o script com o comando `python script.py`.
4. Siga as instruções na tela para selecionar o diretório de entrada e saída.
