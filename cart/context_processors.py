from .cart import Cart

# Create context processor so our cart can work on all pages of the site
def cart(request):
	# Return default data from our Cart
	return {'cart': Cart(request)}