#2-3-basic-gather-more
# import asyncio and time.
import asyncio
import time

# build hello function : sent output as started and done time.
async def hello(i):
    print(f"{time.ctime()} hello {i} started")
    # delay 4 seconds
    await asyncio.sleep(4)
    print(f"{time.ctime()} hello {i} done")

# build main and build 2 tasks    
async def main():
    # collect many coroutines together into a coros list
    coros = [hello(i) for i in range(10)]
    # unwrapping the coros list into separate expressions.
    await asyncio.gather(*coros)
    
if __name__ == '__main__':
    # set time Start.
    start = time.time()
    # run main function.
    asyncio.run(main())
    # set time End.
    end = time.time()
    print(f'Time: {end-start:.2f} sec')    