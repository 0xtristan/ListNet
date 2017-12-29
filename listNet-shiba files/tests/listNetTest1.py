import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
#from components.core import GameLoopEvents

from rank import ListNet
Model = ListNet.ListNet()
#Model.fit(X, y)
