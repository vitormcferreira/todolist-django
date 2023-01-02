from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from todolist.models import ToDoItem


class ToDoItemMixin(LoginRequiredMixin):
    def get_queryset(self):
        qs = super().get_queryset()

        # somente os itens que o usuário criou
        qs = qs.filter(user=self.request.user)

        return qs


class ToDoItemCreateView(ToDoItemMixin, generic.CreateView):
    model = ToDoItem
    fields = ['title', 'text']
    success_url = reverse_lazy('todolist:home')
    template_name_suffix = '_create'

    def form_valid(self, form):
        response = super().form_valid(form)

        self.object.user_id = self.request.user.pk
        self.object.save()

        return response


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
