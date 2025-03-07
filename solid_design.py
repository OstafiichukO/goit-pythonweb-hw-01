from abc import ABC, abstractmethod
from typing import List
from colorama import Fore, init
import logging

init(autoreset=True)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Принцип SRP: клас Book для зберігання інформації про книгу
class Book:
    def __init__(self, title: str, author: str, year: str):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"


# Принцип ISP: Інтерфейс для роботи з бібліотекою
class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book) -> None:
        pass

    @abstractmethod
    def remove_book(self, title: str) -> None:
        pass

    @abstractmethod
    def get_books(self) -> List[Book]:
        pass


# Принцип LSP: клас Library реалізує інтерфейс LibraryInterface
class Library(LibraryInterface):
    def __init__(self):
        self._books = []

    def add_book(self, book: Book) -> None:
        self._books.append(book)

    def remove_book(self, title: str) -> None:
        self._books = [book for book in self._books if book.title != title]

    def get_books(self) -> List[Book]:
        return self._books


# Принцип DIP: LibraryManager залежить від інтерфейсу LibraryInterface
class LibraryManager:
    def __init__(self, library: LibraryInterface):
        self.library = library

    def add_book(self, title: str, author: str, year: str) -> None:
        book = Book(title, author, year)
        self.library.add_book(book)
        logger.info(f'{Fore.GREEN}Book "{title}" added successfully.{Fore.RESET}')

    def remove_book(self, title: str) -> None:
        self.library.remove_book(title)
        logger.info(f'{Fore.RED}Book "{title}" removed successfully.{Fore.RESET}')

    def show_books(self) -> None:
        books = self.library.get_books()
        if books:
            logger.info(f"{Fore.YELLOW}Books in the library:{Fore.RESET}")
            for book in books:
                logger.info(f"{Fore.CYAN}{book}{Fore.RESET}")
        else:
            logger.info(f"{Fore.MAGENTA}The library is empty.{Fore.RESET}")


# Принцип OCP: код Library розширюється через композицію
class ExtendedLibrary(Library):
    def find_books_by_author(self, author: str) -> List[Book]:
        return [book for book in self._books if book.author == author]


def main():
    library = Library()
    manager = LibraryManager(library)

    while True:
        command = (
            input(f"{Fore.BLUE}Enter command (add, remove, show, exit): {Fore.RESET}")
            .strip()
            .lower()
        )

        match command:
            case "add":
                title = input(f"{Fore.CYAN}Enter book title: {Fore.RESET}").strip()
                author = input(f"{Fore.CYAN}Enter book author: {Fore.RESET}").strip()
                year = input(f"{Fore.CYAN}Enter book year: {Fore.RESET}").strip()
                manager.add_book(title, author, year)
            case "remove":
                title = input(
                    f"{Fore.CYAN}Enter book title to remove: {Fore.RESET}"
                ).strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                logger.info(f"{Fore.RED}Exiting program...{Fore.RESET}")
                break
            case _:
                logger.warning(f"{Fore.YELLOW}Invalid command. Please try again.{Fore.RESET}")


if __name__ == "__main__":
    main()
