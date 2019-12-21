from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.exceptions import APIException, AuthenticationFailed

from core.models import Tag

from recipe import serializers


class TagViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
	"""Manage tags in the db"""
	authentication_classes = (TokenAuthentication, )
	permission_classes = (IsAuthenticated, )
	queryset = Tag.objects.all()
	serializer_class = serializers.TagSerializer

	def get_queryset(self):
		"""Return objects for the current authenticated user only"""
		if self.request.user.is_authenticated:
			return self.queryset.filter(user=self.request.user).order_by('-name')
		else:
			raise AuthenticationFailed()
