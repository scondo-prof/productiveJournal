# Day of Constriction and Restriction

## Snakety Snake

### Code Practices

#### PEP 484

One of my biggest gripes with PYYYYTHHHONNNN is how loose it can feel when you don’t clearly declare the types you’re working with. But fear not, `Pydantic` modeling (see April 30th, 2025) demonstrates one way to add strong typing. _Parameter_ and _Return Type_ hints for functions are also introduced by the same `PEP`, namely `PEP 484`, which lays the foundation not only for typing function parameters and return values but also for _Variable Annotation_. _Variable Annotation_ further extends that clarity by letting you specify the expected type of any variable. Think of it as taking the explicitness of your function signatures and applying it to all your local variables.

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

I continued working on the key progression for this song. My tempo is still a bit off, but the chord transitions are improving.

#### I by Old Gray

This piece is reserved for those moments when I simply want to play for enjoyment. Tonight, the open window and gentle rainfall created the perfect atmosphere to let it flow.

## Feelin the Felt

### Stroke Practice

#### Genie in a Bottle

- I used a water bottle to practice my pool cue stroke. During the back half of the stroke, I noticed a wobble in my upper arm, which I corrected by raising my elbow slightly and adjusting its angle.

- Moving forward, my cue stroke will follow these steps:

  1. Assess the angle of the object ball.
  2. Lower into position and check alignment with body.
  3. If body signals the angle is off, stand up and realign.
  4. Lower into position again, placing the cue tip about a quarter’s length from the cue ball.
  5. Draw the cue back in a full stroke, then pause at the intended contact point.
  6. Execute the stroke, striking the cue ball.
  7. Finish with an exaggerated follow-through.

`This bottle training is invaluable for practicing the same stroke length at varying speeds. Each hit maintains identical mechanics but differs only in velocity, helping you adapt to the feel of different cloth.`

---

![Monkai Of Typing](./assets/monkaiOfTyping.png)
