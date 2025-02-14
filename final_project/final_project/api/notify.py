from django.views.generic import View
from .helper_functions import *
from game.models import History


class NotifyView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            id = data['id']
            if type(id) != str:
                raise TypeError
            win = data['win']
            if type(win) != bool:
                raise TypeError
            price = data['price']
            if type(price) != float:
                raise TypeError
            click = data['click']
            if type(click) != bool:
                raise TypeError
            conversion = data['conversion']
            if type(conversion) != bool:
                raise TypeError
            revenue = data['revenue']
            if type(revenue) != float:
                raise TypeError

        except KeyError:
            return failed_status("missed parameter")
        except TypeError:
            return failed_status("wrong type")
        history = History.objects.latest('id')
        history.win = win
        if win:
            history.budget -= price
        history.save()
        return ok_status()
