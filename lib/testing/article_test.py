import pytest
from classes.many_to_many import Article, Author, Magazine


class TestArticle:

    def test_article_initialized_with_author_magazine_title(self):
        author = Author("George Orwell")
        mag = Magazine("Political Review", "Politics")
        article = Article(author, mag, "1984")

        assert article.author == author
        assert article.magazine == mag
        assert article.title == "1984"

    def test_article_author_must_be_author_instance(self):
        mag = Magazine("Science Daily", "Science")
        with pytest.raises(Exception):
            Article("Not an Author", mag, "Title")

    def test_article_magazine_must_be_magazine_instance(self):
        author = Author("Marie Curie")
        with pytest.raises(Exception):
            Article(author, "Not a Magazine", "Title")

    def test_article_title_must_be_string(self):
        author = Author("Albert Einstein")
        mag = Magazine("Physics Today", "Science")
        with pytest.raises(Exception):
            Article(author, mag, 123)
