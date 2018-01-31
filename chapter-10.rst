
##################
Chapter 10: WLAN QoS Design
##################

AireOS WLC QoS Design

This section discusses AireOS wireless LAN controller platforms within
the EasyQoS solution. For the APIC-EM 1.3 release and higher, only Cisco
WLCs running the AireOS operating system are supported within the
EasyQoS application. Dedicated IOS XE WLCs such as the Cisco 5760 are
not currently supported. WLC functionality within Catalyst 3850, 3650,
and Catalyst 4500-E Series switches are also not currently supported.
Further, only centralized (local) mode configurations, in which traffic
is tunneled from the Access Point to the WLC before being placed onto
the LAN, are supported.

EasyQoS within APIC-EM release 1.5 introduced support for Fastlane QoS
within WLCs running AireOS software version 8.2.112 and higher. FastLane
QoS on AireOS WLCs is essentially a macro which enables best-practice
configurations on both the overall WLC platform and the specific
WLAN/SSID in which it is enabled. The actual configuration provisioned
onto the WLC by enabling Fastlane QoS is nearly identical to the
configuration which EasyQoS has been provisioning on AireOS WLCs as of
APIC-EM release 1.1.

The following sections detail the configuration steps implemented by
EasyQoS when configuring wireless policy. The steps apply to both
Fastlane and non-Fastlane policies. With APIC-EM release 1.5 EasyQoS
policy automatically enabled the Fastlane feature within a WLAN/SSID to
which policy was applied if the WLC was running AireOS release 8.3.112
and higher. With APIC-EM release 1.6, the network operator must choose
to enable the Fastlane feature within the EasyQoS wireless policy
applied to the policy scope which contains the WLC. Enabling the
Fastlane feature within the EasyQoS web-based GUI was discussed in the
***Wireless Policies*** section of the ***APIC-EM and the EasyQoS
Application*** chapter.

The Fastlane feature is enabled through the following CLI command.

config qos fastlane enable <WLAN –id>

<WLAN –id> refers to the WLAN/SSID to which Fastlane is to be enabled.
From a web GUI perspective, Fastlane is enabled per WLAN/SSID as shown
in the figure below.

1. Enabling per WLAN / SSID QoS Features

|image110|

As a result of enabling the Fastlane feature, the steps discussed within
the following sections are implemented automatically by the WLC platform
itself. For AireOS WLCs running AireOS releases below 8.3.112, EasyQoS
itself provisions each of the steps discussed within the following
sections. Any differences between Fastlane and non-Fastlane policies are
pointed out within the sections below.

Disabling WLANs and Radios

In order to provision the global QoS configuration (meaning the QoS
configuration which affects the entire WLC) required for EasyQoS Static
QoS discussed in the sections below, all SSIDs and WLANs must be first
disabled. In addition, the 802.11 b/g/n and the 802.11a/n/ac radios in
all APs controlled by the WLC must also be disabled. APIC-EM uses an SSH
session established to AireOS WLCs in order to provision QoS policy,
instead of the web-based GUI.

-  Note: Screen captures from the web-based GUI interface are shown
   throughout this chapter for ease of understanding of the
   configuration only, because many network operators are familiar with
   the web-based GUI interface. The examples within this chapter are
   based on WLCs running AireOS release 8.3.112 software. WLCs running
   different AireOS software releases may have subtle differences in
   screen appearance

The following global commands provisioned either directly by APIC-EM
EasyQoS, or indirectly by the WLC as a result of enabling the Fastlane
feature, disable all WLANS and radios on an AireOS WLC.

config 802.11a disable network

config 802.11b disable network

config wlan disable all

This means that the initial provisioning of EasyQoS Static QoS policy is
a disruptive process to the WLCs that are part of a policy. Wireless
connectivity itself will be disrupted for wireless clients connected to
any WLAN/SSID on any Access Point serviced by a WLC that contains a
WLAN/SSID to which EasyQoS policy is to be applied. To emphasize this
again, the disruption will be to network connectivity and not just QoS
marking. Hence, is it recommended that the initial provisioning of
EasyQoS Static QoS policies deployed to WLANs should be scheduled during
normal network change-control hours. The disruption will be to all
WLANs/SSIDs serviced by the AireOS WLC.

