from .cart import Cart

# Create context processor so cart works on all pages
def cart(request):
    # Return default data from Cart Class
    return{'cart': Cart(request)}