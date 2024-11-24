from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
#forms is a file in our directory  and loginForm is class i.e import 
from .forms import LoginForm, MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm



urlpatterns = [
    path('', views.ProductView.as_view(), name='home'),
    path('product-detail/<int:pk>',
         views.ProductDetailView.as_view(), name='product-detail'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='showcart'),
    path('pluscart/', views.plus_cart, name='pluscart'),
    path('minuscart/', views.minus_cart, name='minuscart'),
    path('removecart/', views.remove_cart, name='removecart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('laptop/', views.laptop, name='laptop'),
    path('laptop/<slug:data>', views.laptop, name='laptopdata'),
    path('mobile/', views.mobile, name='mobile'),
    path('mobile/<slug:data>', views.mobile, name='mobiledata'),
    path('checkout/', views.checkout, name='checkout'),
    path('paymentdone/', views.payment_done, name='paymentdone'),


    # --------------------------- Authentication Starts Here ---------------------------    
      
    # Password change done view used in urls only, no such views exist in views.py
    
    path('accounts/login/', auth_views.LoginView.as_view(template_name='app/login.html',
                                                         authentication_form=LoginForm), name='login'),

 # -----------------------logout-------------------
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

# -----------------------password change -----(jese hi passwordchange url pe click hoga vese hii passwordchangeview(uilt-in hai)  vo template ko render krega)  --------------
# ------------ User Accesses the URL ------------
# The user navigates to /passwordchange/, triggering this URL pattern.

# ------------ Django Matches the URL ------------
# Django routes the request to auth_views.PasswordChangeView.as_view() based on the URL pattern.

# ------------ Rendering the Form ------------
# The PasswordChangeView uses MyPasswordChangeForm to render the form on the app/passwordchange.html template.

# ------------ User Submits the Form ------------
# When the user submits the form, Django handles the POST request to process the form.
# The view checks if the current password matches and validates the new password.

# ------------ Password Change Success ------------
# If the form is valid and the password change is successful, the user is redirected to /passwordchangedone/ 
# as specified by the success_url.

# ------------ Redirected to Success Page ------------
# The user sees a confirmation or success page indicating that the password has been changed.

    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='app/passwordchange.html',
                                                                  form_class=MyPasswordChangeForm, success_url='/passwordchangedone/'), name='passwordchange'),


     # -----------------------password change  done -------------------                                                             
    path('passwordchangedone/', auth_views.PasswordChangeView.as_view(
        template_name='app/passwordchangedone.html'), name='passwordchangedone'),

       # -----------------------password reset -------------------   
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='app/password_reset.html',
                                                                 form_class=MyPasswordResetForm), name='password_reset'),

 # -----------------------password reset/done -------------------
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='app/password_reset_done.html'), name='password_reset_done'),

 # -----------------------password reset confirm -------------------
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='app/password_reset_confirm.html', form_class=MySetPasswordForm), name='password_reset_confirm'),

 # -----------------------password reset complete -------------------

    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='app/password_reset_complete.html'), name='password_reset_complete'),
    # ---------------------------- Authentication Ends Here --------------------------------------------  



    path('registration/', views.CustomerRegistrationView.as_view(),
         name='customerregistration'),

   # -------------------------search functionality---------------------------------------------------
    path('search', views.search, name='search')      
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
