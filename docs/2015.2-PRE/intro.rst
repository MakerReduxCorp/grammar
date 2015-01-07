Version 2015.2-PRE

A recipe consists of a series of blocks: parts, worksteps, parameters, and makers.

For example: ::

    recipe "Tabletops"
    
    maker default_maker
        version 2015.2-PRE
    
    workstep default_workstep
        version 2015.2-PRE
        industry assembly
        function workbench
        maker default_maker
        output default_part
            final


