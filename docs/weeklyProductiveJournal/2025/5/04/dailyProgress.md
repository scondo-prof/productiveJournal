# Day of Coding and Cranking that Soulja Boy

## [theToolKit Repository](https://github.com/scondo-prof/theToolKit)

---

### upload_s3_obj() && bulk_s3_upload()

#### aiboto3 Implimentation

Jamming to niminio [Creek Album](https://open.spotify.com/album/4wFyqyU8erSQITJyyoUOhk?si=zZrugydLRbeWFs3XlQWiAw) while diving into the 1s and 0s

##### Corrected Syntax

Utilized aiboto3.Session in conjunction with async, then turned the session into an s3 client named s3_client. From there all generic boto3 calls worked asynchronusly as intended

Example Run

```
(tools-env) PS C:\Users\scott\Documents\github\tools\tools\videographyTools> python .\s3_upload.py
Files Gathered and Ready For Upload
---
Gathered File: C:\Users\scott\Documents\github\tools\tools\videographyTools\s3_upload.py
To be Uploaded To
S3 Key: test/s3_upload.py
About to upload file with S3 key: test/s3_upload.py
Inside Catch
session made
---
Gathered File: C:\Users\scott\Documents\github\tools\tools\videographyTools\youtube_to_mp3.py
To be Uploaded To
S3 Key: test/youtube_to_mp3.py
About to upload file with S3 key: test/youtube_to_mp3.py
Inside Catch
session made
---
Gathered File: C:\Users\scott\Documents\github\tools\tools\videographyTools\__init__.py
To be Uploaded To
S3 Key: test/__init__.py
About to upload file with S3 key: test/__init__.py
Inside Catch
session made
---
Gathered File: C:\Users\scott\Documents\github\tools\tools\videographyTools\videos\wow.txt
To be Uploaded To
S3 Key: test/videos/wow.txt
About to upload file with S3 key: test/videos/wow.txt
Inside Catch
session made
Successfully Uploaded: test/__init__.py
Successfully Uploaded: test/videos/wow.txt
Successfully Uploaded: test/youtube_to_mp3.py
Successfully Uploaded: test/s3_upload.py
```

---

#### PR For Code Implementation

[PR](https://github.com/scondo-prof/theToolKit/pull/12)

#### The Pivot from aiboto3 -> boto3

[Commit](https://github.com/scondo-prof/theToolKit/commit/87744c454162ff30969cf9fdf9814e7a6ee5c616)