Specifically the changes provisioned by EasyQoS that require the 802.11
b/g/n and 802.11a/n/ac radios and the WLAN/SSIDs to be disabled are as
follows:

-  Changes to the EDCA parameters

-  Changes to Call Admission Control (CAC) settings

-  Changes to the Global QoS Profile settings (specifically the Platinum
   QoS Profile)

-  Changes to the QoS Map settings

Changes to the specific WLAN/SSID to which the EasyQoS policy is being
applied require only the WLAN/SSID to be disabled. These are as follows:

-  Applying the QoS Profile to the WLAN/SSID

-  Enabling AVC on the WLAN/SSID

-  Applying the AVC Profile to the WLAN/SSID

Therefore, after the initial provisioning of EasyQoS policy to any
WLAN/SSID on the WLC, further modifications to an EasyQoS policy that
simply involve changes to the applications within the policy may only be
disruptive to the specific WLAN/SSID to which the policy is applied.

QoS Trust Boundaries and Policy Enforcement Points

QoS trust boundaries and policy enforcement points are more complicated
with IEEE 802.11 wireless infrastructure due to the fact that
over-the-air QoS is based on Layer 2 headers, not Layer 3 headers. IEEE
802.11 QoS consists of eight User Priorities (UPs) that are mapped to
four Access Categories (ACs)—Voice, Video, Best Effort, and Background.
Layer 3 DSCP values must be mapped to and from the eight Layer 2 IEEE
802.11 UPs, which are then mapped to the four ACs. Hence, multiple QoS
trust boundaries can exist—depending upon whether the trust boundary is
based on Layer 2 UP or Layer 3 DSCP marking. Additionally, there can be
multiple policy enforcement points:

-  Policy enforcement points for mapping Layer 3 DSCP value to Layer 2
   UP values to-and-from wireless clients

-  Policy enforcement points for re-mapping Layer 3 DSCP values to other
   Layer 3 DSCP values based on AVC profiles

An example of the various wireless trust boundaries and policy
enforcement points is shown in the following figure.

1. Wireless Trust Boundaries and Policy Enforcement Points

|image111|

Explanation of the various trust boundaries and policy enforcement
points can best be explained based on type of wireless client as
follows:

-  Non- `WiFi Multimedia
   (WMM) <http://www.cisco.com/c/en/us/td/docs/wireless/access_point/12-4_3g_JA/configuration/guide/ios1243gjaconfigguide/s43qos.html#pgfId-1066300>`__
   capable wireless clients

-  WMM capable wireless clients (non-802.11u capable)

-  802.11u capable wireless clients

Non-WMM Capable Wireless Clients

Non-WMM capable wireless clients are less common in deployments today.
Such devices do not send wireless frames with the IEEE 802.11 QoS
Control field. Hence there is no Layer 2 IEEE 802.11 QoS UP information
included within frames sent by these clients, and therefore no Layer 2
QoS trust boundary. All traffic sent by these clients is by default
placed into the Best Effort AC when it is sent over-the-air from the
wireless client to the Access Point (AP).

From the AP to the WLC, IEEE 802.11 frames are encapsulated within an IP
packet with a CAPWAP header and sent upstream. CAPWAP effectively
tunnels IEEE 802.11 frames through an IP network between the AP and the
WLC. Within the IEEE 802.11 frame itself, there is also an encapsulated
IP packet from the wireless client. The ToS field of that inner IP
packet can have any DSCP marking—assuming the application, the operating
system, and the potentially the wireless drivers running on the wireless
device allow such DSCP markings.

For the EasyQoS solution, the Platinum QoS Profile within the WLC is
applied to the WLAN/SSID by EasyQoS. The global Platinum QoS Profile is
modified—either directly by EasyQoS, or indirectly by the WLC itself as
a result of enabling Fastlane—to allow upstream and downstream traffic
sent over the wireless medium to use up to the Voice AC. However, the
global Platinum QoS Profile is also modified to set the unicast default
priority and multicast default priority to the best effort Access
Category. This means that any unicast and multicast traffic without an
802.11 QoS Control field are set to best effort. This is accomplished
via the two “besteffort” parameters in the following global command
provisioned onto the AireOS WLCs:

