# This file is part of the Frescobaldi project, http://www.frescobaldi.org/
#
# Copyright (c) 2013 - 2013 by Wilbert Berendsen
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
# See http://www.gnu.org/licenses/ for more information.

"""
Reading the Frescobaldi User Manual.
"""

from __future__ import unicode_literals

import os
import re


def split_document(s):
    """Split the help page text and its #SUBDOCS and other headers.
    
    Returns a tuple consisting of the document text and a dictionary
    representing the #-named blocks; every value is the content of the block
    with a list of lines for every block.
    
    """
    l = re.split(r'^#([A-Z]+)\s*$', s, flags = re.MULTILINE)
    i = iter(l[1:])
    return l[0], dict((name, split_lines(value)) for name, value in zip(i, i))

def split_lines(s):
    """Split s in lines and strip() all lines. Returns a list."""
    return list(line.strip() for line in s.strip().splitlines())

def document(filename):
    if not filename.endswith('.md'):
        filename += '.md'
    if not os.path.isabs(filename):
        from . import __path__
        filename = os.path.join(__path__[0], filename)
    with open(filename, 'rb') as f:
        return split_document(f.read().decode('utf-8'))


