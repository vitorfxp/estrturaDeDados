class musica:
    def __init__(self, titulo, artista):
        self.titulo = titulo
        self.artista = artista
        self.proximo = None
        self.anterior = None
    
    def __str__(self):
        return f"{self.titulo} - {self.artista}"

class playlist: 
    def __init__(self):
        self.atual = None
        self.tamanho = 0 
    
    def adicionar_musica(self, titulo, artista):
        nova_musica = musica(titulo , artista)

        if self.tamanho == 0:
            self.atual = nova_musica
            nova_musica.proximo = nova_musica
            nova_musica.anterior = nova_musica
        else:
            nova_musica.proximo = self.atual.proximo
            nova_musica.anterior = self.atual
            self.atual.proximo.anterior = nova_musica
            self.atual.proximo = nova_musica

        self.tamanho += 1 

    def proxima_musica(self):
        if self.atual:
            self.atual = self.atual.proximo 
        return self.atual
        
    def musica_anterior(self):
        if self.atual:
            self.atual = self.atual.anterior
        return self.atual

def exemplo_playlist():
    minha_playlist = playlist ()

    minha_playlist.adicionar_musica("bohemian rhapsody", "Queen")
    minha_playlist.adicionar_musica("Piscar de olhos","pumapjl")
    minha_playlist.adicionar_musica("Rises the moon","Liana flores")
    minha_playlist.adicionar_musica("Judas","Lady gaga")

    print("Playlist Criada!")
    print(f"Musica ayual:{minha_playlist.atual}")

    print("\nNavegando para frente:")
    for i in range(3): 
        print(f"Tocando: {minha_playlist.proxima_musica()}")

    print("\nNavegando para trás:")
    for i in range(4):
        print(f"Tocando:{minha_playlist.musica_anterior()}")

exemplo_playlist()