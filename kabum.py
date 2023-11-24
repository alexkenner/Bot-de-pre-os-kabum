import requests
from bs4 import BeautifulSoup

# Função para encurtar URL usando TinyURL
def shorten_url_with_tinyurl(original_url):
    api_url = "http://tinyurl.com/api-create.php?url="
    response = requests.get(api_url + original_url)
    if response.status_code == 200:
        return response.text
    else:
        return None

# Lista de URLs de produtos
produtos_urls = [
    "https://www.kabum.com.br/produto/442399/placa-mae-asus-tuf-gaming-b650m-plus-am5-microatx-ddr5",
    "https://www.kabum.com.br/produto/422923/placa-mae-asrock-b650m-pg-riptide-amd-micro-atx-ddr5-90-mxbj9-",
    "https://www.kabum.com.br/produto/429941/placa-mae-gigabyte-b650m-ds3h-ud-amd-ryzen-7000-m-2-ddr5-displayport-hdmi",
    # Adicione mais URLs conforme necessário
]

# Iterar sobre os URLs dos produtos
for url in produtos_urls:
    # Encurtar a URL com TinyURL
    shortened_url = shorten_url_with_tinyurl(url)

    if shortened_url:
        # Enviar uma solicitação HTTP para o site
        response = requests.get(url)

        # Verificar se a solicitação foi bem-sucedida (código 200)
        if response.status_code == 200:
            # Analisar o conteúdo HTML da página
            soup = BeautifulSoup(response.text, 'html.parser')

            # Exemplo: Extrair nome do produto usando classe
            product_name_element = soup.find('h1', class_='sc-89bddf0f-6 dVrDvy')

            # Exemplo: Extrair preço à vista usando classe
            price_avista_element = soup.find('h4', class_='sc-5492faee-2 hAMMrD finalPrice')

            if product_name_element and price_avista_element:
                product_name = product_name_element.text.strip()
                price_avista = price_avista_element.text.strip()

                # Imprimir em verde
                print(f"Produto: {product_name}")
                print(f"Preço à vista: \033[92m{price_avista}\033[0m")  # \033[92m é o código de cor verde
                print(f"URL encurtada: {shortened_url}")
                print("-----")
            else:
                print(f"Informações incompletas para {url}")
                print("-----")

        else:
            print(f"Erro {response.status_code} ao acessar o site para {url}")
            print("-----")
    else:
        print(f"Falha ao encurtar a URL para {url}")
        print("-----")
