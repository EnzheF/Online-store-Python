from django.shortcuts import render
from django.views import View
from store.mixins import ProfileMixin
from store.models.customer import Customer


class SaveBuy(ProfileMixin, View):
    def post(self, request):
        # paket = Paket.objects.get(id=pk)
        # m = paket.months
        # startdate = date.today()
        userprofile = Customer.objects.get(user=request.user)
        # userprofile.podpiska = True
        # userprofile.DateSubDie = str(startdate + timedelta(days=30 * m))
        # form.userprofile = userprofile
        userprofile.save()

        return render(request, 'base.html')