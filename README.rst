Django Secret Key
=================

.. image:: https://travis-ci.org/blinglnav/djangosecretkey.svg?branch=master
   :target: https://travis-ci.org/blinglnav/djangosecretkey

In Django web framework, it has SECRET_KEY variable in settings.py
this variable use to manage credential values like session.

Therefore, SECRET_KEY value have to store outside of settings.py and
use this value to read from file or environment variables.

Install
-------
.. code:: bash

    pip instal djangosecretkey

This project has not any dependencies.
*You cannot download yet*

Usage
-----

Use file to store secret key
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In settings.py

.. code:: python

    import os
    from secret_key import secret_key
    # ...
    SECRET_KEY = secret_key.from_file(os.path.join(BASE_DIR, 'secret_key'))

**If use .from_file() method, you have to secert key file add to .gitignore**

Use env to store secret key
~~~~~~~~~~~~~~~~~~~~~~~~~~~

In settings.py

.. code:: python

    import os
    from secret_key import secret_key
    # ...
    SECRET_KEY = secret_key.from_env('env_name')

default env_name is "DJANGO_SECRET_KEY"

Generate secret key manually
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can also generate secret key manually.

.. code:: python

    import os
    from secret_key import secret_key
    # ...
    SECRET_KEY = secret_key.generate()

But, this method not recommanded.

