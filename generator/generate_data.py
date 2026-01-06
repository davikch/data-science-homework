import random
import numpy as np

from decimal import Decimal

import models
import names


def generate_entry() -> models.Ride:
    return models.Ride(
        client=random.choice(names.GIVEN_NAMES),
        driver=random.choice(names.GIVEN_NAMES),
        price=_calculate_price(
            coefficient=_calculate_coefficient(random.randint(1, 10)),
            urban_distance=min(np.random.normal(5, 2), 0.5),
            nonurban_distance=np.random.normal(5, 3) * 1
            if (random.randint(1, 10) >= 8)
            else 0,
        ),
        destination=f"{random.choice(names.STREETS)}, {random.randint(1,150)}",
    )


def _calculate_price(coefficient: int, urban_distance: float, nonurban_distance: float):
    PRICE_PER_KM = 100
    return Decimal(
        coefficient * PRICE_PER_KM * (urban_distance + 1.5 * nonurban_distance)
    )


def _calculate_coefficient(seed: int) -> Decimal:
    if seed < 7:
        return 1
    else:
        return 3
