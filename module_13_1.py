import asyncio

async def start_strongman(name, power):
    print(f"Силач {name} начал соревнования.")
    for balls in range(1, 6):
        print(f"Силач {name} поднял {balls}")
        await asyncio.sleep(power)
    print(f"Силач {name} закончил соревнования.")
    
async def main():
    task1, task2, task3 = asyncio.create_task(start_strongman('Pasha', 3)), asyncio.create_task(start_strongman('Denis', 4)), asyncio.create_task(start_strongman('Apollon', 5))
                          
    for t in [task1, task2, task3]:
        await t
    

asyncio.run(main())
