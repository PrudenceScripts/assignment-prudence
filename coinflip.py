import random

def coin_flip_simulation(n_flips=10):
    results = [random.choice(['Heads', 'Tails']) for _ in range(n_flips)]
    print("Coin Flip Results:")
    print(results)
    heads_count = results.count('Heads')
    tails_count = results.count('Tails')
    print(f"Heads: {heads_count}, Tails: {tails_count}")

coin_flip_simulation()
