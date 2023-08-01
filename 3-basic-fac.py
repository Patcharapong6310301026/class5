#3-basic-fac
# import asyncio and time.
import asyncio
import time

async def factorial(n):
    f = 1
    for i in range(2, n+1):
        print(f"Computing factorial({n}), currently i={i}...")
        # delay 1 seconds
        await asyncio.sleep(1)
        f *= i
    return f

async def main():
    # schedule three calls concurrently.
    L = await asyncio.gather(factorial(2), factorial(3), factorial(4))
    print(L) # [2, 6, 24]
    
if __name__ == '__main__':
    # set time Start.
    start = time.time()
    # run main function.
    asyncio.run(main())
    # set time End.
    end = time.time()
    print(f'Time: {end-start:.2f} sec')    
