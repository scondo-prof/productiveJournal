# Day of Understanding the Process of Cranial Computation

## Learning Styles

---

### Determining How the Brain Thinks

#### Terminology-Strong Memory

- This memory process involves easily retaining information through spoken words or written text.
- Commonly found in students excelling in hard sciences such as Physics, Biology, Chemistry, and Mathematics.
- For example, hearing someone introduce themselves as Susan and remembering the name without any additional mental association.

#### Image/Process-Strong Memory

- This memory process is grounded in visual or process-oriented comprehension, relying heavily on diagrams.
- Often observed in engineers who work with infrastructure or process design.
- For example, remembering someone named Susan by mentally linking her to the main character from _Monsters vs. Aliens_.

#### Tactile/Procedural Memory

- Involves understanding and retaining information through hands-on problem solving or full-procedure reading.
- Breaks complex tasks into smaller, manageable components through either physical or conceptual deconstruction.
- For example, remembering the name Susan by responding, "Great to meet you, Susan," and then reinforcing it through conversational repetition.

## Networking

---

### CIDR Blocks

#### Understanding IP Ranges

- CIDR blocks consist of 32 bits.
- Each octet is 8 bits long.
- A `/8` CIDR block means three octets are mutable.

  - Example: `10.0.0.0/8` — the `10` is fixed, while the remaining three octets can range from 0 to 255.

- The total number of IP addresses is calculated using `256^n`, where `n` is the number of mutable octets:
  - `/24` → 1 octet mutable → `256` addresses.
  - `/16` → 2 octets mutable → `65,536` addresses.

## Snakety Snake

---

### Requests with the HTTPX Library

#### Sending Requests with a Body

- When you need to include a request body, it's often best to use `httpx.request` instead of the shorthand methods like `httpx.delete` or `httpx.post`.
  - This approach allows you to pass a Python dictionary as a JSON object via the `json` argument for cleaner, more accurate request bodies.

##### Code Example

```python

def delete_customer_api(customer_number: str, api: str) -> str:
    headers = {"x-api-key": os.getenv("TEST_API_KEY")}
    body = {"customer_number": customer_number, "api": api}

    url = "https://test.execute-api.us-east-1.amazonaws.com/test/customer/API"

    response = httpx.request(method="DELETE", url=url, headers=headers, json=body)

    return response.status_code
```

---

![Cranial Creator](./assets/cranialCreator.png)
