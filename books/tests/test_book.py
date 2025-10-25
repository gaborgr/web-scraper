import unittest
from scrapy.http import HtmlResponse, Request
from books.spiders.book import BookSpider
from books.items import BooksItem


class BookSpiderTest(unittest.TestCase):
    def setUp(self):
        self.spider = BookSpider()
        self.example_html = """ 
            <html>
                <body>
                    <article class="product_pod">
                        <h3>
                            <a href="catalogue/a-book_1/index.html" title="A Book">A Book</a>
                        </h3>
                        <p class="price_color">£51.77</p>
                    </article>

                    <article class="product_pod">
                        <h3>
                            <a href="catalogue/another-book_2/index.html" title="Another Book">Another Book</a>
                        </h3>
                        <p class="price_color">£35.50</p>
                    </article>

                    <li class="next"><a href="catalogue/page-2.html">next</a></li>
                </body>
            </html>
        """
        self.response = HtmlResponse(
            url="https://books.toscrape.com",
            body=self.example_html,
            encoding="utf-8",
        )

    def test_parse_scrapes_all_items(self):
        """Test if the spider scrapes books and pagination links."""
        results = list(self.spider.parse(self.response))

        book_items = [item for item in results if isinstance(item, BooksItem)]
        pagination_requests = [item for item in results if isinstance(item, Request)]

        self.assertEqual(len(book_items), 2)
        self.assertEqual(len(pagination_requests), 1)

    def test_parse_scrape_correct_book_information(self):
        """Test if the spider scrapes the correct information from each book"""
        pass

    def test_parse_creates_pagination_request(self):
        """Test if the spider creates a pagination request correctrly"""
        pass


if __name__ == "__main__":
    unittest.main()
