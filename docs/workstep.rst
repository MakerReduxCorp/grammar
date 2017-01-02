Workstep
========

.. raw:: html

    <pre><b>workstep</b> <i>label</i></pre>

..

*A single step in the process of building the final product.*

A workstep is a description of what must be *done* to completely build a part. Worksteps generally list 'input' parts first, have a 'maker' then 'do stuff', and then 'output' parts.

.. sidebar:: Variations
   
   There are additional attributes based on **industry** :
   
     * ``adhesive`` - :doc:`workstep.industry.adhesive`
     * ``assembly`` - :doc:`workstep.industry.assembly`
     * ``ceramic`` - :doc:`workstep.industry.ceramic`
     * ``chem`` - :doc:`workstep.industry.chem`
     * ``composite`` - :doc:`workstep.industry.composite`
     * ``elecopt`` - :doc:`workstep.industry.elecopt`
     * ``metal`` - :doc:`workstep.industry.metal`
     * ``poly`` - :doc:`workstep.industry.poly`
     * ``paper`` - :doc:`workstep.industry.paper`
     * ``stone`` - :doc:`workstep.industry.stone`
     * ``textile`` - :doc:`workstep.industry.textile`
     * ``wood`` - :doc:`workstep.industry.wood`
   

''''''''''
Attributes
''''''''''

.. raw:: html

    <pre><b>version</b> <i>string</i></pre>

..

    *The version of Maker Redux's recipe system that this was defined with.*
    
    A recipe can be made up of elements made up at different times in Maker Redux's history. This line simply indicates which version this element should be interpreted with.
    
    
.. raw:: html

    <pre><b>description</b> <i>string</i></pre>

..

    *A general description of this workstep.*
    
    A generate description of this workstep. While most of the attributes are for possible automation, this attribute is free-form and meant to be read by other people.
    
    
.. raw:: html

    <pre><b>maker</b> <i>label</i></pre>

..

    *The maker role assigned to perform this workstep.*
    
    The label of the maker role assigned to perform this workstep.
    
    
.. raw:: html

    <pre><b>input</b> <i>label</i></pre>

..

    *A part (or workstep output) to be consumed by this workstep.*
    
    If part(s) are needed to perform this workstep, then the 'input' attributes declare those inputs. Add one 'input' for each unique part needed. If the name given for the 'input' is not a known part, the system checks to see if there is a workstep with a matching name that does not have a named output. If that isn't found, then the system *automatically* creates the part and begins tracking it.
    
    The following can further define this attribute:
    
        .. raw:: html
        
            <pre><b>qty</b> <i>integer</i></pre>
        
        ..
        
            *The number of parts needed.*
            
            If you need more than one (1) of the part, then add a 'qty' attribute to tell the system the total needed. If you don't add a 'qty' the system defaults to 1.
            
            
    
    
.. raw:: html

    <pre><b>output</b> <i>label</i></pre>

..

    *A part created by this workstep.*
    
    The workstep will produce one or more parts.  If the parts are not explicitly declared, the system will automatically create parts with a name matching the workstep name.
    
    The following can further define this attribute:
    
        .. raw:: html
        
            <pre><b>final</b> <i>boolean</i></pre>
        
        ..
        
            
        .. raw:: html
        
            <pre><b>qty</b> <i>integer</i></pre>
        
        ..
        
            *The number of parts produced by the workstep*
            
            A workstep may produce more than one part.  If you don't add a 'qty' the system defaults to 1.
            
            
    
    
.. raw:: html

    <pre><b>instructions</b> <i>string</i></pre>

..

    
.. raw:: html

    <pre><b>pre_event_timer</b> <i>duration</i></pre>

..

    
.. raw:: html

    <pre><b>post_event_timer</b> <i>duration</i></pre>

..

    
.. raw:: html

    <pre><b>repeat</b> <i>qty</i></pre>

..

    *How many times must this one unit of work be repeated to complete a single product. Must be a whole positive number.*
    
    For an example of how to use of amount vs repeat:
    
    
    
        workstep abc
    
            repeat 3
    
            amount 0.5
    
            amount_unit hr
    
    
    
    Would be interpreted as: an "abc" workstep takes 0.5 hours and is repeated 3 times.
    
    So a total of 1.5 hrs is needed to produce one product.
    
    
.. raw:: html

    <pre><b>amount</b> <i>decimal</i></pre>

..

    *The amount of __something__ that will be used to embody one unit of work. It is often measured in hours when used for human labor.*
    
    
.. raw:: html

    <pre><b>amount_unit</b> <i>text</i></pre>

..

    *For the amount needed, what is the unit of measurement. Defaults to hr (hours.)*
    
    
.. raw:: html

    <pre><b>estimates</b></pre>

..

    *Unofficial budgetary pricing.*
    
    The following can further define this attribute:
    
        .. raw:: html
        
            <pre><b>prototype_price</b> <i>price</i></pre>
        
        ..
        
            
        .. raw:: html
        
            <pre><b>prototype_setup</b> <i>price</i></pre>
        
        ..
        
            
        .. raw:: html
        
            <pre><b>prototype_time</b> <i>duration</i></pre>
        
        ..
        
            
        .. raw:: html
        
            <pre><b>pilot_price</b> <i>price</i></pre>
        
        ..
        
            
        .. raw:: html
        
            <pre><b>pilot_setup</b> <i>price</i></pre>
        
        ..
        
            
        .. raw:: html
        
            <pre><b>pilot_time</b> <i>duration</i></pre>
        
        ..
        
            
        .. raw:: html
        
            <pre><b>production_price</b> <i>price</i></pre>
        
        ..
        
            
        .. raw:: html
        
            <pre><b>production_setup</b> <i>price</i></pre>
        
        ..
        
            
        .. raw:: html
        
            <pre><b>production_time</b> <i>duration</i></pre>
        
        ..
        
            
    
    
.. raw:: html

    <pre><b>industry</b> <i>label</i></pre>

..

    
.. raw:: html

    <pre><b>function</b> <i>label</i></pre>

..

    
.. raw:: html

    <pre><b>industry</b> <i>label</i></pre>

..

    
