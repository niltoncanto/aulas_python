class FilterStrategy:
    def apply(self, image):
        pass

class BlackAndWhiteFilter(FilterStrategy):
    def apply(self, image):
        print(f"Aplicando filtro preto e branco em {image}")

class SepiaFilter(FilterStrategy):
    def apply(self, image):
        print(f"Aplicando filtro sépia em {image}")

class ImageEditor:
    def __init__(self, filter_strategy: FilterStrategy):
        self.filter_strategy = filter_strategy

    def set_filter(self, filter_strategy: FilterStrategy):
        self.filter_strategy = filter_strategy

    def apply_filter(self, image):
        self.filter_strategy.apply(image)

# Uso do ImageEditor com Strategy
editor = ImageEditor(BlackAndWhiteFilter())
editor.apply_filter("foto.jpg")  # Saída: Aplicando filtro preto e branco em foto.jpg

# O usuário decide mudar para o filtro sépia
editor.set_filter(SepiaFilter())
editor.apply_filter("foto.jpg")  # Saída: Aplicando filtro sépia em foto.jpg
