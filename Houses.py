class House:
    def __init__(self, price, size, location_score):
        self.price = price
        self.size = size
        self.location_score = location_score

def rank_houses(houses, criteria_weights):
    ranked_houses = sorted(houses, key=lambda x: sum(getattr(x, criteria) * weight for criteria, weight in criteria_weights.items()), reverse=True)
    return ranked_houses

# Sample houses with numeric location scores
houses = [
    House(price=300000, size=2000, location_score=8),
    House(price=250000, size=1800, location_score=6),
    House(price=400000, size=2200, location_score=9),
    House(price=350000, size=1900, location_score=7)
]

# Define criteria weights (higher weight means higher importance)
criteria_weights = {
    'price': 0.5,
    'size': 0.3,
    'location_score': 0.2
}

# Rank houses based on criteria
ranked_houses = rank_houses(houses, criteria_weights)

# Print ranked houses
for i, house in enumerate(ranked_houses):
    print(f"Rank {i+1}: Price=${house.price}, Size={house.size} sqft, Location Score={house.location_score}")
