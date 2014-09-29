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

''''''''''
Attributes
''''''''''

version : string
    title: Version to Interpret By
    
    abstract: The version of Maker Redux Recipe that this was defined.
    
    body: A recipe can be made up of elements made up at different times in Maker Redux's history. This line simply indicates which version this element should be interpreted with.
    
    
company_id : hexadecimal
    title: Company ID
    
    abstract: The Maker Redux ID code of the suggested or original company to use in this Maker Role
    
    body: The Maker Redux ID code of the suggested or original company to use in this Maker Role
    
    
company_name : string
    title: Company Name
    
    abstract: The name of the suggested or original company to use in this Maker Role
    
    body: The name of the suggested or original company to use in this Maker Role
    
    
url : string
    title: Web URL
    
    abstract: A link to the suggested or original company.
    
    body: A link to the suggested or original company. Often, it is a web URL in the form of 'http://domain.com/'
    
    
description : string
    title: Description
    
    abstract: A description of the maker.
    
    body: An open description of the maker. Often the label given to the maker (such as 'woodshop' or 'printer') is sufficient to describe the makers role. But if additional information is helpfull, place that information in the description.
    
    
