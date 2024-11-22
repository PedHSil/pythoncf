import argparse
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import csv
from datetime import datetime

'''# ID da playlist para verificar duplicatas
playlist_id = 'ID_DA_PLAYLIST'

# Buscar músicas da playlist
results = sp.playlist_tracks(playlist_id)
tracks = results['items']

# Encontrar duplicatas
track_ids = {}
duplicates = []

for item in tracks:
    track = item['track']
    if track['id'] in track_ids:
        duplicates.append(item['track']['id'])
    else:
        track_ids[track['id']] = True

# Remover duplicatas
if duplicates:
    sp.playlist_remove_specific_occurrences_of_items(playlist_id, [{'uri': uri} for uri in duplicates])
    print(f'{len(duplicates)} duplicatas removidas.')
else:
    print('Nenhuma duplicata encontrada.')'''

# Configuração da autenticação com o escopo correto
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id='5081c3fb65fe49f48a7801f422af1647',
    client_secret='12da4a76655a4d9e9778ed7c8382015e',
    redirect_uri='http://localhost:8888/callback',
    scope='user-read-recently-played'  # Adicione este escopo
))


# Obter o histórico das últimas músicas tocadas
recent_tracks = sp.current_user_recently_played(limit=20)

# Exibir informações das músicas ouvidas recentemente
print("Músicas ouvidas recentemente:")
for idx, item in enumerate(recent_tracks['items']):
    track = item['track']
    print(f"{idx + 1}. {track['name']} - {track['artists'][0]['name']} - {track['album']['name']}")
    
# Abrir o arquivo CSV e gravar os dados
with open('musicas.csv', 'w', newline='', encoding='utf8') as csvfile:
    '''open('musicas.csv', 'w') abre o arquivo chamado musicas.csv no modo de escrita ('w'). Se o arquivo não existir, ele será criado automaticamente. Caso já exista, ele será sobrescrito.
    newline='' evita que o Python insira uma linha em branco extra entre as linhas gravadas no CSV.
    encoding='utf8' garante que os caracteres especiais, como acentos e cedilhas, sejam corretamente salvos no arquivo.'''
    spawriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    '''csv.writer(csvfile) cria um objeto que pode escrever no arquivo csvfile aberto anteriormente.
        delimiter=',' define que as colunas no arquivo CSV serão separadas por uma vírgula (,) — que é o padrão em arquivos CSV.
        quotechar='"' indica que os valores contendo vírgulas ou caracteres especiais serão envoltos por aspas ("). Isso é importante para garantir que a vírgula não seja interpretada como delimitador.
        quoting=csv.QUOTE_MINIMAL faz com que as aspas sejam usadas apenas quando necessário (por exemplo, quando o valor contém vírgulas).'''
    
    # Escrever o cabeçalho do CSV
    spawriter.writerow(['Nome da Música', 'Artista', 'Álbum', 'Duração (min:seg)', 'Data de Reprodução'])
    
    # Loop para escrever cada música no arquivo
    for item in recent_tracks['items']:
        track = item['track']
        
        # Conversão da duração da música de milissegundos para min:seg
        duration_ms = track['duration_ms']
        duration_min = duration_ms // 60000
        duration_sec = (duration_ms % 60000) // 1000
        duration = f"{duration_min}:{duration_sec:02d}"
        
        # Data de reprodução com milissegundos e 'Z'
        played_at = item['played_at']
        played_at_datetime = datetime.strptime(played_at, "%Y-%m-%dT%H:%M:%S.%fZ")
        played_at_str = played_at_datetime.strftime("%d/%m/%Y %H:%M:%S")
        
        # Escrever os dados no CSV
        spawriter.writerow([track['name'], track['artists'][0]['name'], track['album']['name'], duration, played_at_str])

print("Músicas exportadas com sucesso para 'musicas.csv'!")