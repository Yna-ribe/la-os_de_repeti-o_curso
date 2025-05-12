class ProdutoEletronico:
  def __init__(self, nome, marca, preco):
      self.nome = nome
      self.marca = marca
      self.preco = preco

  def exibir_informacoes(self):
      print(f"Nome: {self.nome}, Marca: {self.marca}, Preço: {self.preco}")

class Smartphone(ProdutoEletronico):
  def __init__(self, nome, marca, preco, armazenamento, ligado, volume):
      super().__init__(nome, marca, preco)
      self.armazenamento = armazenamento
      self.ligado=ligado
      self.volume = volume

  def exibir_informacoes(self):
      super().exibir_informacoes()
      print(f"Armazenamento: {self.armazenamento}GB")
      if(self.ligado == True):
          print('o celular está ligado')
      else:
          print('o celular está desligado')

  def aumentar_volume(self):
      if (self.ligado == False):
          print('não é possivel aumenta o volume')
      else:
          self.volume=self.volume + 10
          print(f"O celular está com {self.volume} de volume")

  def diminuir_volume(self):
      if (self.ligado == False):
          print('não é possivel aumenta o volume')
      else:
          self.volume=self.volume - 10
          print(f"O celular está com {self.volume} de volume")

  def ligar(self):
      self.ligado = True

class Laptop(ProdutoEletronico):
  def __init__(self, nome, marca, preco, memoria_ram):
      super().__init__(nome, marca, preco)
      self.memoria_ram = memoria_ram

  def exibir_informacoes(self):
      super().exibir_informacoes()
      print(f"Memória RAM: {self.memoria_ram}GB")

class Televisor(ProdutoEletronico):
  def __init__(self, nome, marca, preco, tamanho):
      super().__init__(nome, marca, preco)
      self.tamanho = tamanho

  def exibir_informacoes(self):
      super().exibir_informacoes()
      print(f"Tamanho: {self.tamanho}\"")

smar=Smartphone("iphone 15 PRO MAX","apple",13000,128, True, 30)
smar.diminuir_volume()
smar.exibir_informacoes()
smar2=Smartphone('Redmi Note 12','Xiaomi',1000,64, False, 51)
smar2.ligar()
smar2.aumentar_volume()
smar2.exibir_informacoes()
