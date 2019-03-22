# Description

A simple example project of using requests, attrs and cattrs to prevent yourself
from using JSON schema to validate response from server. `attrs` is used to
describe `Type` classes.

I also override base `requests.request` method in order to:
- use authorization token
- unstructure given `Type` classes, when they came in `data` parameter
- changed `Response` class - to use only necessary data

Tests a written for this REST API: https://restful-booker.herokuapp.com

# Run

```bash
pip install -r requirements.txt
pytest ./tests
```