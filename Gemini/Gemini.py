from absl.testing import absltest
import google.generativeai as genai
import pathlib
media = pathlib.Path(__file__).parents[1] / "third_party"

class GeminiGeradorDeTextos(absltest.TestCase):
    def setUp(self):
        # Substitua 'SUA_CHAVE_API' pela chave da API do Google que você deseja usar.
        GOOGLE_API_KEY = 'SUA_CHAVE_API'
        genai.configure(api_key=GOOGLE_API_KEY)

    def test_text_gen_text_only_prompt(self):
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content("Escreva uma questão do tipo teste com 5 alternativas sobre Arquitetura de Computadores - Memória cache.")
        print(response.text)
        
if __name__ == "__main__":
    absltest.main()
