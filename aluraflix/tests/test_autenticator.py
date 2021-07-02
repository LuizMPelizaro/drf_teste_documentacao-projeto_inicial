from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework import status


class AutenticatorUserTestCase(APITestCase):
    def setUp(self):
        self.list_url = reverse('programas-list')
        self.user = User.objects.create_user(
            'c3p0', password='123456'
        )

    def test_autenticacao_user_com_credencias_corretas(self):
        """Teste de autenticação de usuario com as credenciais corretas"""
        user = authenticate(username='c3p0', password='123456')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_autenticacao_user_com_username_incorretas(self):
        """Teste de autenticação de um usuario com as credencial de usuario incorretas"""
        user = authenticate(username='c3po', password='123456')
        self.assertFalse((user is not None) and user.is_authenticated)

    def test_autenticacao_user_com_password_incorreto(self):
        """Teste de autenticação de um usuario com a credencial de senha incorreta"""
        user = authenticate(username='c3p0', password='123457')
        self.assertFalse((user is not None) and user.is_authenticated)

    def test_requisicao_get_nao_autorizada(self):
        """Teste do metodo GET que o usuario não foi autorizado"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_requisicao_get_user_autorizado(self):
        """Teste do metodo GET com um usuario autenticado"""
        self.client.force_authenticate(self.user)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
