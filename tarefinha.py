from tarefa import Pessoa
from tarefa import Carro

atributos1 = Pessoa("Obama", 63, "Havai", "Im very good at videogames")
atributos2 = Pessoa("Raila", 12, "Ivannova", "Criarei um novo paraíso")
atributos3 = Pessoa("Keffera", 520, "São Paulo", "Tenha piedade de mim")

atributos1.exibirDados()
atributos2.exibirDados()
atributos3.exibirDados()

#==========================================================================================

atributosCarro1 = Carro("Fiat", "Uno", 1971)
atributosCarro2 = Carro("Audi", "R8", 2014)
atributosCarro3 = Carro("Tesla", "Cybertruck", 2019)

atributosCarro1.carroDados()
atributosCarro1.acelera()

atributosCarro2.carroDados()
atributosCarro2.acelera()

atributosCarro3.carroDados()
atributosCarro3.freia()