import functools
import operator

def spell_reducer(spells: list[int], operation: str) -> int:
    operations = {
        "min": min,
        "max": max,
        "add": operator.add,
        "multiply": operator.mul
    }

    if operation not in operations:
        return "unknown operation"

    return functools.reduce(operations[operation], spells)

    

def base_enchantment(power, element, target):
    return f"{element} enchantment with power {power} cast on {target}"

def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    return {
        'fire_enchant': functools.partial(base_enchantment, 50, "fire"),
        'ice_enchant': functools.partial(base_enchantment, 50, 'ice'),
        'lightning_enchant': functools.partial(base_enchantment, 50, 'lightning')
    }

@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n):
    if n < 0:
        raise ValueError("n must be >= 0")
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)

def spell_dispatcher():
    @functools.singledispatch
    def cast_spell(spell):
        return f"Unknown spell type: {type(spell).__name__}"

    @cast_spell.register
    def _(spell: int):
        return f"Damage spell deals {spell} damage"

    @cast_spell.register
    def _(spell: str):
        return f"Enchantment cast: {spell}"

    @cast_spell.register
    def _(spell: list):
        return f"Multi-cast spells: {', '.join(str(s) for s in spell)}"

    return cast_spell


def test_functions():
    print("=== Testing partial_enchanter ===")
    enchants = partial_enchanter(base_enchantment)

    print(enchants['fire_enchant']("dragon"))
    print(enchants['ice_enchant']("goblin"))
    print(enchants['lightning_enchant']("wizard"))


    # import time
    # start = time.perf_counter()
    print("\n=== Testing memoized_fibonacci ===")
    print("fib(0):", memoized_fibonacci(0))
    print("fib(1):", memoized_fibonacci(1))
    print("fib(10):", memoized_fibonacci(10))
    print("fib(20):", memoized_fibonacci(20))
    # end = time.perf_counter()
    # print(f"Execution time: {end - start:.4f} seconds")

    print("\n=== Testing spell_dispatcher ===")
    dispatcher = spell_dispatcher()

    print(dispatcher(100))
    print(dispatcher("flame shield"))
    print(dispatcher(["fireball", "ice"]))
    print(dispatcher(3.14))


if __name__ == '__main__':
    test_functions()