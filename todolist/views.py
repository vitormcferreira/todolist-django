from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import QuerySet
from django.urls import reverse_lazy
from django.views import generic

from todolist.models import ToDoItem


class ToDoItemMixin(LoginRequiredMixin):
    model = ToDoItem
    fields = ['title', 'text']
    success_url = reverse_lazy('todolist:home')

    def get_queryset(self):
        qs: QuerySet = super().get_queryset()

        qs = self.__filter_user_items(qs)

        return qs

    def __filter_user_items(self, qs: QuerySet):
        return qs.filter(user=self.request.user)

    def get_success_url(self):
        next = self.request.GET.get('next')

        if next:
            return next

        return super().get_success_url()


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
