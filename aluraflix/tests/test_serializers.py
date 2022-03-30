from django.test import TestCase
from aluraflix.models import Programa
from aluraflix.serializers import ProgramaSerializer


class ProgramaSerializerTestCase(TestCase):

    
    def setUp(self):
        self.programa = Programa(
            titulo = 'Procurando Ninguém',
            data_lancamento  = '2007-04-09',
            tipo = 'F',
            likes = 20090,
            dislikes = 1500
        )

        self.serializer = ProgramaSerializer(instance=self.programa)



    def test_verifica_campos_serializados(self):
        """ Teste para verificar se os campos necessários estão sendo serializados """

        data = self.serializer.data

        self.assertEqual(set(data.keys()), set(['titulo', 'tipo', 'data_lancamento', 'likes']))



    def test_verifica_conteudo_campos_serializados(self):
        """ Teste para verificar o conteúdo dos campos que estão sendo serializados """

        data = self.serializer.data

        self.assertEqual(data['titulo'],self.programa.titulo)
        self.assertEqual(data['data_lancamento'],self.programa.data_lancamento)
        self.assertEqual(data['tipo'],self.programa.tipo)
        self.assertEqual(data['likes'],self.programa.likes)
