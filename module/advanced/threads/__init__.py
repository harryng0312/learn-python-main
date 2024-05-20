# import os
# import sys
# current = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
# sys.path.append(current)
__package__ = "threadsPkg"
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../', '../')))