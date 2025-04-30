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
