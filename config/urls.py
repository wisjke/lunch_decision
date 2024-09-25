from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core.views import RestaurantCreateView, MenuViewSet, EmployeeCreateView, VoteViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.DefaultRouter()
router.register(r'api/create_restaurant', RestaurantCreateView)
router.register(r'api/menus', MenuViewSet)
router.register(r'api/create_employee', EmployeeCreateView)
router.register(r'api/votes', VoteViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
