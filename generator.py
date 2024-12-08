import logging

import random
import randomname

from tqdm import tqdm

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


def main():
    # Set up groups of appropriate word combinations
    foods = ("nn/seasonings", "nn/condiments", "nn/fast_food", "nn/food", "nn/fruit")
    animals = ("nn/apex_predators", "nn/fish", "nn/birds", "nn/cats", "nn/dogs")
    # animals = ("nn/apex_predators", "nn/fish", "nn/birds", "nn/cats", "nn/dogs", "nn/snakes", "nn/monkeys")  # Pending update of randomname
    groups = [
        (("adj/size", "adj/speed"), "adj/taste", foods),
        (("adj/size", "adj/speed"), "adj/colors", animals),
        (("adj/size", "adj/speed"), "adj/emotions", "nn/plants"),
        (("adj/size", "adj/speed"), "adj/character", "nn/cheese"),
    ]

    n = 1000000
    names = [None] * n  # Preallocate memory for names

    logger.info(f"Generating names ({n} iterations)...")
    for i in tqdm(range(n)):
        # Select a random group
        idx = random.randrange(0, len(groups))
        group = groups[idx]
        logger.debug(f"Using group {idx}: {group}")

        # Generate a name
        name = randomname.generate(*group, sep="-")
        names[i] = name
        logger.debug(f"Generated name: {name}")

    # Extract all unique names
    names = list(set(names))
    logger.info(f"Generated {len(names)} unique names.")

    with open("names.txt", "w") as f:
        # Write all names to a file
        f.write("\n".join(names))

    logger.info("Examples: \n" + "\n".join([f"{name}" for name in names[:25]]))


if __name__ == "__main__":
    main()
