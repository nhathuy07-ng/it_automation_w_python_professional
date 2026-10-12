#!/bin/bash

sudo turbostat --show PkgWatt,CorWatt,RAMWatt,GFXWatt,SysWatt --quiet -S -i 0.5
