Part
====

.. raw:: html

    <pre><b>part</b> <i>label</i></pre>

..

*A discrete component or subassembly of a product.  Parts may be created or consumed as a normal consequence of the manufacturing process.*

Parts are used in worksteps as both inputs and as outputs.  A part such as 'board' may be the input to a CNC operation that consumes the part and produces a new part such as 'right_side_frame'.

.. sidebar:: Variations
   
   There are additional attributes based on **category** :
   
     * ``lumber`` - :doc:`part.category.lumber`
     * ``wood_panel`` - :doc:`part.category.wood_panel`
     * ``wood_round_stock`` - :doc:`part.category.wood_round_stock`
     * ``from_distributor`` - :doc:`part.category.from_distributor`
     * ``open`` - :doc:`part.category.open`
   

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

    
.. raw:: html

    <pre><b>sku_source</b> <i>string</i></pre>

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

    *The estimates block is optional.  Including it will cause the values given to be used when generating as production estimate. Values given in the estimates are non-binding.*
    
    ::
    
        estimates
    
            prototype_cost $0.0
    
            pilot_cost $0.0
    
            production_cost $0.0
    
            prototype_time 0 minutes
    
            pilot_time 0 minutes
    
            production_time 0 minutes
    
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

    
