IPAM
====

Some thoughts on an IPAM infrastructure.

Registry - Top level of heirarchy.  inheritance - addresses assigned from RIR
to LIR to end-user - RIR->LIR heirarchy needed?

Family - Second level (v4/v6) is this needed, or is it an attribute rather than
an object type? I lean towards object type because different families need
different data structures and policies.

Networks - The meat of it all. is:publishable

If each network has a registry entry - registry entry could indicate if changes
need to be pushed upstream.  If object is delegated by customer/peer no need to
push updates to RIR.

Generation of SWIP/RPSL objects.

Owners - End user information.  Ability to sync to external database...
is:publishable

Flag on is:publishable - on change to generate updated objects.
