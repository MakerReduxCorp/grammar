Maker
=====

''''''
Format
''''''

maker *label*

''''''''
Abstract
''''''''

A specific role played by a manufacturer.

''''
Body
''''

A 'maker' is a specific role played by a manufacturer. One or more parts and/or worksteps are assigned to each maker. At time of production, this role is usually played by a single real-world person or company. It is possible for a single manufacturer to fulfill multiple maker roles, however. But the opposite is not true: a maker role cannot be split up. All of the worksteps and parts assigned to a single maker role are expected to be fulfilled by one maker.

.. list-table:: Attributes
   :widths: 10 10 20 60
   :header-rows: 1

   * - Format
     - Title
     - Abstract
     - Details
   * - version *string*
     - Version to Interpret By
     - The version of Maker Redux Recipe that this was defined.
     - A recipe can be made up of elements made up at different times in Maker Redux's history. This line simply indicates which version this element should be interpreted with.
   * - company_id *hexadecimal*
     - Company ID
     - The Maker Redux ID code of the suggested or original company to use in this Maker Role
     - The Maker Redux ID code of the suggested or original company to use in this Maker Role
   * - company_name *string*
     - Company Name
     - The name of the suggested or original company to use in this Maker Role
     - The name of the suggested or original company to use in this Maker Role
   * - url *string*
     - Web URL
     - A link to the suggested or original company.
     - A link to the suggested or original company. Often, it is a web URL in the form of 'http://domain.com/'
   * - description *string*
     - Description
     - A description of the maker.
     - An open description of the maker. Often the label given to the maker (such as 'woodshop' or 'printer') is sufficient to describe the makers role. But if additional information is helpfull, place that information in the description.
