from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework import status



class AuthenticationUserTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('programas-list')
        self.user = User.objects.create_user('c3po', password = '123456')

    def test_verifica_se_usuario_consegue_autenticar(self):
        """ Varifica se usuario criado consegue authenticar corretamente """

        user = authenticate(username='c3po', password = '123456')

        self.assertTrue((user is not None) and user.is_authenticated)

    def test_requisicao_get_nao_autorizada(self):
        """ Teste que verifica uma GETrequisicao sem autenticar  """
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    def test_verifica_se_usuario_nao_consegue_autenticar_com_username_errado(self):
        """ Varifica se usuario criado não consegue autenticar com o username errado"""

        user = authenticate(username='c3pt', password = '123456')

        self.assertFalse((user is not None) and user.is_authenticated)

    def test_verifica_se_usuario_nao_consegue_autenticar_com_senha_errada(self):
        """ Varifica se usuario criado não consegue autenticar com o senha errada"""

        user = authenticate(username='c3po', password = '123456XS')

        self.assertFalse((user is not None) and user.is_authenticated)

    def test_requisicao_get_com_usuario_autenticado(self):
        """ Varifica se usuario autenticado consegue fazer uma requisicao GET com status 200 """

        self.client.force_authenticate(self.user)

        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)