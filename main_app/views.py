from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import TrainingForm
# from .forms import *
# Create your views here.


class PlayerList(LoginRequiredMixin, ListView):
  model = Player

  def get_queryset(self):
    return self.model.objects.filter(user=self.request.user)

def player_detail(request, player_id):
    player = Player.objects.get(id=player_id)
    id_list = player.boots.all().values_list('id')
    boots_player_doesnt_have = Boot.objects.exclude(id__in=id_list)

    training_form = TrainingForm()
    return render(request, 'main_app/player_detail.html', {
        'player': player, 'training_form': training_form,
        'boots': boots_player_doesnt_have
    })
# class PlayerDetailView(LoginRequiredMixin, FormMixin, DetailView, player_id):
#   model = Player
#   player = Player.objects.get(id=player_id)
  
#   def get_context_data(self, **kwargs):
#     context = super().get_context_data(**kwargs)
#     context['today'] = date.today()
#     return context

class PlayerCreateView(LoginRequiredMixin, CreateView):
  model = Player
  fields = ['name', 'position', 'club', 'birth_date']

  def form_valid(self, form):
   form.instance.user = self.request.user
   return super().form_valid(form)

class PlayerUpdateView(LoginRequiredMixin, UpdateView):
  model = Player
  fields = ['name', 'position', 'club', 'birth_date']

class PlayerDeleteView(LoginRequiredMixin, DeleteView):
  model = Player
  success_url = '/players'

def add_training(request, player_id):
  form = TrainingForm(request.POST)
  if form.is_valid():
    new_training = form.save(commit=False)
    new_training.player_id = player_id
    new_training.save()
  return redirect('player_detail', player_id=player_id)

class BootList(ListView):
  model = Boot

class BootDetail(DetailView):
  model = Boot

class BootCreate(CreateView):
  model = Boot
  fields = '__all__'

class BootUpdate(UpdateView):
  model = Boot
  fields = ['name', 'manufacturer']

class BootDelete(DeleteView):
  model = Boot
  success_url = '/boots'

def assoc_boot(request, player_id, boot_id):
  Player.objects.get(id=player_id).boots.add(boot_id)
  return redirect('player_detail', player_id=player_id)

def unassoc_boot(request, player_id, boot_id):
  Player.objects.get(id=player_id).boots.remove(boot_id)
  return redirect('player_detail', player_id=player_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('player_list')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

def home(request):
  return render(request, 'home.html')