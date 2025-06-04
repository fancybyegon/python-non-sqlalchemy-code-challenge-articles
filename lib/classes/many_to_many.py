class Author:
    all = []

    def __init__(self, name: str):
        if not isinstance(name, str):
            raise Exception("Author name must be a string.")
        self.name = name
        Author.all.append(self)

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        if not isinstance(magazine, Magazine):
            raise Exception("Magazine must be a Magazine instance.")
        Article(self, magazine, title)


class Magazine:
    all = []

    def __init__(self, name: str, category: str):
        if not isinstance(name, str):
            raise Exception("Magazine name must be a string.")
        if not (2 <= len(name) <= 16):
            raise Exception("Magazine name must be between 2 and 16 characters.")
        self._name = name

        if not isinstance(category, str):
            raise Exception("Magazine category must be a string.")
        if len(category) == 0:
            raise Exception("Magazine category must not be empty.")
        self._category = category

        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise Exception("Magazine name must be a string.")
        if not (2 <= len(new_name) <= 16):
            raise Exception("Magazine name must be between 2 and 16 characters.")
        self._name = new_name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        if not isinstance(new_category, str):
            raise Exception("Magazine category must be a string.")
        if len(new_category) == 0:
            raise Exception("Magazine category must not be empty.")
        self._category = new_category

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        contributors_list = [article.author for article in self.articles()]
        unique_authors = []
        for author in contributors_list:
            if author not in unique_authors:
                unique_authors.append(author)
        return unique_authors

    def article_titles(self):
        articles = self.articles()
        if not articles:
            return None
        return [article.title for article in articles]

    def contributing_authors(self):
        authors = self.contributors()
        contributing = []
        for author in authors:
            count = sum(1 for article in self.articles() if article.author == author)
            if count > 2:
                contributing.append(author)
        if contributing:
            return contributing
        return None


class Article:
    all = []

    def __init__(self, author: Author, magazine: Magazine, title: str):
        if not isinstance(author, Author):
            raise Exception("Author must be an Author instance.")
        if not isinstance(magazine, Magazine):
            raise Exception("Magazine must be a Magazine instance.")
        if not isinstance(title, str):
            raise Exception("Article title must be a string.")

        self.author = author
        self.magazine = magazine
        self.title = title

        Article.all.append(self)
