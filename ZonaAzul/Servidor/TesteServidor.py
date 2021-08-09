from InterfaceUsuario import InterfaceUsuario
from Usuario import Usuario

if __name__ == '__main__':
    
    interface = InterfaceUsuario()

    user = Usuario("Renan", "08299152909", "renan@teste")
    user2 = Usuario("Renan", "12345678901", "x@gmail")

    interface.criarConta(user,"renaner123","444998")
    interface.criarConta(user2,"lara","444998")
    #interface.criarConta(user2,"renaner123","444998")

    print(interface.fazerLogin("renaner123","444998"))

    interface.cadastrarVeiculo(user,"MIJ5419", "Uno")

    interface.efetuarPagamento(user, 2, "123")


    print(interface.getUsuarios())



    