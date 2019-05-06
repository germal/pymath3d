# Official Resources

Please use the official repository and issue tracker at https://gitlab.com/morlin/pymath3d

Releases are tagged and published to https://pypi.org/project/math3d/


# Basic Usage

This section illustrates a simple usage scenarios for representing vectors, points, reference systems, as well as some arithmetics and construction of these objects. The terminology is kept simple, and thus is not strictly correct everywhere.

A reference system is a coordinate system located at a distinct point in space, the origo, and having three associated, pair-wise orthonormal directions, the unit basis vector. 

A vector, or a free vector, is a direction and length in Euclidean 3D space. The length of a free vector is invariant under reference system transformation. The unit basis vectors of a reference system are examples of free vectors.

A position vector is a representation of point in space as observed in some reference system. The origo of a reference system is an example of a point.

`math3d` does not, yet, distinguish the representation between free and position vectors. Both are represented by `m3d.Vector` objects.

Let `A` be a reference system and `p` let be a point in space. Then we may represent `p` in `A` by a `m3d.Vector` object, which we symbolize by `Ap`. We may say that `p` has coordinates 1, 2, 0 from the origo of `A` along the ordered unit basis vectors of `A` and write `Ap = m3d.Vector(1, 2, 0)`. Likewise with a free vector, `v`.

Let `B` be another reference system. The relation between `A` and `B` can be expressed by a `m3d.Transform` object. A `m3d.Tranform` is composed by a `m3d.Orientation` and a `m3d.Vector`. These represent the relative orientation and position of the relation between `A` and `B`. Once established, we may use the mnemonic `AB` for symbolizing that the transform represents `B` with reference to `A`. 

The origin of `B` with respect to `A` is represented by the (position) vector part. This position vector is accessible through the property `pos`, as in `AB.pos`.

The orientation part of a transform is not as trivial as the position part. Orientations and rotations can be constructed and represented in many different ways. Some common representations, which are implemented in `math3d`, are 3x3 rotation matrix, unit quaternions, Euler angles, axis-angle, rotation vector. They have various advantages and disadvantages. Rotation matrices are the representation directly used in the `m3d.Orientation` class, which is again used in the `m3d.Transform` class. Unit quaternions are represented with their arithmetics in the `m3d.UnitQuaternions` class. The other representations are generally only managed for constructing of or conversion from `m3d.Orientation` objects. 

Euler angles are intuitive, at least in some situations, and commonly found in many systems with spatial aspects. Euler angles is a family of representations of three sequential rotations around reference system axes. These axes must, for a given Euler angles representation, be specified as either intrinsic (moving) or extrinsic (static) axes. In `math3d` all three rotations must be either intrinsic or extrinsic. Intrinsic rotations are labeled by upper case, e.g. 'YZY', and extrinsic by lower case letters, e.g. 'xyz'. Example: If the orientation of `B` with respect to `A` is obtained by a rotation of `np.pi/2` around the x-axis, then a rotation of `np.pi/4` around the new y-axis, and finally a rotation of `-np.pi/6` around the new z-axis, this is  the resulting orientation could be obtained by `m3d.Orientation.new_euler((np.pi/2, np.pi/4, -np.pi/6), encodint='XYZ')`. On the other hand, if for a given orientation `o`, one wishes to obtain the 'zyx'-angles, these are returned by invoking `o.to_euler('zyx')`.The convention found in http://en.wikipedia.org/wiki/Euler_angles is followed in `math3d`.

In other situations axis-angle or the related rotation-vector representations are more suitable. These are very intuitive, but it is not always easy to determine them. See https://en.wikipedia.org/wiki/Axis%E2%80%93angle_representation#Rotation_vector for a gentle introduction to these representations and their relation. If one wishes to obtain an orientation representing the rotation vector `(np.pi/2, 0, -np.pi)` then this orientation can be constructed by `m3d.Orientation((np.pi/2, 0, -np.pi)`, where the standard constructor is used. If the axis-angle representation `((1, 1, 1), np.pi/2)` is wanted then use `m3d.Orientation.new_axis_angle((1, 1, 1), np.pi/2)`. Conversely, given an orientation, `o`, the rotation-vector is retrieved by the property `o.rotation_vector` and the axis-angle parameters are retrieved by the property `o.axis_angle`.

Quaternions are not intuitive, but are excellent for their arithmetic properties. The are notably great for blending and interpolation. They are out of the scope of this short usage note.
