"""
Copyright (C) 2011 Morten Lind
mailto: morten@lind.no-ip.org

This file is part of PyMath3D (Math3D for Python).

PyMath3D is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

PyMath3D is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with PyMath3D.  If not, see <http://www.gnu.org/licenses/>.
"""
"""
Module implementing the R^3 interpolator class.
"""

from math3d.vector import Vector

class R3Interpolation(object):
    """ Simple linear position interpolation in R^3."""

    class Error(Exception):
        """ Exception class."""
        def __init__(self, message):
            self.message = message
        def __repr__(self):
            return self.__class__ + '.Error :' + self.message, None

    def __init__(self, p0, p1):
        """ Make a position interpolation between 'p0' and' p1'. 'p0' and 'p1'
        must be suitable data for creation of Vectors."""
        self._p0 = Vector(p0)
        self._p1 = Vector(p1)
        self._displ  = self._p1 - self._p0

    def __call__(self, time, checkrange=True):
        """ Class callable method for directly invoking the pos
        method. 'time' must be given in the interval [0;1]."""
        return self.pos(time, checkrange)

    def pos(self, time, checkrange=True):
        """ Called to get the interpolated position at 'time'."""
        if checkrange:
            time = float(time)
            if time < 0.0 or time > 1.0:
                raise self.Error('"time" must be number in [0,1]. Was %f' % time)
        return self._p0 + time * self._displ
    
PositionInterpolation = R3Interpolation

def _test():
    """ Simple test function."""
    global p0, p1, pint
    p0 = [0, 1, 0]
    p1 = [1, 0, 1]
    pint = R3Interpolation(p0, p1)
    
if __name__ == '__main__':
    import readline
    import rlcompleter
    readline.parse_and_bind("tab: complete")
