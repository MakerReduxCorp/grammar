Version 2014.4

A recipe consists of a series of blocks: parts, worksteps, parameters, and makers.

For example: ::

    recipe "Tabletops"
    
    maker default_maker
        version 2015.1-PRE
    
    workstep default_workstep
        version 2015.1-PRE
        industry assembly
        function workbench
        maker default_maker
        output default_part
            final


