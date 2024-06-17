# -*- coding: utf-8 -*-
# Licensed under a 3-clause BSD style license - see LICENSE.rst

# This file was automatically generated from ply. To re-generate this file,
# remove it from this folder, then build astropy and run the tests in-place:
#
#   python setup.py build_ext --inplace
#   pytest astropy/coordinates/angles
#
# You can then commit the changes to this file.


# angle_parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'COLON DEGREE EASTWEST HOUR MINUTE NORTHSOUTH SECOND SIGN SIMPLE_UNIT UFLOAT UINT\n            angle : sign hms eastwest\n                  | sign dms dir\n                  | sign arcsecond dir\n                  | sign arcminute dir\n                  | sign simple dir\n            \n            sign : SIGN\n                 |\n            \n            eastwest : EASTWEST\n                     |\n            \n            dir : EASTWEST\n                | NORTHSOUTH\n                |\n            \n            ufloat : UFLOAT\n                   | UINT\n            \n            colon : UINT COLON ufloat\n                  | UINT COLON UINT COLON ufloat\n            \n            spaced : UINT ufloat\n                   | UINT UINT ufloat\n            \n            generic : colon\n                    | spaced\n                    | ufloat\n            \n            hms : UINT HOUR\n                | UINT HOUR ufloat\n                | UINT HOUR UINT MINUTE\n                | UINT HOUR UFLOAT MINUTE\n                | UINT HOUR UINT MINUTE ufloat\n                | UINT HOUR UINT MINUTE ufloat SECOND\n                | generic HOUR\n            \n            dms : UINT DEGREE\n                | UINT DEGREE ufloat\n                | UINT DEGREE UINT MINUTE\n                | UINT DEGREE UFLOAT MINUTE\n                | UINT DEGREE UINT MINUTE ufloat\n                | UINT DEGREE UINT MINUTE ufloat SECOND\n                | generic DEGREE\n            \n            simple : generic\n                   | generic SIMPLE_UNIT\n            \n            arcsecond : generic SECOND\n            \n            arcminute : generic MINUTE\n            '
    
