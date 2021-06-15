# basylic-python-client
Class to access Basylic's API

# Summary

Basylic is a SaaS solution that allows you to perform automatic extraction of information on various documents, and to perform anti-fraud controls. It is developed by Etaonis. This module provides a python interface for accessing the API.

# Installation

This module is available on PyPI, so you can install it with with `pip`:

```>>> pip install basylic```

Alternatively, you can access the source code on GitHub:

* https://github.com/basylic-team/basylic-python-client

# Basic usage

To access the API, you must provide a token. We recommend you to store the token in an environment variable called `BASYLIC_ACCESS_TOKEN`. 

```
from basylic import Basylic
basylic = Basylic()
```

If you token is stored in a non-standard location, you can specify it with the `token=` argument during class instantiation:

```
from basylic import Basylic
basylic = Basylic(token=...)
```

2. The minimal set of arguments to use the document checker are `document_type` and `file_path`:
>>> basylic.check_document(file_path = "corinne-berthier-recto-verso.pdf", document_type="french_ids")

* The `file_path` argument is self-evident. 
* `document_type` is a string that specifies which Basylic sub-service will be used.

Possible values for `document_type` are: `'french_ids'`, `'rib'`, `'ri'`, `'avis-imposition'`...

With those arguments specified, `check_document` returns a comprehensive JSON document with document compliance check and OCR transcription, among other information.

3. It is recommended to include data about applicants. Data extracted by Basylic's OCR will be crosschecked with those data.
>>> applicant_information = {"applicant_0": {"name": "BERTHIER"}}
>>> basylic.check_document(file_path="corinne-berthier-recto-verso.odf", document_type="french_ids")

4. Various arguments could be passed as kwargs. For example:
a. `save_report=True` will save the result of your request to your user space on Basylic's Portal.
b. `with_image=True` will return a base64 image for each recognised document. This is handy if you wish to print the input image for comparison.
c. `reference='abc...'` will add this key-value pair to the API output. If this key is specified, the report will appear under this name in Basylic's Portal.

