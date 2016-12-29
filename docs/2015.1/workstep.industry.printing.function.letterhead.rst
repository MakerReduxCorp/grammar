Letterhead
==========

*Printing custom letterhead on paper.*

''''''''''
Attributes
''''''''''

.. raw:: html

    <pre><b>paper_size</b> <i>radio_select</i></pre>

..

    choices:
    
      * ``8.5x11``
    
      * ``7.5x10``
    
      * ``custom``
    
        The following can further define this choice:
        
        .. raw:: html
        
            <pre><b>length</b> <i>length</i></pre>
        
        ..
        
            
        .. raw:: html
        
            <pre><b>width</b> <i>length</i></pre>
        
        ..
        
            
        
    
    *Size of the paper for the letterhead.*
    
    The 8.5" x 11" and 7.5" x 10" sizes are common. For any other size, choose 'custom' and specify the length and width of the FINAL product.
    
    
.. raw:: html

    <pre><b>method</b> <i>radio_select</i></pre>

..

    choices:
    
      * ``digital``
    
      * ``offset``
    
    
    
.. raw:: html

    <pre><b>ink_colors</b> <i>radio_select</i></pre>

..

    choices:
    
      * ``PMS_spot``
    
        The following can further define this choice:
        
        .. raw:: html
        
            <pre><b>pantone</b> <i>string</i></pre>
        
        ..
        
            
        .. raw:: html
        
            <pre><b>pdf_file</b> <i>file</i></pre>
        
        ..
        
            
        
      * ``process``
    
        The following can further define this choice:
        
        .. raw:: html
        
            <pre><b>cyan_pdf_file</b> <i>file</i></pre>
        
        ..
        
            
        .. raw:: html
        
            <pre><b>magenta_pdf_file</b> <i>file</i></pre>
        
        ..
        
            
        .. raw:: html
        
            <pre><b>yellow_pdf_file</b> <i>file</i></pre>
        
        ..
        
            
        .. raw:: html
        
            <pre><b>key_pdf_file</b> <i>file</i></pre>
        
        ..
        
            
        
    
    
.. raw:: html

    <pre><b>paper_color</b> <i>radio_select</i></pre>

..

    choices:
    
      * ``white``
    
      * ``natural``
    
      * ``cream``
    
      * ``ivory``
    
    
    
.. raw:: html

    <pre><b>paper_basis_weight</b> <i>radio_select</i></pre>

..

    choices:
    
      * ``20lb_writing``
    
      * ``24lb_writing``
    
      * ``28lb_writing``
    
      * ``32lb_writing``
    
      * ``50lb_text``
    
      * ``60lb_text``
    
      * ``70lb_text``
    
      * ``80lb_text``
    
    
    
.. raw:: html

    <pre><b>paper_texture</b> <i>radio_select</i></pre>

..

    choices:
    
      * ``smooth``
    
      * ``wove``
    
      * ``linen``
    
      * ``laid``
    
      * ``cotton``
    
      * ``vellum``
    
      * ``fiber``
    
    
    
.. raw:: html

    <pre><b>bleed</b> <i>boolean</i></pre>

..

    
.. raw:: html

    <pre><b>slip_sheet_count</b> <i>qty</i></pre>

..

    
.. raw:: html

    <pre><b>packaging</b> <i>radio_select</i></pre>

..

    choices:
    
      * ``ream_wrapped``
    
        The following can further define this choice:
        
        .. raw:: html
        
            <pre><b>sheets_per</b> <i>radio_select</i></pre>
        
        ..
        
            choices:
            
              * ``500``
            
            
            
        
      * ``shrink_wrapped``
    
      * ``boxed``
    
        The following can further define this choice:
        
        .. raw:: html
        
            <pre><b>sheets_per</b> <i>radio_select</i></pre>
        
        ..
        
            choices:
            
              * ``500``
            
              * ``1000``
            
              * ``2500``
            
              * ``5000``
            
            
            
        
    
    
