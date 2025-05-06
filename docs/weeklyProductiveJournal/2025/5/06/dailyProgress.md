# Day of Constriction and Restriction

## Snakety Snake

### Code Practices

#### PEP 484

One of my biggest gripes with PYYYYTHHHONNNN is how loose it can feel when you don’t clearly declare the types you’re working with. But fear not, `Pydantic` modeling (see April 30th, 2025) demonstrates one way to add strong typing. _Parameter_ and _Return Type_ hints for functions are also introduced by the same `PEP`, namely `PEP 484`, which lays the foundation not only for typing function parameters and return values but also for _Variable Annotation_. _Variable Annotation_ further extends that clarity by letting you specify the expected type of any variable. Think of it as taking the explicitness of your function signatures and applying it to all your local variables. It’s simple, immensely helpful, and should be part of every Pythonista’s toolbox.

##### Code Example

```python

def throw_rocks(at_car: bool, how_hard: int, scapegoat: str) -> dict[str, any]:
    # Determine if you’re in trouble based on how hard you throw
    if how_hard > 12:
        in_trouble: bool = True
    else:
        in_trouble: bool = False

    # Calculate money owed for hitting the car
    if at_car:
        money_owed: int = 17
    else:
        money_owed: int = 0

    # Adjust status if you blame someone else
    if scapegoat == "brittany":
        in_trouble = False
        status: str = "Cool as a Cucumber"
    elif scapegoat == "tammy":
        in_trouble = True
        status: str = "Bottom Feeder"
    else:
        status: str = "Pro Rock Athlete"

    return {
        "in_trouble": in_trouble,
        "money_owed": money_owed,
        "status": status
    }
```

Notice how every variable carries its intended type right alongside its assignment. That extra clarity helps catch bugs early and makes your code more self‑documenting.

`Why do snakes read self-improvement books?`

`They’re trying to shed their old skin.`
