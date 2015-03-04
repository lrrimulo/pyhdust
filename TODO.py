#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Modified by D. Moser in 2015-03-02

""" TODOs

| GENERAL
|   -pip install for pyhdust
|   -Transparent legend-box on the graphs
|   -Change scipy interpolate with numpy.interp (hdt.doFilterConv, others...)
|   *Define unique 'Planejamento_LNA' reference (targets [coordinates], P and Ph0
|   [mags.], nights observed vs. bad weather, etc.)
|   *Define flux units at SED2 file read
|   -Standardization at CGS/SI units
|   -Finish help docs+translations to English
|   *Define `path` policy
|   -Replace if os.path.exists+os...mkdir with phc.outfld
|   -Remove *ra2deg* variable
|   -Remove *rmext*. Replace with os.* tool (Bebnarski)
|   -Remove *outfold* from spectools
|   -Check *makeInpJob* `scrid` variable

| MAIN
|   -update obs_calcs (spherical triangles)

| PHC
|   -update phc.rot_stars (Beta(W))

| SPEC
|   -Implement Kurucz flux unity correction

| INPUT
|   -Implement Mdot11 option in makeDiskGrid

| BEATLAS
|   -Create XDR BeAtlas, rotine correlations emcee (+maps)
|   -Update beatlas.py stellar parameters

"""

import pyhdust as hdt
print("# pyhdust")
print("\n".join([x for x in dir(hdt) if x[0] != "_"]))

import pyhdust.beatlas as bat
print("# pyhdust.beatlas")
print("\n".join([x for x in dir(bat) if x[0] != "_"]))

import pyhdust.input as inp
print("# pyhdust.input")
print("\n".join([x for x in dir(inp) if x[0] != "_"]))

import pyhdust.interftools as intt
print("# pyhdust.interftools")
print("\n".join([x for x in dir(intt) if x[0] != "_"]))

import pyhdust.poltools as polt
print("# pyhdust.poltools")
print("\n".join([x for x in dir(polt) if x[0] != "_"]))

import pyhdust.phc as phc
print("# pyhdust.phc")
print("\n".join([x for x in dir(phc) if x[0] != "_"]))

import pyhdust.singscat as sst
print("# pyhdust.singscat")
print("\n".join([x for x in dir(sst) if x[0] != "_"]))

import pyhdust.spectools as spt
print("# pyhdust.spectools")
print("\n".join([x for x in dir(spt) if x[0] != "_"]))
