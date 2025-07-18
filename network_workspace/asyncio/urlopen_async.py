from time import time
from urllib.request import Request, urlopen
import asyncio

urls=['https://www.google.co.kr/search?q=' + i
      for i in ['apple','pear','grape','pineapple', 'orange','strawberry']]

async def fetch(url):
    #뭐가 없으면 403 에러
    request = Request(url, headers={'User-Agent' : 'Mozilla/5.0'})
    #run_in_executor 사용
    loop=asyncio.get_running_loop()
    response=await loop.run_in_executor(None, urlopen, request)
    #run in executor 사용
    page=await loop.run_in_executor(None, response.read)
    return len(page)

async def main():
    futures=[asyncio.ensure_future(fetch(url)) for url in urls]
    
    #결과를 한꺼번에 가져옴
    result=await asyncio.gather(*futures)
    print(result)

begin=time()
asyncio.run(main())
end=time()
print('실행 시간 : {0:.3f}초'.format(end-begin))
