# Day of Organization and Data Reckoning

## productiveJournal Repository

---

### Directory Structure Enhancements

#### DND Journal Integration

- Created a new journal entry process for DND sessions, written from the perspective of the character in the campaign.
- Entries follow the same directory structure as the `weeklyProductiveJournal` but are organized within the `dndJournal` directory.

---

### GitHub Pages Integration

#### Managing Clutter

- The repository was becoming populated with various Markdown files, requiring a more structured organizational system beyond a single `README.md`.
- Integrated a CI/CD pipeline to build repository documentation utilizing GitHub Pages for better navigation and management.

#### GitHub Pages Layout

- Iterated through multiple layout structures for GitHub Pages.
- Finalized the current layout, configured in the `mkdocs.yaml` file located at the root of this repository.

## [theToolKit Repository](https://github.com/scondo-prof/theToolKit)

---

### s3_upload.py Enhancements

#### `upload_s3_obj(file_name: str, s3_path: str) -> str`

- Developed a generic function to upload a single object to S3.
- The function leverages transfer acceleration when available on the target bucket.
- Implements an intentionally constructed multi-part upload process to optimize efficiency for both small and large files.
  - Designed with workflows in mind that involve varied asset sizes, such as Adobe Premiere project files (small) and large video files (large).

#### `bulk_s3_upload(dir_path: str) -> list[str]`

- Began constructing a function to recursively upload all files and directories starting from the provided `dir_path` into S3.
- This function is still under active development.

---

![Master of Creation and Organization](./assets/masterOfCreationAndOrganization.png)
