#!/usr/bin/env python3
__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2020"
__credits__ = ["Jason M. Pittman"]
__license__ = "GPLv3"
__version__ = "0.1.0"
__maintainer__ = "Jason M. Pittman"
__email__ = "jpittman@highpoint.edu"
__status__ = "Development"

import sys
from zettel import Zettel

if __name__ == "__main__":
    try:
        if len(sys.argv) > 1:
            z = Zettel('types.ini', sys.argv[1])
            z.create()
        else:
            z = Zettel('types.ini', None)
    except Exception as e:
        print("Error attempting to create new zettel: " + str(e))


