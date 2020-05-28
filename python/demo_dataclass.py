# DEMO
# Python Syntax
# dataclasses Module
# 
# This module shows some example demonstrations of how the `dataclasses` module
# in the Python Standard Library (PSL) can be used for generating data-oriented
# `NamedTuple` instances with built-in features for comparison and equality.
# 
# Arguably, some of these examples don't do much more than eliminate the need
# for explicitly defining the `__init__` method. Also, similar to `NamedTuple`
# instances, there are arguments to be made that these syntax variations may
# or may not benefit readability. The decorator (`@`) declarations simply save
# the amount of code that needs to be typed by the developer, but don't actually
# modify the underlying Object Oriented design. These `dataclass` instances
# could be built from a fully custom class, but would require slightly more code
# and may not have the advantage of certain interpreter optimizations depending
# on how the code is written.
# 
# Most of the benefit of a `dataclass` will be from using the built-in features
# through the `order`, `frozen`, and `eq` flags for the decorator. If you aren't
# using these flags and are writing a lot of custom code, there may not be much
# readability or compatibility benefit to using a `dataclass` instead of writing
# a standard Python class.
#
# References:
# - https://towardsdatascience.com/data-classes-in-python-8d1a09c1294b
# - https://docs.python.org/3/library/dataclasses.html
# 
# @author Tommy Vegetables <leafyrabbet@gmail.com>
# @copyright 2020, TenonGarden Productions
# @license Creative Commons Attribution-NonCommercial 4.0

import math;
import random;
import sys;

crnt_version_info = sys.version_info;
if (
     (crnt_version_info.major >= 3)
     and (crnt_version_info.minor >= 7)
   ):
   print ("> Valid Python Version");
else:
   raise SystemError("Invalid Python | dataclasses module is supported only in Python 3.7 or higher");
# fi

import dataclasses;
print("> dataclasses Module Imported");


@dataclasses.dataclass(eq= True, order= True)
class DataPoint3D:
   length: float = dataclasses.field(init=False); # See NOTE below...
   x: float;
   y: float;
   z: float;

   def __post_init__(self,):
      self.length = (
         math.sqrt(
            (self.x ** 2)
            + (self.y ** 2)
            + (self.z ** 2)
         )
      );
# ssalc


@dataclasses.dataclass(eq= False, order= False)
class ComparableDataPoint3D:
   length: float = dataclasses.field(init=False); # See NOTE below...
   x: float;
   y: float;
   z: float;

   def __post_init__(self,):
      self.length = (
         math.sqrt(
            (self.x ** 2)
            + (self.y ** 2)
            + (self.z ** 2)
         )
      );

   def __gt__(self, other,):
      return (self.length > other.length);
   # fed

   def __ge__(self, other,):
      return (self.length >= other.length);
   # fed

   def __lt__(self, other,):
      return (self.length < other.length);
   # fed

   def __le__(self, other,):
      return (self.length <= other.length);
   # fed

   def __eq__(self, other,):
      return (self.length == other.length);
   # fed
# ssalc


@dataclasses.dataclass(frozen= True) # Immutable after Instantiation
class Ellipse:
   a: float;
   b: float;

   @property
   def area(self,):
      return (self.pi * (self.r ** 2));
   # fed

   @property
   def semimajor(self,):
      return (max(self.a, self.b));
   # fed

   @property
   def semiminor(self,):
      return (min(self.a, self.b));
   # fed

   @property
   def c(self,):
      return (
         math.sqrt(
            (self.semimajor ** 2)
            - (self.semiminor ** 2)
         )
      );
   # fed

   @property
   def f1(self,):
      return (self.c);
   # fed

   @property
   def f2(self,):
      return (-self.c);
   # fed

   @property
   def eccentricity(self,):
      return (self.c / self.semimajor);
   # fed

   @property
   def area(self,):
      return (math.pi * self.semimajor * self.semiminor);
   # fed

   def summary(self,):
      print("  >            Semimajor Axis:", self.semimajor);
      print("  >            Semiminor Axis:", self.semiminor);
      print("  >       Linear Eccentricity:", self.c);
      print("  >              Eccentricity:", self.eccentricity);
      print("  > F1 (along Semimajor Axis):", self.f1);
      print("  > F2 (along Semimajor Axis):", self.f2);
      print("  >                      Area:", self.area);
      print("  >       (Object is Mutable):", (self.__hash__ is None));
      return (None);
   # fed
