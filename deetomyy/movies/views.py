from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views
from .models import Movie, BasketItem
from .forms import CreateMovieForm
from django.contrib import messages


def profile_page(request):
    if request.user.is_authenticated:
        user = request.user
        user_info = {
            'username': user.username,
            'email': user.email,
        }
        return render(request, 'profile.html', {'user_info': user_info})
    else:
        return redirect('login')


def index_page_view(request):
    return redirect('movie_page')


def movie_page_view(request):
    if request.method == 'GET':
        form = CreateMovieForm()
        movies = Movie.objects.all()
        return render(request, 'movies/index.html', {'movies': movies, 'form': form})
    if request.method == 'POST':
        form = CreateMovieForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            description = form.cleaned_data.get('description')
            due_date = form.cleaned_data.get('due_date')
            status = form.cleaned_data.get('status')
            movie = Movie(title=title, description=description, due_date=due_date, status=status)
            movie.save()
        movies = Movie.objects.all()
        return render(request, 'movies/index.html', {'movies': movies, 'form': form})


def movie_details_view(request, pk):
    movie = Movie.objects.get(id=pk)
    return render(request, 'movies/movie-details.html', {'movie': movie})


def delete_movie_page_view(request, pk):
    try:
        movie = Movie.objects.get(id=pk)
        movie.delete()
        return redirect('movie_page')
    except Movie.DoesNotExist:
        error = 'Movie not Found'
        messages.error(request, message=error)
        return redirect('movie_page')


def basket_page_view(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            basket_items = BasketItem.objects.filter(owner=request.user)
            return render(request, 'movies/basket.html', {'basket_items': basket_items})
    else:
        return redirect('login')


def add_movie_to_basket_view(request, pk):
    if request.user.is_authenticated:
        movie = Movie.objects.get(pk=pk)
        basket_item = BasketItem(movie=movie, owner=request.user)
        basket_item.save()
        return redirect('basket_page')
    else:
        return redirect('login')


def delete_from_basket_view(request, pk):
    basket_item = BasketItem.objects.get(pk=pk)
    if request.user.is_authenticated and request.user == basket_item.owner:
        basket_item.delete()
        return redirect('basket_page')
    else:
        return redirect('index_page')
