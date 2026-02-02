import random

# Flip a coin 100 times
flips = [random.choice(['Heads', 'Tails']) for _ in range(100)]

# Count heads and tails
heads_count = flips.count('Heads')
tails_count = flips.count('Tails')

# Display results
print(f"Heads（Heads）: {heads_count}次")
print(f"Tails（Tails）: {tails_count}次")