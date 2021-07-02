from django.test import TestCase

from aluraflix.models import Programa
from aluraflix.serializers import ProgramaSerializer


class ProgramaSerializerTestCase(TestCase):
    def setUp(self):
        self.programa = Programa(
            titulo='Ednaldo Pereira em busca do vale nada vale tudo',
            tipo='F',
            data_lancamento='2021-05-01',
            likes=1054,
            dislikes=0
        )
        self.serializer = ProgramaSerializer(instance=self.programa)

    def test_verifica_serializer(self):
        """Teste que verifica os campos que estão sendo serializados """
        data = self.serializer.data
        # A variavel data pega todos os campos do serilizer
        self.assertEqual(set(data.keys()), set(
            ['titulo', 'tipo', 'data_lancamento', 'likes', 'dislikes']))
        # set(data.keys()) garante que a saida do serializer tenha as chaves exatas

    def test_verifica_conteudo_dos_campos_serializardos(self):
        """Teste que verifica se o conteudo dos campos serializados é igual ao do banco"""
        data = self.serializer.data
        self.assertEqual(data['titulo'], self.programa.titulo)
        self.assertEqual(data['tipo'], self.programa.tipo)
        self.assertEqual(data['data_lancamento'],
                         self.programa.data_lancamento)
        self.assertEqual(data['likes'], self.programa.likes)
        # self.assertEqual(data['dislikes'],self.programa.dislikes)
