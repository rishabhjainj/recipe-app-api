from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from user.serializers import UserSerializer, MyAuthTokenSerializer
from rest_framework.exceptions import APIException, AuthenticationFailed


class CreateUserView(generics.CreateAPIView):
	"""Create a new user in the system"""
	serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
	"""Create a new auth token for user"""
	serializer_class = MyAuthTokenSerializer
	renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(generics.RetrieveUpdateAPIView):
	"""Manage the authenticated view"""
	serializer_class = UserSerializer
	authentication_classes = (authentication.TokenAuthentication,)
	permissions_classes = (permissions.IsAuthenticated,)

	def get_object(self):
		"""Retrieve and return authenticated user"""
		user = self.request.user
		if user.is_authenticated:
			return user
		else:
			raise AuthenticationFailed()


