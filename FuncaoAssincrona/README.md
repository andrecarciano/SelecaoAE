# Assynchronous Programming com Python

Este script é um exemplo simples de implementação de uma função assíncrona em Python que 
faz três chamadas simuladas de rede com asyncio.sleep e retorna o tempo total de execução. 
O objetivo é mostrar o ganho de performance com execução assíncrona.

## Técnologias Ultilizadas
### Python 3.13.2 - Biblioteca (asyncio) - Biblioteca (time)

## Funcionamento

### Execução Asíncrona

O script é composto por duas funções: _sleep(tempo) e _funcao_asincrona (tempo1, tempo2, tempo3).

A função principal é a _funcao_asincrona (tempo1, tempo2, tempo3) que recebe 3 valores em segundos
e faz tres chamadas para a função _sleep(tempo) que simula a chamada de rede.

O script utiliza a função asyncio.TaskGroup() para estanciar e executar as tres chamadas ao mesmo tempo.

Após a execução o tempo total é exibido no console.

Como são funções assíncronas executadas ao mesmo tempo, podemos notar que mesmo inserindo 2 delays de 3 segundo 
e 1 delay de 1 segundo execução dura apenas 3 segundos, provando a eficiência da execução assíncrona.

