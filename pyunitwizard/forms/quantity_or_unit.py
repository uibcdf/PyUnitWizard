# TypeVars to represent unit, quantities and arraylike objects

from typing import TypeVar
import numpy as np
import openmm.unit as openmm_unit
import pint

ArrayLike = TypeVar("ArrayLike",
                    tuple,
                    list,
                    np.ndarray)

QuantityLike = TypeVar("QuantityLike", 
                    str,
                    openmm_unit.Quantity,
                    pint.Quantity,  
                    )

UnitLike = TypeVar("UnitLike",
                str,
                openmm_unit.Unit,
                pint.Unit,
                )

QuantityOrUnit = TypeVar("QuantityOrUnit", 
                str,
                openmm_unit.Unit,
                pint.Unit,
                openmm_unit.Quantity,
                pint.Quantity)