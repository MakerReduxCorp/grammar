Part
====

.. raw:: html

    <pre><b>part</b> <i>label</i></pre>

..

*A discrete component or subassembly of a product.  Parts may be created or consumed as a normal consequence of the manufacturing process.*

Parts are used in worksteps as both inputs and as outputs.  A part such as 'board' may be the input to a CNC operation that consumes the part and produces a new part such as 'right_side_frame'.

.. sidebar:: Variations
   
   There are additional attributes based on **industry** :
   
     * ``adhesive`` - :doc:`part.industry.adhesive`
     * ``assembly`` - :doc:`part.industry.assembly`
     * ``ceramic`` - :doc:`part.industry.ceramic`
     * ``chem`` - :doc:`part.industry.chem`
     * ``composite`` - :doc:`part.industry.composite`
     * ``elecopt`` - :doc:`part.industry.elecopt`
     * ``metal`` - :doc:`part.industry.metal`
     * ``poly`` - :doc:`part.industry.poly`
     * ``paper`` - :doc:`part.industry.paper`
     * ``stone`` - :doc:`part.industry.stone`
     * ``textile`` - :doc:`part.industry.textile`
     * ``wood`` - :doc:`part.industry.wood`
   

''''''''''
Attributes
''''''''''

.. raw:: html

    <pre><b>version</b> <i>string</i></pre>

..

    
.. raw:: html

    <pre><b>description</b> <i>string</i></pre>

..

    
.. raw:: html

    <pre><b>maker</b> <i>label</i></pre>

..

    *The maker role that will supply this part.*
    
    
.. raw:: html

    <pre><b>sku_source</b> <i>string</i></pre>

..

    The following can further define this attribute:
    
        .. raw:: html
        
            <pre><b>url</b> <i>string</i></pre>
        
        ..
        
            
        .. raw:: html
        
            <pre><b>company_name</b> <i>string</i></pre>
        
        ..
        
            
    
    
.. raw:: html

    <pre><b>sku</b> <i>string</i></pre>

..

    
.. raw:: html

    <pre><b>qty</b> <i>integer</i></pre>

..

    *How many copies of this part will be used to produce one unit of product. Must be a whole positive number.*
    
    For an example of use of amount vs qty:
    
    
    
    part xyz
    
        qty 3
    
        amount 2.1
    
        amount_unit g
    
    
    
    Would be interpreted as: a 'xyz part' has 2.1g of material and is needed 3 times.
    
    So a total of 6.3g is used to produce one product.
    
    
.. raw:: html

    <pre><b>amount</b> <i>decimal</i></pre>

..

    *The amount of *substance* that will be used to embody one unit of part.*
    
    
.. raw:: html

    <pre><b>amount_unit</b> <i>text</i></pre>

..

    *For the amount needed, what is the unit of measurement.*
    
    
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
        
            <pre><b>pilot_price</b> <i>price</i></pre>
        
        ..
        
            
        .. raw:: html
        
            <pre><b>pilot_setup</b> <i>price</i></pre>
        
        ..
        
            
        .. raw:: html
        
            <pre><b>production_price</b> <i>price</i></pre>
        
        ..
        
            
        .. raw:: html
        
            <pre><b>production_setup</b> <i>price</i></pre>
        
        ..
        
            
    
    
.. raw:: html

    <pre><b>category</b> <i>label</i></pre>

..

    
.. raw:: html

    <pre><b>industry</b> <i>label</i></pre>

..

    
.. raw:: html

    <pre><b>industry</b> <i>label</i></pre>

..

    
