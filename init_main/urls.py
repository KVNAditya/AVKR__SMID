"""social_mediaand_misleading_informationURL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin as djo_admin
from django.conf.urls import url
from django.conf.urls.static import static
from init_main import settings
from template.agent.py import py__agent as agent
from template.org.py import py__org as org




urlpatterns = [
    url('admin/', djo_admin.site.urls),

    url(r'^$',org.serviceproviderlogin, name="serviceproviderlogin"),
    url(r'View_Remote_Users/$',org.View_Remote_Users,name="View_Remote_Users"),
    url(r'^likeschart/(?P<like_chart>\w+)', org.likeschart, name="likeschart"),
    url(r'^Find_Social_Media_News_Type_Ratio/$', org.Find_Social_Media_News_Type_Ratio, name="Find_Social_Media_News_Type_Ratio"),
    url(r'^Train_Test_DataSets/$', org.Train_Test_DataSets, name="Train_Test_DataSets"),
    url(r'^Predict_Social_Media_News_Type/$', org.Predict_Social_Media_News_Type, name="Predict_Social_Media_News_Type"),
    url(r'^Download_Trained_DataSets/$', org.Download_Trained_DataSets, name="Download_Trained_DataSets"),

    url(r'^login/$', agent.login, name="login"),
    url(r'^Register1/$', agent.Register1, name="Register1"),
    url(r'^Traverse_DataSets/$', agent.Traverse_DataSets, name="Traverse_DataSets"),
    url(r'^ViewYourProfile/$', agent.ViewYourProfile, name="ViewYourProfile"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
