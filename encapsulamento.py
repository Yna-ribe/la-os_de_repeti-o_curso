print('acesso a mensagens da empresa para gerentes, analistas e estagiarios')
funcionarios= ["gerente","analista","estagiario"]
dias=['domingo','segunda-feira','terça-feira','quarta-feira','quinta-feira','sexta-feira','sabado']
acesso=input('digite seu cargo: ')
dia_do_acesso=input('digite o dia da semana: ')

class funcionario:
    def __init__(self,cargo):
        self.cargo=cargo
class gerente(funcionario):
    def dia (self,dias_da_semana):
        if(acesso == 'gerente' and dia_do_acesso == dias_da_semana):
            print ('Acesso permitido', acesso)
        return

class analista(funcionario):
    def dia (self):
        if(acesso == 'analista' and dia_do_acesso in dias[1:6]):
            print('acesso permitido ',acesso)
        else:
            print('acesso negado')
        return

class estagiario(funcionario):
    def dia (self, dia_do_acesso):
        if (acesso == estagiario and dia_do_acesso in dias[1:6]):
            print('acesso permitido ',acesso)
        else:
            print('acesso negado')
        return

'''def main ():
    car = Carro()
    cam = Caminhao()
    bike = Bicicleta()
    distancia =100
    quantcombustivel = 10
    tempo_carro = car.calcular(distancia)
    tempo_caminhao = cam.calcular(distancia)
    tempo_bicicleta = bike.calcular(distancia)

    custo_carro = car.Abastecer(quantcombustivel)
    custo_caminhao = cam.Abastecer(quantcombustivel)
    custo_bicicleta = bike.Abastecer(quantcombustivel)

    print('Tempo carro' ,tempo_carro)
    print('Tempo caminhao' ,tempo_caminhao)
    print('Tempo Bicicleta' ,tempo_bicicleta)

    print('Custo do carro: ' ,custo_carro)
    print('Custo do caminhao: ' ,custo_caminhao)
    print('Custo da Bicicleta: ' ,custo_bicicleta)
main()'''