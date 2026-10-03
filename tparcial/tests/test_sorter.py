# tests/test_sorter.py
import unittest
from src.tparcial.sorter import Sorter 

class TestSorter(unittest.TestCase):
    
    # SetUp: Se ejecuta antes de cada prueba
    def setUp(self):
        self.sorter = Sorter()

    def test_arreglo_un_elemento(self):
        # Arrange (Inicializar)
        valores_prueba = [5]
        resultado_esperado = [5]
        
        # Act (Ejecutar)
        resultado_actual = self.sorter.bubble_sort(valores_prueba)
        
        # Assert (Verificar)
        self.assertEqual(resultado_actual, resultado_esperado, "El arreglo de 1 elemento no debe cambiar")

    def test_arreglo_ya_ordenado(self):
        # Arrange
        valores_prueba = [1, 2]
        resultado_esperado = [1, 2]
        
        # Act
        resultado_actual = self.sorter.bubble_sort(valores_prueba)
        
        # Assert
        self.assertEqual(resultado_actual, resultado_esperado, "El arreglo ya ordenado debe mantenerse igual")

    def test_arreglo_desordenado(self):
        # Arrange
        valores_prueba = [2, 1]
        resultado_esperado = [1, 2]
        
        # Act
        resultado_actual = self.sorter.bubble_sort(valores_prueba)
        
        # Assert
        self.assertEqual(resultado_actual, resultado_esperado, "El arreglo desordenado debe ordenarse correctamente")

    # TearDown: Opcional, para limpiar recursos (no es estrictamente necesario aquí)
    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
