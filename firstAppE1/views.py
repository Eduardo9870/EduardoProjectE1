from django.shortcuts import render

# Create your views here.

def index (request):
    return render(request, 'index.html')

def playstation (request):
    data={
        "title": "PlayStation",
        "name": "Mejora FPS",
        "client": "Sony Interactive Entertainment LLC",
        "detail": "Mejora de los fotogramas por segundo de los juegos de la marca",
        "year": "2021",
        "version": "2.2",
        "code": "F5-S4567",
        "image": "{%static 'img/fpsPS5.jpg'%}",
        "link": "https://www.playstation.com/es-cl/"
    }
    return render(request, 'proyectos.html', data)

def google (request):
    data={
        "title": "Google",
        "name": "Corrección de errores",
        "client": "Google",
        "detail": "Corregír errores de compativilidad en algunos equipos",
        "year": "2022",
        "version": "1.3",
        "code": "FE23-45",
        "image": "{%static 'img/googleref.png'%}",
        "link": "https://about.google/?utm_source=google-CL&utm_medium=referral&utm_campaign=hp-footer&fg=1"
    }
    return render(request, 'proyectos.html', data)

def vivaldi (request):
    data={
        "title": "Vivaldi",
        "name": "Mejorad de velocidad de navegación",
        "client": "© Vivaldi Technologies™",
        "detail": "Aumento de velocidad carga de páginas desde el browser",
        "year": "2022",
        "version": "5.2",
        "code": "H2J3-25KL",
        "image": "{% static 'img/vivaldiref.webp' %}",
        "link": "https://vivaldi.com/es/"
    }
    return render(request, 'proyectos.html', data)