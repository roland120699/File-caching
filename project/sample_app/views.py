from django.core.cache import cache


class ProductDetailView(DetailView):
    template_name = 'sample_app/product_detail.html'
    queryset = Product.objects.all()

    def get_object(self, *args, **kwargs):
        obj = cache.get(f'product-{self.kwargs["pk"]}',
                        None)
        if not obj:
            obj = super().get_object(queryset=self.queryset)
            cache.set(f'product-{self.kwargs["pk"]}', obj)
            return obj