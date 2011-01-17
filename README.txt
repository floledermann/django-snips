django-snips
============

A very simple Django application to be used for defining text blocks or pages on a website. It is called django-snips to avoid confusion with the `django snippets`_ website, internally the package and models are called *snippets*.

It is similar to the ``django.contrib.flatpages`` or flatblocks_, adding the following features:

* Each snippet can have a single file attached to it - this can be used for images and other media.
* A snippet can have child snippets. This and the above allows you to create galleries.
* A snippet can be assigned to categories. You can create menus or other lists with all snippets from a category.
* A snippet can have a language associated with it. You can easily select snippets matching the visitor's language.

.. _`django snippets`: http://djangosnippets.org/
.. _flatblocks: https://github.com/zerok/django-flatblocks
