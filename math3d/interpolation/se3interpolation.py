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
Module implementing the SE(3) interpolator class.
"""

from math3d.transform import Transform
from math3d.interpolation.so3interpolation import SO3Interpolation
from math3d.interpolation.r3interpolation import R3Interpolation

class SE3Interpolation(SO3Interpolation, R3Interpolation):
    """ A class for object representing a linear interpolation in task
    space, SE(3), between two points. Interpolation is done from one
    configuration, trf0, to another, trf1. trf0 and trf1 can be given
    as Transform objects."""

    class Error(Exception):
        """ Exception class."""
        def __init__(self, message):
            self.message = message
        def __repr__(self):
            return self.__class__ + '.Error :' + self.message, None

    def __init__(self, trf0, trf1, shortest=True):
        """ Initialise an SE(3) interpolation from transform 'trf0' to
        transform 'trf1'. If 'shortest' is true, the shortest rotation
        path is chosen, if false, it is indeterminate.""" 
        self._trf0 = trf0
        self._trf1 = trf1
        SO3Interpolation.__init__(self, self._trf0.orient, self._trf1.orient, shortest)
        R3Interpolation.__init__(self, self._trf0.pos, self._trf1.pos)

    def __call__(self, time, checkrange=True):
        """ Class callable method for giving the transform at time
        'time'; in [0,1]."""
        if checkrange:
            time = float(time)
            if time < 0.0 or time > 1.0:
                raise self.Error('"time" must be number in [0,1]. Was %f' % time)
        return Transform(self.orient(time, False), self.pos(time, False))

TaskLinearInterpolation = SE3Interpolation
EuclideanInterpolation = SE3Interpolation

def _test():
    """ Simple test function."""
    global o0, o1, tint, p0, p1
    from math3d.orientation import Orientation
    from math3d.vector import Vector
    from math import pi
    p0 = Vector([0, 1, 0])
    p1=Vector([1, 0, 1])
    o0 = Orientation()
    o0.rotX(pi / 2)
    o1 = Orientation()
    o1.rotZ(pi / 2)
    tint = SE3Interpolation(Transform(o0, p0), Transform(o1, p1))

if __name__ == '__main__':
    import readline
    import rlcompleter
    readline.parse_and_bind("tab: complete")
