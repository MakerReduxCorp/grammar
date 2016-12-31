Version 2017.1

A recipe consists of a series of blocks: parts, worksteps, parameters, and makers.

For example: ::

    recipe "Tabletops"
    
    maker DEFAULT_MAKER
        version 2017.1
        
    workstep DEFAULT_WORKSTEP
        version 2017.1
        industry assembly
        function package
        maker DEFAULT_WORKSTEP
        output DEFAULT_PART
            final

            
.. sidebar:: Other Versions

    * 2015.1:  :doc:`2015.1/index`
    * 2014.4:  :doc:`2014.4/index`
   
..


