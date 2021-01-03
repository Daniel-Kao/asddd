from .views import LanguageViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('snippets/(?P<lang_id>[0-9a-f-]+)/languages', LanguageViewSet, basename='language')
urlpatterns = router.urls