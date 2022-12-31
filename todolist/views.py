from django.views import generic
from django.urls import reverse_lazy
from todolist.models import ToDoItem


class ToDoItemCreateView(generic.CreateView):
    model = ToDoItem
    fields = ['title', 'text']
    success_url = reverse_lazy('todolist:home')
    template_name_suffix = '_create'

    # TODO: salvar a chave estrangeira do usuário quando criar o ToDoitem


class ToDoItemUpdateView(generic.UpdateView):
    model = ToDoItem
    fields = ['title', 'text']
    success_url = reverse_lazy('todolist:home')
    template_name_suffix = '_update'


class ToDoItemDeleteView(generic.DeleteView):
    model = ToDoItem
    success_url = reverse_lazy('todolist:home')


class ToDoItemListView(generic.ListView):
    model = ToDoItem
    template_name = 'todolist/home.html'


class ToDoItemDetailView(generic.DetailView):
    model = ToDoItem
    template_name_suffix = '_detail'
