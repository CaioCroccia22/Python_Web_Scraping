import scrapy


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
         # Seleciona todos os artigos de livros na página
        books = response.css('article.product_pod')
        
        for book in books:
            # Extrai o título e o preço do livro
            title = book.css('h3 a::attr(title)').get()
            price = book.css('div.product_price p.price_color::text').get()

            # Retorna os dados extraídos
            yield {
                'title': title,
                'price': price
            }

        # Segue para a próxima página, se existir
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
