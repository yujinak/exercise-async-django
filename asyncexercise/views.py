import asyncio
from time import sleep

import httpx
from django.http import HttpResponse

async def http_call_async():
    print('Contador de tempo:')
    for num in range(1, 6):
        await asyncio.sleep(1)
        print(num, 's')
    async with httpx.AsyncClient() as client:
        r = await client.get('https://httpbin.org')
        print(r)

async def async_view(request):
    loop = asyncio.get_event_loop()
    loop.create_task(http_call_async())
    return HttpResponse('Aplicação assíncrona - Requisição HTTP concluída!')
