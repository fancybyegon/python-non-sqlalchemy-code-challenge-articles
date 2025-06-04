import pytest

from classes.many_to_many import Article, Magazine, Author


class TestMagazine:

    def test_has_name(self):
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")
        assert magazine_1.name == "Vogue"
        assert magazine_2.name == "AD"

    def test_name_is_mutable_string(self):
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")
        assert isinstance(magazine_1.name, str)
        assert isinstance(magazine_2.name, str)

        magazine_1.name = "New Yorker"
        assert magazine_1.name == "New Yorker"

        with pytest.raises(Exception):
            magazine_2.name = 2

        with pytest.raises(Exception):
            Magazine(2, "Numbers")

    def test_name_len(self):
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")
        assert 2 <= len(magazine_1.name) <= 16
        assert 2 <= len(magazine_2.name) <= 16

        with pytest.raises(Exception):
            magazine_1.name = "New Yorker Plus X"

        with pytest.raises(Exception):
            magazine_2.name = "A"

    def test_has_category(self):
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")
        assert magazine_1.category == "Fashion"
        assert magazine_2.category == "Architecture"

    def test_category_is_mutable_string(self):
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")

        assert isinstance(magazine_1.category, str)
        assert isinstance(magazine_2.category, str)

        magazine_1.category = "Life Style"
        assert magazine_1.category == "Life Style"
        assert isinstance(magazine_1.category, str)

        with pytest.raises(Exception):
            magazine_2.category = 2

        with pytest.raises(Exception):
            Magazine("GQ", 2)

    def test_category_len(self):
        magazine_1 = Magazine("Vogue", "Fashion")
        assert magazine_1.category != ""

        with pytest.raises(Exception):
            magazine_1.category = ""

    def test_has_many_articles(self):
        author_1 = Author("Carry Bradshaw")
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")
        article_1 = Article(author_1, magazine_1, "How to wear a tutu with style")
        article_2 = Article(author_1, magazine_1, "Dating life in NYC")
        article_3 = Article(author_1, magazine_2, "2023 Eccentric Design Trends")

        assert len(magazine_1.articles()) == 2
        assert len(magazine_2.articles()) == 1
        assert article_1 in magazine_1.articles()
        assert article_2 in magazine_1.articles()
        assert article_3 not in magazine_1.articles()
        assert article_3 in magazine_2.articles()

    def test_articles_of_type_articles(self):
        author_1 = Author("Carry Bradshaw")
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")
        Article(author_1, magazine_1, "How to wear a tutu with style")
        Article(author_1, magazine_1, "Dating life in NYC")
        Article(author_1, magazine_2, "2023 Eccentric Design Trends")

        assert isinstance(magazine_1.articles()[0], Article)
        assert isinstance(magazine_1.articles()[1], Article)
        assert isinstance(magazine_2.articles()[0], Article)

    def test_has_many_contributors(self):
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")
        magazine_1 = Magazine("Vogue", "Fashion")
        Article(author_1, magazine_1, "How to wear a tutu with style")
        Article(author_2, magazine_1, "Dating life in NYC")

        assert len(magazine_1.contributors()) == 2
        assert author_1 in magazine_1.contributors()
        assert author_2 in magazine_1.contributors()

    def test_contributors_of_type_author(self):
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")
        magazine_1 = Magazine("Vogue", "Fashion")
        Article(author_1, magazine_1, "How to wear a tutu with style")
        Article(author_2, magazine_1, "Dating life in NYC")

        assert isinstance(magazine_1.contributors()[0], Author)
        assert isinstance(magazine_1.contributors()[1], Author)

    def test_contributors_are_unique(self):
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")
        magazine_1 = Magazine("Vogue", "Fashion")
        Article(author_1, magazine_1, "How to wear a tutu with style")
        Article(author_1, magazine_1, "How to be single and happy")
        Article(author_2, magazine_1, "Dating life in NYC")

        assert len(set(magazine_1.contributors())) == len(magazine_1.contributors())
        assert len(magazine_1.contributors()) == 2

    def test_article_titles(self):
        author_1 = Author("Carry Bradshaw")
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")
        magazine_3 = Magazine("GQ", "Fashion")
        Article(author_1, magazine_1, "How to wear a tutu with style")
        Article(author_1, magazine_2, "2023 Eccentric Design Trends")
        Article(author_1, magazine_2, "Carrara Marble is so 2020")

        assert magazine_1.article_titles() == ["How to wear a tutu with style"]
        assert magazine_2.article_titles() == [
            "2023 Eccentric Design Trends",
            "Carrara Marble is so 2020",
        ]
        assert magazine_3.article_titles() is None

    def test_contributing_authors(self):
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")
        Article(author_1, magazine_1, "How to wear a tutu with style")
        Article(author_1, magazine_1, "How to be single and happy")
        Article(author_1, magazine_1, "Dating life in NYC")
        Article(author_1, magazine_2, "Carrara Marble is so 2020")
        Article(author_2, magazine_2, "2023 Eccentric Design Trends")

        assert author_1 in magazine_1.contributing_authors()
        assert author_2 not in magazine_1.contributing_authors()
        assert all(isinstance(author, Author) for author in magazine_1.contributing_authors())
        assert magazine_2.contributing_authors() is None
