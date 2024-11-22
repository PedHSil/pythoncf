#pip install schedule

import argparse
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import csv
import json
import pandas as pd
from datetime import datetime
import schedule
import time

# Configuração da autenticação do Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='CHANGE_THIS',
                                               client_secret='CHANGE_THIS',
                                               redirect_uri='http://localhost:8888/callback',
                                               scope='playlist-modify-public playlist-read-private user-library-read user-read-recently-played'))

# Função para coletar os dados do Spotify
def get_recent_tracks(limit=20):
    recent_tracks = sp.current_user_recently_played(limit=limit)
    tracks = []
    for item in recent_tracks['items']:
        track = item['track']
        tracks.append({
            'nome': track['name'],
            'artista': track['artists'][0]['name'],
            'album': track['album']['name'],
            'duracao': track['duration_ms'] / 60000,  # duração em minutos
            'data_reproducao': item['played_at']
        })
    return tracks

# Função para salvar os dados em cache
def save_to_cache(data, filename='musicas_cache.json'):
    with open(filename, 'w') as f:
        json.dump(data, f)
    print(f"Dados salvos em {filename}")

# Função para ler os dados do cache
def load_from_cache(filename='musicas_cache.json'):
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        return None

# Função para exportar os dados para CSV
def export_music_data(limit, output_file):
    recent_tracks = get_recent_tracks(limit=limit)
    
    with open(output_file, 'w', newline='', encoding='utf8') as csvfile:
        spawriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        spawriter.writerow(['Nome da Música', 'Artista', 'Álbum', 'Duração (min:seg)', 'Data de Reprodução'])
        
        for track in recent_tracks:
            duration_min = int(track['duracao'])
            duration_sec = int((track['duracao'] - duration_min) * 60)
            played_at_datetime = datetime.strptime(track['data_reproducao'], "%Y-%m-%dT%H:%M:%S.%fZ")
            played_at_str = played_at_datetime.strftime("%d/%m/%Y %H:%M:%S")
            
            spawriter.writerow([track['nome'], track['artista'], track['album'], f"{duration_min}:{duration_sec:02d}", played_at_str])

    print(f"Músicas exportadas com sucesso para '{output_file}'!")

# Função para análise de dados com pandas
def analyze_music_data():
    recent_tracks = get_recent_tracks(limit=20)
    df = pd.DataFrame(recent_tracks)
    
    print("Duração média das músicas (em minutos):", df['duracao'].mean())
    print("Primeiras 5 músicas do histórico:")
    print(df.head())

# Função para obter recomendações com base em uma música
def get_recommendations(track_id):
    recommendations = sp.recommendations(seed_tracks=[track_id], limit=5)
    print("Músicas recomendadas com base na música:", track_id)
    for track in recommendations['tracks']:
        print(f"{track['name']} - {track['artists'][0]['name']}")

# Função agendada para exportar músicas
def job():
    print("Exportando músicas...")
    export_music_data(limit=20, output_file="musicas_exportadas.csv")
    analyze_music_data()

# Usar argparse para pegar os argumentos do terminal
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Exportar músicas do Spotify para CSV e realizar análise.")
    parser.add_argument('--limit', type=int, default=20, help="Número de músicas a exportar")
    parser.add_argument('--output', type=str, default="musicas.csv", help="Nome do arquivo de saída")
    parser.add_argument('--analyze', action='store_true', help="Realizar análise dos dados")
    parser.add_argument('--recommend', type=str, help="Obter recomendações com base na música (ID da música)")

    args = parser.parse_args()

    # Se o arquivo de cache existir, tenta carregar os dados
    cached_tracks = load_from_cache()
    if cached_tracks:
        print("Dados carregados do cache.")
    else:
        print("Nenhum cache encontrado. Buscando dados do Spotify...")
        cached_tracks = get_recent_tracks(limit=args.limit)
        save_to_cache(cached_tracks)

    # Exportação de músicas para CSV
    export_music_data(limit=args.limit, output_file=args.output)

    # Análise de dados com pandas, se solicitado
    if args.analyze:
        analyze_music_data()

    # Recomendação com base na ID da música
    if args.recommend:
        get_recommendations(args.recommend)

    # Agendar a execução semanal (ou em intervalos)
    schedule.every().week.do(job)
    while True:
        schedule.run_pending()
        time.sleep(60)  # Espera 1 minuto para rodar novamente
