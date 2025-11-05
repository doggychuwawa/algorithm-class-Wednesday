class Node:
    def __init__(self, elem, link=None):
        self.data = elem
        self.link = link

    def append(self, new):
        if new is not None:
            new.link = self.link
            self.link = new

    def popNext(self):
        deleted = self.link
        if deleted is not None:
            self.link = deleted.link
            deleted.link = None
        return deleted


class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def isFull(self):
        return False

    def getNode(self, pos):
        if pos < 0:
            return None
        ptr = self.head
        for _ in range(pos):
            if ptr is None:
                return None
            ptr = ptr.link
        return ptr

    def getEntry(self, pos):
        node = self.getNode(pos)
        if node is None:
            return None
        return node.data

    def insert(self, pos, elem):
        if pos < 0:
            raise ValueError("잘못된 위치 값!")
        new = Node(elem)
        before = self.getNode(pos - 1)
        if before is None:
            if pos == 0:
                new.link = self.head
                self.head = new
            else:
                raise IndexError("삽입 위치 오류")
        else:
            before.append(new)

    def delete(self, pos):
        if pos < 0:
            raise ValueError("잘못된 위치 값!")
        before = self.getNode(pos - 1)
        if before is None:
            if pos == 0:
                deleted = self.head
                if deleted is not None:
                    self.head = deleted.link
                    deleted.link = None
                    return deleted
            raise IndexError("삭제 위치 오류")
        else:
            return before.popNext()

    def size(self):
        ptr = self.head
        count = 0
        while ptr is not None:
            count += 1
            ptr = ptr.link
        return count

    def find_by_title(self, title):
        ptr = self.head
        while ptr is not None:
            if ptr.data.title == title:
                return ptr.data  # //도서 객체 반환
            ptr = ptr.link
        return None  # //책 제목 없음 오류

    def find_pos_by_title(self, title):
        ptr = self.head
        idx = 0
        while ptr is not None:
            if ptr.data.title == title:
                return idx  # //위치 반환
            ptr = ptr.link
            idx += 1
        return -1  # //위치 없음


class Book:
    def __init__(self, num, title, author, year):
        self.num = num
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.num} | {self.title} | {self.author} | {self.year}"


class BookManagement:
    def __init__(self):
        self.books = LinkedList()

    def add_book(self, book_id, title, author, year):
        ptr = self.books.head
        while ptr is not None:
            if ptr.data.num == book_id:
                print("이미 존재하는 책 번호입니다.")  # //중복 번호 오류
                return
            ptr = ptr.link
        book = Book(book_id, title, author, year)
        self.books.insert(self.books.size(), book)
        print("도서가 추가되었습니다.")  # //추가 성공

    def remove_book(self, title):
        pos = self.books.find_pos_by_title(title)
        if pos == -1:
            print("해당 제목의 도서가 없습니다.")  # //삭제 대상 없음
            return
        self.books.delete(pos)
        print("도서가 삭제되었습니다.")  # //삭제 성공

    def search_book(self, title):
        book = self.books.find_by_title(title)
        if book is None:
            print("해당 제목의 도서가 없습니다.")  # //조회 실패
        else:
            print(f"책 번호: {book.num}")
            print(f"책 제목: {book.title}")
            print(f"저자: {book.author}")
            print(f"출판 연도: {book.year}")  # //조회 성공

    def display_books(self):
        if self.books.isEmpty():
            print("현재 등록된 도서가 없습니다.")  # //공백 리스트
            return
        ptr = self.books.head
        while ptr is not None:
            print(ptr.data)  # //도서 정보 출력
            ptr = ptr.link

    def run(self):
        while True:
            print("\n=== 도서 관리 프로그램 ===")
            print("1. 도서 추가")
            print("2. 도서 삭제 (책 제목으로 삭제)")
            print("3. 도서 조회 (책 제목으로 조회)")
            print("4. 전체 도서 목록 출력")
            print("5. 종료")
            menu = input("메뉴를 선택하세요: ")
            if menu == '1':
                book_id = input("책 번호: ")
                title = input("책 제목: ")
                author = input("저자: ")
                year = input("출판 연도: ")
                self.add_book(book_id, title, author, year)
            elif menu == '2':
                title = input("삭제할 책 제목을 입력하세요: ")
            elif menu == '3':
                title = input("조회할 책 제목을 입력하세요: ")
                self.search_book(title)
            elif menu == '4':
                print("현재 등록된 도서 목록:")
                self.display_books()
            elif menu == '5':
                print("프로그램을 종료합니다.")  # //종료
                break
            else:
                print("잘못된 입력입니다.")  # //입력 오류


if __name__ == "__main__":
    manager = BookManagement()
    manager.run()
