from django import test
from django.test import TestCase
from aluraflix.models import Programa


class ProgamaTestModelsCase(TestCase):
    def setUp(self):
        self.progama = Programa(
            titulo='Ednaldo Pereira em busca do vale nada vale tudo',
            data_lancamento='2021-05-01'
        )

    def test_verifica_atributos_do_progama(self):
        """Teste que verifica os campos do banco"""
        self.assertEqual(self.progama.titulo,
                         'Ednaldo Pereira em busca do vale nada vale tudo')
        self.assertEqual(self.progama.tipo, 'F')
        self.assertEqual(self.progama.data_lancamento, '2021-05-01')
        self.assertEqual(self.progama.likes, 0)
        self.assertEqual(self.progama.dislikes, 0)
