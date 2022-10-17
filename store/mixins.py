from .models import customer
from django import views
from .models.customer import Customer


class ProfileMixin(views.generic.detail.SingleObjectMixin, views.View):
    def dispatch(self, request, *args, **kwargs ):
        if request.user.is_authenticated:
            userprofile = Customer.objects.filter(user=request.user).first()
            if not userprofile:
                userprofile = Customer.objects.create(user=request.user)
            userprofile.save()
        return super().dispatch(request, *args, **kwargs)