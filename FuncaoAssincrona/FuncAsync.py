import asyncio
import time

##USO DO asyncio.sleep PARA SIMULAR CHAMADA DE REDE
async def _sleep(tempo):
    await asyncio.sleep(tempo)



async def _funcao_asincrona (tempo1, tempo2, tempo3):

    #USO DO asyncio.TaskGroup() PARA CRIAR E EXECUTAR AS 3 TASKS DE UMA VEZ SIMULANDO AS CHAMADAS DE REDE
    async with asyncio.TaskGroup() as tg:
        #DECLARAÇÃO DAS TASKS COM asyncio.sleep A SEREM EXECUTADAS
        task1 = tg.create_task(_sleep(tempo1))
        task2 = tg.create_task(_sleep(tempo2))
        task3 = tg.create_task(_sleep(tempo3))

        # GUARDA O TEMPO INICIAL
        inicio = time.perf_counter()


    #GUARDA O TEMPO FINAL APOS A EXECUÇÃO DO asyncio.TaskGroup()
    fim = time.perf_counter()

    #CALCULA O TEMPO TOTAL GASTO EM SEGUNDOS FORMATADO COM 2 CASAS DECIMAIS
    print(f'Tempo total Gasto: {fim - inicio:.2f} segundos')  # Calcula e retorna o tempo total gasto

##chamando com asyncio.run por ser uma função asincrona
asyncio.run(_funcao_asincrona(1,3,3))