config qos priority platinum voice besteffort besteffort

The net effect is that if the operating system and wireless drivers of
the non-WMM wireless device allow an application running on the wireless
device to mark IP packets with a DSCP value, the DSCP marking of the
CAPWAP header will still be set to the default DSCP value (DSCP =0) as
the traffic is sent from the AP to the WLC. If the operating system and
wireless drivers of the wireless device do not allow an application to
mark IP packets with a DSCP value, or if the application itself simply
sends all traffic with a default DSCP value, the DSCP marking of the
CAPWAP header also be set to the default DSCP value. In other words, all
traffic from non-WMM clients will receive best effort (Default)
treatment from the AP to the WLC.

With this configuration, the AP serves as a trust boundary and policy
enforcement point for non-WMM devices. Regardless of the DSCP values of
the IP packets sent by the wireless client, the DSCP value of the outer
CAPWAP header will be set to the default DSCP value (DSCP = 0), when
packets are sent from the AP to the WLC. Note, however, that the
original DSCP markings of the IP packets within the CAPWAP tunnel are
still preserved up to the WLC. The AVC policy applied at the WLC may,
however, remark this traffic if the application is part of the AVC
policy.

For downstream traffic, the DSCP marking of the outer CAPWAP header will
match the DSCP marking of inner IP packet, also encapsulated within an
IEEE 802.11 frame. This is because traffic up to the voice Access
Category is allowed with the Platinum QoS Profile as shown in the
configuration example above. This preserves the Layer 3 DSCP QoS marking
from the WLC to the AP. For non-WMM wireless clients, 802.11 frames are
sent over-the-air with no UP value, because the 802.11 QoS field is not
supported by non-WMM clients. However, the traffic is still scheduled
into the appropriate AC queues, based on the mapping of the DSCP value
of the outer CAPWAP header to the UP. So, effectively, QoS is preserved
downstream.

WMM Capable Wireless Clients (non-802.11u Capable)

WMM capable wireless clients send wireless frames with the IEEE 802.11
QoS Control field. Hence there is Layer 2 UP information included within
frames sent by these clients, and therefore the Layer 2 trust boundary
is at the wireless client, as shown in Figure 111 above. However, the
operating system and wireless drivers of the wireless device must allow
application traffic to be marked with a Layer 2 UP. Further, the
application must also be able to send traffic with DSCP markings. The
mapping of those DSCP markings to the appropriate IEEE 802.11 UPs is
then largely determined by the vendor of the wireless device if the
device does not support IEEE 802.11u.

Traffic sent by these clients is placed into an IEEE 802.11 AC as it is
sent over-the-air from the wireless client to the AP, based on the UP as
shown in the figure below.

1. 802.11 UP Values and ACs

|image112|

The following global command configured on AireOS WLCs by APIC-EM
EasyQoS will cause the AP to mark the ToS field of the outer CAPWAP
header to match the DSCP marking of the encapsulated IP packet within
the IEEE 802.11 frame sent by the wireless client.

config qos qosmap trust-dscp-upstream enable

For the EasyQoS solution, the Platinum QoS profile within the WLC is
configured to allow upstream and downstream traffic sent over the
wireless medium to use up to the Voice AC. This is accomplished via the
following global command on AireOS WLCs.

config qos priority platinum voice besteffort besteffort

The “voice” parameter within the command allows the AP to send traffic
up to and including the IEEE 802.11 AC of Voice and UP values up to and
including 7, to wireless clients that support WMM. It also honors
traffic sent from wireless clients that support WMM to the AP that
includes the IEEE 802.11 AC of Voice and UP value up to and including 7.

The net effect is that if the operating system and wireless drivers of
the wireless device allow an application running on the wireless device
to mark IP packets with a DSCP value, the DSCP marking of the CAPWAP
header will match this DSCP value as the traffic is sent from the AP to
the WLC. If the operating system and wireless drivers of the wireless
device do not allow an application to mark IP packets with a DSCP value,
or if the application simply sends all traffic with a default DSCP value
(DSCP = 0), the DSCP marking of the CAPWAP header also be set to the
default DSCP value.

