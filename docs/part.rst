Part
====

''''''
Format
''''''

part *label*

''''''''
Abstract
''''''''

A discrete component or subassembly of a product.  Parts may be created or consumed as a normal consequence of the manufacturing process.

''''
Body
''''

Parts are used in worksteps as both inputs and as outputs.  A part such as 'board' may be the input to a CNC operation that consumes the part and produces a new part such as 'right_side_frame'.

''''''''''
Attributes
''''''''''

version : string
    
description : string
    
maker : label
    A *label* value is expected.
    
    
typical_cost : price
    A *price* value is expected.
    
    
sku_source : string
    A *string* value is expected.
    
    
sku : string
    A *string* value is expected.
    
    
qty : integer
    A *integer* value is expected.
    
    
label : label
    A *label* value is expected.
    
    
