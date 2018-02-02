
############################
Chapter 1: Solution Overview
############################

*******************
Customer Challenges
*******************

Today there is a virtual explosion of rich media applications on the IP
network. This explosion of content and media types, both managed and
unmanaged, requires network architects to take a new look at their
Quality of Service (QoS) designs.

.. note::

  Some note.

Virtually all businesses are looking to increase the productivity of
their employees though the effective and innovative use of collaborative
applications, regardless of the hardware-platforms these applications
run on (PCs, laptops, tablets, smartphones, etc.), the physical or
geographical location of the collaborating employees, or the types of
media they wish to share on-demand. However, enabling and providing
seamless Quality of Experience (QoE) around such services has
traditionally placed challenging demands on network operators, to the
point where the foremost barrier to enabling QoS/QoE for collaborative
applications is the not technical abilities of the infrastructure.
Instead, it is the intrinsic complexity of enabling these features
across disparate devices in a comprehensive, yet cohesive, manner.

In order for QoS to be effective, it needs to be deployed end-to-end,
the same way a chain needs to be deployed end-to-end between a source
and a target in order to have utility. Every link in the chain must have
a cohesive, compatible QoS policy in order to achieve an end-to-end
service level. However, it is the platform-by-platform variations in
customizing, optimizing, and tuning that present the biggest barrier to
QoS/QoE deployments.

Enter the network controller. The network controller helps by
simplifying and abstracting platform-specific complexity from the
network operator. Specifically, the network controller is programmed
with all the link-specific information and Cisco best-practice knowledge
so as to construct optimal end-to-end QoS “chains.” An operator does not
need to know the hardware or software queuing structures of the
underlying infrastructure, nor do they need to know the QoS implications
of interconnecting wired and wireless networks, nor do they need to know
how the applications are to be recognized, despite the fact that an
increasing number of these are encrypted. All the operator needs to know
is which applications are important to his/her business. End-to-end
provisioning is done in minutes (vs. months), leveraging industry
standards and Cisco Validated Designs (CVDs).

********************
Solution Description
********************

Cisco Application Policy Infrastructure Controller Enterprise Module
(APIC-EM) is Cisco’s enterprise Software-Defined Networking (SDN)
controller. APIC-EM provides the automation functionality within Cisco’s
new enterprise architecture, called the *Digital Network Architecture
(DNA)*. A high level overview of the architecture is shown in the
following figure.

1. High-Level Overview of the Cisco Digital Network Architecture

.. image:: media/image3.png

EasyQoS is an application that runs on top of APIC-EM. Hence, it is an
integral part of the overall DNA architecture. The EasyQoS solution
abstracts QoS policy by using a declarative model as opposed to an
imperative model. A *declarative model* focuses on the intent or WHAT is
to be accomplished, without describing HOW it is to be accomplished. For
example, a network operator may express that an application such as
Cisco Jabber is business-relevant—meaning that it is to be treated with
the appropriate service—but he/she does not specify the details of how
the QoS/QoE policies are to be configured in order to achieve this
intent.

In contrast, an *imperative model* focuses on the execution of the
intent (describing in detail HOW the objective is to be realized). For
example, an imperative policy may include assigning Cisco Jabber to a
hardware priority queue with a given bandwidth allocation percentage on
a specific network switch interface.

Using a declarative model for policy-expression, rather than an
imperative model, frees the network operator from having to spend
extensive time-consuming cycles to deploy QoS policies. With a network
controller, changes can be made in minutes, rather than months,
resulting in agile networks that are tightly-aligned with evolving
business requirements.

The following figure provides an overview of how the solution works.

1. High-Level Overview of the EasyQoS Solution

.. image:: media/image4.png

In the center of the figure is the APIC-EM controller with the EasyQoS
application running on top of it. Network operators express their
business intent directly through a web-based graphical user interface
(GUI). EasyQoS then translates this business intent into platform
specific configurations that are provisioned via southbound Application
Programming Interfaces (APIs) onto groups of network infrastructure
devices (referred to as policy scopes), based upon the application-level
business intent. This functionality is referred to as *Static QoS*
within this document.

Not only can a network controller simplify QoS/QoE deployments and
accelerate these like never before, but it can also deliver completely
new functionality in the form of application-integration. Traditionally
applications have been separate and at arms-length from the network
infrastructure, often with dedicated yet distinct teams of IT personnel
to administer each. However, the role of the network isn’t primarily to
forward packets but rather to interconnect users via applications. As
such, the network controller can play a crucial new role as the broker
or intermediary between applications and the network. In order to do so,
it has to understand the languages of each, which it does via two main
types of APIs:

-  Northbound API (NB API)/Northbound Interface (NBI): this interface
   allows for applications to communicate with the network controller,
   informing it of network policy requirements in real-time. Northbound
   APIs are commonly deployed with Representational State Transfer
   (REST) models.

-  Southbound API (SB API)/Southbound Interface (SBI): this interface
   allows for the controller to communicate to individual network
   devices to configure the application policy-requirements. Southbound
   APIs include NETCONF/YANG models, as well as more traditional methods
   such as command line interface (CLI) and Simple Network Management
   Protocol (SNMP).

Specific to the context of QoE for collaboration, the network controller
can receive information from the call-manager of the collaborative
application—such as Cisco Unified Communications Manager (CUCM) for
Cisco Jabber or Cisco WebEx or Cisco Spark—via the Northbound APIs, in
order to inform it of any voice and/or video calls that are proceeding
on the network, providing it with the details of these flows. With this
information, the controller can then quickly deploy QoS end-to-end
across the enterprise for these voice and video calls, via the
Southbound APIs. This functionality is referred to as Dynamic QoS within
this document.

In summary the following is the business value of the EasyQoS solution:

-  The EasyQoS solution provides end-to-end orchestration of QoS in the
   Enterprise network.

-  The EasyQoS solution makes QoS policy simple and easy to deploy with
   an operator expressing business relevance for applications and the
   controller doing the rest under the hood.

-  The EasyQoS solution works for both greenfield and brownfield
   deployments.

-  The EasyQoS solution provides a declarative model that is
   business-intent driven, while abstracting away the
   platform/media/capability details.