# ssalc


if (__name__ == "__main__"):

   print("");
   print("> Demos:");
   print("");

   pt_a = DataPoint3D(
            random.random(),
            random.random(),
            random.random(),
         );

   pt_b = DataPoint3D(
            random.random(),
            random.random(),
            random.random(),
         );

   print("Point A:", pt_a);
   print("Point B:", pt_b);
   print("Pt A > Pt B ?:", (pt_a > pt_b));
   print("");

   # NOTE:
   # This is a very fragile example of how to "cheat" and take advantage of some
   # implicit Python features to get a built-in "clever" comparator for free.
   # 
   # The comparison (`pt_a > pt_b`) below only works correctly because the
   # `length` field is declared first, even though it is deferred and defined in
   # the override of the `__post_init__` method. Since the `length` is first
   # named field, it is also the first element in the `NamedTuple`-like
   # instantiation of the `DataPoint3D` instances. This relies on the fact that,
   # by default, the comparators auto-defined when `order= True` will do `tuple`
   # comparisons which go through each tuple element and do short-circuit
   # comparisons. This means that the comparator will "bail-out" when it reaches
   # the first non-trivial comparison.
   #
   # https://stackoverflow.com/questions/5292303/how-does-tuple-comparison-work-in-python
   #
   # So, for example, if we have (l, x, y, z) as the tuples, and two instances
   # are:
   # a = (7.07, 3, 4, 5)
   # b = (5.19, 5, 1, 1)
   #
   # If we do `a > b`, we'd start with:
   # 7.07 > 5.19 ?
   # Which is TRUE, so the comparator will bail-out, since the values are not
   # equivalent and a valid comparison could take place. It doesn't matter that
   # x is smaller in a than b, because the comparison never reaches that value.
   #
   # However, this has a glaring flaw when comparing two objects where the
   # `length` value is equal, but the order of x, y, and z are such that you can
   # get two different answers with two different comparators:
   #
   # a = (3.74, 1, 2, 3)
   # b = (3.74, 3, 1, 2)
   # 
   # a > b: False
   # a < b: True
   # a == b: False
   # 
   # The above results are very misleading because the `length` values are equal
   # but that constitutes a trivial > or < comparison, so the comparator keeps
   # going through the tuple to make the comparisons.
   # 
   # This was demonstrated in the reference article mentioned at the top of this
   # file and was discussed at length here because this is a really misleading
   # "cheat" that should not be trusted.
   # 
   # It is demonstrably safer to simply define your own comparator overrides,
   # which is not only strictly accurate (while the previous approach is not)
   # but is also arguably far more readable and thus less prone to bugs.

   pt_c = DataPoint3D(
            1,
            2,
            3,
         );

   pt_d = DataPoint3D(
            3,
            1,
            2,
         );

   print("> Example of Bad Comparisons:");
   print("Point C:", pt_c);
   print("Point D:", pt_d);
   print("pt_c > pt_d ?:", (pt_c > pt_d));
   print("pt_c < pt_d ?:", (pt_c < pt_d));
   print("pt_c == pt_d ?:", (pt_c == pt_d));
   print("");

   pt_e = ComparableDataPoint3D(
            1,
            2,
            3,
         );

   pt_f = ComparableDataPoint3D(
            3,
            1,
            2,
         );

   print("> Example of Good Comparisons:");
   print("Point E:", pt_e);
   print("Point F:", pt_f);
   print("pt_e > pt_f ?:", (pt_e > pt_f));
   print("pt_e < pt_f ?:", (pt_e < pt_f));
   print("pt_e == pt_f ?:", (pt_e == pt_f));
   print("");

   ell_a = Ellipse(3, 7);
   ell_b = Ellipse(5, 1);
   ell_c = Ellipse(2, 2);

   print("Ellipse A:", ell_a);
   ell_a.summary();
   print("");

   print("Ellipse B:", ell_b);
   ell_b.summary();
   print("");
   
   print("Ellipse C:", ell_c);
   ell_c.summary();
   print("");

# fi
