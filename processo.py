from abc import ABC, abstractmethod


class Veiculo(ABC):

    def calcular(self, distancia):
        pass

    def Abastecer(self, quantcombustivel):
        pass


class Carro(Veiculo):

    def calcular(self, distancia):
        return distancia / 60

    def Abastecer(self, quantcombustivel):
        return quantcombustivel * 5


class Caminhao(Veiculo):

    def calcular(self, distancia):
        return distancia / 40

    def Abastecer(self, quantcombustivel):
        return quantcombustivel * 4


class Bicicleta(Veiculo):

    def calcular(self, distancia):
        return distancia / 15

    def Abastecer(self, quantcombustivel):
        return quantcombustivel * 50


def main():
    car = Carro()
    cam = Caminhao()
    bike = Bicicleta()
    distancia = 100
    quantcombustivel = 10
    tempo_carro = car.calcular(distancia)
    tempo_caminhao = cam.calcular(distancia)
    tempo_bicicleta = bike.calcular(distancia)

    custo_carro = car.Abastecer(quantcombustivel)
    custo_caminhao = cam.Abastecer(quantcombustivel)
    custo_bicicleta = bike.Abastecer(quantcombustivel)

    print('Tempo carro', tempo_carro)
    print('Tempo caminhao', tempo_caminhao)
    print('Tempo Bicicleta', tempo_bicicleta)

    print('Custo do carro: ', custo_carro)
    print('Custo do caminhao: ', custo_caminhao)
    print('Custo da Bicicleta: ', custo_bicicleta)


main()
