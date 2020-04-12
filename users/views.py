from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, ListView
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib.auth.models import User
from movie.models import Movie
from rank.models import Rank
from django.db.models import F


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'{username} is now an Avenger, now login')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
    ranks = Rank.objects.filter(user_id=request.user).order_by('number')
    context = {
        'user_form': user_form,
        'ranks': ranks
    }
    return render(request, 'users/profile.html', context)


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'users/user_detail.html'

    def get_object(self):
        return get_object_or_404(User, username=self.kwargs['username'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_ranks'] = Rank.objects.filter(
            user__username=self.kwargs['username']).order_by(F('number').asc(nulls_last=True))
        return context
