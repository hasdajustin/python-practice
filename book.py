class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, Year: {self.year}")

# Example usage
if __name__ == "__main__":
    book = Book("Python Basics", "John Doe", 2023)
    book.display_info()