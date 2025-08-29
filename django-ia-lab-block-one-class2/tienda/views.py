from django.shortcuts import render, get_object_or_404
from .models import Producto, Pedido, Cliente

def home(request):
    # render() recibe: request, ruta de template, contexto (diccionario)
    return render(request, "tienda/home.html", {})

def lista_productos(request):
    productos = Producto.objects.all().order_by("nombre")
    return render(request, "tienda/lista_productos.html", {"productos": productos})

def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, "tienda/detalle_producto.html", {"producto": producto})

def lista_pedidos(request):
    pedidos = Pedido.objects.select_related("cliente").prefetch_related("productos").order_by("-fecha")
    return render(request, "tienda/lista_pedidos.html", {"pedidos": pedidos})

def detalle_pedido(request, pk):
    pedido = get_object_or_404(Pedido.objects.select_related("cliente").prefetch_related("productos"), pk=pk)
    return render(request, "tienda/detalle_pedido.html", {"pedido": pedido})

def detalle_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    pedidos = cliente.pedidos.select_related("cliente").prefetch_related("productos"). order_by("-fecha")

    return render(request, "tienda/detalle_cliente.html", {"cliente": cliente, "pedidos": pedidos})
