# from django.shortcuts import render
# from .models import Movie
# from django.http import JsonResponse

# # Create your views here.
# def movielist(request):
#     movies = Movie.objects.all()
#     data = {
#         'movies': list(movies.values())
#     }

#     return JsonResponse(data)

# def moviedetails(request, pk):
#     movie = Movie.objects.get(pk=pk)
#     data = {
#         'name': movie.name,
#         'description': movie.description,
#         'active': movie.active
#     }
#     return JsonResponse(data)