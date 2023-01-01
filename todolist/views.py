from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from todolist.models import ToDoItem


class ToDoItemMixin(LoginRequiredMixin):
    pass


class ToDoItemCreateView(ToDoItemMixin, generic.CreateView):
    model = ToDoItem
    fields = ['title', 'text']
    success_url = reverse_lazy('todolist:home')
    template_name_suffix = '_create'

    # TODO: salvar a chave estrangeira do usuário quando criar o ToDoitem


class ToDoItemUpdateView(ToDoItemMixin, generic.UpdateView):
    model = ToDoItem
    fields = ['title', 'text']
    success_url = reverse_lazy('todolist:home')
    template_name_suffix = '_update'


class ToDoItemDeleteView(ToDoItemMixin, generic.DeleteView):
    model = ToDoItem
    success_url = reverse_lazy('todolist:home')


class ToDoItemListView(ToDoItemMixin, generic.ListView):
    model = ToDoItem
    template_name = 'todolist/home.html'


class ToDoItemDetailView(ToDoItemMixin, generic.DetailView):
    model = ToDoItem
    template_name_suffix = '_detail'
