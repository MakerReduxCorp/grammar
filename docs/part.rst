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

    
.. raw:: html

    <pre><b>estimates</b></pre>

..

    *Unofficial budgetary pricing.*
    
    The following can further define this attribute:
    
        .. raw:: html
        
            <pre><b>prototype_price</b> <i>price</i></pre>
        
        ..
        
            
        .. raw:: html
        
            <pre><b>pilot_price</b> <i>price</i></pre>
        
        ..
        
            
        .. raw:: html
        
            <pre><b>production_price</b> <i>price</i></pre>
        
        ..
        
            
    
    
.. raw:: html

    <pre><b>category</b> <i>label</i></pre>

..

    
.. raw:: html

    <pre><b>industry</b> <i>label</i></pre>

..

    
