from django.contrib import messages


class SuccessMessageMixin:
    success_message = ''

    def form_valid(self, form):
        messages.success(self.request, self.get_success_message())
        return super(SuccessMessageMixin, self).form_valid(form)  # Difference here

    def get_success_message(self):
        return self.success_message