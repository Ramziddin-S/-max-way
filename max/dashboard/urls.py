from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard_page, name="dashboard"),
    path('login/', views.dashboard_login, name="login"),
    path('logout/', views.dashboard_logout, name="logout"),

    path('category_list/', views.category_list, name="category_list"),
    path('category/<int:pk>/edit/', views.category_edit, name="category_edit"),
    path('category/<int:pk>/delete/', views.category_delete, name="category_delete"),
    path('category_add/', views.category_create, name="category_add"),


    path('user_list/', views.user_list, name="user_list"),
    path('user_add/', views.user_create, name="user_add"),
    path('user/<int:pk>/edit/', views.user_edit, name="user_edit"),
    path('user/<int:pk>/delete/', views.user_delete, name="user_delete"),

    path('order_list/', views.order_list, name="order_list"),
    path('order_add/', views.order_create, name="order_add"),
    path('status/<int:pk>/<int:status>/', views.order_status, name="status"),

    path('product_list/', views.product_list, name="product_list"),
    path('product_add/', views.product_create, name="product_add"),
    path('product/<int:pk>/edit/', views.product_edit, name="product_edit"),
    path('product/<int:pk>/delete/', views.product_delete, name="product_delete"),

]














# @login_required_decorator
# def status(request, pk):
#     model = Order.objects.get(id=pk)
#     form = OrderForm(request.POST or None, instance=model)
#     if request.POST:
#         if form.is_valid():
#             form.save()
#             return redirect('order_list ')
#         else:
#             print(form.errors)
#     ctx = {
#         'form': form,
#     }
#     return render(request, 'dashboard/order/form.html', ctx)






#
# <div class="slide">
#             {% for cat in categories %}
#           <div class="big__title category_{{cat.id}}">{{cat.name}}</div>
#           <div class="row category_{{cat.id}}">
#               {% for prod in products %}
#               {% if cat.id == prod.category_id %}
#             <div class="col-6 col-md-12 col-xs-12">
#               <div class="item category_{{cat.id}}">
#                 <div class="box">
#                   <div class="box__img">  <img class="img" src="/media/{{prod.image}}" alt=""/>
#                     <div class="img__hot"><img class="hot" src="{% static 'fronted/img/hot.svg' %}" alt=""/></div>
#                   </div>
#                   <div class="box__content">
#                     <div class="box__title">{{prod.title}}<img src="{% static 'fronted/img/chesse.svg' %}" alt=""/></div>
#                     <div class="box__text">{{prod.description}}</div>
#                     <div class="cost__btn">
#                       <div class="box__cost">{{prod.price}} UZS</div>
#                       <button class="box__btn"> <img src="{% static 'fronted/img/plus.png' %}" alt=""/></button>
#                     </div>
#                   </div>
#                 </div>
#               </div>
#             </div>
#               {% endif %}
#             {% endfor %}
#           </div>
#           <div class="slide__btn pitsa" data-id="category_{{cat.id}}">
#             <button>Ko‘proq ko‘rish</button>
#           </div>
#             {% endfor %}
#         </div>
#
#









