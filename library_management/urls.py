from django.contrib import admin
from django.urls import path
from library.views import book_list, member_list, issue_book, return_book, search_books, import_books, add_book, edit_book, delete_book,add_member,edit_member,delete_member

urlpatterns = [
    path("", book_list, name="book_list"),
    path("members/", member_list, name="member_list"),
    path("issue/", issue_book, name="issue_book"),
    path("return/<int:transaction_id>/", return_book, name="return_book"),
    path("search/", search_books, name="search_books"),
    path("import/", import_books, name="import_books"),
    path("books/add/", add_book, name="add_book"),
    path("books/edit/<int:book_id>/", edit_book, name="edit_book"),
    path("books/delete/<int:book_id>/", delete_book, name="delete_book"),
    path("members/add/", add_member, name="add_member"),
    path("members/edit/<int:member_id>/", edit_member, name="edit_member"),
    path("members/delete/<int:member_id>/", delete_member, name="delete_member"),
]
