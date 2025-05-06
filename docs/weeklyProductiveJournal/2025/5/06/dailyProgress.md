# Day of Constriction and Restriction

## Snakety Snake

### Code Practices

#### PEP 484

A large gripe that I have with PYYYYTHHHONNNN would be the ability to be lack luster in declaring items being worked with. But fret not, there are ways to help you out as seen with Pydantic Modeling in the entry April the 30th 2025. Like that one can do what is called Variable Annotation. Introduced in PEP 484, allows one to set the expected type of a variable. This is similar to setting expected types for function parameters and return types. Very helpful and should be utilized.

##### Code Example:

```Python

def throw_rocks(at_car: bool, how_hard: int, scapegoat: str) -> dict[str, any]:

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
        status: str = "Cool as Cucumber"

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