Hence, with this configuration, the wireless client is trusted to send
traffic marked with the correct DSCP value. In other words, the DSCP
trust boundary is extended to the wireless client. The AP serves as a
policy enforcement point, mapping the trusted DSCP values of the IP
packets sent by the wireless client to the DSCP values of the CAPWAP
headers when packets are sent from the AP to the WLC. Note that the
original DSCP markings of the IP packets within the CAPWAP tunnel are
also preserved up to the WLC. The AVC policy applied at the WLC may,
however, remark this traffic if the application is part of the AVC
policy.

For downstream traffic, the DSCP marking of the outer CAPWAP header will
match the DSCP marking of the inner IP packet, also encapsulated within
an IEEE 802.11 frame. For WMM-enabled wireless clients, IEEE 802.11
frames are sent over-the-air with UP values, because the IEEE 802.11 QoS
field is supported by WMM clients.

Additional modifications to the global Platinum QoS profile provisioned
by EasyQoS are as follows:

-  802.11p marking is disabled (all wired marking is DSCP-based) via the
   following command provisioned by EasyQoS.

config qos protocol-type platinum none

-  Downstream UDP traffic is set to be unrestricted by EasyQoS through
   the following commands.

config qos burst-realtime-rate platinum per-ssid downstream 0

config qos average-realtime-rate platinum per-ssid downstream 0

From the perspective of the web-based graphical user, the configuration
of the Platinum QoS Profile is modified to appear as shown in the figure
below.

1. Platinum QoS Profile Configuration After EasyQoS / Fastlane
   Modifications

|image113|

The Platinum QoS Profile is applied to every SSID/WLAN controlled by
EasyQoS. This is accomplished via the following SSID/WLAN-level command
on AireOS WLCs:

config wlan qos x platinum

Note that “x” refers to the ID of the particular SSID/WLAN of the AireOS
WLC.

The AP will set the IEEE 802.11 UP value based on the QoS Map
configuration within the WLC. As of AireOS software version 8.1.111.0
and higher, the QoS Map is now configurable, and applies globally to the
entire WLC.

The following is the QoS Map Configuration along with exceptions that is
provisioned by EasyQoS to AireOS WLCs for EasyQoS policies.

config qos qosmap disable

config qos qosmap default

config qos qosmap up-to-dscp-map 0 0 0 7

config qos qosmap up-to-dscp-map 1 8 8 15

config qos qosmap up-to-dscp-map 2 16 16 23

config qos qosmap up-to-dscp-map 3 24 24 31

config qos qosmap up-to-dscp-map 4 32 32 39

config qos qosmap up-to-dscp-map 5 34 40 47

config qos qosmap up-to-dscp-map 6 46 48 62

config qos qosmap up-to-dscp-map 7 56 56 63

config qos qosmap clear-all

config qos qosmap dscp-to-up-exception 16 0

config qos qosmap dscp-to-up-exception 8 1

config qos qosmap dscp-to-up-exception 10 2

config qos qosmap dscp-to-up-exception 12 2

config qos qosmap dscp-to-up-exception 14 2

config qos qosmap dscp-to-up-exception 18 2

config qos qosmap dscp-to-up-exception 20 3

config qos qosmap dscp-to-up-exception 22 3

config qos qosmap dscp-to-up-exception 38 4

config qos qosmap dscp-to-up-exception 36 4

config qos qosmap dscp-to-up-exception 34 4

config qos qosmap dscp-to-up-exception 30 4

config qos qosmap dscp-to-up-exception 28 4

config qos qosmap dscp-to-up-exception 26 4

config qos qosmap dscp-to-up-exception 24 4

config qos qosmap dscp-to-up-exception 40 5

config qos qosmap dscp-to-up-exception 32 5

config qos qosmap dscp-to-up-exception 46 6

config qos qosmap dscp-to-up-exception 44 6

config qos qosmap trust-dscp-upstream enable

config qos qosmap enable

From the perspective of the web-based graphical user, the configuration
of the QoS Map is modified to appear as shown in the figure below.

1. QoS Map Configuration After EasyQoS / Fastlane Modifications

|image114|

The result of the QoS Map configuration is to map values as shown in the
table below.

1. EasyQoS QoS Map Values

