Shipping
========

''''''''
Abstract
''''''''
Preparation of materials for transport by a third party carrier.  Includes packaging, labeling, and handling instructions."

''''
body
''''
The shipping grammar includes functions related to getting physical goods ready to be handled by a shipper.

The grammar will focus on the differences between 'packaging' (ie. the outward facing carton, crate, box, or envelope) and 'fill' (ie the cushioning material between the product and the package).

functions:
''''''''''
* :ref:`function-package`

.. toctree::
   :maxdepth: 2

Functions
=========

.. _function-package:

package
=======

"Pack materials for shipping"

========= ======== ============ ============================== ===========
Attribute Required Type         Choices                        Description
========= ======== ============ ============================== ===========
fill      True     radio_select  starch_peanuts, preform_styro "material to fill around shipped parts"
========= ======== ============ ============================== ===========
