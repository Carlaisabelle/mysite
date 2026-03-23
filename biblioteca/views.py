from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Libro
from .models import Autore
from .models import Lingua_og

# La lista dei libri della biblioteca, creata come lista di dizionari
# libri = [
#     {'titolo': '1984', 'autore': 'George Orwell'},
#     {'titolo': 'Dune', 'autore': 'Frank Herbert'},
#     {'titolo': 'Il nome della rosa', 'autore': 'Umberto Eco'},
#     {'titolo': 'La neve se ne frega', 'autore': 'Luciano Ligabue'},
#     {'titolo': 'Opera struggente di un formidabile genio', 'autore': 'Dave Eggers'},
#     {'titolo': 'Dermatocosmetologia - dall\'inestetismo al trattamento estetico', 'autore': 'Andrea Bovero'},
# ]

def home(request):
    return HttpResponse("Benvenut* nella Biblioteca Django!")

def lista_libri(request):
    # Query che seleziona tutti gli oggetti che fanno parte della classe Libro e li mette dentro la variabile libri
    # La query: SELECT * FROM biblioteca_libro
    libri = Libro.objects.all()
    return render(request, 'biblioteca/lista.html', {'libri': libri})

def dettaglio_libro(request, id):
    libri = Libro.objects.all()
    libro = libri[int(id)]
    return HttpResponse(
        f"<h1>\"{libro.titolo}\"</h1>"
        f"<p>scritto da {libro.autore}</p>"
        # f"<p>Genere: {libro.genere}"
    )

def catalogo(request):
    libri = Libro.objects.all()
    return render(request, 'biblioteca/catalogo.html', {
        'libri': libri,
        'totalelibri': len(libri)
    })

def autori(request):
    return render(request, 'biblioteca/autori.html')

@login_required
def aggiungilibro(request):
    if request.method == 'POST':
        Libro.objects.create(
            titolo = request.POST['titolo'],
            autore = request.POST['autore'],
            anno = int(request.POST['anno'])
        )
        return redirect('lista')
    return render(request, 'biblioteca/aggiungi.html')

@login_required
def aggiungiautore(request):
    if request.method == 'POST':
        Autore.objects.create(
            nome_completo = request.POST['nome_completo'],
            nome = request.POST['nome'],
            cognome = request.POST['cognome'],
            nazionalita = request.POST['nazionalita']
        )
        return redirect('autori')
    return render(request, 'biblioteca/autori.html')

@login_required
def modificalibro(request, id):
    libro = Libro.objects.get(id=id)
    if request.method == 'POST':
        libro.titolo = request.POST['titolo']
        libro.autore = request.POST['autore']
        libro.anno = int(request.POST['anno'])
        libro.genere = request.POST['genere']
        libro.lingua_og = request.POST ['lingua_og']
        libro.save()
        return redirect('lista')
    return render(request, 'biblioteca/modifica.html', {'libro': libro})

@login_required
def eliminalibro(request, id):
    Libro.objects.get(id=id).delete()
    return redirect('lista')