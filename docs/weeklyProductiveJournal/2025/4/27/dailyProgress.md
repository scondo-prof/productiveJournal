# Day of Organization, and Data Reckoning

## productiveJournal Repo

### Directory Structure

#### DND Notes Integration

- Created new journal entry process for dnd journals from the perspective of the charcter in the campaign

- Entries are located with the same directory structure as weeklyProductiveJournal entries, but reside in the dndJournal Directory

---

### GitHub Pages Integration

#### Cluttered Integration Structure

- The repo was starting to get populated, and it needed an ability to organize beyond a single readme.md

- Solution was to integrate a CI/CD pipeline I have used before to create repo docs utilizing GitHub Pages

---

#### GitHub Pages Layout

- Went through many interations of the GitHub Pages Layout, and landed on the current structure that is located in the mkdocs.yaml file in the root of this repo

## theToolKit Repo

### s3_upload.py

#### def upload_s3_obj(file_name: str, s3_path: str) -> str:

- Created a generic funciton to upload a singular object.

- This function will utilize transfer acceleration if the bucket has it

- It also utilizes a intentionally constructed multi part upload to maximize efficiency for projects with small and large files

  - This was done with the mindset of projects that have both project files such as Adobe Premiere Working Files, and their Assets ranging from Large Video Files, to Small Picture Files

#### def bulk_s3_upload(dir_path: str) -> list[str]:

- Under construction is a function that will be given a directory, and it will upload every file/directory (starting at the given dir_path) into s3

---

![Master of Creation and Organization](./assets/masterOfCreationAndOrganization.png)
