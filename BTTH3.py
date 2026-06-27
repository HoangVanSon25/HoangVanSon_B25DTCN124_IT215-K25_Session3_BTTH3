from fastapi import FastAPI

app = FastAPI()

books = [
    {
        "id": 1,
        "title": "Python Basic",
        "author": "Nguyen Van A",
        "category": "programming",
        "year": 2022,
        "is_available": True
    },
    {
        "id": 2,
        "title": "Web API Design",
        "author": "Tran Van B",
        "category": "web",
        "year": 2021,
        "is_available": False
    },
    {
        "id": 3,
        "title": "Web API",
        "author": "Tran Manh C",
        "category": "web",
        "year": 2023,
        "is_available": True
    },
    {
        "id": 4,
        "title": "Cyber Security",
        "author": "Hoàng Văn Sơn",
        "category": "An Toàn Thông Tin",
        "year": 2026,
        "is_available": False
    },
    {
        "id": 5,
        "title": "Pentest",
        "author": "Hoàng Văn Sơn",
        "category": "An Toàn Thông tin",
        "year": 2025,
        "is_available": True
    }
]


@app.get("/books/statistics")
def statistics_books():
    toltal_book = len(books)
    available_book = [book for book in books if book["is_available"]]
    borrowed_book = [book for book in books if not book["is_available"]]
    return {
        "total_books": toltal_book,
        "available_books": len(available_book),
        "borrowed_books": len(borrowed_book)
    }


@app.get("/books/categories")
def categories_book():
    new_category = []

    for category in books:
        if category["category"].lower().strip() not in new_category:
            new_category.append(category["category"].lower().strip())

    return {
        "categories": new_category
    }


@app.get("/books/latest")
def new_year_book():
    new_year = max(books, key=lambda book: book["year"], default=None)
    if new_year:
        return {
            "message": "Cuốn sách mới nhất",
            "data": new_year
        }
    return {
        "message": "No books available"
    }
