================
 GitHub-Compose
================

.. image:: https://travis-ci.org/jacquerie/github-compose.svg?branch=master
    :target: https://travis-ci.org/jacquerie/github-compose

.. image:: https://coveralls.io/repos/github/jacquerie/github-compose/badge.svg?branch=master
    :target: https://coveralls.io/github/jacquerie/github-compose?branch=master


About
=====

Orchestrate your GitHub repositories like ``docker-compose`` orchestrates your
Docker containers. Inspired by `metainvenio`_ by `@inveniosoftware`_.

.. _`metainvenio`: https://github.com/inveniosoftware/metainvenio
.. _`@inveniosoftware`: https://github.com/inveniosoftware


Install
=======

``github-compose`` is on PyPI, so all you have to do is:

.. code-block:: console

    $ pip install github-compose


Usage
=====

Currently ``github-compose`` implements one subcommand:

.. code-block:: console

    $ github-compose update

This will update the configuration of your repositories on GitHub so that it
matches what is described in a file called (by default) ``github-compose.yml``.
Here's an example of such a file:

.. code-block:: yaml

    orgs:
      foo-org:
        repos:
          bar-repo:
            description: "Description of the bar repo."

Running the ``update`` command on this file will update the description of the
``bar-repo`` of the ``foo-org`` to be "Description of the bar repo."
Here's another example:

.. code-block:: yaml

    orgs:
      foo-org:
        repos:
          bar-repo:
            description: "Description of the bar repo."
          baz-repo:
            description: "Description of the baz repo."

Suppose that the ``foo-org`` currently has only the ``bar-repo``: running the
``update`` command with this file will create an empty ``baz-repo`` whose
description is "Description of the baz repo."


Author
======

Jacopo Notarstefano (`@Jaconotar`_)

.. _`@Jaconotar`: https://twitter.com/Jaconotar


License
=======

MIT
