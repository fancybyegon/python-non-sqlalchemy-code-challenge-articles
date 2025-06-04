import pytest
from classes.many_to_many import Author, Magazine, Article


class TestAuthor:

    def test_author_has_name(self):
        author = Author("Ernest Hemingway")
        assert author.name == "Ernest Hemingway"

    def test_author_name_must_be_string(self):
        with pytest.raises(Exception):
            Author(123)

    def test_author_articles(self):
        author = Author("Agatha Christie")
        magazine = Magazine("Mystery Mag", "Mystery")
        article1 = Article(author, magazine, "Murder on the Orient Express")
        article2 = Article(author, magazine, "Death on the Nile")

        articles = author.articles()
        assert article1 in articles
        assert article2 in articles
        assert all(isinstance(article, Article) for article in articles)

    def test_author_magazines(self):
        author = Author("J.K. Rowling")
        mag1 = Magazine("Fantasy World", "Fantasy")
        mag2 = Magazine("Magic Times", "Fantasy")
        Article(author, mag1, "Wizards and Wands")
        Article(author, mag2, "Potions 101")

        magazines = author.magazines()
        assert mag1 in magazines
        assert mag2 in magazines
        assert all(isinstance(mag, Magazine) for mag in magazines)

    def test_add_article_creates_article(self):
        author = Author("Stephen King")
        mag = Magazine("Horror House", "Horror")
        author.add_article(mag, "It")

        articles = author.articles()
        assert any(article.title == "It" and article.magazine == mag for article in articles)

    def test_add_article_raises_for_invalid_magazine(self):
        author = Author("Stephen King")
        with pytest.raises(Exception):
            author.add_article("Not a Magazine", "It")
