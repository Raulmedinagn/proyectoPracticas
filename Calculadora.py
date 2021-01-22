from Calculador import Calculador

class Calculadora(Calculador):
    def get_precision(self,relevantes, recuperados):
        precision =((relevantes/recuperados) * recuperados)/recuperados
        return precision
    """
    De esta forma, cuanto más se acerque el valor de la precisión al valor nulo, mayor será el número de documentos recuperados que no consideren relevantes. Si por el contrario, el valor de la precisión es igual a uno, se entenderá que todos los documentos recuperados son relevantes. Esta forma de entender la precisión introduce el concepto de ruido informativo y de silencio informativo.
    """
    def get_exhaustividad(self,relevantes, recuperados):
        exhaustividad =((relevantes/recuperados) * recuperados)/relevantes
        return exhaustividad
    """
    Si el resultado de esta fórmula arroja como valor 1, se tendrá la exhaustividad máxima posible, y esto viene a indicar que se ha encontrado todo documento relevante que residía en la base de datos, por lo tanto no se tendrá ni ruido, ni silencio informativo: siendo la recuperación de documentos entendida como perfecta. Por el contrario en el caso que el valor de la exhaustividad sea igual a cero, se tiene que los documentos obtenidos no poseen relevancia alguna.
    """
    def execute(self,tipo,relevantes,recuperados):
        if tipo == "precision":
            return self.get_precision(relevantes, recuperados)
        if tipo == "exhaustividad":
            return self.get_exhaustividad(relevantes, recuperados)