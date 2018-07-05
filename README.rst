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


Author
======

Jacopo Notarstefano (`@Jaconotar`_)

.. _`@Jaconotar`: https://twitter.com/Jaconotar


License
=======

MIT
