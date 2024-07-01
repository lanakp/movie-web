from django.shortcuts import render
from django.views.generic import View,CreateView

# Create your views here.
class HomeView(View):
    def get(self,request,*args,**kw):
        return render(request,"home.html")
    

# class RegView(CreateView):
#     templates_name = 'reg.html'
#     success_url  = reverse_lazy('log')

#     def form_valid(self,form: BaseModelForm) -> httpResponse:
#         message.success(self.request,"registration successfull")
#         return super().form_unvalid(form)
    
#     def form_valid(self,form: BaseModelForm) -> httpResponse:
#         message.success(self.request,"registration failed")
#         return super().form_unvalid(form)

