from django.shortcuts import render,redirect, get_object_or_404
from .models import Book,Member,Transaction
from .forms import BookForm,MemberForm, IssueForm
from django.db.models import Q
from django.utils import timezone
import requests 

#Home Page
def book_list(request):
    books=Book.objects.all
    return render(request,"books/book_list.html",{"books":books})

#CRUD operations for books
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm()
    return render(request,"books/book_form.html",{"form": form})

def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect("book_list")
    return render(request, "books/book_form.html", {"form": form})

def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect("book_list")

#Member Page
def member_list(request):
    members=Member.objects.all()
    return render(request,"members/member_list.html",{"members":members})

#CRUD operations for Members
def add_member(request):
    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("member_list")
    else:
        form = MemberForm()
    return render(request, "members/member_form.html", {"form": form})

def edit_member(request, member_id):
    member = get_object_or_404(Member, id=member_id)
    form = MemberForm(request.POST or None, instance=member)
    if form.is_valid():
        form.save()
        return redirect("member_list")
    return render(request, "members/member_form.html", {"form": form})

def delete_member(request, member_id):
    member = get_object_or_404(Member, id=member_id)
    member.delete()
    return redirect("member_list")

#Search book
def search_books(request):
    title = request.GET.get("title","")
    author = request.GET.get("author","")
    books= Book.objects.all()
    if title:
        books=books.filter(title__icontains=title)

    if author:
        books=books.filter(author__icontains=author)
    return render(request,"books/search_books.html",{"books":books,"title":title,"author":author})

#Issue Book
def issue_book(request):
    issued_transactions = Transaction.objects.filter(returned=False)

    if request.method == 'POST':
        form=IssueForm(request.POST)
        if form.is_valid():
            book=form.cleaned_data['book']
            member=form.cleaned_data['member']

            if book.stock <=0:
                error = "This book is out of stock."
            elif member.outstanding_debt >= 500:
                error = f"{member.name} has outstanding debt over ₹500."
            else:
                book.stock -= 1
                book.save()

                Transaction.objects.create(book=book, member=member)
                return redirect("issue_book")
            return render(request, "issue.html", {"form": form,"error": error,"issued_transactions": issued_transactions})
    else:
        form = IssueForm()
    return render(request,"issue.html",{"form":form,"issued_transactions": issued_transactions})

#Return_Book
def return_book(request,transaction_id):
    transaction = get_object_or_404(Transaction, id =transaction_id)
    if not transaction.returned:
        transaction.return_date = timezone.now()
        transaction.rent_fee = 50  # fee

        transaction.member.outstanding_debt += transaction.rent_fee
        transaction.book.stock += 1
        transaction.returned = True
        transaction.save()
        transaction.member.save()
        transaction.book.save()
    return redirect('book_list')

#Import Books
def import_books(request):
    if request.method=="POST":
        title=request.POST.get('title','')
        count=int(request.POST.get('count',10))
        imported=0
        page=1
        while imported < count:
            url = f'https://frappe.io/api/method/frappe-library?page={page}&title={title}'
            response = requests.get(url)
            data = response.json().get('message', [])
            if not data:
                break
            for item in data:
                Book.objects.create(
                    title=item['title'],
                    author=item['authors'],
                    isbn=item.get('isbn', ''),
                    publisher=item.get('publisher', ''),
                    pages=int(item.get('num_pages') or 0),
                    stock=1
                )
                imported += 1
                if imported >= count:
                    break
            page += 1
        return redirect('book_list')
    return render(request, 'books/import.html')