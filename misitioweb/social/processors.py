from .models import Red

def ctx_dict(request):
    ctx = {}
    redes = Red.objects.all()
    for red in redes:
        ctx[red.key] = red.url
    return ctx