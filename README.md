# FlatFile Python Library

[![pypi](https://img.shields.io/pypi/v/flatfile.svg)](https://pypi.python.org/pypi/flatfile)
[![fern shield](https://img.shields.io/badge/%F0%9F%8C%BF-SDK%20generated%20by%20Fern-brightgreen)](https://github.com/fern-api/fern)

## Installation

Add this dependency to your project's build file:

```bash
pip install flatfile
# or
poetry add flatfile
```

## Usage

```python
from flatfile.client import FlatFile
import flatfile

flatfile_client = FlatFile(
  token="API_KEY"
)

environment = flatfile_client.environments.create(
  name = 'dev',
  is_prod = False,
  new_spaces_inherit = False,
  guest_authentication = [flatfile.GuestAuthenticationEnum.SHARED_LINK],
);

print(f"Created environment with id {environment.id}");
```

## Async Client

```python
from flatfile.client import AsyncFlatFile
import flatfile

import asyncio

flatfile_client = AsyncFlatFile(
  token="API_KEY"
)

async def create_environment() -> None:
    environment = flatfile_client.environments.create(
      name = 'dev',
      is_prod = False,
      new_spaces_inherit = False,
      guest_authentication = [flatfile.GuestAuthenticationEnum.SHARED_LINK],
    );
    print(f"Created environment with id {environment.id}");

asyncio.run(create_environment())
```

## Timeouts
By default, the client is configured to have a timeout of 60 seconds. You can customize this value at client instantiation. 

```python
from flatfile.client import FlatFile
import flatfile

flatfile_client = FlatFile(
  token="API_KEY",
  timeout=30
)
```

## Handling Exceptions
All exceptions thrown by the SDK will sublcass [flatfile.ApiError](./src/flatfile/core/api_error.py). 

```python
from flatfile.core import ApiError
import flatfile

try:
  flatfile_client.environments.get(id="environment-id")
except flatfile.BadRequestError as e: 
  # handle bad request error
except APIError as e:  
  # handle any api related error
```

Error codes are as followed:

| Status Code | Error Type                 |
| ----------- | -------------------------- |
| 400         | `BadRequestError`          |
| 404         | `NotFoundError`            |

## Beta status

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning the package version to a specific version in your pyproject.toml file. This way, you can install the same version each time without breaking changes unless you are intentionally looking for the latest version.

## Contributing

While we value open-source contributions to this SDK, this library is generated programmatically. Additions made directly to this library would have to be moved over to our generation code, otherwise they would be overwritten upon the next generated release. Feel free to open a PR as a proof of concept, but know that we will not be able to merge it as-is. We suggest opening an issue first to discuss with us!

On the other hand, contributions to the README are always very welcome!
