from django.test import TestCase
from aluraflix.models import Programa

class ProgramaModelTestCase(TestCase):
    def setUp(self):
        self.programas = Programa(
            titulo = 'Procurando ninguém',
            data_lancamento = '2003-07-04'
        )

    def test_verifica_atributos_do_programa(self):
        """ Teste que verifica atributos de um programa com valores default """
        self.assertEqual(self.programas.titulo, 'Procurando ninguém')
        self.assertEqual(self.programas.tipo, 'F')
        self.assertEqual(self.programas.likes, 0)
        self.assertEqual(self.programas.dislikes, 0)
        