+-------------------------------+-------------+--------------------------+
| DSCP Values                   | UP Values   | 802.11 Access Category   |
+===============================+=============+==========================+
| CS0 (DSCP 0)                  | UP 0        | Best Effort              |
|                               |             |                          |
| DSCP 1—7                      |             |                          |
|                               |             |                          |
| CS2 (DSCP 16)                 |             |                          |
+-------------------------------+-------------+--------------------------+
| CS1 (DSCP 8)                  | UP 1        | Background               |
|                               |             |                          |
| DSCP 9, 11, 13, 15            |             |                          |
+-------------------------------+-------------+--------------------------+
| AF11 (DSCP 10)                | UP 2        | Background               |
|                               |             |                          |
| AF12 (DSCP 12)                |             |                          |
|                               |             |                          |
| AF13 (DSCP 14)                |             |                          |
|                               |             |                          |
| DSCP 17, 19, 21, 23           |             |                          |
+-------------------------------+-------------+--------------------------+
| AF21 (DSCP 18)                | UP 3        | Best Effort              |
|                               |             |                          |
| AF22 (DSCP 20)                |             |                          |
|                               |             |                          |
| AF23 (DSCP 22)                |             |                          |
|                               |             |                          |
| DSCP 25, 27, 29, 31           |             |                          |
+-------------------------------+-------------+--------------------------+
| CS3 (DSCP 24)                 | UP 4        | Video                    |
|                               |             |                          |
| AF31 (DSCP 26)                |             |                          |
|                               |             |                          |
| AF32 (DSCP 28)                |             |                          |
|                               |             |                          |
| AF33 (DSCP 30)                |             |                          |
|                               |             |                          |
| AF41 (DSCP 34)                |             |                          |
|                               |             |                          |
| AF42 (DSCP 36)                |             |                          |
|                               |             |                          |
| AF43 (DSCP 38)                |             |                          |
|                               |             |                          |
| DSCP 33, 35, 37, 39           |             |                          |
+-------------------------------+-------------+--------------------------+
| CS4 (DSCP 32)                 | UP 5        | Video                    |
|                               |             |                          |
| CS5 (DSCP 40)                 |             |                          |
|                               |             |                          |
| DSCP 41, 42, 43, 45, 47, 48   |             |                          |
+-------------------------------+-------------+--------------------------+
| EF (DSCP 46)                  | UP 6        | Voice                    |
|                               |             |                          |
| Admitted Voice (DSCP 44)      |             |                          |
|                               |             |                          |
| CS6 (DSCP 48)                 |             |                          |
|                               |             |                          |
| DSCP 49—55                    |             |                          |
+-------------------------------+-------------+--------------------------+
| CS7 (DSCP 56)                 | UP 7        | Voice                    |
|                               |             |                          |
| DSCP 57—63                    |             |                          |
+-------------------------------+-------------+--------------------------+

AireOS WLCs must be running a minimum of software version 8.1.111.0 in
order to support configurable DSCP-to-UP mappings (via the QoS Map)
required for the EasyQoS solution. Downstream traffic is scheduled into
the appropriate IEEE 802.11 AC queues based on the mapping of the DSCP
value to UP, preserving QoS downstream across the Layer 2 wireless
medium.

-  Note: For AireOS WLC platforms, modifications to the mapping of
   traffic-classes to DSCP values within the EasyQoS web-based GUI will
   not affect the DSCP-to-UP mapping tables within WLC platforms
   configured by EasyQoS. In some situations, a sub-optimal QoS
   implementation may result. For example, if the network operator
   changes the Multimedia-Conferencing traffic-class to a DSCP marking
   which maps to a User Priority (UP) which lies within the Access
   Category (AC) of Background traffic, then Multimedia-Conferencing
   traffic will be treated as Background traffic across the 802.11
   wireless medium. The network operator should use caution when
   modifying the DSCP markings of traffic-classes.

IEEE 802.11u Capable Wireless Clients

