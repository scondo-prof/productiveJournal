# Day of Constriction and Restriction

## Snakety Snake

### Code Practices

#### PEP 484

One of my biggest gripes with PYYYYTHHHONNNN is how loose it can feel when you don’t clearly declare the types you’re working with. But fear not, `Pydantic` modeling (see April 30th, 2025) demonstrates one way to add strong typing. _Parameter_ and _Return Type_ hints for functions are also introduced by the same `PEP`, namely `PEP 484`, which lays the foundation not only for typing function parameters and return values but also for _Variable Annotation_. _Variable Annotation_ further extends that clarity by letting you specify the expected type of any variable. Think of it as taking the explicitness of your function signatures and applying it to all your local variables. It’s simple, immensely helpful, and should be part of every Pythonista’s toolbox.

##### Code Example

```python

def throw_rocks(at_car: bool, how_hard: int, scapegoat: str) -> dict[str, any]:
    """
    Launch some rocks and see what chaos unfolds.

    You’re armed with stones, a target (maybe a car?), and a cunning plan to pass the blame.

    Args:
        at_car (bool): True to aim at a car, False for general mischief.
        how_hard (int): Strength of your throw (0 = gentle tap, 100 = meteor strike).
        scapegoat (str): Name of your unwitting fall guy for this stunt.

    Returns:
        dict[str, any]: A playful summary of the aftermath including:
            - in_trouble (bool): Whether you’ve earned a scolding or worse.
            - money_owed (int): Currency you owe for any broken windows.
            - status (str): Your rock‑throwing persona (e.g., “Pro Rock Athlete”).
    """

    if how_hard > 12:
        in_trouble: bool = True
    else:
        in_trouble: bool = False

    if at_car:
        money_owed: int = 17
    else:
        money_owed: int = 0

    if scapegoat == "brittany":
        in_trouble = False
        status: str = "Cool as a Cucumber"
    elif scapegoat == "tammy":
        in_trouble = True
        status: str = "Bottom Feeder"
    else:
        status: str = "Pro Rock Athlete"

    return {"in_trouble": in_trouble, "money_owed": money_owed, "status": status}

```

Notice how every variable carries its intended type right alongside its assignment. That extra clarity helps catch bugs early and makes your code more self‑documenting.

`Why do snakes read self-improvement books?`

`They’re trying to shed their old skin.`

## Tickling the Ivories, Not the Ovaries

### Song Practice

#### II by Old Gray

Continued to strive on learning the key progression for this song. My tempo is a bit off, but the chords are coming along

#### I by Old Gray

It is at that point where this song is played for fun when the mood strikes. Tonight the mood striked with an open window and rainfall

## Strokin not Pokin

### Stroke Practice

#### Genie in the Bottle

- Utilized a water bottle to practice stroking my pool stick. I noticed a wobble in my upper arm in the draw back which was corrected by elevating my elbow a bit higher and a touch more in.

- My pattern of hitting a ball from hence forth will follow thus,

1. Assess angle of object ball
2. Get down into position and listen to body
3. If body indicates angle is off, get up and start over
4. Get down into position placing the tip of the cue roughly the length of a quarter away from the cue ball
5. Draw the stick back full stroke extension and bring back to intended spot on the cueball to hit
6. Re Do stroke but this time hit cue ball
7. Follow Through in exagerated mannor

---

![Monkai Of Typing](./assets/monkaiOfTyping.png)
