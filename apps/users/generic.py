from django.views.generic.base import ContextMixin

class ModelExtraView(ContextMixin):
	#model_extra
	def get_context_data(self, *args , **kwargs):
		context = super().get_context_data(*args, **kwargs)
		if 'object_extra' not in context and hasattr(self, 'model_extra'):
			context['object_extra'] = self.model_extra.objects.get(id=self.kwargs['pk'])
		return context