IEEE 802.11u capable wireless clients also send wireless frames with the
IEEE 802.11 QoS Control field. Hence there is Layer 2 UP information
included within frames sent by these clients, and therefore the Layer 2
trust boundary is at the wireless client, as shown in Figure 111 above.
Again, the operating system and wireless drivers of the wireless device
must allow application traffic to be marked with a Layer 2 UP. The
application must also be able to send traffic with DSCP markings.
However, the mapping of those DSCP markings to the appropriate IEEE
802.11 UPs is set via the QoS Map pushed from the AP to the IEEE 802.11u
capable wireless client. Hence the Layer 3 DSCP QoS trust boundary is
again at the wireless client, although the mapping of the DSCP values to
User Priority is controlled now via the QoS Map configuration on the
AireOS WLC. The upstream and downstream marking of traffic is identical
to that discussed in the ***WMM capable wireless clients (non-802.11u
capable)*** section.

AVC-Based Classification & Marking Policy

With the EasyQoS solution design, an AVC profile is also applied to the
inner IP packet—meaning after the removal of the CAPWAP header and IEEE
802.11 frame for upstream traffic and before encapsulation with the
CAPWAP header for downstream traffic. This applies to all types of
wireless clients discussed in the sections above. In other words,
classification & marking policies are applied in the upstream direction
or in both the upstream and downstream directions, via AVC profiles
applied to individual SSIDs/WLANs controlled by EasyQoS. This is
accomplished via the following AireOS WLC SSID/WLAN-level commands.

config wlan avc x visibility enable

config wlan avc x profile EZQoS-WlanId-1 enable

Note that “x” refers to the ID of the particular SSID/WLAN. The profile
name configured by the EasyQoS application will always be
EZQoS-WlanId-N, where N refers to the WLAN/SSID number.

For WLANs/SSIDs in which Fastlane is enabled, EasyQoS will change the
default AVC Profile created by Fastlane and assigned to the WLAN/SSID,
to the AVC Profile created based upon the applications selected for the
EasyQoS policy applied to the policy-scope which contains the WLC.

-  Note: AVC policies can specify either marking or dropping of traffic,
   based on an AVC profile. Only marking of traffic is used by EasyQoS.

Because AVC contains the NBAR2 engine, WLAN QoS policies consist of
classification & marking policies that are based on the Cisco NBAR
protocol pack supported by the WLC. These policies are currently applied
at the WLC. Hence, the AVC Profile serves as another Layer 3 policy
enforcement point for the original IP packet sent by the wireless
client, as shown in Figure 111 above.

The specific applications within the profile are based upon the
Favorites chosen by the network operator in the EasyQoS GUI, when
applying a QoS Policy to a WLAN/SSID within Policy Scope that contains
an AireOS WLC. This is discussed further in the ***APIC-EM and the
EasyQoS Application*** chapter. AireOS WLCs are currently limited to
only 32 applications per AVC policy. If less than 32 Favorites are
chosen, APIC-EM EasyQoS will select the remaining applications for the
AVC profile based upon applications that are most commonly used within
the network. All 1300+ applications within the NBAR2 taxonomy have an
attribute called “commonly-used”. This attribute can have a value from 1
(least commonly used) to 10 (most commonly used). For applications that
have identical values of the “commonly-used” attribute, EasyQoS will
select the applications to be provisioned into the AVC-based policy
based on the alphabetical name of the application.

An example of the commands provisioned by APIC-EM EasyQoS in order to
create an AVC profile is shown in the configuration below.

config avc profile EZQoS-WlanId-1 create

config avc profile EZQoS-WlanId-1 rule add application cifs mark 10
UPSTREAM

config avc profile EZQoS-WlanId-1 rule add application
cisco-jabber-control mark 24 UPSTREAM

config avc profile EXQoS-WlanId-1 rule add application crashplan mark 10
UPSTREAM

config avc profile EZQoS-WlanId-1 rule add application datex-asn mark 24
UPSTREAM

config avc profile EZQoS-WlanId-1 rule add application dnp mark 24
UPSTREAM

config avc profile EZQoS-WlanId-1 rule add application exchange mark 10
UPSTREAM

config avc profile EZQoS-WlanId-1 rule add application google-play mark
10 UPSTREAM

config avc profile EZQoS-WlanId-1 rule add application h323 mark 24
UPSTREAM

config avc profile EZQoS-WlanId-1 rule add application mgcp mark 24
UPSTREAM

config avc profile EZQoS-WlanId-1 rule add application netvmg-traceroute
mark 24 UPSTREAM

