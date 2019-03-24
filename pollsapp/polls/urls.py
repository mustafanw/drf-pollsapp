from django.urls import path
from pollsapp import routers

from . import views
from . import api

router = routers.SharedAPIRootRouter()
router.register(r'questions', api.QuesViewSet)
router.register(r'choices', api.ChoiceViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('pollqn', views.pollqn),
    path('pollch', views.pollch),
    path('polltr', views.polltr),
    path('pollqnAdd', views.pollqn),
    path('editqn/<int:id>', views.editqn),
    path('editch/<int:id>', views.editch),
    path('edittr/<int:id>', views.edittr),
    path('viewqn', views.QuesViewSet),
    path('viewch', views.ChoiceViewSet),
    path('viewtr', views.TrackViewSet),
    path('updateqn/<int:id>', views.updateqn),
    path('updatech/<int:id>', views.updatech),
    path('updatetr/<int:id>', views.updatetr),
    path('deleteqn/<int:id>', views.destroyqn),
    path('deletech/<int:id>', views.destroych),
    path('deletetr/<int:id>', views.destroytr),

    path('viewqnch', views.QnChViewSet),
]
