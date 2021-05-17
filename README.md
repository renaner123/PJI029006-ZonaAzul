## Proposta do Projeto da disciplina PJI029006 

Tabela de conteúdos
=================
<!--ts-->
   * [Sobre o Projeto](#Sobre)
      * [Requisitos inicias do projeto](#Requisitos-iniciais)
      * [Requisitos inicias do servidor](#O-sistema-servidor-deve)      
   * [Leventamento de requisitos](#Requisitos-funcionais)
      * [Requisitos usuários](#Requisitos-funcionais-usuários)
      * [Requisitos fiscais](#Requisitos-funcionais-fiscais)
      * [Requisitos servidor](#Requisitos-funcionais-servidor)
      * [Requisitos totem](#Requisitos-funcionais-totem)
      * [Requisitos não funcionais](#Requisitos-não-funcionais)
   * [Regras de negócio](#Regras-de-negócio)

<!--te-->

![cenario](img/cenario.png)

Sistema de estacionamento "zona azul" para uma cidade.

### Requisitos iniciais:
* Prever a possibilidade de vários totems para cobrir a * cidade toda.
* O usuário pode fazer o pagamento no Totem ou por meio digital usando o smartphone.
* Os sensores podem ser com fio ou sem fio.
* O totem deve prover uma interface de serviço para adição, configuração e remoção de
sensores.

### O sistema servidor deve:
* Reportar o número de vagas ocupadas; 
* Localização de  vagas na cidade;
* Gerar sinais de alerta para os fiscais; 
* Informações para usuário sobre o tempo
decorrido;
* Gerar alerta de tempo expirado


## Requisitos Funcionais

<h4 align="center"> 
	🚧 Em construção...  🚧
</h4>

### Requisitos funcionais usuários:
* Cadastrar usuário
* Cadastrar veículo
* Efetuar pagamento
* Renovar vaga em uso
* Alterar veículo do cadastro
* Verificar tempo decorrido
* Histórico de pagamentos

### Requisitos funcionais fiscais:
* Verificar status do veículo do usuário
* Gerar notificação para o usuário

### Requisitos funcionais servidor:
* Cadastrar fiscais
* Receber pagamento
* Reportar o número de vagas ocupadas; 
* Localizar  vagas na cidade; 
* Gerar sinais de alerta para os fiscais; 
* Gerar alerta de tempo expirado para o usuário

### Requisitos funcionais totem:
* Adicionar sensores
* Remover sensores
* Configurar sensores
* Verificar status de ocupação do sensor
* Efetuar pagamento
* Listar sensores

### Requisitos não funcionais
* Aplicativo deve ser desenvolvido na linguagem Java
* A interface do usuário deve ser simples e objetiva...
* Os sensores devem ser sem fio


## Regras de negócio.

<h4 align="center"> 
	🚧 Em construção...  🚧
</h4>

* Usuário não pode estacionar por mais de 4 horas por dia na mesma vaga
* Usuário só pode cadastrar 1 veículo
* Totem não pode ter mais de 50 sensores cadastrados
* Servidor deve notificar os usuário quando estiver faltando 10 minutos para acabar o seu tempo.
* Servidor deve notificar os fiscais sempre que um usuário teve seu tempo expirado.
