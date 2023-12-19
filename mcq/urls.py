from django.urls import path
from . import views
from django.urls import path, include


urlpatterns = [path('', views.login, name='login'),
               path('signup/', views.signup, name='signup'),
               path('home/', views.home, name='home'),
               path('logout/', views.logout, name='logout'),
               path('testList/', views.testList, name='testList'),
               path('testContent/<str:lang>',
                    views.testContent, name='testContent'),
               path('testInstruction/<str:cont>/<str:languageName>', views.testInstruction,
                    name='testInstruction'),
               path('questions/<str:languageTopic>',
                    views.questions, name='questionPage'),
               path('questionPart/<str:languageTopic>', views.questionsPagePart2,
                    name='questionsPart'),
               path('resultPage/',
                    views.resultLogic, name='resultPage'),
               path('demo/', views.demo, name="demo"),
               # path('image',)

               ]