_lr_action_items = {'SIGN':([0,],[3,]),'UINT':([0,2,3,9,23,24,26,27,43,45,47,],[-7,9,-6,23,33,35,38,41,33,33,33,]),'UFLOAT':([0,2,3,9,23,24,26,27,43,45,47,],[-7,11,-6,11,11,37,40,11,11,11,11,]),'$end':([1,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,48,49,50,51,52,],[0,-9,-12,-12,-12,-12,-14,-21,-13,-36,-19,-20,-1,-8,-2,-10,-11,-3,-4,-5,-14,-22,-17,-29,-28,-35,-38,-39,-37,-14,-18,-14,-23,-13,-14,-30,-13,-14,-15,-24,-25,-31,-32,-26,-33,-16,-27,-34,]),'EASTWEST':([4,5,6,7,8,9,10,11,12,13,14,23,24,25,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,48,49,50,51,52,],[16,18,18,18,18,-14,-21,-13,-36,-19,-20,-14,-22,-17,-29,-28,-35,-38,-39,-37,-14,-18,-14,-23,-13,-14,-30,-13,-14,-15,-24,-25,-31,-32,-26,-33,-16,-27,-34,]),'NORTHSOUTH':([5,6,7,8,9,10,11,12,13,14,23,25,26,29,30,31,32,33,34,38,39,40,41,42,45,46,49,50,52,],[19,19,19,19,-14,-21,-13,-36,-19,-20,-14,-17,-29,-35,-38,-39,-37,-14,-18,-14,-30,-13,-14,-15,-31,-32,-33,-16,-34,]),'HOUR':([9,10,11,12,13,14,23,25,33,34,41,42,50,],[24,-21,-13,28,-19,-20,-14,-17,-14,-18,-14,-15,-16,]),'DEGREE':([9,10,11,12,13,14,23,25,33,34,41,42,50,],[26,-21,-13,29,-19,-20,-14,-17,-14,-18,-14,-15,-16,]),'COLON':([9,41,],[27,47,]),'SECOND':([9,10,11,12,13,14,23,25,33,34,41,42,48,49,50,],[-14,-21,-13,30,-19,-20,-14,-17,-14,-18,-14,-15,51,52,-16,]),'MINUTE':([9,10,11,12,13,14,23,25,33,34,35,37,38,40,41,42,50,],[-14,-21,-13,31,-19,-20,-14,-17,-14,-18,43,44,45,46,-14,-15,-16,]),'SIMPLE_UNIT':([9,10,11,12,13,14,23,25,33,34,41,42,50,],[-14,-21,-13,32,-19,-20,-14,-17,-14,-18,-14,-15,-16,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'angle':([0,],[1,]),'sign':([0,],[2,]),'hms':([2,],[4,]),'dms':([2,],[5,]),'arcsecond':([2,],[6,]),'arcminute':([2,],[7,]),'simple':([2,],[8,]),'ufloat':([2,9,23,24,26,27,43,45,47,],[10,25,34,36,39,42,48,49,50,]),'generic':([2,],[12,]),'colon':([2,],[13,]),'spaced':([2,],[14,]),'eastwest':([4,],[15,]),'dir':([5,6,7,8,],[17,20,21,22,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> angle","S'",1,None,None,None),
  ('angle -> sign hms eastwest','angle',3,'p_angle','formats.py',162),
  ('angle -> sign dms dir','angle',3,'p_angle','formats.py',163),
  ('angle -> sign arcsecond dir','angle',3,'p_angle','formats.py',164),
  ('angle -> sign arcminute dir','angle',3,'p_angle','formats.py',165),
  ('angle -> sign simple dir','angle',3,'p_angle','formats.py',166),
  ('sign -> SIGN','sign',1,'p_sign','formats.py',177),
  ('sign -> <empty>','sign',0,'p_sign','formats.py',178),
  ('eastwest -> EASTWEST','eastwest',1,'p_eastwest','formats.py',187),
  ('eastwest -> <empty>','eastwest',0,'p_eastwest','formats.py',188),
  ('dir -> EASTWEST','dir',1,'p_dir','formats.py',197),
  ('dir -> NORTHSOUTH','dir',1,'p_dir','formats.py',198),
  ('dir -> <empty>','dir',0,'p_dir','formats.py',199),
  ('ufloat -> UFLOAT','ufloat',1,'p_ufloat','formats.py',208),
  ('ufloat -> UINT','ufloat',1,'p_ufloat','formats.py',209),
  ('colon -> UINT COLON ufloat','colon',3,'p_colon','formats.py',215),
  ('colon -> UINT COLON UINT COLON ufloat','colon',5,'p_colon','formats.py',216),
  ('spaced -> UINT ufloat','spaced',2,'p_spaced','formats.py',225),
  ('spaced -> UINT UINT ufloat','spaced',3,'p_spaced','formats.py',226),
  ('generic -> colon','generic',1,'p_generic','formats.py',235),
  ('generic -> spaced','generic',1,'p_generic','formats.py',236),
  ('generic -> ufloat','generic',1,'p_generic','formats.py',237),
  ('hms -> UINT HOUR','hms',2,'p_hms','formats.py',243),
  ('hms -> UINT HOUR ufloat','hms',3,'p_hms','formats.py',244),
  ('hms -> UINT HOUR UINT MINUTE','hms',4,'p_hms','formats.py',245),
  ('hms -> UINT HOUR UFLOAT MINUTE','hms',4,'p_hms','formats.py',246),
  ('hms -> UINT HOUR UINT MINUTE ufloat','hms',5,'p_hms','formats.py',247),
  ('hms -> UINT HOUR UINT MINUTE ufloat SECOND','hms',6,'p_hms','formats.py',248),
  ('hms -> generic HOUR','hms',2,'p_hms','formats.py',249),
  ('dms -> UINT DEGREE','dms',2,'p_dms','formats.py',260),
  ('dms -> UINT DEGREE ufloat','dms',3,'p_dms','formats.py',261),
  ('dms -> UINT DEGREE UINT MINUTE','dms',4,'p_dms','formats.py',262),
  ('dms -> UINT DEGREE UFLOAT MINUTE','dms',4,'p_dms','formats.py',263),
  ('dms -> UINT DEGREE UINT MINUTE ufloat','dms',5,'p_dms','formats.py',264),
  ('dms -> UINT DEGREE UINT MINUTE ufloat SECOND','dms',6,'p_dms','formats.py',265),
  ('dms -> generic DEGREE','dms',2,'p_dms','formats.py',266),
  ('simple -> generic','simple',1,'p_simple','formats.py',277),
  ('simple -> generic SIMPLE_UNIT','simple',2,'p_simple','formats.py',278),
  ('arcsecond -> generic SECOND','arcsecond',2,'p_arcsecond','formats.py',287),
  ('arcminute -> generic MINUTE','arcminute',2,'p_arcminute','formats.py',293),
]
