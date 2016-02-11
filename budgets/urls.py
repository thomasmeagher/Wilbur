from django.conf.urls import url
from django.contrib.auth import views as auth_views
from cuser.forms import UserAuthenticationForm

from budgets import views

urlpatterns = [
    url(r'^$', views.OverviewView.as_view(), name='overview'),

    url(r'^budgets/$', views.BudgetsView.as_view(), name='budgets'),
    url(r'^budgets/add/$', views.BudgetsAddView.as_view(), name='add-budget'),
    url(r'^budgets/edit/(?P<budget_id>[0-9]+)/$', views.BudgetsEditView.as_view(), name='edit-budget'),
    url(r'^budgets/delete/(?P<budget_id>[0-9]+)/$', views.delete_budget, name='delete-budget'),

    url(r'^transactions/$', views.TransactionsView.as_view(), name='transactions'),
    url(r'^transactions/budget/(?P<budget_id>[0-9]+)/$', views.TransactionsView.as_view(), name='transactions-filter'),
    url(r'^transactions/add/$', views.TransactionsAddView.as_view(), name='add-transaction'),
    url(r'^transactions/edit/(?P<transaction_id>[0-9]+)/$', views.TransactionsEditView.as_view(),
        name='edit-transaction'),
    url(r'^transactions/delete/(?P<transaction_id>[0-9]+)/$', views.delete_transaction, name='delete-transaction'),

    url(r'^profile/$', views.ProfileView.as_view(), name='profile'),
    url(r'^profile/edit/password/$', views.PasswordEditView.as_view(), name='edit-password'),

    url('^signup/$', views.SignUpView.as_view(), name="signup"),
    url('^login/$', auth_views.login, {
        'template_name': 'registration/login.html',
        'redirect_field_name': 'next',
        'authentication_form': UserAuthenticationForm,
    }, name="login"),
    url('^logout/$', auth_views.logout, {'next_page': '/'}, name="logout"),

    url(r'^style/$', views.StyleGuideView.as_view(), name='style'),
]
