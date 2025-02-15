# Programação Asíncrona com Python 🚀

Este script é um exemplo simples de implementação de uma função assíncrona em Python que faz três chamadas simuladas de rede com `asyncio.sleep` e retorna o tempo total de execução. O objetivo é mostrar o ganho de performance com execução assíncrona.

## Tecnologias Utilizadas 🧑‍💻

- **Python 3.13.2**  
- **Biblioteca `asyncio`**  
- **Biblioteca `time`**  

---

## Funcionamento ⚙️

### Execução Assíncrona 🔄

O script é composto por duas funções: 
- `_sleep(tempo)` 
- `_funcao_asincrona(tempo1, tempo2, tempo3)`.

#### Explicação:

- A função principal é a `_funcao_asincrona(tempo1, tempo2, tempo3)` que recebe 3 valores em segundos e faz três chamadas para a função `_sleep(tempo)`, que simula uma chamada de rede.
- O script utiliza a função `asyncio.TaskGroup()` para instanciar e executar as três chamadas **simultaneamente**.

Executar com Python o Arquivo `"FuncAsync.py"`.

Após a execução, o tempo total é exibido no console.

### Exemplo Visual 🌟

```python
import asyncio
import time

## USO DO asyncio.sleep PARA SIMULAR CHAMADA DE REDE
async def _sleep(tempo):
    await asyncio.sleep(tempo)

async def _funcao_asincrona(tempo1, tempo2, tempo3):

    # USO DO asyncio.TaskGroup() PARA CRIAR E EXECUTAR AS 3 TASKS DE UMA VEZ SIMULANDO AS CHAMADAS DE REDE
    async with asyncio.TaskGroup() as tg:
        # DECLARAÇÃO DAS TASKS COM asyncio.sleep A SEREM EXECUTADAS
        task1 = tg.create_task(_sleep(tempo1))
        task2 = tg.create_task(_sleep(tempo2))
        task3 = tg.create_task(_sleep(tempo3))

        # GUARDA O TEMPO INICIAL
        inicio = time.perf_counter()

    # GUARDA O TEMPO FINAL APOS A EXECUÇÃO DO asyncio.TaskGroup()
    fim = time.perf_counter()

    # CALCULA O TEMPO TOTAL GASTO EM SEGUNDOS FORMATADO COM 2 CASAS DECIMAIS
    print(f'Tempo total Gasto: {fim - inicio:.2f} segundos')  # Calcula e retorna o tempo total gasto

## Chamando com asyncio.run por ser uma função assíncrona
asyncio.run(_funcao_asincrona(1, 3, 3))
```


## Como funciona:
As funções são **assíncronas**, o que significa que são executadas **simultaneamente**.  
Mesmo inserindo **2 delays de 3 segundos** e **1 delay de 1 segundo**, a execução do script dura **apenas 3 segundos**, provando a eficiência da execução assíncrona! ⚡

---

## Vantagens de Execução Assíncrona 📈

- **Redução do tempo total de execução** ⏱️
- **Maior eficiência em chamadas simultâneas** ⚡
- **Aproveitamento otimizado de recursos do sistema** 💻

---

## Resultado esperado:

**Tempo total de execução: 3 segundos**  
(Em vez de 7 segundos como seria em uma execução síncrona)

---

## Imagem de Demonstração 📊

![Exemplo de execução assíncrona](https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExYnFkazd3ZXBzN3p3eHFldDk2YXdiejhnOXZuMDd5bHVhY2Q4dTVpciZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/XWDtz4xtKVDPs6ayI8/giphy.gif)

---

## Conclusão 🎯

Esse exemplo simples de **programação assíncrona** em Python mostra como podemos melhorar a performance em aplicações que realizam múltiplas tarefas simultâneas, como chamadas de rede.

---

### ⭐ **Dica**: 
Experimente modificar os tempos e veja como a execução assíncrona mantém a performance consistente!

---

### **Referências e Links Úteis** 🔗

- [Documentação oficial do Python - asyncio](https://docs.python.org/3/library/asyncio.html)
- [Python 3.13.2 Release Notes](https://docs.python.org/3/whatsnew/3.13.html)
