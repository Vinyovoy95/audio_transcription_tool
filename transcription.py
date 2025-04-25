import os
import zipfile
import json
import whisper
from pathlib import Path
from pydub.utils import mediainfo
from datetime import datetime
from tqdm import tqdm

try:
    import rarfile
    rar_disponivel = True
except ImportError:
    print("⚠️ Módulo 'rarfile' não instalado. Arquivos .rar serão ignorados.")
    rar_disponivel = False

def descompactar_arquivos(diretorio):
    for root, _, files in os.walk(diretorio):
        for file in files:
            caminho = os.path.join(root, file)
            try:
                if file.endswith('.zip'):
                    with zipfile.ZipFile(caminho, 'r') as zip_ref:
                        zip_ref.extractall(root)
                elif file.endswith('.rar') and rar_disponivel:
                    with rarfile.RarFile(caminho, 'r') as rar_ref:
                        rar_ref.extractall(root)
            except Exception as e:
                print(f"[ERRO] Falha ao descompactar {file}: {e}")

def buscar_audios(diretorio, extensoes=None):
    if extensoes is None:
        extensoes = ['.mp3', '.wav', '.m4a', '.aac', '.flac', '.ogg', '.caf', '.amr', '.opus']
    arquivos_audio = []
    for root, _, files in os.walk(diretorio):
        for file in files:
            if any(file.lower().endswith(ext) for ext in extensoes):
                arquivos_audio.append(Path(root) / file)
    return arquivos_audio

def coletar_metadados(caminho_audio):
    try:
        info = mediainfo(str(caminho_audio))
        duracao = float(info['duration']) if 'duration' in info else 0
    except:
        duracao = 0
    stat = caminho_audio.stat()
    return {
        "arquivo": caminho_audio.name,
        "caminho": str(caminho_audio.resolve()),
        "tamanho_MB": round(stat.st_size / (1024 * 1024), 2),
        "duracao_segundos": duracao,
        "data_modificacao": datetime.fromtimestamp(stat.st_mtime).isoformat()
    }

def transcrever_audio(modelo, caminho_audio):
    try:
        resultado = modelo.transcribe(str(caminho_audio))
        return resultado.get("text", "").strip()
    except Exception as e:
        return f"[ERRO] Transcrição falhou: {e}"

def main():
    dir_base = input("📂 Diretório para análise: ").strip()
    dir_base = Path(dir_base).resolve()
    if not dir_base.exists():
        print("❌ Diretório não encontrado.")
        return

    print("🔍 Descompactando arquivos...")
    descompactar_arquivos(dir_base)

    print("🎧 Buscando arquivos de áudio...")
    arquivos = buscar_audios(dir_base)
    print(f"✅ {len(arquivos)} arquivos de áudio encontrados.")

    print("🚀 Carregando modelo Whisper...")
    modelo = whisper.load_model("base")  # Pode usar "medium" ou "large" para maior qualidade

    resultados = []

    for audio_path in tqdm(arquivos, desc="📝 Transcrevendo"):
        metadados = coletar_metadados(audio_path)
        texto = transcrever_audio(modelo, audio_path)
        metadados["transcricao"] = texto
        resultados.append(metadados)

    pasta_saida = input("📁 Onde salvar os relatórios de transcrição? ").strip()
    pasta_saida = Path(pasta_saida).resolve()
    pasta_saida.mkdir(parents=True, exist_ok=True)

    nome_arquivo = f"relatorio_transcricao_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    caminho_saida = pasta_saida / nome_arquivo

    with open(caminho_saida, 'w', encoding='utf-8') as f:
        json.dump(resultados, f, ensure_ascii=False, indent=4)

    print(f"\n✅ Transcrições salvas em: {caminho_saida}")

if __name__ == "__main__":
    main()
