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
