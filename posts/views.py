from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Post
from .forms import PostForm

# Listar posts (Acceso público)
class ListadoPostsView(ListView):
    model = Post
    template_name = 'posts/listado_posts.html'
    context_object_name = 'posts'

# Detalle del post (Acceso público)
class DetallePostView(DetailView):
    model = Post
    template_name = 'posts/detalle_post.html'
    context_object_name = 'post'

# Crear post (Ruta protegida)
class CrearPostView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/post_form.html'
    success_url = reverse_lazy('listado_posts')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

# Editar post (Ruta protegida)
class EditarPostView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/post_form.html'
    success_url = reverse_lazy('listado_posts')

# Eliminar post (Ruta protegida)
class EliminarPostView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'posts/post_confirmar_borrado.html'
    success_url = reverse_lazy('listado_posts')

# Búsqueda de posts (Acceso público)
def buscar_posts(request):
    query = request.GET.get('q', '')
    resultados = []
    if query:
        resultados = Post.objects.filter(
            Q(titulo__icontains=query) | Q(contenido__icontains=query)
        )
    return render(request, 'posts/buscar_posts.html', {'posts': resultados, 'query': query})