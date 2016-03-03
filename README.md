# django-simple-wiki
## Installation
DO NOT USE THIS APPLICATION YET. Features are not completed yet.

## Usage
  1. Add 'simple_wiki' in the `INSTALLED_APPS`.
  2. Add the url pattern in the `urls.py`.

    urlpatterns = ['',
        ...
        url(r'^wiki/', include('simple_wiki.urls')),
        ...
    ]

  3. That's all!