# -*- coding: utf-8 -*-
"""Project metadata

Information describing the project.
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

# The package name, which is also the "UNIX name" for the project.
from future import standard_library
standard_library.install_aliases()
from builtins import *
package = 'oktaauth'
project = "Okta CLI authentication"
project_no_spaces = project.replace(' ', '')
version = '0.2'
description = 'Authenticates from the CLI'
authors = ['Peter Gillard-Moss']
authors_string = ', '.join(authors)
emails = ['pgillard@thoughtworks.com']
license = 'Apache 2.0'
copyright = '2015 Thoughtworks Inc'
url = 'https://www.thoughtworks.com/'
