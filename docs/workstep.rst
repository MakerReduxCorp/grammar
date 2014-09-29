Workstep
========

''''''
Format
''''''

workstep *label*

''''''''
Abstract
''''''''

A single step in the process of building the final product.

''''
Body
''''

A workstep is a description of what must be *done* to completely build a product. Worksteps generally 'input' parts first, have a 'maker' then 'do stuff', and then 'output' parts.

''''''''''
Attributes
''''''''''

version : string
    title: System Version
    
    abstract: The version of Maker Redux's recipe system that this was defined with.
    
    body: A recipe can be made up of elements made up at different times in Maker Redux's history. This line simply indicates which version this element should be interpreted with.
    
    
description : string
    title: Description
    
    abstract: A general description of this workstep.
    
    body: A generate description of this workstep. While most of the attributes are for possible automation, this attribute is free-form and meant to be read by other people.
    
    
maker : label
    A *label* value is expected.
    
    title: Maker Label
    
    abstract: The label of the maker role assigned to perform this workstep.
    
    body: The label of the maker role assigned to perform this workstep.
    
    
input : label
    A *label* value is expected.
    
    title: Input Part
    
    abstract: A part (or workstep output) to be consumed by this workstep.
    
    body: If part(s) are needed to perform this workstep, then the 'input' attributes declare those inputs. Add one 'input' for each unique part needed. If the name given for the 'input' is not a known part, the system checks to see if there is a workstep with a matching name that does not have a named output. If that isn't found, then the system *automatically* creates the part and begins tracking it.
    
    The following items can be below this attribute:
    
    qty : integer
        A *integer* value is expected.
        
        title: Quantity Needed
        
        abstract: The number of parts needed.
        
        body: If you need more than one (1) of the part, then add a 'qty' attribute to tell the system the total needed. If you don't add a 'qty' the system defaults to 1.
        
        
    
    
output : label
    A *label* value is expected.
    
    The following items can be below this attribute:
    
    final : boolean
        A *boolean* value is expected.
        
        
    qty : integer
        A *integer* value is expected.
        
        
    
    
instructions : string
    
pre_event_timer : duration
    A *duration* value is expected.
    
    
post_event_timer : duration
    A *duration* value is expected.
    
    
repeat : qty
    A *qty* value is expected.
    
    
estimates : ignore
    The following items can be below this attribute:
    
    prototype_price : price
        A *price* value is expected.
        
        
    prototype_time : duration
        A *duration* value is expected.
        
        
    pilot_price : price
        A *price* value is expected.
        
        
    pilot_time : duration
        A *duration* value is expected.
        
        
    production_price : price
        A *price* value is expected.
        
        
    production_time : duration
        A *duration* value is expected.
        
        
    
    
industry : string
    
function : string
    
