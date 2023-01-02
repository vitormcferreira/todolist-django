from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from todolist.models import ToDoItem


class ToDoItemMixin(LoginRequiredMixin):
    model = ToDoItem
    fields = ['title', 'text']
    success_url = reverse_lazy('todolist:home')

    def get_queryset(self):
        qs = super().get_queryset()

        # somente os itens que o usuário criou
        qs = qs.filter(user=self.request.user)

        return qs


class ToDoItemCreateView(ToDoItemMixin, generic.CreateView):
    def form_valid(self, form):
        response = super().form_valid(form)

        self.object.user_id = self.request.user.pk
        self.object.save()

        return response


class ToDoItemUpdateView(ToDoItemMixin, generic.UpdateView):
    pass


class ToDoItemDeleteView(ToDoItemMixin, generic.DeleteView):
    pass


class ToDoItemListView(ToDoItemMixin, generic.ListView):
    template_name = 'todolist/home.html'


class ToDoItemDetailView(ToDoItemMixin, generic.DetailView):
    pass
