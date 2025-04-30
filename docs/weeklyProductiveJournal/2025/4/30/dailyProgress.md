# Day of the Dingo

## Snakety Snake

This entry documents a day of technical refinement involving internal Python imports and data validation using Pydantic models. The focus was on structuring resilient code for clean modularity and strong data typing.

---

### Internal Imports

#### Importing Internal Libraries from Parent Directories

When dealing with complex directory structures, direct imports of internal modules from parent directories can often fail due to Python's default import resolution. To handle this, we can use the built-in `sys` and `os` libraries to modify the `sys.path`, enabling Python to recognize parent paths as valid import sources.

##### Directory Structure Example

```
requirements.txt
|
main.py
|
utils/
|   └── utils.py
|
requests/
    ├── get_requests.py
    └── requests_logic.py
```

##### Example File: `requests_logic.py`

```python
import os
import sys

import get_requests

# Append the utils directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../utils")))

import utils

def get_employee_ids_from_connectors() -> dict[str, dict[str, any]]:
    employee_ids = {}
    connectors = get_requests.get_connectors()

    for connector in connectors:
        employee_id = utils.get_employee_id(connector["employee_data"])
        if employee_id:
            if employee_id not in employee_ids:
                employee_ids[employee_id] = []
            employee_ids[employee_id].append(connector)

    return employee_ids
```

> This method keeps your code modular without needing package reconfiguration or hardcoded paths.

---

### Pydantic Models for Data Validation

#### Embracing Models for Structure and Type Safety

Pydantic models offer a declarative way to enforce schema structure and validate incoming data. This supports a "fail early, fix early" philosophy that ensures clean and predictable data throughout your pipeline.

##### Code Example: `harvest_organs.py`

```python
from typing import Optional
from pydantic import BaseModel

class License(BaseModel):
    state: str
    height: str
    dob: str
    exp: Optional[str] = None
    organ_donor: bool

def harvest_organs(drivers_license: dict[str, any]) -> bool:
    drivers_license = License(**drivers_license)
    return drivers_license.organ_donor

if __name__ == "__main__":
    drivers_license_full_pass = {
        "state": "WA",
        "height": "6'-11\"",
        "dob": "11/11/1911",
        "exp": "11/11/1981",
        "organ_donor": True,
    }

    drivers_license_not_full_pass = {
        "state": "WA",
        "height": "6'-11\"",
        "dob": "11/11/1911",
        "organ_donor": True,
    }

    drivers_license_fail = {
        "stat": "WA",
        "height": "6'-11\"",
        "dob": "11/11/1911",
        "exp": "11/11/1981",
        "organ_donor": True,
    }

    print(harvest_organs(drivers_license=drivers_license_full_pass))
    print(harvest_organs(drivers_license=drivers_license_not_full_pass))
    print(harvest_organs(drivers_license=drivers_license_fail))
```

> The final example (`drivers_license_fail`) will raise a `ValidationError` due to the incorrect key `stat` instead of `state`.

---

![Dingo Dan](./assets/dingoDan.png)
