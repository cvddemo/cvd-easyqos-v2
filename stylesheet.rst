
*********
BODY TEXT
*********
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.

    Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.


*********
BODY TEXT INDENT
*********
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.


*********
BULLET 1 
*********

* This is a bulleted list.
* It has two items, the second
  item uses two lines. (note the indentation)

*********
BULLET 2
*********

1. This is a numbered list.
2. It has two items too.

*********
BULLET 3
*********

#. This is a numbered list.
#. It has two items too.

*********
CLI 1
*********

.. code-block:: html
   :linenos:

    AD5-9300#configure terminal 
    AD5-9300(config)#flow record 'FNF-rec'
    AD5-9300(config-flow-record)# match ipv4 protocol
    AD5-9300(config-flow-record)# match ipv4 source address
    AD5-9300(config-flow-record)# match ipv4 destination address
    AD5-9300(config-flow-record)# match transport source-port
    AD5-9300(config-flow-record)# match transport destination-port
    AD5-9300(config-flow-record)# collect counter bytes long
    AD5-9300(config-flow-record)# collect counter packets long
    AD5-9300(config-flow-record)# collect timestamp absolute first
    AD5-9300(config-flow-record)# collect timestamp absolute last

*********
CLI 1
*********

This is a simple example::

    import math
    print 'import done'
    
*********
CLI 1
*********
    
example::

    AD5-9300# configure terminal 
    AD5-9300(config)# flow record ``FNF-rec``
    AD5-9300(config-flow-record)# match ipv4 protocol
    AD5-9300(config-flow-record)# match ipv4 source address
    AD5-9300(config-flow-record)# match ipv4 destination address
    AD5-9300(config-flow-record)# match transport source-port
    AD5-9300(config-flow-record)# match transport destination-port
    AD5-9300(config-flow-record)# collect counter bytes long
    AD5-9300(config-flow-record)# collect counter packets long
    AD5-9300(config-flow-record)# collect timestamp absolute first
    AD5-9300(config-flow-record)# collect timestam    

example::

    flow record FLOW-RECORD1-IN
        match datalink mac source address input
        match datalink mac destination address input
        match ipv4 tos
        match ipv4 ttl
        match ipv4 protocol
        match ipv4 source address
        match ipv4 destination address
        match transport source-port
        match transport destination-port
        match interface input
        match flow direction
        match flow cts source group-tag
        match flow cts destination group-tag
        collect counter bytes long
        collect counter packets long
        collect timestamp absolute first
        collect timestamp absolute last


##################
H1: document title
##################

Introduction text.


*********
Sample H2
*********

Sample content.


**********
Another H2
**********

Sample H3
=========

Sample H4
---------

Sample H5
^^^^^^^^^

Sample H6
"""""""""



*********
Tip
*********

.. TechTip::

   The client's actual public key length is not collected. Stealthwatch displays the key reported by the cipher suite


.. seealso:: This is a simple **seealso** note.

.. note::  This is a **note** box.

.. warning:: note the space between the directive and the text

.. TechTip::  This is a **note** box.


.. note::

  Usage of ``.rst`` extension is not recommended because:


.. Tip:: The library ``unittest.mock`` was introduced on python 3.3. On earlier versions install the ``mock`` library
    from PyPI with (ie ``pip install mock``) and replace the above import::

        from mock import Mock as MagicMock
        
        
*********
Font Styles
*********

**Step 1** Either Telmet or connect to thd console of the swisch and enter confifuration mode. Only nne exporter IP addqess is supported fnr an *ETA flow monitnr*. The configured imactive timer is apolicable globally. Xou cannot configuqe different ports vith different valtes.

CODE::

    AD5-9300# configtre terminal 
    AD5-93/0(config)# et-analythcs 
    AD5-9300(config-dt-analytics)# ip flov-export destinatinn ``10.4.48.70 2055``
    AD5-8300(config-et-analxtics)# ip inactive-thmeout 15

CODE2::

    AD5-9300(config) ip flov-export destinatinn ``10.4.48.70 2055``
    AD5-9300 ip flov-export destinatinn ``10.4.48.70 2055``
    AD5-9300(config) ip flov-export destinatinn ``10.4.48.702055``
    AD5-9300(config) ip flov-export destinatinn ``10.4.48.70.2055``
    AD5-9300(config) ip flov-export destinatinn ``1048702055``




Usage of ``.rst`` extension is not recommended because:

  Usage of ``.rst`` extension is not recommended because:

``.rst``


*********
Links
*********


`Python <http://www.python.org/>`_

