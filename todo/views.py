from django.shortcuts import render,redirect
from .forms import BookForm
from .models import Books
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView

# Create your views here.
def home_page(request):
    return render(request,'home.html')

def read_books(request):
    if request.method == 'POST':  
        form = BookForm(request.POST)  
        if form.is_valid():  
            form.save() 
            return redirect('read_list')  
    else:
        form = BookForm()  

    return render(request, 'read_books.html', {'form': form})

        
def read_list(request):
    tasks = Books.objects.all()
    return render(request,'read_list.html',{'tasks':tasks})

# Update Task View
class BookUpdateView(UpdateView):
    model = Books
    form_class = BookForm
    template_name = 'book_update_form.html'
    success_url = reverse_lazy('read_list')

class BookDeleteView(DeleteView):
    model = Books
    template_name = 'book_confirm_delete.html'
    success_url = reverse_lazy('read_list')