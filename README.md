# Bot Web Scraping de Produtos Kabum 

Este é um script simples em Python para realizar web scraping em páginas de produtos e extrair informações como nome do produto, preço à vista, e URL encurtada usando TinyURL.

## Requisitos

- Python 3.x
- Bibliotecas Python: requests, BeautifulSoup

## Como Usar

1. **Clone o Repositório:**
    ```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd seu-repositorio
    ```

2. **Instale as Dependências:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Execute o Script:**
    ```bash
    python kabum.py
    ```

4. **Saída Esperada:**
    ```plaintext
    Produto: Nome do Produto
    Preço à vista: R$ 100,00
    URL encurtada: http://tinyurl.com/abcdef
    -----
    ```

## Configuração do TinyURL

Antes de executar o script, é necessário configurar a API do TinyURL e obter uma chave de API. Substitua `SEU_TINYURL_API_KEY` no script pela sua chave de API.

## Autor

Alex Leontino

## Contribuição

Sinta-se à vontade para contribuir com melhorias, correções de bugs ou novas funcionalidades. Abra uma issue para discutir grandes alterações.

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.
