Tabela de conteúdos
=================
<!--ts-->
   * [Requisitos inicias do projeto](#Requisitos-iniciais)  
   * [Leventamento de requisitos](#Requisitos-funcionais)
      * [Requisitos do Servidor](#Requisitos-funcionais-servidor)
      * [Requisitos do Totem](#Requisitos-funcionis-totem)
   * [Regras de negócio](#Regras-de-negócio)
   * [Diagrama de casos de uso](#Diagramas-de-casos-de-uso)
      * [Diagrama de casos de uso lado servidor](#Diagrama-de-casos-de-uso-do-servidor)
      * [Diagrama de casos de uso lado totem](#Diagrama-de-casos-de-uso-do-totem)
<!--te-->

## Proposta do Projeto da disciplina PJI029006 

<div style="text-align:center">
   <img src="./img/cenario.PNG" />
</div>

Sistema de estacionamento "zona azul" para uma cidade.

### Requisitos iniciais:
* Prever a possibilidade de vários totems para cobrir a * cidade toda.
* O usuário pode fazer o pagamento no Totem ou por meio digital usando o smartphone.
* Os sensores podem ser com fio ou sem fio.
* O totem deve prover uma interface de serviço para adição, configuração e remoção de
sensores.
*  O sistema servidor deve:
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

### Requisitos funcionais servidor:
* Servidor de informar o número de vagas ocupadas 
* Servidor deve localizar vagas na cidade 
* Servidor deve gerar notificações para os fiscais caso haja alguma vaga com tempo excedido
* Servidor deve gerar notificação de tempo expirando para o usuário
* Servidor deve gerar notificação para o técnico se algum sensor estiver inoperante
* Permitir o usuário criar uma conta
* Permitir o usuário se autenticar no sistema
* Permitir o usuário Cadastrar um veículo
* Permitir o usuário Alterar veículo do cadastrado
* Permitir o usuário Efetuar pagamento
* Permitir o usuário Renovar vaga em uso
* Permitir o usuário Verificar tempo decorrido
* Permitir o usuário ver histórico de pagamentos
* Permitir o fiscal se autenticar no sistema
* Permitir o fiscal a verificar status do veículo
* Permitir o fiscal gerar notificação de não conformidade para o veículo
* Permitir o Totem cadastrar os sensores no servidor
### Requisitos funcionis totem
* Permitir o técnico a logar no sistema de manutenção
* Permitir o técnico adicionar sensores
* Permitir o técnico remover sensores
* Permitir o técnico configurar sensores
* Permitir o técnico verificar status dos sensores
* Permitir o usuário cadastrar veículo na vaga
* Permitir o usuário definir o tempo de estacionamento
* Permitir o usuário efetuar pagamento
* Permitir o servidor consultar status dos sensores 
* Permitir o servidor consultar status das vagas

### Requisitos não funcionais
* Aplicativo deve ser desenvolvido na linguagem Java
* A interface do usuário deve ser simples e objetiva
* Os sensores devem ser sem fio

## Regras de negócio.

<h4 align="center"> 
	🚧 Em construção...  🚧
</h4>

* Usuário não pode estacionar por mais de 2 horas por dia na mesma vaga
* Usuário só pode cadastrar 1 veículo
* Servidor deve notificar os usuário quando estiver faltando 10 minutos para acabar o seu tempo.
* Servidor deve bloquear o usuário se tiver 3 notificações no período de 1 mês.

## Diagramas de casos de uso

### Diagrama de casos de uso do servidor

<div style="text-align:center">
   <img src="./img/cases_servidor.png" />
</div>

### Diagrama de casos de uso do totem

<div style="text-align:center">
   <img src="./img/cases_totem.png" />
</div>