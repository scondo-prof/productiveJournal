# Day of the Dingo

## Snakety Snake

---

### Internal Imports

#### Importing Internal Lib from Up Directory

- In some cases, the directory structure forces an import of an internal file that exists up directory. If one was to try to directly import it, there would be an error due to directory resolution. A solution is to utilize the general sys import to fix your jazz.

##### Directory Structure

```
requirements.txt
|
|
main.py
|
|
utils
|   |
|   |
|   utils.py
|
|
requests
       |
       |
       get_requests.py
       |
       |
       requests_logic.py
```

##### Code Example File is requests_logic.py

```python
import os
import sys

import get_requests

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../utils")))

import utils

def get_employee_ids_from_connectors() -> dict[str, dict[str, any]]:
       employee_ids = {}
       connectors = get_requests.get_connectors()

       for connector in connectors:
              employee_id = utils.get_employee_id(connector["employee_data"])
              if employee_id:
                     if not employee_id in connector_ids:
                            employee_ids[employee_id] = []
                     employee_ids[employee_id].append(connector)

       return employee_ids


```

---

### Pydantic

#### Utilizing Models

- Pydantic Models are a fantastic way to ensure your data has the fields you expect, and are typed with the correct datatype

- This helps solidify data pipelines and ensure a fail early fix early mentality when malstructured data is passed

##### Code Example

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

    if drivers_license.organ_donor:
        return True
    else:
        return False


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

---

![Dingo Dan](./assets/dingoDan.png)