config avc profile EZQoS-WlanId-1 rule add application nfs mark 10
UPSTREAM

config avc profile EZQoS-WlanId-1 rule add application
outlook-web-service mark 10 UPSTREAM

config avc profile EZQoS-WlanId-1 rule add application prm-nm mark 24
UPSTREAM

config avc profile EZQoS-WlanId-1 rule add application prm-sm mark 24
UPSTREAM

config avc profile EZQoS-WlanId-1 rule add application rpc2portmap mark
24 UPSTREAM

config avc profile EZQoS-WlanId-1 rule add application rsvp\_tunnel mark
24 UPSTREAM

config avc profile EZQoS-WlanId-1 rule add application rtcp mark 24
UPSTREAM

config avc profile EZQoS-WlanId-1 rule add application rtsp mark 24
UPSTREAM

config avc profile EZQoS-WlanId-1 rule add application rtsps mark 24
UPSTREAM

config avc profile EZQoS-WlanId-1 rule add application sflow mark 24
UPSTREAM

config avc profile EZQoS-WlanId-1 rule add application sgcp mark 24
UPSTREAM

config avc profile EZQoS-WlanId-1 rule add application sip mark 24
UPSTREAM

config avc profile EZQoS-WlanId-1 rule add application sip-tls mark 24
UPSTREAM

config avc profile EZQoS-WlanId-1 rule add application skinny mark 24
UPSTREAM

config avc profile EZQoS-WlanId-1 rule add application snpp mark 24
UPSTREAM

config avc profile EZQoS-WlanId-1 rule add application spsc mark 24
UPSTREAM

config avc profile EZQoS-WlanId-1 rule add application ss7ns mark 24
UPSTREAM

config avc profile EZQoS-WlanId-1 rule add application svrloc mark 24
UPSTREAM

config avc profile EZQoS-WlanId-1 rule add application
telepresence-control mark 24 UPSTREAM

config avc profile EZQoS-WlanId-1 rule add application
telepresence-media mark 32 UPSTREAM

config avc profile EZQoS-WlanId-1 rule add application tpip mark 24
UPSTREAM

config avc profile EZQoS-WlanId-1 rule add application ups mark 24
UPSTREAM

From the perspective of the web-based graphical user, the configuration
of the AVC Profile is as shown in the figure below.

1. Configuration of the AVC Profile

|image115|

By default, the AVC policy is unidirectional. This means that the AVC
policy is applied to individual applications within the profile only in
the upstream direction. In order to make the policy for individual
applications within the AVC profile bi-directional, the network operator
must select QoS policy to be applied bidirectionally for the given
application within the EasyQoS policy screen. This is discussed
***Policies*** section of this document.

-  Note: FlexConnect designs are not supported with the APIC-EM 1.6
   release of EasyQoS. Only centralized (local mode) deployments are
   supported within EasyQoS.

Custom Queuing Profiles and Changing the Traffic-Class of an Application

The configuration of custom Queuing Profiles was discussed in the
***Advanced Settings*** section of the ***APIC-EM and the EasyQoS
Application*** chapter. Custom queuing profiles allow the network
operator to specify the amount of bandwidth allocated per traffic-class
and the DSCP marking per traffic-class. However, AireOS WLCs do not
enforce any per traffic-class bandwidth allocations within the QoS
policy provisioned by EasyQoS. Therefore, bandwidth allocations within
custom Queuing Profiles are not enforced on WLC platforms.

Changing the DSCP markings of traffic-classes within Custom Queuing
Profiles applied to a policy scope will modify the AVC Profile
provisioned to the WLAN as part of the EasyQoS policy. Each application
known to the NBAR taxonomy has a default setting for the traffic-class
attribute. Changing the DSCP marking for a traffic-class within the
EasyQoS web-based GUI will cause all applications that have a
traffic-class attribute value matching that traffic-class to be marked
to the new DSCP value within the AVC Profile.

For example, changing the DSCP marking for the Signaling traffic-class
to CS5 will cause all applications which have a traffic-class attribute
value of Signaling to be marked CS5 within the AVC Profile. Note,
however, that the AVC Profile on WLC platforms can only hold 32
applications. Any applications which have a traffic-class attribute
value of Signaling, which do not get provisioned into the AVC Profile,
will be unaffected by the Custom Queuing Profile.

