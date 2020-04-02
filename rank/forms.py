from django import forms
from .models import User, Movie, Rank

movies = Movie.objects.filter(active=True)
movie_count = movies.count()
movie_list = [tuple([x, x]) for x in range(1, movie_count)]

movie_list_and_placeholder = [('', 'Select Rank')] + movie_list


class RankForm(forms.ModelForm):
    number = forms.IntegerField(widget=forms.Select(
        choices=movie_list_and_placeholder, attrs={'placeholder': 'Select Rank'}))
    review = forms.CharField(
        max_length=2100, widget=forms.Textarea(attrs={'rows': 3, 'cols': 15}))

    class Meta:
        model = Rank
        fields = ['number', 'review']
