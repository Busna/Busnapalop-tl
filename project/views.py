from django.shortcuts import render
from django.views import View


class Despesasdospaises(View):
    def get(self, request):
        ctx = {

        }

        return render(request, 'despesasdospaises.html', context=ctx)