Changing the traffic-class of an application was discussed in the
***Application Registry*** section of the ***APIC-EM and the EasyQoS
Application*** chapter. Changing the traffic-class of an application
will also modify the AVC Profile provisioned to the WLAN as part of the
EasyQoS policy. Changing the traffic-class for an application within the
EasyQoS web-based GUI will cause that application to be marked to a new
DSCP value, corresponding to the new traffic-class within the AVC
profile.

For example, changing the traffic-class attribute value for the SIP
application (which has a default traffic-class attribute value of
Signaling) to VoIP Telephony will cause the SIP application to be marked
EF within the AVC Profile. Again, note that the AVC Profile on WLC
platforms can only hold 32 applications. The network operator may need
to mark the application (SIP in this example) as a Favorite in order to
ensure the application is provisioned into the AVC Profile. Note also,
that changes to the Application Registry are global, and affect all
policies in all policy scopes.

EDCA Profile

For WLCs running AireOS software version 8.3.112 and higher, all EEE
802.11a/n/ac and 802.11b/g/n radios within APs in which at least one
SSID/WLAN is controlled by EasyQoS with Fastlane enabled, are configured
with the Fastlane EDCA profile. This is accomplished via the following
global configuration commands automatically configured by the WLC when
Fastlane is enabled on any WLAN/SSID by EasyQoS.

config advanced 802.11a edca-parameter fastlane

config advanced 802.11b edca-parameter fastlane

For WLCs running AireOS software versions below 8.3.112, all EEE
802.11a/n/ac and 802.11b/g/n radios within APs in which at least one
SSID/WLAN is controlled by EasyQoS are configured with the WMM EDCA
profile. This is accomplished via the following global configuration
commands provisioned by EasyQoS onto the WLC.

config advanced 802.11a edca-parameter wmm-default

config advanced 802.11b edca-parameter wmm-default

The Fastlane EDCA profile is considered to be better optimized for
support of voice and video in current 802.11 media which support
functionality such as frame aggregation.

From the perspective of the web-based graphical user, an example of the
configuration of the EDCA Profile on a radio for Fastlane is as shown in
the figure below.

1. Configuration of the EDCA Profile for Fastlane on a Radio

|image116|

Voice Call Admission Control

All EEE 802.11a/n/ac and 802.11b/g/n radios within APs, in which at
least one SSID/WLAN is controlled by EasyQoS, are configured for
load-based voice call admission control (CAC). Up to 50% of the
bandwidth is reserved for voice calls and 6% of the allocated bandwidth
reserved for roaming voice clients. Additionally, Expedited Bandwidth is
enabled. This feature pertains only to CCXv5 compliant wireless clients.
It allows such clients to indicate the urgency of a WMM traffic
specifications request to the WLAN. This allows for some additional
bandwidth to be used for emergency voice calls when usage exceeds 50%.
CAC is enabled via the following global configuration commands, either
provisioned onto the WLC by EasyQoS, or configured by the WLC
automatically when Fastlane is enabled on any WLAN/SSID:

config 802.11a cac voice acm enable

config 802.11b cac voice acm enable

config 802.11a cac voice max-bandwidth 50

config 802.11b cac voice max-bandwidth 50

config 802.11a cac voice roam-bandwidth 6

config 802.11b cac voice roam-bandwidth 6

config 802.11a exp-bwreq enable

config 802.11b exp-bwreq enable

From the perspective of the web-based graphical user, the configuration
of voice CAC per radio is as shown in the figure below.

1. Configuration of Voice CAC per Radio

|image117|

Enabling WLANs and Radios

After the EasyQoS Static QoS configuration has been applied, the
following commands—either provisioned onto the WLC by EasyQoS or
configured by the WLC as a result of enabling Fastlane on any
WLAN/SSID—re-enable all WLANs and radios on the AireOS WLC.

config wlan enable all

config 802.11b enable network

config 802.11a enable network

From the perspective of the web-based graphical user, examples of
enabling/disabling the radios and of enabling/disabling WLANs are shown
in the figures below.

1. Enabling / Disabling Radios

|image118|

1. Enabling / Disabling WLANs

|image119|
