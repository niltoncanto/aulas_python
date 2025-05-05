from abc import ABC, abstractmethod

# Classe abstrata Media (Mídia) que define o método abstrato 'play' (reproduzir).
class Media(ABC):
    @abstractmethod
    def play(self):
        pass

# Implementações concretas de Media para diferentes tipos de mídia.
class Audio(Media):
    def play(self):
        print("Reproduzindo áudio.")

class Video(Media):
    def play(self):
        print("Reproduzindo vídeo.")

# Implementação concreta de Media para indicar que nenhuma mídia foi selecionada.
class NullMedia(Media):
    def play(self):
        # Nenhuma mídia para reproduzir
        print("Nenhuma mídia selecionada.")

# Classe MediaPlayer que utiliza uma instância de Media para reproduzir a mídia.
class MediaPlayer:
    def __init__(self, media):
        self.media = media

    def play_media(self):
        self.media.play()

# Função cliente que utiliza um objeto MediaPlayer para reproduzir a mídia.
def client_code(media_player):
    media_player.play_media()

# Exemplo de uso:
# 1. Criamos instâncias das diferentes classes de mídia.
audio = Audio()
video = Video()
null_media = NullMedia()

# 2. Criamos instâncias do MediaPlayer e passamos a instância da mídia desejada.
# 3. Chamamos a função cliente para reproduzir a mídia usando o MediaPlayer.
# 4. Repetimos o processo para diferentes tipos de mídia.
player = MediaPlayer(audio)
client_code(player)

player = MediaPlayer(video)
client_code(player)

player = MediaPlayer(null_media)
client_code(player)


