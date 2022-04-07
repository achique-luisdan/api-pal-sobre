from rest_framework.routers import SimpleRouter
from .views import ExpenseViewset, GoalViewset

from django.urls import path

router = SimpleRouter()
router.register('expenses', ExpenseViewset)
router.register('goals', GoalViewset)

urlpatterns = router.urls