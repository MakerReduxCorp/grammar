Version 2015.1

A recipe consists of a series of blocks: parts, worksteps, parameters, and makers.

For example: ::

    recipe "Tabletops"
    
    maker default_maker
        version 2015.1
        
    workstep default_workstep
        version 2015.1
        industry assembly
        function workbench
        maker default_maker
        output default_part
            final

            
.. sidebar:: Other Versions

    * 2015.2-PRE (Not fully tested!):  :doc:`2015.2-PRE/index`
    * 2014.4:  :doc:`2014.4/index`
   
..


