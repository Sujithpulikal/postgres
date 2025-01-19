from django.shortcuts import render, get_object_or_404, redirect
from . models import Movieinfo
from . forms import MovieForm

# Create your views here.

def create(request):
    if request.method == "POST":
        frm = MovieForm(request.POST, request.FILES)  # Include request.FILES for images
        if frm.is_valid():
            frm.save()  # Save to the database
            return redirect("/")  # Redirect to a success page or home
        else:
            return render(request, "create.html", {"frm": frm})  # Re-render with errors
    else:
        frm = MovieForm()
    return render(request, "create.html", {"frm": frm})
# Edit View
def edit(request, movie_id):
    movie = get_object_or_404(Movieinfo, id=movie_id)
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movie_list')  # Redirect to movie list view
    else:
        form = MovieForm(instance=movie)
    return render(request, 'edit.html', {'form': form})

# Delete View
def delete(request, movie_id):
    movie = get_object_or_404(Movieinfo, id=movie_id)
    movie.delete()
    return redirect('movie_list')  # Redirect to movie list view

# List View
def movie_list(request):
    movies = Movieinfo.objects.all()
    return render(request, 'list.html', {'movies': movies})
def home(request):
    return render(request,'menu.html')

