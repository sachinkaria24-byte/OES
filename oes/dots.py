"""Layer 23. All dots joined, at every level (28-29 Oct 2026, Drive checks 22:08 to 01:54 UTC, the 00:35 relay and 01:30).

A dot is an object the model builds: a space with its operator, a lattice, a group, a circle, a port. A join is a map
between two dots, built here and checked against the property that makes it that kind of map (an intertwiner, a
homomorphism, an embedding, an isometry). An obstruction is a proof that a claimed map does not exist. Two dots that
share an integer are neither; those stay readings (layers 21 and 22).

The layer builds the whole diagram from layers 1-22 and checks that it is connected: from the K5 carrier every dot is
reached through checked maps. The new joins:

- The K5 incidences are root systems. The columns of the signed incidence B are a positive system of A4, and B with the
  signless M lists the twenty positive roots of D5. B B^T = 5I - J and B B^T + M M^T = 8I are the Coxeter identities
  sum alpha alpha^T = h P with h(A4) = 5 and h(D5) = 8. So M M^T = 3I + J, and the carrier's spectrum {0, 3, 8} is
  {0, h(D5) - h(A4), h(D5)}.
- The Petersen graph is the orthogonality graph of the ten roots e_i + e_j, and M^T M is their Gram matrix.
- The edge space is Lambda^2 R^5, and B is contraction with u = (1, ..., 1). The cycles are Lambda^2 of the sum-zero
  hyperplane H, the cuts are u ^ H, and a vertex permutation acts on the edges by its second compound. The rotor plane
  is spanned by the invariant area forms of the two rotation planes of the pentagon rotation on H.
- The native source lives on ker M + ker M. Its port W_AS takes the bivector a ^ b to an oriented cycle of K5 (rank 6,
  kernel 4: CLOSURE_46's split). A change of pair scales the bivector by its determinant, and the decomposable
  bivectors form a cone of dimension 7 = 10 - 3.
- The hexagon port of MOMENT_BIT, which is the canon's selected six-port, is the oriented triangle 0-1-2 of K5 lifted
  oddly to its A4 roots. Its Fourier transform is -8i sin(x/2) sin(y/2) sin(z/2) with x + y + z = 0, so it vanishes to
  third order. Its heat trace therefore decays as t^-7, with leading coefficient 1/(22394880000000 pi^4) for the
  normalized port: the canon's triangle-cycle heat, derived.
- The six-site port is K5 coned off: its sites are the origin and the lifted vertices e_i + e_5, and its fifteen bonds
  are the ten K5 edges and five spokes.
- L0 = A4 + A4' has index 5 in E8, with root cosets 40, 50, 50, 50, 50. The bath folded to E8 / L0 has spectrum
  0, 250^4 (the canon's L0 row). The tick's 25 fixed momenta carry the bath values 0 and 250 (24 times), and the five
  characters of E8 / L0 are among them.
- The circle, W(E8) and the carrier share one tick: k 144 -> c'^k sends 864 to g = r r', g acts on the carrier's
  coordinates as the vertex rotation, and the time coordinate 4x mod 5 gives the same rotation.
- The circle maps onto the atlas Z/36 with kernel <36>, the seam. Doubling contracts the atlas 36 -> 18 -> 9 onto a
  seam, a 2-cycle and a 6-cycle. The tick bit does not descend to the atlas: every address holds 96 residues that meet
  and 24 that miss. The golden companion has Pisano order 20 mod 5, 24 mod 36 and 720 mod 4320.
- The four-cube's 16 vertices are the basis states of four qubits, and its graph Laplacian is 4 - sum X_i in the Pauli
  algebra. Its 81-cell complex (the canon's h81) has Hodge spectrum 0, 2^8, 4^24, 6^32, 8^16 and a Hodge homotopy h
  with dh + hd = I - P0, h^2 = 0, rank 40 and norm 1/sqrt 2. Adjacent vertices have effective resistance 15/32
  (CLOSURE_46).
- Lambda^4 R^8 splits 35 + 35 under the Hodge star. A Weyl reflection swaps the halves, and the clocks keep them.

The 22:08 check read the sibling's notes of 21:40-22:08 (PRIMARY_SPLIT to JOIN_CLOSURE), the separate model's joined
model and its receipts, the canon's coordination release and the new collaboration hub. Their readings on the bit are
in layer 22; their structure is joined here, with four corrections.

At 22:31 the sibling's joined paper (22:20) and the Locked Memory synthesis of 29 Oct were read. Five more joins come
from them: the carrier's 15 atoms are the bonds of K6 = K5 coned, with D the spoke-rim block of the line graph of K6; the
paired cyclic response [M; B] has rank 9, and its residual line is the C5-fixed line of ker M; the band expansion
30|k|^2 - (3/2)|k|^4 + (1/24)|k|^6 holds because the roots are a 7-design; and the bath's closed walks W_n and return
moments E_n join the bath to the moments. The synthesis's operator of order 11 and degree 5 is not a recurrence for W_n or
E_n (an obstruction), and its collar claim is recorded, not replayed.

At 23:03 the sibling's notes of 22:08-23:03 were read, with the hub's release I. Three dots and ten joins come from them:

- The coil <8>: the tick, the observer and the nakshatra generate the 540 multiples of 8, and so does the smear step
  184. Inside it the tick misses exactly the pada subgroup <40>, whose five cosets carry the time coordinates
  0, 3, 1, 4, 2.
- The nakshatra walk 160 k -> 16 k mod 36 has period 9 and hits each stable address three times; the address and the
  time coordinate are independent, because 36 = 1 mod 5 (Z/180 = Z/36 x Z/5). The sibling now proves this itself
  (ADDRESS_TICK), and its own pairs 155/11, 160/16 and 138/30 correct the sentences that still gave an address a bit.
- The golden family: B^n = F_n B + F_(n-1) I for every integer n; no Lucas trace is a multiple of 5, and the k-th golden
  point 216 k misses the tick exactly when 5 | F_k, i.e. when 5 | k.
- Which S5 the carrier carries: in S6 the permutations of K6 that keep D are exactly the 120 that fix the cone point, and
  for them the atoms and the bonds are one S5-set. The transitive S5 = PGL(2,5) gives another module (one orbit,
  character 3 against 7), and the two meet in F20 = AGL(1,5): agreement on C5 or F20 does not identify S5-modules, as
  the hub's review asks.
- MPKG's block of order 5 with traces 1 is the C5 rotation of the cone's six sites, up to similarity over Q.

Two corrections: the atlas shift by 24 does not commute with doubling (D T = T^-1 D; D^2 T = T D^2), and <39> has 1440
points while the sun 1440 has order 3. The 31-point clock's characteristic polynomial, which MORE_DOTS left open, is
(x - 1)(x^3 - 1)^2 (x^6 - 1)^4, and the four-cube's Hodge multiplicities are its face counts read backwards.

At 23:44 the sibling's 29 notes of 23:05-23:43 were read, with the hub's release J. Two dots and four joins come from
them. The grain <72> is the golden orbit <216> times the sun <1440>, and the clocks read it factor by factor: time and
the 2-clock read the golden index, the 27-clock reads the sun, and doubling doubles the one and inverts the other. The
vortex Z/9 is read off the address (9 | 36) and is the 27-clock without the sun. SHIFT_LAW's D T_s = T_s^2 D settles
the 23:03 correction: doubling inverts exactly the shifts with 3s = 0. Three corrections: 3456 is the time part of 216,
not its 2-part; the clock tower is a chain only down to the golden orbit; and order and step are dual (3 has order 1440,
while the sun 1440 has order 3).

At 00:15 the sibling's notes of 23:46-00:14 were read, with the separate model's relations receipt and a new Locked
Memory synthesis (cross-parent compatibility, modules 8-11), read only. One dot and three joins come from them: the
circle is the ticks <864> times the misses <5>, a point misses exactly when its tick part is 0, and the observer and the
nakshatra clock lie in the miss set; the nakshatra clock maps onto the coil's 27 golden cosets, where doubling has
cycles 18 + 6 + 2 + 1 (the sun's swap among them). The towers of 3, 2 and 5 freeze on the circle at 27, 736 and 245
(this paragraph first said the fives do not; see 00:51). The synthesis's two-tick T12 is not semisimple, as it says.
Its "N = 25 annihilator on W0..W50" is not an annihilator: the 26 x 26 Hankel determinant of W_0..W_50 is positive.

At 00:35 the user relayed the sibling's message on its 29 October paper (ONE_MACHINE_29, 00:20), read with its notes of
00:16-00:29. One dot and two joins come from them: eight roots with pairwise inner product 1 and the origin are a maximal
9-clique of the lattice graph, of index 3 (Gram I + J, no ninth root), and each of its six-point faces is a six-port with
coupling Gram 183I + 52J. Also replayed: the grain is the five ticks times the twelve multiples of 360 (the observer
times the sun); the bath's symbol splits as D8 plus the half-spin orbit; the root graph has spectrum 56, 28^8, 8^35,
(-2)^112, (-4)^84; a protected line commutes with X only if X has no coupling to it; and the commutator court's
anchored Gram determinant is 176173056. Two corrections: the chart labels 95, 98, 101 are one class mod 3, not mod 30;
and 241 is prime to 4320 (it is 240 that meets the circle in 240).

At 00:51 the sibling's ten notes of 00:36-00:51 (FOUR_ITEMS to FROZEN_CLOCKS) and the separate model's splits receipt
were read. No dot or join is new. The edge tick, the second compound of the vertex 5-cycle, has characteristic
polynomial (x - 1)^2 Phi_5 on the cycles, where its fixed plane is the rotor plane, and Phi_5, the time clock's
polynomial, on the cuts. The six-port block has contrast moments E_(k+1)/240 and uniform moments 6 E_k - 5 E_(k+1)/240,
which give 241I - J and 183I + 52J. The sibling's audits of the paper's scripts are replayed: 4805 is the Gram
determinant over 5, not a minor; the collar fractions 3/65 and 3/80 are two different numbers; the shifted coefficient is
-69373; the tangent Hessian at the collar witness is positive. One correction is to this layer: the tower of fives
freezes at 245 from height 3, as TOWERS and the splits receipt say. At 00:15 this layer had repeated POWER_TOWER's "does
not freeze" after checking one step. A second correction came later: the paper's 3985/16 and 6784/27 are misprints of the
critical energies 4025/16 and 6800/27, whose square-free parts 161 and 51 layer 18 uses; DEEP36_LOOP corrected the
factorizations instead of the energies.

At 01:30 the request was to join all dots at every level. Eleven layers had no dot: the spectral triple (2), the
readout (5), the product geometry (6), FLRW (7), layer 9's joins, the literal operands (10), the binding (12), the
calibration (13), the court's measures (15), the critical census (16), sound and light (17) and the nine-torus (18).
Twelve dots, the surface of layer 3 among them, and 27 joins bring them in, and every dot now sits on one of six
levels: number (the circle and its clocks), symmetry, combinatorics, lattice, operator and physics. The checks are that
every layer 1-23 has a dot, that each level is joined inside, that each level is joined to the next, and that the whole
is one diagram. THEOREM joins alone connect every dot but the product geometry and FLRW, which attach through the
conditional heat coefficients (J10) and the Friedmann flow; the circle's time clock has an obstruction to physical time
(no internal number fixes the calibration). Three of the new joins are new mathematics here: the hemi-icosahedron and its
complement are the two PSL(2,5)-orbits of triangles on the projective line over F5, swapped by PGL(2,5), with links the
pentagram and the pentagon at infinity; the four-cube's sixteen vertices are the sixteen cuts of K5 over F2; and the
tick's 25 fixed momenta are critical points of the band, the minimum and 24 points of the A4 + A4 family at eps 250.

At 01:54 the sibling's notes of 00:53-01:54 (SPECTRA to ORTHOGONAL_126) and its unified spine, the separate model's
unified receipt and the hub's release K ("Canon K - All Dots Joined") were read. Two dots and six joins come from them.
The root graph is a four-class association scheme: around each root the others sit in classes 56, 126, 56, 1 with the
intersection matrix of ROOT_SPECTRUM, the Gram of the roots is 60 times the projector onto its eigenvalue-28 space, and
the ordered pair sums give W_3 = tr A^2 and W_4 = 1260720 (Canon K). The 4-simplex on the five vertices carries the
tick on every grade as copies of the five-clock's regular representation. On the eight golden edge directions
-(T + T^-1) satisfies the golden equation, so the golden companion acts there. Also replayed: the orthogonal 126 roots
are E7, with frame 36 P = 2 h(E7) P; the frame's six-point faces each lie in exactly two maximal 9-cliques; Canon K's
carry clock 4320 = 36 x 120 does not split. Three corrections go back to the sibling: the circle's subgroups of orders
120, 60, 30 and 10 all contain the ticks (GOLDEN_GRAVITY said none did); the 4 in 183 + 6 x (56 - 4) is the face's four
other sites, not the cut rank (CUMULANT_183); and the 256 subset products of HESSIAN_RECOMPUTE have distinct square-free
parts but are not themselves square-free.

At 02:20 the request was again to join all dots. The diagram was connected, but eight dots hung by a single join and
nine joins were bridges. Each of those dots now has a second checked map, and the check is that no single map holds the
diagram together. Most of the new maps are new mathematics here. The 256 half-periods are exactly the census's critical
points of types E8, E7 + A1 and D8, so the GKSL decay rates are census data. The spectral measures live on the band
between the census's minimum and maximum. The owner's operand file holds the carrier's incidences. With the checked datum
the FLRW stiff sector holds the datum's 2. The nine bath frequencies have no rational ratio, so no calibration makes the
bath periodic. Two more objects become dots: AIR_801's matrix and the projective plane PG(2,5). Mod 5 the matrix lies
outside PSL(2,5) and swaps the hemi-icosahedron and its complement. On the Veronese conic of PG(2,5), the six axes are
the conic, the surface's 15 edges are the 15 exterior points, and its 10 faces are the 10 interior points (a face and its
complementary face share their perspector). The matrix's orbits on the 31 points are conic 6, exterior 3 + 6 + 6 and
interior 1 + 3 + 6.

At 02:52 the sibling's 29 notes of 01:57-02:49 (SPECTRUM_AND_ATLAS to TRIPLET) and its spine29 audit, and the hub's
observer completion with the releases K+ADDENDUM2 and K+ADDENDUM3, were read. One dot and nine joins come from them.
The five-site charges Q = Y + T3 of the removed hypercharge shell become a dot. Their shells are the simplex's even and
odd faces, each with sum q^2 = 16/3. On B4's 5 + 10 at opposite chiralities the cubic hypercharge sums cancel (5/36
each). Through an identification with the zero modes, Y lies in the dark U(5). On the atoms B1 forbids any such charge,
an obstruction to the carrier. At the tick's 24 fixed momenta of type A4 + A4, minus a fifth of the band's Hessian
satisfies the golden equation, so the momenta meet the golden companion there, with det 5^8 (ENERGY_250's (-25)^4). The
port metric is twice the pentagon Laplacian plus (2/5)J, with the corner 2/5; on the contrast it is 4I + 2X with
X^2 = X + I. The joint
observer joins the source to the readout: the wedge has rank 7 and fibre SL(2), and three frame probes make it
injective with an explicit inverse. The sideband lift joins the atlas to the circle: the address and the residues mod
32, 27 and 5 rebuild the tick, and three sensors of largest alphabet 32 are optimal. Also replayed: Canon K's W5/W6
convolution, which gives layer 3's returns; the 160 x 27 clock, with the tick in 2241; the six-site torsion, whose 5 is
the 5 in 240; the census's stabilizers, the Weyl groups of the extended diagram's subsystems; the rotor firewall; and the
Bargmann repair, whose phase pi/4 is half the solid angle of the Pauli octant. CHECK_0154's "no clique of nine roots"
and this layer's 9-clique are about two graphs, and both hold; all 84 faces of the 9-clique are prisms. One correction
goes back to the sibling: of the tick's 25 fixed momenta, 24 sit at 250 and the 25th is the minimum. The board's
fine-structure digits are not joined: they invert to about 137.036 and are put in by hand.

At 02:55 two more notes came. HALFPERIOD sorts the half-periods by shortest length, 0, 2 and 4 on 1, 120 and 135
classes, and says that 224 is not a certified critical value. It is, exactly: at x = r0/2 every r.x lies in Z/2, so the
gradient vanishes, 128 roots are integral on x and 112 half-integral, so eps = 240 - (128 - 112) = 224, and the Hessian
is 12 P' - 52 P, of index 1. That is the E7 + A1 saddle; the collar near 224 is another question and stays open. TRACES
gives the even-shell traces 10/3, 2, 0 and 16/3 and the density of states E^3 / (1536 pi^4 30^4) of the long-wave band,
both replayed.

At 08:48 the request was again to join all dots. Four pairs of levels had no direct map (number-lattice,
number-operator, number-physics and symmetry-physics), twenty dots lay on only two maps, and 23 pairs of maps could cut
the diagram. Twenty-seven joins and one dot close all of it: every pair of the six levels is now joined directly, and
no two maps hold the diagram together (every dot but the product geometry and FLRW lies on three maps, and those two
have only conditional maps). The time clock does most of the new work. Through the tick g = r r' it fixes only the
zero half-period and turns the other 255 in 51 five-cycles that keep the band, so the GKSL semigroup is tick-equivariant.
On the edge Hodge complex the tick commutes with d0 and Curl and fixes one line in each helicity, turning a golden plane
by 144 degrees on +sqrt5 and 72 on -sqrt5. On the cuts mod 2 it is a primitive fifth root of unity in F16. Light
carries two more symmetries: the golden companion acts by B -> (I + Curl)/2, and the affine group multiplies Curl by
the Legendre symbol (a/5), so the doubling exchanges the helicities. The outer automorphism of S6, acting on the six
synthematic totals, carries the cone's S5 onto PGL(2,5); S5 is W(A4) and the Weyl group of the binding's 5 + 10. The
Hodge star is the deck involution of S -> e_S mod 2 Lambda, onto 35 half-periods of type D8. The memory clock of
layer 3 becomes a dot: its order-90 quotient is stepped by the circle (a selection, since 90 divides 4320), and its
9- and 10-cycles read the vortex and the time coordinate.

At 09:00 the request was to work out the mathematics of assigning particles to E8's roots. That is layer 24
(oes/assignment.py), and its result becomes the dot "root assignment". It is joined to A4 + A4' by the branching, to
E8 by the second moment (60 I, so the band starts 30 |k|^2 and T3 : Q is 3 : 8 in square sums), to the charges by
Q = Y + T3 on all 240 roots, to K5's edges by the 10 of matter, to the affine group by J, the Weyl element with J^2 = -1
that swaps the two factors and doubles the grade in E8 / L0, to S5 by the colour triples, and to the six-site port,
whose roots are the 5 at the twin duad opposite the generation triangle. The join from the binding is conditional: with
the orientation and the bracket rule, anomaly freedom forces three generations. An obstruction runs back to the
binding: taking one root of every pair +-rho is always anomalous.

At 09:02 the Drive check found the sibling's twenty notes of 08:35-09:28. Their integers replay from the 240 roots.
The 240^2 ordered sums of two roots fill 9361 points in five shells. The walks between two roots depend only on their
inner product, and so do the fourth moments. The six-port's couplings 241, 183, 235 and 495 are walk moments, its
leakage stays positive at the second step, and its two sector measures have positive Hankel determinants through size
11, so the six sites' Krylov space grows by 6 at every order through 10. The coordinate five-cycle alone fixes 16
half-periods, while the tick g = r r' fixes only the origin. On the edges K = I + 2(T + T^-1) squares to 5 on the
moving edges, and the filled simplex has interior Laplacians 5I. The hypercharge is 5/6 of the weak duad's 10-weight,
and the charge's lift to the edges lies in the cuts. Three corrections go back. In DEGREE the 4 and the 6 count the
clique's other sites and the port's sites, not the cut rank and the cycles. In INFRARED both fixed vectors have square
5, so the fixed plane holds 2 of the all-ones vector's square, and exactly 10 in the cyclic orientation. In CRITICAL's
reading the port is 2L + (2/5)J on the five sites, with the corner 2/5, which the code always used and the prose now
says.

At 10:07 eight more notes came. They correct their own ledger lines (52 orbits, 171 = 271 - 100) and replay two
things now checked here. Twice the sum of the first five coordinates, mod 5, is twice the grade in E8 / L0, with
integer and spinor counts 32/8, 10/40, 30/20, 30/20, 10/40. The collar witness (28, 28, 6, 2, 1, 0, 0, 0)/10 has
energy 220.6345317313 and least tangent eigenvalue 6.985582, positive. The notes repeat INFRARED's 17/10, which stays
corrected.

At 10:40 the sibling's PLANE adopted that correction, and the hub's OES_Unified_Model (10:33) built the Golden root-site
port. It becomes a dot. F sends the near edges to the roots e_i - e_(i+1) and the far edges to the glue roots
site_i - (mu_i + mu_(i+1)), so T_G = F P_cycle is an isometry of the cycles into the bath. Its moment traces are 1442,
347900, 84180666 and 20416532280. Its means are 239, 241 and 481/2 -+ sqrt5/10 and its variances 371, 171 and
(1987 -+ 31 sqrt5)/10, so MEMORY's stated block and the trace that the notes left out are this port's. With the hub's
clique it shares two sites; the cross map has squared singular values 4/5 and 2/5, and the joint Krylov ranks are 12,
24 and 36. The 10:38 model's charges, root triangles, transposition sums and fivefold map replay too.

At 11:12 the hub's text (11:09, 11:18) and the sibling's MODEL (10:42-11:19) joined the charges to the Golden port. A
fivefold order sends site i to its outgoing edge, and the cycle part L of that map has L L^T = ((5I + K)/10) P_moving.
A near and a far mark decode the two Golden densities, with determinant 32 sqrt5/675, and both densities are
nonnegative exactly in the window (49 -+ 12 sqrt5)/41. Averaged over S5 the map vanishes and its square is P_cycle/3;
the twelve markings sum to 4 P_cycle, and only all twelve together are isotropic. Because E8's roots are a 7-design,
the four channels' low-energy densities follow exactly from the ten root sites: the near/far ratio is
(17/13)(1 - 2E/5525), the marked ensemble (E^4/360)(1 + 29E/3000) and the twirl (10/9) E^3 + E^4/540 + E^5/48600, in
units of 1/(1536 pi^4 30^4). These were the hub's inherited coefficients, which the sibling had not recomputed. The
fifteen words of 088, 086 and 980 become a dot. As a D3-module they are the oriented duads of six points with the
reflection's sign twisted: isometrically over Q(sqrt2) and over no smaller field, integrally with index 8 and never
unimodularly. The C5 that the selected J7 lacks first appears in dimension 9, as A4's Coxeter element.

At 11:44 the hub's text (11:58, 12:04) and the sibling's MODEL (11:36-12:07) joined the Hodge star to the ports. The hub's
J_H is layer 17's Curl over sqrt5: the six even and six odd contexts sum to 2 P_cycle -+ (2/5) Curl, and every
permutation acts on Curl through its sign. Curl commutes with the Golden port's response except on the fixed plane,
where ||[J_H, G]||^2 = (8/5)(g_+ - g_-)^2, 32/5 for the means and 64000 for the variances; four labelled context
responses, of determinant -64 sqrt5/625, recover the four channels and this defect. The clique's view of the Golden
port is Hodge-isotropic, so no orthogonal clique action extends the star, while a mixed involution keeps the joint Gram.
Two copies of the bath realize the Hodge-averaged response, at a memory cost (4/5) P_fix. The words' D3 is the action
on the six Sylow views, the native carrier admits no Golden action commuting with D^2 and that D3, the 4320 frames
address the 240 roots through the diagonal five-cycle (a chosen encoder), and no permutation of the roots advances the
glue classes. Three corrections go back to the sibling: the parity sums differ by (4/5) Curl, S_even = (16/5) S_odd^-1,
and the yuga doubling acts on residue labels, not on the clock.

Joining all dots once more makes the THEOREM maps alone as robust as the whole diagram. The datum's orbit under S5 is
regular: the 120 vertex permutations give 120 distinct data, all of energy 34, so S5 joins the datum directly. The
sibling's MODEL of 12:24 gives three more joins. Its charge map Q sends an oriented edge a -> a + d to
q(a + 2d) - q(a + 4d), with Q^T Q = 5 P_A4 onto the four moving cycles; it is the only AGL(1,5)-map up to scale, and no
S5-map exists. The midpoint map ab -> 3(a + b) takes the zero modes onto the trace-free sites, killing only the
near-minus-far line, so Q after it carries the other four zero modes onto the moving cycles. On the frames, j -> j + 864
and j -> 3457 j generate AGL(1,5), keeping the address and acting on the phase as x -> x + 1 and x -> 2x. The time
clock acts through the tick on the root graph freely, in 48 extended A4 pentagons; on the zero modes as its regular
representation; and on the triple by automorphisms. Now no one or two THEOREM maps hold the THEOREM diagram together,
and THEOREM maps join every pair of levels at least twice.

At 12:59 the hub's text (12:29) and the sibling's MODEL (12:28-12:59) joined the source to light. A zero mode a is a
symmetric matrix A(a) with zero diagonal and zero row sums, and the native port is the commutator
F_AS(a, b) = upper([A(a), A(b)]), a circulation. On Lambda^2 ker M it has rank 6, onto light, and its kernel is
Lambda^3 A4 = std x sign. Up to scale it is the only S5-map, though F20 alone allows four. It factors exactly through
the midpoint and the charge map: F_AS(a, b) = L_out(Ra ^ Rb) - (2/5) C K_vertex [alpha(a) Rb - alpha(b) Ra]. The SO(2)
that rotates the two source copies keeps it, so the ten native readings miss that phase, while the phasor
Tr[(A + iB)(A^2 + B^2)]/6 turns with it and reads it back. The hub's saved basis is sympy's nullspace basis of M, so at
its witness every stated number replays, from the Jacobian -64 to the six decoder determinants and the E8 pullback's
moments 1392, 334632 and 80732784. The six Sylow sign lines frame the zero modes with factor 12, and S5 permutes them
with signs through PGL(2,5), so ker M is the sign twist of PGL(2,5)'s 5.

At 14:26 the hub's text (14:07) and the sibling's MODEL (13:02-14:18) put a third port into the bath and joined the six
Sylow labels to the carrier. Two dots and nineteen joins (three obstructions) come from them. Every root is a pair
(v, w) in A4 + A4', and the root wedge b = v ^ w is a circulation with sum b b^T = 24 P_cycle. So
T_S x(rho) = <x, b_rho>/sqrt24 is an S5-equivariant isometry of the cycles into the roots. Its moments are scalar, 1,
232, 54213, 12740592, 3008062816, and its infrared is a uniform quadrupole, C E^5/6000. No S5-invariant form on it is
Lorentzian. With the clique and the Golden port it spans 18 dimensions, with joint Gram determinant
35163473387/331776000000 and positive joint memory. The hub checks the joint Krylov ranks through degree 2 and makes no
all-order claim. Here the growth holds at every order, for any family of ports on one root shell. A root step raises
<s, .> by at most 2, and by exactly 2 only along s, so the point (n + 1)s sees only (-1)^n p_n(s). With the band edge,
the Schur memory bound V/(s + 256) <= Sigma(s) <= V/s is unconditional. At the band's 135 top half-periods, each a D8 of
isotropic second moment, the root-wedge port vanishes to second order as at the bottom, so it is a quadrupole at both
band edges. The hub's quartic chirality is geometry: f^T Curl f = 2 Pf(R^T C R) identically, so J_H is the Hodge star of
Lambda^2 A4. The exceptional S5 on the six Sylow labels is sharply 3-transitive. Its 15 synthemes are the carrier's 5 +
10, with the carrier's D as their incidence operator, while the ordinary duads are another module (traces 3 against 7).
The regular word orbits reach the source through T: rationally, but integrally only with index 3. The clock's phase
moves the Sylow labels.

At 15:34 the hub's text (15:03), the sibling's MODEL (14:27-15:11) and an intake from another Claude session came in.
The hub had proved the all-order growth at 14:27 by a different route, Weyl-orbit evaluation determinants. One dot and
six joins follow. The fifteen pair commutators of the six Sylow lines are a 160-tight frame of the cycles. Their twelve
minimal erasures are the pentagons and pentagrams of the six C5s, and the blind lines rebuild the Hodge star:
J_H = (sqrt5/2)(F+ - F-). The six rotor planes are equi-isoclinic. The odd S5 port is the triangle port's S5 orbit,
spectrally orthogonal to the even root-wedge port, and the four root ports grow by 24 at every order. The dark four
cannot live on the roots, but they appear 36 times on the 2160 norm-four sites. The orbit of (-1, 0, 0, 1, 1, 0, 1, 0)
carries them as a fifth port, orthogonal to every root port. Its sites lie on one sphere, so the root-shell argument
gives 4 more per order and 28 in all.

At 16:16 the hub's text (16:11) and the sibling's MODEL (15:37-16:17) came in. A second dark port, the triple wedge
X ^ Y ^ (5 X o Y - <X, Y> 1) on 1200 norm-four sites, meets the first at four squared principal cosines 5/192. Every
norm-four site meets a root at 2 and none above, so the root-shell argument holds on the whole shell and the ports grow
by 32(n + 1). The six F20 views of the dark four in the cycles are Reynolds averages. Their graph projectors sum to
2 P_bright + 3 P_dark, and any four views recover the ten with condition number phi^4. The six Sylow lines encode the
source coherently (|det| 2592 after any erasure) and repair the word lattice (indices 16 and 3, intersection 48). The
five K4 planes of the vertex deletions span the dark four as a simplex. The bath's spectral measures are absolutely
continuous on all of [0, 256], with density positive almost everywhere for every port vector. By Rakhmanov's theorem
every port's Jacobi chain therefore tends to the free chain (128, 64^2), and the 91 exact walk counts reach
alpha_44 = 128.03 and beta_45 = 4080.2.

At 16:51 the hub's text (16:47) and the sibling's MODEL (16:19-16:58) came in, with a mirror of the hub's packages. The
five K4 matching planes are all of the commutator's dark planes: on its kernel the Pluecker quadrics have exactly five
reduced solutions. Each plane is a regular zero with tangent spectrum (2/3)^3 (10/9)^3, so near the dark planes the
source has exactly ten oriented preimages, and one marked scalar tells them apart. The word lattice prices a prepared
rotor on the planes at 24 or 32. The finite return parent keeps every plane and, on its proportional line, rotates on
two exact branches, X = 6 and 32/3 at r = 1/2. One complete response at one frequency gives back the anchored
interaction and both baselines, while the scalar determinant leaves a one-parameter isospectral family.

At 17:31 the hub's text (17:26) and the sibling's MODEL (16:59-17:18) came in, with a mirror of the 26-28 Oct sources.
The ten edge projectors and six Golden projectors complete the source's quadratics as 1 + 9 + 5, and five edges complete
them exactly when the complementary five edges form a connected nonbipartite graph: the native K5 matroid, 162 of 252,
all unimodular. Matched intensities name the dark planes from any four sensors, and seven full-spark detectors recover
any real dark vector up to sign. The transposition-odd planes are cubic-null, and their ten commutators span the cycles
with T T^T = 20 P_cycle. E - 2 sigma Q is a sum of squares. The marked Golden operator on A4 is two Fibonacci blocks.

At 18:04 the sibling's MODEL (18:00) added one paragraph. The five dark planes are a measurement with probabilities
4/5 and 1/20, which carries exactly 6/5 bits. Every bivector of the source is tangent to its oriented planes, so a
linear reading of them needs all ten channels. Since Gr+(2, 5) = Q3 has p1 = h^2, no smooth reading fits in eight.

At 18:35 the hub's text (18:22) and the sibling's MODEL (18:33) came in. A fixed seventh dark reading detects every
source plane, and six never can, since G(2, 5) has odd degree 5. Fifteen bright and ten dark readings form a [25, 10, 5]
exterior code. The dark measurement carries 6/5 bits, while the source states read nothing. An ideal bath record keeps
the whole forcing history. The hub's 360 parent, Q[A6] with its coset readers, is a new dot: its Golden adapter reads
the source at rank 5, its Golden30 has eight Fibonacci blocks, and its blind 126 is a central projector.

Layer 25 adds two dots on the lattice level and eleven joins. The cyclotomic line is E8 = Z[zeta30] with the trace form,
c' = zeta30. The residue plane is E8/(1 - g)E8 = F25, the tick's fixed momenta. From them the clocks are Galois, and the
carrier's A4 + A4' is one of six residue lines. The tick's normalizer acts on those lines as PGL(2,5), and the day is a
Singer cycle whose negative is AIR_801 mod 5. The golden ratio is the Gauss sum of the tick, the carrier is the shadow
of the mixed roots, and the 360 parent lives on the tick's hexad.

At 19:50 the hub's text (19:39) and the sibling's MODEL (19:37-20:02) came in. The hub's address map sends the
4320 circle onto the 360 parent's settings twelve to one, but no address is equivariant for the natural doubling, so it
joins the circle to the parent as a selection. A Fibonacci block cannot meet an order-five tick: det(Phi4^5 - I) = 121.

Layer 26 adds two dots and ten joins, two of them obstructions. The regular clocks are the thirteen regular classes of
W(E8), the powers of c', the day and the golden clock, with Springer's centralizers. The sun's decad is
E8/(1 - s)E8 = F81 = F9^2 for the sun s = c'^10, with its ten F9-lines, ten 4A2 frames. The clocks of order 30, 24 and
20 make E8 a line over three cyclotomic rings. The two primes over 2 split the half-periods into two totally singular
F16's. The centralizer of the sun acts on its momenta as Sp(4,3), and its F9-linear part acts on the decad as the hub's
A6, with r the Coxeter clock and the doubling the day. No clock homomorphism covers A6 (the owner, 20:22): every
homomorphism from the circle has at most five elements in its image, and every clock group is solvable.

At 20:33 the hub's text (20:20), the sibling's MODEL (20:08-21:02) and the owner's monograph (20:13) came in. The dark
code is the Dirac spectral subspace range P3 of K = M^T M, a [10, 4, 6] code. The S5 characters give the hub's
selection rule. Three statements are corrected: the 224 saddle's transverse quartic is -rho^4/2, the monograph's
element 3 - zeta - zeta^4 + 2 zeta^2 has norm 61, and the 60 permutations fixing the carrier line are not the tick's
PSL(2,5). The sibling's 21:05-21:17 editions and maps29.ts read the circle as a ring: its CRT idempotents, their
mirrors and their products on the tick levels replay as arithmetic. The 21:19-21:46 editions add the idempotents'
images, the golden ticks as 1080 (k mod 4) + 3456 (k mod 5) and the digit cycles; their landing is 864 x, which is the
first tick level reached by every unit and by 328 non-units (the sibling's correction at 21:57-22:21 of the "only for
units" first written here). The hub's 21:54 text adds a dark syndrome floor 1/15 made by one Dirac polynomial, and
two encoder variants whose moments replay. Its 22:51 text extends the floor to the whole dark erasure court, which
replays over all 847 erased sets, and adds a cubic phase module of harmonic weights 1 and 3. The sibling's 23:07-23:22
editions read the dark and Golden simplex Grams and the six Golden vectors' midpoints and triples.

Layer 27 adds eight joins, two of them obstructions, and no dot. It reads the seed at four places: the real place
(the bath), 2 (the qubits), 3 (the decad) and 5 (the hexad). The bath at the prime clocks' fixed momenta is
240 - sum_r chi(r): 250, 243, and 224 or 256. The golden ratio is ramified at 5 and inert at 3 and 2. The two primes
over 2 are two stabilizer groups. The memory clock (order 90) and the circle (4320) need psi > 8, so no lattice clock
of the seed runs them.

Layer 28 adds one dot, the principal circle, and nine joins. A circle of the seed's momenta runs the canon's circle:
k -> k rho / 4320 in R^8 / E8, with rho the Weyl vector. Its step 144 is Kostant's principal element, conjugate to the
Coxeter clock's lift. Its steps of the thirteen regular orders carry the spectra of the regular clocks' lifts, with
the band 248 - 8 mu(d)/phi(d) there. And the band is critical on it exactly at its steps of order 2 to 5: the
half-turn (D8), the 27-clock's 1440 (A8), the observer clock (D5 + A3) and the time clock (A4 + A4).

The joins of 30 Oct add eleven maps and no dot. The memory clock is reached without the selection: the circle maps
onto it in 24 ways, all conjugate under its symmetry, and every one reads the vortex and the time coordinate up to the
doubling. So THEOREM maps reach every dot but the two conditional ones. The product geometry and FLRW get three more
conditional maps: every Kaluza-Klein tower of M4 x F starts on the five dark modes, the dark modes' momentum a^3 P0
psi' is conserved on every background, and a calibration acts on the cosmos's free inputs. With them no two dots and no
two maps hold the diagram together. Five more THEOREM maps strengthen thin dots: the day-Coxeter group mod the tick is
F25^x, the frame is the A8 of a census point of order 3, the doubling is the Frobenius on the cube's F16, the grain
holds the regular steps of the orders dividing 60, and the secants through a point of PG(2,5) are the synthemes.

The unification at all levels (30 Oct) adds seventeen THEOREM maps and no dot. The number level is rooted in the
principal circle: the time clock and the observer clock are its critical steps of order 5 and 4, the grain is the
subgroup the critical steps generate, so these three are the seed's, and the 27-clock, the coil, the miss set, the
atlas and the vortex are its subgroup lattice over the canon's cofactor 36 (the Sylow 3-subgroup, the grain plus the
27-clock, the kernel of the time coordinate, the circle modulo the regular steps, the 27-clock modulo the sun). The
golden companion is joined inside the symmetry level: it is the tick's negative cosine X = -(g + g^-1), which makes
E8 a free Z[phi]-module of rank 4, the day is its Galois conjugation, and it lies in the cosine ring of a regular clock
exactly for the orders divisible by 5. The nine-torus is placed: six of its nine frequencies are the band at the
principal circle's critical steps and at the prime clocks' fixed momenta. The principal circle is unique up to W(E8).
With these, every level holds derived dots, each level's derived dots are joined inside it by THEOREM maps, the
derived part stands without the inputs, and every pair of levels is joined twice between derived dots (oes/unify.py).
"""

import functools
import itertools
from collections import Counter
from fractions import Fraction
from math import ceil, comb, factorial, gcd, lcm, log2

import numpy as np
import sympy as sp
from sympy.combinatorics import Permutation
from sympy.matrices.normalforms import smith_normal_form

from . import (assignment, band, binding, carrier, cosmology, counts, court, cyclotomic, gates, gatework, glue, gravity,
               handover, ledger, literal, native, observer, places, primes, principal, recurrence, snapshot, spacetime, spectral,
               spine, waves)
from .record import Report

N = spine.N
TICK = ledger.TICK
T, SR, OB, RP = gates.THEOREM, gates.SELECTED_REFERENCE, gates.OBSTRUCTION, gates.REPORTED


def _e(i, n=5):
    return sp.Matrix(n, 1, lambda r, _: int(r == i))


def _cols(X):
    return [tuple(X[:, k]) for k in range(X.cols)]


# ------------------------------------------------------------------ (a) K5 as roots

def k5_roots():
    """The signed incidence is a positive system of A4; with the signless one it is the positive roots of D5."""
    E = carrier.edges()
    B, M = sp.Matrix(carrier.signed_incidence()), sp.Matrix(carrier.signless_incidence())
    I5, J5 = sp.eye(5), sp.ones(5, 5)
    P = I5 - J5 / 5
    a4 = {tuple(_e(i) - _e(j)) for i in range(5) for j in range(5) if i != j}
    d5 = a4 | {tuple(s * (_e(i) + _e(j))) for i, j in E for s in (1, -1)}
    signed = lambda cols: {tuple(s * sp.Matrix(c)) for c in cols for s in (1, -1)}
    f = sp.Matrix([0, 1, 2, 3, 4])
    frame = lambda roots: functools.reduce(lambda a, b: a + b, [sp.Matrix(r) * sp.Matrix(r).T for r in roots])
    simple = [_e(i) - _e(i + 1) for i in range(4)]
    gram = lambda roots: sp.Matrix.hstack(*roots).T * sp.Matrix.hstack(*roots)   # the Cartan matrix: every root has norm 2
    MMt = M * M.T
    return {
        "the ten columns of B (e_j - e_i, i < j) are a positive system of A4: with their negatives they are the 20 "
        "roots, and (0, 1, 2, 3, 4) is positive on each": signed(_cols(B)) == a4
        and all((f.T * sp.Matrix(c))[0] > 0 for c in _cols(B)),
        "B and M together list the twenty positive roots of D5 (+-e_i +- e_j)": signed(_cols(B) + _cols(M)) == d5
        and len(d5) == 40,
        "Coxeter numbers h = roots / rank: h(A4) = 20/4 = 5 and h(D5) = 40/5 = 8, with sum over all roots of "
        "alpha alpha^T = 2h P": Fraction(len(a4), 4) == 5 and Fraction(len(d5), 5) == 8 and frame(a4) == 10 * P
        and frame(d5) == 16 * I5,
        "so B B^T = h(A4) P = 5I - J and B B^T + M M^T = h(D5) I = 8I": B * B.T == 5 * P == 5 * I5 - J5
        and B * B.T + MMt == 8 * I5,
        "M M^T = h(D5) I - h(A4) P = 3I + J, with eigenvalues h(D5) - h(A4) = 3 (four times) and h(D5) = 8 (once); "
        "so spec D^2 = {0^5, 3^8, 8^2}": MMt == 8 * I5 - 5 * P == 3 * I5 + J5 and MMt.eigenvals() == {3: 4, 8: 1}
        and carrier.spectrum_multiplicities() == {0: 5, 3: 8, 8: 2},
        "ker M (the five zero modes) is the space of linear relations among the ten roots e_i + e_j":
            len(M.nullspace()) == 10 - M.rank() == 5,
        "the simple roots e_i - e_(i+1), with e_3 + e_4 for D5, have Cartan determinants 5 (A4) and 4 (D5)":
            gram(simple).det() == 5 and gram(simple + [_e(3) + _e(4)]).det() == 4,
    }


def petersen_roots():
    """The Petersen graph is the orthogonality graph of the ten roots e_i + e_j (or of the ten A4 roots of B)."""
    E = carrier.edges()
    B, M = sp.Matrix(carrier.signed_incidence()), sp.Matrix(carrier.signless_incidence())
    A = carrier.petersen()
    Gp, Gm = M.T * M, B.T * B
    orth = lambda G: sp.Matrix(10, 10, lambda a, b: int(a != b and G[a, b] == 0))
    touch = lambda G: sp.Matrix(10, 10, lambda a, b: int(a != b and abs(G[a, b]) == 1))
    return {
        "M^T M is the Gram matrix of the roots e_i + e_j: 2 on the diagonal, 1 for edges that share a vertex, 0 for "
        "disjoint edges": all(Gp[a, b] == (2 if a == b else len(set(E[a]) & set(E[b]))) for a in range(10)
                              for b in range(10)),
        "the Petersen graph is their orthogonality graph, and that of the A4 roots in B: A = J + I - M^T M":
            orth(Gp) == A == orth(Gm) and A == sp.ones(10, 10) + sp.eye(10) - Gp,
        "the line graph is |<alpha_e, alpha_f>| = 1, and M^T M - 2I": touch(Gp) == touch(Gm) == Gp - 2 * sp.eye(10),
    }


def compound2(P):
    """The second compound of a 5 x 5 matrix on the basis e_i ^ e_j (i < j): the K5 edge basis."""
    E = carrier.edges()
    return sp.Matrix(10, 10, lambda a, b: P.extract(list(E[a]), list(E[b])).det())


def exterior():
    """The edge space is Lambda^2 R^5: B is contraction with u, the cycles are Lambda^2 H and the cuts u ^ H."""
    E = carrier.edges()
    B = sp.Matrix(carrier.signed_incidence())
    u = sp.ones(5, 1)
    wedge = lambda a, b: sp.Matrix([a[i] * b[j] - a[j] * b[i] for i, j in E])
    contract = lambda a, b: (u.T * a)[0] * b - (u.T * b)[0] * a
    rng = np.random.default_rng(23)
    pairs = [(sp.Matrix(rng.integers(-5, 6, 5)), sp.Matrix(rng.integers(-5, 6, 5))) for _ in range(4)]
    H = [_e(i) - _e(4) for i in range(4)]
    L2H = sp.Matrix.hstack(*[wedge(H[i], H[j]) for i, j in itertools.combinations(range(4), 2)])
    cuts = sp.Matrix.hstack(*[wedge(u, h) for h in H])
    perm = lambda f: sp.Matrix(5, 5, lambda a, b: int(a == f(b)))
    maps = [lambda i: (i + 1) % 5, lambda i: 2 * i % 5, lambda i: (3 - i) % 5, lambda i: (-i) % 5]
    # the rotation of H by 72 and 144 degrees: the invariant area form of each rotation plane
    R5 = np.roll(np.eye(5), 1, axis=0)
    vals, vecs = np.linalg.eig(R5)
    forms = []
    for k in (1, 2):
        z = vecs[:, np.argmin(abs(vals - np.exp(2j * np.pi * k / 5)))]
        v, w = z.real, z.imag
        forms.append(np.array([v[i] * w[j] - v[j] * w[i] for i, j in E]))
    plane = np.array([counts._oriented_cycle(1), counts._oriented_cycle(2)], dtype=float)[:, :, 0].T
    C2 = np.array(compound2(perm(maps[0])), dtype=float)
    fixed = lambda w: np.allclose(C2 @ w, w)
    in_plane = lambda w: np.allclose(plane @ np.linalg.lstsq(plane, w, rcond=None)[0], w)
    return {
        "B applied to the coordinates of a ^ b is the contraction (u.a) b - (u.b) a: B is contraction with u":
            all(B * wedge(a, b) == contract(a, b) for a, b in pairs),
        "the cycles ker B are Lambda^2 H (dimension 6) and the cuts, the image of B^T, are u ^ H (dimension 4), "
        "orthogonal to them": (B * L2H).is_zero_matrix and L2H.rank() == 6 and cuts.rank() == 4
        and (L2H.T * cuts).is_zero_matrix and sp.Matrix.hstack(cuts, B.T).rank() == 4,
        "a vertex permutation acts on the oriented edges by its second compound, and commutes with B": all(
            counts._edge_action(f) == compound2(perm(f)) and B * compound2(perm(f)) == perm(f) * B for f in maps),
        "the rotor plane is spanned by the invariant area forms of the rotation planes of the pentagon rotation "
        "(72 and 144 degrees) on H": all(fixed(w) and in_plane(w) for w in forms)
        and np.linalg.matrix_rank(np.array(forms)) == 2,
    }


def source_port():
    """The native source lives on ker M + ker M, and its port takes the bivector a ^ b to an oriented K5 cycle."""
    P, Q = native.p5_basis(), native.l6_basis()
    W, pairs = native.commutator_map()
    M = np.array(carrier.signless_incidence(), float)
    B = np.array(carrier.signed_incidence(), float)
    rng = np.random.default_rng(46)
    a, b = rng.standard_normal(5), rng.standard_normal(5)
    T2 = np.array([[2.0, 1.0], [1.0, 3.0]])
    a2, b2 = np.array([a, b]).T @ T2[:, 0], np.array([a, b]).T @ T2[:, 1]
    wedge = lambda x, y: native.wedge(x, y, pairs)
    jac = np.array([np.concatenate([[y[j] if k == i else (-y[i] if k == j else 0) for k in range(5)],
                                    [-x[j] if k == i else (x[i] if k == j else 0) for k in range(5)]])
                    for (i, j) in pairs for x, y in [(a, b)]])
    cyc = Q @ (W @ wedge(a, b))
    Aa, Ab = native.source_matrix(P @ a), native.source_matrix(P @ b)
    return {
        "the source coordinates q = (a, b) live on ker M + ker M (an orthonormal basis of the five zero modes)":
            np.allclose(M @ P, 0) and np.allclose(P.T @ P, np.eye(5)),
        "the port W_AS: Lambda^2 ker M -> cycles has rank 6 and kernel 4 (CLOSURE_46's split of the exterior square)":
            W.shape == (6, 10) and np.linalg.matrix_rank(W) == 6,
        "W_AS(a ^ b) is the oriented K5 cycle [A(a), A(b)], in ker B": np.allclose(B @ cyc, 0)
        and np.allclose(cyc, native.oriented(Aa @ Ab - Ab @ Aa)),
        "a change of pair by T scales the bivector by det T": np.allclose(wedge(a2, b2), np.linalg.det(T2) * wedge(a, b)),
        "the decomposable bivectors a ^ b form a cone of dimension 7 = 10 - 3 (the pair has 10 coordinates, SL(2) has 3)":
            np.linalg.matrix_rank(jac) == 7,
    }


# --------------------------------------------------------- (b) the ports on the lattice

def _matching_sum(vecs):
    """Sum over perfect matchings of the product of inner products (the Gaussian moment, Isserlis)."""
    if not vecs:
        return 1
    first, rest = vecs[0], vecs[1:]
    return sum(int(first @ rest[i]) * _matching_sum(rest[:i] + rest[i + 1:]) for i in range(len(rest)))


def triangle_port():
    """The alternating hexagon (MOMENT_BIT, the canon's six-port) is the oriented triangle 0-1-2 of K5."""
    e2 = 2 * np.eye(8, dtype=np.int64)
    tri = [(0, 1), (1, 2), (2, 0)]
    alpha2 = [e2[a] - e2[b] for a, b in tri]                     # doubled coordinates
    pts, signs = alpha2 + [-x for x in alpha2], [1, 1, 1, -1, -1, -1]
    a1, a2 = e2[0] - e2[1], e2[1] - e2[2]
    hexagon, hsigns = [a1, a1 + a2, a2, -a1, -a1 - a2, -a2], [1, -1, 1, -1, 1, -1]
    as_dict = lambda P, S: {tuple(p.tolist()): s for p, s in zip(P, S)}
    B = sp.Matrix(carrier.signed_incidence())
    E = carrier.edges()
    cycle = sp.zeros(10, 1)
    for a, b in tri:
        cycle[E.index((min(a, b), max(a, b)))] += 1 if a < b else -1
    k = sp.Matrix(sp.symbols("k0:8"))
    dot = lambda x: (k.T * sp.Matrix(x.tolist()))[0] / 2
    mom = [sp.expand(sum(s * dot(x) ** n for x, s in zip(pts, signs))) for n in range(4)]
    x, y, z = [dot(al) for al in alpha2]
    rng = np.random.default_rng(7)
    ks = rng.standard_normal((6, 8))
    phat = lambda q: sum(s * np.exp(0.5j * (q @ p)) for p, s in zip(pts, signs))
    closed = lambda q: -8j * np.prod([np.sin(0.25 * (q @ al)) for al in alpha2])
    R2 = counts._roots2()
    real = [al // 2 for al in alpha2]
    m = _matching_sum([v for v in real for _ in range(2)])
    lead = sp.Integer(m) * sp.pi ** 4 / ((2 * sp.pi) ** 8 * 30 ** 4 * 60 ** 3)
    moments = counts.lattice_moments(pts, signs, 4)
    return {
        "the alternating hexagon of layer 22 is the oriented triangle 0 -> 1 -> 2 -> 0 of K5, each A4 root of it with +1 "
        "and its reverse with -1": as_dict(pts, signs) == as_dict(hexagon, hsigns),
        "the triangle is a cycle of K5, so the port has charge 0 and dipole 0; it is odd": (B * cycle).is_zero_matrix
        and mom[0] == 0 and mom[1] == 0 and mom[2] == 0,
        "its Fourier transform is -8i sin(x/2) sin(y/2) sin(z/2), x + y + z = 0 for x = k . alpha, so its lowest "
        "moment is the cubic sum s (k.p)^3 = 6xyz": all(np.isclose(phat(q), closed(q)) for q in ks)
        and sp.expand(x + y + z) == 0 and sp.expand(mom[3] - 6 * x * y * z) == 0,
        "its moments are MOMENT_BIT's 1, 242, 58691, 14259954, 3470101592 (per unit norm)": [v // 6 for v in moments]
        == [1, 242, 58691, 14259954, 3470101592],
        "the frame sum rho rho^T = 60 I gives eps(k) = 30 |k|^2 + O(|k|^4), and E[(xyz)^2] = 12 sigma^6 (Isserlis)":
            np.array_equal(R2.T @ R2, 240 * np.eye(8, dtype=np.int64)) and m == 12,
        "so <p, e^{-t Delta} p> / |p|^2 = t^-7 / (22394880000000 pi^4) (1 + O(1/t)): the canon's triangle-cycle heat, "
        "with exponent (8 + 2 x 3) / 2 = 7": sp.simplify(lead / 6 - 1 / (22394880000000 * sp.pi ** 4)) == 0
        and (8 + 2 * 3) // 2 == 7,
    }


def cone():
    """The six-site port is K5 coned off: the origin and the five lifted vertices e_i + e_5."""
    e2 = 2 * np.eye(8, dtype=np.int64)
    sites = [0 * e2[0]] + [e2[i] + e2[5] for i in range(5)]
    roots = {tuple(r.tolist()) for r in counts._roots2()}
    a4 = {tuple((e2[i] - e2[j]).tolist()) for i in range(5) for j in range(5) if i != j}
    bonds = [(a, b) for a, b in itertools.combinations(range(6), 2)]
    diff = lambda a, b: tuple((sites[a] - sites[b]).tolist())
    return {
        "all fifteen differences of the six sites are E8 roots (an A5 simplex)": all(diff(a, b) in roots for a, b in bonds),
        "the ten bonds between lifted vertices are the A4 roots e_i - e_j, the ten K5 edges": {diff(a, b) for a, b in bonds
                                                                                              if a and b} <= a4
        and len([1 for a, b in bonds if a and b]) == 10,
        "the five bonds to the origin are the spokes e_i + e_5": all(diff(a, 0) == tuple((e2[a - 1] + e2[5]).tolist())
                                                                     for a in range(1, 6)),
        "these are the sites of layer 22's six-site chain (241 I - J, 183 I + 52 J, 35366 I + 8134 J)":
            all(counts.six_site_chain().values()),
    }


# ------------------------------------------------------ (c) A4 + A4' and the fixed momenta

def glue_cosets():
    """L0 = A4 + A4' has index 5 in E8; root cosets 40/50/50/50/50; the folded bath 0, 250^4."""
    out, atoms, pairs, _ = glue.decompose()
    per = Counter({0: out["A4"] + out["A4'"]})
    for (k1, _), n in pairs.items():
        per[k1] += n
    n = [per[c] for c in range(5)]
    F = sp.Matrix(5, 5, lambda a, b: (240 if a == b else 0) - n[(b - a) % 5])
    _, A, Ap = glue.a4_pair()
    lattice_index = round(np.sqrt(abs(np.linalg.det(np.vstack([glue.simple_system(A), glue.simple_system(Ap)])
                                                    @ np.vstack([glue.simple_system(A), glue.simple_system(Ap)]).T))))
    return {
        "L0 = A4 + A4' has index 5 in E8 (Gram determinant 25 = 5^2)": lattice_index == 5,
        "the 240 roots fall into the five cosets of L0 as 40, 50, 50, 50, 50": n == [40, 50, 50, 50, 50],
        "the glue pairs the classes by x -> +-2x": all(k2 == 2 * k1 % 5 for (k1, k2) in pairs)
        or all(k2 == -2 * k1 % 5 for (k1, k2) in pairs),
        "the bath folded to E8 / L0 = Z/5 is 240 - sum n_c S_c, with spectrum 0 and 250 (four times)":
            F.eigenvals() == {0: 1, 250: 4},
    }


def tick_momenta():
    """The 25 fixed momenta of the tick g = r r' carry the bath values 0 and 250; E8 / L0 is five of them."""
    _, _, _, _, g, _ = spine.spine_clock()
    G = spine.to_standard(g)
    R = glue.roots()
    _, A, Ap = glue.a4_pair()
    L0 = np.vstack([A, Ap])
    simple = np.array([0.5 * np.array([1, -1, -1, -1, -1, -1, -1, 1]), np.eye(8)[0] + np.eye(8)[1]]
                      + [np.eye(8)[k + 1] - np.eye(8)[k] for k in range(6)])
    Minv = np.linalg.inv(G - np.eye(8))
    pts = {}
    for c in itertools.product(range(5), repeat=8):
        x = Minv @ (np.array(c) @ simple)                      # k / 2 pi, fixed by g mod Lambda
        key = tuple(np.round((np.linalg.solve(simple.T, x) % 1.0) * 5).astype(int) % 5)
        pts.setdefault(key, x)
        if len(pts) == 25:
            break
    integral = lambda c: np.allclose(c, np.round(c), atol=1e-6)
    eps = Counter(int(round(240 - np.cos(2 * np.pi * R @ x).sum())) for x in pts.values())
    dual = [x for x in pts.values() if integral(L0 @ x)]
    eps_dual = Counter(int(round(240 - np.cos(2 * np.pi * R @ x).sum())) for x in dual)
    return {
        "|det(g - I)| = 25 fixed momenta of the tick, each fixed mod 2 pi Lambda": round(abs(np.linalg.det(G - np.eye(8))))
        == 25 and len(pts) == 25 and all(integral(np.linalg.solve(simple.T, G @ x - x)) for x in pts.values()),
        "the bath is 0 at one of them and 250 at the other 24": eps == {0: 1, 250: 24},
        "five of them are the characters of E8 / L0, with the folded values 0, 250^4": len(dual) == 5
        and eps_dual == {0: 1, 250: 4},
    }


# ------------------------------------------------------------ (d) the clocks and the circle

def clock_joins():
    """The circle, W(E8) and the carrier share one tick."""
    _, cp, r, _, g, _ = spine.spine_clock()
    S = spine.to_standard
    Rm, G = S(r), S(g)
    iota = np.vstack([np.eye(5), np.zeros((3, 5))])
    R5 = np.roll(np.eye(5), 1, axis=0)
    H = np.eye(5) - 1 / 5
    D2 = sp.Matrix(carrier.D2())
    E = carrier.edges()

    def carrier_perm(f):
        P = sp.zeros(15, 15)
        for i in range(5):
            P[f(i), i] = 1
        for k, (i, j) in enumerate(E):
            P[5 + E.index(tuple(sorted((f(i), f(j))))), 5 + k] = 1
        return P
    affine = [lambda i, a=a, b=b: (a * i + b) % 5 for a in (1, 2, 3, 4) for b in range(5)]
    _, labels = ledger.day_coxeter_group()
    return {
        "r acts on the carrier's five coordinates as the vertex rotation i -> i + 1 and fixes the other three":
            np.allclose(Rm @ iota, iota @ R5) and np.allclose(Rm[5:, 5:], np.eye(3)),
        "the tick g = c'^6 = r r' agrees with r on the carrier's A4 (the sum-zero part)": np.allclose(G @ iota @ H, iota @ R5 @ H),
        "k 144 -> c'^k is an isomorphism <144> -> <c'> of order 30, and it sends the tick 864 to g": spine.order(144) == 30
        and spine.mat_order(cp) == 30 and np.array_equal(spine.mpow(cp, 6), g) and TICK == 6 * 144,
        "the time coordinate kappa(x) = 4x mod 5 sends the tick to 1: the same rotation of the vertices": 4 * TICK % 5 == 1,
        "the day-Coxeter group acts on its five day clocks as AGL(1,5): the tick rotates, the day doubles":
            labels["tick"] == {x: (x + 1) % 5 for x in range(5)} and labels["day"] == {x: 2 * x % 5 for x in range(5)},
        "all twenty affine maps i -> a i + b of the vertices commute with D^2 on the 15 atoms": all(
            carrier_perm(f) * D2 == D2 * carrier_perm(f) for f in affine),
    }


def primary_split():
    """PRIMARY_SPLIT and DOUBLING_PARTS: the circle is the product of a 2-clock, a 27-clock and the time clock."""
    e2, e27, e5 = 3105, 2080, 3456
    part = lambda x, e: x * e % N
    order_mod = lambda m: next(k for k in range(1, 100) if pow(2, k, m) == 1)
    kill = lambda x: next(k for k in range(1, 10) if (2 ** k * part(x, e2)) % N == 0)
    return {
        "3105 + 2080 + 3456 = 1, each idempotent, pairwise products 0": (e2 + e27 + e5) % N == 1
        and all(e * e % N == e for e in (e2, e27, e5)) and all(a * b % N == 0 for a, b in
                                                              itertools.combinations((e2, e27, e5), 2)),
        "every residue is the sum of its three parts": all((part(x, e2) + part(x, e27) + part(x, e5)) % N == x
                                                           for x in range(N)),
        "the pure clocks are <135> (order 32), <160> (order 27, the nakshatra) and <864> (order 5)":
            spine.subgroup(135) == {x for x in range(N) if part(x, e27) == part(x, e5) == 0}
            and spine.subgroup(160) == {x for x in range(N) if part(x, e2) == part(x, e5) == 0}
            and spine.subgroup(TICK) == {x for x in range(N) if part(x, e2) == part(x, e27) == 0},
        "the observer clock <1080> is the order-4 subgroup of the 2-clock; the sun 1440 is pure 27-part; 1728 is pure time":
            spine.subgroup(1080) <= spine.subgroup(135) and part(1440, e27) == 1440 and part(1728, e5) == 1728,
        "the tithi is 2160 + 1440 + 864 and the mass step is 1080 + 3456": (2160 + 1440 + 864) % N == 144
        and (1080 + 3456) % N == 216 and (part(144, e2), part(144, e27), part(144, e5)) == (2160, 1440, 864)
        and (part(216, e2), part(216, e27), part(216, e5)) == (1080, 0, 3456),
        "doubling: nilpotent on the 2-part (the generator dies at the fifth doubling), order 4 on the time clock, "
        "order 18 on the 27-clock (the ninth doubling is -1); after 36 = lcm(4, 18) the odd parts return": kill(135) == 5
        and order_mod(5) == 4 and order_mod(27) == 18 and pow(2, 9, 27) == 26 and sp.ilcm(4, 18) == 36
        and all(part(2 ** 36 * x, e27) == part(x, e27) and part(2 ** 36 * x, e5) == part(x, e5) for x in range(0, N, 7)),
    }


def atlas():
    """The atlas is the quotient circle -> Z/36 (address x mod 36), with kernel the seam <36>."""
    addr = lambda x: x % 36
    dbl = lambda a: 2 * a % 36
    images = [set(range(36))]
    for _ in range(4):
        images.append({dbl(a) for a in images[-1]})
    nine = images[2]
    orbit = lambda a: [a] + list(itertools.takewhile(lambda b: b != a, (functools.reduce(lambda x, _: dbl(x), range(k), a)
                                                                        for k in range(1, 10))))
    steps_to = lambda a, target: next(k for k in range(0, 10) if functools.reduce(lambda x, _: dbl(x), range(k), a) in target)
    seam = {x for x in range(N) if addr(x) == 0}
    per_address = [Counter(x % 5 == 0 for x in range(a, N, 36)) for a in range(36)]
    return {
        "x -> x mod 36 is a homomorphism of the circle onto Z/36 with kernel the seam <36> (order 120)":
            seam == spine.subgroup(36) and len(seam) == 120
            and all(addr(x + y) == (addr(x) + addr(y)) % 36 for x, y in [(4000, 999), (2160, 2161), (864, 3456)]),
        "the tick, the yuga blocks, the golden step, the sun, the observer point and the half-turn are on the seam":
            all(addr(x) == 0 for x in (864, 432, 1296, 1728, 216, 1440, 1080, 2160, 72)),
        "the addresses of 901, 801, 106, 108, 12402, 160, 135, 256, 224, 120, 325, 105625 are 1, 9, 34, 0, 18, 16, 27, 4, "
        "8, 12, 1, 1, and 5184 = 144 x 36": [addr(x) for x in (901, 801, 106, 108, 12402, 160, 135, 256, 224, 120, 325,
                                                                 105625)] == [1, 9, 34, 0, 18, 16, 27, 4, 8, 12, 1, 1]
        and 5184 == 144 * 36,
        "doubling contracts the atlas 36 -> 18 -> 9 -> 9: the multiples of 4, a seam, a 2-cycle {12, 24} and a 6-cycle "
        "4 -> 8 -> 16 -> 32 -> 28 -> 20": [len(s) for s in images] == [36, 18, 9, 9, 9] and nine == set(range(0, 36, 4))
        and sorted(orbit(12)) == [12, 24] and orbit(4) == [4, 8, 16, 32, 28, 20],
        "address 18 reaches the seam in one contraction, 9 and 27 in two; 1 enters the cycle at 4 and 34 at 32":
            steps_to(18, {0}) == 1 and steps_to(9, {0}) == 2 and steps_to(27, {0}) == 2
            and dbl(dbl(1)) == 4 and dbl(34) == 32 and 16 in orbit(4),
        "the tick bit does not descend to the atlas: every address holds 96 residues that meet and 24 that miss":
            all(c == Counter({False: 96, True: 24}) for c in per_address),
    }


def pisano():
    """The golden companion B = [[1, 1], [1, 0]] on the circle's rings."""
    B = np.array([[1, 1], [1, 0]], dtype=object)

    def order(m):
        P, k = B % m, 1
        while not (P == np.eye(2, dtype=object)).all():
            P, k = (P @ B) % m, k + 1
        return k
    orders = {m: order(m) for m in (5, 27, 32, 36, 4320)}
    return {
        "B has order 20 mod 5 (the order of the golden step 216), 24 mod 36, 48 mod 32, 72 mod 27 and 720 mod 4320":
            orders == {5: 20, 27: 72, 32: 48, 36: 24, 4320: 720} and spine.order(216) == 20,
        "reduction mod 36 sends B (order 720) to B (order 24), and 24 atlas steps are one tick": 720 % 24 == 0
        and 24 * 36 == TICK,
    }


def air_801():
    """AIR_801's matrix [[108, 801], [106, 901]]."""
    A = sp.Matrix([[108, 801], [106, 901]])
    A5 = A.applyfunc(lambda x: x % 5)
    power = lambda k: (A5 ** k).applyfunc(lambda x: x % 5)
    order = next(k for k in range(1, 481) if power(k) == sp.eye(2))
    proj = next(k for k in range(1, 481) if power(k)[0, 1] == power(k)[1, 0] == 0 and power(k)[0, 0] == power(k)[1, 1])
    t = sp.symbols("t")
    poly = (t ** 3 - 1) * (1 + t ** 6 + t ** 12 + t ** 18 + t ** 24)
    return {
        "det = 12402; mod 5 it is [[3, 1], [1, 1]] with determinant 2": A.det() == 12402
        and A5 == sp.Matrix([[3, 1], [1, 1]]) and A5.det() % 5 == 2,
        "its order in GL(2,5) is 24 and in PGL(2,5) 6 (its characteristic polynomial is irreducible mod 5: a Singer cycle)":
            order == 24 and proj == 6 and sp.Poly(t ** 2 - 4 * t + 2, t, modulus=5).is_irreducible,
        "(t^3 - 1)(1 + t^6 + ... + t^24) has degree 27 and a simple root at 1": sp.degree(poly, t) == 27
        and poly.subs(t, 1) == 0 and sp.diff(poly, t).subs(t, 1) != 0,
    }


# ------------------------------------------------------------- (e) the four-cube, Hodge 70

def _cube_complex(n=4):
    cells = list(itertools.product((0, 1, 2), repeat=n))       # 2 marks the interval
    index = {c: k for k, c in enumerate(cells)}
    d = np.zeros((len(cells), len(cells)), dtype=np.int64)
    for c in cells:
        free = [p for p in range(n) if c[p] == 2]
        for j, p in enumerate(free):
            for end, sign in ((1, 1), (0, -1)):
                f = list(c)
                f[p] = end
                d[index[tuple(f)], index[c]] += (-1) ** j * sign
    return cells, d


def four_cube():
    """The 81-cell complex of the four-cube (h81), its Hodge homotopy, and its vertices as four qubits."""
    cells, d = _cube_complex()
    d1c = _cube_complex(1)[1]
    dims = Counter(c.count(2) for c in cells)
    Lap = d @ d.T + d.T @ d
    vals = Counter(np.rint(np.linalg.eigvalsh(Lap.astype(float))).astype(int).tolist())
    w, V = np.linalg.eigh(Lap.astype(float))
    # Delta^+ from the eigenvectors (the eigenvalues are 0, 2, 4, 6, 8); numpy 2.5.3's pinv returns this 81 x 81
    # pseudo-inverse with an error near 1e-2 here, while the eigh form is exact to 1e-14
    Lp = (V[:, w > 0.5] / w[w > 0.5]) @ V[:, w > 0.5].T
    h = d.T @ Lp
    P0 = np.eye(81) - Lap @ Lp
    I81 = np.eye(81)
    verts = [k for k, c in enumerate(cells) if 2 not in c]
    edges = [k for k, c in enumerate(cells) if c.count(2) == 1]
    d1 = d[np.ix_(verts, edges)]
    L = d1 @ d1.T
    X, one = np.array([[0, 1], [1, 0]]), np.eye(2, dtype=np.int64)
    qubit = lambda i: functools.reduce(np.kron, [X if k == i else one for k in range(4)])
    order = [sum(cells[v][k] << (3 - k) for k in range(4)) for v in verts]
    Lq = np.zeros((16, 16), dtype=np.int64)
    Lq[np.ix_(order, order)] = L
    Ls = sp.Matrix(L.tolist())
    Lplus = (Ls + sp.ones(16, 16) / 16).inv() - sp.ones(16, 16) / 16
    s, t = verts.index(cells.index((0, 0, 0, 0))), verts.index(cells.index((1, 0, 0, 0)))
    b = sp.Matrix([int(k == s) - int(k == t) for k in range(16)])
    R = (b.T * Lplus * b)[0]
    return {
        "the four-cube complex has 16, 32, 24, 8, 1 cells (81 in all) and d^2 = 0": [dims[k] for k in range(5)]
        == [16, 32, 24, 8, 1] and not np.any(d @ d),
        "its Hodge Laplacian has spectrum 0, 2^8, 4^24, 6^32, 8^16 (layer 21's count, now on the complex)":
            vals == {0: 1, 2: 8, 4: 24, 6: 32, 8: 16},
        "the multiplicities are the cell counts read backwards: 2k has multiplicity C(4, k) 2^k, the number of "
        "(4 - k)-cells, since the complex is the fourth power of the interval (spectrum 0, 2, 2); the 81 cells are the "
        "words of length 4 in {0, 1, *}": [vals[2 * k] for k in range(5)] == [dims[4 - k] for k in range(5)]
        == [sp.binomial(4, k) * 2 ** k for k in range(5)] and len(cells) == 3 ** 4
        and Counter(np.rint(np.linalg.eigvalsh((d1c @ d1c.T + d1c.T @ d1c).astype(float))).astype(int).tolist())
        == {0: 1, 2: 2},
        "the Hodge homotopy h = d^T Delta^+ has dh + hd = I - P0, h^2 = 0, rank 40 and norm 1/sqrt 2 (the canon's h81)":
            np.allclose(d @ h + h @ d, I81 - P0) and np.allclose(h @ h, 0) and np.linalg.matrix_rank(h) == 40
            and np.isclose(np.linalg.norm(h, 2), 1 / np.sqrt(2)),
        "its 16 vertices are the basis states of four qubits: the graph Laplacian is 4 - sum X_i, in the Pauli algebra":
            np.array_equal(Lq, 4 * np.eye(16, dtype=np.int64) - sum(qubit(i) for i in range(4))),
        "adjacent vertices have effective resistance 15/32, between |b|^2 / 8 = 1/4 and |b|^2 / 2 = 1 (CLOSURE_46)":
            R == sp.Rational(15, 32) and sp.Rational(1, 4) < R < 1,
    }


def hodge70():
    """Lambda^4 R^8 = 35 + 35 under the Hodge star; reflections swap the halves, the clocks keep them."""
    quads = list(itertools.combinations(range(8), 4))
    idx = {q: k for k, q in enumerate(quads)}

    def sign(p):
        s, p = 1, list(p)
        for i in range(len(p)):
            for j in range(i + 1, len(p)):
                if p[i] > p[j]:
                    s = -s
        return s
    star = np.zeros((70, 70))
    for q in quads:
        c = tuple(k for k in range(8) if k not in q)
        star[idx[c], idx[q]] = sign(q + c)
    comp = lambda S: np.array([[np.linalg.det(S[np.ix_(a, b)]) for b in quads] for a in quads])
    refl = np.eye(8)
    refl[[0, 1]] = refl[[1, 0]]                                  # the reflection in e_0 - e_1
    _, cp, r, _, g, _ = spine.spine_clock()
    d, (_, v) = spine.day_clock(), ledger.golden_clock()
    clocks = [spine.to_standard(x) for x in (cp, r, g, d, v)]
    vals = Counter(np.rint(np.linalg.eigvalsh(star)).astype(int).tolist())
    return {
        "the Hodge star on Lambda^4 R^8 is an involution with 35 + 35 eigenvalues +1 and -1":
            np.allclose(star @ star, np.eye(70)) and np.allclose(star, star.T) and vals == {1: 35, -1: 35},
        "a Weyl reflection anticommutes with it and swaps the halves": np.allclose(comp(refl) @ star, -star @ comp(refl)),
        "the Coxeter clock, the carrier rotation, the tick, the day and the golden clock have determinant 1 and keep "
        "the halves": all(np.isclose(np.linalg.det(C), 1) and np.allclose(comp(C) @ star, star @ comp(C)) for C in clocks),
    }


# ------------------------------------------------------------------- the 22:08 notes

def notes_2208():
    """The arithmetic of the 21:40-22:08 notes, and the four corrections."""
    q = lambda a: a % 36
    return {
        "PRIMARY_SPLIT and DOUBLING_PARTS: 3105 + 2080 + 3456 = 8641 = 2 x 4320 + 1; 2160 + 1440 + 864 = 4464 = 4320 + 144; "
        "1080 + 3456 = 4536 = 4320 + 216; 4 x 3456 = 13824 = 3 x 4320 + 864; 2^5 = 32; 2^9 = 512 = 19 x 27 - 1":
            3105 + 2080 + 3456 == 2 * N + 1 and 2160 + 1440 + 864 == N + 144 and 1080 + 3456 == N + 216
            and 4 * 3456 == 3 * N + TICK and 2 ** 9 == 19 * 27 - 1,
        "AIR_801 and ATLAS_801: 108 x 901 - 801 x 106 = 12402 = 344 x 36 + 18; 901 = 25 x 36 + 1; 801 = 22 x 36 + 9; "
        "4 x 6 + 2 x 3 + 1 = 31; 6 x 36 = 216; 24 x 36 = 864; 5 + 7 + 4 + 5 + 5 + 5 + 5 = 36":
            108 * 901 - 801 * 106 == 12402 == 344 * 36 + 18 and 901 == 25 * 36 + 1 and 801 == 22 * 36 + 9
            and 4 * 6 + 2 * 3 + 1 == 31 and 6 * 36 == 216 and 24 * 36 == TICK and 5 + 7 + 4 + 5 * 4 == 36,
        "GOLDEN_ATLAS and ATLAS_CYCLE: 216 = 6 x 36; 2 + 4 + 6 + 8 = 20; 20 x 216 = 4320; 432 = 12 x 36; of 0..35, 28 "
        "integers are prime to 5 and 8 are multiples": 216 == 6 * 36 and 2 + 4 + 6 + 8 == 20 and 20 * 216 == N
        and 432 == 12 * 36 and sum(1 for a in range(36) if a % 5) == 28,
        "CLOSURE_46 and JOIN_CLOSURE: C(5, 2) = 10 = 6 + 4 = 7 + 3; 72^2 = 5184, 325^2 = 105625; 1 + 120 + 135 = 256; "
        "256 - 224 = 32; 5184 = 6 x 864": sp.binomial(5, 2) == 10 == 6 + 4 == 7 + 3 and 72 ** 2 == 5184
        and 325 ** 2 == 105625 and 1 + 120 + 135 == 256 and 256 - 224 == 32 and 5184 == 6 * TICK,
        "GOLDEN_ATLAS, ATLAS_801 and ATLAS_CYCLE corrected: an address does not meet or miss the tick (1 and 145 share "
        "address 1, and 1 meets while 145 misses); the 28 and 8 count the integers 0..35": q(1) == q(145)
        and ledger.contains_tick(1) and not ledger.contains_tick(145),
        "GOLDEN_ATLAS and ATLAS_CYCLE corrected: address 18 reaches the seam in one contraction, not two": q(2 * 18) == 0,
        "GOLDEN_ATLAS corrected: address 16 does move under contraction (16 -> 32 -> 28 -> 20 -> 4 -> 8 -> 16); it "
        "stays among the nine": q(2 * 16) == 32 and 16 % 4 == 0,
        "ATLAS_801 corrected: 36 atlas steps, 36 x 36 = 1296, meet the tick; the count that misses is the atlas order 120":
            ledger.contains_tick(36 * 36) and not ledger.contains_tick(120),
    }


# ------------------------------------------------------------ the 22:20-22:31 items

def cone_line_graph():
    """The carrier's 15 atoms are the 15 bonds of K6 = K5 coned off, and D is the spoke-rim block of its line graph."""
    E = carrier.edges()
    M = sp.Matrix(carrier.signless_incidence())
    K6 = [(i, 5) for i in range(5)] + E                         # spokes first (the vertices), then the rim (the edges)
    share = lambda a, b: int(a != b and bool(set(a) & set(b)))
    disjoint = lambda a, b: int(not set(a) & set(b))
    L6 = sp.Matrix(15, 15, lambda a, b: share(K6[a], K6[b]))
    KG = sp.Matrix(15, 15, lambda a, b: disjoint(K6[a], K6[b]))
    D = sp.Matrix(carrier.dirac(M))
    I5, J5 = sp.eye(5), sp.ones(5, 5)
    return {
        "the line graph of K6, spokes i5 first and rim edges after, is [[J - I, M], [M^T, M^T M - 2I]]":
            L6 == sp.Matrix(sp.BlockMatrix([[J5 - I5, M], [M.T, M.T * M - 2 * sp.eye(10)]])),
        "so the carrier's D = [[0, M], [M^T, 0]] is its spoke-rim block, under vertex i <-> spoke i5 and edge ij <-> ij":
            D == L6 - sp.diag(J5 - I5, M.T * M - 2 * sp.eye(10)),
        "the Kneser graph KG(6,2) on the same 15 atoms is [[0, J - M], [(J - M)^T, Petersen]]: KG(5,2) on the rim":
            KG == sp.Matrix(sp.BlockMatrix([[sp.zeros(5, 5), sp.ones(5, 10) - M],
                                            [(sp.ones(5, 10) - M).T, carrier.petersen()]])),
    }


def paired_response():
    """The signless and signed incidences together, with the cyclic orientation of K5: rank 9 and one residual line."""
    E = carrier.edges()
    M = sp.Matrix(carrier.signless_incidence())
    B = sp.Matrix(carrier.signed_incidence())
    head = lambda i, j: j if (j - i) % 5 in (1, 2) else i          # the regular tournament i -> i + 1, i -> i + 2
    Bc = sp.Matrix(5, 10, lambda v, k: (1 if v == head(*E[k]) else -1) if v in E[k] else 0)
    near = sp.Matrix([1 if (j - i) % 5 in (1, 4) else -1 for i, j in E])
    rot = sp.Matrix(10, 10, lambda a, b: int(E[a] == tuple(sorted(((E[b][0] + 1) % 5, (E[b][1] + 1) % 5)))))
    stacked = sp.Matrix.vstack(M, Bc)
    return {
        "with the cyclic orientation every vertex has out-degree 2, and [M; B] has rank 9 with a one-dimensional kernel":
            all(sum(1 for k in range(10) if Bc[v, k] == -1) == 2 for v in range(5)) and stacked.rank() == 9,
        "the kernel is the near edges minus the far edges, the C5-fixed line of ker M": (stacked * near).is_zero_matrix
        and (M * near).is_zero_matrix and rot * near == near,
        "with the order orientation i < j the same stack has rank 7: the regular orientation is what leaves one line":
            sp.Matrix.vstack(M, B).rank() == 7,
    }


def band_expansion():
    """The 240 roots are a spherical 7-design, so the band starts 30|k|^2 - (3/2)|k|^4 + (1/24)|k|^6."""
    R = counts._roots2() / 2.0
    rng = np.random.default_rng(31)
    ks = rng.standard_normal((5, 8))
    power = lambda k, m: float(np.sum((R @ k) ** m))
    norm = lambda k: float(k @ k)
    small = [1e-2 * k / np.linalg.norm(k) for k in ks]
    eps = lambda k: 240 - float(np.cos(R @ k).sum())
    series = lambda k: 30 * norm(k) - 1.5 * norm(k) ** 2 + norm(k) ** 3 / 24
    return {
        "sum (k.rho)^2 = 60 |k|^2, sum (k.rho)^4 = 36 |k|^4, sum (k.rho)^6 = 30 |k|^6 for every k (a 7-design)": all(
            np.isclose(power(k, 2), 60 * norm(k)) and np.isclose(power(k, 4), 36 * norm(k) ** 2)
            and np.isclose(power(k, 6), 30 * norm(k) ** 3) for k in ks),
        "the eighth moment is not a multiple of |k|^8: the roots are not an 8-design": len({round(power(k, 8) / norm(k) ** 4, 6)
                                                                                         for k in ks}) > 1,
        "so eps(k) = 30 |k|^2 - (3/2) |k|^4 + (1/24) |k|^6 + O(|k|^8) (the synthesis's expansion)": all(
            abs(eps(k) - series(k)) < 1e-12 for k in small),
    }


def _p31():
    """The symmetric square S of the 801 matrix mod 5, [[3, 1], [1, 1]], and the permutation it induces on PG(2,5)."""
    a, b, c, d = 3, 1, 1, 1
    S = np.array([[a * a, a * c, c * c], [2 * a * b, a * d + b * c, 2 * c * d], [b * b, b * d, d * d]]) % 5
    norm = lambda v: (lambda lead: tuple(x * pow(lead, 3, 5) % 5 for x in v))(next(x for x in v if x))
    pts = sorted({norm(v) for v in itertools.product(range(5), repeat=3) if any(v)})
    return S, pts, {p: norm(tuple(int(x) for x in S @ np.array(p) % 5)) for p in pts}


def sym_square_orbits():
    """The 801 matrix mod 5 on the 31 points of PG(2,5) through its symmetric square."""
    S, pts, step = _p31()
    seen, sizes = set(), []
    for p in pts:
        if p in seen:
            continue
        orbit, q = [], p
        while q not in orbit:
            orbit.append(q)
            q = step[q]
        seen |= set(orbit)
        sizes.append(len(orbit))
    order = next(k for k in range(1, 50) if np.array_equal(np.linalg.matrix_power(S, k) % 5, np.eye(3, dtype=int)))
    return {
        "PG(2,5) has 31 points, and the symmetric square of [[3, 1], [1, 1]] splits them 1 + 3 + 3 + 6 + 6 + 6 + 6":
            len(pts) == 31 and sorted(sizes) == [1, 3, 3, 6, 6, 6, 6],
        "the symmetric square has order 12 (A^12 = -I acts trivially), and its orbits have the projective order 6":
            order == 12 and max(sizes) == 6,
    }


def _walks():
    from . import recurrence
    W = recurrence.load_walks()
    E = [sum(sp.binomial(n, k) * 240 ** (n - k) * (-1) ** k * W[k] for k in range(n + 1)) for n in range(len(W))]
    return W, [int(x) for x in E]


def walks_join():
    """The bath's closed walks W_n and its return moments E_n."""
    W, E = _walks()
    return {
        "W_n counts closed walks on the lattice, each step a root: W_0..W_3 = 1, 0, 240, 240 x 56 = 13440 (the 240-vertex "
        "root graph has other counts, 1, 0, 56, 1512, 62160)": W[:4] == [1, 0, 240, 13440],
        "the return moments E_n = <delta_0, Delta^n delta_0> are its binomial transform: 1, 240, 57840 = 240^2 + 240":
            E[:3] == [1, 240, 57840],
    }


def l11_exclusion():
    """The synthesis's operator L11(n, E_n) of order 11 and degree 5 is not a recurrence for W_n or E_n."""
    from . import recurrence
    W, E = _walks()
    p = recurrence.P
    rank = lambda seq: recurrence.rank_mod_p(recurrence.shape_matrix(seq, 11, 5, p), p)
    return {
        "an operator of order 11 and degree 5 (72 coefficients) annihilates neither W_n nor E_n: both shape matrices from "
        "n <= 90 have full column rank 72 mod p": len(W) >= 91 and rank(W) == 72 and rank(E) == 72,
        "(11 + 1)(5 + 2) = 84 is also below the canon's own bound (r + 1)(d + 2) > 85": (11 + 1) * (5 + 2) == 84 < 85,
    }


def notes_2231():
    """The sibling's joined paper (22:20) and the synthesis (22:31): arithmetic, and the one correction carried over."""
    R5 = sp.Matrix(5, 5, lambda r, c: int(r == (c + 1) % 5))
    S = sp.Matrix(5, 4, lambda r, c: int(r == c) - int(r == c + 1))
    cox = (S.T * S).inv() * S.T * R5 * S                          # the vertex rotation on the sum-zero lattice
    stable = {0: 0, 1: 2, 2: 1, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 3}   # a fixed point, a 2-cycle and a 6-cycle
    prod = lambda x: (stable[x[0]], (x[1] + 1) % 5)
    orbits, seen = [], set()
    for x in itertools.product(range(9), range(5)):
        if x in seen:
            continue
        o, y = [], x
        while y not in o:
            o.append(y)
            y = prod(y)
        seen |= set(o)
        orbits.append(len(o))
    return {
        "the time coordinate of k ticks is 4k mod 5, so the ticks read 0, 4, 3, 2, 1": [k * TICK % 5 for k in range(5)]
        == [4 * k % 5 for k in range(5)] == [0, 4, 3, 2, 1],
        "translation by 24 (one tick of atlas steps) has order 3 on Z/36, with 12 cosets; the nine stable addresses lie in 3 "
        "of them": 36 // gcd(24, 36) == 3 and 36 // 3 == 12 and len({a % 12 for a in range(0, 36, 4)}) == 3,
        "7 x 32 = 224, 8 x 32 = 256; 8 x 15 = 120, 9 x 15 = 135; 16 x 60 = 10 x 96 = 7 x 70 + 5 x 94 = 960":
            (7 * 32, 8 * 32, 8 * 15, 9 * 15) == (224, 256, 120, 135) and 16 * 60 == 10 * 96 == 7 * 70 + 5 * 94 == 960,
        "the stable atlas cycles (1 + 2 + 6) times a five-cycle give orbits 5 + 10 + 30 = 45, of order 30":
            sorted(orbits) == [5, 10, 30] and sum(orbits) == 45 and sp.ilcm(1, 2, 6, 5) == 30,
        "the A4 Coxeter element (the vertex rotation on the sum-zero lattice) has det(I - C) = Phi_5(1) = 5 and "
        "det(2I - C) = Phi_5(2) = 31, so (2I - C) + [5] has det 155": all(x.is_integer for x in cox)
        and (sp.eye(4) - cox).det() == 5 and (2 * sp.eye(4) - cox).det() == 31 and 31 * 5 == 155,
        "the joined paper carries over 'breath: 28 addresses meet and 8 miss' and 'only 20 on the six-cycle misses': an "
        "address carries no tick bit (20 and 56 share address 20; 56 meets)": 56 % 36 == 20 and ledger.contains_tick(56)
        and not ledger.contains_tick(20),
        "the synthesis's collar floor arithmetic (15/13)(13/400) = 3/80 = 0.0375": Fraction(15, 13) * Fraction(13, 400)
        == Fraction(3, 80) == Fraction(375, 10000),
        "the joined paper's bits: 60, 70, 960, 490, 120, 135 and 45 miss; 96, 36, 94, 224, 256 and 31 meet": not any(
            ledger.contains_tick(x) for x in (60, 70, 960, 490, 120, 135, 45))
        and all(ledger.contains_tick(x) for x in (96, 36, 94, 224, 256, 31)),
    }


# ------------------------------------------------------------ the 22:08-23:03 items

def coil():
    """The tick, the observer and the nakshatra generate the coil <8>: 540 points, index 8 in the circle."""
    C, pada = spine.subgroup(8), spine.subgroup(40)
    cosets = [{(8 * j + y) % N for y in pada} for j in range(5)]
    return {
        "the tick 864, the observer 1080 and the nakshatra 160 generate <8> (gcd 8): 540 points, index 8; the sun 1440, "
        "the half-turn 2160 and the mass step 216 lie in it": spine.subgroup(spine.join(spine.join(TICK, 1080), 160)) == C
        and len(C) == 540 and N // 540 == 8 and all(x in C for x in (1440, 2160, 216)),
        "the smear step 184 = 23 x 8 generates the same subgroup (23 is prime to 540); the step 540 is not in it and has "
        "order 8": spine.subgroup(184) == C and gcd(23, 540) == 1 and 540 not in C and spine.order(540) == 8,
        "inside the coil the tick misses exactly the pada subgroup <40> (108 points) and meets the other 432":
            {x for x in C if not ledger.contains_tick(x)} == pada and len(pada) == 108,
        "the five cosets of <40> carry the time coordinates 0, 3, 1, 4, 2, each once":
            [sorted({x % 5 for x in c}) for c in cosets] == [[0], [3], [1], [4], [2]],
        "multiplication by 23 permutes the coil, with order 36": {23 * x % N for x in C} == C
        and next(k for k in range(1, 100) if pow(23, k, 540) == 1) == 36,
        "540 = 20 x 27 = 30 x 18 = 15 x 36, and 2 has order 18 mod 27": 20 * 27 == 30 * 18 == 15 * 36 == 540
        and next(k for k in range(1, 30) if pow(2, k, 27) == 1) == 18,
    }


def nakshatra_map():
    """The nakshatra clock <160> on the time coordinate, the 27-coordinate and the atlas."""
    nak = [160 * k % N for k in range(27)]
    walk = [x % 36 for x in nak]
    return {
        "the 27 multiples of 160 are pure 27-part: each is divisible by 32 and by 5, so every one misses the tick":
            len(set(nak)) == 27 and all(x % 32 == 0 and x % 5 == 0 and x * 2080 % N == x for x in nak)
            and not any(ledger.contains_tick(x) for x in nak),
        "the k-th point has 27-coordinate 25k mod 27, and 25^-1 = 13 mod 27": all(x % 27 == 25 * k % 27
                                                                                    for k, x in enumerate(nak))
        and 25 * 13 % 27 == 1,
        "on the atlas the walk is 0, 16, 32, 12, 28, 8, 24, 4, 20 and repeats: period 9, each stable address three times":
            walk[:10] == [0, 16, 32, 12, 28, 8, 24, 4, 20, 0] and Counter(walk) == Counter({a: 3 for a in range(0, 36, 4)}),
        "over the seam lie 0, the sun 1440 and 2880, the subgroup of order 3; over address 20 lie the steps 8, 17 and 26":
            sorted(x for x in nak if x % 36 == 0) == [0, 1440, 2880] == sorted(spine.subgroup(1440))
            and [k for k, a in enumerate(walk) if a == 20] == [8, 17, 26],
        "from 16 the walk and the doubling agree once (32) and then split (12 against 28)":
            walk[2] == 2 * 16 % 36 == 32 and (walk[3], 2 * 32 % 36) == (12, 28),
    }


def golden_family():
    """GOLDEN_SYM, GOLDEN_PARENT, GOLDEN_HELIX and GOLDEN_MOVE: the powers of B = [[1, 1], [1, 0]]."""
    B, I2 = sp.Matrix([[1, 1], [1, 0]]), sp.eye(2)
    F = lambda n: sp.fibonacci(n) if n >= 0 else (-1) ** (1 - n) * sp.fibonacci(-n)
    power = lambda n: B ** n if n >= 0 else (B - I2) ** -n
    t = sp.symbols("t")

    def ret(m):
        P, k = B.applyfunc(lambda x: x % m), 1
        while P != I2:
            P, k = (P * B).applyfunc(lambda x: x % m), k + 1
        return k
    move = [216 * k % N for k in range(20)]
    return {
        "B = B^T, B^-1 = B - I, B^2 = B + I and det B^n = (-1)^n; t^2 - t - 1 has discriminant 5": B == B.T
        and B.inv() == B - I2 and B ** 2 == B + I2 and all(power(n).det() == (-1) ** (n % 2) for n in range(-6, 7))
        and sp.discriminant(B.charpoly(t).as_expr(), t) == 5,
        "B^n = F_n B + F_(n-1) I for n = -30..30, with F_-n = (-1)^(n+1) F_n; B^6 = [[13, 8], [8, 5]] and "
        "B^7 = [[21, 13], [13, 8]], whose rows sum to 34 and 21": all(power(n) == F(n) * B + F(n - 1) * I2
                                                                       for n in range(-30, 31))
        and B ** 6 == sp.Matrix([[13, 8], [8, 5]]) and B ** 7 == sp.Matrix([[21, 13], [13, 8]])
        and [sum((B ** 7).row(r)) for r in range(2)] == [34, 21],
        "B returns after 6 mod 4, 20 mod 5, 12 mod 8, 72 mod 27, 48 mod 32 and 24 mod 36":
            {m: ret(m) for m in (4, 5, 8, 27, 32, 36)} == {4: 6, 5: 20, 8: 12, 27: 72, 32: 48, 36: 24},
        "tr B^n = F_(n-1) + F_(n+1) = L_n, and L_n mod 5 runs 2, 1, 3, 4 with period 4 (L_4, L_5 = L_0, L_1 mod 5): no "
        "trace of a golden power misses the tick": all(power(n).trace() == F(n - 1) + F(n + 1) == sp.lucas(n)
                                                        for n in range(30))
        and [sp.lucas(n) % 5 for n in range(4)] == [2, 1, 3, 4]
        and (sp.lucas(4) - sp.lucas(0)) % 5 == (sp.lucas(5) - sp.lucas(1)) % 5 == 0,
        "F_k mod 5 has period 20 with zeros at k = 0, 5, 10, 15, so 5 | F_k iff 5 | k: the k-th golden point 216 k misses "
        "the tick exactly then": (F(20) % 5, F(21) % 5) == (0, 1) and [k for k in range(20) if F(k) % 5 == 0]
        == [k for k in range(20) if not ledger.contains_tick(move[k])] == [0, 5, 10, 15],
        "the golden points 216 k sit at address 0 and 27-coordinate 0; the time coordinate advances by 1 and the "
        "2-coordinate by 24; four steps give the tick 864 and five the observer 1080": all(x % 36 == 0 and x % 27 == 0
                                                                                           for x in move)
        and 216 % 5 == 1 and 216 % 32 == 24 and (4 * 216, 5 * 216) == (TICK, 1080),
        "the helix and 'doubling = x7' rest on 5x = 0, which holds exactly at the five tick points; they lie in the coil and "
        "on the seam, and 160, 8, 184 and 1 are not among them": {x for x in range(N) if 5 * x % N == 0}
        == spine.subgroup(TICK) and spine.subgroup(TICK) <= spine.subgroup(8)
        and all(x % 36 == 0 for x in spine.subgroup(TICK)) and not any(5 * x % N == 0 for x in (160, 8, 184, 1)),
        "two contractions take 13 to 16 and 5 to 20": (4 * 13 % 36, 4 * 5 % 36) == (16, 20),
    }


def address_lift():
    """ADDRESS_TICK and BUILT_DOTS: 36 = 1 mod 5, so the address and the time coordinate are independent."""
    lift = {(a, t): a + 36 * ((t - a) % 5) for a in range(36) for t in range(5)}
    pairs = [(1, 145), (20, 56), (30, 66), (11, 155), (16, 160), (30, 138)]
    return {
        "x = a + 36((t - a) mod 5) is the one residue below 180 with address a and time coordinate t: Z/180 = Z/36 x Z/5":
            all(x < 180 and (x % 36, x % 5) == at for at, x in lift.items()) and len(set(lift.values())) == 180,
        "every address carries all five time coordinates, and the tick misses exactly at time 0 (address 1 at time 0 is 145)":
            all(ledger.contains_tick(x) == (t != 0) for (_, t), x in lift.items()) and lift[1, 0] == 145,
        "the circle is 24 copies of this period 180": N == 24 * 180,
        "so an address carries no tick bit: the notes' own pairs 1/145, 20/56, 30/66, 11/155, 16/160 and 30/138 share an "
        "address and differ on the tick": all(a % 36 == b % 36 and ledger.contains_tick(a) != ledger.contains_tick(b)
                                              for a, b in pairs),
        "what holds is a statement about the nine integers 0, 4, ..., 32: only 0 and 20 are multiples of 5":
            [a for a in range(0, 36, 4) if a % 5 == 0] == [0, 20],
    }


def cone_symmetry():
    """Which S5: the permutations of K6 that keep D fix the cone point; the transitive S5 = PGL(2,5) gives another module."""
    E = carrier.edges()
    D = np.array(carrier.dirac(sp.Matrix(carrier.signless_incidence())).tolist(), dtype=np.int64)
    K6 = [(i, 5) for i in range(5)] + E
    index = {frozenset(e): k for k, e in enumerate(K6)}

    def bonds(s):
        P = np.zeros((15, 15), dtype=np.int64)
        for k, (i, j) in enumerate(K6):
            P[index[frozenset((s[i], s[j]))], k] = 1
        return P

    def atoms(f):
        P = np.zeros((15, 15), dtype=np.int64)
        for i in range(5):
            P[f[i], i] = 1
        for k, (i, j) in enumerate(E):
            P[5 + E.index(tuple(sorted((f[i], f[j])))), 5 + k] = 1
        return P

    keeps = lambda s: np.array_equal(bonds(s) @ D @ bonds(s).T, D)
    cone = {s for s in itertools.permutations(range(6)) if keeps(s)}
    pgl, psl = projective_line()
    involutions = lambda G: [s for s in G if s != tuple(range(6)) and all(s[s[i]] == i for i in range(6))]
    chi = lambda G: Counter(int(np.trace(bonds(s))) for s in involutions(G))
    orbits = lambda G: len({frozenset(int(np.argmax(bonds(s)[:, k])) for s in G) for k in range(15)})
    affine = {s for s in pgl if s[5] == 5}
    return {
        "of the 720 permutations of K6's vertices exactly the 120 that fix the cone point keep D on the 15 bonds":
            len(cone) == 120 and all(s[5] == 5 for s in cone),
        "on them the atoms and the bonds are one S5-set (vertex i <-> spoke i5, edge ij <-> ij); transpositions have "
        "character 7 and double transpositions 3": all(np.array_equal(atoms(s[:5]), bonds(s)) for s in cone)
        and chi(cone) == Counter({7: 10, 3: 15}),
        "the transitive S5 = PGL(2,5) on the projective line over F5 has one orbit on the bonds (the cone S5 has two) and "
        "character 3 on all 25 involutions, the 10 outside PSL(2,5) included: a different S5-module (the hub's 7 versus 3)":
            len(pgl) == 120 and len(psl) == 60 and orbits(pgl) == 1 and orbits(cone) == 2
            and chi(pgl) == Counter({3: 25}) and len(involutions(pgl - psl)) == 10,
        "the two meet in the twenty affine maps x -> a x + b, F20 = AGL(1,5), which holds the 5-cycle; these are the only "
        "elements of PGL(2,5) that keep D": affine == cone & pgl and len(affine) == 20
        and {s for s in pgl if keeps(s)} == affine and (1, 2, 3, 4, 0, 5) in affine,
    }


def mpkg_block():
    """MPKG_L4: a 6 x 6 block of order 5 with traces 1, 1, 1, 1 is the C5 rotation of the cone's six sites."""
    R6 = np.zeros((6, 6), dtype=np.int64)
    for i in range(6):
        R6[(i + 1) % 5 if i < 5 else 5, i] = 1
    stated = [6, 1, 1, 1, 1]                                   # tr B^0, ..., tr B^4 as the note states them
    w = np.exp(2j * np.pi / 5)
    mult = [sum(stated[k] * w ** (-j * k) for k in range(5)) / 5 for j in range(5)]
    four = np.kron(np.eye(4, dtype=np.int64), R6)
    return {
        "the rotation of the five rim sites with the cone point fixed has order 5 and traces 1, 1, 1, 1, 6": [
            int(np.trace(np.linalg.matrix_power(R6, k))) for k in range(1, 6)] == [1, 1, 1, 1, 6]
        and np.array_equal(np.linalg.matrix_power(R6, 5), np.eye(6, dtype=np.int64)),
        "a 6 x 6 matrix with B^5 = I and those traces has the eigenvalue 1 twice and each primitive fifth root once, so it "
        "is similar to that rotation over Q": np.allclose(mult, [2, 1, 1, 1, 1]),
        "four copies have trace 4 and return at 5 to an identity of trace 24": int(np.trace(four)) == 4
        and np.array_equal(np.linalg.matrix_power(four, 5), np.eye(24, dtype=np.int64)),
        "doubling sends the levels 0, 6, 12, 18 to 0, 12, 24, 0": [2 * x % 36 for x in (0, 6, 12, 18)] == [0, 12, 24, 0],
        "the stored block [[-1, 4], [6, 1]] squares to 25 I": sp.Matrix([[-1, 4], [6, 1]]) ** 2 == 25 * sp.eye(2),
    }


def p31_clock():
    """MORE_DOTS left the 31-point clock's characteristic polynomial open; for P31 it is (x - 1)(x^3 - 1)^2 (x^6 - 1)^4."""
    _, pts, step = _p31()
    at = {p: k for k, p in enumerate(pts)}
    P = sp.zeros(31, 31)
    for p in pts:
        P[at[step[p]], at[p]] = 1
    x = sp.symbols("x")
    return {
        "the symmetric square's permutation P31 of the 31 points has characteristic polynomial (x - 1)(x^3 - 1)^2 "
        "(x^6 - 1)^4 and order 6": sp.expand(P.charpoly(x).as_expr() - (x - 1) * (x ** 3 - 1) ** 2 * (x ** 6 - 1) ** 4)
        == 0 and P ** 6 == sp.eye(31) and P ** 2 != sp.eye(31) and P ** 3 != sp.eye(31),
        "rank(P31 - I) = 31 - 7 = 24, one kernel vector per orbit": (P - sp.eye(31)).rank() == 24,
    }


def notes_2303():
    """The 22:08-23:03 notes: arithmetic, and two corrections (the shift and the doubling; the sun's order)."""
    dbl, shift = (lambda x: 2 * x % 36), (lambda x: (x + 24) % 36)
    C3 = sp.Matrix([[0, -1], [1, -1]])
    R5 = sp.Matrix(5, 5, lambda r, c: int(r == (c + 1) % 5))
    S = sp.Matrix(5, 4, lambda r, c: int(r == c) - int(r == c + 1))
    T6 = sp.diag(2 * sp.eye(4) - (S.T * S).inv() * S.T * R5 * S, sp.Matrix([[5]]))
    M, B = sp.Matrix(carrier.signless_incidence()), sp.Matrix(carrier.signed_incidence())
    six = set(range(0, 36, 6))
    return {
        "MORE_DOTS corrected: the shift T by 24 does not commute with the doubling D on the atlas; D T = T^2 D = T^-1 D and "
        "D^2 T = T D^2 (the hub's atlas verifier agrees)": all(dbl(shift(x)) == shift(shift(dbl(x)))
                                                              and dbl(dbl(shift(x))) == shift(dbl(dbl(x))) for x in range(36))
        and any(dbl(shift(x)) != shift(dbl(x)) for x in range(36)),
        "MORE_DOTS: the companion [[0, -1], [1, -1]] has order 3; 96 = 60 + 36, 70 = 60 + 10, 94 = 96 - 2; "
        "4 x 96 + 6 x 36 = 600, where both parts meet and the sum misses": C3 ** 3 == sp.eye(2) and C3 != sp.eye(2)
        and (96, 70, 94) == (60 + 36, 60 + 10, 96 - 2) and 4 * 96 + 6 * 36 == 600 and ledger.contains_tick(384)
        and ledger.contains_tick(216) and not ledger.contains_tick(600),
        "PAULI_CYCLE: 256 and 224 sit at addresses 4 and 8, doubling runs 4 -> 8 -> 16 -> 32, and 1 + 8 x 15 + 9 x 15 = 256":
            (256 % 36, 224 % 36) == (4, 8) and [4 * 2 ** k % 36 for k in range(4)] == [4, 8, 16, 32]
            and 1 + 8 * 15 + 9 * 15 == 256,
        "SIBLING_540: C(9, 2) = 36, C(9, 3) = 84; Phi_5(2) = 31 = 15 + 4 + 6 + 6 = 6 + 15 + 10; 3(10 - 1) = 27":
            sp.binomial(9, 2) == 36 and sp.binomial(9, 3) == 84 and sp.cyclotomic_poly(5, 2) == 31
            and 15 + 4 + 6 + 6 == 6 + 15 + 10 == 31 and 3 * (10 - 1) == 27,
        "CANON_JOIN: rank M = 5, rank B = 4 and 10 - 4 = 6 cycles; a T with det 155, such as (2I - C) + [5], has a Gram "
        "T^T T of det 155^2 = 24025, and 4805 = 31 x 155; 12 x 16 < 195 <= 12 x 17": M.rank() == 5 and B.rank() == 4
        and T6.det() == 155 and (T6.T * T6).det() == 24025 == 155 ** 2 and 4805 == 31 * 155 and 12 * 16 < 195 <= 12 * 17,
        "CANON_CYCLE, DEEP_H and LEVEL_DOTS on the atlas: 155, 24025, 4805 -> 11, 13, 17; 174108 = 40 x 4320 + 1308 with "
        "1308 = 12 x 109 -> 12; 168 -> 24, 42 -> 6, 138 -> 30, 2415 and 39 -> 3, 4834 -> 10, 77 -> 5": [
            x % 36 for x in (155, 24025, 4805, 174108, 168, 42, 138, 2415, 39, 4834, 77)]
        == [11, 13, 17, 12, 24, 6, 30, 3, 3, 10, 5] and 174108 == 40 * N + 1308 and 1308 == 12 * 109,
        "doubling keeps the six multiples of 6 (6, 30 -> 12, 24; 18 -> 0) and takes 3 -> 6 -> 12, 10 -> 20, 5 -> 10 -> 20":
            {dbl(a) for a in six} <= six and (dbl(6), dbl(30), dbl(18)) == (12, 24, 0)
            and (dbl(3), dbl(6), dbl(10), dbl(5)) == (6, 12, 20, 10),
        "DEEP_H: <35> = <5> holds the 864 multiples of 5, exactly the points that miss the tick; 7 x 24 = 168":
            spine.subgroup(35) == spine.subgroup(5) == {x for x in range(N) if not ledger.contains_tick(x)}
            and len(spine.subgroup(5)) == TICK and 7 * 24 == 168,
        "DEEP_H corrected: <39> = <3> has 1440 points, the sun's step; the sun 1440 itself has order 3":
            spine.order(39) == 1440 and spine.order(1440) == 3,
    }


# ------------------------------------------------------------ the 23:05-23:43 items

def grain():
    """The grain <72> is the golden orbit <216> times the sun <1440>, and each clock reads one factor."""
    G = spine.subgroup(72)
    coord = {(216 * k + 1440 * j) % N: (k, j) for k in range(20) for j in range(3)}
    other = spine.subgroup(36) - G
    return {
        "every multiple of 72 is one golden point 216 k plus one sun point 1440 j: a direct product of 20 x 3 = 60, "
        "with 72 = 1512 + 2880 (golden index 7, two sun steps)": set(coord) == G and len(coord) == 60
        and spine.subgroup(216) & spine.subgroup(1440) == {0} and coord[72] == (7, 2),
        "time reads k mod 5 and the 2-clock 24 k mod 32, the 27-clock reads 9 j mod 27, and the atlas reads 0":
            all((x % 5, x % 32, x % 27, x % 36) == (k % 5, 24 * k % 32, 9 * j % 27, 0) for x, (k, j) in coord.items()),
        "doubling doubles the golden index and inverts the sun coordinate": all(
            coord[2 * x % N] == (2 * k % 20, -j % 3) for x, (k, j) in coord.items()),
        "the grain lies in the coil with index 9; the other half of the seam, 36 + grain, has 2-coordinates 4, 12, 20, "
        "28 and falls into the grain in one doubling": G <= spine.subgroup(8) and len(spine.subgroup(8)) == 9 * len(G)
        and sorted({x % 32 for x in other}) == [4, 12, 20, 28] and all(2 * x % N in G for x in other),
        "the golden orbit is the ticks plus the observer, index 4a + 5b (a mod 5, b mod 4); its twelve mixed positions "
        "all meet the tick, and negation fixes only 0 and 10 (the half-turn 2160)": sorted(
            (4 * a + 5 * b) % 20 for a in range(5) for b in range(4)) == list(range(20))
        and [n for n in range(20) if n % 4 and n % 5 and ledger.contains_tick(216 * n % N)] == [n for n in range(20)
                                                                                                if n % 4 and n % 5]
        and sum(1 for n in range(20) if n % 4 and n % 5) == 12 and [n for n in range(20) if -n % 20 == n] == [0, 10],
        "on the 2-clock the golden step and the observer step add the same 24 (5 = 1 mod 4); the inverse step 4104 adds 8":
            216 % 32 == 1080 % 32 == 24 and 4104 == 216 * 19 and 4104 % 32 == 8 and (4104 + 216) % N == 0,
    }


def shift_law():
    """SHIFT_LAW: doubling turns a shift by s into a shift by 2s, so it inverts exactly the shifts of order 3."""
    dbl = lambda x, m: 2 * x % m
    inverted = lambda m: [s for s in range(m) if dbl(s, m) == -s % m]   # D is additive: D T_s = T_s^-1 D iff 2s = -s
    return {
        "D T_s = T_s^2 D for every shift s: doubling a shifted point is the doubled point shifted twice": all(
            dbl((x + s) % N, N) == (dbl(x, N) + 2 * s) % N for s in (1, 216, TICK, 1440) for x in range(0, N, 37)),
        "it is T_s^-1 D exactly when 3s = 0: the sun's shifts 0, 1440, 2880 on the circle, 0, 9, 18 on the 27-clock and "
        "0, 12, 24 on the atlas (the shift by 24 of the 23:03 correction)": inverted(N) == [0, 1440, 2880]
        and inverted(27) == [0, 9, 18] and inverted(36) == [0, 12, 24],
        "doubling keeps the tick bit, because 2 is prime to 5": all(
            ledger.contains_tick(x) == ledger.contains_tick(2 * x % N) for x in range(N)),
    }


def golden_identities():
    """DOUBLE_CHILD, KARMA_COMM, BASS_STOP and GOLDEN_REST: identities of the golden family for every n."""
    B, I2 = sp.Matrix([[1, 1], [1, 0]]), sp.eye(2)
    F = lambda n: sp.fibonacci(n) if n >= 0 else (-1) ** (1 - n) * sp.fibonacci(-n)
    power = lambda n: B ** n if n >= 0 else (B - I2) ** -n
    K = sp.Matrix([[0, 1], [-4, 0]])
    C = K * B - B * K
    t = sp.symbols("t")

    def ret(M, m):
        P, k = M.applyfunc(lambda x: x % m), 1
        while P != I2:
            P, k = (P * M).applyfunc(lambda x: x % m), k + 1
        return k
    ratios, x = [], sp.Integer(1)
    for _ in range(6):
        x = 1 + 1 / x
        ratios.append(x)
    return {
        "F(2n) = F(n) L(n) for n = -20..40: B^2n = (F_n B + F_(n-1) I)^2": all(
            F(2 * n) == F(n) * (F(n - 1) + F(n + 1)) for n in range(-20, 41)),
        "B^2 has determinant 1 and returns after 3, 10, 6, 36, 24 and 12 mod 4, 5, 8, 27, 32 and 36": (B ** 2).det() == 1
        and {m: ret(B ** 2, m) for m in (4, 5, 8, 27, 32, 36)} == {4: 3, 5: 10, 8: 6, 27: 36, 32: 24, 36: 12},
        "karma's K = [[0, 1], [-4, 0]] has det 4 and K^2 = -4I (the source's q'' + 4q = 0); [K, B^n] = F_n [K, B] for "
        "n = -15..30, with trace 0 and det -29 F_n^2, and 29 = 4^2 + 3 x 4 + 1": K.det() == 4 and K ** 2 == -4 * I2
        and C.trace() == 0 and C.det() == -29 and 4 ** 2 + 3 * 4 + 1 == 29
        and all(K * power(n) - power(n) * K == F(n) * C for n in range(-15, 31)),
        "x -> 1 + 1/x from 1 gives 2, 3/2, 5/3, 8/5, 13/8, 21/13, the first rows of the golden children, and 21 x 8 - 13^2 "
        "= -1; it shares the fixed-point equation t^2 - t - 1 = 0 with z -> z^2 - 1, which sends 2 to 3, not 3/2":
            ratios == [F(n + 1) / F(n) for n in range(2, 8)] and 21 * 8 - 13 ** 2 == -1
            and sp.expand(sp.numer(sp.together(t - 1 - 1 / t))) == sp.expand(t ** 2 - 1 - t) == t ** 2 - t - 1
            and (1 + sp.Rational(1, 2), 2 ** 2 - 1) == (sp.Rational(3, 2), 3),
        "GOLDEN_REST corrected: over Z, B^10 = [[89, 55], [55, 34]] has infinite order, but mod 5, where B has order 20 "
        "like 216, B^10 = -I has order 2, like 2160": B ** 10 == sp.Matrix([[89, 55], [55, 34]])
        and (B ** 10).applyfunc(lambda v: v % 5) == 4 * I2 and spine.order(2160) == 2,
    }


def vortex():
    """The vortex Z/9: doubling runs through its six units, it reads the atlas, and it is the 27-clock without the sun."""
    nak = [160 * k % N for k in range(27)]
    loops = {frozenset((c + 216 * k) % N for k in range(20)) for c in range(N)}
    units = [u for u in range(1, 27) if u % 3]
    return {
        "doubling mod 9 runs through the six units 2, 4, 8, 7, 5, 1; the pass sums to 27 and the axis 3 + 6 + 9 to 18 "
        "(4320 / 18 = 240); the units multiply to 2240, which shares 160 with the circle":
            [pow(2, k, 9) for k in range(1, 7)] == [2, 4, 8, 7, 5, 1] and 2 + 4 + 8 + 7 + 5 + 1 == 27
            and N // (3 + 6 + 9) == 240 and 2 * 4 * 8 * 7 * 5 == 2240 and gcd(2240, N) == 160,
        "9 | 36, so the whole seam (the grain, the golden step, the tick, the observer and the sun) sits at vortex "
        "coordinate 0, and the multiples of 9 are four copies of the seam": all(x % 9 == 0 for x in spine.subgroup(36))
        and len(spine.subgroup(9)) == 4 * len(spine.subgroup(36)),
        "the nakshatra 160 sits at 7, and along <160> each coordinate appears three times; the three at 0 are the sun":
            160 % 9 == 7 and Counter(x % 9 for x in nak) == Counter({r: 3 for r in range(9)})
            and sorted(x for x in nak if x % 9 == 0) == [0, 1440, 2880],
        "Z/27 -> Z/9 has kernel 0, 9, 18, the sun's 27-coordinates; doubling has order 18 on the 18 units mod 27, with "
        "2^9 = -1; the units sum to 243 = 3^5 = 9 x 27, and four of them (5, 10, 20, 25) are multiples of 5":
            [s for s in range(27) if s % 9 == 0] == [0, 9, 18] == sorted({1440 * j % 27 for j in range(3)})
            and sorted(pow(2, k, 27) for k in range(18)) == units and pow(2, 9, 27) == 26
            and sum(units) == 243 == 3 ** 5 == 9 * 27 and [u for u in units if u % 5 == 0] == [5, 10, 20, 25],
        "adding 216 keeps the vortex coordinate: the 216 loops of 20 (the cosets of <216>) fall into 9 layers of 24":
            len(loops) == 216 and all(len({x % 9 for x in c}) == 1 for c in loops)
            and Counter(min(c) % 9 for c in loops) == Counter({r: 24 for r in range(9)}),
    }


def doubling_split():
    """DOUBLE_SPLIT and TWO_DOUBLES: doubling is nilpotent on the 2-part and has order 36 on the odd part."""
    period = lambda m, start: next(p for p in range(1, 100) if all(pow(2, k + p, m) == pow(2, k, m)
                                                                  for k in range(start, start + 60)))
    return {
        "on the 2-clock five doublings kill every coordinate (1 needs all five), and two kill the golden ones 8, 16, 24":
            all(32 * c % 32 == 0 for c in range(32)) and 16 % 32 != 0 and all(4 * c % 32 == 0 for c in (8, 16, 24)),
        "on the odd part Z/135 doubling has order 36 = lcm(4, 18), its orders on the time pentagon and the 27-clock":
            next(k for k in range(1, 100) if pow(2, k, 135) == 1) == 36 == sp.ilcm(4, 18),
        "so the powers of 2 settle into period 36 on the circle but period 6 on the atlas: the atlas modulus and the "
        "circle's doubling period are the same integer, not the same cycle": period(N, 5) == 36 and period(36, 2) == 6,
        "TWO_DOUBLES: a doubled odd golden index has 2-coordinate 16, the half-turn's; doubled twice it is a golden tick; "
        "the observer points doubled twice give 0": all(2 * 216 * k % 32 == 16 for k in range(1, 20, 2))
        and all(4 * 216 * k % N in spine.subgroup(TICK) for k in range(20)) and all(4 * x % N == 0 for x in (1080, 2160, 3240)),
    }


def notes_2343():
    """The 23:05-23:43 notes: arithmetic, and three corrections (the 2-part of 216, the clock tower, order and step)."""
    duads = list(itertools.combinations(range(6), 2))
    synthemes = [s for s in itertools.combinations(duads, 3) if len(set(itertools.chain(*s))) == 6]
    totals = [s for s in itertools.combinations(synthemes, 5) if len(set(itertools.chain(*s))) == 15]
    lam = [Fraction(1, 9), Fraction(-1, 3), Fraction(2, 3), Fraction(0)]
    v = [Fraction(0)] + [Fraction(1, 4)] * 4
    t = sp.symbols("t")
    sub = spine.subgroup
    return {
        "GOLDEN_EVERYWHERE corrected: 216 = 1080 + 3456 with 1080 the 2-part and 3456 the time part, not the 2-part (the "
        "hub's release J agrees); 216 = 6 x 36 = 8 x 27 = 9 x 24 = 3 x 72": (216 * 3105 % N, 216 * 3456 % N) == (1080, 3456)
        and 216 == 6 * 36 == 8 * 27 == 9 * 24 == 3 * 72,
        "ALL_RANKS corrected: circle, seam, grain, golden orbit is a chain (indices 36, 2, 3), but below it the ticks "
        "(index 4) and the observer (index 5) are two subgroups of the golden orbit meeting in 0, and the sun lies in the "
        "grain (index 20), not in the observer clock": sub(36) >= sub(72) >= sub(216) >= sub(TICK) | sub(1080)
        and sub(TICK) & sub(1080) == {0} and not sub(1080) <= sub(TICK) and not sub(1440) <= sub(1080)
        and sub(1440) <= sub(72) and len(sub(72)) // len(sub(1440)) == 20,
        "order and step are dual: a divisor d of 4320 has order 4320 / d. So 3 has order 1440 while the sun 1440 has order "
        "3, and 27 has order 160 while the nakshatra 160 has order 27 (VORTEX_JOIN, VORTEX_LIFT and SOUND_LIGHT name the "
        "dual step)": all(spine.order(d) == N // d for d in sp.divisors(N))
        and (spine.order(3), spine.order(1440), spine.order(27), spine.order(160)) == (1440, 3, 160, 27),
        "the syntheme catalogue of six points is 6 + 15 + 15 = 36 (totals, synthemes, duads), the 6 x 6 matrices are "
        "21 + 15 (symmetric, skew), and 36 x 6 = 216": (len(totals), len(synthemes), len(duads)) == (6, 15, 15)
        and 21 + 15 == 36 and 36 * 6 == 216,
        "the bass fiber: 7 x 4 + 4 x 2 + 2 = 38, 18 + 6 = 24; the losses 1 - lambda^2 at 1/9, -1/3, 2/3, 0 are 80/81, 8/9, "
        "5/9, 1 and the coefficients lambda - 1/9 are 0, -4/9, 5/9, -1/9, equal only at 2/3 (the other root of "
        "lambda^2 + lambda = 10/9 is -5/3); 37 generates the circle and 38 the evens; 38 x 2160 / 4320 = 19; 117 = 9 x F_7":
            7 * 4 + 4 * 2 + 2 == 38 and 18 + 6 == 24
            and [1 - x * x for x in lam] == [Fraction(80, 81), Fraction(8, 9), Fraction(5, 9), 1]
            and [x - Fraction(1, 9) for x in lam] == [0, Fraction(-4, 9), Fraction(5, 9), Fraction(-1, 9)]
            and set(sp.solve(t ** 2 + t - sp.Rational(10, 9), t)) == {sp.Rational(2, 3), sp.Rational(-5, 3)}
            and gcd(37, N) == 1 and spine.order(38) == 2160 and 38 * 2160 // N == 19 and 117 == 9 * sp.fibonacci(7),
        "the source shape: p1(CP^4) = c1^2 - 2 c2 = 25 - 20 = 5 (times u^2); a 5 x 5 matrix has 15 symmetric and 10 skew "
        "entries; the contact point (0, 1/4, 1/4, 1/4, 1/4) has centered square 1/20 = 4/80; 1728 = 8 x 216":
            sp.binomial(5, 1) ** 2 - 2 * sp.binomial(5, 2) == 5 and 15 + 10 == 25
            and sum((a - sum(v) / 5) ** 2 for a in v) == Fraction(4, 80) and 1728 == 8 * 216,
        "SOUND_LIGHT and SYNTHESIS_I: 432 x 2 = 864 with 432 of order 10; 24 x 180 = 4320; 4 x 180 + 144 = 864; "
        "100 + 19 + 50 = 169 and 169 - 50 = 119": 432 * 2 == TICK and spine.order(432) == 10 and 24 * 180 == N
        and 4 * 180 + 144 == TICK and 100 + 19 + 50 == 169 and 169 - 50 == 119,
        "GOLDEN_INVERSE: 216 x 19 = 4104 sits at address 0, 27-coordinate 0, time 4 and 2-coordinate 8, and B^19 = B - I "
        "mod 5": (4104 % 36, 4104 % 27, 4104 % 5, 4104 % 32) == (0, 0, 4, 8)
        and (sp.Matrix([[1, 1], [1, 0]]) ** 19).applyfunc(lambda x: x % 5) == sp.Matrix([[0, 1], [1, 4]]),
    }


# ------------------------------------------------------------ the 23:46-00:14 items

def tick_miss():
    """TICK_MISS and COORD_LAW: the circle is the ticks times the misses, and the tick bit is the tick coordinate."""
    tick, miss = spine.subgroup(TICK), spine.subgroup(5)
    part = lambda x: 3456 * x % N                              # the time idempotent: the tick part of x
    loops = {frozenset((c + 216 * k) % N for k in range(20)) for c in range(N)}
    misses = [sorted(x for x in c if not ledger.contains_tick(x)) for c in loops]
    fate = lambda n: functools.reduce(lambda m, _: 2 * m % 20, range(10), n)
    return {
        "Z/4320 is the direct sum of the five ticks <864> and the 864 misses <5>: every point is a tick part plus a miss":
            tick & miss == {0} and len(tick) * len(miss) == N and {(a + m) % N for a in tick for m in miss} == set(range(N)),
        "a point misses the tick exactly when its tick part is 0; the golden step is 216 = 3456 + 1080, tick part -864 "
        "and miss part 1080 (5 x 216)": all(ledger.contains_tick(x) == (part(x) != 0) for x in range(N))
        and (part(216), (216 - part(216)) % N) == (3456, 1080),
        "864 copies of a point clear its miss part and land on the pure tick with the opposite coordinate (13, of tick "
        "coordinate 2, lands on 2592); two doublings and 864 copies agree exactly on the golden orbit <216>":
            all(TICK * x % N == -part(x) % N for x in range(N)) and part(13) == 2 * TICK and 13 * TICK % N == 2592
            and {x for x in range(N) if 4 * x % N == TICK * x % N} == spine.subgroup(216),
        "each of the 216 golden loops holds exactly four misses, one coset of the observer clock; the observer and the "
        "whole nakshatra clock lie in the miss set": len(loops) == 216
        and all(len(m) == 4 and {(y - m[0]) % N for y in m} == spine.subgroup(1080) for m in misses)
        and spine.subgroup(1080) <= miss and spine.subgroup(160) <= miss,
        "doubling sorts the golden orbit by the tick bit: an index prime to 5 ends in the tick cycle 4, 8, 16, 12, a "
        "multiple of 5 ends at 0": all((fate(n) in (4, 8, 12, 16)) == (n % 5 != 0) for n in range(20))
        and [216 * n % N for n in (4, 8, 16, 12)] == [TICK, 1728, 3456, 2592],
    }


def doubling_orbits():
    """TICK_CYCLE, OBS_FALLS, NAKSHATRA_SPLIT and THREE_DOUBLES: what doubling does to each clock."""
    def cycle_lengths(points, step):
        seen, lengths = set(), []
        for s in points:
            if s in seen:
                continue
            n, y = 0, s
            while y not in seen:
                seen.add(y)
                y, n = step(y), n + 1
            lengths.append(n)
        return sorted(lengths)
    nak = [160 * k % N for k in range(27)]
    coset = lambda x: frozenset((x + 216 * k) % N for k in range(20))
    cosets = {coset(x) for x in spine.subgroup(8)}
    odd = cycle_lengths(range(135), lambda y: 2 * y % 135)
    return {
        "doubling cycles the four nonzero ticks, 864 -> 1728 -> 3456 -> 2592 -> 864 (one doubling squares the shift, "
        "two invert it), and kills the observer: 1080 and 3240 fall to 2160 and then to 0": [2 * x % N for x in (
            TICK, 1728, 3456, 2592)] == [1728, 3456, 2592, TICK] and [2 * x % N for x in (1080, 3240, 2160)] == [2160, 2160, 0]
        and 4 * TICK % N == -TICK % N,
        "doubling permutes the 27 nakshatra points as an 18-cycle, a 6-cycle through 480, the sun's swap 1440 <-> 2880 "
        "and 0": cycle_lengths(nak, lambda y: 2 * y % N) == [1, 2, 6, 18] and (2 * 1440 % N, 2 * 2880 % N) == (2880, 1440)
        and len({480 * 2 ** k % N for k in range(6)}) == 6,
        "three doublings put every point in the coil, and on the coil's 27 golden cosets doubling has the same cycles; "
        "the nakshatra clock meets every coset once": all(8 * x % N in spine.subgroup(8) for x in range(N))
        and len(cosets) == 27 and cycle_lengths(cosets, lambda c: coset(2 * min(c) % N)) == [1, 2, 6, 18]
        and {coset(x) for x in nak} == cosets,
        "corrected (the separate model's relations receipt, adopted by the sibling's CORRECTIONS): on the odd part "
        "doubling has order 36 but its orbit lengths are 1, 2, 4, 6, 12, 18, 36, not one 36-cycle; and doubling keeps "
        "the vortex coordinate 0, not the points (216 -> 432)": sorted(set(odd)) == [1, 2, 4, 6, 12, 18, 36]
        and 2 * 216 % N == 432 and 432 % 9 == 0,
    }


def towers():
    """POWER_TOWER, SALINA_CONG, TOWERS and FROZEN_CLOCKS: the towers of 3, 2 and 5 on the circle and mod 12."""
    return {
        "the tower of threes freezes at 27: 3^3 = 27, 3^27 = 27 and 3^(3^27) = 27 mod 4320 (an exponent = 3 mod 8 returns "
        "27 mod 32, and mod 5 and 27 as well)": (27 % N, pow(3, 27, N), pow(3, 3 ** 27, N)) == (27, 27, 27),
        "the tower of twos freezes one floor later: 2^16 = 736 = 32 x 23 and 2^65536 = 736 mod 4320":
            pow(2, 16, N) == pow(2, 2 ** 16, N) == 736 == 32 * 23,
        "the tower of fives freezes too, at 245 from height 3: 5^5 = 3125, 5^3125 = 245 and 5^(5^3125) = 245 mod 4320. "
        "POWER_TOWER said it does not freeze, and at 00:15 this layer repeated that from one step; the separate model's "
        "splits receipt and the sibling's TOWERS correct it": pow(5, 5, N) == 3125 and pow(5, 3125, N) == 245
        and pow(5, 5 ** 3125, N) == 245,
        "each frozen value is 0 on its own clock and a unit on the other two: 736 generates the 135 points that are 0 on "
        "the 2-clock, 27 the 160 that are 0 on the 27-clock, and 245 the 864 misses (FROZEN_CLOCKS)": all(
            v % p == 0 and spine.subgroup(v) == {y for y in range(N) if y % p == 0} and spine.order(v) == o
            for v, p, o in ((736, 32, 135), (27, 27, 160), (245, 5, 864)))
        and (736 % 27, 736 % 5, 27 % 32, 27 % 5, 245 % 32, 245 % 27) == (7, 1, 27, 2, 21, 2),
        "mod 12 all three freeze at once, at 3, 4 and 5, which sum to 12 (3125 and 245 are both 5 mod 12); the step 12 "
        "has order 360 and index 12, and 72 x 12 = 864": (pow(3, 27, 12), pow(2, 16, 12), pow(5, 3125, 12), 245 % 12)
        == (3, 4, 5, 5) and 3 + 4 + 5 == 12 and spine.order(12) == 360 and N // len(spine.subgroup(12)) == 12
        and 72 * 12 == TICK,
    }


def modules_8_11():
    """The Locked Memory synthesis's modules 8-11 (00:06), read only: what can be checked from the stated formulas."""
    R6 = sp.Matrix(6, 6, lambda r, c: int(r == (c + 1) % 6))
    I6, I12 = sp.eye(6), sp.eye(12)
    T12 = sp.BlockMatrix([[sp.zeros(6), R6], [-R6, 2 * R6]]).as_explicit()
    U = sp.BlockMatrix([[sp.zeros(6), I6], [-I6, 2 * I6]]).as_explicit()
    x, y = sp.symbols("x y")
    r2 = 1 + x ** 2 + y ** 2
    reader = lambda s: gcd(s, 240) + (11 if s % 241 == 0 else 1)
    B, K = sp.Matrix([[1, 1], [1, 0]]), sp.Matrix([[0, 1], [-4, 0]])
    R5 = sp.Matrix(5, 5, lambda r, c: int(r == (c + 1) % 5))
    z = sp.symbols("z")
    return {
        "the 5-cycle has characteristic polynomial z^5 - 1, and JOIN_MODULES's missing map exists: kappa(x) = 4x mod 5 "
        "carries the tick translation to the vertex 5-cycle (the join time -> K5 vertices)": R5.charpoly(z).as_expr()
        == z ** 5 - 1 and 4 * TICK % 5 == 1,
        "the two-tick T12 = [[0, B6], [-B6, 2 B6]] (B6 the 6-cycle) is (B6 + B6) U with U = [[0, I], [-I, 2I]] unipotent, "
        "U != I and (U - I)^2 = 0, the factors commuting; so T12 - B6 + B6 squares to 0, T12 is not semisimple, has "
        "infinite order and keeps no positive-definite form, unlike the 5-cycle": sp.diag(R6, R6) * U == T12
        == U * sp.diag(R6, R6) and ((U - I12) ** 2).is_zero_matrix and not (U - I12).is_zero_matrix
        and ((T12 - sp.diag(R6, R6)) ** 2).is_zero_matrix and all(T12 ** k != I12 for k in (6, 12, 30, 60)),
        "the curvature of A = (x dy - y dx)/(1 + x^2 + y^2) is dA = 2 dx dy / (1 + x^2 + y^2)^2": sp.simplify(
            sp.diff(x / r2, x) - sp.diff(-y / r2, y) - 2 / r2 ** 2) == 0,
        "the stride reader gcd(s, 240) + 1 (or + 11 when 241 | s) gives 2, 121, 241, 12 at s = 1, 120, 240, 241; the "
        "formal period lcm(240, 241) = 57840 = 240^2 + 240, the bath's second return moment, meets the circle in 240 "
        "and has lcm 241 x 4320 with it": [reader(s) for s in (1, 120, 240, 241)] == [2, 121, 241, 12]
        and sp.ilcm(240, 241) == 57840 == 240 ** 2 + 240 and gcd(57840, N) == 240 and sp.ilcm(57840, N) == 241 * N,
        "121 and 241 generate the circle, are 1 mod 12 and differ by 120 = 10 x 12; 120 has order 36 and 36 has order "
        "120; dim SU(6) = 35; B sends (2, 1) to (3, 2)": gcd(121, N) == gcd(241, N) == 1 and 121 % 12 == 241 % 12 == 1
        and 241 - 121 == 10 * 12 and (spine.order(120), spine.order(36)) == (36, 120) and 6 ** 2 - 1 == 35
        and B * sp.Matrix([2, 1]) == sp.Matrix([3, 2]),
        "KARMA_COMM corrected (relations receipt): [K, B^5] = [[25, -5], [-20, -25]] has det -725 = -29 x 25, so the "
        "determinant is divisible by 25 and the entries only by 5": K * B ** 5 - B ** 5 * K == sp.Matrix([[25, -5], [-20, -25]])
        and (K * B ** 5 - B ** 5 * K).det() == -725 == -29 * 25,
    }


def hankel_25():
    """The synthesis's 'N = 25 Stieltjes-Jacobi annihilator on W0..W50' is not an annihilator of the walk counts."""
    W, _ = _walks()
    H = sp.Matrix(26, 26, lambda i, j: W[i + j])
    return {
        "the 26 x 26 Hankel matrix [W_(i+j)] of W_0..W_50 has positive determinant, so no nonzero c gives "
        "sum_k c_k W_(n+k) = 0 for n = 0..25: the walk counts have no order-25 annihilator on that window":
            H.det(method="bareiss") > 0,
        "what 51 moments always give is a depth-25 Jacobi fit, which reproduces them by construction and predicts "
        "nothing; the walk measure has infinite support, so every Hankel determinant is positive": all(
            sp.Matrix(n, n, lambda i, j: W[i + j]).det(method="bareiss") > 0 for n in (2, 5, 10)),
    }


# ------------------------------------------- the 00:16-00:29 items and the sibling's 29 October paper

def eight_roots():
    """ONE_MACHINE_29, sec. 4: eight roots with pairwise products 1 and the origin form a maximal 9-clique of index 3."""
    e = lambda i: np.eye(8)[i]
    R = np.array([-e(0) - e(i) for i in range(1, 8)] + [-0.5 * np.ones(8)])
    G = np.rint(R @ R.T).astype(int)
    roots = glue.roots()
    half = {tuple(np.rint(2 * r).astype(int)) for r in roots}
    key = lambda v: tuple(np.rint(2 * v).astype(int))
    q = R.sum(axis=0) / 3
    c = np.linalg.solve(R @ R.T, np.ones(8))
    duals = np.linalg.inv(R).T
    face = [np.zeros(8)] + list(R[:5])
    inside = {key(p) for p in face}
    nbrs = lambda p: {tuple(a + b for a, b in zip(key(p), r)) for r in half}
    BB = np.array([[len(nbrs(a) - inside) if i == j else len((nbrs(a) & nbrs(b)) - inside) for j, b in enumerate(face)]
                   for i, a in enumerate(face)])
    J8, I8 = np.ones((8, 8), dtype=int), np.eye(8, dtype=int)
    return {
        "the roots -e1 - e2, ..., -e1 - e8 and -(1, ..., 1)/2 have Gram I + J, with (I + J)(9I - J) = 9I: det 9, inverse "
        "I - J/9": all(key(r) in half for r in R) and np.array_equal(G, I8 + J8) and np.array_equal((I8 + J8) @ (9 * I8 - J8), 9 * I8),
        "their coordinates have det 3 (768 doubled), so they span a sublattice of index 3; the quotient generator, their "
        "sum over 3, is (-5/2, -1/2, ..., -1/2), a lattice vector of squared length 8": round(np.linalg.det(2 * R)) == 768
        and round(abs(np.linalg.det(R))) == 3 and np.allclose(q, [-2.5] + [-0.5] * 7) and np.isclose(q @ q, 8)
        and round(2 * q.sum()) % 4 == 0,
        "no ninth root meets all eight: the only vector with all eight products 1 is their sum over 9, of squared length "
        "8/9; with the origin they are a 9-clique of the lattice graph that does not extend": np.allclose(c, 1 / 9)
        and np.isclose((c @ R) @ (c @ R), 8 / 9) and not any(np.allclose(R @ r, 1) for r in roots)
        and all(key(a - b) in half for a, b in itertools.combinations([np.zeros(8)] + list(R), 2)),
        "six times the dual basis is the integer matrix 6R - 2q, and it pairs with the roots to 6I": np.allclose(
            6 * duals, np.rint(6 * duals)) and np.allclose(6 * duals, 6 * R - 2 * q) and np.allclose(6 * duals @ R.T, 6 * np.eye(8)),
        "a six-point face (the origin and five roots) has 235 outside neighbours per point and 52 per pair: coupling Gram "
        "183I + 52J, the six-port of layer 22": np.array_equal(BB, 183 * np.eye(6, dtype=int) + 52 * np.ones((6, 6), dtype=int)),
        "on five of the roots the Gram is I + J, and the carrier's vertex Gram is H H^T = 3I + J = (I + J) + 2I: equal "
        "off the diagonal, not the same operator": np.array_equal(G[:5, :5] + 2 * np.eye(5, dtype=int), 3 * np.eye(5, dtype=int)
                                                                    + np.ones((5, 5), dtype=int)),
    }


def root_symbol():
    """ONE_MACHINE_29, sec. 5, FRAME_WALKS and DEEP_COURT: the bath's symbol, the root graph and the collar witness."""
    roots = glue.roots()
    sym = lambda t: float(np.cos(roots @ t).sum())
    formula = lambda t: (2 * (np.cos(t).sum() ** 2 - (np.cos(t) ** 2).sum())
                         + 128 * (np.prod(np.cos(t / 2)) + np.prod(np.sin(t / 2))))
    rng = np.random.default_rng(29)
    A = (np.abs(roots @ roots.T - 1) < 1e-9).astype(float)
    spec = Counter(np.rint(np.linalg.eigvalsh(A)).astype(int).tolist())
    w = np.array([28, 28, 6, 2, 1, 0, 0, 0]) / 10
    return {
        "sum over the 240 roots of cos(a.t) = 2[(sum cos t_k)^2 - sum cos^2 t_k] + 128[prod cos(t_k/2) + prod sin(t_k/2)] "
        "(the D8 roots and the half-spin orbit); it is 240 at 0 and -16 at pi(1, 1, 1, 1, 0, 0, 0, 0), so the "
        "dispersion reaches 0 and 256": all(abs(sym(t) - formula(t)) < 1e-9 for t in 3 * rng.standard_normal((6, 8)))
        and np.isclose(sym(np.zeros(8)), 240) and np.isclose(sym(np.pi * np.array([1, 1, 1, 1, 0, 0, 0, 0])), -16),
        "the root graph (240 roots, edges at inner product 1) has spectrum 56, 28^8, 8^35, (-2)^112, (-4)^84, trace 0, "
        "and its closed walks 1, 0, 56, 1512, 62160 follow (the separate script's list, of trace -240, does not)":
            spec == Counter({56: 1, 28: 8, 8: 35, -2: 112, -4: 84})
            and [sum(m * v ** n for v, m in spec.items()) // 240 for n in range(5)] == [1, 0, 56, 1512, 62160],
        "the collar witness (28, 28, 6, 2, 1, 0, 0, 0)/10 has squared length 1609/100 and dispersion 220.635, inside "
        "(220.2460, 223.25); the endpoints themselves are not re-certified": np.isclose(w @ w, 16.09)
        and abs((240 - sym(w)) - 220.635) < 5e-4 and 220.2460 < 240 - sym(w) < 223.25,
        "240 x 56 / 12 = 1120 planes of type A2; 17280 x 3 + 2160 x 128 = 328320 = 76 x 4320, and 328320 + 8 = 328328":
            240 * 56 // 12 == 1120 and 17280 * 3 + 2160 * 128 == 328320 == 76 * N and 328320 + 8 == 328328,
    }


def protection():
    """CLOSURE_092 and ONE_MACHINE_29, sec. 2: a protected line has no coupling; the commutator court; the channel law."""
    a, b, d, z, g0, P = sp.symbols("a b d z g0 P")
    X = sp.Matrix([[a, b], [b, d]])
    M = sp.Matrix([[0, 1, 2], [1, 0, 0], [2, 0, 0]])           # one mediator with |v|^2 = 1 + 4 = 5
    K1, K2 = np.diag([0.0, 1.0, 3.0]), np.ones((3, 3))
    herm = []
    for i in range(3):
        E = np.zeros((3, 3), complex)
        E[i, i] = 1
        herm.append(E)
    for i, j in itertools.combinations(range(3), 2):
        E, F = np.zeros((3, 3), complex), np.zeros((3, 3), complex)
        E[i, j] = E[j, i] = 1
        F[i, j], F[j, i] = 1j, -1j
        herm += [E, F]

    def court(X, anchor):
        out = []
        for K in (K1, K2):
            C = K @ X - X @ K
            out += list(C.real.ravel()) + list(C.imag.ravel())
        return out + ([np.trace(X).real] if anchor else [])
    L = lambda anchor: np.array([court(X, anchor) for X in herm]).T
    Gc, Gu = (1 + z * g0) / 240, ((1440 - 5 * z) * g0 - 5) / 240
    W = native.port_metric()
    return {
        "a protected line cannot also be the coupling: X commutes with the line's projector diag(1, 0) exactly when its "
        "off-diagonal entry is 0": sp.diag(1, 0) * X - X * sp.diag(1, 0) == sp.Matrix([[0, b], [-b, 0]]),
        "one mediator of squared length 5 squares to eigenvalues 0, 5, 5 and corrects the doublet by a rank-1 block, so a "
        "full-rank correction needs two": (M ** 2).eigenvals() == {5: 2, 0: 1} and (M ** 2)[1:, 1:].rank() == 1,
        "for K1 = diag(0, 1, 3) and K2 = J the commutator map on 3 x 3 Hermitian matrices has rank 8 (the scalars), a "
        "trace anchor raises it to 9, and the anchored Gram determinant is 176173056": np.linalg.matrix_rank(L(False)) == 8
        and np.linalg.matrix_rank(L(True)) == 9 and round(np.linalg.det(L(True).T @ L(True))) == 176173056,
        "the written six-port channels satisfy (1440 - 5z) G_c - z G_u = 6 for every z and g0 (g0 cancels); at z = 0, "
        "G_c = 1/240 and, with g0 = 1/(240(1 - P)), G_u = (1 + 5P)/(240(1 - P)) = 1/sigma": sp.simplify(
            (1440 - 5 * z) * Gc - z * Gu) == 6 and Gc.subs(z, 0) == sp.Rational(1, 240)
        and sp.simplify(Gu.subs({z: 0, g0: 1 / (240 * (1 - P))}) - (1 + 5 * P) / (240 * (1 - P))) == 0,
        "the port metric W_p has eigenvalues 2/5, 2, 5 - sqrt 5 (twice) and 5 + sqrt 5 (twice), as the paper states, and "
        "the corner 241I - J acts as 235 on the mean and 241 on the contrast": np.allclose(
            np.linalg.eigvalsh(W), sorted([0.4, 2, 5 - 5 ** 0.5, 5 - 5 ** 0.5, 5 + 5 ** 0.5, 5 + 5 ** 0.5]))
        and np.allclose(np.linalg.eigvalsh(241 * np.eye(6) - np.ones((6, 6))), [235] + [241] * 5),
    }


def notes_0029():
    """The 00:16-00:29 notes and the 29 October paper: arithmetic, and three corrections."""
    part = lambda x: 3456 * x % N
    a216 = part(216) // TICK
    b216 = next(b for b in range(TICK) if 5 * b % N == (216 - TICK * a216) % N)
    return {
        "the grain splits twice: it is the five ticks times the twelve multiples of 360, and those twelve are the observer "
        "times the sun, the unique subgroups of orders 4 and 3 in the miss set; all twelve miss; 360 has order 12 and 12 "
        "has order 360": spine.subgroup(TICK) & spine.subgroup(360) == {0}
        and {(x + y) % N for x in spine.subgroup(TICK) for y in spine.subgroup(360)} == spine.subgroup(72)
        and {(x + y) % N for x in spine.subgroup(1080) for y in spine.subgroup(1440)} == spine.subgroup(360)
        and not any(ledger.contains_tick(x) for x in spine.subgroup(360))
        and {x for x in spine.subgroup(5) if spine.order(x) == 4} == {1080, 3240}
        and {x for x in spine.subgroup(5) if spine.order(x) == 3} == {1440, 2880}
        and (spine.order(360), spine.order(12)) == (12, 360),
        "DEEP_COURT: 216 has tick-miss coordinates (4, 216) but residues 1 mod 5 and 216 mod 864; the point with residues "
        "(4, 216) is 1944 = 9 x 216 = 864 + 1080. On the time clock 2 x 3 = 1 and 2 + 3 = 0, one fact since x^2 = -1 mod 5 "
        "has the roots 2 and 3": (a216, b216) == (4, 216) and (216 % 5, 216 % TICK) == (1, 216)
        and next(x for x in range(N) if x % 5 == 4 and x % TICK == 216) == 1944 == 9 * 216 == TICK + 1080
        and (2 * 3 % 5, (2 + 3) % 5) == (1, 0) and [x for x in range(5) if x * x % 5 == 4] == [2, 3],
        "the paper's chart classes corrected: 95, 98 and 101 are one class mod 3, not mod 30 (where they are 5, 8, 11); "
        "30 and 66 are another, 44 joins the first, and 51, 52 differ; every pada address 40p is 0 mod 5":
            [x % 30 for x in (95, 98, 101)] == [5, 8, 11] and [x % 3 for x in (95, 98, 101, 44)] == [2, 2, 2, 2]
            and [x % 3 for x in (30, 66)] == [0, 0] and 51 % 3 != 52 % 3 and all(40 * p % 5 == 0 for p in counts.CHART_PADAS),
        "LEVELS corrected: the field prime 241 is prime to 4320; it is 240 = 241 - 1 that meets the circle in 240":
            gcd(241, N) == 1 and gcd(240, N) == 240,
        "the paper's arithmetic: 1728 : 1296 : 864 : 432 = 4 : 3 : 2 : 1, summing to 4320; 10 x 1728 = 17280, 864 + 1296 = "
        "2160; 64 x 6^3 x 5 = 69120; C(8, 2) = 28 = 6 + 16 + 6; 108 = 21 x 5 + 3, so R^108 = R^3 at order 5":
            [x // 432 for x in (1728, 1296, TICK, 432)] == [4, 3, 2, 1] and 1728 + 1296 + TICK + 432 == N
            and 10 * 1728 == 17280 and TICK + 1296 == 2160 and 64 * 6 ** 3 * 5 == 69120
            and sp.binomial(8, 2) == 28 == 6 + 16 + 6 and 108 % 5 == 3,
        "CLOSURE_092: the unread dimensions 360, 270, 190, 110, 30, 0 step by 90, 80, 80, 80, 30; 90 + 35 = 125; "
        "36 x 360 = 12960 = 360 + 12600": [a - b for a, b in zip((360, 270, 190, 110, 30), (270, 190, 110, 30, 0))]
        == [90, 80, 80, 80, 30] and 90 + 35 == 125 and 36 * 360 == 12960 == 360 + 12600,
    }


# ------------------------------------------------------------------- the 00:36-00:51 notes

def edge_tick():
    """CYCLE_TICK and CUT_TICK: the signed edge tick (the second compound of the vertex 5-cycle) on cycles and cuts."""
    E = carrier.edges()
    B = sp.Matrix(carrier.signed_incidence())
    R5 = sp.Matrix(5, 5, lambda r, c: int(r == (c + 1) % 5))
    T = compound2(R5)
    x = sp.symbols("x")
    phi5 = x ** 4 + x ** 3 + x ** 2 + x + 1
    cycles = sp.Matrix.hstack(*B.nullspace())
    cuts = sp.Matrix.hstack(*[B.T[:, k] for k in range(4)])
    restrict = lambda V: (V.T * V).inv() * V.T * T * V
    G = B.T * B

    def fundamental(k):                                        # the star tree at vertex 0: the triangle 0-i-j
        i, j = E[k]
        v = sp.zeros(10, 1)
        v[k], v[E.index((0, j))], v[E.index((0, i))] = 1, -1, 1
        return v
    F = sp.Matrix.hstack(*[fundamental(k) for k in range(10) if E[k][0] != 0])
    rotor = sp.Matrix.hstack(*[sp.Matrix(counts._oriented_cycle(k)) for k in (1, 2)])
    return {
        "the edge tick has characteristic polynomial (x - 1)^2 Phi_5 on the six cycles (trace 1), Phi_5 on the four cuts "
        "(trace -1) and (x - 1)^2 Phi_5^2 on all ten edges (trace 0); Phi_5(2) = 31 and Phi_5(1) = 5":
            sp.expand(restrict(cycles).charpoly(x).as_expr() - (x - 1) ** 2 * phi5) == 0 and restrict(cycles).trace() == 1
            and sp.expand(restrict(cuts).charpoly(x).as_expr() - phi5) == 0 and restrict(cuts).trace() == -1
            and sp.expand(T.charpoly(x).as_expr() - (x - 1) ** 2 * phi5 ** 2) == 0 and T.trace() == 0
            and (phi5.subs(x, 2), phi5.subs(x, 1)) == (31, 5),
        "the factor (x - 1)^2 is the rotor plane: the edge tick fixes exactly a plane of cycles, the C5-fixed plane "
        "spanned by the near and far pentagons": len((T - sp.eye(10)).nullspace()) == 2
        and rotor.rank() == 2 and sp.Matrix.hstack(rotor, *(T - sp.eye(10)).nullspace()).rank() == 2
        and (B * rotor).is_zero_matrix,
        "the signed edge Gram B^T B squares to 5 B^T B, has trace 20 and spectrum 5^4 0^6, and commutes with the tick; "
        "its complement I - B^T B / 5 is the rank-6 cycle projector": G ** 2 == 5 * G and G.trace() == 20
        and G.eigenvals() == {5: 4, 0: 6} and T * G == G * T and (sp.eye(10) - G / 5).rank() == 6,
        "the star tree's six fundamental triangles have cycle Gram spectrum 1^3 5^3 and determinant 125":
            (B * F).is_zero_matrix and (F.T * F).eigenvals() == {1: 3, 5: 3} and (F.T * F).det() == 125,
        "the cut tick has the time clock's polynomial Phi_5, and the map is the layer-22 join kappa(x) = 4x mod 5, as "
        "the sibling's TOWERS note now says too": 4 * TICK % 5 == 1,
    }


def port_moments():
    """FOUR_ITEMS and REPAIR_AUDIT: the six-port's moment blocks from the bath's return moments."""
    _, E = _walks()
    contrast = [E[k + 1] // 240 for k in range(3)]
    uniform = [6 * E[k] - 5 * E[k + 1] // 240 for k in range(3)]
    return {
        "every root alpha gives the same <delta_0, Delta^k delta_alpha> = F_k (W(E8) is transitive on roots), and summing "
        "over the 240 roots gives F_k = E_k - E_(k+1)/240": all(E[k + 1] % 240 == 0 for k in range(6)),
        "so the six-port block E_k I + F_k (J - I) has contrast moments E_(k+1)/240 = 1, 241, 58264 (variance 183) and "
        "uniform moments 6 E_k - 5 E_(k+1)/240 = 1, 235, 55720 (variance 495): the blocks 241I - J and 183I + 52J of the "
        "cone, and REPAIR_AUDIT's factor 6": contrast == [1, 241, 58264] and contrast[2] - contrast[1] ** 2 == 183
        and uniform == [1, 235, 55720] and uniform[2] - uniform[1] ** 2 == 495,
        "without the factor 6 the uniform line gives E_1 - 5 E_2/240 = -965 (FOUR_ITEMS), and both blocks use only W_0..W_3 "
        "= 1, 0, 240, 13440; W_4 = 1260720": E[1] - 5 * E[2] // 240 == -965 and _walks()[0][:5] == [1, 0, 240, 13440, 1260720],
    }


def notes_0051():
    """The 00:36-00:51 notes: the sibling's audits of the paper's scripts, replayed, and their corrections."""
    R5 = sp.Matrix(5, 5, lambda r, c: int(r == (c + 1) % 5))
    S = sp.Matrix(5, 4, lambda r, c: int(r == c) - int(r == c + 1))
    C = (S.T * S).inv() * S.T * R5 * S
    T6 = sp.diag(2 * sp.eye(4) - C, sp.Matrix([[5]]))

    def minors(M):
        return {abs(M.extract(list(r), list(c)).det()) for k in range(1, M.rows + 1)
                for r in itertools.combinations(range(M.rows), k) for c in itertools.combinations(range(M.rows), k)}
    x = sp.symbols("x")
    crit = [240, 16, -3, -8, -10, -11, Fraction(-185, 16), Fraction(-320, 27), -12, -16]
    R = sp.Poly(sp.prod([x - 240, x - 16, x + 3, x + 8, x + 10, x + 11, 16 * x + 185, 27 * x + 320, x + 12, x + 16]), x)
    roots = glue.roots()
    w = np.array([28, 28, 6, 2, 1, 0, 0, 0]) / 10
    grad = (roots * np.sin(roots @ w)[:, None]).sum(axis=0)
    H = (roots.T * np.cos(roots @ w)) @ roots
    n = grad / np.linalg.norm(grad)
    tangent = sorted(np.linalg.eigvalsh((np.eye(8) - np.outer(n, n)) @ H @ (np.eye(8) - np.outer(n, n))))[1:]
    port = np.linalg.eigvalsh(native.port_metric())
    spec = carrier.spectrum_multiplicities()
    pair_orbits = {frozenset(tuple(sorted(((a + k) % 6, (b + k) % 6))) for k in range(6))
                   for a, b in itertools.combinations(range(6), 2)}
    return {
        "the companion C of Phi_5 (the vertex rotation on the sum-zero hyperplane, in the basis e_i - e_(i+1)) has "
        "det(2I - C) = 31 and det(I - C) = 5; T6 = (2I - C) + [5] has det 155 and Gram det 24025, and 4805 = 24025 / 5 = "
        "31 x 155 is not a minor of T6 nor of its Gram (MASTER_LEDGER)":
            C == sp.Matrix([[0, 0, 0, -1], [1, 0, 0, -1], [0, 1, 0, -1], [0, 0, 1, -1]])
            and ((2 * sp.eye(4) - C).det(), (sp.eye(4) - C).det(), T6.det(), (T6.T * T6).det()) == (31, 5, 155, 24025)
            and 4805 not in minors(T6) and 4805 not in minors(T6.T * T6) and 4805 == 31 * 155,
        "the two collar fractions differ (PASS2): (15/13)(1/25) = 3/65, while on the cone d^2 = (3/13) r^2 a Euclidean "
        "square 1/25 gives r^2 = 13/400 and (15/13)(13/400) = 3/80": Fraction(15, 13) * Fraction(1, 25) == Fraction(3, 65)
        and Fraction(1, 25) / (1 + Fraction(3, 13)) == Fraction(13, 400) and Fraction(15, 13) * Fraction(13, 400) == Fraction(3, 80),
        "the ten critical values sum to 74557/432 (185/16 + 320/27 = 10115/432), so 432 R(x) has x^9 coefficient -74557 "
        "and R(x)(x + 12) has -69373, as FOUR_ITEMS and REPAIR_AUDIT say": sum(Fraction(v) for v in crit) == Fraction(74557, 432)
        and Fraction(185, 16) + Fraction(320, 27) == Fraction(10115, 432) and R.all_coeffs()[:2] == [432, -74557]
        and sp.Poly(R.as_expr() * (x + 12), x).all_coeffs()[:2] == [432, -69373],
        "at the collar witness the gradient has length 24.927 and the tangent Hessian of the level set is positive, least "
        "eigenvalue 6.986 (not 5.0708); the endpoints stay uncertified": abs(np.linalg.norm(grad) - 24.927) < 1e-3
        and abs(tangent[0] - 6.986) < 1e-3 and min(tangent) > 0,
        "the port metric's eigenvalues sum to 112/5 and multiply to 320; (-5/2, -1/2, ..., -1/2) meets exactly 8 roots, "
        "at 3, and (2, 0, ..., 0) exactly 14, at 2; |W(E8)| / 8! = 17280 and |W(E8)| / |W(D7)| = 2160":
            np.isclose(port.sum(), 112 / 5) and np.isclose(np.prod(port), 320)
            and sum(np.isclose(r @ np.array([-2.5] + [-0.5] * 7), 3) for r in roots) == 8
            and sum(np.isclose(r @ np.array([2.0] + [0.0] * 7), 2) for r in roots) == 14
            and 696729600 // sp.factorial(8) == 17280 and 696729600 // (2 ** 6 * sp.factorial(7)) == 2160,
        "the fourteen are e_1 +- e_j; the roots are 112 integer and 128 half-integer, so 240 - (112 - 128) = 256, the "
        "dispersion's top (PASS2, REPAIR_AUDIT)": all(np.isclose(r[0], 1) and np.isclose(np.abs(r[1:]).sum(), 1)
                                                     for r in roots if np.isclose(2 * r[0], 2))
        and sum(np.allclose(r, np.round(r)) for r in roots) == 112 and 240 - (112 - 128) == 256,
        "the carrier D^2 has trace 40 and its square trace 200, so 9/40 is 9 over the carrier trace; the identity does "
        "not put it in the action (MASTER_LEDGER, JOIN_ALL)": sum(k * m for k, m in spec.items()) == 40
        and sum(k * k * m for k, m in spec.items()) == 200,
        "DEEP36_LOOP and PASS2: 4320 = 1 mod 7 (no element of order 7); 48 divisors; C(n, 2) = 2n only at n = 5, and the "
        "middle binomial exceeds 2n for 6 <= n < 200": N % 7 == 1 and len(sp.divisors(N)) == 48
        and [k for k in range(1, 300) if k * (k - 1) == 4 * k] == [5] and all(sp.binomial(k, k // 2) > 2 * k for k in range(6, 200)),
        "the paper's 3985/16 and 6784/27 are misprints of the critical energies 240 + 185/16 = 4025/16 = (5/4)^2 x 161 "
        "and 240 + 320/27 = 6800/27 = (20/9)^2 x 51, so its factorizations are right and two of its energies wrong. "
        "DEEP36_LOOP keeps the misprints and changes the square-free parts to 3985 and 318; the census's parts stay 161 "
        "and 51, and layer 18's density on T^9 stands": Fraction(3985, 16) != Fraction(5, 4) ** 2 * 161
        and Fraction(6784, 27) != Fraction(20, 9) ** 2 * 51 and 240 + Fraction(185, 16) == Fraction(4025, 16) == Fraction(5, 4) ** 2 * 161
        and 240 + Fraction(320, 27) == Fraction(6800, 27) == Fraction(20, 9) ** 2 * 51
        and [snapshot.squarefree_part(sp.Rational(a, b)) for a, b in ((3985, 16), (6784, 27), (4025, 16), (6800, 27))]
        == [3985, 318, 161, 51],
        "JOIN_ALL and DEEP36_LOOP on the circle: 216 = 6 x 36 has order 20, the golden companion's period mod 5; the "
        "address step 36 and seven of them, 252, have order 120, the step 120 order 36 and 720 order 6; the coil is 27 "
        "returns (540 = lcm(20, 27)); a 6-cycle splits the fifteen pairs into orbits 6, 6, 3; 252 - 7 = 245, 252 + 4 = "
        "256, 2^5 - 1 = 31 nonempty faces of the 4-simplex, 16 x 4320 = 69120": 216 == 6 * 36 and spine.order(216) == 20
        and [spine.order(s) for s in (36, 252, 120, 720)] == [120, 120, 36, 6] and 540 == sp.ilcm(20, 27) == 27 * 20
        and sorted(len(o) for o in pair_orbits) == [3, 6, 6] and (252 - 7, 252 + 4, 2 ** 5 - 1, 16 * N) == (245, 256, 31, 69120),
    }


def splits_corrections():
    """The separate model's splits receipt (00:49): its five source corrections, replayed."""
    loops = {frozenset((c + 216 * k) % N for k in range(20)) for c in range(N)}
    agree = {x for x in range(N) if 4 * x % N == TICK * x % N}
    cycle = {216 * n % N for n in (4, 8, 12, 16)}                          # the tick cycle of doubling, in the golden orbit
    golden = [216 * n % N for n in range(20) if n % 5]
    return {
        "POWER_TOWER and LEVELS: the tower of fives freezes, at 245 from height 3; an early 3125 does not stop it":
            pow(5, 5, N) == 3125 and pow(5, 3125, N) == pow(5, 5 ** 3125, N) == 245,
        "SPINE_29: there are 216 golden loops in all, the golden orbit among them, so 215 others": len(loops) == 216
        and frozenset(spine.subgroup(216)) in loops and len(loops) - 1 == 215,
        "TWO_AGREE: two doublings and 864 copies agree on the 20 points of the golden orbit, so 4300 points disagree in "
        "all, the point 1 among them": agree == spine.subgroup(216) and N - len(agree) == 4300 and 1 not in agree,
        "LEVELS: doubling brings every golden point of index prime to 5 into the tick cycle after two doublings; one "
        "doubling misses the cycle exactly for the odd indices": all(4 * g % N in cycle for g in golden)
        and {n for n in range(20) if n % 5 and 2 * 216 * n % N not in cycle} == {n for n in range(20) if n % 5 and n % 2},
    }


# ------------------------------------------------------------------- the 00:53-01:54 notes and release K

def root_scheme():
    """ROOT_SPECTRUM, GRAM_28, ORTHOGONAL_126 and Canon K: the root graph is an association scheme."""
    R = glue.roots()
    ip = np.rint(R @ R.T).astype(int)
    A, Mn, P = ((ip == v).astype(float) for v in (1, -1, -2))
    order = [2, 1, 0, -1, -2]
    cls = {v: np.nonzero(ip[0] == v)[0] for v in order}
    Bm = np.array([[int(A[cls[a][0], cls[b]].sum()) for b in order] for a in order])
    w, V = np.linalg.eigh(A)
    P28 = V[:, np.isclose(w, 28)] @ V[:, np.isclose(w, 28)].T
    orth = R[ip[0] == 0]
    orth_keys = {tuple(np.rint(2 * r).astype(int)) for r in orth}
    sums = Counter(map(tuple, np.rint(2 * (R[:, None, :] + R[None, :, :])).reshape(-1, 8).astype(int).tolist()))
    classes = Counter((sum(v * v for v in x) // 4, c) for x, c in sums.items())
    wrong = {56: 1, 8: 35, -4: 84, -2: 120}
    return {
        "from any root the other 239 lie at inner products 1, 0, -1, -2 in classes 56, 126, 56, 1, and the neighbour counts "
        "between classes are constant, with the intersection matrix of ROOT_SPECTRUM; its eigenvalues are 56, 28, 8, -2, "
        "-4": [len(cls[v]) for v in order] == [1, 56, 126, 56, 1]
        and all(len({int(A[i, cls[b]].sum()) for i in cls[a]}) == 1 for a in order for b in order)
        and Bm.tolist() == [[0, 56, 0, 0, 0], [1, 27, 27, 1, 0], [0, 12, 32, 12, 0], [0, 1, 27, 27, 1], [0, 0, 0, 56, 0]]
        and np.allclose(sorted(np.linalg.eigvals(Bm).real), [-4, -2, 8, 28, 56]),
        "the 240 x 240 Gram 2I + A - M - 2P is 60 times the projector onto the eigenvalue-28 space (GRAM_28): eigenvalue 28 "
        "is the coordinate space": np.allclose(2 * np.eye(240) + A - Mn - 2 * P, R @ R.T) and np.allclose(R @ R.T, 60 * P28),
        "the 126 roots orthogonal to a root are closed under their reflections, of rank 7: the E7 roots, with frame 36 P = "
        "2 h(E7) P, h(E7) = 126 / 7 = 18 (ORTHOGONAL_126's 4320 / 240 = 18 is the same integer)": len(orth) == 126
        and all(tuple(np.rint(2 * (b - (a @ b) * a)).astype(int)) in orth_keys for a in orth for b in orth)
        and np.linalg.matrix_rank(orth) == 7 and np.allclose(orth.T @ orth, 36 * (np.eye(8) - np.outer(R[0], R[0]) / 2)),
        "ordered pair sums r + s fall in classes (norm^2, count, multiplicity) (0, 1, 240), (2, 240, 56), (4, 2160, 14), "
        "(6, 6720, 2), (8, 240, 1), so W_3 = tr A^2 = 240 x 56 = 13440 and W_4 = sum of squared multiplicities = 1260720 "
        "(Canon K)": sorted(classes.items()) == [((0, 240), 1), ((2, 56), 240), ((4, 14), 2160), ((6, 2), 6720), ((8, 1), 240)]
        and int(round(np.trace(A @ A))) == 13440 and sum(c * c for c in sums.values()) == 1260720,
        "the separate script's list 56, 8^35, (-4)^84, (-2)^120 has trace -240 and power sums over 240 of 1, -1, 30, 780, "
        "41672 (MASTER_LEDGER, SPECTRA): it put the eight coordinate directions on -2": [
            sum(m * v ** n for v, m in wrong.items()) // 240 for n in range(5)] == [1, -1, 30, 780, 41672],
    }


def frame_cliques():
    """INDEX_VECTOR and SIBLING_AGREEMENT: the frame's index vector, and two maximal cliques through each face."""
    e = lambda i: np.eye(8)[i]
    F = np.array([-e(0) - e(i) for i in range(1, 8)] + [-0.5 * np.ones(8)])
    R = glue.roots()
    half = {tuple(np.rint(2 * r).astype(int)) for r in R}
    key = lambda v: tuple(np.rint(2 * v).astype(int))
    q = F.sum(axis=0) / 3

    def common(points):
        out = None
        for p in points:
            nb = {tuple(a + b for a, b in zip(key(p), r)) for r in half}
            out = nb if out is None else out & nb
        return out - {key(p) for p in points}
    adjacent = lambda x, y: tuple(a - b for a, b in zip(x, y)) in half
    frame = {key(p) for p in F}
    faces = [[np.zeros(8)] + [F[i] for i in S] for S in itertools.combinations(range(8), 5)]

    def prism(face):
        c = common(face)
        inside, outside = c & frame, c - frame
        matched = [[y for y in inside if adjacent(x, y)] for x in outside]
        return (len(inside) == len(outside) == 3 and all(adjacent(x, y) for x, y in itertools.combinations(outside, 2))
                and all(len(m) == 1 for m in matched) and len({m[0] for m in matched}) == 3)
    return {
        "the eight frame roots sum to 3q with q a lattice vector of squared length 8, and q meets the 240 roots in -3..3 "
        "with class sizes 8, 28, 56, 56, 56, 28, 8 (INDEX_VECTOR)": np.isclose(q @ q, 8)
        and sorted(Counter(int(round(v)) for v in R @ q).items()) == [(-3, 8), (-2, 28), (-1, 56), (0, 56), (1, 56), (2, 28), (3, 8)],
        "each six-point face (the origin and five frame roots) has six common neighbours forming a triangular prism: the "
        "frame's other three, three outside points that complete the face to a second 9-clique, and a perfect matching "
        "between them. So 'three extensions' holds for each clique, and every face lies in exactly two maximal cliques":
            all(prism(f) for f in faces),
        "two adjacent sites of a face have 56 common neighbours, four of them the face's other sites: 52 outside, so in "
        "183 + 6 x (56 - 4) = 495 the 4 is the face's four other sites, not the cut rank (CUMULANT_183)": all(
            len(common(f[a:a + 1] + f[b:b + 1])) == 56 and len(common(f[a:a + 1] + f[b:b + 1]) & {key(p) for p in f}) == 4
            for f in faces[:4] for a, b in itertools.combinations(range(6), 2)) and 183 + 6 * (56 - 4) == 495,
    }


def simplex_grades():
    """TRIANGLES, TETRAHEDRA, ALL_GRADES and FIVE_CLOCK_COPIES: the 4-simplex and the tick on every grade."""
    faces = {k: list(itertools.combinations(range(5), k + 1)) for k in range(5)}

    def boundary(k):
        M = sp.zeros(len(faces[k - 1]), len(faces[k]))
        for j, f in enumerate(faces[k]):
            for i in range(len(f)):
                M[faces[k - 1].index(f[:i] + f[i + 1:]), j] += (-1) ** i
        return M

    def turn(k):
        M = sp.zeros(len(faces[k]), len(faces[k]))
        for j, f in enumerate(faces[k]):
            g = [(v + 1) % 5 for v in f]
            M[faces[k].index(tuple(sorted(g))), j] = Permutation(sorted(range(len(g)), key=lambda t: g[t])).signature()
        return M
    x = sp.symbols("x")
    phi5 = x ** 4 + x ** 3 + x ** 2 + x + 1
    expected = [(x - 1) * phi5, ((x - 1) * phi5) ** 2, ((x - 1) * phi5) ** 2, (x - 1) * phi5, x - 1]
    orbits = lambda k: len({frozenset(tuple(sorted((v + s) % 5 for v in f)) for s in range(5)) for f in faces[k]})
    return {
        "the 4-simplex's boundaries from edges, triangles, tetrahedra and the body have ranks 4, 6, 4, 1, each composition "
        "is zero, and the only homology is the point: the triangles fill the cycles, Euler characteristic 1":
            [boundary(k).rank() for k in range(1, 5)] == [4, 6, 4, 1]
            and all((boundary(k) * boundary(k + 1)).is_zero_matrix for k in range(1, 4)) and 5 - 10 + 10 - 5 + 1 == 1,
        "the signed rotation commutes with every boundary and has polynomial (x - 1) Phi_5 on vertices and tetrahedra, "
        "(x - 1)^2 Phi_5^2 on edges and triangles, x - 1 on the body: the orbits 1, 2, 2, 1, 1 are copies of the "
        "five-clock's regular representation (ALL_GRADES, FIVE_CLOCK_COPIES)": all(
            turn(k - 1) * boundary(k) == boundary(k) * turn(k) for k in range(1, 5))
        and all(sp.expand(turn(k).charpoly(x).as_expr() - expected[k]) == 0 for k in range(5))
        and [orbits(k) for k in range(5)] == [1, 2, 2, 1, 1],
        "the 31 nonempty faces are Phi_5(2) = 2^5 - 1; the 63 nonempty subsets of a five-cycle and an anchor make 15 "
        "orbits (3 fixed, 12 of five); a subset's polynomial is divisible by Phi_5 only for the empty and full set, so "
        "every proper nonempty subset meets both golden planes (SUPPORT15, SUPPORT_FACES)": phi5.subs(x, 2) == 2 ** 5 - 1 == 31
        and len({frozenset(frozenset((v + s) % 5 if v < 5 else 5 for v in S) for s in range(5))
                 for n in range(1, 7) for S in itertools.combinations(range(6), n)}) == 15
        and [S for n in range(6) for S in itertools.combinations(range(5), n)
             if sp.rem(sum((x ** v for v in S), sp.Integer(0)), phi5, x) == 0] == [(), (0, 1, 2, 3, 4)],
    }


def golden_split():
    """TICK_SPLIT, GOLDEN_EIGENSPACES and GOLDEN_MATCH: Phi_5 splits over the golden field, and B acts on the edges."""
    T = np.array(compound2(sp.Matrix(5, 5, lambda r, c: int(r == (c + 1) % 5))), float)
    pentagon, pentagram = (np.array(counts._oriented_cycle(k), float).ravel() for k in (1, 2))
    average = sum(np.linalg.matrix_power(T, k) for k in range(5)) / 5
    S = T + T.T
    w, V = np.linalg.eigh(S)
    B = np.array(carrier.signed_incidence(), float)
    cuts = B.T @ B / 5
    golden = np.eye(10) - average
    X = -S @ golden
    x, phi = sp.symbols("x"), (1 + sp.sqrt(5)) / 2
    split = lambda lam: (lambda Vl: (Vl.shape[1], round(np.trace(Vl.T @ (np.eye(10) - cuts) @ Vl)),
                                     round(np.trace(Vl.T @ cuts @ Vl))))(V[:, np.isclose(w, lam)])
    return {
        "the tick's fixed space is spanned by the oriented pentagon and pentagram, orthogonal, of squared length 5, and the "
        "average of its five powers is the sum of their rank-one projectors; rank(T - I) = 8 (TICK_SPLIT)":
            np.linalg.matrix_rank(T - np.eye(10)) == 8 and np.isclose(pentagon @ pentagram, 0)
            and np.isclose(pentagon @ pentagon, 5) and np.isclose(pentagram @ pentagram, 5)
            and np.allclose(average, (np.outer(pentagon, pentagon) + np.outer(pentagram, pentagram)) / 5),
        "T + T^-1 has eigenvalues 2 (the two fixed cycles), 2 cos 72 = (sqrt5 - 1)/2 and 2 cos 144 = -(sqrt5 + 1)/2, four "
        "each, and each golden space is two cycle and two cut directions (GOLDEN_EIGENSPACES)": Counter(
            np.round(w, 9).tolist()) == Counter({2.0: 2, round((5 ** 0.5 - 1) / 2, 9): 4, round(-(5 ** 0.5 + 1) / 2, 9): 4})
        and split((5 ** 0.5 - 1) / 2) == split(-(5 ** 0.5 + 1) / 2) == (4, 2, 2),
        "on the eight golden directions X = -(T + T^-1) satisfies X^2 = X + I, the golden companion's equation, so "
        "B -> -(T + T^-1) represents Z[B] there; Phi_5 = (x^2 + phi x + 1)(x^2 + (1 - phi) x + 1), whose linear "
        "coefficients are the eigenvalues of B (GOLDEN_MATCH)": np.allclose(X @ X, X + golden)
        and sp.expand((x ** 2 + phi * x + 1) * (x ** 2 + (1 - phi) * x + 1)) == sp.expand(sum(x ** k for k in range(5)))
        and set(sp.Matrix([[1, 1], [1, 0]]).eigenvals()) == {phi, 1 - phi},
        "a cycle readout's unseen part is the cut space, which the tick keeps, so the visible quotient carries its own step "
        "and recovers 10 - 4 = 6 directions (OBSERVABLE; Canon K's descent criterion)": np.allclose(T @ cuts, cuts @ T)
        and np.linalg.matrix_rank(cuts) == 4,
    }


def notes_0154():
    """The 00:53-01:54 notes and release K: arithmetic, the separate model's corrections and four of our own."""
    x, u = sp.symbols("x u")
    phi5 = x ** 4 + x ** 3 + x ** 2 + x + 1
    chern = sp.Poly(sp.expand((1 + u) ** 5), u).all_coeffs()[::-1]
    rng = np.random.default_rng(154)
    unit = lambda: (lambda z: z / np.linalg.norm(z))(rng.standard_normal(3) + 1j * rng.standard_normal(3))
    bargmann = max(abs(np.vdot(a, b) * np.vdot(b, c) * np.vdot(c, a)) for a, b, c in ((unit(), unit(), unit()) for _ in range(500)))
    B = sp.Matrix([[1, 1], [1, 0]])
    carry = lambda p, q: ((p[0] + q[0]) % 36, (p[1] + q[1] + (p[0] + q[0]) // 36) % 120)
    coords = lambda j: (j % 36, j // 36)
    picks = [(int(a), int(b)) for a, b in rng.integers(0, N, (200, 2))]
    exps = [sp.factorint(n) for n in (3, 7, 14, 10, 62, 51, 161, 251)]
    primes = sorted({p for e in exps for p in e})
    E2 = [[e.get(p, 0) % 2 for p in primes] for e in exps]
    products = [sp.prod([n for n, b in zip((3, 7, 14, 10, 62, 51, 161, 251), bits) if b])
                for bits in itertools.product((0, 1), repeat=8)]
    free = lambda n: sp.prod([p for p, k in sp.factorint(n).items() if k % 2])
    return {
        "GOLDEN_GRAVITY corrected: the circle's subgroups of orders 120, 60, 30 and 10 are <36>, <72>, <144> and <432>, and "
        "each contains the ticks, since 5 divides its order (the order-5 subgroup is unique, and 864 = 2 x 432)": all(
            spine.subgroup(TICK) <= spine.subgroup(N // d) for d in (120, 60, 30, 10)),
        "the separate model's corrections replayed: c(CP4) = (1 + u)^5 with u^5 = 0, so the formal sixth coefficient "
        "vanishes and p1 = c1^2 - 2 c2 = 5u^2; a rank-9 map is excluded only into a parallelizable target such as the "
        "Hermitian 3 x 3 matrices; the full edge polynomial is 0 at 1 and 961 at 2, the cycle polynomial 0 and 31":
            chern == [1, 5, 10, 10, 5, 1] and chern[1] ** 2 - 2 * chern[2] == 5
            and [((x - 1) ** 2 * phi5 ** 2).subs(x, v) for v in (1, 2)] == [0, 961]
            and [((x - 1) ** 2 * phi5).subs(x, v) for v in (1, 2)] == [0, 31],
        "the hub's conflicts replayed: three rank-one projections have |Tr P1 P2 P3| <= 1 < |1 + i|; t^6 - 1 is not "
        "(t^5 - 1)(t - 1); over Q, B^19 = 4181 B + 2584 I is not B^-1 = B - I, while mod 5 it is": bargmann <= 1 + 1e-12
        and abs(1 + 1j) > 1 and sp.expand(x ** 6 - 1 - (x ** 5 - 1) * (x - 1)) != 0
        and B ** 19 == 4181 * B + 2584 * sp.eye(2) and B ** 19 != B.inv() and B.inv() == B - sp.eye(2)
        and (B ** 19 - B.inv()).applyfunc(lambda e: e % 5).is_zero_matrix,
        "Canon K's carry clock: j = a + 36 b adds with the carry floor((a + a') / 36), the extension of Z/36 by <36> does "
        "not split (Z/36 x Z/120 has largest order 360), and the moon 120 has order 36 but image 12 of order 3, while the "
        "sun 1440 maps to 0": all(carry(coords(a), coords(b)) == coords((a + b) % N) for a, b in picks)
        and sp.ilcm(36, 120) == 360 and spine.order(120) == 36 and 120 % 36 == 12 and 36 // gcd(12, 36) == 3 and 1440 % 36 == 0,
        "SEVEN_TWENTY: an element of order 5 splits 360 points into 72 five-cycles and the ten edges into two, so the "
        "equivariant maps form a space of dimension 72 x 2 x 5 = 720, and clock matching does not pick one":
            360 // 5 == 72 and 72 * 2 * 5 == 720,
        "HESSIAN_RECOMPUTE's certificate, corrected: the prime-exponent matrix of 3, 7, 14, 10, 62, 51, 161, 251 is "
        "invertible over F2, so the 256 subset products have distinct square-free parts, which is what independence needs; "
        "the products are not all square-free (7 x 14 = 98 = 2 x 7^2; 196 of 256 are not). The parts are the census's 161 "
        "and 51, now used by the sibling too": spacetime.rank_mod_p(E2, 2) == 8 and len(primes) == 8
        and len({free(n) for n in products}) == 256 and 7 * 14 == 98 == 2 * 7 ** 2
        and sum(1 for n in products if n > 1 and free(n) != n) == 196,
        "the spine's arithmetic: 36 x 360 = 12960 coordinates, 192 - 9 = 183 flat directions, 100 + 19 + 50 = 169 = 13^2, "
        "the quadratic with discriminant 120 has roots 6 +- sqrt30, and (sqrt5 - 1)/2 + (sqrt5 + 1)/2 = sqrt5":
            36 * 360 == 12960 and 192 - 9 == 183 and 100 + 19 + 50 == 169 == 13 ** 2
            and set(sp.solve(x ** 2 - 12 * x + 6, x)) == {6 - sp.sqrt(30), 6 + sp.sqrt(30)} and 12 ** 2 - 4 * 6 == 120,
    }


# ------------------------------------------------------------------- every layer, every level

def projective_line():
    """PGL(2,5) and PSL(2,5) as permutations of the projective line F5 + {infinity}, with infinity = 5."""
    def mobius(a, b, c, d):                                    # x -> (a x + b) / (c x + d)
        inv = lambda y: pow(y, 3, 5)
        image = lambda x: ((a * inv(c) % 5 if c else 5) if x == 5
                           else 5 if (c * x + d) % 5 == 0 else (a * x + b) * inv(c * x + d) % 5)
        return tuple(image(x) for x in range(6))
    det = lambda m: (m[0] * m[3] - m[1] * m[2]) % 5
    pgl = {mobius(*m) for m in itertools.product(range(5), repeat=4) if det(m)}
    psl = {mobius(*m) for m in itertools.product(range(5), repeat=4) if det(m) in (1, 4)}
    return pgl, psl


def surface():
    """Layer 3's RP^2 and J5: its 1-skeleton is K6, and its triangles are an orbit of PSL(2,5)."""
    tri, comp = spacetime.rp2_triangulations()
    pgl, psl = projective_line()
    image = lambda s, F: {tuple(sorted(s[i] for i in f)) for f in F}
    orbit = lambda t: {tuple(sorted(s[i] for i in t)) for s in psl}
    phi = next(p for p in itertools.permutations(range(6)) if p[5] == 5 and image(p, tri) == orbit(min(image(p, tri))))
    A, Ac = image(phi, tri), image(phi, comp)
    aut = [s for s in itertools.permutations(range(6)) if image(s, tri) == set(tri)]
    steps = lambda F: {(b - a) % 5 for a, b, c in F if c == 5} | {(a - b) % 5 for a, b, c in F if c == 5}
    E = carrier.edges()
    M = np.array(carrier.signless_incidence(), float)
    D = np.array(carrier.dirac(carrier.signless_incidence()), float)
    skeleton = {p for f in tri for p in itertools.combinations(f, 2)}
    atoms = [(i, 5) for i in range(5)] + E
    LG = np.array([[1.0 if a != b and set(a) & set(b) else 0.0 for b in atoms] for a in atoms])
    block = np.zeros((15, 15))
    block[:5, :5], block[5:, 5:] = np.ones((5, 5)) - np.eye(5), M.T @ M - 2 * np.eye(10)
    return {
        "the hemi-icosahedron on the six axes has 1-skeleton K6, the ten K5 edges and five spokes to a cone point, and "
        "D = A(line graph of K6) - diag(J - I, M^T M - 2I) (J5)": len(skeleton) == 15 and np.allclose(D, LG - block),
        "its 60 symmetries are transitive on the axes; labelled by the projective line over F5 (the cone point at "
        "infinity), it and its complement are the two PSL(2,5)-orbits of triangles, and the 60 elements of PGL(2,5) "
        "outside PSL(2,5) swap them": len(aut) == 60 and len({s[0] for s in aut}) == 6 and A == orbit(min(A))
        and Ac == orbit(min(Ac)) and len(A | Ac) == 20 and all(image(s, A) == Ac for s in pgl - psl),
        "at infinity the hemi-icosahedron's link is the pentagram (steps +-2) and its complement's is the pentagon "
        "(steps +-1), the far and near cycles of the rotor plane": steps(A) == {2, 3} and steps(Ac) == {1, 4},
    }


def cube_cuts():
    """The four-cube's vertices are the cuts of K5 over F2, and a cube edge adds one vertex star."""
    E = carrier.edges()
    B2 = np.array(carrier.signed_incidence(), int) % 2
    cut = lambda S: tuple(int((i in S) != (j in S)) for i, j in E)
    add = lambda a, b: tuple((p + q) % 2 for p, q in zip(a, b))
    cube = list(itertools.product((0, 1), repeat=4))
    f = {x: cut({k + 1 for k in range(4) if x[k]}) for x in cube}
    cuts = {tuple(np.array(c) @ B2 % 2) for c in itertools.product((0, 1), repeat=5)}
    stars = [cut({i}) for i in range(5)]
    return {
        "x -> the cut of {i : x_i = 1} is linear and maps the sixteen vertices of the four-cube onto the sixteen cuts "
        "of K5 over F2, the row space of B mod 2": len(set(f.values())) == 16 and set(f.values()) == cuts
        and all(f[tuple((a + b) % 2 for a, b in zip(x, y))] == add(f[x], f[y]) for x in cube for y in cube),
        "two vertices are adjacent in the cube exactly when their cuts differ by the star of a vertex 1..4, and the "
        "antipode 1111 goes to the fifth star: the four qubits are the four independent cuts": all(
            (sum(a != b for a, b in zip(x, y)) == 1) == (add(f[x], f[y]) in stars[1:]) for x in cube for y in cube)
        and f[(1, 1, 1, 1)] == stars[0],
    }


def golden_clock():
    """The golden companion and the golden clock of W(E8) are both cyclic of order 20, with the tick as fourth power."""
    _, v = ledger.golden_clock()
    _, _, _, _, g, _ = spine.spine_clock()
    B = sp.Matrix([[1, 1], [1, 0]])
    mod5 = lambda X: X.applyfunc(lambda e: e % 5)
    return {
        "B mod 5 and the golden clock v both have order 20, and v^4 is the tick g, so B^k -> v^k is an isomorphism "
        "of the two cyclic groups taking B^4 to g (a selection: any generator could be matched)":
            next(k for k in range(1, 41) if mod5(B ** k) == sp.eye(2)) == 20 and spine.mat_order(v) == 20
            and np.array_equal(np.linalg.matrix_power(v, 4), g),
    }


@functools.lru_cache(maxsize=1)
def _census():
    return handover.critical_census()


def _tick_fixed_momenta():
    _, _, _, _, g, _ = spine.spine_clock()
    G = spine.to_standard(g)
    simple = np.array([0.5 * np.array([1, -1, -1, -1, -1, -1, -1, 1]), np.eye(8)[0] + np.eye(8)[1]]
                      + [np.eye(8)[k + 1] - np.eye(8)[k] for k in range(6)])
    Minv = np.linalg.inv(G - np.eye(8))
    pts = {}
    for c in itertools.product(range(5), repeat=8):
        x = Minv @ (np.array(c) @ simple)                      # k / 2 pi, fixed by g mod Lambda
        key = tuple(np.round((np.linalg.solve(simple.T, x) % 1.0) * 5).astype(int) % 5)
        pts.setdefault(key, x)
        if len(pts) == 25:
            break
    return simple, list(pts.values())


def dual_torus():
    """E8 is unimodular, so the momenta live on R^8 / 2 pi E8, where the tick has 25 fixed points."""
    simple, pts = _tick_fixed_momenta()
    _, _, _, _, g, _ = spine.spine_clock()
    G = spine.to_standard(g)
    return {
        "the Cartan matrix of E8 has determinant 1, so E8* = E8 and the momentum torus is R^8 / 2 pi E8":
            round(np.linalg.det(simple @ simple.T)) == 1,
        "on it the tick has |det(g - I)| = 25 fixed points": round(abs(np.linalg.det(G - np.eye(8)))) == 25 and len(pts) == 25,
    }


def census():
    """Layer 16: the band's critical census on the alcove."""
    fam = _census()
    return {
        "eps = 240 - sum cos(2 pi r.x) has 11 nondegenerate critical families on the alcove's vertices and edges, "
        "243600 points with Morse sum 0": len(fam) == 11 and sum(f["orbit"] for f in fam.values()) == 243600
        and sum((-1) ** f["index"] * f["orbit"] for f in fam.values()) == 0 and all(f["nondegenerate"] for f in fam.values()),
    }


def critical_momenta():
    """The tick's fixed momenta are critical points of the band."""
    R = glue.roots()
    _, pts = _tick_fixed_momenta()
    kinds = Counter()
    for x in pts:
        gradient = (np.sin(2 * np.pi * R @ x)[:, None] * R).sum(axis=0)
        kinds[(handover.stabiliser(R, x)[0], int(round(240 - np.cos(2 * np.pi * R @ x).sum())),
               bool(np.linalg.norm(gradient) < 1e-9))] += 1
    a4 = next(f for (_, t), f in _census().items() if t == "A4+A4")
    return {
        "the tick's 25 fixed momenta are critical points of the band: the minimum (type E8, eps 0) and 24 points of the "
        "A4 + A4 family (eps 250, index 4, 48384 points in all)": kinds == Counter({("E8", 0, True): 1, ("A4+A4", 250, True): 24})
        and a4["orbit"] == 48384 and a4["index"] == 4,
    }


def _critical_values():
    values = Counter()
    for f in _census().values():
        q = Fraction(f["lambda"]).limit_denominator(1000)
        values[sp.Rational(q.numerator, q.denominator)] += 1
    return values


def census_walks():
    """The critical values are the in-band characteristic roots of the walk recurrence."""
    dat, _ = recurrence.load_operator()
    band = {sp.Rational(r): m for r, m in dat["characteristic_roots"].items() if -16 <= sp.Rational(r) <= 240}
    return {
        "the 11 critical values 240 - eps, with their multiplicities, are the in-band characteristic roots of the "
        "order-16 recurrence of W_n (layer 14)": dict(_critical_values()) == band,
    }


def nine_torus():
    """Layer 18: the nine positive critical energies give a dense flow on T^9."""
    eps = sorted({240 - v for v in _critical_values()} - {0})
    parts = [snapshot.squarefree_part(e) for e in eps]
    return {
        "the nine positive critical energies are 224, 243, 248, 250, 251, 4025/16, 6800/27, 252, 256; their square-free "
        "parts 14, 3, 62, 10, 251, 161, 51, 7, 1 are distinct, so the square roots are independent over Q and the flow "
        "of the nine frequencies is dense on T^9 (Besicovitch, Kronecker)": eps == sorted(
            [224, 243, 248, 250, 251, sp.Rational(4025, 16), sp.Rational(6800, 27), 252, 256])
        and parts == [14, 3, 62, 10, 251, 161, 51, 7, 1] and len(set(parts)) == 9,
    }


def literal_port():
    """Layer 10: the owner's operands give the reconstructed port up to a commutant element."""
    d = literal.load()
    cmp = literal.compare_with_reference(d)
    Pn = d["P_native_to_boundary_order"]
    return {
        "native_matrices_input.json hashes to the canon's 73e07429..., and its W_p in boundary order is the "
        "reconstruction's exactly": literal.sha256() == literal.SHA256
        and np.allclose(np.array(Pn * d["Wp_source_HS"] * Pn.T, dtype=float), native.port_metric()),
        "the literal port is U times the reconstructed one, U a W_p-isometry commuting with the C5 rotation":
            cmp["fit_residual"] < 1e-9 and cmp["Wp_isometry_residual"] < 1e-9 and cmp["commutes_with_boundary_rotation"] < 1e-9,
    }


def measure():
    """Layer 15: the six-port's sector moments are moments of measures on the band."""
    sec = court.sector_moments(court.laplacian_moments(recurrence.load_walks(), 52), 50)
    hausdorff = {k: court.hausdorff(M) for k, M in sec.items()}
    nodes = lambda M, x: court.eigen_count_below(*court.chebyshev(M[:50])[:2], Fraction(x))
    return {
        "the true sector moments M_0..M_50 pass the Hausdorff test on [0, 256] exactly, so each sector has a spectral "
        "measure there, and its 25-node Gauss rule lies inside the band": all(
            v["fails_at"] is None for h in hausdorff.values() for v in h.values())
        and all(nodes(M, 0) == 0 and nodes(M, 256) == 25 for M in sec.values()),
        "their first moments are the block eigenvalues 241 (contrast) and 235 (uniform)":
            sec["V5 contrast"][1] == 241 and sec["V1 uniform"][1] == 235,
    }


def triple():
    """Layer 2 and J7: the finite spectral triple of the carrier."""
    D = sp.Matrix(carrier.dirac(carrier.signless_incidence()))
    M = sp.Matrix(carrier.signless_incidence())
    mom = spectral.moments(4)
    w, V = np.linalg.eigh(np.array(D * D, float))
    ker = V[:, np.abs(w) < 1e-9]
    gamma = np.diag(np.array(carrier.grading(), float))
    return {
        "the triple's D is odd for the grading and D^2 = M M^T + M^T M, the carrier, with moments Tr D^0..D^8 = 15, 40, "
        "200, 1240, 8840": all(D[i, j] == 0 for i in range(15) for j in range(15) if (i < 5) == (j < 5))
        and D * D == sp.diag(M * M.T, M.T * M) == sp.Matrix(carrier.D2()) and [mom[k] for k in range(5)] == [15, 40, 200, 1240, 8840],
        "ker D^2 lies on the edges and is ker M, and the Witten index Tr(gamma on ker D^2) is -5 (J7)":
            ker.shape[1] == 5 and np.allclose(ker[:5], 0) and np.isclose(((ker ** 2) * gamma[:, None]).sum(), -5)
            and np.linalg.matrix_rank(np.hstack([ker[5:], native.p5_basis()])) == 5,
    }


def readout():
    """Layer 5 and J6: the carrier as a control system."""
    A = observer.system_matrix()
    K = np.array(carrier.D2(), float)
    Bedge = np.vstack([np.zeros((15, 10)), np.eye(15)[:, 5:]])
    reach = observer.kalman_ctrl(A, Bedge)
    blind = observer.null_space(observer.kalman_obs(A, observer.readouts()["Dirac image D psi"]))
    Pr, Pb = reach @ reach.T, blind @ blind.T
    w, V = np.linalg.eigh(Pr @ Pb @ Pr)
    hidden = V[:, w > 1 - 1e-8]
    P5 = native.p5_basis()
    source = np.zeros((30, 10))
    source[5:15, :5], source[20:30, 5:] = P5, P5
    return {
        "the readout's generator A = [[0, I], [-D^2, 0]] is the triple's D^2 in first-order form: A^2 = -(D^2 + D^2)":
            np.allclose(A @ A, -np.kron(np.eye(2), K)),
        "the hidden controllable sector of (edge force, D psi) is ker M + ker M in (position, velocity), the native "
        "source's space (J6)": hidden.shape[1] == 10 and observer.rank(np.hstack([hidden, source])) == 10,
    }


def product_geometry():
    """Layer 6 and J10: the carrier's traces become the heat coefficients of M4 x F (conditional)."""
    coeffs, (t, R, m) = gravity.product_heat_coefficients()
    mom = spectral.moments(2)
    return {
        "for any closed spin 4-manifold, (4 - tR/3) Tr exp(-t m^2 D_F^2) has coefficients 4 Tr D^0 = 60, "
        "-(4 Tr D^2 m^2 + Tr D^0 R/3) = -(160 m^2 + 5R) and 2 Tr D^4 m^4 + Tr D^2 m^2 R/3 = 400 m^4 + 40 m^2 R/3 (J10); G "
        "and Lambda_cc need the free inputs f, L and m": sp.simplify(coeffs[0] - 4 * mom[0]) == 0
        and sp.simplify(coeffs[1] + 4 * mom[1] * m ** 2 + mom[0] * R / 3) == 0
        and sp.simplify(coeffs[2] - 2 * mom[2] * m ** 4 - mom[1] * m ** 2 * R / 3) == 0,
    }


@functools.lru_cache(maxsize=1)
def _flrw():
    """Layer 7's flow from the datum, with G and Lambda_cc from the spectral action (L = 10 m, Lambda_cc tuned to 0)."""
    L, m = 10.0, 1.0
    G, Lcc = gravity.newton_and_vacuum(1, 1, gravity.tuned_F2(1, 1, L, m, 0.0), L, m)
    U = cosmology.FLRW(G, Lcc, m)
    psi0, v0 = carrier.canon_initial_datum()
    return U, U.evolve(psi0, v0, 40.0, n=400), (G, Lcc, m, psi0, v0)


def friedmann():
    """Layer 7: the carrier field on a flat FLRW background with the conditional G and Lambda_cc."""
    U, sol, _ = _flrw()
    rho0 = np.array([U.sector_rho(sol.y[:, i])[0] for i in range(sol.y.shape[1])])
    return {
        "with G and Lambda_cc from the spectral action the Friedmann constraint holds along the flow": max(
            abs(U.constraint(sol.y[:, i])) for i in range(sol.y.shape[1])) < 1e-8,
        "the kernel sector, which holds the datum's 2, is stiff: its energy times a^6 stays 2": np.isclose(rho0[0], 2)
        and np.allclose(rho0 * np.exp(6 * sol.y[0]), 2, rtol=1e-6),
    }


def binding_joins():
    """Layer 12: the symmetries a physical binding must respect."""
    D = np.array(carrier.dirac(carrier.signless_incidence()), float)
    K, pairs = native.commutator_map()
    five, ten, _ = binding.su5_weights()
    h = np.array([1.0, 2.0, 3.0, 4.0, -10.0])
    return {
        "the commutant of D is M5 + M4 + M4 + C + C, dimension 59, and its only atom-diagonal element is the phase":
            binding.commutant_dim(D) == 59 and binding.diagonal_commutant_dim() == 1,
        "the port lives on Lambda^2 ker D (dimension 10) and breaks the dark O(5) completely; the zero modes' 5 and this "
        "10, at opposite chirality, have equal SU(5) anomalies, so 5 + 10 = 15 is anomaly-free": K.shape == (6, 10)
        and len(pairs) == 10 and binding.port_stabiliser_dim() == 0
        and np.isclose(binding.anomaly(five, h), binding.anomaly(ten, h)) and len(five) + len(ten) == 15,
    }


def calibration():
    """Layer 13: a calibration t = tau u intertwines the flows, and no internal number fixes tau."""
    gap, freq = gatework.countermodel_A()
    return {
        "S U(u) = U_tau(tau u) S for every calibration tau (the Salina and Prema courts vanish)":
            gatework.salina_prema(2.7) < 1e-9 and gatework.salina_prema(0.5) < 1e-9,
        "calibrations tau and 2 tau give identical native records with frequencies in ratio 2 (countermodel A)":
            gap < 1e-9 and np.isclose(freq[1.0], 2 * freq[2.0]),
    }


def sound_light():
    """Layer 17: the K5 edge Hodge complex, sound and light."""
    d0, d1, _, curl = waves.complex_ops()
    B, M = carrier.signed_incidence(), carrier.signless_incidence()
    E5 = sp.eye(5)
    A4 = [E5[:, i] - E5[:, j] for i in range(5) for j in range(5) if i != j]
    _, _, A = carrier.hodge_block()
    Cf, _ = carrier.fundamental_cycles()
    X = (Cf * Cf.T).inv() * Cf * curl * Cf.T
    cycles = sp.Matrix.hstack(*B.nullspace())
    return {
        "the edge complex has d0 = B^T, d1 d0 = 0 and ranks 4 + 6: sound im d0 is the cuts, light ker d0^T the cycles":
            d0 == B.T and (d1 * d0).is_zero_matrix and d0.rank() == 4 and d1.rank() == 6 and (d0.T * cycles).is_zero_matrix,
        "Curl = *d1 has spectrum +-sqrt5 (three each) on the cycles and 0 on sound: the two helicities":
            curl.eigenvals() == {sp.sqrt(5): 3, -sp.sqrt(5): 3, 0: 4} and (curl * cycles).rank() == 6,
        "in the fundamental-cycle basis Curl is -A, the carrier's Hodge block (6I - G) sigma": curl * Cf.T == Cf.T * X and X == -A,
        "the sound operator B B^T = 5I - J is half the A4 frame, and with the triple's vertex block it makes 8: "
        "M M^T + B B^T = 8I": B * B.T == 5 * E5 - sp.ones(5, 5) == sum((a * a.T for a in A4), sp.zeros(5, 5)) / 2
        and M * M.T + B * B.T == 8 * E5,
    }


# ------------------------------------------------------------------- no dot hangs by one join

def _surface_labels():
    """The two triangulations on the projective line over F5 (the cone point at infinity = 5)."""
    tri, comp = spacetime.rp2_triangulations()
    _, psl = projective_line()
    image = lambda s, F: {tuple(sorted(s[i] for i in f)) for f in F}
    orbit = lambda t: {tuple(sorted(s[i] for i in t)) for s in psl}
    phi = next(p for p in itertools.permutations(range(6)) if p[5] == 5 and image(p, tri) == orbit(min(image(p, tri))))
    return image(phi, tri), image(phi, comp)


def _plane():
    """PG(2,5) with the Veronese conic of the projective line: points, conic labels, tangent lines."""
    p = 5

    def norm(v):
        v = [x % p for x in v]
        k = next(x for x in v if x)
        inv = pow(k, p - 2, p)
        return tuple(y * inv % p for y in v)
    points = sorted({norm(v) for v in itertools.product(range(p), repeat=3) if any(v)})
    vec = lambda x: (1, 0) if x == 5 else (x, 1)
    conic = {norm((vec(x)[0] ** 2, vec(x)[0] * vec(x)[1], vec(x)[1] ** 2)): x for x in range(6)}
    tangent = {c: norm((-c[2], 2 * c[1], -c[0])) for c in conic}          # the polar of b^2 - ac at c
    cross = lambda u, v: norm((u[1] * v[2] - u[2] * v[1], u[2] * v[0] - u[0] * v[2], u[0] * v[1] - u[1] * v[0]))
    on = lambda L, q: sum(a * b for a, b in zip(L, q)) % p == 0

    def sym2(m):                                               # (x, y) -> (a x + b y, c x + d y) on (x^2, xy, y^2)
        a, b, c, d = m
        return lambda v: norm((a * a * v[0] + 2 * a * b * v[1] + b * b * v[2],
                               a * c * v[0] + (a * d + b * c) * v[1] + b * d * v[2],
                               c * c * v[0] + 2 * c * d * v[1] + d * d * v[2]))
    return points, conic, tangent, cross, on, sym2


def projective_plane():
    """The Veronese conic: the six axes, the fifteen edges and the ten faces in PG(2,5)."""
    points, conic, tangent, cross, on, sym2 = _plane()
    label = {x: c for c, x in conic.items()}
    count = {q: sum(on(L, q) for L in tangent.values()) for q in points}
    exterior = {q for q in points if q not in conic and count[q] == 2}
    interior = {q for q in points if q not in conic and count[q] == 0}
    pole = lambda a, b: cross(tangent[label[a]], tangent[label[b]])

    def perspector(T):
        a, b, c = T
        lines = [cross(label[a], pole(b, c)), cross(label[b], pole(a, c)), cross(label[c], pole(a, b))]
        X = cross(lines[0], lines[1])
        return X if on(lines[2], X) else None
    A, Ac = _surface_labels()
    det = lambda m: (m[0] * m[3] - m[1] * m[2]) % 5
    gl = [m for m in itertools.product(range(5), repeat=4) if det(m)]
    orbit = lambda q: {sym2(m)(q) for m in gl}
    return {
        "PG(2,5) has 31 points: the six on the conic v -> v^2 of the projective line, 15 exterior points on two tangents "
        "and 10 interior points on none": len(points) == 31 and len(conic) == 6 and len(exterior) == 15 and len(interior) == 10,
        "the exterior points are the pairs of axes, so the surface's 15 edges: the tangents at a and b meet in one exterior "
        "point, and every exterior point arises once": {pole(a, b) for a, b in itertools.combinations(range(6), 2)} == exterior,
        "for every inscribed triangle the lines from each vertex to the meeting point of the other two tangents are "
        "concurrent at an interior point, a face and its complementary face share it, and so the ten faces of either "
        "triangulation are the ten interior points": all(perspector(T) in interior for T in A | Ac)
        and {perspector(T) for T in A} == interior == {perspector(T) for T in Ac}
        and all(perspector(T) == perspector(tuple(sorted(set(range(6)) - set(T)))) for T in A)
        and all(tuple(sorted(set(range(6)) - set(T))) in Ac for T in A),
        "PGL(2,5) acts on the plane through the symmetric square, keeps the conic and is transitive on the conic, the "
        "exterior and the interior points": all(sym2(m)(c) in conic for m in gl for c in conic)
        and orbit(next(iter(conic))) == set(conic) and orbit(next(iter(exterior))) == exterior
        and orbit(next(iter(interior))) == interior,
    }


def air_801_joins():
    """AIR_801: a Singer cycle mod 5, outside PSL(2,5), acting on the line, the triangulations and the plane."""
    points, conic, tangent, cross, on, sym2 = _plane()
    m = (108 % 5, 801 % 5, 106 % 5, 901 % 5)
    mobius = tuple(conic[sym2(m)(c)] for c in sorted(conic, key=conic.get))
    A, Ac = _surface_labels()
    pgl, psl = projective_line()
    image = lambda s, F: {tuple(sorted(s[i] for i in f)) for f in F}
    step = sym2(m)
    seen, orbits = set(), []
    for q in points:
        if q not in seen:
            o, r = [], q
            while r not in o:
                o.append(r)
                r = step(r)
            seen |= set(o)
            orbits.append(o)
    count = {q: sum(on(L, q) for L in tangent.values()) for q in points}
    kind = lambda o: "conic" if o[0] in conic else ("exterior" if count[o[0]] == 2 else "interior")
    turn = [0]
    while mobius[turn[-1]] != 0:
        turn.append(mobius[turn[-1]])
    return {
        "mod 5 the matrix is [[3, 1], [1, 1]], of determinant 2, a non-square: in PGL(2,5) it lies outside PSL(2,5), has "
        "order 6 and turns the six points of the projective line in one cycle": m == (3, 1, 1, 1) and (m[0] * m[3] - m[1] * m[2]) % 5 == 2
        and mobius in pgl - psl and len(turn) == 6,
        "so it swaps the hemi-icosahedron and its complement": image(mobius, A) == Ac and image(mobius, Ac) == A,
        "its symmetric square keeps the conic and splits the 31 points as conic 6, exterior 3 + 6 + 6 and interior "
        "1 + 3 + 6 (the joined paper's 1 + 3 + 3 + 6 + 6 + 6 + 6)": sorted((kind(o), len(o)) for o in orbits) == [
            ("conic", 6), ("exterior", 3), ("exterior", 6), ("exterior", 6), ("interior", 1), ("interior", 3), ("interior", 6)],
    }


def gksl_census():
    """The half-periods are the census's critical points of types E8, E7 + A1 and D8."""
    R = glue.roots()
    simple = np.array([0.5 * np.array([1, -1, -1, -1, -1, -1, -1, 1]), np.eye(8)[0] + np.eye(8)[1]]
                      + [np.eye(8)[k + 1] - np.eye(8)[k] for k in range(6)])
    kinds = Counter()
    for c in itertools.product((0, 1), repeat=8):
        x = np.array(c) @ simple / 2
        gradient = (np.sin(2 * np.pi * R @ x)[:, None] * R).sum(axis=0)
        kinds[(handover.stabiliser(R, x)[0], int(round(240 - np.cos(2 * np.pi * R @ x).sum())),
               bool(np.linalg.norm(gradient) < 1e-9))] += 1
    fam = {t: (f["orbit"], int(round(240 - f["lambda"]))) for (_, t), f in _census().items()}
    return {
        "the 256 half-periods are critical points of the band: one of type E8 (eps 0), 120 of type E7 + A1 (eps 224) and "
        "135 of type D8 (eps 256), the census's whole orbits of those types": kinds == Counter(
            {("E8", 0, True): 1, ("E7+A1", 224, True): 120, ("D8", 256, True): 135})
        and (fam["E8"], fam["E7+A1"], fam["D8"]) == ((1, 0), (120, 224), (135, 256)),
        "so the GKSL semigroup e^-tL decays the identity, the 120 antisymmetric and the 135 symmetric Paulis at those "
        "critical values, 0, 224 and 256 (layer 22's Pauli generator)": all(counts.pauli_bath().values()),
    }


def stage_landings():
    """The stages that meet the tick land on a nonzero tick level of the time clock."""
    levels = {k: counts.first_landing(k) for k in range(15)}
    return {
        "each of the twelve stages prime to 5 lands first on a nonzero tick level, 864, 1728 or 2592, and the stages 0, 5 "
        "and 10 never land (SANSKRIT_DEEP, EVERY_WORD)": all((levels[k] is None) == (k % 5 == 0) for k in range(15))
        and {v[1] for v in levels.values() if v} <= set(spine.subgroup(TICK)) - {0}
        and levels == counts.STAGE_LANDINGS,
    }


def torus_calibration():
    """A calibration rescales the nine frequencies together; their ratios are irrational, so the flow has no period."""
    eps = sorted({240 - v for v in _critical_values()} - {0})
    free = lambda q: snapshot.squarefree_part(q)
    tau = 2.7
    w = np.sqrt(np.array([float(e) for e in eps]))
    return {
        "a calibration t = tau u divides all nine frequencies by tau, so the flow's orbit on T^9 is the same for every "
        "calibration and only its speed changes": np.allclose((w / tau) / (w[0] / tau), w / w[0]),
        "no two frequencies have a rational ratio (the square-free parts differ), so no calibration makes the bath flow "
        "periodic: the bath supplies no clock": all(free(a * b) != 1 for a, b in itertools.combinations(eps, 2)),
    }


def literal_incidences():
    """The owner's operand file holds the carrier's incidences in the carrier's edge order."""
    d = literal.load()
    return {
        "native_matrices_input.json lists the edges in the carrier's order, and its H_signless and boundary_oriented are "
        "the carrier's M and B": [tuple(e) for e in d["edge_order"]] == carrier.edges()
        and d["H_signless"] == carrier.signless_incidence() and d["boundary_oriented"] == carrier.signed_incidence(),
    }


def measure_band():
    """The spectral measures live on the band, whose ends are the census's minimum and maximum."""
    values = [240 - v for v in _critical_values()]
    sec = court.sector_moments(court.laplacian_moments(recurrence.load_walks(), 52), 50)
    nodes = lambda M, x: court.eigen_count_below(*court.chebyshev(M[:50])[:2], Fraction(x))
    return {
        "the band [0, 256] runs from the census's minimum (type E8, eps 0) to its maximum (type D8, eps 256), and every "
        "sector's 25 Gauss nodes lie strictly inside it": (min(values), max(values)) == (0, 256) == (0, court.BAND)
        and all(nodes(M, 0) == 0 and nodes(M, 256) == 25 for M in sec.values()),
    }


def wave_calibration():
    """A calibration turns the native frequencies into physical ones; the register keeps their ratios."""
    reg = gatework.register()
    cal = gatework.Calibration(2.7)
    ladder = {"carrier": 3 ** 0.5, "source": 2.0, "sound": 5 ** 0.5, "light": 5 ** 0.5, "port": 4.0, "band top": 16.0}
    phys = {k: cal.frequency(v) for k, v in ladder.items()}
    M, B = carrier.signless_incidence(), carrier.signed_incidence()
    return {
        "a calibration divides every native frequency by tau; light/sound = 1, port/source = 2 and band top/source = 8 "
        "are calibration-invariant and stand in the prediction register": np.isclose(phys["light"] / phys["sound"], 1)
        and np.isclose(phys["port"] / phys["source"], reg["native"]["port_to_source_frequency_ratio"])
        and np.isclose(phys["band top"] / phys["source"], reg["native"]["band_edge_to_source_frequency_ratio"]),
        "and so is carrier^2 + sound^2 = 8 on every vertex mode (M M^T + B B^T = 8I)": M * M.T + B * B.T == 8 * sp.eye(5),
    }


def no_bridge():
    """Every dot has at least two maps, and no single map holds the diagram together."""
    maps = [j for j in JOINS if j[4] in MAPS]
    degree = Counter(x for j in maps for x in j[:2])
    bridges = [j[:3] for j in maps if len(components([k is not j for k in JOINS])) > 1]
    return {"every dot has at least two maps": all(degree[k] >= 2 for k in DOTS),
            "removing any one map leaves the diagram connected: it has no bridge": not bridges}


# ------------------------------------------------------------------- the 01:57-02:52 notes and release K+ADDENDUM3

def _keys(V):
    """Integer keys for doubled lattice vectors with entries in -16..15 (base 32, one digit per coordinate)."""
    return ((np.asarray(V, dtype=np.int64) + 16) * (32 ** np.arange(8, dtype=np.int64))).sum(axis=-1)


def walk_convolutions():
    """Canon K's W5/W6 root convolution: the pair, triple and quadruple sums of the 240 roots."""
    D = np.rint(2 * glue.roots()).astype(np.int64)
    off = int(_keys(np.zeros(8, dtype=np.int64)))
    k2, c2 = np.unique(_keys(D)[:, None] + _keys(D)[None, :] - off, return_counts=True)
    k3, inv = np.unique((k2[:, None] + _keys(D)[None, :] - off).ravel(), return_inverse=True)
    c3 = np.rint(np.bincount(inv, weights=np.repeat(c2, 240))).astype(np.int64)
    at = lambda keys: (lambda i: np.where(k3[np.minimum(i, len(k3) - 1)] == keys, c3[np.minimum(i, len(k3) - 1)], 0))(
        np.searchsorted(k3, keys))
    c3_roots = at(_keys(D))
    c4_roots = at(_keys(D)[:, None] - _keys(D)[None, :] + off).sum(axis=1)
    W5, W6 = int(c4_roots.sum()), int((c3 * c3).sum())
    return {
        "the ordered pair sums of the 240 roots take 9361 values and the triple sums 131041, with total 240^3 = "
        "13824000; every root is a triple sum in exactly 5253 ways and a quadruple sum in 574224 (Canon K)":
            len(k2) == 9361 and len(k3) == 131041 and int(c3.sum()) == 240 ** 3 == 13824000
            and set(c3_roots.tolist()) == {5253} and set(c4_roots.tolist()) == {574224},
        "so W_5 = 240 x 574224 = 137813760 and W_6 = sum of the squared triple counts = 17141798400, layer 3's "
        "returns N_5 and N_6; WALKS_CLOCK's 'orders five and six are new' holds for the sibling, not here":
            W5 == 240 * 574224 == 137813760 and W6 == 17141798400 and _walks()[0][5:7] == [W5, W6],
    }


def clock_sidebands():
    """WALKS_CLOCK, LEVELS_160, SUN_MOON_ORDERS and the observer completion: the clock as 160 x 27 and its sidebands."""
    j = np.arange(N)
    A, r32, r27, r5 = j % 36, j % 32, j % 27, j % 5
    t8, t3, t5 = (r32 - A) % 32 // 4, (r27 - A) % 27 // 9, (r5 - A) % 5
    t = (105 * t8 + 40 * t3 + 96 * t5) % 120
    div = [int(d) for d in sp.divisors(N)]
    covers = lambda ms: lcm(36, *ms) == N
    best = lambda n: min(max(ms) for ms in itertools.combinations(div, n) if covers(ms))
    return {
        "4320 = 160 x 27 with idempotents 2241 = 3105 + 3456 (the 2-part and the time part) and 2080, so j = 2241 (j mod "
        "160) + 2080 (j mod 27) for every j; 2241 is 1 mod 5 and 2080 is 0, so the tick bit is read on the 160-clock, "
        "and every residue mod 27 meets all five time residues: the 27-clock is blind to the tick; 2241 = 3^8 mod 4320":
            np.array_equal((2241 * (j % 160) + 2080 * (j % 27)) % N, j) and (3105 + 3456) % N == 2241
            and (2241 % 5, 2080 % 5) == (1, 0) and all(len(set(r5[r27 == b])) == 5 for b in range(27))
            and pow(3, 8, N) == 2241,
        "the sun 1440 is (0, 9), of order 3 on the 27-clock and fixed on the 160-clock; the moon 120 is (120, 12), of "
        "orders 4 and 9 on the two clocks and 36 = 4 x 9 on the circle; and the moon's square 14400 is the sun "
        "mod 4320 (ENERGY_250's squared tail)": (1440 % 160, 1440 % 27, 120 % 160, 120 % 27) == (0, 9, 120, 12)
        and (27 // gcd(9, 27), 160 // gcd(120, 160), 27 // gcd(12, 27)) == (3, 4, 9)
        and (spine.order(1440), spine.order(120)) == (3, 36) and 120 ** 2 % N == 1440,
        "the observer completion's sidebands: with the address A = j mod 36, the residues mod 32, 27 and 5 meet the "
        "checksums mod 4 and mod 9, and t8, t3, t5 rebuild t = 105 t8 + 40 t3 + 96 t5 mod 120 and j = A + 36 t for all "
        "4320 ticks; each atlas fibre holds its 120 = 8 x 3 x 5 sideband states once; the direct CRT is j = 3105 r32 + "
        "2080 r27 + 3456 r5": np.all((r32 - A) % 4 == 0) and np.all((r27 - A) % 9 == 0)
        and np.array_equal((A + 36 * t) % N, j) and all(len(set(zip(t8[A == a], t3[A == a], t5[A == a]))) == 120 for a in range(36))
        and np.array_equal((3105 * r32 + 2080 * r27 + 3456 * r5) % N, j)
        and [(e % 8, e % 3, e % 5) for e in (105, 40, 96)] == [(1, 0, 0), (0, 1, 0), (0, 0, 1)],
        "over residue sensors whose moduli divide 4320 (48 divisors), one sensor beside the address must read j mod "
        "4320 itself, two need a largest alphabet of 135 (32 and 135), three one of 32 (5, 27 and 32, 64 symbols); a "
        "120-state fibre needs at least 7 bits": len(div) == 48 and [m for m in div if covers((m,))] == [N]
        and best(2) == 135 and covers((32, 135)) and best(3) == 32 and covers((5, 27, 32)) and 5 + 27 + 32 == 64
        and ceil(log2(120)) == 7,
    }


def observer_completion():
    """The hub's observer completion: the wedge readout misses SL(2), and three frame probes complete it."""
    a, b = sp.symbols("a1:6"), sp.symbols("b1:6")
    pairs = list(itertools.combinations(range(5), 2))
    wedge = lambda x, y: [x[i] * y[k] - x[k] * y[i] for i, k in pairs]
    w = sp.Matrix(wedge(a, b))
    X = sp.Matrix(list(a) + list(b))
    point = dict(zip(X, (2, 1, -1, 3, 1, 1, 3, 2, -1, 4)))
    J = w.jacobian(X).subs(point)
    probes = sp.Matrix([[int(k == m) for k in range(10)] for m in (0, 1, 5)])

    def recover(W, a1, a2, b1):
        W = dict(zip(pairs, W))
        w12 = W[(0, 1)]
        b2 = (w12 + a2 * b1) / a1
        return ([a1, a2] + [(a2 * W[(0, i)] - a1 * W[(1, i)]) / w12 for i in (2, 3, 4)],
                [b1, b2] + [(b2 * W[(0, i)] - b1 * W[(1, i)]) / w12 for i in (2, 3, 4)])
    rng = np.random.default_rng(225)
    trials = []
    while len(trials) < 53:
        p, q = ([Fraction(int(v), int(d)) for v, d in zip(rng.integers(-9, 10, 5), rng.integers(1, 6, 5))] for _ in range(2))
        if p[0] != 0 and p[0] * q[1] - p[1] * q[0] != 0:
            trials.append((p, q))
    U = ((2, 1), (1, 1))
    turned = lambda p, q: ([U[0][0] * x + U[1][0] * y for x, y in zip(p, q)], [U[0][1] * x + U[1][1] * y for x, y in zip(p, q)])
    plucker = lambda W: (lambda W: W[(0, 1)] * W[(2, 3)] - W[(0, 2)] * W[(1, 3)] + W[(0, 3)] * W[(1, 2)])(dict(zip(pairs, W)))
    e = lambda i: [int(k == i) for k in range(5)]
    simple_sum = [x + y for x, y in zip(wedge(e(0), e(1)), wedge(e(2), e(3)))]
    tick = lambda A, r32, r27, r5: (A + 36 * ((105 * ((r32 - A) % 32 // 4) + 40 * ((r27 - A) % 27 // 9)
                                          + 96 * ((r5 - A) % 5)) % 120)) % N
    return {
        "the wedge (a, b) -> a ^ b of a source pair in five dimensions has derivative rank 7 at a generic pair, and the "
        "three probes a1, a2, b1 complete it to rank 10": J.rank() == 7 and sp.Matrix.vstack(J, probes).rank() == 10,
        "a pair turned by U of determinant 1 has the same wedge, so the readout's fibre is the SL(2) frame (Canon K's "
        "joint observer; the clock residues do not see it either)": all(
            wedge(*turned(p, q)) == wedge(p, q) for p, q in trials[:10]),
        "on the chart a1 w12 != 0 the explicit inverse b2 = (w12 + a2 b1)/a1, a_i = (a2 w1i - a1 w2i)/w12, b_i = (b2 w1i "
        "- b1 w2i)/w12 rebuilds the pair exactly in 53 rational trials, and with the sidebands the whole observation "
        "(a ^ b, a1, a2, b1, j mod 36, 32, 27, 5) is injective": all(
            recover(wedge(p, q), p[0], p[1], q[0]) == (p, q) for p, q in trials)
        and all(recover(wedge(p, q), p[0], p[1], q[0]) == (p, q) and tick(k % 36, k % 32, k % 27, k % 5) == k
                for (p, q), k in zip(trials, map(int, rng.integers(0, N, 53)))),
        "the anti-alias court: every wedge a ^ b meets the Pluecker relation w12 w34 - w13 w24 + w14 w23 = 0, and e1 ^ e2 "
        "+ e3 ^ e4 gives 1, so the rank-7 locus is a cone, not a linear 7-space": sp.expand(plucker(wedge(a, b))) == 0
        and plucker(simple_sum) == 1,
    }


def six_site_torsion():
    """SEVEN_PAIRS, TORSION_FIVE and INVERSE_TWO: the six-site moment blocks carry one 5, on the uniform line."""
    I6, J6 = sp.eye(6), sp.ones(6, 6)
    G0, G1 = 183 * I6 + 52 * J6, 35366 * I6 + 8134 * J6
    stack = sp.Matrix.vstack(G0, G1)
    snf = lambda M: [smith_normal_form(M, domain=sp.ZZ)[i, i] for i in range(6)]
    masks = [sp.Matrix([[int(i in S) for i in range(6)]]) for n in range(1, 7) for S in itertools.combinations(range(6), n)]
    clears = [sum(m) % 5 != 0 for m in masks]
    rng = np.random.default_rng(57)
    x = sp.Matrix(rng.integers(-9, 10, 6).tolist())
    mod5 = lambda M: M.applyfunc(lambda v: v % 5)
    contrasts = [sp.Matrix([int(i == k) - int(i == 5) for i in range(6)]) for k in range(5)]
    _, E = _walks()
    uniform = [6 * E[k] - 5 * E[k + 1] // 240 for k in range(4)]
    return {
        "35366 G0 - 183 G1 = 350510 J for G0 = 183I + 52J and G1 = 35366I + 8134J, so on a mask of k sites the same "
        "combination of the masked sums gives 350510 k times the sum of the six coordinates, and not the coordinates":
            35366 * G0 - 183 * G1 == 350510 * J6 and all(
                (35366 * m * G0 * x - 183 * m * G1 * x)[0] == 350510 * sum(m) * sum(x) for m in masks),
        "the stacked blocks have Smith form diag(1, 1, 1, 1, 1, 5): their rows span the vectors with coordinate sum "
        "divisible by 5, so a mask clears the 5 exactly when 5 does not divide its size, 57 masks, and the six of size 5 "
        "do not": snf(stack) == [1, 1, 1, 1, 1, 5] and all(sum(stack.row(i)) % 5 == 0 for i in range(12))
        and snf(sp.Matrix.vstack(stack, masks[0]))[-1] == 1 and snf(sp.Matrix.vstack(stack, masks[-2]))[-1] == 5
        and sum(masks[-2]) == 5 and clears.count(True) == 57 and clears.count(False) == 6,
        "mod 5 the blocks are 3I + 2J and I - J, both kill the all-ones vector, and 2 inverts the first on the five "
        "contrasts (INVERSE_TWO); det G0 = 183^5 x 495 has one factor 5, as do 350510 and gcd(495, 84170)":
            mod5(G0) == mod5(3 * I6 + 2 * J6) and mod5(G1) == mod5(I6 - J6) and mod5(G0 * sp.ones(6, 1)).is_zero_matrix
            and mod5(G1 * sp.ones(6, 1)).is_zero_matrix and all(mod5(2 * G0 * c) == mod5(c) for c in contrasts)
            and G0.det() == 183 ** 5 * 495 and sp.multiplicity(5, G0.det()) == sp.multiplicity(5, 350510) == 1
            and gcd(495, 84170) == 5,
        "the 5 is the 5 in 240: the uniform moments 6 E_k - 5 E_(k+1)/240 are E_k mod 5, and E_1, E_2, E_3 are multiples "
        "of 240, so every uniform moment past the zeroth, and the cumulants 495 and 84170, vanish mod 5, while the "
        "contrast values 183 and 35366 are units": uniform[:3] == [1, 235, 55720]
        and all((u - E[k]) % 5 == 0 for k, u in enumerate(uniform)) and all(E[k] % 240 == 0 for k in (1, 2, 3))
        and uniform[2] - uniform[1] ** 2 == 495 and 183 % 5 != 0 and 35366 % 5 != 0,
    }


def seven_pairs_algebra():
    """SEVEN_PAIRS's operator identities: the weights' second moment, the compression defect and the protected lift."""
    Z = sp.diag(1, -1)
    W = {-1: sp.Matrix([[1, 1], [1, 1]]) / 4, 0: sp.Matrix([[1, -1], [-1, 1]]) / 2, 1: sp.Matrix([[1, 1], [1, 1]]) / 4}
    M = [sum((x ** n * W[x] for x in W), sp.zeros(2, 2)) for n in range(3)]
    rng = np.random.default_rng(7)
    rnd = lambda r, c: sp.Matrix(rng.integers(-4, 5, (r, c)).tolist())
    A, B, U1, U2 = rnd(5, 5), rnd(5, 5), rnd(3, 3), rnd(3, 3)
    E = sp.Matrix.vstack(sp.eye(3), rnd(2, 3))
    L = sp.Matrix.hstack(sp.eye(3), sp.zeros(3, 2))
    P, Q = E * L, sp.eye(5) - E * L
    lift = lambda U: E * U * L + Q
    return {
        "weights with off-diagonals 1/4, -1/2, 1/4 at -1, 0, 1 (here rank-one and positive): the moments of order 0 and "
        "1 are diagonal and commute with diag(1, -1), and [diag(1, -1), M_2] = [[0, 1], [-1, 0]] whatever the diagonals":
            all(w.is_positive_semidefinite for w in W.values()) and Z * M[0] == M[0] * Z and Z * M[1] == M[1] * Z
            and Z * M[2] - M[2] * Z == sp.Matrix([[0, 1], [-1, 0]]),
        "with L E = I and P = E L the compression defect L A (I - P) B E is L A B E - (L A E)(L B E), and the lift "
        "U -> E U L + Q, Q = I - E L, multiplies correctly and fixes Q": L * E == sp.eye(3)
        and L * A * (sp.eye(5) - P) * B * E == L * A * B * E - (L * A * E) * (L * B * E)
        and lift(U1) * lift(U2) == lift(U1 * U2) and lift(U1) * Q == Q == Q * lift(U1),
        "and the arithmetic: 3 x 6 - 2 x 9 = 0, 33 x 15 x 2 = 990, 66 + 99 - 33 = 132": 3 * 6 - 2 * 9 == 0
        and 33 * 15 * 2 == 990 and 66 + 99 - 33 == 132,
    }


def golden_port():
    """GOLDEN_PORT, PORT_FORMULA, CANON_BOARD and CAYLEY: the port is twice the pentagon Laplacian plus (2/5) J."""
    x, k = sp.symbols("x"), sp.symbols("k", real=True)
    R = sp.Matrix(5, 5, lambda r, c: int(r == (c + 1) % 5))
    L5 = 2 * sp.eye(5) - R - R.T
    W = sp.diag(sp.Rational(2, 5), 4 * sp.eye(5) + sp.ones(5, 5) * sp.Rational(2, 5) - 2 * (R + R.T))
    r5 = sp.sqrt(5)
    Xc = -(R + R.T)
    contrast = sp.Matrix.hstack(*[sp.Matrix([int(i == m) - int(i == 4) for i in range(5)]) for m in range(4)])
    Lp = (L5 + sp.ones(5, 5) / 5).inv() - sp.ones(5, 5) / 5
    g = sp.Matrix([[0, 0, 0, -1], [1, 0, 0, -1], [0, 1, 0, -1], [0, 0, 1, -1]])
    S = (1 - sp.I * k) / (1 + sp.I * k)
    angle = np.array([np.cos(2 * np.pi * i / 5) for i in range(5)])
    block = np.array(W[1:, 1:].tolist(), float)
    return {
        "the port metric W_p is [2/5] + 4I + (2/5)J - 2(R + R^-1) (PORT_FORMULA), that is twice the pentagon Laplacian "
        "plus (2/5) J on the five sites, with the corner 2/5": np.allclose(native.port_metric(), np.array(W.tolist(), float))
        and W[1:, 1:] == 2 * L5 + sp.ones(5, 5) * sp.Rational(2, 5),
        "its characteristic polynomial is (x - 2/5)(x - 2)(x^2 - 10x + 20)^2: eigenvalues 2/5, 2 and 5 -+ sqrt5 twice, "
        "trace 112/5, determinant 320, and the golden pair multiplies to 20, the order of the golden step 216":
            sp.expand(W.charpoly(x).as_expr() - (x - sp.Rational(2, 5)) * (x - 2) * (x ** 2 - 10 * x + 20) ** 2) == 0
            and W.trace() == sp.Rational(112, 5) and W.det() == 320 and spine.order(216) == 20,
        "on the five sites' contrast X = -(R + R^-1) satisfies X^2 = X + I, the golden equation, and the port block is "
        "4I + 2X there: its golden eigenvalues are 4 + 2 phi = 5 + sqrt5 and 6 - 2 phi = 5 - sqrt5, 4 - 2 lambda for the "
        "eigenvalues lambda of T + T^-1 on the golden edges; the 72-degree mode has 5 - sqrt5":
            (Xc * Xc - Xc - sp.eye(5)) * contrast == sp.zeros(5, 4)
            and (W[1:, 1:] - 4 * sp.eye(5) - 2 * Xc) * contrast == sp.zeros(5, 4)
            and np.allclose(block @ angle, (5 - 5 ** 0.5) * angle)
            and sp.simplify(4 - 2 * (r5 - 1) / 2 - (5 - r5)) == 0 and sp.simplify(4 + 2 * (r5 + 1) / 2 - (5 + r5)) == 0,
        "CANON_BOARD's four values (5 +- sqrt5)/10, each twice, are the spectrum of the pentagon Laplacian's "
        "pseudo-inverse, with power sums 4, 2, 6/5, 4/5, 14/25 and then 2/5 (the corner of the port, as a number); "
        "tr L^+ = 2 gives the pentagon's Kirchhoff index 5 x 2 = 10 = (5^3 - 5)/12": Lp.rank() == 4
        and [sp.nsimplify((Lp ** n).trace()) for n in range(1, 6)] == [2, sp.Rational(6, 5), sp.Rational(4, 5),
                                                                         sp.Rational(14, 25), sp.Rational(2, 5)]
        and 5 * Lp.trace() == 10 == (5 ** 3 - 5) // 12,
        "CAYLEY: the companion g of Phi_5 has g^5 = I, (g - I)(-(4I + 3g + 2g^2 + g^3)) = 5I and (g^2 - I)(-2I + g - "
        "g^2 + 2g^3) = 5I, and the Cayley map S = (1 - ik)/(1 + ik) has |S| = 1, inverse k = i(S - 1)/(S + 1) and "
        "S'(0) = -2i": g ** 5 == sp.eye(4)
        and (g - sp.eye(4)) * -(4 * sp.eye(4) + 3 * g + 2 * g ** 2 + g ** 3) == 5 * sp.eye(4)
        and (g ** 2 - sp.eye(4)) * (-2 * sp.eye(4) + g - g ** 2 + 2 * g ** 3) == 5 * sp.eye(4)
        and sp.simplify(S * sp.conjugate(S)) == 1 and sp.simplify(sp.I * (S - 1) / (S + 1) - k) == 0
        and sp.diff(S, k).subs(k, 0) == -2 * sp.I,
    }


def charges():
    """ALPHA_JOIN, CHARGE_SHELL, HYPERCHARGE, CUT, KERNEL and TRIPLET: the five-site charges of the removed shell."""
    third, half = Fraction(1, 3), Fraction(1, 2)
    Q = [-third, -third, -third, Fraction(1), Fraction(0)]
    Y = [-third, -third, -third, half, half]
    T3 = [Fraction(0)] * 3 + [half, -half]
    faces = [S for n in range(6) for S in itertools.combinations(range(5), n)]
    q = lambda c, S: sum((c[i] for i in S), Fraction(0))
    shell = lambda par: [q(Q, S) for S in faces if len(S) % 2 == par]
    sq = lambda v: sum(t * t for t in v)
    cubes = lambda c: (sum(t ** 3 for t in c), sum(q(c, S) ** 3 for S in itertools.combinations(range(5), 2)))
    keeps = lambda c: [p for p in itertools.permutations(range(5)) if all(c[p[i]] == c[i] for i in range(5))]
    D = np.array(carrier.dirac(carrier.signless_incidence()), float)
    P = native.p5_basis()
    dark = np.zeros((15, 15))
    dark[5:, 5:] = P @ np.diag([float(t) for t in Y]) @ P.T
    gen = sorted([Fraction(0)] * 2 + [Fraction(1), Fraction(-1)] + [third] * 3 + [-third] * 3 + [2 * third] * 3 + [-2 * third] * 3)
    return {
        "Q = Y + T3 with Y = (-1/3, -1/3, -1/3, 1/2, 1/2) and T3 = (0, 0, 0, 1/2, -1/2): all three sum to 0, Y and T3 are "
        "orthogonal, and sum Q^2 = 4/3 = 5/6 + 1/2 (HYPERCHARGE); sum T3^2 / sum Q^2 = 3/8 and sum Y^2 / sum T3^2 = 5/3, "
        "the SU(5) normalizations, are identities of these charges and not a measured angle": [a + b for a, b in zip(Y, T3)] == Q
        and sum(Q) == sum(Y) == sum(T3) == 0 and sum(a * b for a, b in zip(Y, T3)) == 0
        and (sq(Q), sq(Y), sq(T3)) == (Fraction(4, 3), Fraction(5, 6), half)
        and sq(T3) / sq(Q) == Fraction(3, 8) and sq(Y) / sq(T3) == Fraction(5, 3),
        "on the 32 faces of the simplex (the empty face too) q(S) = sum of Q over S has sum q^2 = 16/3 = 2^(5-3) x 4/3 on "
        "the even faces and on the odd ones (CHARGE_SHELL); the 16 even faces, Lambda^0 + Lambda^2 + Lambda^4, carry one "
        "generation's charges 0, 0, +-1, +-1/3 and +-2/3 three times each; six copies make 32 = 192/6 (ALPHA_JOIN, CUT)":
            sq(shell(0)) == sq(shell(1)) == Fraction(16, 3) == 4 * sq(Q) and sorted(shell(0)) == gen
            and 6 * Fraction(16, 3) == 32 == Fraction(192, 6),
        "the cubic sums over the 5 and over Lambda^2 5 are equal, 5/36 for Y and 8/9 for Q (A(Lambda^2 5) = A(5), B4), "
        "and the linear ones vanish: with the zero modes and Lambda^2 ker D at opposite chiralities the hypercharge "
        "anomaly cancels, while on the zero modes alone it is 5/36": cubes(Y) == (Fraction(5, 36), Fraction(5, 36))
        and cubes(Q) == (Fraction(8, 9), Fraction(8, 9)) and sum(q(Y, S) for S in itertools.combinations(range(5), 2)) == 0,
        "the permutations of the sites that keep Q are the 3! = 6 of the three -1/3 sites and those that keep Y are 12; "
        "the 5-cycle keeps neither (TRIPLET); 3Q has eigenvalues -1, -1, -1, 3, 0, rank 4 and nonzero product -3 (KERNEL)":
            len(keeps(Q)) == 6 and len(keeps(Y)) == 12 and (1, 2, 3, 4, 0) not in keeps(Q) + keeps(Y)
            and sorted(3 * t for t in Q) == [-1, -1, -1, 0, 3] and sum(1 for t in Q if t) == 4
            and sp.prod([3 * t for t in Q if t]) == -3,
        "through an identification of the five zero modes with the sites, Y acts on ker D inside the exact dark U(5) of "
        "B2 and commutes with D (a selection)": np.allclose(D @ dark, dark @ D) and not np.allclose(dark, 0),
        "on the atoms no charge but the global phase commutes with D (B1): the diagonal commutant has dimension 1, so "
        "Q and Y on the five atoms are not symmetries of the carrier": binding.diagonal_commutant_dim() == 1
        and len(set(Q)) > 1 and len(set(Y)) > 1,
    }


def census_stabilizers():
    """CENSUS_STABILIZERS, ENERGY_250 and CENSUS_CUBE: Weyl stabilizers, and the Hessian at the tick's momenta."""
    weyl = lambda c: {"A": lambda n: sp.factorial(n + 1), "D": lambda n: 2 ** (n - 1) * sp.factorial(n),
                      "E": lambda n: {6: 51840, 7: 2903040, 8: 696729600}[n]}[c[0]](int(c[1:]))
    parts = lambda t: Counter(t.split("+"))
    fam = {t: f for (_, t), f in _census().items()}
    eps = {t: (lambda q: 240 - sp.Rational(q.numerator, q.denominator))(Fraction(f["lambda"]).limit_denominator(1000))
           for t, f in fam.items()}
    # the extended E8 diagram: Bourbaki nodes 1..8 and the affine node 0
    edges = [(1, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (2, 4), (8, 0)]

    def kind(nodes):
        adj = {v: [u for e in edges if v in e for u in e if u != v and u in nodes] for v in nodes}
        hub = [v for v in nodes if len(adj[v]) == 3]
        if not hub:
            return f"A{len(nodes)}"

        def arm(u, prev):
            n, nxt = 1, [w for w in adj[u] if w != prev]
            while nxt:
                prev, u = u, nxt[0]
                n, nxt = n + 1, [w for w in adj[u] if w != prev]
            return n
        arms = tuple(sorted(arm(u, hub[0]) for u in adj[hub[0]]))
        return {(1, 2, 2): "E6", (1, 2, 3): "E7", (1, 2, 4): "E8"}.get(arms, f"D{len(nodes)}")

    def deleted(d):
        rest, out = set(range(9)) - {d}, []
        while rest:
            comp, todo = set(), [rest.pop()]
            while todo:
                v = todo.pop()
                comp.add(v)
                todo += [u for e in edges if v in e for u in e if u != v and u in rest]
                rest -= set(todo)
            out.append(kind(comp))
        return Counter(out)
    R = glue.roots()
    D2 = np.rint(2 * R).astype(int)
    cosines = {0: sp.Integer(1), 1: (sp.sqrt(5) - 1) / 4, 4: (sp.sqrt(5) - 1) / 4, 2: -(sp.sqrt(5) + 1) / 4,
               3: -(sp.sqrt(5) + 1) / 4}
    _, pts = _tick_fixed_momenta()
    golden = []
    for p in pts:
        cls = np.rint(5 * (R @ p)).astype(int) % 5
        if not np.allclose(5 * (R @ p), np.rint(5 * (R @ p))):
            golden.append(False)
            continue
        H = sum((cosines[c] * sp.Matrix(sum(np.outer(r, r) for r in D2[cls == c]).tolist()) / 4
                 for c in range(5) if (cls == c).any()), sp.zeros(8, 8))
        X = -H / 5
        golden.append(H == 60 * sp.eye(8) or (X * X - X - sp.eye(8)).applyfunc(sp.expand).is_zero_matrix)
    return {
        "every census family's orbit times the Weyl group of its type is |W(E8)| = 696729600; the nine vertex types are "
        "the extended E8 diagram with one node deleted, and the two edge types A6 + A1 and A7 have rank 7": all(
            f["orbit"] * sp.prod([weyl(c) for c in t.split("+")]) == 696729600 for t, f in fam.items())
        and sorted(map(sorted, (list(parts(t).elements()) for t in fam if sum(int(c[1:]) for c in t.split("+")) == 8)))
        == sorted(map(sorted, (list(deleted(d).elements()) for d in range(9))))
        and sorted(t for t in fam if sum(int(c[1:]) for c in t.split("+")) == 7) == ["A6+A1", "A7"],
        "the class at 250 is A4 + A4 with stabilizer 120^2 = 14400 = 10 x 1440, and 120^2 is the sun mod 4320; the class "
        "at 251 is A5 + A2 + A1 with stabilizer 8640 = 10 x 864 = 2 x 4320; the class at 6800/27 is A7, orbit 17280 = "
        "|W(E8)|/8!, and A8 has stabilizer 9! (CENSUS_STABILIZERS, ENERGY_250)": eps["A4+A4"] == 250 and eps["A5+A2+A1"] == 251
        and 696729600 // fam["A4+A4"]["orbit"] == 14400 == 120 ** 2 == 10 * 1440 and 120 ** 2 % N == 1440
        and 696729600 // fam["A5+A2+A1"]["orbit"] == 8640 == 10 * TICK == 2 * N
        and eps["A7"] == sp.Rational(6800, 27) and fam["A7"]["orbit"] == 17280 == 696729600 // sp.factorial(8)
        and 696729600 // fam["A8"]["orbit"] == sp.factorial(9),
        "at the tick's 24 fixed momenta of type A4 + A4 the Hessian H = sum r r^T cos(2 pi r.x) is -5 times a golden "
        "companion: X = -H/5 satisfies X^2 = X + I exactly in Q(sqrt5), so H has eigenvalues -5 phi and 5/phi four times "
        "each and det 5^8 = (-25)^4 (ENERGY_250's determinant); the 25th is the minimum, where H = 60 I, so 24 of the 25 "
        "momenta sit at 250, not all (CENSUS_CUBE)": len(pts) == 25 and all(golden),
    }


def frame_faces():
    """CHECK_0154: in the root graph the frame is an 8-clique; in the lattice graph every face of its 9-clique is a prism."""
    R = glue.roots()
    half = {tuple(np.rint(2 * r).astype(int)) for r in R}
    e = lambda i: np.eye(8)[i]
    F = [np.zeros(8)] + [-e(0) - e(i) for i in range(1, 8)] + [-0.5 * np.ones(8)]
    K = [tuple(np.rint(2 * f).astype(int)) for f in F]
    add = lambda p, r: tuple(a + b for a, b in zip(p, r))
    sub = lambda p, r: tuple(a - b for a, b in zip(p, r))
    ip = lambda p, r: sum(a * b for a, b in zip(p, r)) / 4
    near = lambda p: {add(p, r) for r in half}

    def prism(face):
        c = set.intersection(*[near(p) for p in face]) - set(face)
        inside, outside = c & set(K), c - set(K)
        matched = [[y for y in inside if sub(x, y) in half] for x in outside]
        return (len(inside) == len(outside) == 3 and all(sub(x, y) in half for x, y in itertools.combinations(outside, 2))
                and all(len(m) == 1 for m in matched) and len({m[0] for m in matched}) == 3)
    roots_faces = []
    for S in itertools.combinations(range(1, 9), 6):
        common = [r for r in half if all(ip(r, K[i]) == 1 for i in S)]
        others = [K[i] for i in range(1, 9) if i not in S]
        out = [r for r in common if r not in others]
        roots_faces.append(sorted(others) == sorted(r for r in common if r in others) and len(common) == 3
                           and len(out) == 1 and all(ip(out[0], o) == 0 for o in others))
    gram = lambda n: sp.eye(n) + sp.ones(n, n)
    return {
        "in the root graph the eight frame roots are a maximal clique: nine roots with pairwise products 1 would have "
        "Gram I + J of size 9, determinant 10 and rank 9 > 8; a face of six frame roots has three common neighbours, the "
        "other two and one root orthogonal to both, so not a triangle (CHECK_0154)": gram(8).det() == 9
        and gram(9).det() == 10 and gram(9).rank() == 9 and len(roots_faces) == 28 and all(roots_faces),
        "in the lattice graph the origin and the frame are a 9-clique, and all 84 of its six-point faces, not only the "
        "56 through the origin, have six common neighbours forming a prism: each lies in exactly two maximal 9-cliques. "
        "The two statements are about two graphs, and both hold": all(
            prism([K[i] for i in S]) for S in itertools.combinations(range(9), 6)),
    }


def rotor_firewall():
    """The hub's rotor firewall and Bargmann repair (Canon K), replayed with the Pauli axes."""
    C6 = sp.Matrix(6, 6, lambda r, c: int(r == (c + 1) % 6))
    Q = sp.diag(sp.Matrix(5, 5, lambda r, c: int(r == (c + 1) % 5)), sp.Matrix([[1]]))
    Xs = sp.Matrix(6, 6, sp.symbols("x0:36"))
    sol = sp.Matrix(list(Xs * C6 - Q * Xs)).jacobian(list(Xs)).nullspace()
    mats = [sp.Matrix(6, 6, list(v)) for v in sol]
    u, v, w = (sp.Matrix(z) for z in ([1, 0], [1, 1], [1, sp.I]))
    dyad = lambda z: z * z.H
    tr3 = lambda a, b, c: (dyad(a) * dyad(b) * dyad(c)).trace()
    norm = lambda z: z / sp.sqrt((z.H * z)[0])
    pauli = [sp.Matrix([[1, 0], [0, -1]]), sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]])]
    a, b, c = np.eye(3)
    omega = 2 * np.arctan2(abs(a @ np.cross(b, c)), 1 + a @ b + b @ c + c @ a)
    return {
        "the intertwiners X C6 = (C5 + I1) X form a space of dimension 2 and every nonzero one has rank 1, since the "
        "six-cycle and the five-cycle with a fixed line share only the eigenvalue 1: 6 = 5 + 1 is no faithful bridge":
            len(mats) == 2 and all(m.rank() == 1 for m in mats + [mats[0] + mats[1], mats[0] - 2 * mats[1]]),
        "raw dyads of u = (1, 0), v = (1, 1), w = (1, i) give tr = 1 + i and 1 - i reversed, but v v* squares to twice "
        "itself; normalized they give (1 + i)/4, of phase pi/4": sp.expand(tr3(u, v, w)) == 1 + sp.I
        and sp.expand(tr3(w, v, u)) == 1 - sp.I and dyad(v) ** 2 == 2 * dyad(v)
        and sp.simplify(tr3(*map(norm, (u, v, w))) - (1 + sp.I) / 4) == 0,
        "the three are the +1 eigenvectors of sigma_z, sigma_x and sigma_y, and pi/4 is half the solid angle pi/2 of "
        "the octant their Bloch vectors span": all(s * z == z for s, z in zip(pauli, (u, v, w)))
        and np.isclose(omega, np.pi / 2),
    }


def notes_0252():
    """The 01:57-02:52 notes and release K+ADDENDUM3: arithmetic, the board's digits and one correction."""
    a = Fraction("0.0072973525664")
    O = sp.symbols("O")
    al = sp.symbols("alpha", positive=True)
    return {
        "SPECTRUM_AND_ATLAS: the moon 120 is 12 in the atlas, of order 3, the sun 1440 is 0 there, and an order-11, "
        "degree-5 recurrence has (11 + 1)(5 + 2) = 84 < 195 coefficients": 120 % 36 == 12 and 36 // gcd(12, 36) == 3
        and 1440 % 36 == 0 and (11 + 1) * (5 + 2) == 84 < 195,
        "CHECK_0154's tick counts: the circle's subgroups of orders 120, 60, 30 and 10 hold 96, 48, 24 and 8 points with "
        "a nonzero tick part": [sum(1 for y in spine.subgroup(N // d) if ledger.contains_tick(y)) for d in (120, 60, 30, 10)]
        == [96, 48, 24, 8],
        "BOARD_A and CANON_BOARD: the thirteen written digits 0.0072973525664 invert to 312500000000/2280422677, about "
        "137.036, not 137; (5/137) = -1 and 137 = 5 x 27 + 2 = 120 + 17 generates the circle; a/(2 pi) = a^2 O forces "
        "O = 1/(2 pi a)": 1 / a == Fraction(312500000000, 2280422677) and abs(float(1 / a) - 137.036) < 1e-3
        and len("0072973525664") == 13 and sp.legendre_symbol(5, 137) == -1 and gcd(137, N) == 1
        and 137 == 5 * 27 + 2 == 120 + 17 and sp.solve(sp.Eq(al / (2 * sp.pi), al ** 2 * O), O) == [1 / (2 * sp.pi * al)],
        "ALPHA_JOIN: 32 c = 1/(4 pi alpha) puts c = 1/(128 pi alpha) at 0.3407805726 from the written digits and "
        "0.3407805727 from 137.035999177: both are the measurement put in by hand, not computed from the action":
            round(float(1 / a) / (128 * np.pi), 10) == 0.3407805726 and round(137.035999177 / (128 * np.pi), 10) == 0.3407805727,
        "INTEGRATION's older determinant 176173056 = 2^12 3^6 59 is the hub's Hermitian-selector fixture, which this "
        "layer rebuilds as the anchored commutator court's Gram determinant (CLOSURE_092); it is not the port's 320":
            sp.factorint(176173056) == {2: 12, 3: 6, 59: 1} and 176173056 != 320,
        "the spine's rows: 245 generates the 864 misses, 4320 = 1 mod 7, and the chart labels 95, 98, 101 agree mod 3, "
        "not mod 30 (adopted from the 00:29 correction)": spine.order(245) == TICK and spine.subgroup(245) == spine.subgroup(5)
        and N % 7 == 1 and {n % 3 for n in (95, 98, 101)} == {2} and len({n % 30 for n in (95, 98, 101)}) == 3,
    }



def notes_0255():
    """HALFPERIOD and TRACES (02:53-02:55): the half-periods by length, 224 certified exactly, the shell traces."""
    R = glue.roots()
    D2 = np.rint(2 * R).astype(int)
    simple = np.array([0.5 * np.array([1, -1, -1, -1, -1, -1, -1, 1]), np.eye(8)[0] + np.eye(8)[1]]
                      + [np.eye(8)[k + 1] - np.eye(8)[k] for k in range(6)])
    to_class = lambda v2: tuple(np.rint(np.linalg.solve(simple.T, v2 / 2)).astype(int) % 2)
    ip4 = D2 @ D2.T                                            # 4 r.s
    short = {to_class(np.zeros(8)): 0}
    for v2 in D2:
        short.setdefault(to_class(v2), 2)
    for i, j in zip(*np.nonzero(ip4 == 0)):
        short.setdefault(to_class(D2[i] + D2[j]), 4)
    band = {}
    for c, n in short.items():
        v2 = np.array(c) @ np.rint(2 * simple).astype(int)
        band.setdefault(n, set()).add(240 - int(sum((-1) ** ((r2 @ v2 // 4) % 2) for r2 in D2)))
    r0 = D2[0]
    integral = (D2 @ r0 // 4) % 2 == 0                         # r.(r0/2) integral iff r.r0 is even
    H4 = 2 * (D2[integral].T @ D2[integral]) - 240 * np.eye(8, dtype=int)   # 4 x sum r r^T cos(pi r.r0)
    third, half = Fraction(1, 3), Fraction(1, 2)
    Y = [-third, -third, -third, half, half]
    T3 = [Fraction(0)] * 3 + [half, -half]
    even = [S for n in (0, 2, 4) for S in itertools.combinations(range(5), n)]
    tr = lambda a, b: sum(sum((a[i] for i in S), Fraction(0)) * sum((b[i] for i in S), Fraction(0)) for S in even)
    Q = [y + t for y, t in zip(Y, T3)]
    B = np.array(carrier.signed_incidence(), int)
    signs = itertools.product((1, -1), repeat=10)
    E, r, k = sp.symbols("E r k", positive=True)
    states = sp.pi ** 4 / 24 * (E / 30) ** 4 / (2 * sp.pi) ** 8          # vol{30 |k|^2 < E} / (2 pi)^8 in R^8
    _, Ew = _walks()
    return {
        "HALFPERIOD: the 256 classes of the lattice mod twice itself have shortest lengths 0, 2 and 4 on 1, 120 and 135 "
        "classes, and at a shortest vector v the band at v/2 is 0, 224 and 256; the stabilizer names E8, E7 + A1 and D8, "
        "which the note did not recompute, are layer 23's (02:20)": len(short) == 256
        and Counter(short.values()) == Counter({0: 1, 2: 120, 4: 135}) and band == {0: {0}, 2: {224}, 4: {256}},
        "and 224 is a certified critical value, against the note: at x = r0/2 every r.x lies in Z/2, so the gradient "
        "vanishes exactly; 128 roots (E7 + A1) have r.x integral and 112 half-integral, so eps = 240 - (128 - 112) = 224; "
        "the Hessian sum r r^T cos(2 pi r.x) is 2(36 P' + 4 P) - 60 I = 12 P' - 52 P, of index 1 and nondegenerate. The "
        "collar near 224 is another question and stays open": integral.sum() == 128 and 240 - (128 - 112) == 224
        and np.array_equal(H4, 48 * np.eye(8, dtype=int) - 32 * np.outer(r0, r0))
        and sorted(np.linalg.eigvalsh(H4 / 4).round(9)) == [-52.0] + [12.0] * 7,
        "TRACES: on the 16 even faces the hypercharge squares sum to 10/3, the weak squares to 2 and the cross term to 0, "
        "so the charge squares give 16/3; six copies are 20, 12 and 32, and the ratio 2/(16/3) = 3/8 is the same as on "
        "the 5. The traces fix no coupling": (tr(Y, Y), tr(T3, T3), tr(Y, T3), tr(Q, Q)) == (Fraction(10, 3), 2, 0, Fraction(16, 3))
        and (6 * tr(Y, Y), 6 * tr(T3, T3), 6 * tr(Q, Q)) == (20, 12, 32) and tr(T3, T3) / tr(Q, Q) == Fraction(3, 8),
        "B B^T = 5I - J for every one of the 1024 orientations; the moments of 240 - A are 1, 240, 57840, 13983360; with "
        "eps = 30|k|^2 the density of states in eight dimensions is E^3 / (1536 pi^4 30^4) for dk/(2 pi)^8":
            all(np.array_equal((B * s) @ (B * s).T, 5 * np.eye(5, dtype=int) - 1) for s in map(np.array, signs))
            and Ew[:4] == [1, 240, 57840, 13983360]
            and sp.simplify(sp.diff(states, E) - E ** 3 / (1536 * sp.pi ** 4 * 30 ** 4)) == 0,
        "the circle has phi(4320) = 1152 generators, 137 among them; and modules 8-11's area form dA = 2 dx dy/(1 + r^2)^2 "
        "integrates to 2 pi, so (1/2 pi) times it is 1, the qubit's Chern number": sp.totient(N) == 1152
        and sum(1 for x in range(N) if gcd(x, N) == 1) == 1152 and gcd(137, N) == 1
        and sp.integrate(2 / (1 + r ** 2) ** 2 * 2 * sp.pi * r, (r, 0, sp.oo)) / (2 * sp.pi) == 1,
    }


# ------------------------------------------------------------------- every pair of levels, and no two maps

def tick_halfperiods():
    """The time clock on the half-periods and the Paulis, through the tick g = r r' (864 -> r by kappa, r -> r r')."""
    _, _, _, _, g, _ = spine.spine_clock()
    B = np.array(spine.frame()[0], float)
    gi = np.rint(g).astype(int)
    D2 = np.rint(2 * glue.roots()).astype(int)
    classes = list(itertools.product((0, 1), repeat=8))
    index = {c: i for i, c in enumerate(classes)}
    step = [index[tuple(gi @ np.array(c) % 2)] for c in classes]
    band = [240 - int(sum((-1) ** ((r2 @ np.rint(2 * B @ np.array(c)).astype(int) // 4) % 2) for r2 in D2)) for c in classes]
    orbits, seen = [], set()
    for i in range(256):
        if i not in seen:
            o = [i]
            while step[o[-1]] != i:
                o.append(step[o[-1]])
            seen |= set(o)
            orbits.append(o)
    P = np.zeros((256, 256), int)
    P[step, range(256)] = 1
    L = np.diag(band)
    return {
        "the tick g = r r' (the time clock's 864 through kappa and the carrier rotations) is integral of order 5, and "
        "det(g - I) = 25 is odd, so mod 2 it fixes only the zero half-period": np.allclose(g, gi) and spine.mat_order(g) == 5
        and round(abs(np.linalg.det(gi - np.eye(8)))) == 25 and [i for i in range(256) if step[i] == i] == [0],
        "it turns the other 255 half-periods in 51 five-cycles and keeps the band on each: 24 cycles of type E7 + A1 "
        "(eps 224) and 27 of type D8 (eps 256)": Counter((len(o), band[o[0]]) for o in orbits)
        == Counter({(1, 0): 1, (5, 224): 24, (5, 256): 27}) and all(len({band[j] for j in o}) == 1 for o in orbits),
        "in the Pauli basis L is diagonal with the band values, so the tick's permutation of the 256 Paulis commutes with L "
        "and e^-tL is tick-equivariant": np.array_equal(P @ L, L @ P),
    }


def light_symmetries():
    """The tick, the golden companion and the affine group on light, the K5 edge Hodge complex."""
    d0, _, _, curl = waves.complex_ops()
    perm = lambda f: sp.Matrix(5, 5, lambda r, c: int(r == f(c) % 5))
    R5 = perm(lambda c: c + 1)
    T = compound2(R5)
    cycles = sp.Matrix.hstack(*sp.Matrix(carrier.signed_incidence()).nullspace())
    Cn, Tn = np.array(curl.tolist(), float), np.array(T.tolist(), float)
    w, V = np.linalg.eigh(Cn)
    helicity = {s: V[:, np.isclose(w, s * 5 ** 0.5)] for s in (1, -1)}
    spectrum = {s: np.linalg.eigvals(H.T @ Tn @ H) for s, H in helicity.items()}
    turns = lambda s, ks: all(np.isclose(spectrum[s], np.exp(2j * np.pi * k / 5)).any() for k in ks)
    phi = (1 + sp.sqrt(5)) / 2
    X = (sp.eye(10) + curl) / 2
    legendre = {a: sp.legendre_symbol(a, 5) for a in (1, 2, 3, 4)}
    affine = {a: compound2(perm(lambda c, a=a: a * c)) for a in (1, 2, 3, 4)}
    return {
        "the edge tick T = Lambda^2 of the vertex rotation commutes with d0 and with Curl, so the time clock acts on "
        "sound and light and keeps each helicity": T * d0 == d0 * R5 and T * curl == curl * T,
        "on each helicity it fixes one line (the rotor plane splits one line to each) and turns a golden plane, by 144 "
        "degrees on +sqrt5 and 72 on -sqrt5: its traces there are 1 - phi and phi": helicity[1].shape[1] == helicity[-1].shape[1] == 3
        and turns(1, (0, 2, 3)) and turns(-1, (0, 1, 4))
        and np.isclose(np.trace(helicity[1].T @ Tn @ helicity[1]), (1 - 5 ** 0.5) / 2)
        and np.isclose(np.trace(helicity[-1].T @ Tn @ helicity[-1]), (1 + 5 ** 0.5) / 2),
        "Curl^2 = 5 on light, so X = (I + Curl)/2 satisfies the golden equation X^2 = X + I there: the golden companion "
        "acts on light by B -> X, as phi on helicity +sqrt5 and 1 - phi on -sqrt5": ((curl ** 2 - 5 * sp.eye(10)) * cycles).is_zero_matrix
        and ((X * X - X - sp.eye(10)) * cycles).is_zero_matrix and sp.simplify((1 + sp.sqrt(5)) / 2 - phi) == 0,
        "x -> a x + b multiplies Curl by the Legendre symbol (a/5): the rotations and the reflection keep the helicities, "
        "the doubling and its inverse exchange them": all(affine[a] * curl == legendre[a] * curl * affine[a] for a in affine)
        and legendre == {1: 1, 2: -1, 3: -1, 4: 1},
    }


def outer_s6():
    """The outer automorphism of S6 carries the cone's S5 onto PGL(2,5)."""
    def pairings(s):
        s = sorted(s)
        if not s:
            yield frozenset()
            return
        for b in s[1:]:
            for rest in pairings(set(s) - {s[0], b}):
                yield rest | {frozenset((s[0], b))}
    synthemes = list(set(pairings(set(range(6)))))
    totals = [frozenset(f) for f in itertools.combinations(synthemes, 5) if len({d for s in f for d in s}) == 15]
    where = {t: i for i, t in enumerate(totals)}
    sigma = lambda p: tuple(where[frozenset(frozenset(frozenset(p[x] for x in d) for d in s) for s in t)] for t in totals)
    after = lambda p, q: tuple(p[q[i]] for i in range(6))
    S6 = list(itertools.permutations(range(6)))
    gens = [(1, 0, 2, 3, 4, 5), (1, 2, 3, 4, 5, 0)]
    cycle_type = lambda p: sorted(len(c) for c in Permutation(list(p)).full_cyclic_form)
    image = {sigma(p) for p in S6 if p[5] == 5}
    pgl, _ = projective_line()
    match = next((b for b in itertools.permutations(range(6))
                  if {tuple(b[p[b.index(x)]] for x in range(6)) for p in image} == pgl), None)
    return {
        "S6 permutes the 15 synthemes and the 6 synthematic totals; on the totals it acts by an automorphism that sends a "
        "transposition to a product of three, so it is outer": len(synthemes) == 15 and len(totals) == 6
        and all(sigma(after(p, q)) == after(sigma(p), sigma(q)) for p in gens for q in S6)
        and cycle_type(sigma(gens[0])) == [2, 2, 2],
        "it carries the cone's S5, the stabilizer of the cone point, onto a transitive S5 conjugate to PGL(2,5) on the "
        "projective line: the two S5's in S6 are exchanged by the outer automorphism, which is why they act on the carrier "
        "by different modules": len(image) == 120 and len({p[0] for p in image}) == 6 and match is not None,
    }


def s5_weyl():
    """S5 is W(A4): the reflections in e_i - e_j are the transpositions, and they move the weights of 5 + Lambda^2 5."""
    E5 = sp.eye(5)
    refl = {(i, j): E5 - (E5[:, i] - E5[:, j]) * (E5[:, i] - E5[:, j]).T for i, j in itertools.combinations(range(5), 2)}
    swap = lambda i, j: sp.Matrix(5, 5, lambda r, c: int(r == {i: j, j: i}.get(c, c)))
    group, frontier = {tuple(E5)}, [E5]
    while frontier:
        nxt = []
        for M in frontier:
            for s in refl.values():
                key = tuple(s * M)
                if key not in group:
                    group.add(key)
                    nxt.append(s * M)
        frontier = nxt
    weights = [E5[:, i] for i in range(5)] + [E5[:, i] + E5[:, j] for i, j in carrier.edges()]
    atoms = [(i,) for i in range(5)] + list(carrier.edges())
    D = np.array(carrier.dirac(carrier.signless_incidence()), float)
    moves = []
    for (i, j), s in refl.items():
        f = {i: j, j: i}
        p = [atoms.index(tuple(sorted(f.get(v, v) for v in a))) for a in atoms]
        P = np.zeros((15, 15))
        P[p, range(15)] = 1
        moves.append(all(s * weights[k] == weights[p[k]] for k in range(15)) and np.allclose(P @ D, D @ P))
    return {
        "the reflection in e_i - e_j is the transposition (i j), and the ten reflections generate the 120 permutation "
        "matrices: S5 = W(A4)": all(s == swap(i, j) for (i, j), s in refl.items()) and len(group) == 120,
        "each reflection moves the weights e_i of the 5 and e_i + e_j of Lambda^2 5 as it moves the carrier's atoms, and "
        "commutes with D: S5 is the Weyl group of the binding's 5 + 10 (B5)": all(moves),
    }


def air801_surface():
    """AIR_801's matrix maps the hemi-icosahedron's faces onto its complement's."""
    A, Ac = _surface_labels()
    inv = lambda y: pow(y, 3, 5)
    m = lambda x: 3 * inv(1) % 5 if x == 5 else 5 if (x + 1) % 5 == 0 else (3 * x + 1) * inv(x + 1) % 5
    img = lambda F: {tuple(sorted(m(x) for x in f)) for f in F}
    return {
        "x -> (3x + 1)/(x + 1), the 801 matrix mod 5, turns the six axes in one 6-cycle and maps the ten faces of the "
        "hemi-icosahedron onto the ten of its complement, and back": Permutation([m(x) for x in range(6)]).cycle_structure
        == {6: 1} and img(A) == Ac and img(Ac) == A,
    }


def tick_cuts_f2():
    """The time clock on the four-cube's vertices, the cuts of K5 over F2: a fifth root of unity in F16."""
    E = carrier.edges()
    cut = lambda S: tuple(int((i in S) != (j in S)) for i, j in E)
    cube = list(itertools.product((0, 1), repeat=4))
    f = {x: cut({k + 1 for k in range(4) if x[k]}) for x in cube}
    back = {v: x for x, v in f.items()}
    turn = {x: back[cut({(k + 2) % 5 for k in range(4) if x[k]})] for x in cube}
    M = sp.Matrix([[turn[tuple(int(k == j) for k in range(4))][i] for j in range(4)] for i in range(4)])
    mod2 = lambda X: X.applyfunc(lambda e: e % 2)
    orbits = Counter(next(n for n in range(1, 6) if functools.reduce(lambda y, _: turn[y], range(n), x) == x) for x in cube)
    t = sp.symbols("t")
    return {
        "the vertex rotation (the time clock's 864 through kappa) moves the cuts linearly over F2, and on the cube's "
        "coordinates its matrix satisfies M^4 + M^3 + M^2 + M + I = 0 mod 2": all(
            turn[tuple((a + b) % 2 for a, b in zip(x, y))] == tuple((p + q) % 2 for p, q in zip(turn[x], turn[y]))
            for x in cube for y in cube) and mod2(M ** 4 + M ** 3 + M ** 2 + M + sp.eye(4)).is_zero_matrix and mod2(M) != sp.eye(4),
        "Phi_5 is irreducible over F2, so the cuts are F16 and the tick is a primitive fifth root of unity: it fixes the "
        "origin and turns the fifteen other vertices in three 5-cycles": sp.Poly(t ** 4 + t ** 3 + t ** 2 + t + 1, t,
                                                                                 modulus=2).is_irreducible
        and orbits == Counter({1: 1, 5: 15}),
    }


def small_joins():
    """Number-level maps: the grain to time, the misses as a kernel, the stages that never land, x mod 9, the rotor."""
    grain, time = spine.subgroup(72), spine.subgroup(TICK)
    proj = lambda x: 3456 * x % N
    E = carrier.edges()
    perm2 = sp.Matrix(5, 5, lambda r, c: int(r == 2 * c % 5))
    D2 = compound2(perm2)
    pent, star = (sp.Matrix(counts._oriented_cycle(k)) for k in (1, 2))
    tri = sp.zeros(10, 1)
    for (a, b), s in (((0, 1), 1), ((1, 2), 1), ((0, 2), -1)):
        tri[E.index((a, b))] = s
    bd = sp.zeros(10, 1)
    for k, sgn in ((0, 1), (1, -1), (2, 1)):
        bd[E.index((0, 1, 2)[:k] + (0, 1, 2)[k + 1:])] += sgn
    return {
        "the time coordinate x -> 3456 x maps the grain <72> onto the time clock with kernel <360> (12 points): it reads "
        "the golden index a of x = 216 a + 1440 b, since 216 = 1 and 1440 = 0 mod 5": {proj(x) for x in grain} == time
        and {x for x in grain if proj(x) == 0} == spine.subgroup(360) and len(spine.subgroup(360)) == 12
        and all((216 * a + 1440 * b) % 5 == a % 5 for a in range(20) for b in range(3)),
        "the miss set <5> is the kernel of the time coordinate x -> 3456 x": spine.subgroup(5) == {x for x in range(N) if proj(x) == 0},
        "the stages that never land, 0, 5 and 10, are exactly the stages in the miss set <5>": {
            k for k in range(15) if counts.first_landing(k) is None} == {k for k in range(15) if k in spine.subgroup(5)} == {0, 5, 10},
        "x -> x mod 9 maps the circle onto the vortex Z/9 with kernel <9>, through the atlas and through the 27-clock":
            all((x % 36) % 9 == (x % 27) % 9 == x % 9 for x in range(N)) and len(spine.subgroup(9)) == 480,
        "the doubling i -> 2i of AGL(1,5) turns the rotor plane by a quarter: the pentagon goes to the pentagram and the "
        "pentagram to minus the pentagon": D2 * pent == star and D2 * star == -pent,
        "the oriented triangle 0-1-2 of the triangle port is the boundary of the simplex's face 012, a cycle in ker B":
            bd == tri and (sp.Matrix(carrier.signed_incidence()) * tri).is_zero_matrix,
    }


def hodge_halfper():
    """The Hodge star is the deck involution of S -> e_S mod 2 Lambda on the 70 coordinate 4-forms."""
    D2 = np.rint(2 * glue.roots()).astype(int)
    S4 = list(itertools.combinations(range(8), 4))
    v = {S: np.array([int(i in S) for i in range(8)]) for S in S4}

    def in_e8(x2):                                             # is x2 / 2 in E8 (x2 an integer vector)?
        if np.all(x2 % 2 == 0):
            return (x2 // 2).sum() % 2 == 0
        return bool(np.all(x2 % 2 == 1) and ((x2 - 1) // 2).sum() % 2 == 0)
    comp = lambda S: tuple(i for i in range(8) if i not in S)
    band = {S: 240 - int(sum((-1) ** ((r2 @ (2 * v[S]) // 4) % 2) for r2 in D2)) for S in S4}
    halved = lambda x4: in_e8(x4 // 2) if np.all(x4 % 2 == 0) else False      # x4 = 4y: is y in E8?
    short = all(not in_e8(v[S]) and not any(halved(2 * v[S] - r2) for r2 in D2) for S in S4)
    classes = {frozenset((S, comp(S))) for S in S4}
    return {
        "e_S and e_T (S, T four of the eight coordinates) are congruent mod twice the lattice exactly when T = S or T is "
        "its complement, the Hodge dual: the Hodge star is the deck involution of S -> [e_S]": all(
            in_e8(v[S] - v[T]) == (T in (S, comp(S))) for S in S4 for T in S4) and len(classes) == 35,
        "the 35 classes are half-periods of type D8 (band 256), none containing 0 or a root: Hodge 70 = 35 + 35 sits on 35 "
        "of the 135 D8 half-periods": set(band.values()) == {256} and short,
    }


def memory_clock():
    """Layer 3's memory clock: its order-90 quotient, stepped by the circle, reads the vortex and the time clock."""
    _, _, _, A = spacetime.clock_quotient()
    order = spacetime.matrix_order(A)
    nine, ten = list(range(110, 119)), list(range(0, 10))
    powers = {x: np.linalg.matrix_power(A, x) for x in range(1, 50)}
    walk = lambda x, block: next(k for k in range(len(block)) if powers[x][block[k], block[0]] == 1)
    return {
        "the memory clock's 120-state quotient A has order 90, and 90 divides 4320, so k -> A^k is a homomorphism from "
        "the circle with kernel <90> (48 points), one circle step to one memory step (a selection)": order == 90
        and N % 90 == 0 and len(spine.subgroup(90)) == 48,
        "on its 9-cycle A^k moves by k mod 9 and on each 10-cycle by k mod 10, so the circle's composite to the 9-cycle is "
        "the vortex x mod 9, and to a 10-cycle reads the time coordinate x mod 5": all(
            walk(x, nine) == x % 9 and walk(x, ten) == x % 10 for x in range(1, 50)),
    }


def level_pairs():
    """How many maps join each pair of the six levels directly."""
    return Counter(tuple(sorted((LEVEL_OF[a], LEVEL_OF[b]))) for a, b, _, _, s, _ in JOINS
                   if s in MAPS and LEVEL_OF[a] != LEVEL_OF[b])


def no_two_maps():
    """No two maps hold the diagram together."""
    maps = [k for k, j in enumerate(JOINS) if j[4] in MAPS]
    degree = Counter(d for k in maps for d in JOINS[k][:2])
    cuts = [(JOINS[x][:2], JOINS[y][:2]) for x, y in itertools.combinations(maps, 2)
            if len(components([k not in (x, y) for k in range(len(JOINS))])) > 1]
    return {
        "every dot lies on at least three maps": all(degree[k] >= 3 for k in DOTS),
        "removing any two maps leaves the diagram connected": not cuts,
    }


def no_two_dots():
    """No one and no two dots hold the diagram together, nor the THEOREM diagram."""
    held = lambda statuses, dots, drop: len(components(
        [True] * len(JOINS), statuses=statuses, dots=[d for d in dots if d not in drop])) == 1
    thm = [d for d in DOTS if d not in ("gravity", "cosmology")]
    cuts = lambda statuses, dots: [drop for n in (1, 2) for drop in itertools.combinations(dots, n)
                                   if not held(statuses, dots, drop)]
    return {
        "removing any one or any two dots, with their maps, leaves the other dots joined": not cuts(MAPS, list(DOTS)),
        f"and the THEOREM maps alone: removing any one or two of the {len(thm)} dots they reach leaves the rest joined "
        "by THEOREM maps": not cuts((T,), thm),
    }

# ------------------------------------------------------------------- the 08:35-09:28 notes

def _two_root_sums():
    """The 240^2 ordered sums of two roots in doubled coordinates: points, integer codes and multiplicities."""
    R2 = np.rint(2 * glue.roots()).astype(np.int64)
    w = 64 ** np.arange(8, dtype=np.int64)
    code = lambda P: (np.asarray(P, dtype=np.int64) + 32) @ w
    pts, mult = np.unique((R2[:, None, :] + R2[None, :, :]).reshape(-1, 8), axis=0, return_counts=True)
    keys = code(pts)
    order = np.argsort(keys)
    return R2, code, 32 * int(w.sum()), pts[order], keys[order], mult[order]


def _sector_moments(n):
    """The six-site port's contrast and corner moments c_k = E_(k+1)/240 and u_k = 6 E_k - 5 E_(k+1)/240."""
    _, E = _walks()
    c = [sp.Rational(E[k + 1], 240) for k in range(n)]
    u = [6 * E[k] - sp.Rational(5 * E[k + 1], 240) for k in range(n)]
    return c, u


def walks_by_angle():
    """SHELLS, CONVOLUTION, SEVENTH, MEMORY and FOURTH: the walks between two roots depend only on their angle."""
    R2, code, shift, pts, keys, mult = _two_root_sums()

    def at(c):
        i = np.minimum(np.searchsorted(keys, c), len(keys) - 1)
        return np.where(keys[i] == c, mult[i], 0)

    def walks(t):
        ct = code(t)
        return (int(not t.any()), int(any(np.array_equal(t, r) for r in R2)), int(at(np.array([ct]))[0]),
                int(at(ct - code(R2) + shift).sum()), int((mult * at(ct - keys + shift)).sum()))
    table = {}
    for s in R2:
        table.setdefault(int(R2[0] @ s) // 4, set()).add(walks(R2[0] - s))
    one = {k: next(iter(v)) for k, v in table.items()}
    fourth = {k: sum(sp.binomial(4, j) * 240 ** (4 - j) * (-1) ** j * n[j] for j in range(5)) for k, n in one.items()}
    shells = Counter(zip(((pts ** 2).sum(1) // 4).tolist(), mult.tolist()))
    W, _ = _walks()
    return {
        "SHELLS: the 240^2 ordered sums of two roots fill 9361 points in five shells, the origin 240 times, the 240 "
        "roots 56 times each, 2160 vectors of square 4 fourteen times, 6720 of square 6 twice and the 240 doubles once; "
        "6720 = 240 x 56 / 2 and 2160 = 240 x 126 / 14": len(pts) == 9361 and shells == Counter(
            {(0, 240): 1, (2, 56): 240, (4, 14): 2160, (6, 2): 6720, (8, 1): 240})
        and 6720 == 240 * 56 // 2 and 2160 == 240 * 126 // 14 and 240 - 2 - 2 * 56 == 126,
        "MEMORY and FOURTH: the walks of length 0 to 4 between two roots depend only on their inner product (checked "
        "against all 240 partners): (1, 0, 240, 13440, 1260720), (0, 1, 56, 5253, 574224), (0, 0, 14, 1848, 253512), "
        "(0, 0, 2, 600, 107508) and (0, 0, 1, 168, 43936) at 2, 1, 0, -1 and -2, with fourth moments of 240 - A "
        "3389062320, -40411056, 3317832, 222708 and 228256": all(len(v) == 1 for v in table.values()) and one == {
            2: (1, 0, 240, 13440, 1260720), 1: (0, 1, 56, 5253, 574224), 0: (0, 0, 14, 1848, 253512),
            -1: (0, 0, 2, 600, 107508), -2: (0, 0, 1, 168, 43936)}
        and fourth == {2: 3389062320, 1: -40411056, 0: 3317832, -1: 222708, -2: 228256},
        "CONVOLUTION and SEVENTH: a root is a sum of three roots in 5253 = W_4 / 240 ways, of four in 574224 = W_5 / 240 "
        "and of six in 9734696160 = W_7 / 240, since W(E8) is transitive on the roots": one[1][3] == 5253 == W[4] // 240
        and one[1][4] == 574224 == W[5] // 240 and W[7] == 240 * 9734696160,
    }


def port_leak():
    """MOMENTS, DEGREE, LEAK, RANK and SEVENTH: the six-site port is a compression of the walks, at every order tested."""
    c, u = _sector_moments(22)
    W, _ = _walks()
    sites = [np.zeros(8, dtype=int)] + [2 * (np.eye(8, dtype=int)[a] + np.eye(8, dtype=int)[5]) for a in range(5)]
    roots2 = {tuple(r) for r in np.rint(2 * glue.roots()).astype(int)}
    nbr = lambda s: {tuple(s + np.array(r)) for r in roots2}
    V = {tuple(s) for s in sites}
    inside = {len(nbr(sites[i]) & nbr(sites[j]) & V) for i in range(6) for j in range(6) if i != j}
    common = {len(nbr(sites[i]) & nbr(sites[j])) for i in range(6) for j in range(6) if i != j}

    def schur(m):
        G0 = m[2] - m[1] ** 2
        G1 = m[3] - 2 * m[1] * m[2] + m[1] ** 3
        H2 = m[4] - 2 * m[1] * m[3] + m[1] ** 2 * m[2]
        return G0, G1, H2, H2 - G1 ** 2 / G0
    hankel = lambda m, n, a=0: sp.Matrix(n, n, lambda i, j: m[a + i + j]).det()
    R = np.rint(2 * glue.roots()).astype(int) / 2
    x = np.array([0.3, -0.17, 0.41, 0.05, -0.29, 0.13, 0.22, -0.08])
    trace = lambda y: np.trace((R.T * np.cos(2 * np.pi * R @ y)) @ R)
    eps = lambda y: 240 - np.cos(2 * np.pi * R @ y).sum()
    return {
        "MOMENTS and DEGREE: the six-port's couplings are walk moments, 241 = 240 + 1, 183 = 240 - 56 - 1, 235 = 240 - 5 "
        "and 495 = 183 + 6(56 - 4), with 56 = W_3 / W_2 the degree. In G0 = X^T X the 4 counts the other four sites of "
        "the clique next to both of two sites, and the 6 is the number of sites; DEGREE reads them as the cut rank and the "
        "cycle count, which are the same integers but not the same counts": W[3] // W[2] == 56
        and (c[1], c[2] - c[1] ** 2, u[1], u[2] - u[1] ** 2) == (241, 183, 235, 495) and inside == {4} and common == {56}
        and 183 == 240 - 56 - 1 and 495 == 183 + 6 * (56 - 4),
        "LEAK: every root has square 2, so the band's Hessian sum r r^T cos(2 pi r.x) has trace 480 - 2 eps everywhere; it "
        "is 60 I at 0, has trace 32 at the 224 saddles and is -4 I at the 256 points": np.isclose(trace(x), 480 - 2 * eps(x))
        and np.allclose((R.T * np.cos(0 * R[:, 0])) @ R, 60 * np.eye(8))
        and np.isclose(trace(R[0] / 2), 32) and np.allclose((R.T * np.cos(2 * np.pi * R @ np.eye(8)[0])) @ R, -4 * np.eye(8)),
        "LEAK: regressing the energy on the innovation leaves X^T Delta^2 X - G1 G0^-1 G1 with eigenvalues 55487966/183 "
        "and 131183830/99 (X^T Delta^2 X is 7137934 and 15637390 on the contrast and the corner), both positive: the six "
        "channels are a compression at the second step too": schur(c) == (183, 35366, 7137934, sp.Rational(55487966, 183))
        and schur(u) == (495, 84170, 15637390, sp.Rational(131183830, 99)),
        "RANK and SEVENTH: the contrast moments 241, 58264, 14121093, 3429473376, 834329053600, 203278964862240 and the "
        "corner moments 235, 55720, 13294695, 3187007040, 766796393440 have 3 x 3 Hankel windows 355722345463331 = "
        "7 x 11 x 47 x 120193 x 817793, 2865679183195625 = 5^4 x 4585086693113 and, on moments 2 to 6, "
        "2825534000633635065824, none zero": c[1:7] == [241, 58264, 14121093, 3429473376, 834329053600, 203278964862240]
        and u[1:6] == [235, 55720, 13294695, 3187007040, 766796393440]
        and hankel(c, 3, 1) == 355722345463331 == 7 * 11 * 47 * 120193 * 817793
        and hankel(u, 3, 1) == 2865679183195625 == 5 ** 4 * 4585086693113 and hankel(c, 3, 2) == 2825534000633635065824,
        "and every Hankel determinant of both sector measures through size 11 is positive, so the six sites' Krylov space "
        "grows by exactly 6 at every order through 10 (MEMORY lists this as not established)":
            all(hankel(c, n) > 0 and hankel(u, n) > 0 for n in range(1, 12)),
    }


def two_ticks():
    """TICK and COXETER: the coordinate five-cycle and the tick g = r r' are different order-5 actions on Lambda / 2 Lambda."""
    _, _, _, _, g, _ = spine.spine_clock()
    B = np.array(spine.frame()[0], float)
    P = np.zeros((8, 8))
    for i in range(5):
        P[(i + 1) % 5, i] = 1
    P[5:, 5:] = np.eye(3)
    r = np.linalg.solve(B, P @ B)
    D2 = np.rint(2 * glue.roots()).astype(int)
    classes = list(itertools.product((0, 1), repeat=8))
    index = {cl: i for i, cl in enumerate(classes)}
    band = [240 - int(sum((-1) ** ((r2 @ np.rint(2 * B @ np.array(cl)).astype(int) // 4) % 2) for r2 in D2)) for cl in classes]

    def orbits(M):
        step = [index[tuple(M @ np.array(cl) % 2)] for cl in classes]
        seen, out = set(), []
        for i in range(256):
            if i not in seen:
                o = [i]
                while step[o[-1]] != i:
                    o.append(step[o[-1]])
                seen |= set(o)
                out.append(o)
        return Counter((len(o), band[o[0]]) for o in out), all(len({band[j] for j in o}) == 1 for o in out)
    ri, gi = np.rint(r).astype(int), np.rint(g).astype(int)
    return {
        "TICK and COXETER: the coordinate five-cycle r alone keeps the lattice and fixes 16 half-periods (the origin, 10 at "
        "224 and 5 at 256), turning the other 240 in 48 band-keeping five-cycles; the tick g = r r' = c'^6 fixes only the "
        "origin and makes 51 (layer 23). The two order-5 actions differ": np.allclose(r, ri)
        and orbits(ri) == (Counter({(1, 0): 1, (1, 224): 10, (1, 256): 5, (5, 224): 22, (5, 256): 26}), True)
        and orbits(gi) == (Counter({(1, 0): 1, (5, 224): 24, (5, 256): 27}), True),
    }


def filled_simplex():
    """HELICITY: K = I + 2(T + T^-1) on the edges, and the filled 4-simplex."""
    R5 = sp.Matrix(5, 5, lambda r, c: int(r == (c + 1) % 5))
    T = compound2(R5)
    K = sp.eye(10) + 2 * (T + T.T)
    Bs = sp.Matrix(carrier.signed_incidence())
    cyc = sp.Matrix.hstack(*Bs.nullspace())
    mov = sp.Matrix.hstack(*(T - sp.eye(10)).T.columnspace())
    Km = (mov.T * mov).inv() * mov.T * K * mov
    faces = {k: list(itertools.combinations(range(5), k + 1)) for k in range(5)}

    def bd(k):
        M = sp.zeros(len(faces[k - 1]), len(faces[k]))
        for j, f in enumerate(faces[k]):
            for i in range(len(f)):
                M[faces[k - 1].index(f[:i] + f[i + 1:]), j] = (-1) ** i
        return M
    d = {k: bd(k) for k in range(1, 5)}
    return {
        "HELICITY: K = I + 2(T + T^-1) is 5 on the rotor plane and +-sqrt5 four times each elsewhere; on the eight moving "
        "edges K^2 = 5, trace 0, det 625, and on the cycles 5, sqrt5 and -sqrt5 twice each":
            K.eigenvals() == {5: 2, sp.sqrt(5): 4, -sp.sqrt(5): 4} and mov.shape[1] == 8
            and sp.simplify(Km * Km - 5 * sp.eye(8)) == sp.zeros(8) and sp.simplify(Km.trace()) == 0
            and sp.simplify(Km.det()) == 625
            and ((cyc.T * cyc).inv() * cyc.T * K * cyc).eigenvals() == {5: 2, sp.sqrt(5): 2, -sp.sqrt(5): 2},
        "HELICITY: the filled 4-simplex has boundary ranks 4, 6, 4, 1 and its three interior Laplacians are 5I, so its "
        "first homology is 0: the six cycles of K5 bound triangles": [d[k].rank() for k in range(1, 5)] == [4, 6, 4, 1]
        and all(d[k].T * d[k] + d[k + 1] * d[k + 1].T == 5 * sp.eye(len(faces[k])) for k in (1, 2, 3))
        and 10 - d[1].rank() - d[2].rank() == 0,
    }


def charge_marks():
    """MARKS and CHARGE_WEIGHT: the hypercharge is 5/6 of a duad's 10-weight, and the charge lives on the cuts."""
    I5 = sp.eye(5)
    P5 = I5 - sp.ones(5, 5) / 5
    om = lambda S: sum((I5[:, i] for i in S), sp.zeros(5, 1)) - sp.Rational(len(S), 5) * sp.ones(5, 1)
    Yf = lambda i, j: sp.Rational(5, 6) * om((i, j))
    Tf = lambda i, j: (I5[:, i] - I5[:, j]) / 2
    Qf = lambda i, j: Yf(i, j) + Tf(i, j)
    pairs = list(itertools.permutations(range(5), 2))
    avg = lambda f: sum((f(i, j) * f(i, j).T for i, j in pairs), sp.zeros(5)) / 20
    Y, T3, Q = Yf(3, 4), Tf(3, 4), Qf(3, 4)
    Bs = sp.Matrix(carrier.signed_incidence())
    x = Bs.T * Q / 5
    cyc = sp.Matrix.hstack(*Bs.nullspace())
    t = sp.symbols("t")
    L = sp.zeros(5)
    for i, j in carrier.edges():
        L[i, j] = L[j, i] = -(2 if (j - i) % 5 in (1, 4) else 3)
    for i in range(5):
        L[i, i] = -sum(L[i, k] for k in range(5) if k != i)
    return {
        "CHARGE_WEIGHT: Y = (5/6) w_2({3, 4}) is 5/6 of the weak duad's 10-weight, with square 5/6, and it is layer 24's "
        "hypercharge; T3 is half the A4 root e_3 - e_4, square 1/2, orthogonal to Y; |Q|^2 = 4/3": list(Y) == [
            sp.Rational(-1, 3)] * 3 + [sp.Rational(1, 2)] * 2 and [sp.Rational(y.numerator, y.denominator) for y in assignment.Y[:5]]
        == list(Y) and (Y.T * Y)[0] == sp.Rational(5, 6) and (T3.T * T3)[0] == sp.Rational(1, 2) and (Y.T * T3)[0] == 0
        and (Q.T * Q)[0] == sp.Rational(4, 3),
        "MARKS: over the 20 ordered weak pairs the outer products of Y, T3 and Q average (5/24) P, (1/8) P and (1/3) P, "
        "and the 20 charge vectors average 0": avg(Yf) == sp.Rational(5, 24) * P5 and avg(Tf) == P5 / 8
        and avg(Qf) == P5 / 3 and sum((Qf(i, j) for i, j in pairs), sp.zeros(5, 1)) == sp.zeros(5, 1),
        "MARKS: the minimum-norm lift B^T Q / 5 of the charge to the edges has square 4/15 and lies in the cuts with zero "
        "cycle part, so a readout that vanishes on cuts sees no charge": Bs * x == Q and (x.T * x)[0] == sp.Rational(4, 15)
        and cyc.T * x == sp.zeros(6, 1),
        "MARKS: with the pentagon edges weighted 2 and the pentagram 3 the Laplacian's polynomial is t (t^2 - 25 t + 155)^2; "
        "its 155 shares an integer with the 155 block and is not a map to it": sp.expand(L.charpoly(t).as_expr()
                                                                                   - t * (t ** 2 - 25 * t + 155) ** 2) == 0,
    }


def infrared():
    """INFRARED: the infrared density, the heat tails and the fixed plane of the edge tick, in both orientations."""
    E, t, c = sp.symbols("E t c", positive=True)
    R5 = sp.Matrix(5, 5, lambda r, k: int(r == (k + 1) % 5))
    T = compound2(R5)
    one = sp.ones(10, 1)
    fixed = sp.Matrix.hstack(*(T - sp.eye(10)).nullspace())
    proj = lambda F: (one.T * F * (F.T * F).inv() * F.T * one)[0]
    pent, star = (sp.Matrix(counts._oriented_cycle(k)) for k in (1, 2))
    cyc_or = [(i, j) if (j - i) % 5 in (1, 2) else (j, i) for i, j in carrier.edges()]
    Tc = sp.zeros(10, 10)
    for k, (a, b) in enumerate(cyc_or):
        Tc[cyc_or.index(((a + 1) % 5, (b + 1) % 5)), k] = 1
    parts = [14, 3, 62, 10, 251, 161, 51, 7]
    primes = sorted({q for n in parts for q in sp.factorint(n)})
    from sympy.polys.matrices import DomainMatrix
    F2 = DomainMatrix.from_Matrix(sp.Matrix([[sp.factorint(n).get(q, 0) % 2 for q in primes] for n in parts]))
    return {
        "INFRARED: 1536 = 256 x 3 x 2, from (2 pi)^8 = 256 pi^8 and the unit 8-ball pi^4 / 24, and densities c E^3, c E^4, "
        "c E^5 have heat tails 6c t^-4, 24c t^-5 and 120c t^-6": 1536 == 256 * 3 * 2 and all(
            sp.simplify(sp.integrate(c * E ** n * sp.exp(-t * E), (E, 0, sp.oo)) - c * sp.factorial(n) / t ** (n + 1)) == 0
            for n in (3, 4, 5)),
        "INFRARED, corrected: the edge tick's fixed plane is spanned by the oriented pentagon and pentagram, both of square "
        "5, with sums 3 and 1 in the lexicographic orientation, so it holds 9/5 + 1/5 = 2 of the all-ones vector's square "
        "(the note has squares 5 and 6 and 17/10); in the cyclic orientation the tick is a plain permutation fixing the "
        "all-ones vector, and the value is exactly 10": fixed.shape[1] == 2 and proj(fixed) == 2
        and (pent.T * pent)[0] == (star.T * star)[0] == 5 and (sum(pent), sum(star)) == (3, 1) and (pent.T * star)[0] == 0
        and T * pent == pent and T * star == star and Tc * one == one and proj(sp.Matrix.hstack(*(Tc - sp.eye(10)).nullspace())) == 10,
        "MOMENTS: the eight square-free parts 14, 3, 62, 10, 251, 161, 51, 7 of the positive critical energies below 256 "
        "have full rank 8 over F2": F2.convert_to(sp.GF(2)).rank() == 8 and len(primes) == 8,
    }


def stated_block():
    """MEMORY's stated fixed block, as arithmetic (the block is not stored here)."""
    return {
        "mean [[240, -1], [-1, 240]] has eigenvalues 239 and 241, variance [[271, 100], [100, 271]] has 171 and 371, and "
        "the golden variance 1987/10 - (31/10) K exceeds 171 on both helicities because 277^2 = 76729 > 5 x 31^2 = 4805":
            sp.Matrix([[240, -1], [-1, 240]]).eigenvals() == {239: 1, 241: 1}
            and sp.Matrix([[271, 100], [100, 271]]).eigenvals() == {171: 1, 371: 1}
            and all(sp.Rational(1987, 10) - sp.Rational(31, 10) * k > 171 for k in (sp.sqrt(5), -sp.sqrt(5)))
            and 277 ** 2 == 76729 > 5 * 31 ** 2 == 4805,
    }

def notes_1007():
    """ATLAS, SCRIPT, SHELLS (09:43) and SYMBOL: the coordinate classes, the angle multiplicities and the collar witness."""
    R = glue.roots()
    integer = np.all(np.isclose(R, np.round(R)), axis=1)
    cls = [int(round(2 * r[:5].sum())) % 5 for r in R]
    table = Counter((k, bool(i)) for k, i in zip(cls, integer))
    grade = Counter((assignment.GRADE[k], int(round(2 * r[:5].sum() / 10)) % 5) for r, k, _, _ in assignment.classify())
    zero3 = [r for r in R if np.allclose(r[5:], 0)]
    _, _, Ap = glue.a4_pair()
    Ap_int = np.all(np.isclose(Ap, np.round(Ap)), axis=1)
    angles = Counter(int(round(R[0] @ r)) for r in R)
    x = np.array([28, 28, 6, 2, 1, 0, 0, 0]) / 10
    c = np.cos(R @ x)
    grad = (R.T * np.sin(R @ x)).sum(1)
    H = (R.T * c) @ R
    g = grad / np.linalg.norm(grad)
    P = np.eye(8) - np.outer(g, g)
    v = g + np.sign(g[0]) * np.eye(8)[0]
    tangent = (np.eye(8) - 2 * np.outer(v, v) / (v @ v))[:, 1:]
    least = (np.linalg.eigvalsh(P @ H @ P)[1], np.linalg.eigvalsh(tangent.T @ H @ tangent)[0])
    return {
        "ATLAS and SCRIPT: twice the sum of the first five coordinates, mod 5, splits the roots 40, 50, 50, 50, 50 with "
        "(integer, spinor) counts (32, 8), (10, 40), (30, 20), (30, 20), (10, 40); that class is twice layer 24's grade in "
        "E8 / L0, the glue's doubling. The roots with zeros on the last three coordinates are D5's 40, of which A4 is the "
        "20 with opposite signs, and A4' is 12 integer roots on the last three coordinates and 8 spinors":
            {k: (table[(k, True)], table[(k, False)]) for k in range(5)} == {0: (32, 8), 1: (10, 40), 2: (30, 20), 3: (30, 20),
                                                                           4: (10, 40)}
            and all(cl == 2 * gr % 5 for gr, cl in grade) and len(zero3) == 40
            and sum(1 for r in zero3 if np.isclose(r[:5].sum(), 0)) == 20 and (Ap_int.sum(), (~Ap_int).sum()) == (12, 8),
        "SHELLS (09:43): the inner products with a fixed root are 2, 1, 0, -1, -2 on 1, 56, 126, 56 and 1 roots, the "
        "multiplicities of the five walk rows": angles == Counter({2: 1, 1: 56, 0: 126, -1: 56, -2: 1}),
        "SYMBOL: at the collar witness x = (28, 28, 6, 2, 1, 0, 0, 0)/10 the integer roots give sum cos = 2[(sum cos x_i)^2 "
        "- sum cos^2 x_i] = 15.8548946233 and the spinors 128 (prod cos(x_i/2) + prod sin(x_i/2)) = 3.5105736454, so "
        "eps = 220.6345317313; the gradient vanishes on the last three axes, which carry the Hessian eigenvalue 12.54149 "
        "three times, and the least eigenvalue on the tangent hyperplane is 6.985582 by the projector and by a Householder "
        "basis, positive (computed, not a closed form)": np.isclose(c[integer].sum(), 15.8548946233, atol=1e-9)
        and np.isclose(c[~integer].sum(), 3.5105736454, atol=1e-9) and np.isclose(240 - c.sum(), 220.6345317313, atol=1e-9)
        and np.isclose(2 * (np.cos(x).sum() ** 2 - (np.cos(x) ** 2).sum()), c[integer].sum())
        and np.isclose(128 * (np.prod(np.cos(x / 2)) + np.prod(np.sin(x / 2))), c[~integer].sum())
        and np.allclose(grad[5:], 0) and np.allclose(H[5:, 5:], 12.54149 * np.eye(3), atol=1e-5) and np.allclose(H[:5, 5:], 0)
        and all(np.isclose(t, 6.985582, atol=1e-6) for t in least),
    }


def notes_1007_arithmetic():
    """LEDGER, LEDGER48 and the 10:07 model: their sums, as arithmetic."""
    return {
        "1 + 255/5 = 52 orbits (51 five-cycles and the origin); 271 - 100 = 171 and 271 + 100 = 371; 2 x 44 x 2 = 176; "
        "4320 = 36 x 120 = 15 x 36 x 8, 864 = 24 x 36 and 9361 = 260 x 36 + 1, shared integers that join nothing":
            1 + 255 // 5 == 52 and 255 % 5 == 0 and (271 - 100, 271 + 100) == (171, 371) and 2 * 44 * 2 == 176
            and 36 * 120 == 15 * 36 * 8 == 4320 and 24 * 36 == 864 and 260 * 36 + 1 == 9361,
    }


# ------------------------------------------------------------------- the hub's Golden port (10:33) and the 10:38 model

def _walk_entries():
    """(H^n)_(x, y) for H = 240 - A and lattice points given times 10, through the two-root sums (n <= 4)."""
    R2, code, shift, pts, keys, mult = _two_root_sums()
    roots10 = {tuple(r) for r in assignment.roots10()}

    def at(c):
        i = np.minimum(np.searchsorted(keys, c), len(keys) - 1)
        return np.where(keys[i] == c, mult[i], 0)
    cache = {}

    def walks(t10):
        k = tuple(int(v) for v in t10)
        if k not in cache:
            t = np.asarray(t10) // 5
            ct = code(t)
            cache[k] = (int(not t.any()), int(k in roots10), int(at(np.array([ct]))[0]),
                        int(at(ct - code(R2) + shift).sum()), int((mult * at(ct - keys + shift)).sum()))
        return cache[k]
    return lambda t10, n: sum(sp.binomial(n, j) * 240 ** (n - j) * (-1) ** j * walks(t10)[j] for j in range(n + 1))


def _golden_sites():
    """The hub's Golden root-site port: near edges to e_i - e_(i+1), far edges to the glue roots site_i - (mu_i + mu_(i+1))."""
    site, sign = [], []
    for a, b in carrier.edges():
        d = (b - a) % 5
        if d in (1, 4):
            i = a if d == 1 else b
            site.append(assignment.SITE[i] - assignment.SITE[(i + 1) % 5])
        else:
            i = a if d == 2 else b
            site.append(assignment.SITE[i] - assignment.TWIN[i] - assignment.TWIN[(i + 1) % 5])
        sign.append(1 if d in (1, 2) else -1)
    return site, sign


def golden_root_port():
    """The hub's OES_Unified_Model (10:33): the Golden root-site port T_G = F P_cycle and its moments."""
    Hn = _walk_entries()
    site, sign = _golden_sites()
    roots10 = {tuple(r) for r in assignment.roots10()}
    B = sp.Matrix(carrier.signed_incidence())
    Pc = sp.eye(10) - B.T * B / 5
    Cb = sp.Matrix.hstack(*B.nullspace())
    G = {n: sp.Matrix(10, 10, lambda e, f: sign[e] * sign[f] * Hn(site[f] - site[e], n)) for n in range(5)}
    M = {n: (Cb.T * Cb).inv() * Cb.T * G[n] * Cb for n in range(3)}
    x = sp.symbols("x")
    return {
        "the hub's F sends the five near edges to the roots e_i - e_(i+1) and the five far edges to the glue roots "
        "site_i - (mu_i + mu_(i+1)), a signed isometry onto ten distinct roots, so T_G = F P_cycle has T_G* T_G = "
        "P_cycle and T_G B^T = 0": all(tuple(t) in roots10 for t in site) and len({tuple(t) for t in site}) == 10
        and G[0] == sp.eye(10),
        "its moment traces tr(P_cycle F^T H^n F) are 1442, 347900, 84180666 and 20416532280 for n = 1 to 4; the fourth "
        "is the trace the notes left out": [(Pc * G[n]).trace() for n in range(1, 5)] == [1442, 347900, 84180666, 20416532280],
        "its means are 239, 241 and 481/2 -+ sqrt5/10 (multiplicities 1, 1, 2, 2) and its variances 371, 171 and "
        "(1987 -+ 31 sqrt5)/10: MEMORY's stated block, with the floor 171, is this port's fixed channels":
            sp.expand(M[1].charpoly(x).as_expr() - (x - 239) * (x - 241) * (x ** 2 - 481 * x + sp.Rational(289201, 5)) ** 2) == 0
            and sp.expand((M[2] - M[1] * M[1]).charpoly(x).as_expr()
                          - (x - 171) * (x - 371) * (x ** 2 - sp.Rational(1987, 5) * x + sp.Rational(985841, 25)) ** 2) == 0,
    }


def shared_bath():
    """The hub's clique port and Golden port in one bath: the cross map, the joint span and the joint Krylov ranks."""
    from sympy.polys.matrices import DomainMatrix
    Hn = _walk_entries()
    clique, sites, TC, Fm = _two_ports()
    roots10 = {tuple(r) for r in assignment.roots10()}
    B = sp.Matrix(carrier.signed_incidence())
    Pc = sp.eye(10) - B.T * B / 5
    cross = TC.T * Fm * Pc * Fm.T * TC
    J = sp.Matrix.hstack(TC, Fm * sp.Matrix.hstack(*B.nullspace()))
    Hm = {n: sp.Matrix(len(sites), len(sites), lambda i, j: Hn(sites[j] - sites[i], n)) for n in range(5)}
    ranks = [DomainMatrix.from_Matrix(sp.Matrix(sp.BlockMatrix([[J.T * Hm[i + j] * J for j in range(d + 1)]
                                                                 for i in range(d + 1)]))).rank() for d in range(3)]
    c, u = _sector_moments(8)
    hankel = lambda m: sp.Matrix(4, 4, lambda i, j: m[i + j]).det()
    return {
        "the hub's clique is six roots whose differences are all roots, a six-site port with the moments of layer 22's; it "
        "shares two of its sites with the Golden port, 14 in all": all(tuple(a - b) in roots10 for a, b in
                                                                       itertools.permutations(clique, 2)) and len(sites) == 14,
        "the cross map T_C* T_G has rank 2 with squared singular values 4/5 and 2/5, the joint span is 12, and the joint "
        "Krylov ranks are 12, 24 and 36 through degree 2": cross.rank() == 2
        and sorted(cross.eigenvals(multiple=True)) == [0, 0, 0, 0, sp.Rational(2, 5), sp.Rational(4, 5)] and J.rank() == 12
        and ranks == [12, 24, 36],
        "the seventh walk gives the clique's 4 x 4 Hankel determinants 31566087163013649 (contrast) and "
        "1694632079790338625 (corner), positive: a fourth frequency in each channel": hankel(c) == 31566087163013649
        and hankel(u) == 1694632079790338625,
    }


def notes_1038():
    """The sibling's MODEL of 10:38: charges on the classes, the root triangles, the transpositions and the fivefold map."""
    F_ = Fraction
    rows = assignment.classify()
    cls = lambda r: int(round(r[:5].sum() / 5)) % 5                      # twice the first-five sum (r is times 10)
    h = [F_(2, 3)] * 3 + [F_(-1)] * 2 + [F_(0)] * 3
    Qp = lambda r: assignment.dot(assignment.T3, r) + assignment.dot(h, r) / 2
    t3 = lambda r: assignment.dot(assignment.T3, r)
    up = Counter(cls(r) for r, *_ in rows if t3(r) == F_(1, 2))
    half = lambda K: (sum(t3(r) ** 2 for r, *_ in rows if cls(r) in K), sum(Qp(r) ** 2 for r, *_ in rows if cls(r) in K))
    cubic = {k: sum(Qp(r) ** 3 for r, *_ in rows if cls(r) == k) for k in range(5)}
    R10 = assignment.roots10()
    roots = {tuple(r) for r in R10}
    tri = Counter(tuple(sorted((cls(a), cls(b), cls(-(a + b))))) for a in R10 for b in R10 if tuple(-(a + b)) in roots)
    P = lambda p: sp.Matrix(5, 5, lambda i, j: int(i == p[j]))
    trans = [tuple(j if k == i else i if k == j else k for k in range(5)) for i, j in itertools.combinations(range(5), 2)]
    B = sp.Matrix(carrier.signed_incidence())
    Pcut = B.T * B / 5
    E = carrier.edges()
    Mp = sp.zeros(10, 5)
    for i in range(5):
        a, b = i, (i + 1) % 5
        Mp[E.index((min(a, b), max(a, b))), i] = 1 if a < b else -1
    Tm = (sp.eye(10) - Pcut) * Mp
    Zb = sp.Matrix.hstack(*sp.ones(1, 5).nullspace())
    A2 = sp.Matrix(5, 5, lambda i, j: int((i - j) % 5 in (2, 3)))
    pent, star = (sp.Matrix(counts._oriented_cycle(k)) for k in (1, 2))
    R5 = sp.Matrix(5, 5, lambda r, k: int(r == (k + 1) % 5))
    Sz = (Zb.T * Zb).inv() * Zb.T * (R5 + R5.T) * Zb
    return {
        "with h = (2, 2, 2, -3, -3)/3 and Q = T3 + h/2 (the note's signs) every charge is a multiple of 1/3, the traces of "
        "T3^2 and Q^2 are 30 and 80 (3 : 8), and 56 roots have T3 = +1/2, 6 + 15 + 10 + 10 + 15 by class; a one-of-each-pair "
        "selection of the mixed roots has 25 of them (layer 24)": all((3 * Qp(r)).denominator == 1 for r, *_ in rows)
        and sum(t3(r) ** 2 for r, *_ in rows) == 30 and sum(Qp(r) ** 2 for r, *_ in rows) == 80
        and up == Counter({0: 6, 1: 15, 2: 10, 3: 10, 4: 15}),
        "the twin's 20 roots carry no T3 and no h, the carrier's are 6 neutral and 14 charged; classes 1 + 4 and 0 + 2 + 3 "
        "each have traces 15 and 40; the cubic charge is 0, 40/9, -80/9, 80/9, -40/9 on classes 0 to 4, cancelling only in "
        "conjugate pairs": half({1, 4}) == half({0, 2, 3}) == (15, 40)
        and cubic == {0: 0, 1: F_(40, 9), 2: F_(-80, 9), 3: F_(80, 9), 4: F_(-40, 9)}
        and Counter(t3(r) == 0 and assignment.dot(h, r) == 0 for r, k, *_ in rows if k == "(24,1)") == Counter({True: 6, False: 14})
        and all(t3(r) == 0 and assignment.dot(h, r) == 0 for r, k, *_ in rows if k == "(1,24)"),
        "three roots sum to zero in 13440 = W_3 ordered ways, with class multisets 0+1+4 and 0+2+3 (3000 each), 1+1+3, "
        "1+2+2, 2+4+4, 3+3+4 (1800 each) and 0+0+0 (240), none inside one mixed class; negation swaps 1 with 4 and 2 with 3":
            sum(tri.values()) == 13440 and tri == Counter({(0, 1, 4): 3000, (0, 2, 3): 3000, (1, 1, 3): 1800, (1, 2, 2): 1800,
                                                            (2, 4, 4): 1800, (3, 3, 4): 1800, (0, 0, 0): 240})
            and Counter((cls(r), cls(-r)) for r in R10) == Counter({(1, 4): 50, (4, 1): 50, (2, 3): 50, (3, 2): 50, (0, 0): 40}),
        "the ten transpositions sum to 5I + J on the sites and to 5 P_cut on the edges (0 on the cycles), so no map that "
        "treats the sites alike reaches the cycles; the fivefold map (site i to its outgoing edge, then the cycle part) has "
        "rank 4 on the trace-free sites, misses the two fixed channels there, and has Gram (2I - A_2)/5 = (5I + T)/10 with "
        "T = 2(P + P^-1) + I, T^2 = 5, eigenvalues (5 +- sqrt5)/10 twice (ratio phi^2)":
            sum((P(t) for t in trans), sp.zeros(5)) == 5 * sp.eye(5) + sp.ones(5, 5)
            and sum((compound2(P(t)) for t in trans), sp.zeros(10)) == 5 * Pcut and (Tm * Zb).rank() == 4
            and pent.T * Tm * Zb == sp.zeros(1, 4) and star.T * Tm * Zb == sp.zeros(1, 4)
            and Zb.T * Tm.T * Tm * Zb == Zb.T * (2 * sp.eye(5) - A2) / 5 * Zb
            and Sz * Sz + Sz - sp.eye(4) == sp.zeros(4) and (2 * Sz + sp.eye(4)) ** 2 == 5 * sp.eye(4)
            and sp.simplify((5 + sp.sqrt(5)) / (5 - sp.sqrt(5)) - ((1 + sp.sqrt(5)) / 2) ** 2) == 0,
        "the root graph's eigenvalue squares 56^2 + 8 x 28^2 + 35 x 8^2 + 112 x 4 + 84 x 16 = 13440 = 240 x 56 = W_3; the clock "
        "steps 120, 1440, 840, 1080, 3360 and 27 have orders 36, 3, 36, 4, 9 and 160, with 1080 + 3360 = 120, and the widths "
        "2, 3, 4, 5, 6, 8 have orders 2160, 1440, 1080, 864, 720, 540 while 7 and 13 generate":
            56 ** 2 + 8 * 28 ** 2 + 35 * 8 ** 2 + 112 * 4 + 84 * 16 == 13440 == 240 * 56
            and [N // gcd(x, N) for x in (120, 1440, 840, 1080, 3360, 27)] == [36, 3, 36, 4, 9, 160] and (1080 + 3360) % N == 120
            and [N // gcd(x, N) for x in (2, 3, 4, 5, 6, 8, 7, 13)] == [2160, 1440, 1080, 864, 720, 540, 4320, 4320],
        "the vector meeting eight roots of pairwise product 1 at product 1 is their sum over 9, of square 8/9, not a root, "
        "so the eight-root frame has no ninth root": (lambda F8: sp.Rational(int(sum(F8) @ sum(F8)), 4 * 81) == sp.Rational(8, 9)
                                                    and all(sp.Rational(int(sum(F8) @ r), 4 * 9) == 1 for r in F8))(_eight_roots2()),
    }


def _eight_roots2():
    """Eight roots with pairwise inner product 1, in doubled coordinates."""
    R2 = np.rint(2 * glue.roots()).astype(int)
    chosen = [R2[0]]
    for r in R2:
        if all(int(r @ c) == 4 for c in chosen):
            chosen.append(r)
        if len(chosen) == 8:
            break
    return chosen


def _marked():
    """The fivefold marking: the edges' signed five-cycle U, K = I + 2(U + U^T), the fixed and moving cycles, and the
    marked map L = P_cycle N P_A4, where N sends each site to its outgoing edge."""
    E = carrier.edges()
    B = sp.Matrix(carrier.signed_incidence())
    Pc = sp.eye(10) - B.T * B / 5
    R5 = sp.Matrix(5, 5, lambda r, c: int(r == (c + 1) % 5))
    U = compound2(R5)
    Qf = sum((U ** k for k in range(5)), sp.zeros(10)) / 5
    N = sp.zeros(10, 5)
    for i in range(5):
        a, b = i, (i + 1) % 5
        N[E.index((min(a, b), max(a, b))), i] = 1 if a < b else -1
    return Pc, R5, U, sp.eye(10) + 2 * (U + U.T), Qf, Pc - Qf, Pc * N * (sp.eye(5) - sp.ones(5, 5) / 5)


def marked_charge():
    """The hub's marked charge map (11:18) and the sibling's marks (11:04): L = P_cycle N P_A4 and its two-probe decoder."""
    Pc, R5, U, K, Qf, Pm, L = _marked()
    r5 = sp.sqrt(5)
    Pg = {s: Pm * (sp.eye(10) + s * K / r5) / 2 for s in (1, -1)}
    A2 = sp.Matrix(5, 5, lambda i, j: int((i - j) % 5 in (2, 3)))
    q = lambda i, j: sp.Matrix([1 if k == i else 0 if k == j else sp.Rational(-1, 3) for k in range(5)])
    W = sp.Matrix(2, 2, lambda m, s: sp.radsimp(((L * q(0, m + 1)).T * Pg[1 - 2 * s] * L * q(0, m + 1))[0]))
    Wi = W.inv().applyfunc(sp.radsimp)
    zero = lambda a: sp.expand(sp.radsimp(a)) == 0
    perms = [sp.Matrix(5, 5, lambda r, c, p=p: int(r == p[c])) for p in itertools.permutations(range(5))]
    lift = [compound2(g) for g in perms]
    marks = [q(i, j) for i, j in itertools.permutations(range(5), 2)]
    return {
        "a chosen fivefold order sends site i to its outgoing edge; the cycle part L = P_cycle N P_A4 has rank 4, "
        "commutes with the five-cycle and misses the two fixed cycles, with L^T L = (2I - A_2)/5 on the sites and "
        "L L^T = ((5I + K)/10) P_moving on the edges, where K^2 = 5":
            L.rank() == 4 and U * L == L * R5 and (Qf * L).is_zero_matrix and L.T * L == (2 * sp.eye(5) - A2) / 5
            and L * L.T == (5 * sp.eye(10) + K) / 10 * Pm and K * K * Pm == 5 * Pm,
        "the twenty marks (1 at i, 0 at j, -1/3 elsewhere) have covariance P_A4/3; a near mark (j = i + 1) puts "
        "(17 +- 5 sqrt5)/45 into the Golden channels K = +-sqrt5 (square 34/45), a far mark (j = i + 2) (13 +- sqrt5)/45 "
        "(square 26/45)": sum((m * m.T for m in marks), sp.zeros(5)) / 20 == (sp.eye(5) - sp.ones(5, 5) / 5) / 3
            and all(zero(W[i, j] - w) for (i, j), w in zip(itertools.product(range(2), repeat=2),
                                                            ((17 + 5 * r5) / 45, (17 - 5 * r5) / 45, (13 + r5) / 45, (13 - r5) / 45))),
        "so the two responses decode the two Golden densities: the mixing determinant is 32 sqrt5/675, rho_phi + rho_psi "
        "= 15(5 R_far - R_near)/16 and rho_phi - rho_psi = 3 sqrt5 (13 R_near - 17 R_far)/16, an error eta in each "
        "response costs at most 45(1 + sqrt5) eta/16, and both densities are nonnegative exactly when R_near/R_far lies "
        "in [(49 - 12 sqrt5)/41, (49 + 12 sqrt5)/41]; with equal densities, at low energy, the ratio is 17/13":
            zero(W.det() - 32 * r5 / 675)
            and zero(Wi[0, 0] + Wi[1, 0] + sp.Rational(15, 16)) and zero(Wi[0, 1] + Wi[1, 1] - sp.Rational(75, 16))
            and zero(Wi[0, 0] - Wi[1, 0] - 39 * r5 / 16) and zero(Wi[0, 1] - Wi[1, 1] + 51 * r5 / 16)
            and zero(max(abs(Wi[k, 0]) + abs(Wi[k, 1]) for k in range(2)) - 45 * (1 + r5) / 16)
            and zero(W[0, 1] / W[1, 1] - (49 - 12 * r5) / 41) and zero(W[0, 0] / W[1, 0] - (49 + 12 * r5) / 41)
            and zero((W[0, 0] + W[0, 1]) / (W[1, 0] + W[1, 1]) - sp.Rational(17, 13)),
        "averaged over S5 the marked map is 0 (Hom_S5(A4, cycles) = 0) while its square averages to P_cycle/3, so the "
        "marks' image covariance L L^T/3 averages to P_cycle/9; on the moving cycles L L^T/3 has inverse (3/2)(5I - K), "
        "and two fixed probes complete the whitened readings to P_cycle":
            sum((h * L * g.T for h, g in zip(lift, perms)), sp.zeros(10, 5)).is_zero_matrix
            and sum((h * L * L.T * h.T for h in lift), sp.zeros(10)) / 120 == Pc / 3
            and L * L.T / 3 * sp.Rational(3, 2) * (5 * sp.eye(10) - K) * Pm == Pm and Pm + Qf == Pc,
    }


def twelve_markings():
    """The sibling's MODEL of 11:19: the 120 relabellings of the marked square take 12 values, ten times each."""
    from sympy.polys.matrices import DomainMatrix
    Pc, R5, U, K, Qf, Pm, L = _marked()
    seen = Counter()
    for p in itertools.permutations(range(5)):
        h = compound2(sp.Matrix(5, 5, lambda r, c: int(r == p[c])))
        seen[tuple(h * L * L.T * h.T)] += 1
    C = [sp.Matrix(10, 10, list(k)) for k in seen]
    x = sp.symbols("x")
    poly = lambda M: sp.expand(sum(sp.Rational(int(c.numerator), int(c.denominator)) * x ** k for k, c in
                                   enumerate(reversed(DomainMatrix.from_Matrix(M).to_field().charpoly()))))
    kinds = {sp.expand(x ** 6 * (x - 1) ** 4): "a marking and its doubling: 1, 1, 1, 1",
             sp.expand(x ** 4 * (x - sp.Rational(1, 5)) ** 2 * (x - sp.Rational(4, 5)) ** 2 * (x - 1) ** 2): "1/5, 4/5, 1",
             sp.expand(x ** 4 * (x - sp.Rational(2, 5)) ** 2 * (x ** 2 - sp.Rational(6, 5) * x + sp.Rational(4, 25))
                       * (x ** 2 - 2 * x + sp.Rational(4, 5))): "(3 -+ sqrt5)/5, 2/5, (5 -+ sqrt5)/5"}
    pairs = Counter(kinds.get(poly(C[a] + C[b])) for a, b in itertools.combinations(range(12), 2))
    r5 = sp.sqrt(5)
    C50 = [np.array((50 * c).tolist(), dtype=np.int64) for c in C]
    P5 = np.array((5 * Pc).tolist(), dtype=np.int64)
    iso = [S for k in range(1, 13) for S in itertools.combinations(range(12), k)
           if (lambda M: np.array_equal(30 * M, np.trace(M) * P5))(sum(C50[i] for i in S))]
    return {
        "the 120 relabellings of the marked square take 12 values, ten times each (one per cyclic order up to "
        "reversal), and the twelve sum to 4 P_cycle, so a cycle vector is a quarter of its twelve labelled readings":
            len(C) == 12 and set(seen.values()) == {10} and sum(C, sp.zeros(10)) == 4 * Pc
            and all(sp.Matrix(50 * c).is_symmetric() and all(v.is_integer for v in 50 * c) for c in C),
        "of the 66 pairs, 6 (a marking and its doubling) sum to a moving projector, eigenvalues 1, 1, 1, 1; 30 have "
        "eigenvalues 1/5, 1/5, 4/5, 4/5, 1, 1 (condition 5) and 30 have (3 -+ sqrt5)/5, 2/5, 2/5, (5 -+ sqrt5)/5 "
        "(condition 5 + 2 sqrt5)": pairs == Counter({"a marking and its doubling: 1, 1, 1, 1": 6, "1/5, 4/5, 1": 30,
                                                       "(3 -+ sqrt5)/5, 2/5, (5 -+ sqrt5)/5": 30})
            and sp.expand(sp.radsimp((5 + r5) / (3 - r5) - (5 + 2 * r5))) == 0,
        "the twelve centred squares C - P_cycle/3 have rank 11, and of the 4095 equal-weight sums only the sum of all "
        "twelve is isotropic": sp.Matrix([list(c - Pc / 3) for c in C]).rank() == 11 and iso == [tuple(range(12))],
    }


def _isotropic(d):
    """The c with sum over the roots of (rho.k)^d = c |k|^d identically, monomial by monomial; None if there is none."""
    R2 = assignment.roots10() // 5
    found = set()
    for combo in itertools.combinations_with_replacement(range(8), d):
        a = np.bincount(combo, minlength=8)
        s = Fraction(int(np.prod(R2 ** a, axis=1).sum()) * factorial(d),
                     int(np.prod([factorial(int(v)) for v in a])) * 2 ** d)
        if (a % 2).any():
            if s:
                return None
        else:
            found.add(s * int(np.prod([factorial(int(v) // 2) for v in a])) / factorial(d // 2))
    return found.pop() if len(found) == 1 else None


@functools.lru_cache(maxsize=None)
def _golden_channels():
    """The Golden port's four channels at low energy, from its ten root sites: the distance kernels S_c, the channel
    weights, the monopole, dipole and quadrupole data, and the densities rho[channel][j], the coefficient of E^j in
    units of C = 1/(1536 pi^4 30^4), exact through relative order E^2."""
    site, sign = _golden_sites()
    Pc, R5, U, K, Qf, Pm, L = _marked()
    X = [sp.Matrix([sp.Rational(int(c), 10) for c in s]) for s in site]
    d2 = sp.Matrix(10, 10, lambda e, f: ((X[e] - X[f]).T * (X[e] - X[f]))[0])
    cs = sorted(set(d2))
    S = {c: sp.Matrix(10, 10, lambda e, f: sign[e] * sign[f] * int(d2[e, f] == c)) for c in cs}
    v = Qf * sp.Matrix(sign)
    Pp = v * v.T / (v.T * v)[0]
    Pn = Qf - Pp
    r5 = sp.sqrt(5)
    w = {"plus": [(Pp * S[c]).trace() for c in cs], "minus": [(Pn * S[c]).trace() for c in cs]}
    for nm, s in (("phi", 1), ("psi", -1)):
        w[nm] = [((Pm * S[c]).trace() + s * (Pm * K * S[c]).trace() / r5) / 4 for c in cs]
    Dp = sp.Matrix.hstack(*[sign[e] * X[e] for e in range(10)])
    mono = sp.Matrix([sign])
    Q2 = sp.Matrix(10, 10, lambda e, f: sign[e] * sign[f] * (X[e].T * X[f])[0] ** 2)
    u, E, t = sp.symbols("u E t", positive=True)
    eps = 30 * u - sp.Rational(3, 2) * u ** 2 + sp.Rational(1, 24) * u ** 3
    uE = E / 30
    for _ in range(5):
        uE = sp.expand(E / 30 + (sp.Rational(3, 2) * uE ** 2 - uE ** 3 / 24) / 30)
        uE = sum(uE.coeff(E, j) * E ** j for j in range(1, 6))
    Phi = lambda z: sum((-z / 4) ** m / (sp.factorial(m) * sp.rf(4, m)) for m in range(6))
    trunc = lambda p, x, n: sum(sp.expand(p).coeff(x, j) * x ** j for j in range(n + 1))
    inv = sp.series(1 / sp.diff(eps, u), u, 0, 6).removeO()
    upow = [sp.Integer(1)]
    for _ in range(7):
        upow.append(trunc(upow[-1] * uE, E, 7))
    rho = {}
    for nm, wt in w.items():
        ser = trunc(30 ** 4 * sum(a * Phi(c * u) for a, c in zip(wt, cs)) * u ** 3 * inv, u, 7)
        ser = sp.expand(sum(ser.coeff(u, j) * upow[j] for j in range(3, 8)))
        rho[nm] = [sp.expand(sp.radsimp(ser.coeff(E, j))) for j in range(8)]
    return dict(cs=cs, S=S, Pp=Pp, Pn=Pn, w=w, Dp=Dp, mono=mono, Q2=Q2, rho=rho, U=U, Pm=Pm)


def golden_infrared():
    """The Golden port's four channels at low energy, from its ten root sites (the hub, 11:18), in units of
    C = 1/(1536 pi^4 30^4). The roots are a 7-design, so eps = 30u - 3u^2/2 + u^3/24 + O(u^4) with u = |k|^2 is
    isotropic; the series below are exact through relative order E^2, where the anisotropic degree-8 term cannot reach."""
    ch = _golden_channels()
    cs, S, Pp, Pn, Dp, mono, Q2, rho, U, Pm = (ch[k] for k in ("cs", "S", "Pp", "Pn", "Dp", "mono", "Q2", "rho", "U", "Pm"))
    r5 = sp.sqrt(5)
    pick = lambda f, j: sp.expand(sp.radsimp(f(*(rho[n][j] for n in ("plus", "minus", "phi", "psi")))))
    near = lambda p, n, f, s: ((17 + 5 * r5) * f + (17 - 5 * r5) * s) / 45
    far = lambda p, n, f, s: ((13 + r5) * f + (13 - r5) * s) / 45
    marked = lambda p, n, f, s: (2 * (5 + r5) * f + 2 * (5 - r5) * s) / 30
    twirl = lambda p, n, f, s: (p + n + 2 * f + 2 * s) / 9
    zero = lambda a: sp.expand(sp.radsimp(a)) == 0
    tw = [pick(twirl, j) for j in (3, 4, 5)]
    return {
        "E8's roots are a 7-design: sum (rho.k)^d = 60, 36, 30 times |k|^d for d = 2, 4, 6, exactly, so the symbol is "
        "eps = 30u - 3u^2/2 + u^3/24 + O(u^4) in every direction": [_isotropic(d) for d in (2, 4, 6)] == [60, 36, 30],
        "the response of the ten sites splits into four scalar channels at every energy: the five distance kernels "
        "commute with the five-cycle and do not mix the plus and minus lines of the fixed plane":
            all(U * S[c] == S[c] * U and (Pp * S[c] * Pn).is_zero_matrix for c in cs),
        "the plus line carries monopole square 10 and no dipole, every unit moving cycle has dipole square 1, and the "
        "minus line has neither monopole nor dipole and a traceless quadrupole with tr Q^2 = 4":
            (Pp * mono.T * mono).trace() == 10 and (Pp * Dp.T * Dp).trace() == 0 and Pm * Dp.T * Dp * Pm == Pm
            and (Pn * mono.T * mono).trace() == 0 and (Pn * Dp.T * Dp).trace() == 0 and (Pn * Q2).trace() == 4,
        "the densities are plus 10 E^3 (1 - E^2/1080000), Golden (E^4/240)(1 + (1/100 -+ sqrt5/3000) E) for K = +-sqrt5 "
        "and minus E^5/36000, with heat tails 60 t^-4, t^-5/10 and t^-6/300":
            rho["plus"][3:6] == [10, 0, sp.Rational(-1, 108000)] and rho["minus"][5] == sp.Rational(1, 36000)
            and rho["phi"][4] == rho["psi"][4] == sp.Rational(1, 240)
            and zero(rho["phi"][5] - (sp.Rational(1, 100) - r5 / 3000) / 240)
            and zero(rho["psi"][5] - (sp.Rational(1, 100) + r5 / 3000) / 240)
            and (10 * 6, sp.Rational(24, 240), sp.Rational(120, 36000)) == (60, sp.Rational(1, 10), sp.Rational(1, 300)),
        "so the near/far ratio is (17/13)(1 - 2E/5525), the marked ensemble (E^4/360)(1 + 29E/3000), and the S5 twirl "
        "(rho_plus + rho_minus + 2 rho_phi + 2 rho_psi)/9 = (10/9) E^3 + E^4/540 + E^5/48600, with heat tail "
        "(20/3) t^-4 (1 + 1/(150 t) + 1/(2700 t^2)): the hub's inherited coefficients, now computed":
            pick(near, 4) / pick(far, 4) == sp.Rational(17, 13)
            and zero((pick(near, 5) * pick(far, 4) - pick(near, 4) * pick(far, 5)) / pick(far, 4) ** 2
                     + sp.Rational(17, 13) * sp.Rational(2, 5525))
            and pick(marked, 4) == sp.Rational(1, 360) and zero(pick(marked, 5) - sp.Rational(29, 3000 * 360))
            and tw == [sp.Rational(10, 9), sp.Rational(1, 540), sp.Rational(1, 48600)]
            and [tw[k] * factorial(k + 3) / (tw[0] * 6) for k in range(3)] == [1, sp.Rational(1, 150), sp.Rational(1, 2700)],
    }


def _words():
    """The fifteen words of the dihedral closure of 088, 086 and 980, orbit by orbit, with rotation C and reversal R."""
    rot, rev = (lambda w: w[1:] + w[:1]), (lambda w: w[::-1])
    orbit = lambda w: sorted({y for x in (w, rev(w)) for y in (x, rot(x), rot(rot(x)))})
    words = [w for w0 in ("088", "086", "980") for w in orbit(w0)]
    idx = {w: i for i, w in enumerate(words)}
    perm = lambda f: sp.Matrix(15, 15, lambda r, c: int(r == idx[f(words[c])]))
    return words, perm(rot), perm(rev)


def _duads():
    """Lambda^2 R^6, the oriented duads of six points, with c: i -> i + 2 and the reflection r: i -> -i taken with a
    sign, and the signed basis vector e_a ^ e_b."""
    di = {d: i for i, d in enumerate(itertools.combinations(range(6), 2))}

    def wedge(f, s=1):
        M = sp.zeros(15, 15)
        for (a, b), i in di.items():
            x, y = f(a), f(b)
            M[di[(min(x, y), max(x, y))], i] = s * (1 if x < y else -1)
        return M
    e = lambda a, b: sp.eye(15)[:, di[(min(a, b), max(a, b))]] * (1 if a < b else -1)
    return wedge(lambda i: (i + 2) % 6), wedge(lambda i: -i % 6, -1), e


def word_duads():
    """The hub's word-to-duad join (11:18), rebuilt here with its own A and B."""
    from sympy.polys.matrices import DomainMatrix
    words, C, R = _words()
    Ct, Rt, e = _duads()
    I = sp.eye(15)
    G = [(I, I), (C, Ct), (C * C, Ct * Ct), (R, Rt), (R * C, Rt * Ct), (R * C * C, Rt * Ct * Ct)]

    def equivariant(w, v):
        M = sp.zeros(15, 15)
        for gs, gt in G:
            M[:, list(gs[:, words.index(w)]).index(1)] = gt * v
        return M
    A = equivariant("808", e(2, 4)) + equivariant("980", e(0, 1))
    Bm = equivariant("086", e(5, 1) + e(0, 3))
    P086 = sp.diag(*[int(sorted(w) == sorted("086")) for w in words])
    O, TZ = A + Bm / sp.sqrt(2), A + Bm
    Ft = sum((gt for _, gt in G), sp.zeros(15)) / 6
    src = sp.Matrix.hstack(*[sp.Matrix([int(sorted(w) == sorted(k)) for w in words]) for k in ("088", "086", "980")])
    tgt = sp.Matrix.hstack(3 * Ft * e(0, 2), 3 * Ft * e(1, 3), 6 * Ft * e(0, 1))
    f2 = lambda M: DomainMatrix.from_Matrix(M).convert_to(sp.GF(2)).rank()
    s6 = lambda d, k: tuple(sorted(((d[0] + k) % 6, (d[1] + k) % 6)))
    duads = list(itertools.combinations(range(6), 2))
    hexo = {frozenset(s6(d, k) for k in range(6)) for d in duads}
    digits = sp.Matrix([[0, 8, 8], [8, 8, 0], [0, 8, 6], [9, 8, 0]])
    return {
        "the 15 words of 088, 086 and 980 fall in orbits of 3, 6 and 6 under rotation C and reversal R, with C^3 = R^2 "
        "= I and RCR = C^2; on Lambda^2 R^6, c: i -> i + 2 and r: i -> -i with the reflection's sign twisted satisfy the "
        "same relations, and both modules have traces (15, 0, 1), while the untwisted duads have reflection trace 3":
            [len({x for x in words if sorted(x) == sorted(k)}) for k in ("088", "086", "980")] == [3, 6, 6]
            and C ** 3 == I and R ** 2 == I and R * C * R == C ** 2 and Ct ** 3 == I and Rt ** 2 == I
            and Rt * Ct * Rt == Ct ** 2 and (C.trace(), R.trace(), Ct.trace(), Rt.trace()) == (0, 1, 0, 1)
            and Rt.applyfunc(abs).trace() == 3,
        "A sends 088 to the oriented triangle 0-2-4 and 980 to the six adjacent pairs, B sends 086 into the triangle "
        "1-3-5 and the diameters, symmetric and antisymmetric; A^T A = I - P086, B^T B = 2 P086, A^T B = 0, both "
        "intertwine, and O = A + B/sqrt2 is an exact equivariant isometry over Q(sqrt2)":
            A.T * A == I - P086 and Bm.T * Bm == 2 * P086 and (A.T * Bm).is_zero_matrix
            and Ct * A == A * C and Rt * A == A * R and Ct * Bm == Bm * C and Rt * Bm == Bm * R
            and (O.T * O).applyfunc(sp.radsimp) == I,
        "no rational isometry exists: the fixed spaces have Grams diag(3, 6, 6) and diag(3, 3, 6), of determinants 108 "
        "and 54, whose ratio 2 is not a rational square":
            src.T * src == sp.diag(3, 6, 6) and Ft.rank() == 3 and Ft * tgt == tgt and tgt.T * tgt == sp.diag(3, 3, 6)
            and (Ft * e(0, 3)).is_zero_matrix and not sp.sqrt(sp.Rational(108, 54)).is_rational,
        "the integral T_Z = A + B has T_Z^T T_Z = I + P086, determinant 8 and Smith form 1^12 2^3 (index 8), and no "
        "integral intertwiner is unimodular: the mod-2 coinvariants have dimensions 3 and 4":
            TZ.T * TZ == I + P086 and abs(TZ.det()) == 8
            and [smith_normal_form(TZ)[i, i] for i in range(15)] == [1] * 12 + [2] * 3
            and (15 - f2(sp.Matrix.hstack(C - I, R - I)), 15 - f2(sp.Matrix.hstack(Ct - I, Rt - I))) == (3, 4),
        "a six-cycle splits the 15 duads into 6 adjacent pairs, 6 at distance two and 3 diameters, each kept by the "
        "reflection, the six-orbits splitting under c into even and odd triangles; the digit rows 088, 880, 086, 980 "
        "have Smith form 1, 2, 8 (index 16) and the primitive relation (3, 9, -4, -8)":
            sorted(len(o) for o in hexo) == [3, 6, 6]
            and all({tuple(sorted((-a % 6, -b % 6))) for a, b in o} == set(o) for o in hexo)
            and all(len({frozenset(s6(d, k) for k in (0, 2, 4)) for d in o}) == 2 for o in hexo if len(o) == 6)
            and [smith_normal_form(digits)[i, i] for i in range(3)] == [1, 2, 8]
            and (sp.Matrix([[3, 9, -4, -8]]) * digits).is_zero_matrix and gcd(3, 9, 4, 8) == 1,
    }


def words_c5():
    """J7's missing Golden action (the hub, 11:18): no rational C5 commutes with D3 on 1 + 3 std; on 1 + 4 std one does,
    and it is A4's Coxeter element."""
    x = sp.symbols("x")
    words, C, R = _words()
    Cs, Rs = sp.Matrix([[0, -1], [1, -1]]), sp.Matrix([[0, 1], [1, 0]])
    comp = sp.Matrix(4, 4, lambda i, j: int(i == j + 1) - int(j == 3))
    alpha = sp.Matrix(5, 4, lambda r, i: int(r == i) - int(r == i + 1))
    R5 = sp.Matrix(5, 5, lambda r, c: int(r == (c + 1) % 5))
    C9, R9 = sp.diag(1, sp.kronecker_product(Cs, sp.eye(4))), sp.diag(1, sp.kronecker_product(Rs, sp.eye(4)))
    Ub = sp.kronecker_product(sp.eye(2), comp)
    U9 = sp.diag(1, Ub)
    Xb = -(Ub + Ub.inv())
    chi = (15, C.trace(), R.trace())
    mult = ((chi[0] + 2 * chi[1] + 3 * chi[2]) // 6, (chi[0] + 2 * chi[1] - 3 * chi[2]) // 6, (2 * chi[0] - 2 * chi[1]) // 6)
    least = min(a + b + 2 * c for a in range(1, 9) for b in range(9) for c in range(3, 9) if max(a, b, c) >= 4)
    return {
        "the words are 3 trivial + 2 sign + 5 standard, room for J7's 1 + 3 std; D3 on 1 + 3 std has commutant Q + M3(Q), "
        "and a rational C5 other than I needs Phi_5, irreducible of degree 4, in a block of dimension 4 or more: none "
        "here, and the least extension with one is 9 = 1 + 4 std": mult == (3, 2, 5)
            and sp.Poly(x ** 4 + x ** 3 + x ** 2 + x + 1, x).is_irreducible and least == 9,
        "there U9 = 1 + I2 x companion(Phi_5) has U9^5 = I, U9 != I, and commutes with C9 = 1 + C_std x I4 and R9 = 1 + "
        "R_std x I4, a D3; the companion is A4's Coxeter element, the five-cycle, on the simple roots e_i - e_(i+1)":
            U9 ** 5 == sp.eye(9) and U9 != sp.eye(9) and U9 * C9 == C9 * U9 and U9 * R9 == R9 * U9
            and C9 ** 3 == sp.eye(9) and R9 ** 2 == sp.eye(9) and R9 * C9 * R9 == C9 ** 2 and R5 * alpha == alpha * comp
            and comp.charpoly(x).as_expr() == x ** 4 + x ** 3 + x ** 2 + x + 1,
        "on the extension's eight moving directions -(U9 + U9^-1) satisfies X^2 = X + I: the golden companion acts there":
            Xb * Xb == Xb + sp.eye(8),
    }


def _two_ports():
    """The hub's clique port T_C and the Golden port's F on their 14 shared root sites."""
    site, sign = _golden_sites()
    S, T_ = assignment.SITE, assignment.TWIN
    clique = [S[0] - S[i] for i in range(1, 5)] + [S[0] - T_[0] - T_[1], S[0] - T_[0] - T_[2]]
    sites = []
    for t in clique + site:
        if not any(np.array_equal(t, q) for q in sites):
            sites.append(t)
    where = lambda t: next(k for k, q in enumerate(sites) if np.array_equal(t, q))
    TC = sp.zeros(len(sites), 6)
    for k, t in enumerate(clique):
        TC[where(t), k] = 1
    Fm = sp.zeros(len(sites), 10)
    for e, (t, g) in enumerate(zip(site, sign)):
        Fm[where(t), e] = g
    return clique, sites, TC, Fm


def notes_1119():
    """The sibling's MODEL of 10:42-11:19 and the hub's text of 11:18: the remaining exact items."""
    R = assignment.roots10()
    A = ((R @ R.T) == 100).astype(np.int64)
    walks, M = [], np.eye(240, dtype=np.int64)
    for n in range(6):
        walks.append(int(np.trace(M)) // 240)
        M = M @ A
    spec = [(56, 1), (28, 8), (8, 35), (-2, 112), (-4, 84)]
    cw = np.cos(R / 10 @ (np.array([28, 28, 6, 2, 1, 0, 0, 0]) / 10))
    orders = Counter(Permutation(list(p)).order() for p in itertools.permutations(range(5)))
    clique, sites, TC, Fm = _two_ports()
    cyc = np.linalg.qr(np.array(sp.Matrix.hstack(*sp.Matrix(carrier.signed_incidence()).nullspace()), dtype=float))[0]
    sv = np.linalg.svd(np.hstack([np.array(TC, dtype=float), np.array(Fm, dtype=float) @ cyc]), compute_uv=False)
    Pc, R5, U, K, Qf, Pm, L = _marked()
    Xs = 2 * sp.eye(10) + U + U.T
    x = sp.symbols("x")
    r5 = sp.sqrt(5)
    t = sp.Matrix([0, 0, 0, sp.Rational(1, 2), sp.Rational(-1, 2)])
    h = sp.Matrix([sp.Rational(-1, 3)] * 3 + [sp.Rational(1, 2)] * 2)
    return {
        "the root graph's closed walks are 1, 0, 56, 1512, 62160 and 2872800 per root, from its spectrum and from the "
        "powers of its adjacency matrix": walks == [1, 0, 56, 1512, 62160, 2872800]
            and walks == [sum(m * lam ** n for lam, m in spec) // 240 for n in range(6)],
        "at the collar witness the 240 cosines sum to 19.3654682687, so the figure 220.6349198210, from 19.3650801790, "
        "is off by 3.9e-4 and wrong": np.isclose(cw.sum(), 19.3654682687, atol=1e-9)
            and abs(cw.sum() - 19.3650801790) > 3e-4 and np.isclose(240 - 19.3650801790, 220.6349198210, atol=1e-9),
        "S5 has 1, 25, 20, 30, 24 and 20 elements of orders 1 to 6, so a map from the cyclic clock fibre 36Z/4320Z = Z/120 "
        "hits at most 6 of them, and Z/4320 is not Z/36 x Z/120 (exponent 360)":
            orders == Counter({1: 1, 2: 25, 3: 20, 4: 30, 5: 24, 6: 20}) and max(orders) == 6 and 4320 // gcd(36, 4320) == 120
            and lcm(36, 120) == 360,
        "the clique and Golden ports' joint window has twelve singular values with extremes sqrt(1 +- 2/sqrt5), so its "
        "condition number is 2 + sqrt5, from the angle 4/5 alone": len(sv[sv > 1e-9]) == 12
            and np.isclose(sv.max() / sv[sv > 1e-9].min(), 2 + 5 ** 0.5)
            and sp.expand(sp.radsimp((2 + r5) ** 2 * (1 - 2 / r5) - (1 + 2 / r5))) == 0,
        "on the moving cycles 2I + U + U^T has eigenvalues (3 +- sqrt5)/2 > 0; its positive root S_phi obeys "
        "S_phi^4 - 3 S_phi^2 + I = 0, and K = 2 S_phi^2 - 3I": ((Xs * Xs - 3 * Xs + sp.eye(10)) * Pm).is_zero_matrix
            and sp.expand((Xs * Pm).charpoly(x).as_expr() - x ** 6 * (x ** 2 - 3 * x + 1) ** 2) == 0
            and K == 2 * Xs - 3 * sp.eye(10),
        "t = (0, 0, 0, 1/2, -1/2) and h + t, h = (-1/3, -1/3, -1/3, 1/2, 1/2), have squares 1/2 and 4/3, so the frame "
        "60 I gives traces 30 and 80: the 3/8 is the ratio of the lengths": (t.T * t)[0] == sp.Rational(1, 2)
            and ((h + t).T * (h + t))[0] == sp.Rational(4, 3) and 60 * (t.T * t)[0] == 30 and 60 * ((h + t).T * (h + t))[0] == 80,
    }


def notes_1119_arithmetic():
    """The 10:42-11:19 model's circle arithmetic, and the hub's small counts, as arithmetic."""
    N = 4320
    widths = (2, 3, 4, 6, 7, 8, 13)
    return {
        "4320 = 36 x 120 = 15 x 36 x 8, 864 = 24 x 36 and 9361 = 260 x 36 + 1; 1728, 1296, 864 and 432 are 48, 36, 24 and "
        "12 copies of 36; twelve signs of 30, twelve times, make 4320; four 27-steps make 108":
            36 * 120 == N == 15 * 36 * 8 and 864 == 24 * 36 and 9361 == 260 * 36 + 1
            and [b // 36 for b in (1728, 1296, 864, 432)] == [48, 36, 24, 12] and 12 * 30 * 12 == N and 4 * 27 == 108,
        "the widths 2, 3, 4, 6, 7, 8 and 13 times 36 land at 72, 108, 144, 216, 252, 288 and 468, of orders 60, 40, 30, "
        "20, 120, 15 and 120; 6 + 15 + 15 = 36, 6 + 15 + 10 = 31 and 2 x 72 x 5 = 720":
            [k * 36 for k in widths] == [72, 108, 144, 216, 252, 288, 468]
            and [N // gcd(k * 36, N) for k in widths] == [60, 40, 30, 20, 120, 15, 120]
            and 6 + 15 + 15 == 36 and 6 + 15 + 10 == 31 and 2 * 72 * 5 == 720,
        "the Return residues diag(0, 0, 3, 3, 3, 3, 0) and diag(0, 0, 3, 3, 3, 3, 2) have ranks 4 and 5; two 7D "
        "displays sharing a scalar make 13 = 7 + 7 - 1, six more than 7; a six-channel port and three readings have "
        "rank at most 9 < 10; (11 + 1)(5 + 2) = 84 < 195": sp.diag(0, 0, 3, 3, 3, 3, 0).rank() == 4
            and sp.diag(0, 0, 3, 3, 3, 3, 2).rank() == 5 and 7 + 7 - 1 == 13 == 7 + 6 and 6 + 3 < 10
            and (11 + 1) * (5 + 2) == 84 < 195,
    }



def _hodge():
    """The Hodge star of the cycles, J_H = Curl/sqrt5 (layer 17's light operator), and the Golden port's four channel
    projectors: the fixed lines f+ (the port's monopole, mean 239) and f- (mean 241) and the Golden doublets."""
    Pc, R5, U, K, Qf, Pm, L = _marked()
    r5 = sp.sqrt(5)
    J = sp.Matrix(waves.complex_ops()[3]) / r5
    ch = _golden_channels()
    P = {"+": ch["Pp"], "-": ch["Pn"], "phi": Pm * (sp.eye(10) + K / r5) / 2, "psi": Pm * (sp.eye(10) - K / r5) / 2}
    return J, P, Pc, U, K, Qf, Pm, L


def _contexts():
    """The twelve marked squares h L L^T h^T, each with the parity of the permutations that give it."""
    Pc, R5, U, K, Qf, Pm, L = _marked()
    out = {}
    for p in itertools.permutations(range(5)):
        h = compound2(sp.Matrix(5, 5, lambda r, c: int(r == p[c])))
        out.setdefault(tuple(h * L * L.T * h.T), Permutation(list(p)).signature())
    return [(sp.Matrix(10, 10, list(k)), s) for k, s in out.items()]


def _zero(a):
    """Exact zero test for scalars and matrices over Q(sqrt5, sqrt2, sqrt3)."""
    f = lambda z: sp.expand(sp.radsimp(z)) == 0
    return all(f(z) for z in a) if hasattr(a, "shape") else f(a)


def hodge_contexts():
    """The hub's text (11:58): the twelve contexts over the six Sylow views, and the Hodge star they reconstruct."""
    J, P, Pc, U, K, Qf, Pm, L = _hodge()
    r5 = sp.sqrt(5)
    lift = lambda p: compound2(sp.Matrix(5, 5, lambda r, c: int(r == p[c])))
    perms = list(itertools.permutations(range(5)))
    ctx = _contexts()
    Se = sum((C for C, s in ctx if s == 1), sp.zeros(10))
    So = sum((C for C, s in ctx if s == -1), sp.zeros(10))
    sylow = {frozenset(tuple((Permutation(list(p)) ** k).array_form) for k in range(5)) for p in perms
             if Permutation(list(p)).order() == 5}
    over = Counter()
    for H in sylow:
        gen = next(h for h in H if Permutation(list(h)).order() == 5)
        over[tuple(sorted(s for C, s in ctx if lift(gen) * C * lift(gen).T == C))] += 1
    stab = [p for p in perms if lift(p) * L * L.T * lift(p).T == L * L.T]
    pairs = Counter()
    for (A, s), (B, t) in itertools.combinations(ctx, 2):
        pairs[((A + B) ** 2 == A + B, s == t, (A * B).trace())] += 1
    x = sp.symbols("x")
    d = lift((0, 2, 4, 1, 3))
    return {
        "J_H = Curl/sqrt5, layer 17's light operator, is symmetric with J_H^2 = P_cycle, and every permutation acts on it "
        "through its sign, U J_H U^T = sgn J_H; its eigenprojectors (P_cycle +- J_H)/2 have rank 3":
            J == J.T and _zero(J * J - Pc) and all(lift(p) * J * lift(p).T == Permutation(list(p)).signature() * J for p in perms)
            and all(((Pc + s * J) / 2).applyfunc(sp.radsimp).rank() == 3 for s in (1, -1)),
        "a context is fixed by 10 permutations (a D10), so there are 12, two over each of the six Sylow five-cycle groups, "
        "six even and six odd; the even sextet sums to 2 P_cycle - (2/sqrt5) J_H and the odd one to 2 P_cycle + "
        "(2/sqrt5) J_H, so their difference is (4/5) Curl": len(stab) == 10 and len(ctx) == 12 and len(sylow) == 6
            and Counter(s for _, s in ctx) == Counter({1: 6, -1: 6}) and over == Counter({(-1, 1): 6})
            and _zero(Se - 2 * Pc + 2 * J / r5) and _zero(So - 2 * Pc - 2 * J / r5) and _zero(So - Se - 4 * r5 * J / 5),
        "each sextet has eigenvalues 2 -+ 2/sqrt5 three times (condition phi^2), and S_even S_odd = (16/5) P_cycle, so on "
        "the cycles S_even^-1 = (5/16) S_odd and S_even = (16/5) S_odd^-1":
            _zero((Se * Pc).charpoly(x).as_expr() - x ** 4 * (x ** 2 - 4 * x + sp.Rational(16, 5)) ** 3)
            and _zero(Se * So - sp.Rational(16, 5) * Pc) and _zero((2 + 2 / r5) / (2 - 2 / r5) - (3 + r5) / 2),
        "J_H is -1 on the Golden doublet K = sqrt5 and +1 on K = -sqrt5, so K P_cycle = 5 P_fix - sqrt5 J_H P_moving; the "
        "doubling i -> 2i is odd, negates J_H, swaps the two sextets and turns U into U^2":
            _zero(J * P["phi"] + P["phi"]) and _zero(J * P["psi"] - P["psi"]) and _zero(K * Pc - 5 * Qf + r5 * J * Pm)
            and d * J * d.T == -J and _zero(d * Se * d.T - So) and d * U * d.T == U ** 2,
        "of the 66 pairs of contexts the 6 within one view sum to a projector (overlap tr(C_i C_j) = 4/5); the 30 of "
        "opposite parity across views have overlap 12/25 and the 30 of equal parity 18/25":
            pairs == Counter({(True, False, sp.Rational(4, 5)): 6, (False, False, sp.Rational(12, 25)): 30,
                              (False, True, sp.Rational(18, 25)): 30}),
    }


def context_responses():
    """The hub's text (11:58): four labelled context responses recover the four channels and measure the Hodge defect."""
    J, P, Pc, U, K, Qf, Pm, L = _hodge()
    r5 = sp.sqrt(5)
    u = 1 / r5
    ex = lambda z: sp.expand(sp.radsimp(z))
    ctx = _contexts()
    keys = ("+", "-", "phi", "psi")
    sig = Counter(tuple(ex((C * P[k]).trace()) for k in keys) for C, _ in ctx)
    M4 = sp.Matrix([[0, 0, 1 + u, 1 - u], [0, 0, 1 - u, 1 + u],
                    [sp.Rational(8, 25), sp.Rational(12, 25), sp.Rational(3, 5) * (1 - u), sp.Rational(3, 5) * (1 + u)],
                    [sp.Rational(12, 25), sp.Rational(8, 25), sp.Rational(3, 5) * (1 + u), sp.Rational(3, 5) * (1 - u)]])
    inverse = sp.Matrix([[-sp.Rational(9, 4), sp.Rational(3, 2), -sp.Rational(5, 2), sp.Rational(15, 4)],
                         [sp.Rational(3, 2), -sp.Rational(9, 4), sp.Rational(15, 4), -sp.Rational(5, 2)],
                         [(1 + r5) / 4, (1 - r5) / 4, 0, 0], [(1 - r5) / 4, (1 + r5) / 4, 0, 0]])
    g = sp.symbols("g_p g_m g_f g_s")
    R = M4 * sp.Matrix(g)
    G = sum((gi * P[k] for gi, k in zip(g, keys)), sp.zeros(10))
    comm = J * G - G * J
    Se = sum((C for C, s in ctx if s == 1), sp.zeros(10))
    So = sum((C for C, s in ctx if s == -1), sp.zeros(10))
    Rn = ((17 + 5 * r5) * g[2] + (17 - 5 * r5) * g[3]) / 45
    Rf = ((13 + r5) * g[2] + (13 - r5) * g[3]) / 45
    chi = sp.symbols("chi")
    ratio = (1 - chi / r5) / (1 + chi / r5)
    eta = Pm + J * Qf
    rho = _golden_channels()["rho"]
    name = {"+": "plus", "-": "minus", "phi": "phi", "psi": "psi"}
    low = [ex(sum(M4[i, j] * rho[name[k]][n] for j, k in enumerate(keys))) for i, n in ((0, 4), (1, 4), (2, 3), (3, 3))]
    parity = [ex(sum((S_ * P[k]).trace() * rho[name[k]][3] for k in keys)) for S_ in (Se, So)]
    return {
        "the twelve contexts give four response signatures on (rho_+, rho_-, rho_phi, rho_psi), with u = 1/sqrt5: R_A = "
        "(0, 0, 1 + u, 1 - u) and R_B = (0, 0, 1 - u, 1 + u) once each, R_C = (8/25, 12/25, (3/5)(1 - u), (3/5)(1 + u)) "
        "and R_D = (12/25, 8/25, (3/5)(1 + u), (3/5)(1 - u)) five times each, with determinant -64 sqrt5/625":
            sig == Counter({tuple(ex(z) for z in M4.row(i)): m for i, m in enumerate((1, 1, 5, 5))})
            and _zero(M4.det() + 64 * r5 / 625),
        "four labelled responses recover the four channels: rho_phi,psi = [R_A + R_B +- sqrt5 (R_A - R_B)]/4, rho_+ = "
        "-(5/2) X + (15/4) Y and rho_- = (15/4) X - (5/2) Y with X = R_C - (3/5) R_B, Y = R_D - (3/5) R_A":
            _zero(M4 * inverse - sp.eye(4)),
        "the defect: for G = sum g_a P_a, ||[J_H, G]||^2 = (8/5)(g_+ - g_-)^2, and g_+ - g_- = (25/4)[R_D - R_C - (3/5)"
        "(R_A - R_B)], so ||[J_H, G]||^2 = (125/2)|R_D - R_C - (3/5)(R_A - R_B)|^2; the port's means 239, 241 and "
        "variances 371, 171 give 32/5 and 64000": _zero((comm.T * comm).trace() - sp.Rational(8, 5) * (g[0] - g[1]) ** 2)
            and _zero(sp.Rational(25, 4) * (R[3] - R[2] - sp.Rational(3, 5) * (R[0] - R[1])) - (g[0] - g[1]))
            and sp.Rational(8, 5) * sp.Rational(25, 4) ** 2 == sp.Rational(125, 2)
            and (sp.Rational(8, 5) * (239 - 241) ** 2, sp.Rational(8, 5) * (371 - 171) ** 2) == (sp.Rational(32, 5), 64000),
        "the Lorentz reference eta = P_moving + J_H P_fix squares to P_cycle with signature (5, 1) and has the same "
        "fixed-plane commutator": _zero(eta * eta - Pc) and ex((eta * Pc).trace()) == 4
            and _zero(((eta * G - G * eta).T * (eta * G - G * eta)).trace() - sp.Rational(8, 5) * (g[0] - g[1]) ** 2),
        "three summaries measure it: D = (R_even - R_odd) - (3/2)(13 R_near - 17 R_far) = (4/5)(g_+ - g_-), so "
        "||[J_H, G]||^2 = (5/2) D^2, and an error eps in each summary moves D by at most 46 eps (47 with the parities "
        "measured apart)": _zero((Se * G).trace() - (So * G).trace() - sp.Rational(3, 2) * (13 * Rn - 17 * Rf)
                                 - sp.Rational(4, 5) * (g[0] - g[1]))
            and 1 + sp.Rational(3, 2) * (13 + 17) == 46 and 2 + sp.Rational(3, 2) * (13 + 17) == 47,
        "for any positive response R_even/R_odd = (1 - chi/sqrt5)/(1 + chi/sqrt5) with chi = tr(J_H R)/tr R in [-1, 1], "
        "so it lies in [phi^-2, phi^2], the ends attained on the Hodge eigenspaces":
            _zero(Se - 2 * Pc + 2 * J / r5) and _zero(ratio.subs(chi, 1) - (3 - r5) / 2) and _zero(ratio.subs(chi, -1) - (3 + r5) / 2),
        "with the computed densities R_A and R_B start at E^4/120 and R_C, R_D at (16/5) E^3 and (24/5) E^3, so R_C/R_D "
        "-> 2/3, while the parity sums give R_even/R_odd -> 3/2 (units 1/(1536 pi^4 30^4))":
            low == [sp.Rational(1, 120), sp.Rational(1, 120), sp.Rational(16, 5), sp.Rational(24, 5)]
            and ex(parity[0] / parity[1]) == sp.Rational(3, 2),
    }


def overlap_hodge():
    """The hub's text (11:58): the two-port Gram, residual whitening, and the overlap's Hodge isotropy."""
    J, P, Pc, U, K, Qf, Pm, L = _hodge()
    clique, sites, TC, Fm = _two_ports()
    X = TC.T * Fm * Pc
    Q = sp.Matrix(sp.BlockMatrix([[sp.eye(6), X], [X.T, Pc]]))
    x = sp.symbols("x")
    CC = X * X.T
    S = sp.eye(6) - CC
    P8 = CC * (CC - sp.Rational(2, 5) * sp.eye(6)) * sp.Rational(25, 8)
    P4 = CC * (CC - sp.Rational(4, 5) * sp.eye(6)) * sp.Rational(-25, 4)
    Sih = sp.eye(6) - P8 - P4 + sp.sqrt(5) * P8 + sp.sqrt(15) / 3 * P4
    F = TC - Fm * Pc * X.T
    N = (J - Pc) * X.T
    Km = sp.Matrix(sp.BlockMatrix([[sp.eye(6), sp.zeros(6, 10)], [N, J]]))
    Hn = _walk_entries()
    site, sign = _golden_sites()
    MG = Pc * sp.Matrix(10, 10, lambda e, f: sign[e] * sign[f] * Hn(site[f] - site[e], 1)) * Pc
    D = J * MG * J - MG
    signed = [sp.diag(*s) * sp.Matrix(6, 6, lambda i, j: int(j == p[i]))
              for p, s in zip(itertools.islice(itertools.permutations(range(6)), 0, 720, 97), itertools.product((1, -1), repeat=6))]
    r5 = sp.sqrt(5)
    return {
        "the joint Gram Q = [[I, C], [C*, I]] has eigenvalues 1 +- 2/sqrt5, 1 +- sqrt(2/5) and 1 eight times on the "
        "12-dimensional range, so det 3/25 there and condition 9 + 4 sqrt5 (the port map's is its root, 2 + sqrt5); "
        "tr(P_C P_G) = 6/5 and the squared chordal distance is 6 - 6/5 = 24/5":
            _zero(Q.charpoly(x).as_expr() - x ** 4 * (x - 1) ** 8 * ((x - 1) ** 2 - sp.Rational(4, 5)) * ((x - 1) ** 2 - sp.Rational(2, 5)))
            and sp.Rational(1, 5) * sp.Rational(3, 5) == sp.Rational(3, 25)
            and _zero((1 + 2 / r5) / (1 - 2 / r5) - (9 + 4 * r5)) and (X.T * X).trace() == sp.Rational(6, 5),
        "residualizing the clique against the Golden port, F = T_C - T_G C* has F*F = S = I - CC* (eigenvalues 1/5, 3/5 "
        "and 1 four times) and F*T_G = 0; S^-1 = I + 4 P_8 + (2/3) P_4 with rational projectors, and S^-1/2 = I - P_8 - "
        "P_4 + sqrt5 P_8 + (sqrt15/3) P_4 squares to it": F.T * F == S and (F.T * Fm * Pc).is_zero_matrix
            and S.eigenvals() == {sp.Rational(1, 5): 1, sp.Rational(3, 5): 1, 1: 4}
            and P8 * P8 == P8 and P4 * P4 == P4 and S * (sp.eye(6) + 4 * P8 + sp.Rational(2, 3) * P4) == sp.eye(6)
            and _zero(Sih * Sih - sp.eye(6) - 4 * P8 - sp.Rational(2, 3) * P4),
        "the overlap is Hodge-isotropic: C J_H C* = 0 and ||[J_H, C*C]||^2 = 8/5, so for every orthogonal A on the clique "
        "||AC - C J_H||^2 = 2 tr(C*C) = 12/5 (24/5 as a Gram defect for involutions): no portwise orthogonal extension of "
        "the Hodge star keeps the cross-Gram": _zero(X * J * X.T)
            and _zero(((J * X.T * X - X.T * X * J).T * (J * X.T * X - X.T * X * J)).trace() - sp.Rational(8, 5))
            and all(_zero(((A * X - X * J).T * (A * X - X * J)).trace() - sp.Rational(12, 5)) for A in signed),
        "the mixed involution K(x, y) = (x, J_H y + (J_H - I) C* x) has K^2 = I, K* Q K = Q and K(0, y) = (0, J_H y), "
        "with a mixed term of rank 2; it moves the Golden first moment by J M_G J - M_G of square 32/5":
            _zero(Km * Km - sp.Matrix(sp.BlockMatrix([[sp.eye(6), sp.zeros(6, 10)], [sp.zeros(10, 6), Pc]])))
            and _zero(Km.T * Q * Km - Q) and N.applyfunc(sp.radsimp).rank() == 2
            and _zero((D.T * D).trace() - sp.Rational(32, 5)),
    }


def hodge_averaging():
    """The hub's text (11:58, 12:04): averaging the response against averaging the stiffness, and the two-copy
    realization of the Hodge-averaged response."""
    J, P, Pc, U, K, Qf, Pm, L = _hodge()
    r5 = sp.sqrt(5)
    a, b, s = sp.symbols("a b s", positive=True)
    fp = P["+"] * sp.Matrix(_golden_sites()[1])
    fp = fp / sp.sqrt((fp.T * fp)[0])
    fm = P["-"] * sp.Matrix([1] * 10)
    fm = fm / sp.sqrt((fm.T * fm)[0])
    Jf = sp.Matrix(2, 2, lambda i, j: sp.radsimp(([fp, fm][i].T * J * [fp, fm][j])[0]))
    Jf = Jf if Jf[0, 1] > 0 else sp.diag(1, -1) * Jf * sp.diag(1, -1)
    E = lambda M: (M + Jf * M * Jf) / 2
    G = sp.diag(a, b)
    q = a ** 2 + 3 * a * b + b ** 2
    simp = lambda M: M.applyfunc(sp.simplify)
    delta = sp.symbols("delta")
    A_ = 1 / s - 239 / s ** 2 + (371 + 239 ** 2) / s ** 3
    B_ = 1 / s - 241 / s ** 2 + (171 + 241 ** 2) / s ** 3
    Hn = _walk_entries()
    site, sign = _golden_sites()
    M = {n: Pc * sp.Matrix(10, 10, lambda e, f: sign[e] * sign[f] * Hn(site[f] - site[e], n)) * Pc for n in (1, 2)}
    EH = lambda Z: (Z + J * Z * J) / 2
    Modd = (M[1] - J * M[1] * J) / 2
    Vbar = EH(M[2]) - EH(M[1]) ** 2
    x = sp.symbols("x")
    fixed = lambda Z: sp.Matrix(2, 2, lambda i, j: sp.radsimp(([fp, fm][i].T * Z * [fp, fm][j])[0]))
    rho = _golden_channels()["rho"]
    alpha, beta = (1 - 1 / r5) / 2, (1 + 1 / r5) / 2
    return {
        "on the fixed plane J_H = (1/sqrt5)[[-1, 2], [2, 1]] in the basis (f+, f-), and for G = diag(a, b) there "
        "E_H(G) = (G + J G J)/2 = (1/5)[[3a + 2b, b - a], [b - a, 2a + 3b]], with ||G - E_H(G)||^2 = (2/5)(a - b)^2 = "
        "(5/8) D^2, against (a - b)^2/2 for the nearest diagonal replacement, and det E_H(G) = (a^2 + 3ab + b^2)/5":
            _zero(Jf - sp.Matrix([[-1, 2], [2, 1]]) / r5) and simp(E(G) - sp.Matrix([[3 * a + 2 * b, b - a], [b - a, 2 * a + 3 * b]]) / 5) == sp.zeros(2)
            and sp.simplify(((G - E(G)).T * (G - E(G))).trace() - sp.Rational(2, 5) * (a - b) ** 2) == 0
            and sp.Rational(2, 5) == sp.Rational(5, 8) * sp.Rational(4, 5) ** 2 and sp.simplify(E(G).det() - q / 5) == 0,
        "averaging after inversion is smaller: E_H(G^-1)^-1 = (5ab/(a^2 + 3ab + b^2)) E_H(G), so E_H(G) - E_H(G^-1)^-1 = "
        "((a - b)^2/(a^2 + 3ab + b^2)) E_H(G) >= 0, equal only when a = b, with relative size 4 delta^2/(5 - delta^2) "
        "for delta = (a - b)/(a + b)": simp(E(G.inv()).inv() - 5 * a * b / q * E(G)) == sp.zeros(2)
            and sp.simplify((a - b) ** 2 / q - (4 * delta ** 2 / (5 - delta ** 2)).subs(delta, (a - b) / (a + b))) == 0,
        "for the port, a(s) - b(s) = 2/s^2 - 760/s^3 + O(s^-4) from the means 239, 241 and variances 371, 171, so "
        "||[J_H, G(s)]||^2 = 32/(5 s^4) + O(s^-5) and the fixed-block gap is 4 P_fix/(5 s^3) + O(s^-4)":
            sp.expand(A_ - B_) == 2 / s ** 2 - 760 / s ** 3
            and sp.limit(sp.Rational(8, 5) * (A_ - B_) ** 2 * s ** 4, s, sp.oo) == sp.Rational(32, 5)
            and sp.limit((A_ - B_) ** 2 / (A_ ** 2 + 3 * A_ * B_ + B_ ** 2) / s * s ** 3, s, sp.oo) == sp.Rational(4, 5),
        "two copies of the bath realize the averaged response at every s: with T~ = (T; T J_H)/sqrt2 on H + H, T~* T~ = "
        "P_cycle, the swap commutes with H + H and sends T~ to T~ J_H, and T~*(H + H)^n T~ = E_H(T* H^n T); the memory "
        "pays M_odd^2 = (4/5) P_fix, so the repaired fixed means are 240 +- 1/sqrt5 and variances 1359/5 +- 20 sqrt5, while "
        "the floor (1987 - 31 sqrt5)/10 > 171 stays on the moving channels":
            _zero((Pc + J * Pc * J) / 2 - Pc) and _zero(Modd * Modd - sp.Rational(4, 5) * Qf)
            and _zero(Vbar - EH(M[2] - M[1] ** 2) - Modd * Modd)
            and _zero(fixed(EH(M[1])).charpoly(x).as_expr() - ((x - 240) ** 2 - sp.Rational(1, 5)))
            and _zero(fixed(Vbar).charpoly(x).as_expr() - ((x - sp.Rational(1359, 5)) ** 2 - 2000))
            and _zero((Vbar * Pm).charpoly(x).as_expr() - x ** 6 * (x ** 2 - sp.Rational(1987, 5) * x + sp.Rational(985841, 25)) ** 2)
            and 1359 / 5 - 20 * 5 ** 0.5 > (1987 - 31 * 5 ** 0.5) / 10 > 171,
        "the Hodge lines mix the port's fixed channels with weights alpha = (1 - 1/sqrt5)/2 and beta = (1 + 1/sqrt5)/2, "
        "so both start at E^3, as (5 -+ sqrt5) E^3: the minus channel's E^5 start is lost, and the averaging channel needs "
        "two Kraus terms, since it kills the nonzero Hodge-odd part":
            _zero(((fp.T * (Pc + J) / 2 * fp)[0]) - alpha) and _zero(alpha * rho["plus"][3] + beta * rho["minus"][3] - (5 - r5))
            and _zero(beta * rho["plus"][3] + alpha * rho["minus"][3] - (5 + r5)) and not _zero(Modd) and _zero(EH(Modd)),
    }


def word_sylow():
    """The hub's text (11:58): the word branch on the six Sylow views, the D3 rank bounds, the native carrier, and the
    two order-five actions mod 5."""
    from sympy.polys.matrices import DomainMatrix
    perm = lambda p: Permutation(list(p))
    c, r = perm((1, 2, 0, 3, 4)), perm((1, 0, 2, 4, 3))
    sylow = sorted({frozenset(tuple((perm(p) ** k).array_form) for k in range(5)) for p in itertools.permutations(range(5))
                    if perm(p).order() == 5}, key=lambda h: sorted(h))
    act = lambda g: tuple(sylow.index(frozenset(tuple((g * Permutation(list(h)) * g ** -1).array_form) for h in H))
                          for H in sylow)
    pc, pr = act(c), act(r)
    cyc = lambda t: sorted(len(o) for o in Permutation(list(t)).full_cyclic_form)
    relabel = next((f for f in itertools.permutations(range(6))
                    if all(pc[f[i]] == f[(i + 2) % 6] and pr[f[i]] == f[-i % 6] for i in range(6))), None)
    pm = lambda p: sp.Matrix(5, 5, lambda i, j: int(i == p(j)))
    Pc_, Pr_ = pm(c), pm(r)
    un = lambda Mx: compound2(Mx).applyfunc(abs)
    Bs = sp.Matrix(carrier.signed_incidence())
    Pcyc = sp.eye(10) - Bs.T * Bs / 5
    mult = lambda chi: ((chi[0] + 2 * chi[1] + 3 * chi[2]) // 6, (chi[0] + 2 * chi[1] - 3 * chi[2]) // 6, (2 * chi[0] - 2 * chi[1]) // 6)
    trs = lambda A, B_, Pr=None: tuple(int((M if Pr is None else M * Pr).trace()) for M in (sp.eye(A.shape[0]), A, B_))
    nat_c, nat_r = sp.diag(Pc_, un(Pc_)), sp.diag(Pr_, un(Pr_))
    native = mult(trs(nat_c, nat_r))
    cyc6 = mult(trs(compound2(Pc_), compound2(Pr_), Pcyc))
    words, C, R = _words()
    word = mult((15, C.trace(), R.trace()))
    schur = lambda m1, m2: min(m1[0], m2[0]) + min(m1[1], m2[1]) + 2 * min(m1[2], m2[2])
    group = [(sp.eye(15), sp.eye(15)), (C, nat_c), (C * C, nat_c ** 2), (R, nat_r), (R * C, nat_r * nat_c), (R * C * C, nat_r * nat_c ** 2)]
    Xr = sp.Matrix(15, 15, lambda i, j: (7 * i + 3 * j * j + i * j) % 11 - 5)
    witness = sum((gn * Xr * gw.inv() for gw, gn in group), sp.zeros(15))
    Ms = sp.Matrix(5, 10, lambda i, e: int(i in carrier.edges()[e]))
    D = sp.Matrix(sp.BlockMatrix([[sp.zeros(5), Ms], [Ms.T, sp.zeros(10)]]))
    K15 = D * D
    proj = {0: (K15 - 3 * sp.eye(15)) * (K15 - 8 * sp.eye(15)) / 24, 3: K15 * (8 * sp.eye(15) - K15) / 15, 8: K15 * (K15 - 3 * sp.eye(15)) / 40}
    eig = {lam: mult(trs(nat_c, nat_r, Pl)) for lam, Pl in proj.items()}
    comp = sp.Matrix(4, 4, lambda i, j: int(i == j + 1) - int(j == 3))
    G8 = sp.kronecker_product(comp, sp.eye(2))
    K8 = sp.eye(8) + 2 * (G8 + G8.inv())
    f5 = lambda Mx: DomainMatrix.from_Matrix(Mx).convert_to(sp.GF(5)).rank()
    sizes = (5, 7, 4, 5, 5, 5, 5)
    return {
        "c = (012) and r = (01)(34) generate a D3 in S5; on the six Sylow five-cycle groups c is two 3-cycles and r fixes "
        "two and swaps two pairs, and an explicit relabeling carries this action to c: i -> i + 2, r: i -> -i on six "
        "points, the action under the words' twisted duads; r is even, so every one-dimensional character of S5 is 1 on "
        "it and the twist is local to D3": len(sylow) == 6 and cyc(pc) == [3, 3] and cyc(pr) == [1, 1, 2, 2]
            and relabel is not None and (r * c * r) == c ** 2 and r.signature() == 1,
        "as D3-modules the words are 3 + 2 sign + 5 std, the native V5 + E10 (unsigned edges) 5 + 2 sign + 4 std, and the "
        "oriented cycles 2 sign + 2 std (with the trivial Lambda^4 A4, 1 + 2 sign + 2 std); so an equivariant map from the "
        "words to the native fifteen has rank at most 13, attained by a Reynolds average, and the stated J7 = 1 + 3 std "
        "gives the bounds 5 and 4": word == (3, 2, 5) and native == (5, 2, 4) and cyc6 == (0, 2, 2)
            and schur(word, native) == 13 and witness.rank() == 13
            and all(gn * witness == witness * gw for gw, gn in group)
            and schur((1, 0, 3), (1, 2, 2)) == 5 and schur((0, 0, 3), cyc6) == 4,
        "on the native carrier D^2 has eigenspaces 0, 3, 8 with D3 multiplicities (1, 0, 2), (2, 2, 2) and (2, 0, 0): "
        "every multiplicity space has dimension at most 2, so no rational operator of order five other than I commutes "
        "with both D^2 and this D3 (Phi_5 needs 4)": eig == {0: (1, 0, 2), 3: (2, 2, 2), 8: (2, 0, 0)}
            and max(max(m) for m in eig.values()) == 2,
        "the auxiliary A4 x V2: G8 = companion(Phi_5) x I2 commutes with the D3 on V2, K8 = I + 2(G8 + G8^-1) has K8^2 = "
        "5I, trace 0 and determinant 625; mod 5, G8 - I has ranks 6, 4, 2, 0 (two J4 blocks) while K8 has rank 4 and "
        "square 0 (I + 4 K8 is four J2 blocks): two different order-five groups":
            G8 * sp.kronecker_product(sp.eye(4), sp.Matrix([[0, -1], [1, -1]])) == sp.kronecker_product(sp.eye(4), sp.Matrix([[0, -1], [1, -1]])) * G8
            and K8 * K8 == 5 * sp.eye(8) and K8.trace() == 0 and K8.det() == 625
            and [f5((G8 - sp.eye(8)) ** k) for k in range(1, 5)] == [6, 4, 2, 0] and f5(K8) == 4
            and all(v % 5 == 0 for v in K8 * K8) and f5(4 * K8) == 4,
        "the exact fields Q(sqrt2) of the words and Q(sqrt5) of the Hodge star meet only in Q (2, 5 and 10 are not "
        "squares), and the atlas weights 1/(7 n) over groups of sizes 5, 7, 4, 5, 5, 5, 5 sum to 1, so W E = I7 and E W "
        "is a rank-7 projector in dimension 252": all(not sp.sqrt(k).is_rational for k in (2, 5, 10))
            and sum(sizes) == 36 and sum(sp.Rational(1, 7 * n) * n for n in sizes) == 1 and 36 * 7 == 252,
    }


def clock_root_address():
    """The hub's text (11:58): two order-five lattice actions, and a 4320-to-240 root address with its limits."""
    R = assignment.roots10()
    keys = {tuple(v): i for i, v in enumerate(R)}
    S, T_ = assignment.SITE, assignment.TWIN
    base = sp.Matrix([list(S[i]) for i in range(4)] + [list(T_[i]) for i in range(4)])
    mat = lambda imgs: (base.inv() * sp.Matrix([list(v) for v in imgs])).T
    Rd = mat([S[(i + 1) % 5] for i in range(4)] + [T_[(i + 1) % 5] for i in range(4)])
    Rf = mat([S[(i + 1) % 5] for i in range(4)] + [T_[i] for i in range(4)])
    on = lambda M_: [keys[tuple(int(z) for z in M_ * sp.Matrix(v))] for v in R]
    cycles = lambda img: Counter(len(o) for o in Permutation(img).full_cyclic_form)
    cls = lambda v: int(round(v[:5].sum() / 5)) % 5
    B8 = np.array(spine.frame()[0], float)
    D2 = np.rint(2 * glue.roots()).astype(int)
    classes = list(itertools.product((0, 1), repeat=8))
    band = [240 - int(sum((-1) ** ((r2 @ np.rint(2 * B8 @ np.array(cl)).astype(int) // 4) % 2) for r2 in D2)) for cl in classes]
    def census(M_):
        Mc = np.rint(np.linalg.inv(B8) @ np.array(M_, float) @ B8).astype(int)
        idx = {cl: i for i, cl in enumerate(classes)}
        step = [idx[tuple(Mc @ np.array(cl) % 2)] for cl in classes]
        out = Counter()
        seen = set()
        for i in range(256):
            if i not in seen:
                o = [i]
                while step[o[-1]] != i:
                    o.append(step[o[-1]])
                seen |= set(o)
                out[(len(o), band[i])] += 1
        return out
    img_d = on(Rd)
    orbit_reps, seen = [], set()
    for i in sorted(range(240), key=lambda i: tuple(R[i])):
        if i not in seen:
            j, orb = i, []
            while j not in orb:
                orb.append(j)
                j = img_d[j]
            seen |= set(orb)
            orbit_reps.append(i)
    def f(j):
        i = orbit_reps[j % 48]
        for _ in range((2 * (j // 48)) % 5):
            i = img_d[i]
        return i
    F = [f(j) for j in range(4320)]
    ip = lambda i, k: int(R[i] @ R[k])
    witness = next((j, k) for j in range(240) for k in range(240) if ip(F[j], F[k]) != ip(F[j + 1], F[k + 1]))
    sizes = Counter(cls(v) for v in R)
    return {
        "R_diag turns both A4's and R_first only the carrier's: they fix 0 and 20 roots, make 48 and 44 root five-cycles, "
        "have det(R - I) = 25 and 0, and both keep the five glue classes 40/50/50/50/50":
            Rd ** 5 == sp.eye(8) and Rf ** 5 == sp.eye(8) and cycles(img_d) == Counter({5: 48})
            and cycles(on(Rf)) == Counter({1: 20, 5: 44}) and (Rd - sp.eye(8)).det() == 25 and (Rf - sp.eye(8)).det() == 0
            and all(cls(R[img_d[i]]) == cls(R[i]) for i in range(240)) and sizes == Counter({0: 40, 1: 50, 2: 50, 3: 50, 4: 50}),
        "on the half-periods R_diag fixes only the origin and turns 24 five-cycles at energy 224 and 27 at 256 (the tick's "
        "census), while R_first fixes 16 (the origin, 10 at 224, 5 at 256) and turns 22 and 26 five-cycles":
            census(Rd) == Counter({(1, 0): 1, (5, 224): 24, (5, 256): 27})
            and census(Rf) == Counter({(1, 0): 1, (1, 224): 10, (1, 256): 5, (5, 224): 22, (5, 256): 26}),
        "the address f(j) = R_diag^(2 floor(j/48) mod 5) r_(j mod 48), with r_a the least root of each of the 48 orbits, "
        "factors through j mod 240, meets every root 18 times, and f(j + 864) = R_diag f(j); the unit step is not an "
        "isometry of the roots": len(orbit_reps) == 48 and all(F[j] == F[j % 240] for j in range(4320))
            and set(Counter(F).values()) == {18} and len(set(F)) == 240
            and all(F[(j + 864) % 4320] == img_d[F[j]] for j in range(4320)) and witness is not None,
        "the address j mod 36 and the phase 4j mod 5 take 180 joint values, 24 frames each; the address with the root "
        "address takes 720, 6 frames each": set(Counter((j % 36, 4 * j % 5) for j in range(4320)).values()) == {24}
            and len(Counter((j % 36, 4 * j % 5) for j in range(4320))) == 180
            and set(Counter((j % 36, F[j]) for j in range(4320)).values()) == {6}
            and len(Counter((j % 36, F[j]) for j in range(4320))) == 720,
        "no permutation of the 240 roots advances every glue class by 1, since class 0 has 40 roots and the others 50, and "
        "the 864 frames of one phase are not a multiple of 40 or 50": sizes[0] != sizes[1] and 864 % 40 and 864 % 50,
    }


def coordinate_bridge():
    """The hub's text (12:04): the A4 coordinate map, the native label, the doubling census and the angle patterns."""
    R = assignment.roots10()
    S, T_ = np.array(assignment.SITE), np.array(assignment.TWIN)
    Mb = np.vstack([S, T_]).T / 10
    keys = {tuple(v): i for i, v in enumerate(R)}
    cls = lambda v: int(round(v[:5].sum() / 5)) % 5
    perm2 = [0, 2, 4, 1, 3]
    dbl = lambda v: np.array([v[perm2.index(i)] for i in range(5)] + list(v[5:]))
    img = [keys[tuple(dbl(v))] for v in R]
    cyc = Counter(len(o) for o in Permutation(img).full_cyclic_form)
    fixed = [i for i in range(240) if img[i] == i]
    twin = [i for i, v in enumerate(R) if not v[:5].any() or len(set(v[:5])) == 1]
    extra = [i for i in fixed if i not in twin]
    rootset = set(keys)
    carrier_copy = [i for i, v in enumerate(R) if not v[5:].any() and v[:5].sum() == 0]
    pattern = lambda i, copy: tuple(sum(1 for k in copy if int(R[i] @ R[k]) == t) for t in (100, 0, -100))
    mixed = [i for i in range(240) if cls(R[i]) != 0]
    gram = Mb.T @ Mb
    P4 = np.eye(5) - np.ones((5, 5)) / 5
    return {
        "the site/twin embedding of layer 24 is the hub's coordinate bridge: its 10 columns have Gram P_A4 + P_A4' on the "
        "two trace-zero five-spaces, and the 240 roots it produces are 112 integer and 128 half-integer vectors":
            np.allclose(gram, np.block([[P4, np.zeros((5, 5))], [np.zeros((5, 5)), P4]]))
            and sum(1 for v in R if not (v % 10).any()) == 112 and sum(1 for v in R if (v % 10).any()) == 128,
        "the doubling i -> 2i of the carrier's sites, the twin fixed, has 40 fixed roots, 10 two-cycles and 45 "
        "four-cycles; the 20 fixed roots beyond the twin copy lie in classes 2 and 3, are not closed under root sums, and "
        "meet the twin copy in 240 nonzero products of 400": cyc == Counter({1: 40, 2: 10, 4: 45}) and len(twin) == 20
            and len(extra) == 20 and Counter(cls(R[i]) for i in extra) == Counter({2: 10, 3: 10})
            and any(tuple(R[i] + R[k]) in rootset and keys[tuple(R[i] + R[k])] not in extra for i in extra for k in extra)
            and sum(1 for i in extra for k in twin if int(R[i] @ R[k])) == 240,
        "every mixed root meets one copy in the pattern (6, 8, 6) and the other in (4, 12, 4) at products 1, 0, -1; "
        "classes 1 and 4 have the first pattern against the carrier's copy, classes 2 and 3 against the twin's":
            len(carrier_copy) == 20
            and all(pattern(i, carrier_copy) == ((6, 8, 6) if cls(R[i]) in (1, 4) else (4, 12, 4)) for i in mixed)
            and all(pattern(i, twin) == ((4, 12, 4) if cls(R[i]) in (1, 4) else (6, 8, 6)) for i in mixed),
    }


def notes_1207():
    """The sibling's MODEL of 11:36-12:07: the remaining exact items, with three corrections."""
    J, P, Pc, U, K, Qf, Pm, L = _hodge()
    r5 = sp.sqrt(5)
    E_ = carrier.edges()
    Bs = sp.Matrix(carrier.signed_incidence())
    Ms = sp.Matrix(5, 10, lambda i, e: int(i in E_[e]))
    both = sp.Matrix.vstack(Ms, Bs).nullspace()
    n_, f_ = sp.Matrix(counts._oriented_cycle(1)), sp.Matrix(counts._oriented_cycle(2))
    v = sp.Matrix([-3, 1, 2, 0, -1, 0, -2, 1, -1, 3])
    D = sp.Matrix(sp.BlockMatrix([[sp.zeros(5), Ms], [Ms.T, sp.zeros(10)]]))
    K15 = D * D
    tr = [(K15 ** n).trace() for n in range(6)]
    I15 = sp.eye(15)
    P0, P3, P8 = (K15 - 3 * I15) * (K15 - 8 * I15) / 24, K15 * (8 * I15 - K15) / 15, K15 * (K15 - 3 * I15) / 40
    matchings = lambda pts: [[]] if not pts else [[(pts[0], q)] + m for q in pts[1:]
                                                  for m in matchings([t for t in pts[1:] if t != q])]
    synth = [frozenset(frozenset(e) for e in m) for m in matchings(list(range(6)))]
    rot = lambda sy: frozenset(frozenset((x + 1) % 6 for x in e) for e in sy)
    ref = lambda sy: frozenset(frozenset(-x % 6 for x in e) for e in sy)
    orbit = lambda sy: frozenset([sy, rot(sy), rot(rot(sy)), rot(rot(rot(sy))), rot(rot(rot(rot(sy)))), rot(rot(rot(rot(rot(sy)))))])
    s_orbits = {orbit(sy) for sy in synth}
    totals = [frozenset(t) for t in itertools.combinations(synth, 5)
              if len({e for sy in t for e in sy}) == 15]
    rot_t = lambda t: frozenset(rot(sy) for sy in t)
    t_orbits = {frozenset([t, rot_t(t), rot_t(rot_t(t)), rot_t(rot_t(rot_t(t))), rot_t(rot_t(rot_t(rot_t(t)))),
                           rot_t(rot_t(rot_t(rot_t(rot_t(t)))))]) for t in totals}
    diam = frozenset(frozenset((i, i + 3)) for i in range(3))
    inv_total = [t for t in totals if rot_t(t) == t]
    Rr = assignment.roots10()
    keys = {tuple(x): i for i, x in enumerate(Rr)}
    cyc5 = [keys[tuple(np.r_[np.roll(x[:5], 1), x[5:]])] for x in Rr]
    fixed = [i for i in range(240) if cyc5[i] == i]
    second = [Rr[i] for i in fixed]
    first = [x for x in Rr if not x[5:].any() and x[:5].sum() == 0]
    Sx = sp.symbols("S", commutative=True)
    ctx = _contexts()
    Se = sum((C for C, s in ctx if s == 1), sp.zeros(10))
    So = sum((C for C, s in ctx if s == -1), sp.zeros(10))
    yuga = [432, 864, 1296, 1728]
    return {
        "the yuga lengths 432, 864, 1296, 1728 are 1, 2, 3, 4 times 432 and sum to 4320, with residues 2, 4, 1, 3 mod 5; "
        "the frame phase 4j mod 5 rises by 1 per tick, each phase holds 864 frames, each (address, phase) 24, and a "
        "tick keeps the address (864 = 24 x 36)": [y // 432 for y in yuga] == [1, 2, 3, 4] and sum(yuga) == 4320
            and [y % 5 for y in yuga] == [2, 4, 1, 3] and (4 * 864) % 5 == 1 and set(Counter(4 * j % 5 for j in range(4320)).values()) == {864}
            and 864 % 36 == 0,
        "under the six-cycle the 15 synthemes fall in orbits of 1, 2, 3, 3 and 6, each kept by the reflection, the "
        "single one being the three diameters; each duad lies in 3 synthemes; the 6 totals fall in orbits of 1, 2 and 3, "
        "and the invariant total is the orbit of 2 with one orbit of 3, without the diameters":
            len(synth) == 15 and sorted(len(o) for o in s_orbits) == [1, 2, 3, 3, 6]
            and all({ref(sy) for sy in o} == set(o) for o in s_orbits) and frozenset([diam]) in s_orbits
            and all(sum(1 for sy in synth if frozenset(e) in sy) == 3 for e in itertools.combinations(range(6), 2))
            and len(totals) == 6 and sorted(len(o) for o in t_orbits) == [1, 2, 3] and len(inv_total) == 1
            and diam not in inv_total[0]
            and sorted(len(o) for o in s_orbits if set(o) <= inv_total[0]) == [2, 3],
        "the coordinate five-cycle fixes the 20 roots of the second copy and makes 44 five-cycles of the rest; each copy "
        "is a root system in which a root meets 6 others at product 1, and all 400 cross products vanish":
            len(fixed) == 20 and len(first) == 20 and all(sum(1 for y in c if int(x @ y) == 100) == 6 for c in (first, second) for x in c)
            and all(int(x @ y) == 0 for x in first for y in second)
            and Counter(len(o) for o in Permutation(cyc5).full_cyclic_form) == Counter({1: 20, 5: 44}),
        "on the edges the signless and signed kernels have dimensions 5 and 6 and meet in 3 (three 4-cycles), filling 8; "
        "J_H does not keep that overlap; the vertex Grams 3I + J and 5I - J commute; the pentagon and pentagram are "
        "cycles outside the overlap, and with it span 5 cycle directions, the sixth being (-3, 1, 2, 0, -1, 0, -2, 1, -1, 3) "
        "of square 30": len(Ms.nullspace()) == 5 and len(Bs.nullspace()) == 6 and len(both) == 3
            and sp.Matrix.hstack(*Ms.nullspace(), *Bs.nullspace()).rank() == 8
            and sp.Matrix.hstack(*both, *(J * w for w in both)).applyfunc(sp.radsimp).rank() > 3
            and (Ms * Ms.T) * (Bs * Bs.T) == (Bs * Bs.T) * (Ms * Ms.T)
            and (Bs * n_).is_zero_matrix and (Bs * f_).is_zero_matrix and sp.Matrix.hstack(n_, f_, *both).rank() == 5
            and (Bs * v).is_zero_matrix and all((v.T * w)[0] == 0 for w in [n_, f_] + both) and (v.T * v)[0] == 30,
        "the signless D^2 has trace moments 15, 40, 200, 1240, 8840, 67480; M_(n+2) = 11 M_(n+1) - 24 M_n from M_1 on, but "
        "11 x 40 - 24 x 15 = 80, not 200; its spectral projectors (K - 3)(K - 8)/24, K(8 - K)/15 and K(K - 3)/40 have "
        "ranks 5, 8, 2 and sum to I; and S^2 + S^-2 = 3 gives (S + S^-1)^2 = 5": tr == [15, 40, 200, 1240, 8840, 67480]
            and all(tr[n + 2] == 11 * tr[n + 1] - 24 * tr[n] for n in range(1, 4)) and 11 * 40 - 24 * 15 == 80
            and [Pj.rank() for Pj in (P0, P3, P8)] == [5, 8, 2] and P0 + P3 + P8 == I15
            and P0 * P3 == sp.zeros(15) and P3 * P8 == sp.zeros(15)
            and sp.expand((Sx + 1 / Sx) ** 2 - (Sx ** 2 + Sx ** -2) - 2) == 0,
        "corrections: the parity sums differ by (4/5) Curl = (4/sqrt5) J_H, not by J_H; on the cycles S_even = (16/5) "
        "S_odd^-1, not 5/16 of it; and the yuga doubling is a label action on residues: in Z/4320 the steps 432 and 864 "
        "have orders 10 and 5, and 2 x 1728 = 3456, not 1296": _zero(So - Se - 4 * J / r5) and not _zero(So - Se - J)
            and _zero(Se * So - sp.Rational(16, 5) * Pc) and 4320 // gcd(432, 4320) == 10 and 4320 // gcd(864, 4320) == 5
            and 2 * 1728 == 3456 != 1296,
    }

# ------------------------------------------------------------------- the 12:24 chain, and THEOREM maps alone

def datum_orbit():
    """The datum under S5: a regular orbit of 120 data, all of energy 34."""
    psi0, v0 = carrier.canon_initial_datum()
    E = carrier.edges()
    K = np.array(carrier.D2(), float)

    def act(p, x):
        out = np.zeros_like(x)
        out[:5] = [x[p.index(i)] for i in range(5)]
        for k, (a, b) in enumerate(E):
            out[5 + E.index(tuple(sorted((p[a], p[b]))))] = x[5 + k]
        return out
    images = [(act(list(p), psi0), act(list(p), v0)) for p in itertools.permutations(range(5))]
    energy = lambda psi, v: v @ v / 2 + psi @ K @ psi / 2
    refl = [3, 2, 1, 0, 4]
    return {
        "the 120 vertex permutations carry the datum (psi0, v0) to 120 distinct data, so its stabilizer in S5 is trivial "
        "and the datum labels S5; every image has energy 34, since S5 commutes with D^2, and the reflection 0 <-> 3, "
        "1 <-> 2 keeps the velocity's 4-cycle but not psi0": len({tuple(np.r_[a, b]) for a, b in images}) == 120
            and all(np.isclose(energy(a, b), 34) for a, b in images)
            and np.allclose(act(refl, v0), v0) and not np.allclose(act(refl, psi0), psi0),
    }


def _chain():
    """The sibling's chain (12:24): the charge map Q (an oriented edge a -> a + d to q(a + 2d) - q(a + 4d)), the
    midpoint map m (an edge ab to the vertex 3(a + b)) and the near-minus-far line h."""
    E = carrier.edges()
    Q, m = sp.zeros(10, 5), sp.zeros(5, 10)
    for k, (i, j) in enumerate(E):
        d = (j - i) % 5
        Q[k, (i + 2 * d) % 5] += 1
        Q[k, (i + 4 * d) % 5] -= 1
        m[(3 * (i + j)) % 5, k] = 1
    return Q, m, sp.Matrix([1 if (j - i) % 5 in (1, 4) else -1 for i, j in E])


def witness_loop():
    """The sibling's MODEL of 12:24 ('Chain'): the charge map, the midpoint map and the witness loop."""
    E = carrier.edges()
    Pc, R5, U, K, Qf, Pm, L = _marked()
    B = sp.Matrix(carrier.signed_incidence())
    Ms = sp.Matrix(5, 10, lambda i, e: int(i in E[e]))
    Q, m, nf = _chain()
    PA4 = sp.eye(5) - sp.ones(5, 5) / 5
    Dv = sp.Matrix(5, 5, lambda r, c: int(r == (2 * c) % 5))
    Tv = sp.Matrix(5, 5, lambda r, c: int(r == [1, 0, 2, 3, 4][c]))

    def intertwiners(gens):
        X = sp.Matrix(10, 5, sp.symbols("x0:50"))
        eqs = [compound2(P) * X - X * P for P in gens] + [B * X, X * sp.ones(5, 1)]
        return 50 - sp.linear_eq_to_matrix([e for Y in eqs for e in Y], list(X))[0].rank()
    kerM = sp.Matrix.hstack(*Ms.nullspace())
    Pk = kerM * (kerM.T * kerM).inv() * kerM.T
    Uu, Du = compound2(R5).applyfunc(abs), compound2(Dv).applyfunc(abs)
    v = sp.Matrix([-3, 1, 2, 0, -1, 0, -2, 1, -1, 3])
    rot = [U ** k * v for k in range(5)]
    G = sp.Matrix(5, 5, lambda a, b: (rot[a].T * rot[b])[0])
    x = sp.symbols("x")
    return {
        "the charge map Q (an oriented edge a -> a + d goes to q(a + 2d) - q(a + 4d)) lands in the cycles with Q^T Q = "
        "5 P_A4 and image the four moving cycles, the witness loop; it commutes with the tick and the doubling, and the "
        "marked map is L = (U^2 - U^4) Q/5": (B * Q).is_zero_matrix and Q.T * Q == 5 * PA4 and Q.rank() == 4
            and (Pm * Q - Q).is_zero_matrix and U * Q == Q * R5 and compound2(Dv) * Q == Q * Dv
            and (U ** 2 - U ** 4) * Q / 5 == L,
        "Q is the only such map up to scale: the AGL(1,5)-maps from the trace-free sites into the cycles form a line, "
        "and no S5-map but 0 exists (the sites carry the standard 4, the cycles Lambda^2 of it)":
            intertwiners([R5, Dv]) == 1 and intertwiners([R5, Tv]) == 0,
        "the midpoint map (edge ab to the vertex 3(a + b), halfway mod 5) takes the five zero modes ker M onto the "
        "trace-free sites with Gram (5/3) P_A4, commuting with the tick and the doubling; its kernel there is the "
        "near-minus-far line (square 10, divergence (0, 2, 0, -2, 0), fixed by the tick, negated by the doubling), and "
        "Q after it carries the other four zero modes onto the witness loop":
            (m * kerM).rank() == 4 and m * Pk * m.T == sp.Rational(5, 3) * PA4
            and ((m * Uu - R5 * m) * Pk).is_zero_matrix and ((m * Du - Dv * m) * Pk).is_zero_matrix
            and (Ms * nf).is_zero_matrix and (m * nf).is_zero_matrix and (nf.T * nf)[0] == 10
            and list(B * nf) == [0, 2, 0, -2, 0] and Uu * nf == nf and Du * nf == -nf
            and (Q * m * kerM).rank() == 4 and (Pm * Q * m * kerM - Q * m * kerM).is_zero_matrix,
        "the loop's seed (-3, 1, 2, 0, -1, 0, -2, 1, -1, 3) is a charge image of square 30, a moving cycle; its five "
        "rotates sum to zero, span the loop and have Gram row (30, 5, -20, -20, 5), with strengths 25 phi^2 and "
        "25 phi^-2 twice each":
            sp.Matrix.hstack(Q, v).rank() == 4 and (v.T * v)[0] == 30 and (Pm * v - v).is_zero_matrix
            and sum(rot, sp.zeros(10, 1)).is_zero_matrix and sp.Matrix.hstack(*rot).rank() == 4
            and list(G.row(0)) == [30, 5, -20, -20, 5]
            and sp.expand(G.charpoly(x).as_expr() - x * (x ** 2 - 75 * x + 625) ** 2) == 0,
    }


def frame_affine():
    """The sibling's MODEL of 12:24: AGL(1,5) acting on the 4320 frames, compatibly with the address and the phase."""
    j = np.arange(N)
    comp = lambda f, g: ((f[0] * g[0]) % N, (f[0] * g[1] + f[1]) % N)
    t, m = (1, 864), (3457, 0)
    group, frontier = {(1, 0)}, [(1, 0)]
    while frontier:
        frontier = [k for k in {comp(h, g) for g in frontier for h in (t, m)} if k not in group]
        group.update(frontier)
    phase = lambda x: (4 * x) % 5
    loop = [3456]
    while 2 * loop[-1] % N != loop[0]:
        loop.append(2 * loop[-1] % N)
    yuga = [y % 5 for y in (432, 864, 1728, 1296)]
    return {
        "j -> j + 864 has order 5 and j -> 3457 j order 4, and conjugating the tick by the multiplication squares it, so "
        "together they generate AGL(1,5) on the frames, 20 maps; both keep the address j mod 36, and on the phase "
        "4j mod 5 they act as x -> x + 1 and x -> 2x": len(group) == 20 and pow(3457, 4, N) == 1 and pow(3457, 2, N) != 1
            and comp(comp(m, t), (pow(3457, -1, N), 0)) == (1, 1728)
            and np.array_equal((j + 864) % 36, j % 36) and np.array_equal(3457 * j % N % 36, j % 36)
            and np.array_equal(phase(j + 864), (phase(j) + 1) % 5) and np.array_equal(phase(3457 * j), 2 * phase(j) % 5),
        "every frame is 3105 (j mod 32) + 2080 (j mod 27) + 864 (4j mod 5); multiplying the yuga residues by 2 runs 432, "
        "864, 1728, 1296 and by 3 runs it backwards, while doubling the lengths runs the different loop 3456, 2592, 864, "
        "1728, which 1296 enters from outside": np.array_equal((3105 * (j % 32) + 2080 * (j % 27) + 864 * phase(j)) % N, j)
            and yuga == [2, 4, 3, 1] and all(2 * a % 5 == b and 3 * b % 5 == a for a, b in zip(yuga, yuga[1:] + yuga[:1]))
            and loop == [3456, 2592, 864, 1728] and 2 * 1296 % N == 2592 and 1296 not in loop,
    }


def tick_actions():
    """The time clock through the tick: free pentagons of roots, one zero mode per character, an automorphism of the
    triple."""
    _, _, _, _, g, _ = spine.spine_clock()
    G = spine.to_standard(g)
    R = glue.roots()
    key = lambda r: tuple(np.rint(2 * r).astype(int))
    index = {key(r): i for i, r in enumerate(R)}
    perm = [index[key(G @ r)] for r in R]
    Gr = np.rint(R @ R.T).astype(int)
    orbits = Permutation(perm).full_cyclic_form
    kinds = Counter((int(Gr[c[0], c[1]]), int(Gr[c[0], c[2]])) for c in orbits)
    _, A, Ap = glue.a4_pair()
    copies = [{index[key(r)] for r in X} for X in (A, Ap)]
    E = carrier.edges()
    R5 = sp.Matrix(5, 5, lambda r, c: int(r == (c + 1) % 5))
    U = sp.diag(R5, compound2(R5).applyfunc(abs))
    ker = sp.Matrix.hstack(*sp.Matrix(carrier.signless_incidence()).nullspace())
    X = (ker.T * ker).inv() * ker.T * U[5:, 5:] * ker
    nf = sp.Matrix([1 if (j - i) % 5 in (1, 4) else -1 for i, j in E])
    D = sp.Matrix(carrier.dirac(carrier.signless_incidence()))
    gamma = sp.Matrix(carrier.grading())
    Pl = carrier.spectral_projectors()
    tr = {lam: [(Pl[lam] * U ** j).trace() for j in range(5)] for lam in (0, 3, 8)}
    mult = {lam: ((t[0] + 4 * t[1]) / 5, (t[0] - t[1]) / 5) for lam, t in tr.items()}
    x = sp.symbols("x")
    return {
        "the time clock acts on the root graph through the tick g = r r', an automorphism with no fixed root: the 240 "
        "roots fall in 48 five-cycles, each summing to zero and spanning an A4 root lattice (Gram determinant 5), an "
        "extended A4 diagram with products -1 around a pentagon, 24 in the order of g and 24 in the order of g^2; each "
        "copy of A4 + A4' is 4 of them": sorted(perm) == list(range(240)) and np.array_equal(Gr[np.ix_(perm, perm)], Gr)
            and len(orbits) == 48 and all(len(c) == 5 and np.allclose(R[c].sum(axis=0), 0) for c in orbits)
            and all(round(np.linalg.det(R[c[:4]] @ R[c[:4]].T)) == 5 for c in orbits)
            and kinds == Counter({(-1, 0): 24, (0, -1): 24})
            and all(sum(1 for c in orbits if set(c) <= s) == 4 for s in copies),
        "through kappa the time clock acts on the five zero modes with characteristic polynomial (x - 1) Phi_5, the "
        "regular representation: one zero mode for each character, the invariant one the near-minus-far line":
            sp.expand(X.charpoly(x).as_expr() - (x - 1) * (x ** 4 + x ** 3 + x ** 2 + x + 1)) == 0
            and U[5:, 5:] * nf == nf,
        "the tick (the vertex five-cycle with its edge permutation) commutes with D and gamma and permutes the atoms, so "
        "it is an automorphism of the triple, free on its 15 points; tr(P_lambda U^j) = 0, -2, 2 for j = 1..4 on the "
        "eigenvalues 0, 3, 8, so each of the five characters has rank 3, with D^2 = 0, 8, 8 on the invariant one and "
        "0, 3, 3 on each other": U * D == D * U and U * gamma == gamma * U
            and Counter(len(c) for c in Permutation([list(U.col(k)).index(1) for k in range(15)]).full_cyclic_form) == Counter({5: 3})
            and all(len(set(t[1:])) == 1 for t in tr.values()) and [tr[lam][1] for lam in (0, 3, 8)] == [0, -2, 2]
            and mult == {0: (1, 1), 3: (0, 2), 8: (2, 0)},
    }


def theorem_connectivity():
    """THEOREM maps alone: the dots they reach, and that no one or two of them hold that diagram together."""
    thm = [k for k, j in enumerate(JOINS) if j[4] == T]
    big = set(max(components([True] * len(JOINS), statuses=(T,)), key=len))
    degree = Counter(d for k in thm for d in JOINS[k][:2])
    pairs = Counter(tuple(sorted((LEVEL_OF[JOINS[k][0]], LEVEL_OF[JOINS[k][1]]))) for k in thm)
    held = lambda drop: sum(1 for c in components([k not in drop for k in range(len(JOINS))], statuses=(T,))
                            if big & set(c)) == 1
    return {
        "THEOREM maps alone reach every dot but the product geometry and FLRW, which need an external 4-manifold, "
        "cutoff and mass scale": set(DOTS) - big == {"gravity", "cosmology"},
        "every one of those dots lies on at least three THEOREM maps": all(degree[d] >= 3 for d in big),
        "no one THEOREM map and no two THEOREM maps hold that diagram together":
            all(held((x,)) for x in thm) and all(held(pair) for pair in itertools.combinations(thm, 2)),
        "every pair of the six levels is joined directly by at least two THEOREM maps":
            all(pairs[p] >= 2 for p in itertools.combinations(range(len(LEVELS)), 2)),
    }


# ------------------------------------------------------------------- the hub's Agni-Soma source (12:29) and the 12:59 model

def _source():
    """The hub's Agni-Soma source (12:29): ker M in sympy's nullspace basis (the hub's saved basis), a zero mode a as the
    symmetric matrix A(a) with zero diagonal and zero row sums, the commutator F_AS(a, b) = upper([A(a), A(b)]), and the
    hub's witness pair."""
    E = carrier.edges()
    N5 = sp.Matrix.hstack(*sp.Matrix(carrier.signless_incidence()).nullspace())

    def sym(a):
        A = sp.zeros(5)
        for k, (i, j) in enumerate(E):
            A[i, j] = A[j, i] = a[k]
        return A

    def F(a, b):
        A, B = sym(a), sym(b)
        return sp.Matrix([(A * B - B * A)[i, j] for i, j in E])
    return E, N5, sym, F, N5 * sp.Matrix([-1, -1, -2, 1, -1]), N5 * sp.Matrix([-1, -2, -1, -2, 0])


def _word_adapter():
    """The hub's word adapter T (14:07): the D3-orbit of (1, -1, 2, -1, -1) in primitive source coordinates, 5 x 6."""
    return sp.Matrix([[1, -2, 2, 3, -1, -1], [-1, 3, -1, -2, 2, 1], [2, 1, -2, -1, -1, 3], [-1, -1, 3, 2, 1, -2],
                      [-1, -1, -1, -1, -1, -1]])


def _edge_perm(p):
    """The unsigned permutation of the ten K5 edges induced by the vertex permutation p."""
    E = carrier.edges()
    return sp.Matrix(10, 10, lambda r, c: int(E[r] == tuple(sorted((p[E[c][0]], p[E[c][1]])))))


def agni_soma():
    """The hub's text (12:29): the Agni-Soma commutator, its kernel, its uniqueness, its source-frame symmetry and its
    Hodge reading."""
    E, N5, sym, F, a, b = _source()
    Bs = sp.Matrix(carrier.signed_incidence())
    Pk = N5 * (N5.T * N5).inv() * N5.T
    Pc = sp.eye(10) - Bs.T * Bs / 5
    pairs = list(itertools.combinations(range(5), 2))
    W = sp.Matrix.hstack(*[F(N5.col(i), N5.col(j)) for i, j in pairs])
    ker = sp.Matrix.hstack(*W.nullspace())
    lam2 = lambda X: sp.Matrix(10, 10, lambda r, c: X.extract(list(pairs[r]), list(pairs[c])).det())

    def chi_kernel(p):
        X = lam2((N5.T * N5).inv() * N5.T * _edge_perm(p) * N5)
        Y = (ker.T * ker).inv() * ker.T * X * ker
        return Y.trace() if (X * ker - ker * Y).is_zero_matrix else None

    def hom(group):
        tot = 0
        for p in group:
            X = _edge_perm(p) * Pk
            cycles = (Pc * compound2(sp.Matrix(5, 5, lambda r, c: int(r == p[c])))).trace()
            tot += (X.trace() ** 2 - (X * X).trace()) / 2 * cycles
        return tot / len(group)
    reps = [[0, 1, 2, 3, 4], [1, 0, 2, 3, 4], [1, 0, 3, 2, 4], [1, 2, 0, 3, 4], [1, 2, 0, 4, 3], [1, 2, 3, 0, 4],
            [1, 2, 3, 4, 0]]
    S5 = [list(p) for p in itertools.permutations(range(5))]
    F20 = [[(u * x + t) % 5 for x in range(5)] for u in (1, 2, 3, 4) for t in range(5)]
    c, s = sp.Rational(3, 5), sp.Rational(4, 5)
    basis = [N5.col(k) for k in range(5)]
    J = _hodge()[0]
    ctx = _contexts()
    Se = sum((C for C, sg in ctx if sg == 1), sp.zeros(10))
    So = sum((C for C, sg in ctx if sg == -1), sp.zeros(10))
    Fw = F(a, b)
    return {
        "a zero mode a is the symmetric matrix A(a) with zero diagonal and zero row sums, so F_AS(a, b) = "
        "upper([A(a), A(b)]) is a circulation; on Lambda^2 ker M it has rank 6, onto light, and a kernel of character "
        "(4, -2, 0, 1, 1, 0, -1), that is Lambda^3 A4 = std x sign and not A4; up to scale it is the only S5-map from "
        "Lambda^2 ker M to the cycles (Hom dimension 1), while F20 alone allows 4":
            all((Bs * F(N5.col(i), N5.col(j))).is_zero_matrix for i, j in pairs) and W.rank() == 6 and ker.shape[1] == 4
            and [chi_kernel(p) for p in reps] == [4, -2, 0, 1, 1, 0, -1] and hom(S5) == 1 and hom(F20) == 4,
        "F_AS is invariant under the SO(2) that rotates the two source copies, F_AS(cA + sB, -sA + cB) = F_AS(A, B), so "
        "the native port g = W_AS(a ^ b) has that symmetry too; at the hub's witness a = (-1, -1, -2, 1, -1), "
        "b = (-1, -2, -1, -2, 0) in sympy's nullspace basis of M, ||F_AS||^2 = 1392 and F_AS^T J_H F_AS = 96 sqrt5, and "
        "the parity contexts read 2592 and 2976 (ratio 31/27): a chirality reading, blind to the phase":
            all(F(c * u + s * v, -s * u + c * v) == F(u, v) for u, v in itertools.product(basis, repeat=2))
            and (Fw.T * Fw)[0] == 1392
            and _zero((Fw.T * J * Fw)[0] - 96 * sp.sqrt(5))
            and _zero((Fw.T * Se * Fw)[0] - 2592) and _zero((Fw.T * So * Fw)[0] - 2976),
    }


def agni_factor():
    """The hub's text (12:29): the whole native commutator factors through the F20 midpoint and charge maps."""
    E, N5, sym, F, a, b = _source()
    Pc, R5, U, K, Qf, Pm, L = _marked()
    Q, m, h = _chain()
    D = compound2(sp.Matrix(5, 5, lambda r, c: int(r == (2 * c) % 5)))
    Kv = sp.eye(5) + 2 * (R5 + R5.T)
    Pk = N5 * (N5.T * N5).inv() * N5.T
    Lout = (-Qf + 3 * D * Qf + 2 * Pm) / 5
    Linv = sp.Rational(5, 2) * Pm - (sp.eye(10) + 3 * D) * Qf / 2
    wedge = lambda x, y: sp.Matrix([x[i] * y[j] - x[j] * y[i] for i, j in E])
    al = lambda v: (h.T * v)[0] / 10
    mix = lambda u, v: Q * Kv * (al(u) * m * v - al(v) * m * u)
    basis = [N5.col(k) for k in range(5)]
    Wh = sp.Matrix.hstack(*[F(h, sp.eye(10).col(k)) for k in range(10)]) * Pk
    return {
        "the near-minus-far line is A(h) = K_vertex - J with A(h)^2 = 5 P_A4, K_vertex = I + 2(R + R^-1); with "
        "alpha(a) = <h, a>/10, the midpoint R and the charge map C the whole commutator is F_AS(a, b) = L_out(Ra ^ Rb) - "
        "(2/5) C K_vertex [alpha(a) Rb - alpha(b) Ra] for every pair, with L_out = [-P_fix + 3D P_fix + 2 P_moving]/5":
            sym(h) == Kv - sp.ones(5, 5) and sym(h) ** 2 == 5 * (sp.eye(5) - sp.ones(5, 5) / 5)
            and all(F(u, v) == Lout * wedge(m * u, m * v) - sp.Rational(2, 5) * mix(u, v)
                    for u, v in itertools.product(basis, repeat=2)),
        "L_out is invertible on the cycles, with L_out^-1 = (5/2) P_moving - (1/2)(I + 3D) P_fix, and not orthogonal, "
        "L_out* L_out = (4/25) P_moving + (2/5) P_fix; the normalized source L_out^-1 F_AS is (Ra ^ Rb) - C K_vertex "
        "[alpha(a) Rb - alpha(b) Ra], the hub's lambda = -1 adapter":
            Lout * Linv == Pc and Linv * Lout == Pc and Lout.T * Lout == sp.Rational(4, 25) * Pm + sp.Rational(2, 5) * Qf
            and all(Linv * F(u, v) == wedge(m * u, m * v) - mix(u, v) for u, v in itertools.product(basis, repeat=2)),
        "F_AS(h, a) = -(2/5) K C R a, so W_h* W_h = (20/3)(P_kerM - P_h): the line h acts on the other four zero modes "
        "through the Golden operator K": all(F(h, u) == -sp.Rational(2, 5) * K * Q * m * u for u in basis)
            and Wh.T * Wh == sp.Rational(20, 3) * (Pk - h * h.T / 10),
    }


def agni_pullback():
    """The hub's text (12:29): the witness's commutator in the Golden root-site port, its moments and its memory."""
    E, N5, sym, F, a, b = _source()
    J, P, Pc, U, K, Qf, Pm, L = _hodge()
    Fw = F(a, b)
    Hn = _walk_entries()
    site, sign = _golden_sites()
    G = {n: sp.Matrix(10, 10, lambda e, f: sign[e] * sign[f] * Hn(site[f] - site[e], n)) for n in range(3)}
    w = [(Fw.T * P[k] * Fw)[0] for k in ("+", "-", "phi", "psi")]
    r5 = sp.sqrt(5)
    return {
        "through the Golden root-site port the witness's commutator has channel weights 288/5, 32/5 and "
        "664 -+ (304/5) sqrt5, summing to 1392, moments 1392, 334632 and 80732784, and memory variance form "
        "F^T (M_2 - M_1^2) F = 1441112/5, above the floor 171 x 1392":
            _zero(w[0] - sp.Rational(288, 5)) and _zero(w[1] - sp.Rational(32, 5)) and _zero(w[2] - 664 + 304 * r5 / 5)
            and _zero(w[3] - 664 - 304 * r5 / 5) and [(Fw.T * G[n] * Fw)[0] for n in range(3)] == [1392, 334632, 80732784]
            and (Fw.T * (G[2] - G[1] * Pc * G[1]) * Fw)[0] == sp.Rational(1441112, 5) > 171 * 1392,
    }


def source_phase():
    """The hub's text (12:29): the source observer at the witness, the phase quadratures and a ten-scalar decoder."""
    E, N5, sym, F, a0, b0 = _source()
    x = sp.symbols("a0:5 b0:5")
    A, B = sym(N5 * sp.Matrix(x[:5])), sym(N5 * sp.Matrix(x[5:]))
    Fs = F(N5 * sp.Matrix(x[:5]), N5 * sp.Matrix(x[5:]))
    wit = dict(zip(x, [-1, -1, -2, 1, -1, -1, -2, -1, -2, 0]))
    S2 = A * A + B * B
    contrast = [S2[i, i] - S2[4, 4] for i in range(4)]
    U, V, eta = (A ** 3 + A * B ** 2).trace() / 6, (A ** 2 * B + B ** 3).trace() / 6, (B ** 3).trace() / 6
    six = list(Fs[4:, 0])
    jac = lambda rows: sp.Matrix([[sp.diff(sp.expand(r), v) for v in x] for r in rows]).subs(wit)
    turn = sp.Matrix([wit[v] for v in x[5:]] + [-wit[v] for v in x[:5]])
    native = jac(six + contrast)
    Aw, Bw = sym(a0), sym(b0)
    c, s = sp.Rational(3, 5), sp.Rational(4, 5)
    Z1 = lambda P, R: ((P + sp.I * R) * (P * P + R * R)).trace() / 6
    Z3 = lambda P, R: ((P + sp.I * R) ** 3).trace() / 6
    Ar, Br = c * Aw + s * Bw, -s * Aw + c * Bw
    z1, z1r = sp.expand(Z1(Aw, Bw)), sp.expand(Z1(Ar, Br))
    u1, v1, u2, v2 = sp.re(z1), sp.im(z1), sp.re(z1r), sp.im(z1r)
    dets = [jac(six + [contrast[i], contrast[k], U, V]).det() for i, k in itertools.combinations(range(4), 2)]
    return {
        "at the witness the six commutator coordinates (the edges 12 to 34) with a0, a1, a2, b0 have Jacobian determinant "
        "-64; the ten native readings (those six and the contrasts s_i = (A^2 + B^2)_ii - (A^2 + B^2)_44) have rank 9, "
        "their Jacobian killing the phase direction (b, -a); eta_B = Tr(B^3)/6 = 144 turns at rate -256, and putting it "
        "in place of any contrast gives rank 10": jac(six + [x[0], x[1], x[2], x[5]]).det() == -64 and native.rank() == 9
            and (native * turn).is_zero_matrix and eta.subs(wit) == 144 and (jac([eta]) * turn)[0] == -256
            and all(jac(six + contrast[:k] + contrast[k + 1:] + [eta]).det() != 0 for k in range(4)),
        "Z1 = Tr[(A + iB)(A^2 + B^2)]/6 = 424/3 + 200i and Z3 = Tr[(A + iB)^3]/6 = -200 + 24i turn as e^-i theta and "
        "e^-3i theta, and U, V give back the phase: cos theta = (U U' + V V')/(U^2 + V^2), sin theta = "
        "(V U' - U V')/(U^2 + V^2); eta_B = (3 Im Z1 - Im Z3)/4 = 150 cos theta - 106 sin theta - 6 cos 3 theta - "
        "50 sin 3 theta (checked at cos theta = 3/5)": z1 == sp.Rational(424, 3) + 200 * sp.I
            and sp.expand(Z3(Aw, Bw)) == -200 + 24 * sp.I and z1r == sp.expand((c - sp.I * s) * z1)
            and sp.expand(Z3(Ar, Br)) == sp.expand((c - sp.I * s) ** 3 * (-200 + 24 * sp.I))
            and (u1 * u2 + v1 * v2) / (u1 ** 2 + v1 ** 2) == c and (v1 * u2 - u1 * v2) / (u1 ** 2 + v1 ** 2) == s
            and (Br ** 3).trace() / 6 == 150 * c - 106 * s - 6 * (4 * c ** 3 - 3 * c) - 50 * (3 * s - 4 * s ** 3),
        "keeping the six coordinates, any two contrasts and U, V gives ten readings whose Jacobian determinants at the "
        "witness are 29047685120/9, 33301037056/9, 47005499392/9, -5420154880/9, -5216829440/3 and -9171140608/9, all "
        "nonzero": dets == [sp.Rational(29047685120, 9), sp.Rational(33301037056, 9), sp.Rational(47005499392, 9),
                            sp.Rational(-5420154880, 9), sp.Rational(-5216829440, 3), sp.Rational(-9171140608, 9)],
    }


def sylow_lines():
    """The sibling's MODEL (12:59): the six Sylow sign lines frame the zero modes, and S5 permutes them with signs."""
    E, N5, sym, F, a, b = _source()
    Pk = N5 * (N5.T * N5).inv() * N5.T
    S5 = [Permutation(list(p)) for p in itertools.permutations(range(5))]
    groups = {}
    for g in S5:
        if g.order() == 5:
            groups.setdefault(frozenset(tuple((g ** k).array_form) for k in range(5)), g)
    keys, gens = list(groups), list(groups.values())
    raw = [sp.Matrix([1 if g.array_form[i] == j or g.array_form[j] == i else -1 for i, j in E]) for g in gens]
    signs = next(t for t in itertools.product((1, -1), repeat=6) if t[0] == 1 and all(
        t[i] * t[k] * (raw[i].T * raw[k])[0] == -2 for i, k in itertools.combinations(range(6), 2)))
    L = [t * r for t, r in zip(signs, raw)]
    conj = lambda g, k: keys.index(frozenset(tuple(((g ** -1 * gens[k] * g) ** e).array_form) for e in range(5)))
    act = {tuple(g.array_form): [conj(g, k) for k in range(6)] for g in S5}
    triples = list(itertools.combinations(range(6), 3))
    mat = {T: (sym(L[T[0]]) * sym(L[T[1]]) * sym(L[T[2]])).trace() for T in triples}
    edge = {T: sum(L[T[0]][e] * L[T[1]][e] * L[T[2]][e] for e in range(10)) for T in triples}
    stab = {T: [g for g in S5 if {act[tuple(g.array_form)][i] for i in T} == set(T)] for T in triples}
    fixed = {T: [e for e in E if all(tuple(sorted((g.array_form[e[0]], g.array_form[e[1]]))) == e for g in stab[T])]
             for T in triples}
    G5 = sp.Matrix(5, 5, lambda i, k: (L[i].T * L[k])[0])
    return {
        "each Sylow five-cycle group gives a sign line (+1 on its pentagon, -1 on its pentagram) in ker M of square 10; "
        "oriented with all products -2, the six sum to zero, frame the zero modes with factor 12 (sum l l^T = 12 P_kerM), "
        "and any five have Gram 12I - 2J, eigenvalues 12 four times and 2":
            all((sp.Matrix(carrier.signless_incidence()) * l).is_zero_matrix and (l.T * l)[0] == 10 for l in L)
            and sum(L, sp.zeros(10, 1)).is_zero_matrix and sum((l * l.T for l in L), sp.zeros(10)) == 12 * Pk
            and G5 == 12 * sp.eye(5) - 2 * sp.ones(5, 5),
        "S5 permutes the six lines up to sign, through its transitive action on the six Sylow groups (PGL(2,5) on the "
        "projective line), and the character of ker M is sign x (that permutation character - 1): the zero modes are "
        "the sign twist of PGL(2,5)'s 5":
            all(_edge_perm(g.array_form) * L[k] in (L[act[tuple(g.array_form)][k]], -L[act[tuple(g.array_form)][k]])
                for g in S5 for k in range(6))
            and all((Pk * _edge_perm(g.array_form)).trace()
                    == g.signature() * (sum(1 for k in range(6) if act[tuple(g.array_form)][k] == k) - 1) for g in S5),
        "the twenty triples have cubic matrix trace Tr(A_i A_j A_k) = 16 or -16, ten each (the edge-by-edge triple sums "
        "are 4 and -4, with the same signs); complementary triples have opposite signs; each triple is kept by six "
        "permutations, which fix exactly one edge, and each edge comes from two triples, one of each sign":
            Counter(mat.values()) == Counter({16: 10, -16: 10}) and all(edge[T] * 4 == mat[T] for T in triples)
            and all(mat[T] == -mat[tuple(sorted(set(range(6)) - set(T)))] for T in triples)
            and all(len(stab[T]) == 6 and len(fixed[T]) == 1 for T in triples)
            and all(sorted(mat[T] for T in triples if fixed[T] == [e]) == [-16, 16] for e in E),
    }


def notes_1259():
    """The sibling's MODEL (12:28-12:59) and the hub's 12:29 text: angles, orientations, the F20 clock and modules, and the
    witness's radial tangent."""
    import mpmath
    from sympy.polys.matrices import DomainMatrix
    E, N5, sym, F, a, b = _source()
    Bs = sp.Matrix(carrier.signed_incidence())
    Ms = sp.Matrix(carrier.signless_incidence())
    Pk = N5 * (N5.T * N5).inv() * N5.T
    Pc, R5, U, K, Qf, Pm, L = _marked()
    Q, m, h = _chain()
    x = sp.symbols("x")
    c1, c2 = N5.col(0), N5.col(1)
    c3 = sp.Matrix([0, 0, 1, -1, 0, 0, 0, -1, 1, 0])
    w5, w7 = sp.Matrix([-1, 1, 0, 0, 1, 0, 0, -1, -1, 1]), sp.Matrix([2, 0, -1, -1, 0, -1, -1, 0, 0, 2])
    C3 = sp.Matrix.hstack(c1, c2, c3)
    n_, f_ = sp.Matrix(counts._oriented_cycle(1)), sp.Matrix(counts._oriented_cycle(2))
    v = sp.Matrix([-3, 1, 2, 0, -1, 0, -2, 1, -1, 3])
    Dv = sp.Matrix(5, 5, lambda r, c: int(r == (2 * c) % 5))
    D = compound2(Dv)
    Uu, Du = U.applyfunc(abs), D.applyfunc(abs)
    fail = (U * Pc - Pc * Uu) * Pk
    avg = sum((U ** k * D ** d * Pc * (Uu ** k * Du ** d).T for k in range(5) for d in range(4)), sp.zeros(10)) * Pk
    marks = [sp.Matrix([1 if t == i else 0 if t == k else sp.Rational(-1, 3) for t in range(5)])
             for i, k in itertools.permutations(range(5), 2)]
    Bn, Kn = np.array(Bs, dtype=float), np.array(N5, dtype=float)
    oriented = sum(np.linalg.matrix_rank(np.hstack([Kn, (Bn * np.array(t)[None, :]).T])) == 9
                   for t in itertools.product((1, -1), repeat=10))
    f2 = DomainMatrix.from_Matrix(sp.Matrix.hstack(N5, Ms.T)).convert_to(sp.GF(2)).rank()
    orbits = {frozenset((u * k + t) % N for u in (1, 3457, pow(3457, 2, N), pow(3457, 3, N)) for t in range(0, N, 864))
              for k in range(N)}
    chars = [(g5.trace(), (Pk * g10.applyfunc(abs)).trace(), (Pc * g10).trace())
             for g5, g10 in ((R5, U), (Dv, D), (Dv ** 2, D ** 2), (R5 * Dv, U * D))]
    mpmath.mp.dps = 50
    R = [mpmath.matrix([mpmath.mpf(int(round(2 * t))) / 2 for t in r]) for r in glue.roots()]
    w = mpmath.matrix([mpmath.mpf(t) / 10 for t in (28, 28, 6, 2, 1, 0, 0, 0)])
    H, grad = mpmath.zeros(8, 8), mpmath.zeros(8, 1)
    for r in R:
        H += mpmath.cos((r.T * w)[0]) * (r * r.T)
        grad += mpmath.sin((r.T * w)[0]) * r
    proj = lambda n: mpmath.eye(8) - (n * n.T) / (n.T * n)[0]
    least = lambda n: sorted(mpmath.eigsy(proj(n) * H * proj(n))[0])[1]
    energy = 240 - sum(mpmath.cos((r.T * w)[0]) for r in R)
    inside = lambda y, lo, hi: mpmath.mpf(lo[0]) / lo[1] < y < mpmath.mpf(hi[0]) / hi[1]
    ctx = _contexts()
    Se = sum((C for C, sg in ctx if sg == 1), sp.zeros(10))
    So = sum((C for C, sg in ctx if sg == -1), sp.zeros(10))
    digits = sp.Matrix([[9, 8, 0], [0, 8, 6], [0, 8, 8], [8, 8, 0]])
    minors = [digits.extract(list(r), [0, 1, 2]).det() for r in itertools.combinations(range(4), 3)]
    return {
        "ker M meets the cycles at squared cosines 1, 1, 1, 7/15 and 1/5: the shared directions are three 4-cycles c1, c2, "
        "c3 of square 4 (Gram determinant 36; c1 and c2 are sympy's first two nullspace vectors), and w = (-1, 1, 0, 0, 1, "
        "0, 0, -1, -1, 1) of square 6 and (2, 0, -1, -1, 0, -1, -1, 0, 0, 2) of square 12 carry the 1/5 and the 7/15; "
        "the loop seed is 5 P_cycle w, and 2h = w' - c1 - c2 - 2c3, so the cycles keep 21/25 of the line (7 in the "
        "shared cycles, 3 along w', none along w); c1 meets the pentagon and the pentagram at -1 and 3":
            sp.expand((Pk * Pc * Pk).charpoly(x).as_expr()
                      - x ** 5 * (x - 1) ** 3 * (x - sp.Rational(7, 15)) * (x - sp.Rational(1, 5))) == 0
            and (Ms * C3).is_zero_matrix and (Bs * C3).is_zero_matrix and (C3.T * C3).det() == 36
            and all((Ms * y).is_zero_matrix and (C3.T * y).is_zero_matrix for y in (w5, w7)) and (w5.T * w7)[0] == 0
            and [(w5.T * w5)[0], (w7.T * w7)[0]] == [6, 12]
            and [(y.T * Pc * y)[0] / (y.T * y)[0] for y in (w5, w7)] == [sp.Rational(1, 5), sp.Rational(7, 15)]
            and v == 5 * Pc * w5 and 2 * h == w7 - c1 - c2 - 2 * c3 and (h.T * Pc * h)[0] == sp.Rational(42, 5)
            and (h.T * C3 * (C3.T * C3).inv() * C3.T * h)[0] == 7 and (h.T * w7)[0] ** 2 == 36 and (h.T * w5)[0] == 0
            and [(c1.T * n_)[0], (c1.T * f_)[0]] == [-1, 3] and all((y.T * z)[0] == 0 for y in (c2, c3) for z in (n_, f_)),
        "the orthogonal projection of ker M to the cycles is injective but not tick-equivariant (the failure has rank 3 "
        "and square 32/5), and its F20 average is 0: the equivariant bridge is the midpoint; the twenty marks (1 at one "
        "site, 0 at another, -1/3 elsewhere) average to P_A4/3":
            (Pc * N5).rank() == 5 and fail.rank() == 3 and (fail.T * fail).trace() == sp.Rational(32, 5)
            and avg.is_zero_matrix
            and sum((y * y.T for y in marks), sp.zeros(5)) / 20 == (sp.eye(5) - sp.ones(5, 5) / 5) / 3,
        "all 1024 orientations of the edges keep the projection of ker M injective, since mod 2 every oriented incidence "
        "is M and [ker M | M^T] has rank 9 over F2 (the hub)": oriented == 1024 and f2 == 9,
        "j -> j + 864 and j -> 3457 j keep j mod 864, so F20 has 864 orbits of five frames, 24 per address; on the phase "
        "functions, the zero modes and the cycles it has characters (0, 1, 1, 1), (0, -1, 1, -1) and (1, 0, -2, 0) on "
        "the tick, the doubling, its square and their product: 1 + A4, sign + A4 and a rotation plane + A4 (the hub)":
            len(orbits) == 864 and all(len(o) == 5 for o in orbits)
            and Counter(min(o) % 36 for o in orbits) == Counter({k: 24 for k in range(36)})
            and chars == [(0, 0, 1), (1, -1, 0), (1, 1, -2), (1, -1, 0)],
        "the witness's energy 220.63453173134856..., its least tangent eigenvalue normal to the gradient 6.9855821612 and "
        "normal to k 10.5099477862 all lie inside the separate model's certified intervals (energy to 10^-40, the "
        "eigenvalues to 2 x 10^-12)": inside(energy, (2206345317313485609935327280537039328500696, 10 ** 40),
                                                (2206345317313485609935327280537039328500922, 10 ** 40))
            and inside(least(grad), (873197770153, 125000000000), (3492791080613, 500000000000))
            and inside(least(w), (2101989557237, 200000000000), (10509947786187, 1000000000000)),
        "the digit vectors 980, 086, 088, 880 have Smith form 1, 2, 8: their 3 x 3 minors 144, -48, -64, 128 have gcd "
        "16, the index of their span": [smith_normal_form(digits, domain=sp.ZZ)[i, i] for i in range(3)] == [1, 2, 8]
            and minors == [144, -48, -64, 128] and gcd(*minors) == 16,
        "correction, still standing: the parity sums differ by (4/5) Curl, whose square is (16/5) P_cycle, not by a Hodge "
        "star J with J^2 = P_cycle": _zero((So - Se) ** 2 - sp.Rational(16, 5) * Pc) and not _zero((So - Se) ** 2 - Pc),
    }


def notes_1259_arithmetic():
    """The sibling's MODEL (12:59): the remaining arithmetic."""
    return {
        "every frame is 2241 (j mod 160) + 2080 (j mod 27), with 2241 + 2080 = 1 mod 4320":
            all((2241 * (j % 160) + 2080 * (j % 27)) % N == j for j in range(N)) and (2241 + 2080) % N == 1,
        "276430/25753 reduces by 7 to 39490/3679; 0.979 - 63/500 = 853/1000, not 0; sqrt 128 = 8 sqrt 2; 495/183 = 165/61":
            Fraction(276430, 25753) == Fraction(39490, 3679) and gcd(276430, 25753) == 7
            and Fraction(979, 1000) - Fraction(63, 500) == Fraction(853, 1000) and sp.sqrt(128) == 8 * sp.sqrt(2)
            and Fraction(495, 183) == Fraction(165, 61),
    }


# --------------------------------------- 14:26: three ports, every order, the syntheme bridge and the word lanes

@functools.lru_cache(maxsize=None)
def _wedge():
    """The hub's root-wedge port (14:07). Every root rho is a pair (v, w) in A4 + A4': v is its carrier part in the site
    coordinates and w_b = <rho, mu_b> its twin part, each an isometry onto the sum-zero R^5. With the two label sets
    aligned, b_rho = v ^ w on the K5 edges (i < j). Returns the roots (times 10), 10 v, 10 w, 5 b (all integers), the
    inner products, and (Delta^n)_(rho, sigma) for n <= 4, which depends only on rho . sigma."""
    R10 = assignment.roots10()
    V = np.array([assignment.carrier_part(r)[:5] for r in R10], dtype=np.int64)
    W = np.array([[int((r - assignment.carrier_part(r)) @ assignment.TWIN[k]) for k in range(5)] for r in R10],
                 dtype=np.int64)
    assert not (W % 10).any()
    W //= 10
    Bw = np.array([[V[k, i] * W[k, j] - V[k, j] * W[k, i] for i, j in carrier.edges()] for k in range(240)],
                  dtype=np.int64)
    assert not (Bw % 20).any()
    Bw //= 20
    G = R10 @ R10.T // 100
    Hn = _walk_entries()
    pair = {int(G[i, j]): (i, j) for i in range(240) for j in range(240)}
    h = {c: [Hn(R10[j] - R10[i], n) for n in range(5)] for c, (i, j) in pair.items()}
    Hc = [np.array([h[c][n] for c in range(-2, 3)], dtype=object)[G + 2] for n in range(5)]
    return R10, V, W, Bw, G, h, Hc


def wedge_port():
    """The hub's text (14:07): the unmarked port T_S x(rho) = <x, b_rho>/sqrt24 into the same bath."""
    R10, V, W, Bw, G, h, Hc = _wedge()
    E = carrier.edges()
    Bs = sp.Matrix(carrier.signed_incidence())
    Pc = sp.eye(10) - Bs.T * Bs / 5
    S5 = list(itertools.permutations(range(5)))
    lab = {tuple(V[k]) + tuple(W[k]): k for k in range(240)}

    def keeps(p):
        inv = list(np.argsort(p))
        C2 = np.array(compound2(sp.Matrix(5, 5, lambda r, c: int(r == p[c]))), dtype=np.int64)
        moved = [lab.get(tuple(V[k][inv]) + tuple(W[k][inv])) for k in range(240)]
        return None not in moved and all(np.array_equal(Bw[moved[k]], C2 @ Bw[k]) for k in range(240))
    mom = [sp.Matrix(Bw.T.dot(Hc[n]).dot(Bw)) / 600 for n in range(5)]
    m = [M_[0, 0] / Pc[0, 0] for M_ in mom]
    hankel = sp.Matrix(3, 3, lambda i, j: m[i + j]).det()
    Jr = sp.Matrix([[232, 389], [1, sp.Rational(72928, 389)]])
    Ed, N5, sym, F, a, b = _source()
    Fw = F(a, b)
    P5 = 5 * np.eye(5, dtype=np.int64) - 1
    mixed = np.einsum("ke,ka,kc->eac", Bw, V, W)
    want = 240 * np.array([[[P5[i, s] * P5[j, t] - P5[i, t] * P5[j, s] for t in range(5)] for s in range(5)]
                           for i, j in E])
    chi = {p: (Pc * compound2(sp.Matrix(5, 5, lambda r, c: int(r == p[c])))).trace() for p in S5}
    sq = lambda p: tuple(p[p[i]] for i in range(5))
    return {
        "every root is (v, w) in A4 + A4' with v . v' + w . w' = rho . rho', and b_rho = v ^ w is a circulation, nonzero on "
        "the 200 mixed roots, with sum b b^T = 24 P_cycle: T_S is an isometry of the cycles into the roots; the diagonal "
        "S5 permutes the roots and carries b by the signed edge action, so T_S intertwines them; on the finite root "
        "graph A T_S = 8 T_S": all(int(V[i] @ V[j] + W[i] @ W[j]) == int(R10[i] @ R10[j]) for i in range(0, 240, 7)
                                   for j in range(240))
            and int((Bw != 0).any(axis=1).sum()) == 200 and sp.Matrix(Bw.T @ Bw) == 600 * Pc
            and all(not (np.array(Bs, dtype=np.int64) @ x).any() for x in Bw) and all(keeps(p) for p in S5)
            and np.array_equal((G == 1).astype(np.int64) @ Bw, 8 * Bw),
        "its moments are scalar, T_S* Delta^n T_S = m_n P_cycle with m = 1, 232, 54213, 12740592, 3008062816: variance "
        "389, 3 x 3 Hankel determinant 219823907 and next Jacobi coefficient 219823907/151321; the two-block Jacobi "
        "model (232, 72928/389, off-diagonal sqrt389) matches m0 to m3 and misses m4 by 219823907/389; at the Agni-Soma "
        "witness the moments are 1392 m_n, 322944, 75464496, 17734904064, and the hidden variance 541488":
            m == [1, 232, 54213, 12740592, 3008062816] and all(mom[n] == m[n] * Pc for n in range(5))
            and m[2] - m[1] ** 2 == 389 and hankel == 219823907 and hankel / 389 ** 2 == sp.Rational(219823907, 151321)
            and [(Jr ** n)[0, 0] for n in range(4)] == m[:4] and m[4] - (Jr ** 4)[0, 0] == sp.Rational(219823907, 389)
            and [(Fw.T * mom[n] * Fw)[0] for n in range(4)] == [1392, 322944, 75464496, 17734904064]
            and (Fw.T * (mom[2] - mom[1] * mom[1]) * Fw)[0] == 541488,
        "its infrared: the monopole, the dipole and both pure quadrupoles vanish, and sum b_ij v_s w_t = "
        "12 (P_is P_jt - P_it P_js) in all 250 components, so the leading amplitude is -(12/sqrt24) <x, p ^ q> = "
        "-sqrt6 <x, p ^ q> for k = (p, q); on the unit sphere of R^4 + R^4, E[p_i p_k q_j q_l] = P_ik P_jl/80, so its "
        "mean square is 6 x 2/80 = 3/20 for every unit cycle x, and with eps = 30 |k|^2 the density is "
        "(3/20)(E/30)^2 C E^3 = C E^5/6000 and the heat tail 5! C/(6000 t^6) = C t^-6/50, C = 1/(1536 pi^4 30^4)":
            not Bw.sum(axis=0).any() and not (V.T @ Bw).any() and not (W.T @ Bw).any()
            and not np.einsum("ka,kc,ke->ace", V, V, Bw).any() and not np.einsum("ka,kc,ke->ace", W, W, Bw).any()
            and np.array_equal(mixed, want) and sp.sqrt(sp.Rational(144, 24)) == sp.sqrt(6)
            and 6 * sp.Rational(2, 80) == sp.Rational(3, 20) and sp.Rational(3, 20) / 900 == sp.Rational(1, 6000)
            and sp.factorial(5) * sp.Rational(1, 6000) == sp.Rational(1, 50),
        "the cycles are real irreducible under S5 (character norm 1, Frobenius-Schur indicator 1), so every S5-invariant "
        "symmetric form on them is a multiple of the Euclidean one: none has signature (5, 1)":
            sum(chi[p] ** 2 for p in S5) == 120 and sum(chi[p] ** 2 + chi[sq(p)] for p in S5) == 240,
    }


def three_ports():
    """The hub's text (14:07): the clique, the Golden port and the root-wedge port in one bath."""
    from sympy.polys.matrices import DomainMatrix
    R10, V, W, Bw, G, h, Hc = _wedge()
    clique, sites, TC, Fm = _two_ports()
    site, sign = _golden_sites()
    Bs = sp.Matrix(carrier.signed_incidence())
    Pc = sp.eye(10) - Bs.T * Bs / 5
    Cb = sp.Matrix.hstack(*Bs.nullspace())
    Cn = np.array(Cb, dtype=np.int64)
    idx = {tuple(r): k for k, r in enumerate(R10)}
    P = np.zeros((240, 18), dtype=np.int64)
    for k, t in enumerate(clique):
        P[idx[tuple(t)], k] = 1
    for e, (t, g) in enumerate(zip(site, sign)):
        P[idx[tuple(t)], 6:12] += g * Cn[e]
    P[:, 12:] = Bw @ Cn
    M = [sp.Matrix(P.T.dot(Hc[n]).dot(P)) for n in range(5)]
    d1, d2 = (Cb.T * Cb).det(), (600 * Cb.T * Cb).det()
    K = np.column_stack([g * Bw[idx[tuple(t)]] for t, g in zip(site, sign)])
    CC = Pc * sp.Matrix(K.T @ K) * Pc / 600
    ci = [idx[tuple(t)] for t in clique]
    Gc = sp.Matrix(6, 6, lambda k, l: int(Bw[ci[k]] @ Bw[ci[l]])) / 600
    x = sp.symbols("x")
    Curl = sp.Matrix(waves.complex_ops()[3])
    ranks = [DomainMatrix.from_Matrix(sp.Matrix(sp.BlockMatrix([[M[i + j] for j in range(d + 1)] for i in range(d + 1)])))
             .rank() for d in range(3)]
    Vj = M[2] - M[1] * M[0].inv() * M[1]
    minors = [DomainMatrix.from_Matrix(Vj[:k, :k]).det() for k in range(1, 19)]
    sub = lambda ix: M[0].extract(ix, ix).det()
    return {
        "the root-wedge port meets the Golden port at squared cosines 1/24 once, 1/120 four times and 0 once (trace 3/40, "
        "pair determinant (23/24)(119/120)^4) and the clique at 1/30, 1/60 and 0 four times (trace 1/20, determinant "
        "1711/1800): six-dimensional, but not the marked port":
            sp.expand(CC.charpoly(x).as_expr() - x ** 5 * (x - sp.Rational(1, 24)) * (x - sp.Rational(1, 120)) ** 4) == 0
            and sp.expand(Gc.charpoly(x).as_expr() - x ** 4 * (x - sp.Rational(1, 30)) * (x - sp.Rational(1, 60))) == 0
            and CC.trace() == sp.Rational(3, 40) and Gc.trace() == sp.Rational(1, 20)
            and sub(list(range(6, 18))) / (d1 * d2) == sp.Rational(23, 24) * sp.Rational(119, 120) ** 4
            and sub(list(range(6)) + list(range(12, 18))) / d2 == sp.Rational(1711, 1800),
        "the three ports span 18 dimensions: in orthonormal port coordinates the joint Gram determinant is "
        "35163473387/331776000000, the joint Krylov ranks are 18, 36 and 54 through degree 2, and the joint memory "
        "M2 - M1 M0^-1 M1 is positive definite (18 positive LDL pivots, the first 8262212012399/35163473387)":
            M[0][:6, :6] == sp.eye(6) and M[0].det() / (d1 * d2) == sp.Rational(35163473387, 331776000000)
            and ranks == [18, 36, 54] and all(v > 0 for v in minors)
            and Vj[0, 0] == sp.Rational(8262212012399, 35163473387),
        "the cross map C from the Golden port to the root-wedge port has ||[J_H, C* C]||^2 = 1/1440 (C* C = "
        "P_cycle K^T K P_cycle / 600 on the edges): the marked port's Hodge star does not pass through the overlap":
            sum(z ** 2 for z in Curl * CC - CC * Curl) / 5 == sp.Rational(1, 1440),
    }


def root_shell_krylov():
    """Every order: ports on one root shell never close their Krylov space."""
    from sympy.polys.matrices import DomainMatrix
    R10, V, W, Bw, G, h, Hc = _wedge()
    Hn = _walk_entries()
    roots = {tuple(r) for r in R10}
    s = R10[0]
    clique, sites, TC, Fm = _two_ports()
    site, sign = _golden_sites()
    e = np.eye(8, dtype=np.int64)
    six = [0 * e[0]] + [10 * (e[a] + e[5]) for a in range(5)]
    tri = [10 * (e[a] - e[b]) for a, b in ((0, 1), (1, 2), (2, 0))]
    idx = {tuple(r): k for k, r in enumerate(R10)}
    ci = [idx[tuple(t)] for t in clique]
    Mc = [sp.Matrix(6, 6, lambda i, j: Hc[n][ci[i], ci[j]]) for n in range(5)]
    ranks = [DomainMatrix.from_Matrix(sp.Matrix(sp.BlockMatrix([[Mc[i + j] for j in range(d + 1)]
                                                                 for i in range(d + 1)]))).rank() for d in range(3)]
    return {
        "distinct roots meet at inner product at most 1, so a root step raises <s, .> by at most 2, and by exactly 2 only "
        "along s": all(G[i, j] <= 1 for i in range(240) for j in range(240) if i != j) and set(np.diag(G)) == {2},
        "so the point (n + 1)s is reached from a root r in n steps only from r = s, along s each time: "
        "(Delta^n)_(r, (n + 1)s) = (-1)^n if r = s and 0 otherwise, and every lower power vanishes there (checked for "
        "n <= 4)": all(Hn((n + 1) * s - r, n) == ((-1) ** n if np.array_equal(r, s) else 0) and
                       all(Hn((n + 1) * s - r, j) == 0 for j in range(n)) for n in range(5) for r in R10),
        "hence if sum_(j <= n) Delta^j p_j = 0 with every p_j supported on a translate c + R of the root shell, its value "
        "at c + (n + 1)s is (-1)^n p_n(c + s) for every root s, so p_n = 0 and, down the degrees, every p_j = 0; a port "
        "family of rank d on one root shell has Krylov rank d (n + 1) at every order, every block Hankel matrix of its "
        "moments is positive definite and its block Jacobi chain never ends: the sites of the clique, the Golden port, "
        "the root-wedge port and the triangle port are roots, and the six-site port's are roots after the shift by "
        "-(1/2, ..., 1/2)": all(tuple(t) in roots for t in list(clique) + list(site) + tri + [-t for t in tri])
            and all(tuple(t - 5) in roots for t in six),
        "so the joint 18 grows by 18 at every order (18, 36, 54 computed through degree 2), each six-port by 6 (the "
        "clique's 6, 12, 18), and no finite comparator or finite memory reproduces any of them": ranks == [6, 12, 18],
    }


def schur_memory():
    """The hub's Schur memory (11:18), now unconditional: the clique's memory and its bounds from the band edge."""
    R10, V, W, Bw, G, h, Hc = _wedge()
    clique, sites, TC, Fm = _two_ports()
    idx = {tuple(r): k for k, r in enumerate(R10)}
    ci = [idx[tuple(t)] for t in clique]
    Mn = [sp.Matrix(6, 6, lambda i, j: Hc[n][ci[i], ci[j]]) for n in range(3)]
    Vm = Mn[2] - Mn[1] ** 2
    s, d = sp.symbols("s d", positive=True)
    x = sp.symbols("x")
    return {
        "on the clique M1 = T* Delta T = 241 I - J, and the memory variance V = T* Delta Q Delta T = M2 - M1^2 "
        "(Q = 1 - T T*) is 183 I + 52 J, eigenvalues 183 five times and 495: positive definite, so no visible direction is "
        "Delta-invariant": Mn[0] == sp.eye(6) and Mn[1] == 241 * sp.eye(6) - sp.ones(6, 6)
            and Vm == 183 * sp.eye(6) + 52 * sp.ones(6, 6)
            and sp.expand(Vm.charpoly(x).as_expr() - (x - 183) ** 5 * (x - 495)) == 0,
        "with spec Delta = [0, 256] proved (the band edge), 0 <= Q Delta Q <= 256 on the hidden space, and "
        "1/(s + 256) <= 1/(s + d) <= 1/s for d in [0, 256]: the Schur memory Sigma(s) = T* Delta Q (s + Q Delta Q)^-1 "
        "Q Delta T satisfies V/(s + 256) <= Sigma(s) <= V/s for every s > 0, and the n-th boundary moment "
        "T* Delta Q (Q Delta Q)^n Q Delta T lies between 0 and 256^n V, of norm at most 495 x 256^n":
            all(band.edge().values()) and sp.simplify(1 / (s + d) - 1 / (s + 256) - (256 - d) / ((s + d) * (s + 256))) == 0
            and sp.simplify(1 / s - 1 / (s + d) - d / (s * (s + d))) == 0 and max(Vm.eigenvals()) == 495,
        "and Sigma is no finite sum of poles: a finite memory would close the clique's Krylov space, which grows by 6 at "
        "every order because its sites are roots (root_shell_krylov)": all(tuple(t) in {tuple(r) for r in R10}
                                                                            for t in clique),
    }


def hodge_star():
    """The hub's quartic chirality (14:07), read as geometry: J_H is the Hodge star of Lambda^2 A4."""
    E, N5, sym, F, a0, b0 = _source()
    Bs = sp.Matrix(carrier.signed_incidence())
    Pc = sp.eye(10) - Bs.T * Bs / 5
    Cb = sp.Matrix.hstack(*Bs.nullspace())
    Curl = sp.Matrix(waves.complex_ops()[3])
    f = Cb * sp.Matrix(sp.symbols("f0:6"))
    R = sp.Matrix.vstack(sp.eye(4), -sp.ones(1, 4))

    def pf(C):
        X = R.T * C * R
        return X[0, 1] * X[2, 3] - X[0, 2] * X[1, 3] + X[0, 3] * X[1, 2]
    asym = lambda g: sp.Matrix(5, 5, lambda i, j: g[E.index((i, j))] if i < j else -g[E.index((j, i))] if i > j else 0)
    lam = lambda p: compound2(sp.Matrix(5, 5, lambda r, c: int(r == p[c])))
    aw, bw = N5 * sp.Matrix([2, 1, -1, 0, 1]), N5 * sp.Matrix([0, -1, 1, 1, -2])
    Cw = sym(aw) * sym(bw) - sym(bw) * sym(aw)
    fw, fo = sp.Matrix([Cw[i, j] for i, j in E]), F(a0, b0)
    x = sp.symbols("x")
    return {
        "the cycles are Lambda^2 of the sum-zero A4 space (a circulation f is an antisymmetric C with zero row sums), and "
        "f^T Curl f = 2 Pf(R^T C R) identically, for the integral A4 basis R = [e_i - e_4] of Gram determinant 5: so "
        "<f, J_H f> = 2 Pf(C) in an oriented orthonormal basis, and J_H = Curl/sqrt5 is the Hodge star of Lambda^2 A4, "
        "with J_H^2 = P_cycle and self-dual and anti-self-dual halves of dimension 3":
            all(sp.expand(sum(asym(f).row(i))) == 0 for i in range(5))
            and sp.expand((f.T * Curl * f)[0] - 2 * pf(asym(f))) == 0
            and (R.T * R).det() == 5 and Curl == Curl.T and Curl * Curl == 5 * Pc
            and sp.expand(Curl.charpoly(x).as_expr() - x ** 4 * (x ** 2 - 5) ** 3) == 0,
        "a permutation acts on A4 with determinant its sign, and accordingly Lambda^2(p)^T Curl Lambda^2(p) = sgn(p) Curl "
        "for all 120: the star's orientation character, which is why the even contexts keep J_H and the odd ones negate it":
            all(lam(p).T * Curl * lam(p) == Permutation(list(p)).signature() * Curl for p in itertools.permutations(range(5))),
        "the hub's quartic witness a = (2, 1, -1, 0, 1), b = (0, -1, 1, 1, -2) has Pf(R^T C R) = 175, ||f||^2 = 258, "
        "f^T Curl f = 350 and f^T J_H f = 70 sqrt5; the Agni-Soma witness has Pfaffian 240 and 96 sqrt5":
            pf(Cw) == 175 and (fw.T * fw)[0] == 258 and (fw.T * Curl * fw)[0] == 350 and pf(asym(fo)) == 240
            and (fo.T * Curl * fo)[0] == 480,
    }


@functools.lru_cache(maxsize=None)
def _six_lines():
    """The six Sylow sign lines as the hub builds them (14:07): h0 is +1 on the pentagon and -1 on the pentagram, the
    others are sgn(p) U(p) h0, and sigma_p, with U(p) h_i = sgn(p) h_(sigma_p(i)), is the exceptional action."""
    E = carrier.edges()
    S5 = [tuple(p) for p in itertools.permutations(range(5))]
    sgn = {p: Permutation(list(p)).signature() for p in S5}
    U = {p: _edge_perm(p) for p in S5}
    h0 = sp.Matrix([1 if (j - i) % 5 in (1, 4) else -1 for i, j in E])
    H = []
    for p in S5:
        if sgn[p] * U[p] * h0 not in H:
            H.append(sgn[p] * U[p] * h0)
    sig = {p: tuple(H.index(sgn[p] * U[p] * x) for x in H) for p in S5}
    return H, sig, S5, sgn, U


def _matchings(s):
    s = list(s)
    if not s:
        return [frozenset()]
    return [frozenset({frozenset((s[0], t))}) | m for t in s[1:] for m in _matchings([y for y in s[1:] if y != t])]


def syntheme_bridge():
    """The hub's text (14:07): the six Sylow labels carry the exceptional S5, and its synthemes are the carrier."""
    H, sig, S5, sgn, U = _six_lines()
    E = carrier.edges()
    M = sp.Matrix(carrier.signless_incidence())
    SY = _matchings(range(6))
    move = lambda p, m: frozenset(frozenset(sig[p][y] for y in pr) for pr in m)
    orbits, seen = [], set()
    for m in SY:
        if m not in seen:
            o = {move(p, m) for p in S5}
            seen |= o
            orbits.append(o)
    special = next(o for o in orbits if len(o) == 5)
    vert = {i: [m for m in special if all(move(p, m) == m for p in S5 if p[i] == i)] for i in range(5)}
    v = {i: vert[i][0] for i in range(5)}
    ends = {m: tuple(i for i in range(5) if not v[i] & m) for m in SY if m not in special}
    edge = {pr: m for m, pr in ends.items()}
    order = [v[i] for i in range(5)] + [edge.get(pr) for pr in E]
    D = sp.zeros(15)
    D[:5, 5:], D[5:, :5] = M, M.T
    Dsyn = sp.Matrix(15, 15, lambda r, c: int((r < 5) != (c < 5) and not order[r] & order[c]))

    def native(p):
        P = sp.zeros(15)
        for i in range(5):
            P[p[i], i] = 1
        for k, (i, j) in enumerate(E):
            P[5 + E.index(tuple(sorted((p[i], p[j])))), 5 + k] = 1
        return P
    syn = lambda p: sp.Matrix(15, 15, lambda r, c: int(order[r] == move(p, order[c])))
    t = (1, 0, 2, 3, 4)
    duads = list(itertools.combinations(range(6), 2))
    K = D * D
    F20 = {tuple(((u * y + a) % 5) for y in range(5)) for u in (1, 2, 3, 4) for a in range(5)}
    items = [("L", i) for i in range(6)] + [("D", frozenset(d)) for d in duads] + [("S", m) for m in SY]
    act = lambda p, it: (("L", sig[p][it[1]]) if it[0] == "L" else ("D", frozenset(sig[p][y] for y in it[1]))
                         if it[0] == "D" else ("S", move(p, it[1])))

    def lengths(group):
        out, done = [], set()
        for it in items:
            if it not in done:
                o = {act(p, it) for p in group}
                done |= o
                out.append(len(o))
        return sorted(out)
    return {
        "sigma_p is sharply 3-transitive on the six Sylow labels (every ordered triple once): the exceptional action, "
        "PGL(2,5) on the projective line": len(H) == 6 and sorted(Counter(s[:3] for s in sig.values()).values()) == [1] * 120,
        "the 15 synthemes (perfect matchings of the six labels) fall in orbits of 5 and 10; the five are a "
        "one-factorization, holding each of the 15 duads once": sorted(len(o) for o in orbits) == [5, 10]
            and Counter(pr for m in special for pr in m) == Counter({frozenset(d): 1 for d in duads}),
        "vertex i's stabilizer fixes exactly one special syntheme v_i, and a syntheme of the ten shares no pair with "
        "exactly two of them, its endpoints: M(i, jk) = 1 exactly when v_i and e_jk share no pair, so the matching Pi "
        "carries the carrier's D to the syntheme Dirac operator, equivariantly for all 120 permutations, with "
        "K = D^2 satisfying K (K - 3)(K - 8) = 0": all(len(vert[i]) == 1 for i in range(5)) and len(set(v.values())) == 5
            and sorted(ends.values()) == sorted(E) and Dsyn == D and all(native(p) == syn(p) for p in S5)
            and K * (K - 3 * sp.eye(15)) * (K - 8 * sp.eye(15)) == sp.zeros(15),
        "a transposition has trace 7 on the carrier's vertices and edges and on the synthemes, but 3 on the 15 ordinary "
        "duads of the six labels: the carrier is the syntheme module, not the duad module":
            native(t).trace() == 7 and syn(t).trace() == 7
            and sum(1 for d in duads if tuple(sorted(sig[t][y] for y in d)) == d) == 3,
        "the 36 = 6 + 15 + 15 of labels, duads and synthemes has S5 orbits 6, 15, 5 and 10 and F20 orbits 1, 5, 5, 5, 10 "
        "and 10: a covariant finite address set, not the transitive Z/36": lengths(S5) == [5, 6, 10, 15]
            and lengths(F20) == [1, 5, 5, 5, 10, 10],
    }


def sylow_frame():
    """The hub's text (14:07): the complex six-line frame of the source, its cubics and its blind stratum."""
    H, sig, S5, sgn, U = _six_lines()
    E, N5, sym, F, a0, b0 = _source()
    Bs = sp.Matrix(carrier.signed_incidence())
    Pc = sp.eye(10) - Bs.T * Bs / 5
    Pk = N5 * (N5.T * N5).inv() * N5.T
    Hm = sp.Matrix.hstack(*H)
    Si = [sym(x) for x in H]
    triples = list(itertools.combinations(range(6), 3))
    eps = {T3: (Si[T3[0]] * Si[T3[1]] * Si[T3[2]]).trace() / 16 for T3 in triples}
    basis = [N5.col(k) for k in range(5)]

    def rebuilt(a, b):
        ur, ui = Hm.T * a, Hm.T * b
        return sum(((ur[i] * ui[j] - ur[j] * ui[i]) * (Si[i] * Si[j] - Si[j] * Si[i])
                    for i, j in itertools.combinations(range(6), 2)), sp.zeros(5)) / 144
    z, ar, br = sp.symbols("z0:5"), sp.symbols("ar0:5"), sp.symbols("br0:5")
    u = Hm.T * N5 * sp.Matrix(z)
    cubic = sp.expand((sym(N5 * sp.Matrix(z)) ** 3).trace()
                      - sum(sp.Rational(eps[T3], 18) * u[T3[0]] * u[T3[1]] * u[T3[2]] for T3 in triples))
    A_, B_ = sym(N5 * sp.Matrix(ar)), sym(N5 * sp.Matrix(br))
    up, um = Hm.T * N5 * (sp.Matrix(ar) + sp.I * sp.Matrix(br)), Hm.T * N5 * (sp.Matrix(ar) - sp.I * sp.Matrix(br))
    first = sp.expand(((A_ + sp.I * B_) ** 2 * (A_ - sp.I * B_)).trace() - sum(
        sp.Rational(eps[T3], 54) * sp.prod([um[y] if k == c else up[y] for k, y in enumerate(T3)])
        for T3 in triples for c in range(3)))
    Zw = sym(a0) + sp.I * sym(b0)
    az, bz = N5 * sp.Matrix([sp.Rational(-1, 2), 1, 0, 0, 0]), N5 * sp.Matrix([sp.Rational(-1, 2), 0, 0, -1, 1])
    Az, Bz = sym(az), sym(bz)
    pz = (1, 0, 3, 2, 4)
    mul = lambda p, q: tuple(p[q[i]] for i in range(5))
    chs = {p: (Pk * U[p]).trace() for p in S5}
    chc = {p: (Pc * compound2(sp.Matrix(5, 5, lambda r, c: int(r == p[c])))).trace() for p in S5}
    pairs = list(itertools.combinations(range(5), 2))
    Wf = sp.Matrix.hstack(*[F(N5.col(i), N5.col(j)) for i, j in pairs])
    Gext = compound2(N5.T * N5)
    Psrc = sp.Rational(9, 10) * Gext.inv() * Wf.T * Wf
    ur, ui = Hm.T * a0, Hm.T * b0
    Rr, Ri = ur * ur.T + ui * ui.T, ui * ur.T - ur * ui.T
    return {
        "the lines are Golden matrices, A(h_i)^2 = 5 P_A4; each triple's six-element stabilizer lies in A5; any five lines "
        "read the complex source (Gram 12I - 2J, determinant 41472), while h_p - h_q is invisible to the other four, so "
        "two erasures lose a direction; the record R = u u* gives z z* = H R H^T/144 up to common phase":
            all(x * x == 5 * sp.eye(5) - sp.ones(5, 5) for x in Si)
            and all(sgn[p] == 1 for T3 in triples for p in S5 if {sig[p][y] for y in T3} == set(T3))
            and all((Hm.extract(list(range(10)), [k for k in range(6) if k != j]).T
                     * Hm.extract(list(range(10)), [k for k in range(6) if k != j])).det() == 41472 for j in range(6))
            and all((H[r].T * (H[p] - H[q]))[0] == 0 for p, q in itertools.combinations(range(6), 2)
                    for r in range(6) if r not in (p, q))
            and Hm * Rr * Hm.T / 144 == a0 * a0.T + b0 * b0.T and Hm * Ri * Hm.T / 144 == b0 * a0.T - a0 * b0.T,
        "[A, B] = (1/144) sum_(i < j) Im(conj(u_i) u_j) [S_i, S_j] for every pair (u = H^T z), and the cubics have twenty-term "
        "formulas, Tr Z^3 = sum eps_ijk u_i u_j u_k / 18 and Tr Z^2 Z* = sum eps_ijk (one factor conjugated) / 54, as "
        "polynomial identities; at the Agni-Soma witness they are -1200 + 144i and 848 + 1200i, 6 Z3 and 6 Z1":
            all(rebuilt(a, b) == sym(a) * sym(b) - sym(b) * sym(a) for a, b in itertools.product(basis, repeat=2))
            and cubic == 0 and first == 0 and sp.expand((Zw ** 3).trace()) == -1200 + 144 * sp.I
            and sp.expand((Zw ** 2 * (sym(a0) - sp.I * sym(b0))).trace()) == 848 + 1200 * sp.I,
        "the cubic phase has a blind stratum: (01)(23) sends a = N(-1/2, 1, 0, 0, 0) and b = N(-1/2, 0, 0, -1, 1) to their "
        "negatives, their commutator has edge-square 4, and both invariant cubics Tr(A^3 + A B^2) and Tr(A^2 B + B^3) "
        "vanish there, as every S5-invariant odd polynomial must":
            U[pz] * az == -az and U[pz] * bz == -bz
            and sum((Az * Bz - Bz * Az)[i, j] ** 2 for i, j in E) == 4
            and (Az ** 3 + Az * Bz ** 2).trace() == 0 and (Az ** 2 * Bz + Bz ** 3).trace() == 0,
        "the source's symmetry: Hom_S5(source, cycles) = 0, Hom_S5(Sym^2 source, source) = 1 and (Sym^3 source)^S5 = 1 "
        "(the cubic is unique up to scale); with the exterior metric G_ext = Lambda^2(N^T N), W W^+ = (10/9) P_cycle and "
        "(9/10) W^+ W is a rank-6 G_ext-orthogonal projector, so (3/sqrt10) W is a coisometry":
            sum(chs[p] * chc[p] for p in S5) == 0
            and sum((chs[p] ** 2 + chs[mul(p, p)]) * chs[p] for p in S5) == 240
            and sum(chs[p] ** 3 + 3 * chs[mul(p, p)] * chs[p] + 2 * chs[mul(p, mul(p, p))] for p in S5) == 720
            and Wf * Gext.inv() * Wf.T == sp.Rational(10, 9) * Pc and Psrc * Psrc == Psrc and Psrc.rank() == 6
            and Psrc.T * Gext == Gext * Psrc,
    }


def word_source():
    """The hub's text (14:07): the two regular word orbits reach the native source, rationally but not integrally."""
    from sympy.combinatorics import PermutationGroup
    from sympy.polys.matrices import DomainMatrix
    E, N5, sym, F, a0, b0 = _source()
    Bs = sp.Matrix(carrier.signed_incidence())
    Nc = sp.Matrix.hstack(*Bs.nullspace())
    Sp_ = lambda p: (_edge_perm(p) * N5)[5:, :]
    c, r, g = (1, 2, 0, 3, 4), (1, 0, 2, 4, 3), (1, 2, 3, 4, 0)
    mul = lambda p, q: tuple(p[q[i]] for i in range(5))
    order = [(0, 1, 2, 3, 4), c, mul(c, c), r, mul(r, c), mul(r, mul(c, c))]
    left = lambda p: sp.Matrix(6, 6, lambda i, j: int(order[i] == mul(p, order[j])))
    T_ = _word_adapter()
    f3 = lambda X: DomainMatrix.from_Matrix(X).convert_to(sp.GF(3)).rank()
    orbit = [f3(sp.Matrix.hstack(*[Sp_(p) * sp.Matrix(y) for p in order])) for y in itertools.product(range(3), repeat=5)]
    Sg = Sp_(g)
    S_ = T_.T * (T_ * T_.T).inv()
    Gh = S_ * Sg * T_ + sp.eye(6) - S_ * T_
    Tp = sp.Matrix.hstack(T_, sp.Matrix([1, 0, 0, 0, 0]))
    cols = [0, 1, 3, 4, 6]
    inv = Tp.extract(list(range(5)), cols).inv()
    Spl = sp.zeros(7, 5)
    for k, cc in enumerate(cols):
        Spl[cc, :] = inv[k, :]
    Gp = Spl * Sg * Tp + sp.eye(7) - Spl * Tp
    pairs = list(itertools.combinations(range(5), 2))
    Wp = sp.Matrix.hstack(*[F(N5.col(i), N5.col(j))[4:, :] for i, j in pairs])
    L2 = lambda p: compound2(Sp_(p))
    cyc = lambda p: (Nc.T * Nc).inv() * Nc.T * compound2(sp.Matrix(5, 5, lambda a, b: int(a == p[b]))) * Nc
    Kq = sp.Matrix.hstack(*Wp.nullspace())
    Gd = (Kq.T * Kq).inv() * Kq.T * L2(g) * Kq
    Kd = sp.eye(4) + 2 * (Gd + Gd.inv())
    ns = DomainMatrix.from_Matrix(Wp).convert_to(sp.GF(5)).nullspace().to_Matrix().T
    G5 = L2(g) * ns
    X = DomainMatrix.from_Matrix(sp.Matrix.hstack(ns, G5)).convert_to(sp.GF(5)).rref()[0].to_Matrix()[:4, 4:]
    f5 = lambda Y: DomainMatrix.from_Matrix(Y.applyfunc(lambda y: y % 5)).convert_to(sp.GF(5)).rank()
    uu, vv = sp.symbols("u0:6"), sp.symbols("v0:6")
    av, bv = T_ * sp.Matrix(uu), T_ * sp.Matrix(vv)
    q = list(F(N5 * av, N5 * bv)[4:, 0]) + [(sym(N5 * bv) ** 3).trace() / 6]
    pt = dict(zip(uu + vv, [1] + [0] * 6 + [1] + [0] * 4))
    xs = sp.symbols("x0:10")
    qa = list(F(N5 * sp.Matrix(xs[:5]), N5 * sp.Matrix(xs[5:]))[4:, 0]) + [(sym(N5 * sp.Matrix(xs[5:])) ** 3).trace() / 6]
    jn = sp.Matrix([[sp.diff(sp.expand(y), v) for v in xs] for y in qa]).subs(dict(zip(xs, list(T_[:, 0]) + list(T_[:, 1]))))
    jw = sp.Matrix([[sp.diff(sp.expand(y), v) for v in uu + vv] for y in q + [av[0], av[1], av[2], uu[0], vv[0]]]).subs(pt)
    S5 = list(itertools.permutations(range(5)))
    gen = lambda gens: {tuple(y.array_form) for y in PermutationGroup([Permutation(list(z)) for z in gens]).elements}
    chi = {p: (Nc * (Nc.T * Nc).inv() * Nc.T * compound2(sp.Matrix(5, 5, lambda a, b: int(a == p[b])))).trace() for p in S5}
    hom = lambda grp: sp.Rational(sum(chi[p] * (1 + sum(1 for i in range(5) if p[i] == i)) for p in grp), len(grp))
    Uc = sp.Matrix([[0, 1, 0, 1, 1, 0], [0, 0, 0, 0, 1, 1], [0, 1, 1, 1, 1, 0], [1, 1, 0, 0, 0, 0], [0, 0, 0, 1, 1, 0],
                    [0, 1, 0, 1, 0, 0]])
    Gs = sp.diag(1, sp.Matrix(5, 5, lambda a, b: int(a == g[b])))
    Mt = Uc.inv().T * (Nc.T * Nc) * Uc.inv()
    return {
        "c = (012) and r = (01)(34) act on each regular word orbit (980, 809, 098, 089, 908, 890 and 086, 860, 608, 680, "
        "068, 806) as left multiplication on 1, c, c^2, r, rc, rc^2, and T, the D3-orbit of (1, -1, 2, -1, -1) in the "
        "primitive source chart (sympy's nullspace basis of M, bottom block I5), intertwines them with the source: "
        "T C_w = S_c T and T R_w = S_r T, rank 5, so two lanes a = Tu, b = Tv cover the ten source coordinates":
            N5[5:, :] == sp.eye(5) and T_ == sp.Matrix.hstack(*[Sp_(p) * T_[:, 0] for p in order])
            and T_ * left(c) == Sp_(c) * T_ and T_ * left(r) == Sp_(r) * T_ and T_.rank() == 5,
        "integrally it is not onto: T has Smith invariants 1, 1, 1, 1, 3, and every one of the 243 orbit matrices over F3 "
        "has rank at most 4 (attained), so a D3-map from one regular orbit onto the source lattice has index divisible by "
        "3, and this T attains 3; rank_F3 [T | S_g T] = 5 > 4 = rank_F3 T, so no integer G has T G = S_g T":
            [smith_normal_form(T_, domain=sp.ZZ)[i, i] for i in range(5)] == [1, 1, 1, 1, 3] and max(orbit) == 4
            and len(orbit) == 243 and f3(sp.Matrix.hstack(T_, Sg * T_)) == 5 and f3(T_) == 4,
        "rationally G = S S_g T + I - S T (S = T^T (T T^T)^-1) has G^5 = I, T G = S_g T, rank(G - I) = 4 and does not "
        "commute with C_w; one more generator repairs the lane integrally: columns 0, 1, 3, 4, 6 of [T | e0] have "
        "determinant 1, and G+ = S+ S_g T+ + I - S+ T+ is an integer matrix with T+ G+ = S_g T+ and G+^5 = I7":
            Gh ** 5 == sp.eye(6) and T_ * Gh == Sg * T_ and (Gh - sp.eye(6)).rank() == 4 and Gh * left(c) != left(c) * Gh
            and Tp.extract(list(range(5)), cols).det() == 1 and all(y == int(y) for y in Gp)
            and Tp * Gp == Sg * Tp and Gp ** 5 == sp.eye(7),
        "the primitive commutator W: Lambda^2 Z^5 -> Z^6 (the last six cycle coordinates) is S5-equivariant with Smith "
        "invariants 1, 2, 2, 2, 2, 2 (F2 rank 1); on its four-dimensional dark kernel the five-cycle satisfies Phi_5, is one "
        "Jordan block mod 5 (ranks 3, 2, 1, 0) and K = I + 2(G + G^-1) has K^2 = 5I and mod-5 rank 2":
            [smith_normal_form(Wp, domain=sp.ZZ)[i, i] for i in range(6)] == [1, 2, 2, 2, 2, 2]
            and DomainMatrix.from_Matrix(Wp).convert_to(sp.GF(2)).rank() == 1
            and all(Wp * L2(p) == cyc(p) * Wp for p in S5) and L2(g) * Kq == Kq * Gd
            and sum((Gd ** k for k in range(5)), sp.zeros(4)) == sp.zeros(4) and Kd * Kd == 5 * sp.eye(4)
            and [f5((X - sp.eye(4)) ** k) for k in range(1, 5)] == [3, 2, 1, 0]
            and f5(sp.eye(4) + 2 * (X + X ** 4)) == 2,
        "at u = e0, v = e1 the cycle coordinates are (8, 2, 0, -2, 0, -4) and eta_B = Tr B^3/6 = 16; q = (W(a ^ b), eta_B) "
        "has rank 7, with a0, a1, a2 the native 10 x 10 Jacobian is 5120, and with u0, v0 the 12 x 12 word Jacobian is "
        "-46080: a local inverse at the witness, not a global or integral one":
            [sp.expand(y).subs(pt) for y in q] == [8, 2, 0, -2, 0, -4, 16] and jn.rank() == 7
            and sp.Matrix.vstack(jn, sp.eye(10)[:3, :]).det() == 5120 and jw.det() == -46080,
        "Hom_C5(cycles, site6) = 8, Hom_D3 = 4 and Hom_A5 = 0, where c, r, g generate A5: no linear map to the natural six "
        "sites carries both D3 and C5; for C5 alone the hub's U (det -1) has U G_cycle = G_site U, it is not an isometry "
        "(U^T U is not N^T N), and the transported metric U^-T (N^T N) U^-1 is C5-invariant":
            len(gen([c, r, g])) == 60 and [hom(gen(G_)) for G_ in ([g], [c, r], [c, r, g])] == [8, 4, 0]
            and Uc.det() == -1 and Uc * cyc(g) == Gs * Uc and Gs.T * Mt * Gs == Mt and Uc.T * Uc != Nc.T * Nc,
    }


def clock_sylow():
    """The hub's text (14:07): the clock phase on the six Sylow labels."""
    H, sig, S5, sgn, U = _six_lines()
    g, d = (1, 2, 3, 4, 0), (0, 2, 4, 1, 3)
    sg, sd = sig[g], sig[d]
    fixed = [i for i in range(6) if sg[i] == i]
    anchor = [i for i in range(6) if sg[i] != i and sd[i] == i]

    def f(p):
        y = anchor[0]
        for _ in range(p % 5):
            y = sg[y]
        return y
    ph = lambda j: 4 * j % 5
    return {
        "sigma_g fixes one Sylow label and turns the other five; exactly one of those five is fixed by sigma_d, and "
        "f(p) = sigma_g^p(anchor) has f(p + 1) = sigma_g f(p) and f(2p) = sigma_d f(p)": len(fixed) == 1 and len(anchor) == 1
            and all(f(p + 1) == sg[f(p)] and f(2 * p) == sd[f(p)] for p in range(5)),
        "with the phase p(j) = 4j mod 5, f(p(j + 864)) = sigma_g f(p(j)) and f(p(3457 j)) = sigma_d f(p(j)) on all 4320 "
        "frames, 864 on each moving label: the clock's AGL(1,5) acts on the source frame's labels (not physical time)":
            all(f(ph(j + 864)) == sg[f(ph(j))] and f(ph(3457 * j)) == sd[f(ph(j))] for j in range(N))
            and sorted(Counter(f(ph(j)) for j in range(N)).values()) == [864] * 5,
    }


def notes_1418():
    """The sibling's MODEL (13:02-14:18): the comparator, the even and odd ports, and two claims now proved."""
    m = [1, 242, 58691, 14259954, 3470101592]
    hank = lambda k: sp.Matrix(k, k, lambda i, j: m[i + j]).det()
    b1, b2 = sp.Integer(127), sp.Rational(15930273, 16129)
    a1 = sp.Rational(25998, 127)
    J3 = lambda a2: sp.Matrix([[242, 1, 0], [b1, a1, 1], [0, b2, a2]])
    x, q = sp.symbols("x q")
    roots = sp.real_roots(J3(200).charpoly(x))
    tri = triangle_port()
    return {
        "the triangle port's moments 1, 242, 58691, 14259954, 3470101592 have b1^2 = 127, a1 = 25998/127 and Hankel "
        "determinant 15930273, so b2^2 = 15930273/16129; the three-state comparator matches m0 to m4 for every last "
        "diagonal (200 or 210 alike) and m5 moves by 10 b1^2 b2^2 = 159302730/127, so it is not unique, and with 200 its "
        "spectrum lies inside (0, 256)": all(tri.values()) and hank(2) == 127 and hank(3) == 15930273
            and all([(J3(a2) ** n)[0, 0] for n in range(5)] == m for a2 in (200, 210))
            and (J3(210) ** 5)[0, 0] - (J3(200) ** 5)[0, 0] == sp.Rational(159302730, 127)
            and len(roots) == 3 and all(0 < r < 256 for r in roots),
        "the even (root-wedge) and odd (triangle) ports start 232 and 242: a mixture has first moment 232 + 10q and "
        "variance 389 - 162q - 100q^2, 389 at one end and 127 at the other, and its 3 x 3 Hankel falls from 219823907 to "
        "15930273": sp.expand((1 - q) * 54213 + q * 58691 - (232 + 10 * q) ** 2 - (389 - 162 * q - 100 * q ** 2)) == 0
            and 389 - 162 - 100 == 127,
        "two of the model's open items are now proved: 'the hidden state grows by exactly 6 at every order' holds for every "
        "six-port on a root shell, and so does the joint 18 (root_shell_krylov); 'if the exterior operator lies between "
        "0 and 256, the n-th boundary moment is at most 495 x 256^n' holds outright (schur_memory). The comparator, a "
        "finite truncation, cannot match every moment": all(band.edge().values()),
    }

def band_top():
    """The band edge seen through the ports: the root-wedge port is a quadrupole at both ends of the band."""
    R10, V, W, Bw, G, h, Hc = _wedge()
    R2 = R10 // 5
    tops = {}
    for u in {tuple(R2[i] + R2[j]) for i in range(240) for j in range(240)}:
        s = np.where((R2 @ np.array(u)) // 4 % 2 == 0, 1, -1)
        if s.sum() == -16:
            tops.setdefault(tuple(s), s)
    S = list(tops.values())
    idx = {tuple(r): k for k, r in enumerate(R10)}
    neg = [idx[tuple(-r)] for r in R10]
    BB, RR = (Bw @ Bw.T).astype(object), (R2 @ R2.T).astype(object)
    q2 = [int((np.outer(s, s).astype(object) * BB * RR * RR).sum()) for s in S]
    Q = [np.einsum("k,ke,ka,kb->eab", s, Bw, R2, R2) for s in S]
    clique, sites, TC, Fm = _two_ports()
    site, sign = _golden_sites()
    ci, gi = [idx[tuple(t)] for t in clique], [idx[tuple(t)] for t in site]
    Cb = np.array(sp.Matrix.hstack(*sp.Matrix(carrier.signed_incidence()).nullspace()), dtype=np.int64)
    gold = [np.array([sign[e] * s[gi[e]] for e in range(10)]) @ Cb for s in S]
    e8 = np.eye(8, dtype=np.int64)
    ti = [idx[tuple(10 * (e8[a] - e8[b]))] for a, b in ((0, 1), (1, 2), (2, 0))]
    first = [sum(s[t] * R2[t] for t in ti) for s in S]
    coef = sp.Rational(sum(q2), 25 * 16) * sp.Rational(1, 6) / 96 / 40 / 4 / 24576
    return {
        "the band's 135 top half-periods u split the roots as a D8 (the 112 with rho . u even, second moment 28 I) and its "
        "128 half-spin weights, with Hessian sum (-1)^(rho.u) rho rho^T = -4 I, so eps = 256 - 2|delta|^2 near each top":
            len(S) == 135 and all(int((s == 1).sum()) == 112 for s in S)
            and all(np.array_equal(R2[s == 1].T @ R2[s == 1], 112 * np.eye(8, dtype=np.int64)) for s in S)
            and all(np.array_equal((R2.T * s) @ R2, -16 * np.eye(8, dtype=np.int64)) for s in S),
        "b_rho is quadratic in rho, so its sum over a set of roots depends only on their second moment: over each top's D8 "
        "it is (28/60) of the full sum, which vanishes, so sum (-1)^(rho.u) b_rho = 0 at all 135 tops; b is even, "
        "b_(-rho) = b_rho, so the first order vanishes too, and the second, Q_x(u) = sum (x . b_rho)(-1)^(rho.u) rho rho^T, "
        "is traceless and nonzero at every top: the root-wedge port is a quadrupole at the band top as at its bottom":
            all(not Bw[s == 1].sum(axis=0).any() and not (s @ Bw).any() for s in S) and np.array_equal(Bw[neg], Bw)
            and all(q.any() for q in Q)
            and all(not np.einsum("eaa->e", q).any() for q in Q),
        "so with the amplitude -delta^T Q_x delta / (2 sqrt24), E[(delta^T Q delta)^2] = |delta|^4 tr Q^2 / 40 on the unit "
        "sphere of R^8 and sum_u ||Q(u)||^2 = 134784, its density near the top is 39 (256 - E)^5 / (655360 pi^4) for "
        "every unit x, the exponent of its bottom, C E^5/6000": sum(q2) == 134784 * 400 and coef == sp.Rational(39, 655360),
        "the clique and the Golden port see every top (their top matrices have rank 6), so their densities start "
        "(256 - E)^3; the odd triangle port vanishes at every half-period, and its first order is nonzero at 108 of the "
        "135 tops, so it starts (256 - E)^4":
            np.linalg.matrix_rank(sum(np.outer(s[ci], s[ci]) for s in S)) == 6
            and np.linalg.matrix_rank(sum(np.outer(a, a) for a in gold)) == 6
            and sum(1 for f in first if f.any()) == 108,
    }

# --------------------------------------------- 15:34: the pair frame, the parity pair and the norm-four dark port

@functools.lru_cache(maxsize=None)
def _pairs15():
    """The hub's pair frame (15:03): the commutators C_ij = upper([A(h_i), A(h_j)]) of the six Sylow lines, the signed
    action of S5 on the oriented pairs, and the cut, bright and dark projectors of R^15."""
    H, sig, S5, sgn, U = _six_lines()
    E = carrier.edges()
    sym = _source()[2]
    Si = [sym(h) for h in H]
    pairs = list(itertools.combinations(range(6), 2))
    C = sp.Matrix.hstack(*[sp.Matrix([(Si[i] * Si[j] - Si[j] * Si[i])[a, b] for a, b in E]) for i, j in pairs])
    B6 = sp.zeros(6, 15)
    for k, (i, j) in enumerate(pairs):
        B6[i, k], B6[j, k] = -1, 1

    def rho(p):
        R = sp.zeros(15)
        for k, (i, j) in enumerate(pairs):
            a, b = sig[p][i], sig[p][j]
            R[pairs.index(tuple(sorted((a, b)))), k] = 1 if a < b else -1
        return R
    Pcut, Pbr = B6.T * B6 / 6, C.T * C / 160
    return pairs, C, rho, Pcut, Pbr, sp.eye(15) - Pcut - Pbr


def pair_frame():
    """The hub's text (15:03): the fifteen pair commutators of the six Sylow lines, their erasures and the rotor planes."""
    H, sig, S5, sgn, U = _six_lines()
    pairs, C, rho, Pcut, Pbr, Pdk = _pairs15()
    Bs = sp.Matrix(carrier.signed_incidence())
    Pc = sp.eye(10) - Bs.T * Bs / 5
    Curl = sp.Matrix(waves.complex_ops()[3])
    lam = lambda p: compound2(sp.Matrix(5, 5, lambda r, c: int(r == p[c])))
    Cn = np.array(C, dtype=np.int64)
    rank = lambda cols: np.linalg.matrix_rank(Cn[:, list(cols)])
    r11 = Counter(int(rank(c)) for c in itertools.combinations(range(15), 11))
    r10 = Counter(int(rank(c)) for c in itertools.combinations(range(15), 10))
    erased = [frozenset(set(range(15)) - set(c)) for c in itertools.combinations(range(15), 10) if rank(c) == 5]
    c5 = {}
    for p in S5:
        if Permutation(list(p)).order() == 5:
            c5.setdefault(frozenset(tuple((Permutation(list(p)) ** k).array_form) for k in range(5)), p)

    def polygon(p, step):
        s = sig[p]
        out = set()
        for x in (i for i in range(6) if s[i] != i):
            y = x
            for _ in range(step):
                y = s[y]
            out.add(pairs.index(tuple(sorted((x, y)))))
        return frozenset(out)
    polygons = {polygon(p, k) for p in c5.values() for k in (1, 2)}
    Fp, Fm, pol = sp.zeros(10), sp.zeros(10), []
    for er in erased:
        v = Pc * next(y for y in C[:, [k for k in range(15) if k not in er]].T.nullspace()
                      if not (Pc * y).is_zero_matrix)
        e = (v.T * Curl * v)[0] / (v.T * v)[0]
        pol.append(e)
        if e > 0:
            Fp += v * v.T / (v.T * v)[0]
        else:
            Fm += v * v.T / (v.T * v)[0]
    Fi = [sum((Pc * lam(p) ** k for k in range(5)), sp.zeros(10)) / 5 for p in c5.values()]
    hs = lambda X, Y: (X.T * Y).trace()
    v_ = [(f - Pc / 3) for f in Fi]
    return {
        "the fifteen pair commutators C_ij = upper([A(h_i), A(h_j)]) have square 64 and C C^T = 160 P_cycle (160 = 12^2 x "
        "10/9), and S5 acts on the oriented pairs with C rho(p) = Lambda^2(p) C; on R^15 the cut projector B6^T B6/6 of K6, "
        "the bright C^T C/160 and the dark rest are orthogonal projectors of ranks 5, 6 and 4":
            all((C[:, k].T * C[:, k])[0] == 64 for k in range(15)) and C * C.T == 160 * Pc
            and all(C * rho(p) == lam(p) * C for p in S5)
            and all(P * P == P for P in (Pcut, Pbr, Pdk)) and [P.rank() for P in (Pcut, Pbr, Pdk)] == [5, 6, 4]
            and (Pcut * Pbr).is_zero_matrix and (Pcut * Pdk).is_zero_matrix and (Pbr * Pdk).is_zero_matrix,
        "every 11 of the 15 readings have rank 6, and of the 3003 sets of ten, 2991 have rank 6 and 12 rank 5: any four "
        "erasures are tolerated, and the twelve failing five-sets are exactly the pentagon and pentagram of each C5 on "
        "its five moving labels": r11 == Counter({6: 1365}) and r10 == Counter({6: 2991, 5: 12})
            and set(erased) == polygons and len(polygons) == 12,
        "each failure leaves one blind cycle line, of Curl-polarization +1 or -1, six each, and the two sums of their "
        "projectors are P_cycle +- Curl/5: J_H = (sqrt5/2)(F+ - F-), the Hodge star again, now from the erasures of an "
        "actual frame": Counter(pol) == Counter({1: 6, -1: 6}) and Fp == Pc + Curl / 5 and Fm == Pc - Curl / 5,
        "the six Sylow fixed planes of the cycles (the rotor plane of each C5) are equi-isoclinic: sum F_i = 2 P_cycle and "
        "F_i F_j F_i = F_i/5, and the centred (sqrt3/2)(F_i - P_cycle/3) have the Gram of the lines h_i/sqrt10 (1 and "
        "-1/5)": all(f * f == f and f.rank() == 2 for f in Fi) and sum(Fi, sp.zeros(10)) == 2 * Pc
            and all(Fi[i] * Fi[j] * Fi[i] == Fi[i] / 5 for i in range(6) for j in range(6) if i != j)
            and all(sp.Rational(3, 4) * hs(v_[i], v_[j]) == (1 if i == j else sp.Rational(-1, 5))
                    for i in range(6) for j in range(6)),
    }


def _odd_port():
    """The hub's odd S5 port (15:03): e_ij -> delta(alpha_ij) - delta(-alpha_ij) on the first A4, as a 240 x 10 matrix."""
    R10 = _wedge()[0]
    idx = {tuple(r): k for k, r in enumerate(R10)}
    e8 = np.eye(8, dtype=np.int64)
    Od = np.zeros((240, 10), dtype=np.int64)
    for k, (i, j) in enumerate(carrier.edges()):
        Od[idx[tuple(10 * (e8[i] - e8[j]))], k] += 1
        Od[idx[tuple(10 * (e8[j] - e8[i]))], k] -= 1
    return Od


def parity_ports():
    """The hub's text (15:03): the odd S5 port, its parity with the root-wedge port, and four root ports."""
    from sympy.polys.matrices import DomainMatrix
    R10, V, W, Bw, G, h, Hc = _wedge()
    Od = _odd_port()
    Bs = sp.Matrix(carrier.signed_incidence())
    Pc = sp.eye(10) - Bs.T * Bs / 5
    Cn = np.array(sp.Matrix.hstack(*Bs.nullspace()), dtype=np.int64)
    idx = {tuple(r): k for k, r in enumerate(R10)}
    mo = [Pc * sp.Matrix(Od.T.dot(Hc[n]).dot(Od)) * Pc / 2 for n in range(5)]
    clique, sites, TC, Fm = _two_ports()
    site, sign = _golden_sites()
    P = np.zeros((240, 24), dtype=np.int64)
    for k, t in enumerate(clique):
        P[idx[tuple(t)], k] = 1
    for e, (t, g) in enumerate(zip(site, sign)):
        P[idx[tuple(t)], 6:12] += g * Cn[e]
    P[:, 12:18], P[:, 18:24] = Bw @ Cn, Od @ Cn
    M = [sp.Matrix(P.T.dot(Hc[n]).dot(P)) for n in range(3)]
    ranks = [DomainMatrix.from_Matrix(sp.Matrix(sp.BlockMatrix([[M[i + j] for j in range(d + 1)] for i in range(d + 1)])))
             .rank() for d in range(2)]
    q = sp.symbols("q")
    me, mo_ = [1, 232, 54213, 12740592, 3008062816], [1, 242, 58691, 14259954, 3470101592]
    mix = [(1 - q) * a + q * b for a, b in zip(me, mo_)]
    Hq = sp.Poly(sp.expand(sp.Matrix(3, 3, lambda i, j: mix[i + j]).det()), q)
    dq = Hq.diff(q)
    return {
        "the odd S5 port T_O e_ij = (delta(alpha_ij) - delta(-alpha_ij))/sqrt2 on the first A4 is an isometry of the cycles "
        "with the triangle port's moments, 1, 242, 58691, 14259954, 3470101592 (variance 127): the S5 orbit of the "
        "triangle, scalar on the cycles": all(mo[n] == mo_[n] * Pc for n in range(5)),
        "the bath commutes with inversion, the root-wedge port is even (b_-rho = b_rho) and T_O is odd, so "
        "T_S* f(Delta) T_O = 0 for every f (checked for Delta^n, n <= 4)":
            all(not np.any(Bw.T.dot(Hc[n]).dot(Od)) for n in range(5)),
        "the clique, the Golden, the root-wedge and the odd port span 24 dimensions on the root shell, so by the root-shell "
        "theorem they grow by 24 at every order (24, 48 computed through degree 1); the hub certifies this by 24 x 24 "
        "Weyl-orbit determinants": sp.Matrix(P.T @ P).rank() == 24 and ranks == [24, 48],
        "S5 does not choose between the two: the mixtures sqrt(1 - q) T_S + sqrt(q) T_O have 3 x 3 Hankel determinant "
        "219823907 - 194728114 q - 84325288 q^2 + 75159768 q^3, decreasing on [0, 1] (its derivative is convex, -194728114 "
        "and -137899386 at the ends) to 15930273 > 0": Hq.all_coeffs()[::-1] == [219823907, -194728114, -84325288, 75159768]
            and Hq.eval(1) == 15930273 and dq.eval(0) == -194728114 and dq.eval(1) == -137899386 and dq.LC() > 0,
    }


@functools.lru_cache(maxsize=None)
def _norm_four():
    """The 2160 norm-four lattice sites (times 10), with their A4 + A4' label coordinates 10 v and 10 w."""
    pts = set()
    for i in range(8):
        for s in (20, -20):
            v = [0] * 8
            v[i] = s
            pts.add(tuple(v))
    for c in itertools.combinations(range(8), 4):
        for sg in itertools.product((10, -10), repeat=4):
            v = [0] * 8
            for k, s in zip(c, sg):
                v[k] = s
            pts.add(tuple(v))
    for i in range(8):
        for sg in itertools.product((5, -5), repeat=8):
            v = list(sg)
            v[i] *= 3
            if sum(v) % 20 == 0:
                pts.add(tuple(v))
    X = np.array(sorted(pts), dtype=np.int64)
    V4 = np.array([assignment.carrier_part(r)[:5] for r in X], dtype=np.int64)
    W4 = np.array([[int((r - assignment.carrier_part(r)) @ assignment.TWIN[k]) for k in range(5)] for r in X],
                  dtype=np.int64)
    assert not (W4 % 10).any()
    return X, V4, W4 // 10


def dark_port():
    """The hub's text (15:03): the dark four need the norm-four shell, and there they make a fifth port."""
    R10, V, W, Bw, G, h, Hc = _wedge()
    X, V4, W4 = _norm_four()
    H6, sig, S5, sgn, U = _six_lines()
    lab2 = {tuple(V[k]) + tuple(W[k]): k for k in range(240)}
    lab4 = {tuple(V4[k]) + tuple(W4[k]): k for k in range(len(X))}

    def fixed(p, Vx, Wx, lab):
        inv = list(np.argsort(p))
        return sum(1 for k in range(len(Vx)) if lab[tuple(Vx[k][inv]) + tuple(Wx[k][inv])] == k)
    chi = lambda p: sgn[p] * (sum(1 for i in range(5) if p[i] == i) - 1)
    mult = [sp.Rational(sum(fixed(p, Vx, Wx, lab) * chi(p) for p in S5), 120) for Vx, Wx, lab in ((V, W, lab2),
                                                                                                    (V4, W4, lab4))]
    k0 = lab4[(-12, -2, -2, 8, 8, 4, 4, -6, 4, -6)]
    sites = [lab4[tuple(V4[k0][list(np.argsort(p))]) + tuple(W4[k0][list(np.argsort(p))])] for p in S5]
    A = np.array([[sgn[p] * (5 * int(i == p[0]) - 1) for i in range(5)] for p in S5], dtype=np.int64)
    P5 = sp.eye(5) - sp.ones(5, 5) / 5
    Hn = _walk_entries()
    Y = X[sites]
    Hs = [np.array([[Hn(Y[j] - Y[i], n) for j in range(120)] for i in range(120)], dtype=object) for n in range(4)]
    Md = [sp.Matrix(A.T.dot(Hs[n]).dot(A)) / 600 for n in range(4)]
    md = [M_[0, 0] / P5[0, 0] for M_ in Md]
    cross = [np.array([[Hn(R10[j] - Y[i], n) for j in range(240)] for i in range(120)], dtype=object) for n in range(3)]
    rs = R10[int(np.argmax(R10 @ Y[0]))]
    top = all(Hn(Y[0] + n * rs - Y[i], n) == ((-1) ** n if i == 0 else 0)
              and all(Hn(Y[0] + n * rs - Y[i], j) == 0 for j in range(n)) for n in range(5) for i in range(120))
    pairs, C, rho, Pcut, Pbr, Pdk = _pairs15()
    rhoA = lambda p: sgn[p] * sp.Matrix(5, 5, lambda r, c: int(r == p[c]))
    seed = sp.zeros(5, 15)
    seed[0, 0] = 1
    K = sum((rhoA(p) * P5 * seed * rho(p).T for p in S5), sp.zeros(5, 15)) * Pdk
    return {
        "the A4 + A4' glue has 2160 norm-four sites, and in its label coordinates the diagonal S5 character sums give the "
        "dark four (A4 x sign, the commutator's kernel) multiplicity 0 on the 240 root sites and 36 on the norm-four "
        "shell: no S5 dark port lives on the roots": len(X) == 2160 and {int(x @ x) for x in X} == {400}
            and bool(((X @ R10.T) % 100 == 0).all()) and mult == [0, 36],
        "the site x0 = (-1, 0, 0, 1, 1, 0, 1, 0) (the hub's (-6, -1, -1, 4, 4; -2, -2, 3, -2, 3)/5, its twin read through "
        "the outer automorphism) has a free S5 orbit of 120 sites, and A_(sigma, i) = sgn(sigma)(5 delta_(i, sigma(0)) - 1) "
        "has A^T A = 600 P_A4: an isometric dark port A/sqrt600":
            list(X[k0]) == [-10, 0, 0, 10, 10, 0, 10, 0] and len(set(sites)) == 120 and sp.Matrix(A.T @ A) == 600 * P5,
        "its moments are scalar, 1, 975/4, 237985/4, 14539767 (variance 1315/16), and it is spectrally orthogonal to every "
        "root-supported port: Delta S5-equivariant and the dark four absent from the root module make T_D* f(Delta) "
        "vanish on all 240 root sites (checked for Delta^n, n <= 2)":
            md == [1, sp.Rational(975, 4), sp.Rational(237985, 4), 14539767] and all(Md[n] == md[n] * P5 for n in range(4))
            and md[2] - md[1] ** 2 == sp.Rational(1315, 16) and all(not np.any(A.T.dot(c)) for c in cross),
        "the root-shell argument holds on any sphere of sites: for s on it and r* a root maximizing <s, .>, the point "
        "s + n r* is reached in n steps only from s along r*, (Delta^n)_(s', s + n r*) = (-1)^n delta_(s s') with lower "
        "powers vanishing (checked on the 120 sites, n <= 4); so the dark port grows by 4 at every order, and with the "
        "four root ports, orthogonal to it, the five ports grow by 28 = 24 + 4": top,
        "the Reynolds average K of e_0 e_01^T over S5 (sign-twisted on A4) is the hub's intertwiner: entries -2, 0, 2, "
        "K rho(p) = sgn(p) p K, K^T K = 60 P_dark and K K^T = 60 P_A4; so D15 = [T_S C/sqrt160; A K/sqrt36000] has "
        "D15* D15 = P_bright + P_dark on the pair space, the cuts its kernel":
            set(K) == {-2, 0, 2} and all(K * rho(p) == rhoA(p) * K for p in S5) and K.T * K == 60 * Pdk
            and K * K.T == 60 * P5,
    }


def notes_1534():
    """The hub's text (15:03), the sibling's MODEL (14:27-15:11) and the U21 intake: the remaining exact items."""
    E, N5, sym, F, a0, b0 = _source()
    Bs = sp.Matrix(carrier.signed_incidence())
    Pc = sp.eye(10) - Bs.T * Bs / 5
    Nc = sp.Matrix.hstack(*Bs.nullspace())
    Pk = N5 * (N5.T * N5).inv() * N5.T
    S5 = list(itertools.permutations(range(5)))
    sgn = lambda p: Permutation(list(p)).signature()
    chd = lambda p: sgn(p) * (sum(1 for i in range(5) if p[i] == i) - 1)
    chc = {p: (Pc * compound2(sp.Matrix(5, 5, lambda r, c: int(r == p[c])))).trace() for p in S5}
    from sympy.combinatorics import PermutationGroup
    gen = lambda gens: [tuple(y.array_form) for y in PermutationGroup([Permutation(list(z)) for z in gens]).elements]
    g, d, r, c = (1, 2, 3, 4, 0), (0, 2, 4, 1, 3), (0, 4, 3, 2, 1), (1, 2, 0, 3, 4)
    groups = [S5, gen([g, (1, 2, 0, 3, 4), (1, 0, 2, 4, 3)]), gen([g, d]), gen([g, r]), gen([g])]
    hom = [sp.Rational(sum(chd(p) * chc[p] for p in grp), len(grp)) for grp in groups]
    T_ = _word_adapter()
    G = N5.T * N5
    a, b = T_[:, 0], T_[:, 1]
    adot, bdot = sp.Matrix([2, 0, -3, 4, 1]), sp.Matrix([1, 3, 0, -2, 2])
    Q = ((a.T * G * bdot)[0] - (b.T * G * adot)[0]) / 4
    xs = sp.symbols("x0:10")
    A_, B_ = sym(N5 * sp.Matrix(xs[:5])), sym(N5 * sp.Matrix(xs[5:]))
    S2 = A_ * A_ + B_ * B_
    U_, V_ = (A_ ** 3 + A_ * B_ ** 2).trace() / 6, (A_ ** 2 * B_ + B_ ** 3).trace() / 6
    rows = list(F(N5 * sp.Matrix(xs[:5]), N5 * sp.Matrix(xs[5:]))[4:, 0]) + [S2[0, 0] - S2[4, 4], S2[1, 1] - S2[4, 4],
                                                                            U_, V_]
    wit = dict(zip(xs, list(a) + list(b)))
    jn = sp.Matrix([[sp.diff(sp.expand(y), v) for v in xs] for y in rows]).subs(wit)
    uu, vv = sp.symbols("u0:6"), sp.symbols("v0:6")
    sub = dict(zip(xs, list(T_ * sp.Matrix(uu)) + list(T_ * sp.Matrix(vv))))
    rows_w = [sp.expand(y.subs(sub, simultaneous=True)) for y in rows] + [uu[0], vv[0]]
    jw = sp.Matrix([[sp.diff(y, v) for v in uu + vv] for y in rows_w]).subs(dict(zip(uu + vv, [1] + [0] * 6 + [1] + [0] * 4)))
    M = sp.Matrix(carrier.signless_incidence())
    Lsub = sp.diag(*([4] * 5 + [2] * 10)) - sp.BlockMatrix([[sp.zeros(5), M], [M.T, sp.zeros(10)]]).as_explicit()
    x = sp.symbols("x")
    s_, E_ = sp.symbols("s E", positive=True)
    return {
        "the dark-to-bright intertwiners step down the subgroups: dim Hom(dark four, cycles) = 0 for S5 and A5, 1 for "
        "F20, 2 for D10 and 4 for C5 (the hub and the sibling)": hom == [0, 0, 1, 2, 4] and [len(x_) for x_ in groups]
            == [120, 60, 20, 10, 5],
        "the hub's selected Lagrangian is invariant under the lane rotation (a, b) -> (cos a - sin b, sin a + cos b) "
        "because Dg (-b, a) = W(a ^ a - b ^ b) = 0, and its Noether charge (a^T G bdot - b^T G adot)/4 is -1/2 at the word "
        "preparation a = T e0, b = T e1 with velocities (2, 0, -3, 4, 1), (1, 3, 0, -2, 2), G = N^T N":
            Q == sp.Rational(-1, 2) and G == sp.Matrix([[4, 2, 2, 1, 3], [2, 4, 1, 2, 3], [2, 1, 4, 2, 3], [1, 2, 2, 4, 3],
                                                        [3, 3, 3, 3, 6]]),
        "there Z1 = (28 + 52i)/3, and six commutator readings, two contrasts and Re Z1, Im Z1 have native 10 x 10 "
        "determinant 2523136; with one word sign from each lane the 12 x 12 word determinant is -22708224":
            [sp.expand(U_).subs(wit), sp.expand(V_).subs(wit)] == [sp.Rational(28, 3), sp.Rational(52, 3)]
            and jn.det() == 2523136
            and jw.det() == -22708224,
        "the address clock 0 -> Z120 -> Z4320 -> Z36 -> 0 does not split: 36 (1 + 36k) = 0 mod 4320 would need "
        "1 + 36k = 0 mod 120, impossible as gcd(36, 120) = 12; Ext(Z36, Z120) = Z12 and the carry is a generator, order 12":
            all((36 * (1 + 36 * k)) % N for k in range(120)) and gcd(36, 120) == 12,
        "with spec Delta = [0, 256] proved, the root-wedge port's scalar resolvent g(s) = int dmu/(s + E), of mean 232, "
        "lies between 1/(s + 232) (Jensen) and the chord (3/32)/s + (29/32)/(s + 256): on [0, 256] the chord of "
        "1/(s + E) exceeds it by E (256 - E)/(s (s + 256)(s + E)) >= 0, and integrating it against the measure of mean 232 "
        "gives the weights (the sibling's conditional statement, now unconditional)":
            sp.simplify((1 - E_ / 256) / s_ + (E_ / 256) / (s_ + 256) - 1 / (s_ + E_)
                        - E_ * (256 - E_) / (s_ * (s_ + 256) * (s_ + E_))) == 0
            and (1 - sp.Rational(232, 256), sp.Rational(232, 256)) == (sp.Rational(3, 32), sp.Rational(29, 32))
            and all(band.edge().values()),
        "the subdivision graph of K5 (vertex-edge incidence, the U21 note's Maxwell map) has Laplacian spectrum 0, 1^4, "
        "2^5, 5^4, 6": sp.factor(Lsub.charpoly(x).as_expr()) == x * (x - 1) ** 4 * (x - 2) ** 5 * (x - 5) ** 4 * (x - 6),
    }

# ------------------------- 16:16: two dark ports, six F20 views, the coherent encoder and the bath's measures

def _shift_sum(field):
    """Delta = 240 - A on a finitely supported vector field {site (times 10): numpy vector}."""
    roots = [tuple(int(c) for c in r) for r in assignment.roots10()]
    out = {}
    for x, val in field.items():
        out[x] = out.get(x, 0) + 240 * val
        for r in roots:
            y = tuple(a + b for a, b in zip(x, r))
            out[y] = out.get(y, 0) - val
    return out


def _pairing(f, g):
    """sum over the sites of f(x) g(x)^T."""
    M = np.zeros((len(next(iter(f.values()))), len(next(iter(g.values())))), dtype=object)
    for x, v in f.items():
        if x in g:
            M = M + np.outer(v, g[x])
    return sp.Matrix(M)


@functools.lru_cache(maxsize=None)
def _two_dark():
    """The hub's two norm-four dark ports (16:11) as vector fields on the sites (times 10). D1 is the 15:34 port A on the
    orbit of x0 (five columns, A^T A = 600 P_A4). D2(x) = [X ^ Y ^ (5 X o Y - <X, Y> 1)]/625 has ten triple coordinates,
    with X = V4/2 and Y = -W4/2 the label blocks scaled by 5; it is even in Y, so the twin's sign drops out, and it is
    stored times 10^4."""
    X, V4, W4 = _norm_four()
    H6, sig, S5, sgn, U = _six_lines()
    lab4 = {tuple(V4[k]) + tuple(W4[k]): k for k in range(len(X))}
    k0 = lab4[(-12, -2, -2, 8, 8, 4, 4, -6, 4, -6)]
    D1 = {}
    for p in S5:
        inv = list(np.argsort(p))
        s = lab4[tuple(V4[k0][inv]) + tuple(W4[k0][inv])]
        D1[tuple(int(c) for c in X[s])] = np.array([sgn[p] * (5 * int(i == p[0]) - 1) for i in range(5)], dtype=object)
    det3 = lambda a, b, c: (a[0] * (b[1] * c[2] - b[2] * c[1]) - a[1] * (b[0] * c[2] - b[2] * c[0])
                            + a[2] * (b[0] * c[1] - b[1] * c[0]))
    D2 = {}
    for x, v, w in zip(X.tolist(), V4.tolist(), W4.tolist()):
        z = [5 * a * b - sum(p * q for p, q in zip(v, w)) for a, b in zip(v, w)]
        row = [det3(*[[u[i] for i in t] for u in (v, w, z)]) for t in itertools.combinations(range(5), 3)]
        if any(row):
            D2[tuple(x)] = np.array(row, dtype=object)
    return D1, D2


def two_dark():
    """The hub's text (16:11): a second norm-four dark port, its angle with the first, and thirty-two at every order."""
    X = _norm_four()[0]
    D1, D2 = _two_dark()
    L1, L2 = _shift_sum(D1), _shift_sum(D2)
    s = sp.Integer(10 ** 4)
    G2 = _pairing(D2, D2) / s ** 2
    M = [G2, _pairing(D2, L2) / s ** 2, _pairing(L2, L2) / s ** 2]
    m = [Mk.trace() / G2.trace() for Mk in M]
    N = [_pairing(D1, D1), _pairing(D1, L1), _pairing(L1, L1)]
    C = [_pairing(D1, D2) / s, _pairing(D1, L2) / s, _pairing(L1, L2) / s]
    Gp = G2 / 7200 ** 2
    P5 = sp.eye(5) - sp.ones(5, 5) / 5
    out = lambda Y: Y + Y.T
    R = [N[0] - C[0] * Gp * C[0].T] + [N[k] - out(C[k] * Gp * C[0].T) + C[0] * Gp * M[k] * Gp * C[0].T for k in (1, 2)]
    r = [Rk[0, 0] / R[0][0, 0] for Rk in R]
    return {
        "D2(x) = [X ^ Y ^ (5 X o Y - <X, Y> 1)]/625 on the label blocks of the norm-four sites (scaled by 5) is nonzero at "
        "1200 of the 2160, has rank 4 and Gram G2 with G2^2 = 7200 G2, and its moments are scalar: 1, 232, 54150, "
        "variance 326": len(D2) == 1200 and G2.rank() == 4 and G2 * G2 == 7200 * G2
            and all(M[k] == m[k] * G2 for k in range(3)) and m == [1, 232, 54150] and m[2] - m[1] ** 2 == 326,
        "with the first dark port D1 = A, C = D1^T D2 has C C^T = 112500 P_A4: four equal squared principal cosines "
        "112500/(600 x 7200) = 5/192, so the two span 8 dimensions. The mixed moments are D1^T Delta D2 = 232 C and "
        "D1^T Delta^2 D2 = 54150 C, and the part of D1 orthogonal to D2 has moments 45640/187 and 11152530/187, "
        "variance 2513510/34969": C[0] * C[0].T == 112500 * P5 and sp.Rational(112500, 600 * 7200) == sp.Rational(5, 192)
            and C[1] == 232 * C[0] and C[2] == 54150 * C[0] and all(R[k] == r[k] * R[0] for k in range(3))
            and r[1:] == [sp.Rational(45640, 187), sp.Rational(11152530, 187)]
            and r[2] - r[1] ** 2 == sp.Rational(2513510, 34969),
        "every norm-four site meets some root at inner product 2 and none above (<s, r> <= sqrt8 < 3). So on the shell "
        "the point s + n r* is reached in n steps only from s along r* (the 15:34 argument, now at every site), the "
        "eight dark columns grow by 8 at every order, and with the four root ports, orthogonal to them because the dark "
        "four are absent from the roots, the ports grow by 32(n + 1)":
            bool(((X @ assignment.roots10().T).max(axis=1) == 200).all()),
    }


@functools.lru_cache(maxsize=None)
def _mixers():
    """The hub's six F20 mixers (16:11). X_0 is half the Reynolds average of e_0 e_0^T over the stabilizer (an F20) of
    Sylow label 0, an F20-equivariant isometry of the dark four (A4 x sign) into the cycles, and
    X_sigma(i) = Lambda^2(sigma) X_i (sgn(sigma) sigma)^T. Returns X_0..X_5 and the rotor planes F_0..F_5 on the same
    labels."""
    H, sig, S5, sgn, U = _six_lines()
    Bs = sp.Matrix(carrier.signed_incidence())
    Pc = sp.eye(10) - Bs.T * Bs / 5
    P5 = sp.eye(5) - sp.ones(5, 5) / 5
    perm = lambda p: sp.Matrix(5, 5, lambda r, c: int(r == p[c]))
    lam = {p: compound2(perm(p)) for p in S5}
    seed = sp.zeros(10, 5)
    seed[0, 0] = 1
    X0 = sum((lam[p] * Pc * seed * P5 * perm(p).T * sgn[p] for p in S5 if sig[p][0] == 0), sp.zeros(10, 5)) / 2
    X = {}
    for p in S5:
        X.setdefault(sig[p][0], lam[p] * X0 * perm(p).T * sgn[p])
    c5 = {}
    for p in S5:
        if Permutation(list(p)).order() == 5:
            c5.setdefault(next(i for i in range(6) if sig[p][i] == i), p)
    F = [sum((Pc * lam[c5[i]] ** k for k in range(5)), sp.zeros(10)) / 5 for i in range(6)]
    return [X[i] for i in range(6)], F


def fusion_frame():
    """The hub's text (16:11): six F20 views of the dark four in the cycles, their graph projectors and the Schur
    response."""
    Xs, F = _mixers()
    H, sig, S5, sgn, U = _six_lines()
    Bs = sp.Matrix(carrier.signed_incidence())
    Pc = sp.eye(10) - Bs.T * Bs / 5
    P5 = sp.eye(5) - sp.ones(5, 5) / 5
    perm = lambda p: sp.Matrix(5, 5, lambda r, c: int(r == p[c]))
    t, a, b, q = sp.symbols("t a b q")
    Pi = [sp.Matrix(sp.BlockMatrix([[x * x.T, x], [x.T, P5]])) / 2 for x in Xs]
    PB, PD = sp.diag(Pc, sp.zeros(5)), sp.diag(sp.zeros(10), P5)
    view = lambda S: sum((Pi[i] for i in S), sp.zeros(15))
    ranks = Counter((k, view(S).rank()) for k in range(1, 7) for S in itertools.combinations(range(6), k))
    cub = t ** 3 - 5 * t ** 2 + sp.Rational(79, 10) * t - 4
    want = {4: (t - 2) * (t - 1) * (t ** 2 - 3 * t + 1) * cub ** 2,
            5: (t - 2) ** 2 * (t ** 2 - 4 * t + sp.Rational(7, 2)) ** 4, 6: (t - 2) ** 6 * (t - 3) ** 4}
    polys = all(sp.expand(sp.cancel(view(S).charpoly(t).as_expr() / t ** 5) - want[k]) == 0
                for k in (4, 5, 6) for S in itertools.combinations(range(6), k))
    det = {k: want[k].subs(t, 0) for k in want}
    itr = {k: -sp.diff(want[k], t).subs(t, 0) / det[k] for k in want}
    lam_ = 2 * q
    Dl = 1 + q * (a + b)
    X0 = Xs[0]
    G = a * PB + b * PD - q / Dl * sp.Matrix(sp.BlockMatrix([[a ** 2 * X0 * X0.T, a * b * X0], [a * b * X0.T, b ** 2 * P5]]))
    resp = ((PB / a + PD / b + lam_ * Pi[0]) * G - PB - PD).applyfunc(sp.cancel)
    cross = G[:10, 10:].subs({a: sp.Rational(1, 2), b: sp.Rational(1, 3), q: sp.Rational(1, 7)})
    return {
        "half the Reynolds average of e_0 e_0^T over the stabilizer F20 of a Sylow label is an F20-equivariant isometry "
        "X_0 of the dark four (A4 x sign) into the cycles; its S5 orbit X_0..X_5 is well defined, sums to zero, has "
        "X_i^T X_i = P_A4 and X_i X_i^T = P_cycle - F_i (the moving plane of the i-th rotor), and Frobenius Gram "
        "(24/5) delta_ij - 4/5": all(compound2(perm(p)) * Xs[i] * perm(p).T * sgn[p] == Xs[sig[p][i]] for p in S5 for i in range(6))
            and sum(Xs, sp.zeros(10, 5)).is_zero_matrix
            and all(x.T * x == P5 and x * x.T == Pc - f for x, f in zip(Xs, F))
            and all((Xs[i].T * Xs[j]).trace() == (4 if i == j else sp.Rational(-4, 5)) for i in range(6) for j in range(6)),
        "their graph projectors Pi_i = (1/2)[[X X^T, X], [X^T, I_D]] on the bright six plus dark four are rank-4 "
        "projectors with sum 2 P_bright + 3 P_dark and tr Pi_i Pi_j = 6/5; k views have rank 4, 7, 9, 10, 10, 10, so any "
        "four reconstruct the ten and any two whole views may be lost": all(P * P == P and P.rank() == 4 for P in Pi)
            and view(range(6)) == 2 * PB + 3 * PD
            and all((Pi[i] * Pi[j]).trace() == sp.Rational(6, 5) for i in range(6) for j in range(6) if i != j)
            and ranks == Counter({(1, 4): 6, (2, 7): 15, (3, 9): 20, (4, 10): 15, (5, 10): 6, (6, 10): 1}),
        "every four views have characteristic polynomial (t - 2)(t - 1)(t^2 - 3t + 1)(t^3 - 5t^2 + (79/10)t - 4)^2 on the "
        "ten, five views (t - 2)^2 (t^2 - 4t + 7/2)^4 and all six (t - 2)^6 (t - 3)^4: determinants 32, 2401/4 and 5184, "
        "inverse traces 169/20, 39/7 and 13/3 (the sixth view cuts the five-view error by 2/9), and since the cubic's "
        "three roots lie in (1, 5/2), the four-view condition number is phi^4 = (7 + 3 sqrt5)/2": polys
            and [det[k] for k in (4, 5, 6)] == [32, sp.Rational(2401, 4), 5184]
            and [itr[k] for k in (4, 5, 6)] == [sp.Rational(169, 20), sp.Rational(39, 7), sp.Rational(13, 3)]
            and (itr[5] - itr[6]) / itr[5] == sp.Rational(2, 9) and sp.Poly(cub, t).count_roots(1, sp.Rational(5, 2)) == 3
            and sp.simplify(((3 + sp.sqrt(5)) / (3 - sp.sqrt(5))) - (7 + 3 * sp.sqrt(5)) / 2) == 0,
        "with block responses a (bright) and b (dark), the retained response to H + lambda Pi_i is a P_B + b P_D - "
        "(q/Delta)[[a^2 X X^T, a b X], [a b X^T, b^2 I_D]] (Woodbury; q = lambda/2, Delta = 1 + q(a + b)), whose cross "
        "block is -X_i/47 at a = 1/2, b = 1/3, q = 1/7": resp.is_zero_matrix and cross == -X0 / 47,
    }


def source_coding():
    """The hub's text (16:11): the six Sylow lines as a coherent encoder of the source, and the Golden repair of the
    word lattice."""
    E, N5, sym, F, a0, b0 = _source()
    H, sig, S5, sgn, U = _six_lines()
    Hm = sp.Matrix.hstack(*H)
    G = N5.T * N5
    V = G.inv() * N5.T * Hm
    S = V.T * G
    T_ = _word_adapter()
    rest = lambda j: [i for i in range(6) if i != j]
    Sj = [S.extract(rest(j), list(range(5))) for j in range(6)]
    Fj = [V.extract(list(range(5)), rest(j)) * V.extract(list(range(5)), rest(j)).T * G for j in range(6)]
    ell = sp.Matrix([[1, 2, 2, 1, 2]])
    pairs = list(itertools.combinations(range(5), 2))
    lam2 = lambda Y: sp.Matrix(10, 10, lambda r, c: Y.extract(list(pairs[r]), list(pairs[c])).det())
    snf = lambda Y: [smith_normal_form(Y, domain=sp.ZZ)[k, k] for k in range(min(Y.shape))]
    anchor = sp.Matrix([[1, 0, 0, 0, 0, 0]])
    return {
        "in primitive source coordinates the six oriented Sylow lines are V = G^-1 N5^T H, with entries +-1 and Smith "
        "factors 1, 2, 2, 2, 2 (index 16), and S = V^T G encodes the source: V S = 12 I, S^T S = 12 G, and the six "
        "readings sum to zero": set(V) == {-1, 1} and N5 * V == Hm and snf(V) == [1, 2, 2, 2, 2]
            and V * S == 12 * sp.eye(5) and S.T * S == 12 * G and (sp.ones(1, 6) * S).is_zero_matrix,
        "any five readings invert: without line j the frame operator 12 I - v_j v_j^T G has eigenvalues 12, 12, 12, 12 "
        "and 2, |det S_-j| = 2592 for every j, and the ten pair coherences of five channels have "
        "|det Lambda^2 S_-j| = 2592^4 = 2^20 3^16": all(f.eigenvals() == {12: 4, 2: 1} for f in Fj)
            and all(abs(M.det()) == 2592 for M in Sj) and abs(lam2(Sj[0]).det()) == 2 ** 20 * 3 ** 16 == 2592 ** 4,
        "a six-word lane is read globally by the five readings S_-j T u and its anchor u0, with |det| 7776 for every j, "
        "so the twelve word coordinates of 980 and 086 have a global linear inverse of |det| 7776^2 = 6^10 = 60466176":
            all(abs(sp.Matrix.vstack(M * T_, anchor).det()) == 7776 for M in Sj) and 7776 ** 2 == 6 ** 10 == 60466176,
        "the word adapter T has index 3, with image ell(a) = a0 + 2a1 + 2a2 + a3 + 2a4 = 0 mod 3. Three of the six lines "
        "satisfy it and three do not, and V Z^6 + T Z^6 = Z^5, since the indices 16 and 3 are coprime. So the "
        "intersection has index 48, and each of the three blocked lines repairs the lane":
            all(x % 3 == 0 for x in ell * T_) and snf(T_) == [1, 1, 1, 1, 3]
            and sorted(int((ell * V)[i] % 3 == 0) for i in range(6)) == [0, 0, 0, 1, 1, 1]
            and snf(sp.Matrix.hstack(V, T_)) == [1] * 5
            and all(snf(sp.Matrix.hstack(T_, V[:, i])) == [1] * 5 for i in range(6) if (ell * V)[i] % 3),
        "a Golden line has A(h)^2 = 5 I - J and Tr A(h)^3 = 0, and its readings S v_i = H^T h_i are 10 on itself and -2 "
        "on the others: intensities 100 and 4, or 5/6 and 1/30 of the total 12 h^T h = 120 (per r^2 on its rotating "
        "orbit, where the 411 normalization has E = 10 r^2 and Q = 5 r^2: 12 E = 24 Q)":
            all(sym(h) ** 2 == 5 * sp.eye(5) - sp.ones(5, 5) and (sym(h) ** 3).trace() == 0 for h in H)
            and S * V == Hm.T * Hm == 12 * sp.eye(6) - 2 * sp.ones(6, 6)
            and (sp.Rational(100, 120), sp.Rational(4, 120)) == (sp.Rational(5, 6), sp.Rational(1, 30)),
    }


def k4_planes():
    """The sibling's MODEL (16:17): the five vertex deletions of K5 are commuting source planes that span the dark four."""
    E, N5, sym, F, a0, b0 = _source()
    H, sig, S5, sgn, U = _six_lines()
    planes = [N5 * sp.Matrix.hstack(*N5.extract([k for k, e in enumerate(E) if v in e], list(range(5))).nullspace())
              for v in range(5)]
    pairs = list(itertools.combinations(range(10), 2))
    wedge = lambda x, y: sp.Matrix([x[i] * y[j] - x[j] * y[i] for i, j in pairs])
    biv = [(-1) ** v * wedge(P[:, 0], P[:, 1]) for v, P in enumerate(planes)]
    gram = sp.Matrix(5, 5, lambda i, j: (biv[i].T * biv[j])[0])
    proj = [P * (P.T * P).inv() * P.T for P in planes]
    return {
        "deleting a vertex of K5 leaves a 2-plane of source vectors supported on its K4 (the differences of its three "
        "perfect matchings); inside each plane the commutator vanishes, so the five bivectors lie in the commutator's "
        "4-dimensional kernel, the dark four": all(P.shape[1] == 2 and P.rank() == 2 for P in planes)
            and all(F(P[:, 0], P[:, 1]).is_zero_matrix for P in planes),
        "with orientations (-1)^v their Gram is 15 I - 3 J, which kills the sum and is 15 on the rest: the five planes "
        "are the vertex simplex of the dark four, seen by a dark port and not by the six-port, and any four span it":
            gram == 15 * sp.eye(5) - 3 * sp.ones(5, 5) and gram.rank() == 4,
        "every golden line puts 2/5 of its squared length into every plane": all(
            (h.T * Q * h)[0] / (h.T * h)[0] == sp.Rational(2, 5) for h in H for Q in proj),
    }


def notes_1616():
    """The hub's text (16:11) and the sibling's MODEL (15:37-16:17): the remaining exact items."""
    E, N5, sym, F, a0, b0 = _source()
    Bs = sp.Matrix(carrier.signed_incidence())
    Nc = sp.Matrix.hstack(*Bs.nullspace())
    cyc = (Nc.T * Nc).inv() * Nc.T
    a, b = sp.Matrix([1, 0, 1, -1, 2]), sp.Matrix([0, 2, -1, 1, 0])
    A, B = sym(N5 * a), sym(N5 * b)
    phi = (((A ** 2 + B ** 2) * A).trace() / 6, ((A ** 2 + B ** 2) * B).trace() / 6)
    c, s = sp.symbols("c s")
    av, bv, uv, vv = [sp.Matrix(sp.symbols(f"{n}0:5")) for n in "abuv"]
    W = lambda x, y: cyc * F(N5 * x, N5 * y)
    C0, C1, C2 = W(av, bv), W(uv, bv) + W(av, vv), W(uv, vv)
    xs = W(av * c + uv * s / 2, bv * c + vv * s / 2)
    DC, CO, SI = C0 / 2 + C2 / 8, C0 / 2 - C2 / 8, C1 / 4
    var = list(av) + list(bv) + list(uv) + list(vv)
    pt = dict(zip(var, [1, 0, 1, -1, 2, 0, 2, -1, 1, 0, 1, 1, 0, 2, -1, 2, 0, 1, -1, 1]))
    J = [C.jacobian(var).subs(pt) for C in (C0, C1, C2)]
    ranks = [sp.Matrix.vstack(*J[:k]).rank() for k in (1, 2, 3)]
    full = sp.Matrix.vstack(*J, sp.Matrix([av[0], av[1], bv[0]]).jacobian(var).subs(pt)).rank()
    N = 4320
    f20 = {(pow(3457, k, N), 864 * j % N) for k in range(4) for j in range(5)}
    c20 = {(1, 216 * n % N) for n in range(20)}
    comp = lambda f, g: (f[0] * g[0] % N, (f[0] * g[1] + f[1]) % N)
    orbit = lambda x: frozenset((m * x + s) % N for m, s in f20)
    orbits = {orbit(x) for x in range(N)}
    fib = Counter(next(iter(o)) % 36 for o in orbits)
    o0 = sorted(orbit(0))
    stab = [f for f in f20 if (f[0] * o0[0] + f[1]) % N == o0[0]]
    marks = [(x, y) for x in o0 for y in o0 if x != y]
    free = all(sum(1 for f in f20 if ((f[0] * x + f[1]) % N, (f[0] * y + f[1]) % N) == (x, y)) == 1 for x, y in marks)
    X = _norm_four()[0]
    return {
        "the formed nonlinear return parent at its witness a = (1, 0, 1, -1, 2), b = (0, 2, -1, 1, 0) has "
        "phi = (Tr[(A^2 + B^2)A], Tr[(A^2 + B^2)B])/6 = (-122/3, -10/3), so at h = (1, 2) the source charge falls at 78 "
        "and the hidden charge rises at 78": phi == (sp.Rational(-122, 3), sp.Rational(-10, 3))
            and -(1 * phi[1] - 2 * phi[0]) == -78,
        "the free source a'' + 4a = 0 = b'' + 4b, with a(t) = a cos 2t + (u/2) sin 2t and b(t) likewise, emits the "
        "bilinear x = W(a(t) ^ b(t)) = cos^2(2t) C0 + cos(2t) sin(2t) C1/2 + sin^2(2t) C2/4 = DC + CO cos 4t + SI sin 4t "
        "(DC = C0/2 + C2/8, CO = C0/2 - C2/8, SI = C1/4): x''' + 16 x' = 0, x(0) = C0, x'(0) = C1, x''(0) = 2 C2 - 8 C0, "
        "and samples at 0, pi/8, pi/4 give (DC, CO, SI) with determinant 2. Its history ranks are 6, 12 and 17 on the "
        "twenty initial data (an SL2 left blind), and 20 with a0, a1 and b0 added":
            (xs - c ** 2 * C0 - c * s * C1 / 2 - s ** 2 * C2 / 4).expand().is_zero_matrix
            and (DC + CO - C0).expand().is_zero_matrix and (-16 * CO - 2 * C2 + 8 * C0).expand().is_zero_matrix
            and sp.Matrix([[1, 1, 0], [1, 0, 1], [1, -1, 0]]).det() == 2 and ranks == [6, 12, 17] and full == 20,
        "on the 4320 clock the golden tick 216 generates a cyclic C20 and 864 with x 3457 an affine F20 (3457 of order 4, "
        "nonabelian); they share only the five translations by 864. F20 has 864 orbits of five, 24 in each fibre of the "
        "36-address atlas, a point's stabilizer is C4, and F20 is regular on the 20 ordered marks, so no equivariant map "
        "sends a clock orbit to the marks": len(f20) == 20 and pow(3457, 2, N) != 1 and pow(3457, 4, N) == 1
            and all(comp(f, g) in f20 for f in f20 for g in f20) and comp((3457, 0), (1, 864)) != comp((1, 864), (3457, 0))
            and f20 & c20 == {(1, 864 * j % N) for j in range(5)} and len(orbits) == 864
            and {len(o) for o in orbits} == {5} and set(fib.values()) == {24} and len(stab) == 4 and free,
        "the norm-four shell has 1136 integer and 1024 half-integer sites and no root (the sibling's split)":
            int((X % 10 == 0).all(axis=1).sum()) == 1136 and int((X % 10 == 5).all(axis=1).sum()) == 1024,
    }


def free_chain():
    """Every port measure fills the band with an absolutely continuous, a.e. positive density; its chain tends to (128, 64).

    Fourier turns Delta into multiplication by eps(k) = 240 - Lambda(k) on L^2(T^8), so a site vector phi has the
    spectral measure mu_phi = eps_*(|phi^|^2 dk). eps is a nonconstant trigonometric polynomial. Its critical set is a
    proper analytic subset of the torus, of measure zero, so by the coarea formula mu_phi has the density
    w_phi(E) = (integral over {eps = E} of |phi^|^2/|grad eps|). The torus is connected and eps runs from 0 to the band
    edge 256, so for almost every E in [0, 256] (Sard) the level set is a nonempty compact hypersurface and the density
    of states rho = w_delta0 is positive there. If phi is finitely supported and nonzero, phi^ vanishes only on a null
    set. Were w_phi = 0 on a set Z of positive measure, phi^ would vanish on eps^-1(Z), of measure int_Z rho > 0. So
    w_phi > 0 almost everywhere on [0, 256], and Rakhmanov's theorem (Rakhmanov 1983; Denisov 2004) sends the Jacobi
    parameters of mu_phi to the free chain's: alpha_k -> 128 and beta_k -> 64^2. Every port vector is finitely supported.
    """
    R = glue.roots()
    v_star = np.pi * np.array([1, 1, 1, 1, 0, 0, 0, 0])
    hess = lambda k: (R.T * np.cos(R @ k)) @ R
    m = court.laplacian_moments(recurrence.load_walks(), 90)
    sec = court.sector_moments(m, 89)
    chains = {"return": court.chebyshev(m), "contrast": court.chebyshev(sec["V5 contrast"]),
              "uniform": court.chebyshev(sec["V1 uniform"])}
    beta = lambda a, b: Fraction(factorial(a - 1) * factorial(b - 1), factorial(a + b - 1))
    edge3 = court.chebyshev([256 ** n * beta(n + 4, 4) / beta(4, 4) for n in range(91)])
    first = [(c[0][0], c[1][0]) for c in (chains["contrast"], chains["uniform"])]
    return {
        "Fourier makes Delta multiplication by eps = 240 - Lambda, a nonconstant trigonometric polynomial with range "
        "exactly [0, 256]: eps(0) = 0, and the band edge (layer 8's theorem). Both edges are nondegenerate, with Hessian "
        "sum r r^T = 60 I at k = 0 and -4 I at the band-edge half-periods, so the density of states vanishes as E^3 and "
        "(256 - E)^3": band.lam(np.zeros(8)) == 240 and abs(band.lam(v_star) + 16) < 1e-12 and all(band.edge().values())
            and np.allclose(hess(np.zeros(8)), 60 * np.eye(8)) and np.allclose(hess(v_star), -4 * np.eye(8)),
        "so every site vector's spectral measure is absolutely continuous, and a nonzero finitely supported one (a site, "
        "any port vector) has density positive almost everywhere on all of [0, 256]. The clique's contrast and uniform "
        "sector measures are E rho/240 and (288 - E) rho/48. Their first Jacobi steps are the block eigenvalues 241 and "
        "235 and the memory variances 183 and 495": first == [(241, 183), (235, 495)],
        "the exact chains from W_0..W_90 (45 levels) lie inside the band, with 0 < alpha_k < 256 and 0 < beta_k < 128^2, "
        "and approach the free chain as Rakhmanov's theorem requires. beta_k increases throughout, and at the last level "
        "|alpha - 128| < 0.13 and 0 < 4096 - beta < 23 (the return chain: alpha_44 = 128.026, beta_45 = 4080.23)":
            all(fail is None and all(0 < x < 256 for x in al) and all(0 < y < 128 ** 2 for y in b2)
                and all(x < y for x, y in zip(b2, b2[1:])) and abs(al[-1] - 128) < Fraction(13, 100)
                and 0 < 4096 - b2[-1] < 23 for al, b2, fail in chains.values()),
        "the slow approach is the edges': the weight (E (256 - E))^3, with the same edge exponents, has beta_45 = 4080.44, "
        "within 1/4 of the return chain's": abs(edge3[1][44] - chains["return"][1][44]) < Fraction(1, 4),
    }


# ------------------- 16:51: the five dark planes, two rotating branches, and the response read at one frequency

def _planes():
    """The five K4 matching planes (16:47): E_r, the source vectors vanishing on the edges at vertex r, as 5 x 2 bases in
    primitive source coordinates (sympy's nullspace basis, Gram [[4, 2], [2, 4]])."""
    E, N5, sym, F, a0, b0 = _source()
    return [sp.Matrix.hstack(*N5.extract([k for k, e in enumerate(E) if v in e], list(range(5))).nullspace())
            for v in range(5)]


def _lagrange(u, v, G):
    """A Lagrange-reduced basis of the plane lattice Z u + Z v under the metric G: its norms are the two minima."""
    n = lambda x: (x.T * G * x)[0]
    while True:
        if n(v) < n(u):
            u, v = v, u
        k = sp.floor((u.T * G * v)[0] / n(u) + sp.Rational(1, 2))
        if k == 0:
            return u, v
        v = v - k * u


def k4_complete():
    """The hub's text (16:47): the five K4 matching planes are all of the commutator's dark planes, and their geometry."""
    E, N5, sym, F, a0, b0 = _source()
    H, sig, S5, sgn, U = _six_lines()
    G = N5.T * N5
    Ur = _planes()
    P = [u * (u.T * G * u).inv() * u.T * G for u in Ur]
    V = G.inv() * N5.T * sp.Matrix.hstack(*H)
    Rj = [V[:, j] * V[:, j].T * G / (V[:, j].T * G * V[:, j])[0] for j in range(6)]
    act = lambda p: G.inv() * N5.T * _edge_perm(p) * N5
    klein = lambda r: [p for p in S5 if p[r] == r and Permutation(list(p)).order() == 2
                       and all(p[i] != i for i in range(5) if i != r)]
    pairs = list(itertools.combinations(range(5), 2))
    wedge = lambda x, y: sp.Matrix([x[i] * y[j] - x[j] * y[i] for i, j in pairs])
    Hm = sp.Matrix(10, 10, lambda r, c: G.extract(list(pairs[r]), list(pairs[c])).det())
    W = sp.Matrix.hstack(*[F(N5[:, i], N5[:, j]) for i, j in pairs])
    K = W.nullspace()
    t = sp.symbols("t0:4")
    b = sum((t[k] * K[k] for k in range(4)), sp.zeros(10, 1))
    c = lambda i, j: b[pairs.index((i, j))] if i < j else -b[pairs.index((j, i))]
    quad = [sp.expand(c(i, j) * c(k, l) - c(i, k) * c(j, l) + c(i, l) * c(j, k))
            for i, j, k, l in itertools.combinations(range(5), 4)]
    pts = set()
    for s in sp.solve(quad, t, dict=True):
        v = [sp.sympify(s.get(x, x)).subs({f: 1 for f in t if f not in s}) for x in t]
        lead = next(z for z in v if z != 0)
        pts.add(tuple(z / lead for z in v))
    jac = sp.Matrix(quad).jacobian(t)
    Km = sp.Matrix.hstack(*K)
    p = [(-1) ** r * wedge(u[:, 0], u[:, 1]) for r, u in enumerate(Ur)]
    cls = set()
    for x in p:
        y = list((Km.T * Km).inv() * Km.T * x)
        cls.add(tuple(z / next(w for w in y if w != 0) for z in y))
    gram = sp.Matrix(5, 5, lambda i, j: (p[i].T * Hm * p[j])[0])
    S = sum((x * x.T * Hm for x in p), sp.zeros(10))
    L = [sum(2 ** r * (p[r].T * Hm * p[s])[0] for r in range(5)) for s in range(5)]
    tags = sorted(L + [-x for x in L])
    lam_ = sp.symbols("lam")
    spec = set()
    for u in Ur:
        comp = (u.T * G).nullspace()
        tang = [wedge(n, u[:, 1]) for n in comp] + [wedge(u[:, 0], n) for n in comp]
        M = sp.Matrix(6, 6, lambda i, j: (tang[i].T * Hm * tang[j])[0])
        J = W * sp.Matrix.hstack(*tang)
        spec.add(sp.expand(sp.cancel((J.T * J - lam_ * M).det() / M.det())))
    ell = sp.Matrix([[1, 2, 2, 1, 2]])
    minima = []
    for u in Ur:
        l0, l1 = (ell * u[:, 0])[0] % 3, (ell * u[:, 1])[0] % 3
        B = (u[:, 0] + ((-l0 * pow(int(l1), -1, 3)) % 3) * u[:, 1], 3 * u[:, 1]) if l1 else (3 * u[:, 0], u[:, 1])
        x, y = _lagrange(B[0], B[1], G)
        minima.append(((x.T * G * x)[0], (y.T * G * y)[0], (sp.Matrix.hstack(*B).T * G * sp.Matrix.hstack(*B)).det()))
    return {
        "deleting vertex r leaves the 2-plane E_r of matching differences, the fixed source space of the Klein four "
        "group on the other four vertices; the five G-projectors have sum 2 I and P_r P_s P_r = P_r/4, so any two planes "
        "meet at both principal angles 60 degrees, and Tr(P_r R_j) = 2/5 against each of the six Golden lines":
            all(len(sp.Matrix.vstack(*[act(q) - sp.eye(5) for q in klein(r)]).nullspace()) == 2
                and all((act(q) * u - u).is_zero_matrix for q in klein(r)) for r, u in enumerate(Ur))
            and all(len(klein(r)) == 3 for r in range(5)) and sum(P, sp.zeros(5)) == 2 * sp.eye(5)
            and all(P[r] * P[s] * P[r] == P[r] / 4 for r in range(5) for s in range(5) if r != s)
            and all((Pr * R).trace() == sp.Rational(2, 5) for Pr in P for R in Rj),
        "on the commutator's 4-dimensional kernel in Lambda^2 of the source the five Pluecker quadrics have exactly five "
        "projective solutions, each reduced (Jacobian rank 3), and they are the five planes: W_AS(a ^ b) = 0 only for "
        "collinear a, b or for a pair spanning one E_r": len(K) == 4 and len(pts) == 5
            and all(jac.subs(dict(zip(t, q))).rank() == 3 for q in pts) and cls == pts,
        "oriented by (-1)^r the planes' bivectors sum to zero and S5 moves them by p_r -> sgn(sigma) p_sigma(r); their "
        "H-Gram is 15 delta - 3 and sum p_r p_r^T H = 15 P_dark, so any four recover the dark four (eigenvalues 15, 15, 15, "
        "3), and the marked scalar L = sum 2^r <p_r, .> tags the ten oriented planes by +-(15 2^s - 93): -78, -63, -33, "
        "27, 147, at least 6 apart": sum(p, sp.zeros(10, 1)).is_zero_matrix
            and all(compound2(act(q)) * p[r] == sgn[q] * p[q[r]] for q in S5 for r in range(5))
            and gram == 15 * sp.eye(5) - 3 * sp.ones(5, 5) and S * S == 15 * S and S.rank() == 4
            and sorted((15 * sp.eye(4) - 3 * sp.ones(4, 4)).eigenvals().items()) == [(3, 1), (15, 3)]
            and L == [-78, -63, -33, 27, 147] and min(y - x for x, y in zip(tags, tags[1:])) == 6,
        "at each plane the commutator's derivative on the six Grassmann tangent wedges has generalized spectrum "
        "(lambda - 2/3)^3 (lambda - 10/9)^3 against their H-Gram: every dark plane is a regular zero (condition number "
        "sqrt(5/3)), so the oriented unit planes near the ten zeros have exactly ten inverse branches":
            spec == {sp.expand((lam_ - sp.Rational(2, 3)) ** 3 * (lam_ - sp.Rational(10, 9)) ** 3)},
        "the word lattice (ell = a0 + 2a1 + 2a2 + a3 + 2a4 = 0 mod 3) meets each plane in index 3 (det 108; ell does not "
        "vanish on any E_r mod 3): its two minima are 12 and 12 on two planes and 4 and 28 on the other three, so the "
        "cheapest prepared rotor z = e^(2it)(a + ib) has energy |a|^2 + |b|^2 = 24 or 32 and charge 12 or 16":
            sorted(minima) == [(4, 28, 108)] * 3 + [(12, 12, 108)] * 2
            and all((ell * u).applyfunc(lambda z: z % 3) != sp.zeros(1, 2) for u in Ur),
    }


def dark_branches():
    """The hub's text (16:47): the finite return parent keeps the dark planes, and its proportional line rotates on two
    branches."""
    E, N5, sym, F, a0, b0 = _source()
    G = N5.T * N5
    av, bv = sp.Matrix(sp.symbols("a0:5")), sp.Matrix(sp.symbols("b0:5"))
    A, B = sym(N5 * av), sym(N5 * bv)
    phi = sp.Matrix([((A ** 2 + B ** 2) * A).trace() / 6, ((A ** 2 + B ** 2) * B).trace() / 6]).applyfunc(sp.expand)
    Ja, Jb = phi.jacobian(list(av)), phi.jacobian(list(bv))
    at = lambda a, b: dict(zip(list(av) + list(bv), list(a) + list(b)))

    def residual(a, b, h, X):
        """The finite parent's equations G a'' = -4 G a + (d_a phi)^T (h - phi), likewise b, h'' = phi - 10 h, on a
        rotating ansatz with a'' = -X a, b'' = -X b, h'' = -X h."""
        s = at(a, b)
        f = h - phi.subs(s)
        out = [(4 - X) * G * a - Ja.subs(s).T * f, (4 - X) * G * b - Jb.subs(s).T * f, (10 - X) * h - phi.subs(s)]
        return all(r.applyfunc(sp.simplify).is_zero_matrix for r in out)
    e = sp.Matrix([-3 if (i, j) == (0, 1) else (1 if (i < 2) != (j < 2) else -1) for i, j in E])
    u = G.inv() * N5.T * e
    s23 = [p for p in itertools.permutations(range(5)) if set(p[:2]) == {0, 1}]
    r = sp.Rational(1, 2)
    phases = [(1, 0), (sp.Rational(3, 5), sp.Rational(4, 5)), (0, 1)]
    branch = {X: all(residual(r * c * u, r * s_ * u, h * sp.Matrix([c, s_]), X) for c, s_ in phases)
              for X, h in ((6, sp.Rational(-1, 2)), (sp.Rational(32, 3), 3))}
    k, X = sp.symbols("k X", positive=True)
    P = X ** 2 - (14 + k) * X + 40 + 9 * k
    nrg = lambda X_, s_: (X_ * (r ** 2 * 18 + s_ ** 2) / 2 + 2 * r ** 2 * 18 + sp.Rational(9, 2) * s_ ** 2
                          + (s_ + 16 * r ** 3) ** 2 / 2)
    chg = lambda X_, s_: sp.sqrt(X_) * (r ** 2 * 18 + s_ ** 2)
    U4 = _planes()[4]
    u1, u2 = U4[:, 0], U4[:, 1]
    rho = sp.symbols("rho", positive=True)
    pk = phi.subs(at(rho * u1, rho * u2))
    Hk = (rho ** 2 * 4 + rho ** 2 * 4) / 2 + 2 * (4 + 4) * rho ** 2 + (pk.T * pk)[0] / 2
    blind = (u1, (u1 - 2 * u2) / sp.sqrt(3))
    Pl = U4 * (U4.T * G * U4).inv() * U4.T * G
    s = at(u1 + 2 * u2, 3 * u1 - u2)
    return {
        "on its proportional line u (the S2 x S3-fixed source: -3 on edge 01, +1 across, -1 within {2, 3, 4}; |u|^2 = 18, "
        "Tr A(u)^3/6 = -16) the finite return parent has two rotating branches, a = r cos(wt) u, b = r sin(wt) u, "
        "h = s (cos wt, sin wt), with X = w^2 on X^2 - (14 + k) X + 40 + 9k = 0 (k = 128 r^4/3): P(4) = 5k, P(9) = -5 and "
        "P(10) = -k put one root in (4, 9) and one above 10 for every r > 0": (N5 * u - e).is_zero_matrix
            and all((G.inv() * N5.T * _edge_perm(p) * N5 * u - u).is_zero_matrix for p in s23)
            and (u.T * G * u)[0] == 18 and (sym(N5 * u) ** 3).trace() / 6 == -16
            and [sp.expand(P.subs(X, x)) for x in (4, 9, 10)] == [5 * k, -5, -k],
        "at r = 1/2 both branches solve the full ten source and two hidden equations at three phases: the lower X = 6, "
        "s = -1/2 with energy 51/2 and charge (19/4) sqrt6, and the upper X = 32/3, s = 3 with energy 134 and charge "
        "18 sqrt6": all(branch.values())
            and sp.solve(P.subs(k, sp.Rational(8, 3)), X) == [6, sp.Rational(32, 3)]
            and [nrg(6, sp.Rational(-1, 2)), nrg(sp.Rational(32, 3), 3)] == [sp.Rational(51, 2), 134]
            and sp.simplify(chg(6, sp.Rational(-1, 2)) - sp.Rational(19, 4) * sp.sqrt(6)) == 0
            and sp.simplify(chg(sp.Rational(32, 3), 3) - 18 * sp.sqrt(6)) == 0,
        "the parent's force keeps every matching plane, so each E_r carries a 12-dimensional all-time commutator-dark "
        "phase space; two matching differences of norm 4 with a' = b, b' = -a give phi = (-4/3, -4/3), energy "
        "20 rho^2 + (16/9) rho^6 = (5/2)|Q| + |Q|^3/288 for Q = -8 rho^2, and the orthogonal pair a = u1, "
        "b = (u1 - 2 u2)/sqrt3 has phi = 0 and the exact circular orbit e^(2it)(a + ib), energy 32 and charge 16, blind to "
        "W and h": all((Pl * G.inv() * Jx.subs(s).T * w - G.inv() * Jx.subs(s).T * w).is_zero_matrix
                       for Jx in (Ja, Jb) for w in (sp.Matrix([1, 0]), sp.Matrix([0, 1])))
            and pk == sp.Matrix([-sp.Rational(4, 3), -sp.Rational(4, 3)]) * rho ** 3
            and sp.expand(Hk - 20 * rho ** 2 - sp.Rational(16, 9) * rho ** 6) == 0
            and sp.expand(sp.Rational(5, 2) * 8 * rho ** 2 + (8 * rho ** 2) ** 3 / 288 - Hk) == 0
            and phi.subs(at(*blind)).applyfunc(sp.simplify).is_zero_matrix
            and residual(blind[0], blind[1], sp.zeros(2, 1), 4)
            and [sp.simplify((x.T * G * x)[0]) for x in blind] == [4, 4] and sp.simplify((blind[0].T * G * blind[1])[0]) == 0
            and ((4 * 4 + 4 * 4) / 2 + 2 * (4 + 4), 2 * (4 + 4)) == (32, 16),
    }


def tomography():
    """The hub's text (16:47): the anchored F20 interaction read back from one complete response, the scalar shift's
    blind direction, and the above-band modes of the two-pole emulators."""
    Xs, F = _mixers()
    Bs = sp.Matrix(carrier.signed_incidence())
    Pc = sp.eye(10) - Bs.T * Bs / 5
    P5 = sp.eye(5) - sp.ones(5, 5) / 5
    PB, PD = sp.diag(Pc, sp.zeros(5)), sp.diag(sp.zeros(10), P5)
    q, a, b = sp.Rational(1, 7), sp.Rational(1, 2), sp.Rational(1, 3)
    X = Xs[0] + 2 * Xs[1]
    Uq = sp.Matrix.vstack(X, P5)
    K = PB / a + PD / b + q * Uq * Uq.T
    Gm = (K + sp.eye(15) - PB - PD).inv() - (sp.eye(15) - PB - PD)
    Kr = (Gm + sp.eye(15) - PB - PD).inv() - (sp.eye(15) - PB - PD)
    A_, C_, D_ = Kr[:10, :10], Kr[:10, 10:], Kr[10:, 10:]
    bright = sorted(e for e, k in A_.eigenvals().items() for _ in range(k) if e != 0)
    ell = bright[0]
    Rm = A_ - ell * Pc
    q_ = (C_ * C_.T).trace() / Rm.trace()
    m = D_.trace() / 4
    G0 = a * PB + b * PD
    dG = G0 - Gm
    sch = dG[10:, 10:] + sp.eye(15)[10:, 10:] - P5
    mean = sum((((PB / a + PD / b + q * sp.Matrix.vstack(x, P5) * sp.Matrix.vstack(x, P5).T + sp.eye(15) - PB - PD).inv()
                 - (sp.eye(15) - PB - PD)) for x in Xs), sp.zeros(15)) / 6
    t = sp.symbols("t")
    Y = Xs[0] + 2 * Xs[1] - Xs[2] + 3 * Xs[4]
    Q = Y.T * Y
    cp = sp.Poly(sp.cancel(Q.charpoly(t).as_expr() / t), t)
    pw = [(Q ** k).trace() for k in range(1, 5)]
    Jp = sp.Matrix(4, 5, lambda k, i: (k + 1) * (Q ** k * (Xs[i].T * Y + Y.T * Xs[i])).trace())
    ker = Jp.nullspace()[0]
    ker = ker / ker[4] * 41885
    c0, d = 1 + q * b, q * a
    Dy = d ** 4 * cp.as_expr().subs(t, -c0 / d)
    e1 = -cp.all_coeffs()[1]
    coef2 = -q * (4 * sp.Rational(975, 4) + 232 * e1) - q ** 2 / 2 * (4 + 2 * e1 + pw[1])
    alb = court.chebyshev([1, 232, 54213, 12740592])[0][1]
    ald = court.chebyshev([1, sp.Rational(975, 4), sp.Rational(237985, 4), 14539767])[0][1]
    edge = lambda m1, var, al: (256 - al) / ((256 - m1) * (256 - al) - var)
    Ab, Bd = edge(232, 389, alb), edge(sp.Rational(975, 4), sp.Rational(1315, 16), ald)
    above = [cp.count_roots((1 / qq - Bd) / Ab, sp.oo) for qq in (sp.Rational(1, 7), 1, 2, 5)]
    return {
        "for the anchored interaction q [X; I][X^T, I] with block responses a and b, the complete retained response "
        "G^-1 = [[A, C], [C^T, D]] gives the model back at one frequency: ell = min spec A = 1/a, q = Tr CC^T/Tr(A - ell), "
        "X = C/q, b = 1/(Tr D/4 - q). For X = X0 + 2X1 (singular squares 9, 1, 17/5, 17/5) the bright inverse spectrum is "
        "2, 2, 15/7, 87/35, 87/35, 23/7 and the read-back is q = 1/7, a = 1/2, b = 1/3":
            sorted(e for e, k in (X.T * X).eigenvals().items() for _ in range(k)) == [0, 1, sp.Rational(17, 5),
                                                                                       sp.Rational(17, 5), 9]
            and bright == [2, 2, sp.Rational(15, 7), sp.Rational(87, 35), sp.Rational(87, 35), sp.Rational(23, 7)]
            and (ell, q_, C_ / q_ == X, 1 / (m - q_)) == (2, q, True, b),
        "the decrement G0 - G has its bright block G_BD (dG_DD)^-1 G_DB (rank 4, coupling-free), the first moments shift "
        "by q U U^T so that 4 Tr dM1_B/Tr dM1_D = |X|^2 = 84/5, and the six views averaged give (45/94) I_B + (15/47) I_D, "
        "inverse residual (4/45, 2/15), a forgotten context adding (8 q^2/9) I_B + q^2 I_D":
            (dG[:10, :10] - Gm[:10, 10:] * sch.inv() * Gm[10:, :10]).applyfunc(sp.simplify).is_zero_matrix
            and 4 * (q * X * X.T).trace() / (4 * q) == sp.Rational(84, 5) == (X.T * X).trace()
            and mean == sp.Rational(45, 94) * PB + sp.Rational(15, 47) * PD
            and [sp.Rational(94, 45) - 2, sp.Rational(47, 15) - 3] == [sp.Rational(4, 45), sp.Rational(2, 15)]
            and [(2 * q) ** 2 * (sp.Rational(1, 3) - sp.Rational(1, 9)), (2 * q) ** 2 * (sp.Rational(1, 2) - sp.Rational(1, 4))]
            == [8 * q ** 2 / 9, q ** 2],
        "the scalar perturbation determinant prod_j [1 + q(b + mu_j a)] sees only the four singular squares: for "
        "X0 + 2X1 - X2 + 3X4 they solve 25t^4 - 1300t^3 + 19140t^2 - 102560t + 162176 (power traces 52, 5864/5, "
        "167408/5, 25763104/25), and the traces' 4 x 5 Jacobian has rank 4 with minor -3201739259904/625 and kernel "
        "(30595, -225, 55235, -6812, 41885), a one-parameter isospectral family. At q = 1/7, a = 1/2, b = 1/3 the "
        "determinant is 55899556/4862025, and log D = 8/s - (459567/245)/s^2 + ... from the moments 232 and 975/4":
            sp.Poly(25 * cp.as_expr(), t) == sp.Poly(25 * t ** 4 - 1300 * t ** 3 + 19140 * t ** 2 - 102560 * t + 162176, t)
            and pw == [52, sp.Rational(5864, 5), sp.Rational(167408, 5), sp.Rational(25763104, 25)]
            and Jp.rank() == 4 and Jp[:, :4].det() == sp.Rational(-3201739259904, 625)
            and list(ker) == [30595, -225, 55235, -6812, 41885] and Dy == sp.Rational(55899556, 4862025)
            and q * (4 + e1) == 8 and coef2 == sp.Rational(-459567, 245),
        "the two-pole emulators of the bright and dark moments have hidden diagonals 72928/389 and 1121463/5260 and edge "
        "responses 26656/488423 and 225097/2325132 at 256, so q[B + mu_j A] > 1 counts 0, 1, 3 and 4 emulator modes above "
        "the band at q = 1/7, 1, 2, 5 (the infinite E8 thresholds stay uncomputed)":
            (alb, ald) == (sp.Rational(72928, 389), sp.Rational(1121463, 5260))
            and (Ab, Bd) == (sp.Rational(26656, 488423), sp.Rational(225097, 2325132)) and above == [0, 1, 3, 4],
    }


def notes_1651():
    """The hub's text (16:47) and the sibling's MODEL (16:19-16:58): the remaining exact items."""
    x, y, r, th = sp.symbols("x y r theta", real=True)
    Ax, Ay = -y / (1 + x ** 2 + y ** 2), x / (1 + x ** 2 + y ** 2)
    curv = sp.simplify(sp.diff(Ay, x) - sp.diff(Ax, y))
    flux = sp.integrate(sp.integrate((2 / (1 + r ** 2) ** 2) * r, (r, 0, sp.oo)), (th, 0, 2 * sp.pi))
    hol = sp.integrate((Ax * sp.diff(sp.cos(th), th) + Ay * sp.diff(sp.sin(th), th)).subs({x: sp.cos(th), y: sp.sin(th)}),
                       (th, 0, 2 * sp.pi))
    N = 4320
    lab = lambda j: 4 * j % 5
    cells = Counter((j % 36, lab(j)) for j in range(N))
    F_ = sp.Matrix([[1, 1], [1, 0]])
    cyc = {frozenset(frozenset((c[i], c[(i + 1) % 5])) for i in range(5)) for c in
           ((0,) + p for p in itertools.permutations(range(1, 5)))}
    R2 = 2 * glue.roots()
    grade = Counter(int(round(v[:5].sum())) % 5 for v in R2)
    return {
        "a complexified dark plane carries the Fubini-Study connection A = (-y dx + x dy)/(1 + x^2 + y^2): curvature "
        "2/(1 + x^2 + y^2)^2, flux 2 pi and unit-circle holonomy pi, a source phase bundle that stays commutator-dark":
            sp.simplify(curv - 2 / (1 + x ** 2 + y ** 2) ** 2) == 0 and flux == 2 * sp.pi and sp.simplify(hol - sp.pi) == 0,
        "the clock labels the planes by p(j) = 4j mod 5: the 864 translation moves p by 1 and the 3457 multiplication "
        "doubles it, both keep j mod 36, and each of the 180 address-plane pairs has exactly 24 clock frames":
            all(lab(j + 864) == (lab(j) + 1) % 5 and lab(3457 * j % N) == 2 * lab(j) % 5 for j in range(N))
            and all((j + 864) % 36 == j % 36 == 3457 * j % N % 36 for j in range(N))
            and len(cells) == 180 and set(cells.values()) == {24},
        "the sibling's checkable numbers hold: K5 has 12 five-cycles; -22708224 = -9 x 2523136; 14539767 = 3 x 11 x 593 "
        "x 743; F = [[1, 1], [1, 0]] has F^2 = F + I, F^6 = [[13, 8], [8, 5]] and traces 7, 11, 18 at powers 4, 5, 6; and "
        "the mod-5 sums of the first five doubled root coordinates split the roots 40, 50, 50, 50, 50":
            len(cyc) == 12 and -9 * 2523136 == -22708224 and 3 * 11 * 593 * 743 == 14539767
            and F_ ** 2 == F_ + sp.eye(2) and F_ ** 6 == sp.Matrix([[13, 8], [8, 5]])
            and [(F_ ** k).trace() for k in (4, 5, 6)] == [7, 11, 18] and sorted(grade.values()) == [40, 50, 50, 50, 50],
    }


# ------------------------ 17:31: the source's quadratics, the dark readout, cubic-null triangles, the Fibonacci bridge

def _connected_nonbipartite(edges):
    """True if the graph on the five vertices with these edges is connected and not bipartite."""
    adj = {v: [] for v in range(5)}
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    col, stack, odd = {0: 0}, [0], False
    while stack:
        v = stack.pop()
        for w in adj[v]:
            if w not in col:
                col[w] = 1 - col[v]
                stack.append(w)
            elif col[w] == col[v]:
                odd = True
    return len(col) == 5 and odd


def quadratic_frames():
    """The hub's text (17:26): the edge and Golden projectors complete the source's quadratics, through the K5 matroid."""
    E, N5, sym, F, a0, b0 = _source()
    H, sig, S5, sgn, U = _six_lines()
    G = N5.T * N5
    I5 = sp.eye(5)
    V = G.inv() * N5.T * sp.Matrix.hstack(*H)
    Ee = [u * u.T * G / (u.T * G * u)[0] for u in (G.inv() * N5[e, :].T for e in range(10))]
    R = [V[:, j] * V[:, j].T * G / (V[:, j].T * G * V[:, j])[0] for j in range(6)]
    vec = lambda X: sp.Matrix(list(X))
    cE = sp.Matrix.hstack(*[vec(x - I5 / 5) for x in Ee])
    cR = sp.Matrix.hstack(*[vec(x - I5 / 5) for x in R])
    zs = lambda xs: sum(xs, sp.zeros(5))

    def recon(X):
        t = X.trace()
        return (t / 5 * I5 + sp.Rational(9, 8) * zs([((x * X).trace() - t / 5) * (x - I5 / 5) for x in Ee])
                + sp.Rational(25, 24) * zs([((r * X).trace() - t / 5) * (r - I5 / 5) for r in R]))

    def norm(X):
        t = X.trace()
        return (((X - t * I5 / 5) ** 2).trace(), sp.Rational(9, 8) * sum(((x * X).trace() - t / 5) ** 2 for x in Ee)
                + sp.Rational(25, 24) * sum(((r * X).trace() - t / 5) ** 2 for r in R))
    basis = []
    for i in range(5):
        for j in range(i, 5):
            Sm = sp.zeros(5)
            Sm[i, j] = Sm[j, i] = 1
            basis.append(G.inv() * Sm)
    Em = sp.Matrix.hstack(*[vec(x) for x in Ee])
    planes = []
    for r, u in enumerate(_planes()):
        c = Em.solve_least_squares(vec(u * (u.T * G * u).inv() * u.T * G))
        planes.append(all(c[k] == (sp.Rational(-1, 4) if r in E[k] else sp.Rational(1, 2)) for k in range(10))
                      and Em * c == vec(u * (u.T * G * u).inv() * u.T * G))
    census = Counter()
    rule = True
    for S in itertools.combinations(range(10), 5):
        d = N5.extract(list(S), list(range(5))).det()
        census[abs(d)] += 1
        rule = rule and (d != 0) == _connected_nonbipartite([E[k] for k in range(10) if k not in S])
    return {
        "the ten edge projectors E_e (Riesz vectors of the edge readings) and the six Golden projectors R_j have "
        "sum E_e = 2 I and sum R_j = (6/5) I, with Tr(E_e E_f) = 1/9, Tr(R_i R_j) = 1/25 and Tr(E_e R_j) = 1/5; centred "
        "they span 9 and 5 mutually orthogonal dimensions, so the source's 15 quadratics split as 1 + 9 + 5":
            zs(Ee) == 2 * I5 and zs(R) == sp.Rational(6, 5) * I5
            and {(Ee[i] * Ee[j]).trace() for i in range(10) for j in range(10) if i != j} == {sp.Rational(1, 9)}
            and {(R[i] * R[j]).trace() for i in range(6) for j in range(6) if i != j} == {sp.Rational(1, 25)}
            and {(x * r).trace() for x in Ee for r in R} == {sp.Rational(1, 5)}
            and (cE.rank(), cR.rank(), sp.Matrix.hstack(cE, cR, vec(I5)).rank()) == (9, 5, 15)
            and all(((x - I5 / 5) * (r - I5 / 5)).trace() == 0 for x in Ee for r in R),
        "X = (t/5) I + (9/8) sum (e_e - t/5)(E_e - I/5) + (25/24) sum (r_j - t/5)(R_j - I/5) inverts the sixteen readings on "
        "all fifteen G-self-adjoint operators, with the matching Parseval identity, and each plane projector is "
        "(1/2)(its six edges) - (1/4)(the four at its vertex)":
            all(recon(X) == X for X in basis) and all(a == b for a, b in (norm(X) for X in basis)) and all(planes),
        "five edges complete the quadratics exactly when their rows of the native chart are a basis: 162 of the 252 "
        "five-sets, every one unimodular (det +-1), and the other 90 singular; the rule is that the complementary five "
        "edges form a connected nonbipartite graph": census == Counter({1: 162, 0: 90}) and rule,
    }


def dark_readout():
    """The hub's text (17:26): what intensities read of the dark four."""
    D = 15 * sp.eye(4) - 3 * sp.ones(4, 4)
    P = [sp.eye(4)[:, k] for k in range(4)] + [-sp.ones(4, 1)]
    ip = lambda x, y: (x.T * D * y)[0]
    match = [[sp.Rational(ip(P[j], P[r]) ** 2, 144) for j in range(5)] for r in range(5)]
    labels = lambda keep: len({tuple(row[j] for j in keep) for row in match}) == 5
    u, v = sp.Matrix([sp.Rational(1, 3), sp.Rational(1, 3), 1, 0]), sp.Matrix([-1, 1, 0, 0])
    xp, xm = u + v, u - v
    cols = [sp.eye(4)[:, k] for k in range(4)] + [sp.Matrix(c) for c in ([-1, -1, -1, -1], [1, 2, 3, 5], [2, 3, 5, 7],
                                                                        [1, 3, 9, 27])]
    dets = lambda n: [sp.Matrix.hstack(*[cols[i] for i in S]).det() for S in itertools.combinations(range(n), 4)]
    return {
        "in the oriented plane bivectors p0..p3 (metric 15 I - 3 J, p4 = -sum) the matched intensities "
        "|<d_j, d_r>|^2 are 1 and 1/16, so any four of the five sensors name the plane and no three do; intensities never "
        "see the sign of d_r": all(match[r][j] == (1 if j == r else sp.Rational(1, 16)) for r in range(5) for j in range(5))
            and all(labels(k) for k in itertools.combinations(range(5), 4))
            and not any(labels(k) for k in itertools.combinations(range(5), 3)),
        "they do not fix a dark vector: x = u + v and u - v (u = (1/3, 1/3, 1, 0), v = (-1, 1, 0, 0)), of norm 40 and "
        "neither equal nor opposite, give the same five intensities 225, 225, 100, 25, 25":
            ip(xp, xp) == ip(xm, xm) == 40 and xp != xm and xp != -xm
            and [ip(p, xp) ** 2 for p in P] == [ip(p, xm) ** 2 for p in P] == [225, 225, 100, 25, 25],
        "seven detectors e0..e3, (-1, -1, -1, -1), (1, 2, 3, 5), (2, 3, 5, 7) are full spark (all 35 four-minors nonzero), "
        "so by the complement property their intensities recover any real dark vector up to sign; with (1, 3, 9, 27) all "
        "70 minors are nonzero (least |det| 1), so eight survive one erasure":
            all(d != 0 for d in dets(7)) and len(dets(7)) == 35 and all(d != 0 for d in dets(8))
            and min(abs(d) for d in dets(8)) == 1,
    }


def cubic_null():
    """The hub's text (17:26): the cubic-null bright triangles, the equilateral double-dark pair, and E >= 2|Q|."""
    E, N5, sym, F, a0, b0 = _source()
    G = N5.T * N5
    Bs = sp.Matrix(carrier.signed_incidence())
    Pc = sp.eye(10) - Bs.T * Bs / 5
    Nc = sp.Matrix.hstack(*Bs.nullspace())
    cyc = (Nc.T * Nc).inv() * Nc.T
    av, bv = sp.Matrix(sp.symbols("a0:5")), sp.Matrix(sp.symbols("b0:5"))
    A, B = sym(N5 * av), sym(N5 * bv)
    phi = sp.Matrix([((A ** 2 + B ** 2) * A).trace() / 6, ((A ** 2 + B ** 2) * B).trace() / 6]).applyfunc(sp.expand)
    var = list(av) + list(bv)
    s1, s2, t1, t2 = sp.symbols("s1 s2 t1 t2")
    cols, nulls = [], []
    for i, j in itertools.combinations(range(5), 2):
        p = list(range(5))
        p[i], p[j] = j, i
        e1, e2 = (G.inv() * N5.T * _edge_perm(tuple(p)) * N5 + sp.eye(5)).nullspace()
        a, b = s1 * e1 + s2 * e2, t1 * e1 + t2 * e2
        nulls.append(phi.subs(dict(zip(var, list(a) + list(b)))).applyfunc(sp.expand).is_zero_matrix)
        cols.append(F(N5 * e1, N5 * e2))
    T_ = sp.Matrix.hstack(*cols)
    ev = lambda pr: sp.Matrix([int(e in [tuple(sorted(x)) for x in pr]) for e in E])
    X, Y, Z = ev([(0, 1), (2, 3)]), ev([(0, 2), (1, 3)]), ev([(0, 3), (1, 2)])
    A0e, B0e = 2 * X - Y - Z, sp.sqrt(3) * (Y - Z)
    A0, B0 = sym(A0e), sym(B0e)
    S2 = (A0 ** 2 + B0 ** 2) / 16
    aP, bP = G.inv() * N5.T * A0e, G.inv() * N5.T * B0e
    pt = dict(zip(var, list(aP) + list(bP)))
    JW, Jp = (cyc * F(N5 * av, N5 * bv)).jacobian(var).subs(pt), phi.jacobian(var).subs(pt)
    na, nb = (A0e.T * A0e)[0], sp.simplify((B0e.T * B0e)[0])
    a, b, ad, bd = [sp.Matrix(sp.symbols(f"{n}0:5")) for n in ("x", "y", "xd", "yd")]
    h, hd, f = [sp.Matrix(sp.symbols(f"{n}0:2")) for n in ("h", "hd", "f")]
    q = lambda x, y: (x.T * G * y)[0]
    J = lambda x: sp.Matrix([-x[1], x[0]])
    En = ((q(ad, ad) + q(bd, bd) + (hd.T * hd)[0]) / 2 + 2 * (q(a, a) + q(b, b)) + sp.Rational(9, 2) * (h.T * h)[0]
          + ((h - f).T * (h - f))[0] / 2)
    Qn = q(a, bd) - q(b, ad) + h[0] * hd[1] - h[1] * hd[0]
    square = all(sp.expand(En - 2 * s * Qn - (q(ad + 2 * s * b, ad + 2 * s * b) + q(bd - 2 * s * a, bd - 2 * s * a)) / 2
                           - ((hd - 2 * s * J(h)).T * (hd - 2 * s * J(h)))[0] / 2 - sp.Rational(5, 2) * (h.T * h)[0]
                           - ((h - f).T * (h - f))[0] / 2) == 0 for s in (1, -1))
    pairs = list(itertools.combinations(range(5), 2))
    Wm = sp.Matrix.hstack(*[F(N5[:, i], N5[:, j]) for i, j in pairs])
    Hm = sp.Matrix(10, 10, lambda r, c: G.extract(list(pairs[r]), list(pairs[c])).det())
    lam = sp.symbols("lam")
    spec = sp.expand(sp.cancel((Wm.T * Wm - lam * Hm).det() / Hm.det()))
    return {
        "each transposition's -1 eigenspace in the source is a plane on which the trace cubic vanishes identically; the "
        "commutator of its primitive basis is twice the boundary of the complementary triangle (edge square 12), and the "
        "ten outputs give T T^T = 20 P_cycle, rank 6: cubic-null preparations span the bright six":
            all(nulls) and {(c.T * c)[0] for c in cols} == {12} and T_ * T_.T == 20 * Pc and T_.rank() == 6,
        "in a K4 plane the equilateral pair A0 = 2X - Y - Z, B0 = sqrt3 (Y - Z) commutes and is cubic-null, with "
        "A0^2 + B0^2 = 16 P3 (P3 a rank-3 projector, trace 48): its rotation solves the finite parent with h = 0, energy 96 "
        "and charge 48, and there D W, D phi and D(W, phi) have ranks 6, 2 and 8, leaving scale and SO2 blind":
            (A0 * B0 - B0 * A0).is_zero_matrix and phi.subs(pt).applyfunc(sp.simplify).is_zero_matrix
            and (S2 * S2 - S2).applyfunc(sp.simplify).is_zero_matrix and S2.rank() == 3 and (16 * S2).trace() == 48
            and (na, nb) == (12, 12) and ((4 * na + 4 * nb) / 2 + 2 * (na + nb), 2 * (na + nb)) == (96, 48)
            and (JW.rank(simplify=True), Jp.rank(simplify=True), sp.Matrix.vstack(JW, Jp).rank(simplify=True)) == (6, 2, 8),
        "E - 2 sigma Q = |a' + 2 sigma b|^2/2 + |b' - 2 sigma a|^2/2 + |h' - 2 sigma J h|^2/2 + (5/2)|h|^2 + |h - phi|^2/2 for "
        "both signs, as an identity in all 26 variables with phi free, so E >= 2|Q|; and the commutator map has "
        "generalized spectrum (10/9)^6 0^4, so |W_AS| = sqrt10/3 and a Haar plane has E|W u|^2 = 6 (10/9)/10 = 2/3":
            square and spec == sp.expand(lam ** 4 * (lam - sp.Rational(10, 9)) ** 6)
            and sp.Rational(6) * sp.Rational(10, 9) / 10 == sp.Rational(2, 3),
    }


def golden_bridge():
    """The hub's text (17:26): the marked Golden operator on A4 is a pair of Fibonacci blocks."""
    E, N5, sym, F, a0, b0 = _source()
    H, sig, S5, sgn, U = _six_lines()
    K = sym(H[0])
    P5 = sp.eye(5) - sp.ones(5, 5) / 5
    Phi = (P5 + K) / 2
    Bm = sp.Matrix([[1, 1], [1, 0]])
    base = [sp.eye(5)[:, k] - sp.eye(5)[:, 4] for k in range(4)]
    S = next(c for c in (sp.Matrix.hstack(v, (K * v - v) / 2, w, (K * w - w) / 2)
                         for v, w in itertools.combinations(base, 2)) if c.rank() == 4)
    return {
        "the marked K = A(h0) keeps A4 with K^2 = 5 there, so Phi = (1 + K)/2 has Phi^2 = Phi + 1, and the rational "
        "S = [v, (Kv - v)/2, w, (Kw - w)/2] carries K to two blocks 2B - 1 and Phi to two blocks B = [[1, 1], [1, 0]]":
            (K * sp.ones(5, 1)).is_zero_matrix and (K * K * P5 - 5 * P5).is_zero_matrix and (Phi * Phi - Phi - P5).is_zero_matrix
            and (K * S - S * sp.diag(2 * Bm - sp.eye(2), 2 * Bm - sp.eye(2))).is_zero_matrix
            and (Phi * S - S * sp.diag(Bm, Bm)).is_zero_matrix,
        "B^6 = [[13, 8], [8, 5]], trace 18, determinant 1 and entry sum 34 (the hub corrects the source's 27)":
            Bm ** 6 == sp.Matrix([[13, 8], [8, 5]]) and (Bm ** 6).trace() == 18 and (Bm ** 6).det() == 1
            and sum(Bm ** 6) == 34,
    }


def notes_1731():
    """The hub's text (17:26), the sibling's MODEL (16:59-17:18) and five 28 Oct notes uploaded 29 Oct: the rest."""
    return {
        "the hub's arithmetic corrections: 17280 + 2160 x 128 = 293760 and 3 x 17280 + 2160 x 128 = 328320":
            17280 + 2160 * 128 == 293760 and 3 * 17280 + 2160 * 128 == 328320,
        "the Haar near-dark coefficient 10 vol B6/(vol Gr+(2, 5) |det|) with |det| = (20/27)^(3/2), the product of the "
        "tangent spectrum (2/3)^3 (10/9)^3, is (5/8)(27/20)^(3/2) = 81 sqrt15/320, and the fourth moments 34/175, 36/175, "
        "69/175 sum to one as E(D + B)^2 must": sp.Rational(2, 3) ** 3 * sp.Rational(10, 9) ** 3 == sp.Rational(20, 27) ** 3
            and sp.simplify(sp.Rational(5, 8) * sp.Rational(27, 20) ** sp.Rational(3, 2) - 81 * sp.sqrt(15) / 320) == 0
            and sp.Rational(34, 175) + 2 * sp.Rational(36, 175) + sp.Rational(69, 175) == 1,
        "the 28 Oct notes: 4320 = 1 mod 7, so the clock has no element of order 7; 8 m^2 = 3 n^2 has no nonzero integer "
        "solution, so the two septuple frequencies share no period; and the dark port's four squared cosines sum to 5/48":
            4320 % 7 == 1 and not any(8 * m * m == 3 * n * n for m in range(1, 200) for n in range(1, 400))
            and sp.sqrt(sp.Rational(8, 3)).is_rational is False and 4 * sp.Rational(5, 192) == sp.Rational(5, 48),
    }


def dark_measurement():
    """The sibling's MODEL (18:00): the five dark planes as a measurement."""
    D = 15 * sp.eye(4) - 3 * sp.ones(4, 4)
    P = [sp.eye(4)[:, k] for k in range(4)] + [-sp.ones(4, 1)]
    ip = lambda x, y: (x.T * D * y)[0]
    M = [p * p.T * D / 15 for p in P]
    prob = [[ip(p, m * p) / ip(p, p) for m in M] for p in P]
    info = sp.log(5, 2) + sum(q * sp.log(q, 2) for q in prob[0])
    return {
        "the five dark planes p0..p3, p4 = -sum (metric D = 15 I - 3 J) have frame operator sum p p^T D = 15 I, so the "
        "rank-one, D-positive M_r = p_r p_r^T D/15 sum to the identity: they are a measurement on the dark four":
            sum(M, sp.zeros(4)) == sp.eye(4)
            and all(D * m == (D * p) * (D * p).T / 15 and m.rank() == 1 for p, m in zip(P, M)),
        "on the plane p_s it reads p_s with probability 4/5 and each other plane with 1/20; with a uniform prior the "
        "outcome is uniform, so the information is log2 5 - H(4/5, 1/20, 1/20, 1/20, 1/20) = 6/5 bits exactly":
            all(prob[s][r] == (sp.Rational(4, 5) if r == s else sp.Rational(1, 20)) for s in range(5) for r in range(5))
            and all(sum(row[r] for row in prob) == 1 for r in range(5))
            and sp.simplify(sp.expand_log(info, force=True)) == sp.Rational(6, 5),
        "any two planes have Bhattacharyya coefficient 2 sqrt(4/5 x 1/20) + 3 x 1/20 = 11/20":
            {sum(sp.sqrt(x * y) for x, y in zip(prob[s], prob[t])) for s, t in itertools.combinations(range(5), 2)}
            == {sp.Rational(11, 20)},
    }


def plane_tomography():
    """The sibling's MODEL (18:00): how many channels read the source's oriented planes everywhere, in orthonormal
    coordinates. Cited: the skew normal form; Gr+(2, 5) = Q3 in CP^4 with T Q3 + O(2) = O(1)^5, H^2 = Z h and h^2 = 2 l
    in H^4 = Z l; the normal bundle of an immersion; and the Lefschetz fixed-point theorem."""
    e = [sp.eye(5)[:, k] for k in range(5)]
    pairs = list(itertools.combinations(range(5), 2))
    up = lambda x, y: sp.Matrix([(x * y.T - y * x.T)[i, j] for i, j in pairs])
    tan = lambda i, j: sp.Matrix.hstack(*[up(e[i], e[k]) for k in range(5) if k not in (i, j)],
                                         *[up(e[k], e[j]) for k in range(5) if k not in (i, j)])
    al, be = sp.symbols("alpha beta", real=True)
    E, N5, sym, F, a0, b0 = _source()
    W = sp.Matrix.hstack(*[F(N5[:, i], N5[:, j]) for i, j in pairs])
    R = sp.diag(sp.Matrix([[3, -4], [4, 3]]) / 5, sp.Matrix([[5, -12], [12, 5]]) / 13, 1)
    fixed = sp.Matrix.hstack(*(sp.Matrix.hstack(*[up(R[:, i], R[:, j]) for i, j in pairs]) - sp.eye(10)).nullspace())
    S = al * (e[0] * e[1].T - e[1] * e[0].T) + be * (e[2] * e[3].T - e[3] * e[2].T)
    planes = sp.solve([S.extract([0, 1, 2, 3], [0, 1, 2, 3]).det(), al ** 2 + be ** 2 - 1], [al, be], dict=True)
    h, m = sp.symbols("h m")
    trunc = lambda f: sp.expand(sp.series(f, h, 0, 4).removeO())
    c, p = trunc((1 + h) ** 5 / (1 + 2 * h)), trunc((1 + h ** 2) ** 5 / (1 + 4 * h ** 2))
    return {
        "every bivector lies in a tangent space of the oriented planes: alpha e0 ^ e1 + beta e2 ^ e3 = e0 ^ (alpha e1) + "
        "(-beta e3) ^ e2 at the plane e0 ^ e2, whose tangent space {u ^ a + b ^ v : a, b perpendicular to u, v} has "
        "dimension 6, and every bivector is a rotation of one of these; so a linear reading immerses the planes only if it "
        "is injective, and ten channels are necessary and sufficient: the commutator's bright six (rank 6 on the source's "
        "bivectors) and its dark four (the kernel)":
            (al * up(e[0], e[1]) + be * up(e[2], e[3]) - up(e[0], al * e[1]) - up(-be * e[3], e[2])).is_zero_matrix
            and tan(0, 2).rank() == 6 and W.rank() == 6 and len(W.nullspace()) == 4,
        "Gr+(2, 5) = Q3 has c(T) = (1 + h)^5/(1 + 2h) = 1 + 3h + 4h^2 + 2h^3 and p(T) = (1 + h^2)^5/(1 + 4h^2) = 1 + h^2; "
        "c3 = 2h^3 = 4 is its Euler number, the count of oriented planes fixed by a rotation with Pythagorean angles "
        "(+-e0 ^ e1 and +-e2 ^ e3, each nondegenerate)":
            c == 1 + 3 * h + 4 * h ** 2 + 2 * h ** 3 and p == 1 + h ** 2 and 2 * c.coeff(h, 3) == len(planes) == 4
            and sp.Matrix.hstack(fixed, up(e[0], e[1]), up(e[2], e[3])).rank() == fixed.shape[1] == 2
            and all(sp.Matrix.hstack(tan(i, j), fixed).rank() == 8 for i, j in ((0, 1), (2, 3))),
        "an immersion in R^8 would have an oriented normal plane bundle with e^2 = p1 = -h^2 (p(nu) = 1/p(T) = 1 - h^2), "
        "so m^2 = -1 for e = m h: eight outputs cannot immerse the planes, and a smooth reading needs at least nine; the "
        "host's 7 channels are 9 - 2 and 10 - 3":
            trunc(1 / p) == 1 - h ** 2 and not any(r.is_real for r in sp.solve(m ** 2 + 1, m)) and (9 - 7, 10 - 7) == (2, 3),
    }


def notes_1804():
    """The sibling's MODEL (18:00): the rest."""
    return {
        "6/5 = 1/(5/6), the reciprocal of the hypercharge's square (CHARGE_WEIGHT), a shared number and not a map; the "
        "atlas's 49 records are 7^2; the stated mixed-history rank 234 = 13 x 18 is 126 below the parent 360":
            1 / sp.Rational(5, 6) == sp.Rational(6, 5) and 49 == 7 ** 2 and 234 == 13 * 18 and 360 - 234 == 126,
    }


# ------------------------------------------------------------------- the 18:22 text

def _dark_chart():
    """The hub's primitive source-wedge chart (18:22): Lambda^2 of the source in primitive coordinates with
    H = Lambda^2 G, the commutator W on it, its kernel basis (sympy's, the hub's) and the consistently oriented dark rays
    z_i = -p_(4-i), whose kernel coordinates are e0, e1, e2, e3, (1, -1, 1, -1) up to sign."""
    E, N5, sym, F, a0, b0 = _source()
    G = N5.T * N5
    pairs = list(itertools.combinations(range(5), 2))
    wedge = lambda x, y: sp.Matrix([x[i] * y[j] - x[j] * y[i] for i, j in pairs])
    Hm = sp.Matrix(10, 10, lambda r, c: G.extract(list(pairs[r]), list(pairs[c])).det())
    W = sp.Matrix.hstack(*[F(N5[:, i], N5[:, j]) for i, j in pairs])
    p = [(-1) ** r * wedge(u[:, 0], u[:, 1]) for r, u in enumerate(_planes())]
    return G, pairs, wedge, Hm, W, sp.Matrix.hstack(*W.nullspace()), [-p[4 - i] for i in range(5)]


def _kkt_gaps():
    """Separate the ten signed labels +-u_k by 1 at least squared norm: magnitudes u0 >= 1/2 with gaps >= 1, sign
    pattern s (s_0 = +1) and sum s_k u_k = 0. Each of the 16 x 32 active sets is a square KKT system; returns the least
    squared norm of every feasible pattern, its minimizer, and the number of cases."""
    u, lam, mu = sp.symbols("u0:5"), sp.symbols("l0:5"), sp.Symbol("mu")
    g = [u[0] - sp.Rational(1, 2)] + [u[k + 1] - u[k] - 1 for k in range(4)]
    best, cases = {}, 0
    for s in itertools.product((1, -1), repeat=4):
        s = (1,) + s
        for act in itertools.product((0, 1), repeat=5):
            cases += 1
            unk = list(u) + [lam[a] for a in range(5) if act[a]] + [mu]
            eqs = [2 * u[i] - sum(lam[a] * sp.diff(g[a], u[i]) for a in range(5) if act[a]) - mu * s[i] for i in range(5)]
            eqs += [g[a] for a in range(5) if act[a]] + [sum(si * ui for si, ui in zip(s, u))]
            A, b = sp.linear_eq_to_matrix(eqs, unk)
            if A.det() == 0:
                continue
            sol = dict(zip(unk, A.LUsolve(b)))
            if all(sol[lam[a]] >= 0 for a in range(5) if act[a]) and all(c.subs(sol) >= 0 for c in g):
                val = sum(sol[x] ** 2 for x in u)
                if val < best.get(s, (sp.oo,))[0]:
                    best[s] = (val, tuple(sol[x] for x in u))
    return best, cases


def seventh_sensor():
    """The hub's text (18:22): a fixed seventh dark reading, and the different minima for detecting, labelling and
    reconstructing the source's planes. Cited: the five dark rays are all the simple bivectors the commutator kills
    (k4_complete); a real linear section of odd degree has a real point; the skew normal form."""
    G, pairs, wedge, Hm, W, Km, z = _dark_chart()
    ip = lambda x, y: (x.T * Hm * y)[0]
    ell12 = sp.Matrix([0, -3, 0, -1, 0, 3, 1, 0, 1, -1])
    star = sp.Matrix([-17, -5, -10, -2, -6, -15, -10, 15, -4, 16])
    h12, hs = (z[0] + z[1]) / 3, Hm.inv() * star
    coords = [list((Km.T * Km).inv() * Km.T * x) for x in z]
    rays = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], [1, -1, 1, -1]]
    ballots = sum(1 for s in set(itertools.permutations([1, 1, 1, -1, -1, -1]))
                  if all(sum(s[:k]) >= 0 for k in range(7)))
    e = [sp.eye(5)[:, k] for k in range(5)]
    up = lambda x, y: sp.Matrix([(x * y.T - y * x.T)[i, j] for i, j in pairs])
    tan = sp.Matrix.hstack(*[up(e[0], e[k]) for k in (1, 3, 4)], *[up(e[k], e[2]) for k in (1, 3, 4)])
    i01, i23 = pairs.index((0, 1)), pairs.index((2, 3))
    L = sp.Matrix([[int(c == k) for c in range(10)] for k in range(10) if k not in (i01, i23)]
                  + [[2 * int(c == i01) - int(c == i23) for c in range(10)]])
    bound = min(max(k, 5 - k) ** 2 * (sp.Rational(1, k) + sp.Rational(1, 5 - k)) for k in range(1, 5))
    best, cases = _kkt_gaps()
    resp = [(star.T * x)[0] for x in z]
    labels = sorted(resp + [-x for x in resp])
    img = [sp.Matrix([[1, 1, 1, 1], [1, 2, 3, 4]]) * sp.Matrix(v) for v in rays]
    return {
        "the fixed dark probe h12 = (z0 + z1)/3, of squared norm 2, has covector ell12 = (0, -3, 0, -1, 0, 3, 1, 0, 1, -1) "
        "in the primitive wedge chart and responses (3, 3, -2, -2, -2) on the five dark rays z_i (kernel coordinates e0, "
        "e1, e2, e3, (1, -1, 1, -1), H-Gram 15 I - 3 J); those rays are the only simple bivectors the six bright readings "
        "miss, so the six readings and ell12 never all vanish on a nonzero simple bivector":
            Hm * h12 == ell12 and ip(h12, h12) == 2 and [(ell12.T * x)[0] for x in z] == [3, 3, -2, -2, -2]
            and all(sp.Matrix(c) in (sp.Matrix(v), -sp.Matrix(v)) for c, v in zip(coords, rays))
            and sp.Matrix(5, 5, lambda i, j: ip(z[i], z[j])) == 15 * sp.eye(5) - 3 * sp.ones(5, 5),
        "six readings never suffice: the Pluecker G(2, 5) has degree 5 (the five ballot sequences, 6!/(4 3 2 3 2 1)), "
        "which is odd, so a real codimension-six section always meets it; and global reconstruction of the simple cone "
        "needs all ten readings (a kernel vector is a multiple or a difference of simple bivectors): the rank-nine observer "
        "keeping eight coordinates and 2 w01 - w23 has kernel e01 + 2 e23 and tangent rank 5 at span(e0, e2)":
            ballots == 5 == factorial(6) // (4 * 3 * 2 * 3 * 2 * 1) and L.rank() == 9
            and L * (up(e[0], e[1]) + 2 * up(e[2], e[3])) == sp.zeros(9, 1) and (L * tan).rank() == 5,
        "a zero-sum response with every |r_i| >= m has square at least (15/2) m^2, at (3m/2, 3m/2, -m, -m, -m), so the "
        "nonblind margin is sqrt2 on primitive rays and 1/sqrt6 on unit planes, attained by h12; to separate the ten signed "
        "labels by 1 (u0 >= 1/2, gaps >= 1) the 512 active-set cases leave six feasible sign patterns, least squares 46, "
        "105/2, 70, 85, 90 and 190, the optimum at (1/2, -3/2, 5/2, 7/2, -5); ell* = (-17, -5, -10, -2, -6, -15, -10, 15, "
        "-4, 16) is dark with responses 10 times that, norm^2 920/3 and label gap 10, so the sharp gap is sqrt(15/46), "
        "or sqrt(5/184) on unit planes":
            bound == sp.Rational(15, 2) and 2 * (sp.Rational(3, 2)) ** 2 + 3 == bound
            and sp.Rational(15, 2) * 2 == 15 and sp.sqrt(sp.Rational(2, 12)) == 1 / sp.sqrt(6)
            and min(abs(x) for x in [3, 3, -2, -2, -2]) / sp.sqrt(ip(h12, h12)) == sp.sqrt(2)
            and cases == 512 and sorted(v for v, _ in best.values()) == [46, sp.Rational(105, 2), 70, 85, 90, 190]
            and best[(1, -1, 1, 1, -1)] == (46, (sp.Rational(1, 2), sp.Rational(3, 2), sp.Rational(5, 2), sp.Rational(7, 2), 5))
            and sp.Matrix.hstack(Km, hs).rank() == 4 and resp == [5, -15, 25, 35, -50] and ip(hs, hs) == sp.Rational(920, 3)
            and min(y - x for x, y in zip(labels, labels[1:])) == 10
            and 10 / sp.sqrt(sp.Rational(920, 3)) == sp.sqrt(sp.Rational(15, 46))
            and sp.sqrt(sp.Rational(15, 46)) / sp.sqrt(12) == sp.sqrt(sp.Rational(5, 184)),
        "two signed dark readings, the kernel-chart rows (1, 1, 1, 1) and (1, 2, 3, 4), send the five rays to five "
        "distinct projective directions, (1, 1), (1, 2), (1, 3), (1, 4) and (0, -2)":
            all(sp.Matrix.hstack(a, b).det() != 0 for a, b in itertools.combinations(img, 2)),
    }


def preparability():
    """The hub's text (18:22): when a reconstructed exterior vector comes from one source pair."""
    G, pairs, wedge, Hm, W, Km, z = _dark_chart()
    quads = list(itertools.combinations(range(5), 4))
    H4 = sp.Matrix(5, 5, lambda r, c: G.extract(list(quads[r]), list(quads[c])).det())
    R, *w = sp.polys.rings.ring(",".join(f"w{k}" for k in range(10)), sp.ZZ)
    K = [[R(0)] * 5 for _ in range(5)]
    for k, (i, j) in enumerate(pairs):
        K[i][j], K[j][i] = w[k], -w[k]
    mm = lambda X, Y: [[sum(X[i][k] * Y[k][j] for k in range(5)) for j in range(5)] for i in range(5)]
    A2 = mm(K, [[int(G[i, j]) for j in range(5)] for i in range(5)])
    A2 = mm(A2, A2)
    tr4 = sum(A2[i][k] * A2[k][i] for i in range(5) for k in range(5))
    c = lambda x, i, j: x[pairs.index((i, j))]
    plu = lambda x: [c(x, i, j) * c(x, k, l) - c(x, i, k) * c(x, j, l) + c(x, i, l) * c(x, j, k) for i, j, k, l in quads]
    q = plu(w)
    s = sum(int(Hm[a, b]) * w[a] * w[b] for a in range(10) for b in range(10))
    l2, d = sp.symbols("l2 d", positive=True)
    l1 = l2 + d
    S, T_ = l1 ** 2 + l2 ** 2, 4 * l1 ** 2 * l2 ** 2
    root = sp.sqrt(sp.factor(S ** 2 - T_))
    fit = lambda s_, t_: ((s_ - sp.sqrt(s_ ** 2 - t_)) / 2, s_ + 1 - 2 * sp.sqrt((s_ + sp.sqrt(s_ ** 2 - t_)) / 2))
    return {
        "in the native chart t = |w ^ w|^2 = 4 q^T H4 q = 2 (w^T H w)^2 - Tr[(K_w G)^4], an identity of quartics in the ten "
        "exterior coordinates (q the five Pluecker quadrics, H = Lambda^2 G, H4 = Lambda^4 G, K_w the skew coefficient "
        "matrix); the unweighted 4 sum q^2 is not, so the metric must be kept":
            4 * sum(int(H4[a, b]) * q[a] * q[b] for a in range(5) for b in range(5)) == 2 * s ** 2 - tr4
            and 4 * sum(x * x for x in q) != 2 * s ** 2 - tr4,
        "the skew normal form's block squares are (s +- sqrt(s^2 - t))/2, so the squared distance to the simple cone is "
        "(s - sqrt(s^2 - t))/2 = lambda_2^2 and to the unit oriented planes s + 1 - 2 lambda_1; at w = e01 + 2 e23 (s = 5, "
        "t = 16) they are 1 and 2, and an orthogonal output error of amplitude 3 makes the best one-pair fit 1 + 9 = 10":
            root == d * (d + 2 * l2) and sp.expand((S - root) / 2 - l2 ** 2) == 0
            and sp.simplify(sp.sqrt(sp.factor((S + root) / 2)) - l1) == 0 and fit(5, 16) == (1, 2) and fit(5, 16)[0] + 9 == 10,
        "two dark planes are each preparable but their sum is not: W kills z0 + z1, whose Pluecker quadrics are "
        "(1, 0, 0, 0, 0), so a dark-four signal need not come from one source pair":
            all(x == 0 for y in z for x in plu(list(y))) and (W * (z[0] + z[1])).is_zero_matrix
            and plu(list(z[0] + z[1])) == [1, 0, 0, 0, 0],
    }


def _rank_mod(rows, p):
    """Rank of an integer matrix over GF(p)."""
    M = [[x % p for x in r] for r in rows]
    rk = 0
    for col in range(len(M[0])):
        piv = next((i for i in range(rk, len(M)) if M[i][col]), None)
        if piv is None:
            continue
        M[rk], M[piv] = M[piv], M[rk]
        iv = pow(M[rk][col], -1, p)
        M[rk] = [(x * iv) % p for x in M[rk]]
        for i in range(len(M)):
            if i != rk and M[i][col]:
                f = M[i][col]
                M[i] = [(a - f * b) % p for a, b in zip(M[i], M[rk])]
        rk += 1
    return rk


def exterior_code():
    """The hub's text (18:22): fifteen bright Golden-pair readings and ten dark duad readings."""
    G, pairs, wedge, Hm, W, Km, z = _dark_chart()
    E, N5, sym, F, a0, b0 = _source()
    H, sig, S5, sgn, U = _six_lines()
    HG = sp.Matrix.hstack(*H)
    V = G.inv() * N5.T * HG
    Q = [wedge(V[:, i], V[:, j]) for i, j in itertools.combinations(range(6), 2)]
    h = [(z[i] + z[j]) / 3 for i, j in itertools.combinations(range(5), 2)]
    SQ, Sh = sum((x * x.T * Hm for x in Q), sp.zeros(10)), sum((x * x.T * Hm for x in h), sp.zeros(10))
    PD = Km * (Km.T * Hm * Km).inv() * Km.T * Hm
    PB = sp.eye(10) - PD
    Bb = sp.Matrix.hstack(*(Km.T * Hm).nullspace())
    Mb = sp.Matrix.vstack(*[x.T * Hm * Bb for x in Q])
    Mb = Mb * sp.ilcm(*[sp.fraction(v)[1] for v in Mb])
    rows = Mb.tolist()
    Md = sp.Matrix.vstack(*[x.T * Hm * Km for x in h])
    four = [Md.extract(list(S), list(range(4))).rank() for S in itertools.combinations(range(10), 4)]
    mod2 = [_rank_mod([Md.row(i) for i in S], 2) for S in itertools.combinations(range(10), 5)]
    return {
        "the six coherently oriented Golden source vectors (H_G^T H_G = 12 I - 2 J) give fifteen exterior pairs "
        "Q_ij = v_i ^ v_j with sum Q Q* = 144 I on all ten coordinates, and the ten dark probes h_ij = (z_i + z_j)/3 give "
        "sum h h* = 5 P_D; so w = (1/144) sum Q_ij <Q_ij, P_B w> + (1/5) sum h_ij <h_ij, w>, the cross terms cancelling, "
        "and |w|^2 = (1/144) sum b^2 + (1/5) sum d^2":
            HG.T * HG == 12 * sp.eye(6) - 2 * sp.ones(6, 6) and SQ == 144 * sp.eye(10) and Sh == 5 * PD
            and SQ * PB / 144 + Sh / 5 == sp.eye(10) and PB.T * Hm * SQ * PB / 144 + Hm * Sh / 5 == Hm,
        "the bright readings are a [15, 6, 5] code: all 1365 eleven-reading sets have rank 6 (over a prime, hence over Q) "
        "and a ten-reading set has rank 5; the dark readings are a [10, 4, 6] code: all 252 five-reading sets have rank 4, "
        "and of the 210 four-reading sets 185 have rank 4 and 25 rank 3; together a [25, 10, 5] code, which corrects two "
        "errors or four erasures":
            all(_rank_mod([rows[i] for i in S], 2147483629) == 6 for S in itertools.combinations(range(15), 11))
            and any(Mb.extract(list(S), list(range(6))).rank() == 5 for S in itertools.combinations(range(15), 10))
            and all(Md.extract(list(S), list(range(4))).rank() == 4 for S in itertools.combinations(range(10), 5))
            and (four.count(4), four.count(3), len(four)) == (185, 25, 210) and min(5, 6) == 5,
        "the dark readings' integer matrix (entries +-2 and +-3) has Smith invariants 1, 5, 5, 5; mod 5 its rank is 1, and "
        "mod 2 thirty of the 252 five-reading sets drop to rank 3 (222 keep 4), so the code's guarantees need "
        "characteristic zero":
            all(x.is_integer for x in Md) and {abs(x) for x in Md} == {2, 3}
            and list(smith_normal_form(Md, domain=sp.ZZ).diagonal()) == [1, 5, 5, 5]
            and _rank_mod(Md.tolist(), 5) == 1 and (mod2.count(3), mod2.count(4)) == (30, 222),
    }


def dark_information():
    """The hub's text (18:22) and the sibling's MODEL (18:33): what the dark measurement can tell, against the source
    states. Cited: the complement property for real intensity recovery."""
    D = 15 * sp.eye(4) - 3 * sp.ones(4, 4)
    P = [sp.eye(4)[:, k] for k in range(4)] + [-sp.ones(4, 1)]
    rho, Ef = [x * x.T * D / 12 for x in P], [x * x.T * D / 15 for x in P]
    prob = [[(Ef[r] * rho[s]).trace() for r in range(5)] for s in range(5)]
    info = sum(x * sp.log(5 * x, 2) for x in prob[0])
    kl = sum(x * sp.log(x / y, 2) for x, y in zip(prob[0], prob[1]))
    E, N5, sym, F, a0, b0 = _source()
    H, sig, S5, sgn, U = _six_lines()
    G = N5.T * N5
    V = G.inv() * N5.T * sp.Matrix.hstack(*H)
    Pr = [u * (u.T * G * u).inv() * u.T * G for u in _planes()]
    eff = [V[:, j] * V[:, j].T * G / 12 for j in range(6)]
    cols = [sp.eye(4)[:, k] for k in range(4)] + [sp.Matrix(c) for c in (
        [-1, -1, -1, -1], [1, 2, 3, 5], [2, 3, 5, 7], [1, 3, 9, 27], [1, 5, 25, 125], [1, 6, 36, 216])]
    dets = lambda n: [sp.Matrix.hstack(*[cols[i] for i in S]).det() for S in itertools.combinations(range(n), 4)]
    return {
        "with pure states rho_r = p_r p_r^T D/12 and effects E_r = p_r p_r^T D/15, uniform-prior success is 4/5, and that "
        "is optimal, since rho_r <= I bounds it by sum Tr E_r / 5 = 4/5; the likelihood ratios are 4 and 1/4, so the "
        "information is 8/5 - 2/5 = 6/5 bits (the outcome entropy log2 5 - 6/5 is about 1.1219); the mean state is I/4, "
        "a Holevo bound of 2 bits, and distinct labels have KL divergence 3 bits":
            all(x.trace() == 1 for x in rho) and all(prob[s][s] == sp.Rational(4, 5) for s in range(5))
            and sum(x.trace() for x in Ef) / 5 == sp.Rational(4, 5)
            and {x * 5 for x in prob[0]} == {4, sp.Rational(1, 4)}
            and sp.simplify(sp.expand_log(info, force=True)) == sp.Rational(6, 5) == 2 * sp.Rational(4, 5) - 2 * sp.Rational(1, 5)
            and abs(sp.N(sp.log(5, 2) - sp.Rational(6, 5)) - sp.Float("1.1219")) < 1e-4
            and sum(rho, sp.zeros(4)) / 5 == sp.eye(4) / 4 and sp.simplify(sp.expand_log(kl, force=True)) == 3,
        "independent repeats err at most 4 (11/20)^n, below 1% from eleven repeats (4 (11/20)^10 > 1/100)":
            4 * sp.Rational(11, 20) ** 11 < sp.Rational(1, 100) < 4 * sp.Rational(11, 20) ** 10,
        "the five mixed source states P(E_r)/2 against the six Golden effects v_j v_j^T G/12 (which sum to I) give "
        "probability 1/6 for every label and outcome, no label information: the dark measurement is another instrument":
            sum(eff, sp.zeros(5)) == sp.eye(5) and {(Pr[r] / 2 * x).trace() for r in range(5) for x in eff} == {sp.Rational(1, 6)},
        "nine and ten real dark sensors, adding (1, 5, 25, 125) and (1, 6, 36, 216), are full spark (all 126 and 210 "
        "four-minors nonzero), so they survive two and three erasures; 7 + r full-spark sensors survive r":
            len(dets(9)) == 126 and all(x != 0 for x in dets(9)) and len(dets(10)) == 210 and all(x != 0 for x in dets(10)),
    }


def causal_records():
    """The hub's text (18:22): an ideal boundary record of the native bath keeps the whole forcing history. Cited: the
    Volterra comparison inequality."""
    E, N5, sym, F, a0, b0 = _source()
    G = N5.T * N5
    t, s = sp.symbols("t s", positive=True)
    c = sp.Rational(495 * 256, 183)
    u = sp.cosh(sp.sqrt(c) * t)
    GC, Pu = 183 * sp.eye(6) + 52 * sp.ones(6, 6), sp.ones(6, 6) / 6
    gk, Mj = sp.symbols("g0:13"), sp.symbols("M0:7")
    gt = sum(gk[k] * t ** k / sp.factorial(k) for k in range(13))
    Kt = sum((-1) ** j * Mj[j] * t ** (2 * j + 1) / sp.factorial(2 * j + 1) for j in range(7))
    y = sp.expand(-sp.integrate(sp.expand(Kt.subs(t, t - s) * gt.subs(t, s)), (s, 0, t)))
    jets = all(sp.expand(sp.diff(y, t, n + 2).subs(t, 0) + sum((-1) ** j * Mj[j] * gk[n - 2 * j] for j in range(n // 2 + 1)))
               == 0 for n in range(11))
    ev = lambda pr: sp.Matrix([int(e in pr) for e in E])
    X, Y, Z = ev([(0, 1), (2, 3)]), ev([(0, 2), (1, 3)]), ev([(0, 3), (1, 2)])
    a, b = X - Z, Y - Z
    va, vb = -2 * b, 2 * a
    n = lambda x, y: (x.T * y)[0] / 4
    A, B = sym(a), sym(b)
    xa, xb, xu, xv = [sp.Matrix(sp.symbols(f"{k}0:5")) for k in ("x", "y", "u", "v")]
    q = lambda x, y: (x.T * G * y)[0]
    En, Qn = (q(xu, xu) + q(xv, xv)) / 8 + (q(xa, xa) + q(xb, xb)) / 2, (q(xa, xv) - q(xb, xu)) / 4
    th = sp.Symbol("th")
    at, bt = a * sp.cos(th) + va / 2 * sp.sin(th), b * sp.cos(th) + vb / 2 * sp.sin(th)
    return {
        "the record y = -K * g with K(t) = C* sin(t sqrtD)/sqrtD C has y'' = -G_C g - int K''(t - s) g(s) ds, a "
        "second-kind Volterra equation: G_C = C* C = 183 P_contrast + 495 P_uniform (the six-site Gram 183 I + 52 J) has "
        "inverse P_contrast/183 + P_uniform/495, and the jets y^(n+2)(0) = -sum (-1)^j M_j g^(n-2j)(0), M_j = C* D^j C, "
        "hold for n <= 10 as formal identities in twelve force jets":
            GC == 183 * (sp.eye(6) - Pu) + 495 * Pu and GC.inv() == (sp.eye(6) - Pu) / 183 + Pu / 495 and jets,
        "with |K''(t)| <= 495 x 256 t the comparison u = cosh(sqrt(c) t), c = 495 x 256/183 = 42240/61, solves "
        "u = 1 + int c (t - s) u(s) ds, so |delta g| <= (1/183) cosh(sqrt(42240/61) T) |delta y''|":
            c == sp.Rational(42240, 61) and sp.simplify(1 + sp.integrate(c * (t - s) * u.subs(t, s), (s, 0, t)) - u) == 0,
        "a harmonic pair q = q0 cos 2t + (v/2) sin 2t is force-free exactly when W(a0, b0) = W(va, vb) = "
        "W(va, b0) + W(a0, vb) = 0; on the native stratum (mass G/4) E - 2 sigma Q = (|va + 2 sigma b|^2 + "
        "|vb - 2 sigma a|^2)/8 for both signs; and a = X - Z, b = Y - Z, va = -2b, vb = 2a has E = 8, Q = 4 and an empty "
        "exterior, but its cubic phasor is (-4/3, -4/3) and its dark wedge has norm^2 12":
            (F(at, bt) - (F(a, b) * sp.cos(th) ** 2 + (F(a, vb) + F(va, b)) / 2 * sp.sin(th) * sp.cos(th)
                          + F(va, vb) / 4 * sp.sin(th) ** 2)).applyfunc(sp.expand).is_zero_matrix
            and all(sp.expand(En - 2 * g * Qn - (q(xu + 2 * g * xb, xu + 2 * g * xb) + q(xv - 2 * g * xa, xv - 2 * g * xa)) / 8)
                    == 0 for g in (1, -1))
            and ((n(va, va) + n(vb, vb)) / 2 + 2 * (n(a, a) + n(b, b)), n(a, vb) - n(b, va)) == (8, 4)
            and F(a, b).is_zero_matrix and F(va, vb).is_zero_matrix and (F(va, b) + F(a, vb)).is_zero_matrix
            and [((A ** 2 + B ** 2) * A).trace() / 6, ((A ** 2 + B ** 2) * B).trace() / 6] == [sp.Rational(-4, 3)] * 2
            and (a.T * a)[0] * (b.T * b)[0] - (a.T * b)[0] ** 2 == 12,
    }


PRIME = 2147483629


def _rref_p(M, p=PRIME):
    """Reduced row echelon form of an integer matrix over GF(p) (numpy, p < 2^31): the basis rows and pivot columns."""
    A = np.array(M, dtype=np.int64) % p
    rk, piv = 0, []
    for c in range(A.shape[1]):
        nz = np.nonzero(A[rk:, c])[0]
        if not len(nz):
            continue
        A[[rk, rk + nz[0]]] = A[[rk + nz[0], rk]]
        A[rk] = (A[rk] * pow(int(A[rk, c]), p - 2, p)) % p
        col = A[:, c].copy()
        col[rk] = 0
        nz = np.nonzero(col)[0]
        if len(nz):
            A[nz] = (A[nz] - (col[nz, None] * A[rk][None, :]) % p) % p
        piv.append(c)
        rk += 1
        if rk == A.shape[0]:
            break
    return A[:rk], piv


def _word_ranks(M, step, levels, p=PRIME):
    """Ranks over GF(p) of the spans V_0 = rows(M), V_(L+1) = V_L + step(V_L), for the given number of levels."""
    B, piv = _rref_p(M, p)
    out = [len(piv)]
    for _ in range(levels):
        X = np.array(step(B), dtype=np.int64) % p
        for k, c in enumerate(piv):
            f = X[:, c].copy()
            nz = np.nonzero(f)[0]
            if len(nz):
                X[nz] = (X[nz] - (f[nz, None] * B[k][None, :]) % p) % p
        R, pv = _rref_p(X, p)
        if pv:
            for k, c in enumerate(pv):
                f = B[:, c].copy()
                nz = np.nonzero(f)[0]
                if len(nz):
                    B[nz] = (B[nz] - (f[nz, None] * R[k][None, :]) % p) % p
            B, piv = np.vstack([B, R]), piv + pv
        out.append(len(piv))
    return out


def _exact_rank(M, p=PRIME):
    """The rank over Q of an integer matrix with a certificate: the rank over GF(p) bounds it below, and an integer
    kernel of the complementary dimension, lifted by rational reconstruction and checked exactly, bounds it above.
    Returns the rank, or None if the lift fails."""
    R, piv = _rref_p(M, p)
    bound = int((p // 2) ** 0.5)

    def lift(a):
        r0, r1, s0, s1 = p, a % p, 0, 1
        while r1 > bound:
            k = r0 // r1
            r0, r1, s0, s1 = r1, r0 - k * r1, s1, s0 - k * s1
        return Fraction(r1, s1) if 0 < abs(s1) <= bound else None
    ker = []
    for f in (c for c in range(M.shape[1]) if c not in piv):
        v = {f: Fraction(1)}
        for i, c in enumerate(piv):
            x = lift(-int(R[i, f]))
            if x is None:
                return None
            v[c] = x
        den = lcm(*(x.denominator for x in v.values()))
        ker.append([int(v.get(c, 0) * den) for c in range(M.shape[1])])
    N = np.array(ker, dtype=object).T
    if ker and (np.array(M, dtype=object).dot(N) != 0).any():
        return None
    if ker and len(_rref_p(np.array(ker, dtype=object) % p, p)[1]) != len(ker):
        return None
    return len(piv)


@functools.lru_cache(maxsize=None)
def _a6():
    """The hub's constructed 360 parent (18:22): A6 on 0..5 with x = (0123)(45), r = (01234), w = (14)(23) and
    t = (23)(45); C4 = <x>, D10 = <r, w>, A5 = Stab(5); the left-coset readers O90 and O36 on Q[A6] (rows the cosets,
    columns the group) and the right action (f U_g)(h) = f(hg)."""
    def perm(*cycles):
        p = list(range(6))
        for c in cycles:
            for a, b in zip(c, c[1:] + c[:1]):
                p[a] = b
        return tuple(p)
    Gr = sorted(p for p in itertools.permutations(range(6)) if Permutation(list(p)).is_even)
    idx = {g: k for k, g in enumerate(Gr)}
    mul = lambda a, b: tuple(a[b[i]] for i in range(6))
    inv = lambda a: tuple(sorted(range(6), key=lambda i: a[i]))

    def closure(gens):
        S, new = {tuple(range(6))}, [tuple(range(6))]
        while new:
            new = [mul(a, g) for a in new for g in gens if mul(a, g) not in S]
            S |= set(new)
        return frozenset(S)

    def cosets(H):
        seen, out = set(), []
        for g in Gr:
            if g not in seen:
                c = frozenset(mul(g, h) for h in H)
                seen |= c
                out.append(c)
        return out
    x, r, w, t = perm((0, 1, 2, 3), (4, 5)), perm((0, 1, 2, 3, 4)), perm((1, 4), (2, 3)), perm((2, 3), (4, 5))
    C4, D10 = closure([x]), closure([r, w])
    c90, c36 = cosets(C4), cosets(D10)
    reader = lambda cs: np.array([[int(g in c) for g in Gr] for c in cs], dtype=np.int64)
    right = lambda M, g: np.asarray(M)[:, [idx[mul(h, g)] for h in Gr]]
    chi5 = {g: sum(g[i] == i for i in range(6)) - 1 for g in Gr}
    chi10 = {g: (chi5[g] ** 2 - chi5[mul(g, g)]) // 2 for g in Gr}
    E = np.array([[int(next(iter(c))[5] == i) for i in range(6)] for c in c36], dtype=np.int64)
    O36 = reader(c36)
    return dict(G=Gr, idx=idx, mul=mul, inv=inv, perm=perm, closure=closure, cosets=cosets, x=x, r=r, w=w, t=t, C4=C4,
                D10=D10, c90=c90, c36=c36, O90=reader(c90), O36=O36, right=right, chi5=chi5, chi10=chi10, E=E,
                F30=(6 * np.eye(36, dtype=np.int64) - E @ E.T) @ O36)


def parent_readers():
    """The hub's text (18:22): the A6 coset readers, their histories, and the marked Golden adapter. Cited: the
    chi-isotypic part of Q[G/H] has dimension d_chi dim chi^H (Frobenius reciprocity)."""
    A = _a6()
    Gr, mul, inv, closure, right, r, t = A["G"], A["mul"], A["inv"], A["closure"], A["right"], A["r"], A["t"]
    C4, D10, O90, O36 = A["C4"], A["D10"], A["O90"], A["O36"]
    conj = lambda H, g: [mul(mul(g, h), inv(g)) for h in H]
    rk = lambda M: len(_rref_p(M)[1])
    hist = [np.vstack([right(O90, g) for g in [tuple(range(6))] + [functools.reduce(mul, [r] * k) for k in range(1, j)]])
            for j in range(1, 6)]
    psl = closure([A["perm"]((0, 1, 2, 3, 4)), A["perm"]((0, 5), (1, 4))])
    fix6 = lambda g, cs: sum(1 for c in cs if frozenset(mul(g, h) for h in c) == c)
    six = A["cosets"](psl)
    chi5b = {g: fix6(g, six) - 1 for g in Gr}
    m = lambda ch: sp.Rational(sum(ch[h] for h in C4), 4)
    irred = lambda ch: sum(ch[g] ** 2 for g in Gr) == 360
    Ed = carrier.edges()
    H, sig, S5, sgn, U = _six_lines()
    HG = sp.Matrix.hstack(*H)

    def golden(g):
        if g[5] != 5:
            return sp.zeros(10, 1)
        o = list(g[:5])
        return sp.Matrix([1 if (o.index(j) - o.index(i)) % 5 in (1, 4) else -1 for i, j in Ed])
    BG = sp.Matrix.hstack(*[golden(g) for g in Gr])
    BGn = np.array(BG.tolist(), dtype=np.int64)
    marked = [c for c in A["c36"] if next(iter(c))[5] == 5]
    s3 = A["perm"]((0, 1, 2))
    gens5 = [r, s3]
    equi = all(BG[:, A["idx"][mul(a, g)]] == _edge_perm(a[:5]) * BG[:, A["idx"][g]] for a in gens5 for g in Gr)
    return {
        "C4 and D10 generate A6, so O90 and O36 share only the constants: their joint static rank is 90 + 36 - 1 = 125; "
        "<C4, t C4 t> has order 24, so O90 with its t-history has rank 180 - 15 = 165; with both readers and both "
        "t-histories the rank is 230, blind 130 (a rank over a prime and an exact integer kernel)":
            len(closure(list(C4 | D10))) == 360 and rk(np.vstack([O90, O36])) == 125
            and len(closure(list(C4) + conj(C4, t))) == 24 and rk(np.vstack([O90, right(O90, t)])) == 165
            and _exact_rank(np.vstack([O90, O36, right(O90, t), right(O36, t)])) == 230,
        "under the right five-cycle r the O90 history ranks are 90, 170 (<C4, r C4 r^-1> has order 36), 250 (with an exact "
        "kernel), 330 and 360: the fourth is at most 330 because chi5, chi5' and chi10 (irreducible, chi5' from the "
        "transitive A5 = <(01234), (05)(14)>) keep 1, 1 and 2 C4-fixed dimensions, leaving 5 + 5 + 20 unread; four "
        "settings share the constant and stay below 1 + 4 x 89 = 357, so five are needed":
            [rk(Mh) for Mh in hist] == [90, 170, 250, 330, 360] and len(closure(list(C4) + conj(C4, r))) == 36
            and _exact_rank(hist[2]) == 250 and len(psl) == 60 and len({g[0] for g in psl}) == 6
            and all(irred(ch) for ch in (A["chi5"], chi5b, A["chi10"])) and A["chi5"] != chi5b
            and (m(A["chi5"]), m(chi5b), m(A["chi10"])) == (1, 1, 2)
            and 360 - 5 * (5 - 4 * 1) * 2 - 10 * (10 - 4 * 2) == 330 and 1 + 4 * 89 == 357 < 360,
        "marking point 5 selects the six cosets A5/D10, the Sylow-five labels; reading each by the Golden line of its "
        "pentagon (g(0), ..., g(4)) gives B_G = H_G O36(marked), H_G^T H_G = 12 I - 2 J, with rank 5 and B_G B_G^T = "
        "120 P_source, A5-equivariant (B_G(a f) = U(a) B_G f for a = (01234), (012)); O36 U_r = O36 and B_G U_r = B_G, so "
        "under the same r that gives O90 rank 360 the adapter keeps rank 5 and blind 355":
            len(marked) == 6 and all(len({tuple(golden(g)) for g in c}) == 1 for c in marked)
            and all(BG[:, k] in H or BG[:, k].is_zero_matrix for k in range(360))
            and HG.T * HG == 12 * sp.eye(6) - 2 * sp.ones(6, 6) and BG.rank() == 5 and BG * BG.T == 10 * HG * HG.T
            and (HG * HG.T / 12) ** 2 == HG * HG.T / 12 and equi
            and np.array_equal(right(O36, r), O36) and np.array_equal(right(BGn, r), BGn),
        "the normalizer of <r> in A6 is D10; on the 90 cosets of C4 its characters are 90, 0 at the rotations and 2 at the "
        "reflections, so the module is 10 trivial + 8 sign + 18 W4, while 18 copies of the five-point action give 90, 0, "
        "18, which is 18 trivial + 18 W4: an action, not a reader, tells them apart":
            {g for g in Gr if set(conj(closure([r]), g)) == set(closure([r]))} == D10
            and {(Permutation(list(g)).order(), fix6(g, A["c90"])) for g in D10} == {(1, 90), (5, 0), (2, 2)}
            and sp.solve([sp.Symbol("a") + sp.Symbol("b") + 4 * sp.Symbol("c") - 90, sp.Symbol("a") + sp.Symbol("b")
                          - sp.Symbol("c"), sp.Symbol("a") - sp.Symbol("b") - 2], sp.symbols("a b c")) ==
            dict(zip(sp.symbols("a b c"), (10, 8, 18)))
            and sp.solve([sp.Symbol("a") + sp.Symbol("b") + 4 * sp.Symbol("c") - 90, sp.Symbol("a") + sp.Symbol("b")
                          - sp.Symbol("c"), sp.Symbol("a") - sp.Symbol("b") - 18], sp.symbols("a b c")) ==
            dict(zip(sp.symbols("a b c"), (18, 0, 18))),
    }


def two_36s():
    """The hub's text (18:22): the coset 36 and the six-label/duad/syntheme 36 are different A5-sets."""
    A = _a6()
    mul, closure, perm = A["mul"], A["closure"], A["perm"]
    psl = closure([perm((0, 1, 2, 3, 4)), perm((0, 5), (1, 4))])
    stab = [g for g in A["G"] if g[5] == 5]

    def orbits(group, pts, act):
        seen, out = set(), []
        for p in pts:
            if p not in seen:
                o = {act(g, p) for g in group}
                seen |= o
                out.append(len(o))
        return sorted(out)
    cact = lambda g, c: frozenset(mul(g, h) for h in c)
    synth = {frozenset(frozenset(m) for m in mt) for mt in _matchings(range(6))}
    pts = [(0, frozenset([i])) for i in range(6)] + [(1, frozenset(d)) for d in itertools.combinations(range(6), 2)] + [
        (2, s) for s in synth]
    sact = lambda g, p: (p[0], frozenset(g[i] for i in p[1])) if p[0] < 2 else (2, frozenset(
        frozenset(g[i] for i in m) for m in p[1]))
    return {
        "the coset 36 has orbits 6 + 30 under Stab(5) and under the transitive A5 = <(01234), (05)(14)>, while the six "
        "labels, fifteen duads and fifteen synthemes have orbits 6 + 15 + 5 + 10 under the transitive A5: invariant "
        "dimensions 2 and 4, so no A5-module isomorphism identifies the two 36s":
            orbits(stab, A["c36"], cact) == [6, 30] and orbits(psl, A["c36"], cact) == [6, 30] and len(synth) == 15
            and orbits(psl, pts, sact) == [5, 6, 10, 15],
    }


def golden30():
    """The hub's text (18:22): the coset 36 minus its fibre means is a global Golden30 with an exact Return."""
    A = _a6()
    E, F30, O36, right, r, t = A["E"], A["F30"], A["O36"], A["right"], A["r"], A["t"]
    I6, I36 = np.eye(6, dtype=np.int64), np.eye(36, dtype=np.int64)
    K = F30 @ right(F30, t).T
    Kq = K // 12
    rk = lambda M: len(_rref_p(M)[1])
    quad = Kq @ Kq + 3 * Kq - 99 * I36
    Ks = sp.Matrix(Kq)
    sector = sp.Matrix.hstack(*(Ks * Ks + 3 * Ks - 99 * sp.eye(36)).nullspace())
    J, Phi = (2 * Ks + 3 * sp.eye(36)) / 9, (Ks + 6 * sp.eye(36)) / 9
    blocks = []
    for k in range(sector.shape[1]):
        cand = blocks + [Phi * sector[:, k], sector[:, k]]
        if sp.Matrix.hstack(*cand).rank() == len(cand):
            blocks = cand
    S16 = sp.Matrix.hstack(*blocks)
    Bm = sp.Matrix([[1, 1], [1, 0]])
    Es, N5, sym, Fc, a0, b0 = _source()
    H, sig, S5, sgn, U = _six_lines()
    K5 = sym(H[0])
    P5 = sp.eye(5) - sp.ones(5, 5) / 5
    Phi4 = (P5 + K5) / 2
    base = [sp.eye(5)[:, k] - sp.eye(5)[:, 4] for k in range(4)]
    S4 = next(c for c in (sp.Matrix.hstack(v, (K5 * v - v) / 2, w, (K5 * w - w) / 2)
                          for v, w in itertools.combinations(base, 2)) if c.rank() == 4)
    T = S16[:, :4] * (S4.T * S4).inv() * S4.T
    a, z = sp.symbols("a z")
    lo = (sp.Rational(177) - 3 * sp.sqrt(5)) / 200
    return {
        "the 36 cosets fibre over the six points by g D10 -> g(5) (E^T E = 6 I); F30 = 6 P30 O36 with P30 = I - E E^T/6 "
        "has F30 F30^T = 360 P30, rank 30, F30 U_r = F30, and [F30; F30 U_t] has rank 60: present 30, delayed 30, blind "
        "300":
            np.array_equal(E.T @ E, 6 * I6) and np.array_equal(F30 @ F30.T, 60 * (6 * I36 - E @ E.T)) and rk(F30) == 30
            and np.array_equal(right(F30, r), F30) and _exact_rank(np.vstack([F30, right(F30, t)])) == 60,
        "K = 30 A = F30 U_t F30^T/12 is an integral symmetric matrix whose factors K, K + 6, K - 6 and K^2 + 3K - 99 have "
        "nullities 6, 5, 9 and 16 and multiply to zero: its characteristic polynomial is q^6 (q + 6)^5 (q - 6)^9 "
        "(q^2 + 3q - 99)^8, so A has visible eigenvalues -1/5 (5), 1/5 (9) and (-1 +- 3 sqrt5)/20 (8 each) and minimal "
        "polynomial (25 A^2 - 1)(100 A^2 + 10 A - 11)":
            not (K % 12).any() and np.array_equal(Kq, Kq.T)
            and [36 - rk(M) for M in (Kq, Kq + 6 * I36, Kq - 6 * I36, quad)] == [6, 5, 9, 16]
            and not (Kq @ (Kq + 6 * I36) @ (Kq - 6 * I36) @ quad).any()
            and set(sp.solve(100 * a ** 2 + 10 * a - 11, a)) == {(-1 + 3 * sp.sqrt(5)) / 20, (-1 - 3 * sp.sqrt(5)) / 20}
            and sp.expand(9 * (100 * (sp.Symbol("q") / 30) ** 2 + 10 * sp.Symbol("q") / 30 - 11)
                          - (sp.Symbol("q") ** 2 + 3 * sp.Symbol("q") - 99)) == 0,
        "the Return I - A^2 has eigenvalues 24/25 (14) and (177 +- 3 sqrt5)/200 (8 each), all above 17/20; Sigma(z) = "
        "(1 - a^2)/(z + a) gives G(z) = (z + a)/(z^2 - 1), with endpoint weights (1 + a)/2 and (1 - a)/2; and "
        "det[[I, A], [A, I]] = (24/25)^14 (7821/10000)^8 > 0":
            1 - sp.Rational(1, 25) == sp.Rational(24, 25) and sp.expand(1 - ((-1 + 3 * sp.sqrt(5)) / 20) ** 2 - (177 + 3 * sp.sqrt(5)) / 200) == 0
            and sp.expand(1 - ((-1 - 3 * sp.sqrt(5)) / 20) ** 2 - lo) == 0
            and lo > sp.Rational(17, 20)
            and sp.simplify(1 / (z - a - (1 - a ** 2) / (z + a)) - (z + a) / (z ** 2 - 1)) == 0
            and sp.simplify((z + a) / (z ** 2 - 1) - ((1 + a) / 2 / (z - 1) + (1 - a) / 2 / (z + 1))) == 0
            and sp.Rational(24, 25) ** 14 * (sp.expand(lo * (sp.Rational(177) + 3 * sp.sqrt(5)) / 200)) ** 8
            == sp.Rational(24, 25) ** 14 * sp.Rational(7821, 10000) ** 8,
        "on the 16-dimensional sector J = (20 A + I)/3 has J^2 = 5 and Phi16 = (I + J)/2 = (K + 6)/9 has Phi16^2 = "
        "Phi16 + I: eight rational Fibonacci blocks B = [[1, 1], [1, 0]]; and a rank-4 T with Phi16 T = T Phi4 carries "
        "A4's two blocks (the Fibonacci bridge) into them, a marked injection, not an A6 map":
            sector.shape[1] == 16 and (J * J * sector - 5 * sector).is_zero_matrix
            and (Phi * Phi * sector - Phi * sector - sector).is_zero_matrix
            and S16.rank() == 16 and (Phi * S16 - S16 * sp.diag(*[Bm] * 8)).is_zero_matrix
            and T.rank() == 4 and (Phi * T - T * Phi4).is_zero_matrix,
    }


def parent_closure():
    """The hub's text (18:22): the all-word closure of the Golden30 rows, its blind central projector, and one
    character reader that completes the parent."""
    A = _a6()
    Gr, mul, inv, right, r, t, chi5, chi10 = A["G"], A["mul"], A["inv"], A["right"], A["r"], A["t"], A["chi5"], A["chi10"]
    step = lambda B: np.vstack([right(B, r), right(B, t)])
    cent = lambda ch, d: np.array([[d * ch[mul(inv(g), h)] for h in Gr] for g in Gr], dtype=np.int64)
    P10 = cent(chi10, 10)
    Pb = np.ones((360, 360), dtype=np.int64) + cent(chi5, 5) + P10
    c = np.array([[chi10[g] for g in Gr]], dtype=np.int64)
    return {
        "r and t generate A6, and closing the F30 rows under them gives ranks 30, 60, 90, 145, 216, 225, 234 by word "
        "length; 234 is exact, because P_blind[g, h] = (1 + 5 chi5(g^-1 h) + 10 chi10(g^-1 h))/360 (chi5 = fix - 1, "
        "chi10 = (chi5^2 - chi5(g^2))/2) is a symmetric central idempotent of trace 126 = 1 + 25 + 100 that kills F30":
            len(A["closure"]([r, t])) == 360 and _word_ranks(A["F30"], step, 8) == [30, 60, 90, 145, 216, 225, 234, 234, 234]
            and np.array_equal(Pb @ Pb, 360 * Pb) and np.array_equal(Pb, Pb.T) and np.trace(Pb) == 360 * 126
            and not (A["F30"] @ Pb).any(),
        "the six fibre means restore O36, whose closure is 260: chi10 has no D10-fixed vector, and its central projector, "
        "of trace 100, kills O36; one more reader c(f) = sum chi10(g) f_g has a 100-dimensional orbit inside that block, "
        "so O36 and c reach 360, with static rank 37":
            np.array_equal(A["F30"] + A["E"] @ (A["E"].T @ A["O36"]), 6 * A["O36"])
            and _word_ranks(A["O36"], step, 10)[-1] == 260 and np.array_equal(P10 @ P10, 360 * P10)
            and np.trace(P10) == 360 * 100 and not (A["O36"] @ P10).any() and sum(chi10[g] for g in A["D10"]) == 0
            and np.array_equal(c @ P10, 360 * c) and _word_ranks(c, step, 12)[-1] == 100
            and len(_rref_p(np.vstack([A["O36"], c]))[1]) == 37,
    }


def notes_1835():
    """The hub's text (18:22) and the sibling's MODEL (18:33): the rest."""
    W = recurrence.load_walks()
    return {
        "the sibling's note: 6/5 = 8/5 - 2/5, the log2 5 terms cancelling; the hub's walk correction W6 = 17141798400 is "
        "the repository's W_6":
            sp.Rational(4, 5) * 2 - 4 * sp.Rational(1, 20) * 2 == sp.Rational(6, 5) and W[6] == 17141798400,
        "the weighted 49-record atlas: context groups (5, 7, 4, 5, 5, 5, 5) weighted 1/(7n) give 25 contexts of weight "
        "1/35, seven of 1/49 and four of 1/28 (total 1); pairing inside these pools gives 12 + 3 + 2 = 17 pairs per slot, "
        "so three slots hold 51 >= 49 = 12 + 12 + 25 records in 98 cells, while pairing inside the groups gives 15 and "
        "only 45; and C(252, 2) = 31626 two-cell locations":
            25 * sp.Rational(1, 35) + 7 * sp.Rational(1, 49) + 4 * sp.Rational(1, 28) == 1
            and 25 // 2 + 7 // 2 + 4 // 2 == 17 and 3 * 17 == 51 >= 49 == 12 + 12 + 25 and 2 * 49 == 98
            and 5 * (5 // 2) + 7 // 2 + 4 // 2 == 15 and 3 * 15 == 45 < 49 and 252 * 251 // 2 == 31626 == 36 * 7 * 251 // 2,
    }


def notes_1909():
    """The sibling's MODEL (19:00-19:15): the exact claims among its readings."""
    D = 15 * sp.eye(4) - 3 * sp.ones(4, 4)
    P = [sp.eye(4)[:, k] for k in range(4)] + [-sp.ones(4, 1)]
    reads = sp.Matrix(5, 5, lambda i, j: (P[i].T * D * P[j])[0] / 3)
    H, sig, S5, sgn, U = _six_lines()
    p = (1, 0, 2, 3, 4)
    fixed_atoms = sum(p[i] == i for i in range(5)) + sum(tuple(sorted((p[i], p[j]))) == (i, j) for i, j in carrier.edges())
    fixed_duads = sum({sig[p][a], sig[p][b]} == {a, b} for a, b in itertools.combinations(range(6), 2))
    t = sp.Symbol("t")
    return {
        "the fixed dark detector p_s/3 reads 4 on its own plane and -1 on the other four, summing to 0":
            reads == 5 * sp.eye(5) - sp.ones(5, 5) and all(sum(reads.row(i)) == 0 for i in range(5)),
        "a transposition fixes 3 vertices and 4 edges, trace 7 on the native 15, but in the exceptional action it fixes "
        "3 of the 15 duads of the six Sylow labels, trace 3: the two 15s are different S5-modules":
            fixed_atoms == 7 and fixed_duads == 3 and all(sig[p][a] != a for a in range(6)),
        "the metric polynomial's factor t^2 - 60 t + 27 has roots 30 +- 3 sqrt97, the larger below 60 since 97 < 100":
            set(sp.solve(t ** 2 - 60 * t + 27, t)) == {30 - 3 * sp.sqrt(97), 30 + 3 * sp.sqrt(97)} and 30 + 3 * sp.sqrt(97) < 60,
    }


def _address():
    """The hub's address map (19:39): address(j) = r^p c_q with p = 4j mod 5, q = floor((j mod 864)/12) and c_q the
    least elements of the 72 left r-cycles of A6."""
    A = _a6()
    Gr, mul, r = A["G"], A["mul"], A["r"]
    seen, reps = set(), []
    for g in Gr:
        if g not in seen:
            cyc = [g]
            for _ in range(4):
                cyc.append(mul(r, cyc[-1]))
            seen |= set(cyc)
            reps.append(min(cyc))
    reps = sorted(reps)
    rp = [functools.reduce(mul, [r] * k, tuple(range(6))) for k in range(5)]
    address = lambda j: mul(rp[(4 * j) % 5], reps[(j % 864) // 12])
    address.reps = reps
    return address


def address_map():
    """The hub's text (19:39): the 4320 circle addresses the 360 parent's settings without becoming their dynamics."""
    A = _a6()
    Gr, mul, inv, r = A["G"], A["mul"], A["inv"], A["r"]
    address = _address()
    reps = address.reps
    d = tuple([(2 * i) % 5 for i in range(5)] + [5])
    Cd = lambda a: mul(mul(d, a), inv(d))

    def orbits(points, moves):
        seen, out = set(), []
        for a in points:
            if a not in seen:
                o, new = {a}, [a]
                while new:
                    new = [y for x in new for y in (m(x) for m in moves) if y not in o and not o.add(y)]
                seen |= o
                out.append(len(o))
        return Counter(out)
    images = Counter(address(j) for j in range(4320))
    return {
        "address(j) = r^p c_q with p = 4j mod 5, q = floor((j mod 864)/12) and c_q the least elements of the 72 left "
        "r-cycles of A6 sends the 4320 circle onto the 360 settings, twelve to one, with address(j + 864) = r address(j)":
            len(reps) == 72 and set(images.values()) == {12} and len(images) == 360
            and all(address((j + 864) % 4320) == mul(r, address(j)) for j in range(4320)),
        "under the clock's F20 (j -> j + 864 and the doubling j -> 3457 j) every orbit has five states, but on the "
        "settings (left r and conjugation by the doubling d, odd in S6) the orbits are 5^4 10^2 20^16, so an equivariant "
        "image covers at most 20 settings: no natural equivariant address exists, and this one has 4200 doubling "
        "mismatches (a selected scheduling convention)":
            set(orbits(range(4320), [lambda j: (j + 864) % 4320, lambda j: (3457 * j) % 4320])) == {5}
            and orbits(Gr, [lambda a: mul(r, a), Cd]) == Counter({5: 4, 10: 2, 20: 16})
            and Permutation(list(d)).is_odd and 3457 % 5 == 2
            and sum(address((3457 * j) % 4320) != Cd(address(j)) for j in range(4320)) == 4200,
    }


def notes_1950():
    """The hub's text (19:39) and the sibling's MODEL (19:37-20:02): the rest."""
    A = _a6()
    Gr, mul, right, r = A["G"], A["mul"], A["right"], A["r"]
    Bm = sp.Matrix([[1, 1], [1, 0]])
    c = np.array([[A["chi10"][g] for g in Gr]], dtype=np.int64)
    order = lambda g: next(k for k in range(1, 7) if functools.reduce(mul, [g] * k) == tuple(range(6)))
    orders = Counter(order(g) for g in Gr)
    sylow = {frozenset(functools.reduce(mul, [g] * k, tuple(range(6))) for k in range(5)) for g in Gr if order(g) == 5}
    w = [1, -3, 3, -1]
    M = sp.Matrix(carrier.signless_incidence())
    return {
        "a Fibonacci block cannot meet an order-five tick: B^5 = [[8, 5], [5, 3]] has det(B^5 - I) = -11 and the native "
        "Phi4 has det(Phi4^5 - I) = 121, so T Phi4 = R T with R^5 = I forces T (Phi4^5 - I) = 0 and T = 0":
            Bm ** 5 == sp.Matrix([[8, 5], [5, 3]]) and (Bm ** 5 - sp.eye(2)).det() == -11
            and (sp.diag(Bm, Bm) ** 5 - sp.eye(4)).det() == 121,
        "under powers of r alone the 37-channel reader (O36 and the chi10 reader) reaches ranks 37, 38, 39, 40, 41, leaving "
        "319 blind: waiting on the five-cycle does not install t":
            _word_ranks(np.vstack([A["O36"], c]), lambda B_: right(B_, r), 5) == [37, 38, 39, 40, 41, 41],
        "the sibling's notes: the weights 1, -3, 3, -1 kill every quadratic, with moments -6, -36, -150 and -540 at "
        "degrees 3 to 6; A6 has 1, 45, 80, 90 and 144 elements of orders 1 to 5, none of order 6, and its 144 of order 5 "
        "form 36 subgroups; M^T M on the ten edges has spectrum 0^5 3^4 8^1":
            [sum(x * k ** j for k, x in enumerate(w)) for j in range(7)] == [0, 0, 0, -6, -36, -150, -540]
            and orders == Counter({1: 1, 2: 45, 3: 80, 4: 90, 5: 144}) and len(sylow) == 36
            and sorted((M.T * M).eigenvals().items()) == [(0, 5), (3, 4), (8, 1)],
    }


def notes_2033():
    """Drive check 20:33: the hub's text (20:20), the sibling's MODEL (20:08-21:02) and the owner's monograph (20:13)."""
    A = _a6()
    Gr, mul = A["G"], A["mul"]
    e6 = tuple(range(6))
    cyc = lambda g: sorted(len(c) for c in Permutation(list(g)).full_cyclic_form)
    order3 = Counter(tuple(cyc(g)) for g in Gr if functools.reduce(mul, [g] * 3) == e6 and g != e6)
    order4 = Counter(tuple(cyc(g)) for g in Gr if functools.reduce(mul, [g] * 4) == e6
                     and functools.reduce(mul, [g] * 2) != e6)
    fix0 = [g for g in Gr if g[0] == 0]
    sizes = [5, 7, 4, 5, 5, 5, 5]
    groups = [list(range(sum(sizes[:k]), sum(sizes[:k + 1]))) for k in range(7)]
    w = {i: sp.Rational(1, 7 * len(gr)) for gr in groups for i in gr}
    mu1, mu2 = sum(w[i] * i for i in w), sum(w[i] * i * i for i in w)
    sq = sum(x * x for x in w.values())
    M = sp.Matrix(carrier.signless_incidence())
    K = M.T * M
    I10, J10 = sp.eye(10), sp.ones(10, 10)
    P0, P3, P8 = (K - 3 * I10) * (K - 8 * I10) / 24, K * (8 * I10 - K) / 15, K * (K - 3 * I10) / 40
    PA4 = sp.eye(5) - sp.ones(5, 5) / 5
    H = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], [-1, -1, -1, -1]])
    G = M.T * H
    rk = lambda rows: G.extract(list(rows), list(range(4))).rank()
    four_fail = [S for S in itertools.combinations(range(10), 4) if rk(S) < 4]
    five_ok = all(rk(S) == 4 for S in itertools.combinations(range(10), 5))
    E = carrier.edges()
    shape = lambda S: tuple(sorted(Counter(v for k in S for v in E[k]).values()))
    witness = M.T * sp.Matrix([1, -1, 1, -1, 0])
    weights = {sum(1 for t in (G * sp.Matrix(c)) if t != 0) for c in itertools.product(range(-1, 2), repeat=4) if any(c)}
    x = sp.Symbol("x")
    phi5 = sp.cyclotomic_poly(5, x)
    norm = lambda f: sp.resultant(phi5, f, x)
    red = lambda f: sp.rem(sp.expand(f), phi5, x)
    comp = sp.Matrix([[0, 0, 0, -1], [1, 0, 0, -1], [0, 1, 0, -1], [0, 0, 1, -1]])
    alpha = 2 * sp.eye(4) + comp - comp ** 2
    cp = alpha.charpoly(x).as_expr()
    run = [sp.Rational((-1) ** r * sp.binomial(3, r), 8) for r in range(4)]
    eps = sp.Symbol("epsilon")
    Bf = sp.Matrix([[1, 1], [1, 0]])
    # the monograph's Golden15 stiffness on the 15 atoms
    U15 = sp.diag(sp.Matrix(5, 5, lambda a, b: int(a == (b + 1) % 5)), counts._edge_action(lambda i: (i + 1) % 5).applyfunc(abs))
    D15 = sp.diag(sp.Matrix(5, 5, lambda a, b: int(a == (2 * b) % 5)), counts._edge_action(lambda i: (2 * i) % 5).applyfunc(abs))
    R15 = 3 * sp.eye(15) - U15 - U15.T
    PF = sum((U15 ** k for k in range(5)), sp.zeros(15)) / 5
    Ravg = (R15 + D15 * R15 * D15.T) / 2
    # the 224 saddle: the transverse quartic
    Rt = glue.roots()
    a = Rt[0]
    y = np.array([0, 0, 1, 2, -1, 0, 3, 1], dtype=float)
    y -= (y @ a) / (a @ a) * a
    y /= np.linalg.norm(y)
    s7 = sum((r @ y) ** 4 for r in Rt if abs(r @ a) < 1e-9)
    s112 = sum((r @ y) ** 4 for r in Rt if abs(abs(r @ a) - 1) < 1e-9)
    # the sibling's 60 that fix the carrier line, against the tick's PSL(2,5)
    psl = {cyclotomic.on_lines(cyclotomic.on_plane(W)) for W in cyclotomic.centralizer()}
    rl = cyclotomic.on_lines(cyclotomic.on_plane(cyclotomic.clocks()["r"]))
    line = next(i for i in range(6) if rl[i] == i)
    even6 = [p for p in itertools.permutations(range(6)) if Permutation(list(p)).is_even]
    stab = {p for p in even6 if p[line] == line}
    # S5 characters on the source, the cycles and the dark four
    maps = [tuple(p) for p in itertools.permutations(range(5))]
    chiV = lambda p: sum(p[i] == i for i in range(5))
    chiE = lambda p: sum(1 for i, j in E if {p[i], p[j]} == {i, j})
    sgn = lambda p: 1 if Permutation(list(p)).is_even else -1
    chiS = lambda p: counts._edge_action(lambda i: p[i]).trace()
    src = {p: chiE(p) - chiV(p) for p in maps}
    cyc6 = {p: chiS(p) - (chiV(p) - 1) for p in maps}
    dark = {p: sgn(p) * (chiV(p) - 1) for p in maps}
    tw = {p: sgn(p) * src[p] for p in maps}
    ip = lambda f, g: sp.Rational(sum(f[p] * g[p] for p in maps), 120)
    prod_ = {p: dark[p] * src[p] for p in maps}
    v4 = [(0, 1, 2, 3, 4), (1, 0, 3, 2, 4), (2, 3, 0, 1, 4), (3, 2, 1, 0, 4)]
    fixed = lambda ch: sp.Rational(sum(ch[p] for p in v4), 4)
    return {
        "A6's 80 elements of order 3 are 40 three-cycles and 40 products of two, its 90 of order 4 are a 4-cycle times a "
        "transposition, and each point is fixed by 15 double transpositions and 24 five-cycles (the sibling, 20:08-21:02)":
            order3 == Counter({(1, 1, 1, 3): 40, (3, 3): 40}) and order4 == Counter({(2, 4): 90})
            and sum(1 for g in fix0 if cyc(g) == [1, 1, 2, 2]) == 15 and sum(1 for g in fix0 if cyc(g) == [1, 5]) == 24,
        "the weighted contexts (5, 7, 4, 5, 5, 5, 5) with weights 1/(7 n) have index moments 251/14 and 5983/14 and "
        "squared weight 39/1372 = (351/343)/36; their weight steps are 2/245 and 1/140, the repaired gamma are 2/35, "
        "12/343 and 9/112, (36/343) x 28 = 144/49, C(36, 3) = 7140, and a quadratic code of context distance 34 corrects "
        "16 errors or 33 erasures (the hub, 20:20)":
            sum(sizes) == 36 and (mu1, mu2) == (sp.Rational(251, 14), sp.Rational(5983, 14))
            and sq == sp.Rational(39, 1372) == sp.Rational(351, 343) / 36
            and (sp.Rational(1, 35) - sp.Rational(1, 49), sp.Rational(1, 28) - sp.Rational(1, 35)) == (sp.Rational(2, 245), sp.Rational(1, 140))
            and [sp.Rational(1, 35) * 2, sp.Rational(1, 49) * (1 + sp.Rational(5, 7)), sp.Rational(1, 28) * (1 + sp.Rational(5, 4))]
            == [sp.Rational(2, 35), sp.Rational(12, 343), sp.Rational(9, 112)]
            and sp.Rational(36, 343) * 28 == sp.Rational(144, 49) and sp.binomial(36, 3) == 7140
            and (34 - 1) // 2 == 16 and 34 - 1 == 33,
        "the dark code is range P3: with K = M^T M (K^2 = 3K + 4J) the projectors (K - 3)(K - 8)/24, K(8 - K)/15 = "
        "M^T P_A4 M/3 and K(K - 3)/40 sum to I, and c = M^T x on the zero-sum x is a [10, 4, 6] code: every five edges "
        "span it, exactly 25 of the 210 four-edge sets fail (15 four-cycles with an isolated vertex, 10 triangles with a "
        "disjoint edge), and (1, -1, 1, -1, 0) has weight 6 (the hub, 20:20)":
            K * K == 3 * K + 4 * J10 and P0 + P3 + P8 == I10 and P3 * P3 == P3 and P3 == M.T * PA4 * M / 3
            and P3.rank() == 4 and (P3 * G - G).is_zero_matrix and five_ok and len(four_fail) == 25
            and Counter(shape(S) for S in four_fail) == Counter({(2, 2, 2, 2): 15, (1, 1, 2, 2, 2): 10})
            and sum(1 for t in witness if t != 0) == 6 and min(weights) == 6,
        "2 + zeta - zeta^2 has norm 31 and squared modulus (13 + 3 sqrt5)/2 = 8 + 3(zeta + zeta^4), and times 5 - 8 zeta + zeta^2 - 10 zeta^3 "
        "it is 31; its companion has characteristic polynomial x^4 - 8x^3 + 24x^2 - 37x + 31, which is 31, 11, 5, 1 at 0, "
        "1, 2, 3, and 6 + sqrt5 also has norm 31. Correction to the monograph: its 3 - zeta - zeta^4 + 2 zeta^2 has norm "
        "61, not 31, so its 155 = 5 x 31 does not come from that element":
            norm(2 + x - x ** 2) == 31 and norm(3 - x - x ** 4 + 2 * x ** 2) == 61
            and sp.expand(red((2 + x - x ** 2) * (2 + x ** 4 - x ** 3)) - red(8 + 3 * x + 3 * x ** 4)) == 0
            and red((2 + x - x ** 2) * (5 - 8 * x + x ** 2 - 10 * x ** 3)) == 31
            and sp.expand(cp - (x ** 4 - 8 * x ** 3 + 24 * x ** 2 - 37 * x + 31)) == 0
            and [cp.subs(x, t) for t in range(4)] == [31, 11, 5, 1] and 36 - 5 == 31,
        "the run-parity weights (1, -3, 3, -1)/8 annihilate quadratics and leak -3/4 of a cubic; a linear gain drift "
        "gives 1 + 3 epsilon/2; the odd and even contrasts have variance factors 5/16 and 5/4; and the sixth Fibonacci "
        "matrix [[13, 8], [8, 5]] sums to 34, not 27 (the separate model's correction, 20:40)":
            all(sum(run[r] * r ** d for r in range(4)) == 0 for d in range(3))
            and sum(run[r] * (-1) ** r for r in range(4)) == 1 and sum(run[r] * r ** 3 for r in range(4)) == sp.Rational(-3, 4)
            and sp.expand(sum(run[r] * (-1) ** r * (1 + eps * r) for r in range(4))) == 1 + 3 * eps / 2
            and sum(t * t for t in run) == sp.Rational(5, 16) and sum((2 * t) ** 2 for t in run) == sp.Rational(5, 4)
            and Bf ** 6 == sp.Matrix([[13, 8], [8, 5]]) and sum(Bf ** 6) == 34,
        "the monograph's Golden15 stiffness R = 3 - U - U^T on the fifteen atoms has characteristic polynomial "
        "(x - 1)^3 (x^2 - 7x + 11)^6, determinant 11^6 and inverse (R^2 - 8R + 18)/11; R - D R D^T has rank 12, and the "
        "F20 average is P_F + (7/2)(I - P_F), off R by Tr = 15":
            sp.factor(R15.charpoly(x).as_expr()) == (x - 1) ** 3 * (x ** 2 - 7 * x + 11) ** 6 and R15.det() == 11 ** 6
            and R15 * (R15 ** 2 - 8 * R15 + 18 * sp.eye(15)) == 11 * sp.eye(15) and (R15 - D15 * R15 * D15.T).rank() == 12
            and Ravg == PF + sp.Rational(7, 2) * (sp.eye(15) - PF) and ((R15 - Ravg) ** 2).trace() == 15,
        "correction to the monograph: at the 224 saddle the transverse quartic is -rho^4/2, not 0, since the 126 E7 roots "
        "give sum (y.r)^4 = 24|y|^4 and the 112 oblique roots 12|y|^4, not 18 each; so its collar regime II rests on an "
        "expansion missing that term":
            abs(s7 - 24) < 1e-9 and abs(s112 - 12) < 1e-9 and abs(-(s7 - s112) / 24 + 0.5) < 1e-9,
        "correction to the sibling: the 60 even permutations that fix the carrier line are a point stabilizer A5, not "
        "the tick's PSL(2,5), which is transitive on the six lines and meets it in 10; the two are the two classes of "
        "A5 in A6":
            len(stab) == 60 and len(psl) == 60 and psl != stab and len(psl & stab) == 10
            and {s[0] for s in psl} == set(range(6)),
        "the hub's selection rule, from S5 characters: the source (ker M), the cycles and the dark four (A4 twisted by "
        "the sign) have dimensions 5, 6, 4; a Klein four fixing one vertex fixes 2, 0 and 1 of them; Hom(dark, cycles) = "
        "Hom(source, cycles) = 0; and dark x source = 6 + 5 + 5 + 4 holds the cycles, the source, its sign twist and the "
        "dark four once each":
            (src[tuple(range(5))], cyc6[tuple(range(5))], dark[tuple(range(5))]) == (5, 6, 4)
            and (fixed(src), fixed(cyc6), fixed(dark)) == (2, 0, 1) and ip(dark, cyc6) == 0 and ip(src, cyc6) == 0
            and [ip(prod_, ch) for ch in (cyc6, src, tw, dark)] == [1, 1, 1, 1] and ip(prod_, prod_) == 4
            and all(ip(ch, ch) == 1 for ch in (src, cyc6, dark, tw)) and ip(src, tw) == 0,
    }


def notes_2117():
    """The sibling's MODEL (21:05-21:17) and maps29.ts: the circle as a ring, read on the tick."""
    N = 4320
    ring = lambda a, b: (a * b) % N
    neg = lambda a: (-a) % N
    ticks = (864, 1728, 2592, 3456)
    meets = lambda x: 864 in {(k * x) % N for k in range(N // gcd(x, N) + 1)}
    first = lambda x: next((k * x) % N for k in range(1, N) if (k * x) % N in ticks)
    depth = lambda x: next(k for k in range(1, N + 1) if (k * x) % N == 864)
    idem = (3105, 2080, 3456)
    seed = [-3, 1, 2, 0, -1, 0, -2, 1, -1, 3]
    petal = 6 * sp.eye(6) - sp.ones(6, 6)
    Bf = sp.Matrix([[1, 1], [1, 0]])
    golden = [(216 * k) % N for k in range(20)]
    cyc = [864]
    for _ in range(4):
        cyc.append(ring(2, cyc[-1]))
    return {
        "3105, 2080 and 3456 are orthogonal idempotents of Z/4320 summing to 1, and 2241 = 3105 + 3456 is the idempotent "
        "of Z/160 (it kills 2080); every frame is 3105 (j mod 32) + 2080 (j mod 27) + 3456 (j mod 5) and also 2241 "
        "(j mod 160) + 2080 (j mod 27), both maps recover all 4320 frames, and the mirrors of 3456, 2080 and 3105 are "
        "864, 2240 and 1215":
            all(ring(e, e) == e for e in idem + (2241,)) and all(ring(a, b) == 0 for a, b in itertools.combinations(idem, 2))
            and sum(idem) % N == 1 and (3105 + 3456) % N == 2241 and ring(2241, 2080) == 0
            and all((3105 * (j % 32) + 2080 * (j % 27) + 3456 * (j % 5)) % N == j
                    and (2241 * (j % 160) + 2080 * (j % 27)) % N == j for j in range(N))
            and (neg(3456), neg(2080), neg(3105)) == (864, 2240, 1215),
        "the tick squares to 3456, its mirror; 3456 and 2241 fix the tick while 3105 and 2080 kill it; the landings 1728 "
        "and 2592 square to the tick; the half-turn 2160 lies 432 (of order 10) from both and squares to 0; and 3456 "
        "fixes the four landings and kills the half-turn, 3105 does the opposite and 2080 kills all five":
            ring(864, 864) == 3456 == neg(864) and ring(3456, 864) == 864 == ring(2241, 864)
            and ring(3105, 864) == 0 == ring(2080, 864) and ring(1728, 1728) == 864 == ring(2592, 2592)
            and 2160 - 1728 == 2592 - 2160 == 432 and N // gcd(432, N) == 10 and ring(2160, 2160) == 0
            and all(ring(3456, t) == t and ring(3105, t) == 0 for t in ticks) and ring(3456, 2160) == 0
            and ring(3105, 2160) == 2160 and all(ring(2080, t) == 0 for t in ticks + (2160,)),
        "a level meets the tick exactly when 5 does not divide it, that is when its gcd with 4320 divides 864: 6, 7, 8, 9, "
        "13, 27, 32, 36, 216, 224 and 256 meet it, and 5, 10, 15, 30, 60, 90, 120, 170, 240, 250, 330, 360 and 2160 miss "
        "it; the readers climb 90, 170, 250, 330, 360 by 80, 80, 80, 30, and 12 x 360 = 5 x 864 = 4320":
            all(meets(x) == (x % 5 != 0) == (864 % gcd(x, N) == 0) for x in range(1, 400))
            and all(meets(x) for x in (6, 7, 8, 9, 13, 27, 32, 36, 216, 224, 256))
            and not any(meets(x) for x in (5, 10, 15, 30, 60, 90, 120, 170, 240, 250, 330, 360, 2160))
            and [170 - 90, 250 - 170, 330 - 250, 360 - 330] == [80, 80, 80, 30] and 12 * 360 == 5 * 864 == N,
        "a unit of residue r mod 5 first lands on 864 r: the host 7 lands on 1728 and reaches the tick in 2592 steps, the "
        "oak 13 lands on 2592 and reaches it in 1728, and the depths add to the circle; the landings 864 r reach the tick "
        "in r^-1 mod 5 = 1, 3, 2, 4 steps, mirror pairs adding to 5":
            all(first(u) == 864 * (u % 5) for u in range(1, 200) if gcd(u, N) == 1)
            and (first(7), depth(7), first(13), depth(13)) == (1728, 2592, 2592, 1728) and depth(7) + depth(13) == N
            and [depth(864 * r) for r in (1, 2, 3, 4)] == [pow(r, -1, 5) for r in (1, 2, 3, 4)] == [1, 3, 2, 4],
        "doubling cycles the landings 864 -> 1728 -> 3456 -> 2592 -> 864 and kills the half-turn; on the twenty golden "
        "ticks 216 k the mirror fixes 0 and 2160 and pairs the other eighteen":
            cyc == [864, 1728, 3456, 2592, 864] and ring(2, 2160) == 0 and len(set(golden)) == 20
            and sorted(t for t in golden if neg(t) == t) == [0, 2160] and all(neg(t) in golden for t in golden),
        "maps29.ts: the petal 6I - J and the dark Gram 2(6I - J) have zero row sums, so each of the six dark lines is minus "
        "the sum of the other five; the golden parent's sixth power is [[13, 8], [8, 5]], of determinant 1, and its "
        "seventh has determinant -1; the seed has squared length 30; an address and a phase leave a fiber of 24":
            (petal * sp.ones(6, 1)).is_zero_matrix and sorted(petal.eigenvals().items()) == [(0, 1), (6, 5)]
            and Bf ** 6 == sp.Matrix([[13, 8], [8, 5]]) and (Bf ** 6).det() == 1 and (Bf ** 7).det() == -1
            and sum(v * v for v in seed) == 30 and sum(1 for j in range(N) if j % 36 == 0 and (4 * j) % 5 == 0) == 24,
    }


def notes_2150():
    """The sibling's MODEL (21:19-21:46): the circle's idempotent images, the digit cycles and the traceless five."""
    N = 4320
    ring = lambda a, b: (a * b) % N
    ticks = (864, 1728, 2592, 3456)
    first = lambda x: next((k * x) % N for k in range(1, N + 1) if (k * x) % N in ticks)
    digits = (471, 714, 147, 174, 741, 417)
    q = [sp.Integer(1)] + [sp.Rational(-1, 3)] * 3 + [sp.Integer(0)]
    pairs = list(itertools.combinations(q, 2))
    x = sp.Symbol("x")
    comp = x ** 4 - 8 * x ** 3 + 24 * x ** 2 - 37 * x + 31
    cubic = lambda t: 135 * t ** 3 - 180 * t ** 2 + 54 * t - 2
    return {
        "multiplication by 3105, 2080, 3456 and 2241 lands on the 32 multiples of 135, the 27 of 160, the 5 tick levels and "
        "the 160 multiples of 27, fixing 135, 160, 864 and 27; the phase idempotent sends a frame of residue r to the "
        "mirror landing -864 r; and the multiples of 27 are the multiples of 135 plus the five tick levels":
            [len({ring(e, j) for j in range(N)}) for e in (3105, 2080, 3456, 2241)] == [32, 27, 5, 160]
            and [ring(e, f) for e, f in ((3105, 135), (2080, 160), (3456, 864), (2241, 27))] == [135, 160, 864, 27]
            and all(ring(3456, j) == (-864 * (j % 5)) % N for j in range(N))
            and {(a + b) % N for a in range(0, N, 135) for b in (0,) + ticks} == set(range(0, N, 27)),
        "the golden tick 216 k is 1080 (k mod 4) + 3456 (k mod 5), so 2 x 1080 = 2160 and the sixth golden tick 1296 is "
        "the half-turn plus the reverse tick; 1296 squares to 3456 and 3105 sends it to 2160; 351 = 13 x 27 squares to "
        "2241, is killed by 2080, fixed by 2241 and sent to 3456 by the phase idempotent":
            all((216 * k) % N == (1080 * (k % 4) + 3456 * (k % 5)) % N for k in range(20)) and (2160 + 3456) % N == 1296
            and ring(1296, 1296) == 3456 and ring(3105, 1296) == 2160 and 13 * 27 == 351 and ring(351, 351) == 2241
            and ring(2080, 351) == 0 and ring(2241, 351) == 351 and ring(3456, 351) == 3456,
        "the digit cycles 471, 714, 147 and 174, 741, 417 each sum to 1332 = 36 x 37 = 1296 + 36; all six are 12 mod 27, "
        "so 2080 sends them to 3360 = 21 x 160, and their phase images are 864, 2592, 3456 twice each; 351 = 9 x 39 and "
        "741 = 19 x 39 have gcd 39 and lcm 6669, and 39 meets 4320 only in 3":
            sum(digits[:3]) == sum(digits[3:]) == 1332 == 36 * 37 == 1296 + 36 and all(d % 27 == 12 for d in digits)
            and {ring(2080, d) for d in digits} == {3360} and 3360 == 21 * 160
            and sorted(ring(3456, d) for d in digits) == [864, 864, 2592, 2592, 3456, 3456]
            and (gcd(351, 741), lcm(351, 741), gcd(39, N)) == (39, 6669, 3),
        "the landing 864 x = 864 (x mod 5) depends only on the residue, and it is the first tick level the multiples of x "
        "reach for every unit (7, 13, 29 and 37 among them) but not always otherwise: 147, 148 and 153 first reach 3456, "
        "1728 and 1728 rather than 1728, 2592 and 2592, while the non-unit 1332 does reach its 1728":
            all(ring(864, j) == 864 * (j % 5) for j in range(N))
            and all(first(u) == 864 * (u % 5) for u in (7, 13, 29, 37))
            and (first(147), first(148), first(153)) == (3456, 1728, 1728) and first(1332) == 1728,
        "the traceless five (1, -1/3, -1/3, -1/3, 0) has square sum 4/3 and cube sum 8/9, its ten pair sums have square "
        "sum 4 and cube sum 8/9, and 60 x 4/3 = 80; the companion polynomial is 31, 11, 5, 1, 11, 71 at 0 to 5; the cubic "
        "135t^3 - 180t^2 + 54t - 2 changes sign between 0.043 and 0.044; sqrt(5/3), sqrt3 and sqrt15 round to 1.291, "
        "1.732 and 3.873, while sqrt(16/3) is 2.309, not 2.306":
            (sum(t * t for t in q), sum(t ** 3 for t in q)) == (sp.Rational(4, 3), sp.Rational(8, 9))
            and (sum((a + b) ** 2 for a, b in pairs), sum((a + b) ** 3 for a, b in pairs)) == (4, sp.Rational(8, 9))
            and 60 * sp.Rational(4, 3) == 80 and [comp.subs(x, t) for t in range(6)] == [31, 11, 5, 1, 11, 71]
            and cubic(sp.Rational(43, 1000)) < 0 < cubic(sp.Rational(44, 1000))
            and [round(float(sp.sqrt(v)), 3) for v in (sp.Rational(5, 3), 3, 15, sp.Rational(16, 3))]
            == [1.291, 1.732, 3.873, 2.309],
    }


def notes_2222():
    """The hub's text (21:54) and the sibling's MODEL (21:57-22:21): the Dirac syndrome polynomial, the encoder
    variants' moments, and the landing count."""
    N = 4320
    ring = lambda a, b: (a * b) % N
    ticks = (864, 1728, 2592, 3456)
    first = lambda x: next(((k * x) % N for k in range(1, N + 1) if (k * x) % N in ticks), None)
    units = [x for x in range(N) if gcd(x, N) == 1]
    others = [x for x in range(1, N) if gcd(x, N) > 1 and x % 5]
    M = sp.Matrix(carrier.signless_incidence())
    K = M.T * M
    I10, J10 = sp.eye(10), sp.ones(10, 10)
    P0, P3, P8 = (K - 3 * I10) * (K - 8 * I10) / 24, K * (8 * I10 - K) / 15, K * (K - 3 * I10) / 40
    SD = P0 + P8
    A = SD - I10 / 15
    subsets = [S for r in range(1, 5) for S in itertools.combinations(range(10), r)]
    minors = [A.extract(list(S), list(S)).det() for S in subsets]
    tight = [S for S in itertools.combinations(range(10), 4) if A.extract(list(S), list(S)).det() == 0]
    E = carrier.edges()
    disjoint = lambda S: sum(1 for a, b in itertools.combinations(S, 2) if not set(E[a]) & set(E[b]))
    T = (K ** 2 - 7 * K - 2 * I10) / 2
    V = SD * T
    sizes = [5, 7, 4, 5, 5, 5, 5]
    w = [sp.Rational(1, 7 * n) for n in sizes for _ in range(n)]
    t = [sp.Rational(2 * c - 35, 35) for c in range(36)]
    mu1, mu2 = sum(a * b for a, b in zip(w, t)), sum(a * b * b for a, b in zip(w, t))
    f1 = [b - mu1 for b in t]
    gam = sum(a * c * (b * b - mu2) for a, b, c in zip(w, t, f1)) / sum(a * c * c for a, c in zip(w, f1))
    f2 = [b * b - mu2 - gam * c for b, c in zip(t, f1)]
    nu = (sum(a * c * c for a, c in zip(w, f1)), sum(a * c * c for a, c in zip(w, f2)))
    lab = lambda u: [(u * i) % 36 for i in range(36)]
    vd = lambda L: min(abs((L[i + 1] - L[i]) * (L[i + 2] - L[i]) * (L[i + 2] - L[i + 1])) for i in range(34))
    best = {u: vd(lab(u)) for u in range(36) if gcd(u, 36) == 1}
    return {
        "correction to this repository's 21:50 statement (the sibling, 21:57-22:21): the landing 864 x is the first tick "
        "level reached by all 1152 units and also by 328 of the 2304 non-units prime to 5, 1332 among them, so being a "
        "unit is sufficient, not necessary":
            len(units) == 1152 and all(first(u) == ring(864, u) for u in units)
            and len(others) == 2304 and sum(first(x) == ring(864, x) for x in others) == 328 and first(1332) == 1728,
        "the hub's sharp dark syndrome floor: with S_D = P0 + P8, all 385 principal minors of orders 1 to 4 of "
        "S_D - I/15 are nonnegative, so every error on at most four edges keeps ||S_D e||^2 >= ||e||^2/15, with "
        "equality on exactly ten supports, an edge with its complementary triangle (the hub, 21:54)":
            len(subsets) == 385 and all(m >= 0 for m in minors) and len(tight) == 10
            and all(disjoint(S) == 3 and len({v for k in S for v in E[k]}) == 5 for S in tight),
        "one polynomial makes those errors: T = (K^2 - 7K - 2I)/2 = 2J - 2K - I = -P0 - 7P3 + 3P8, whose columns are -3 "
        "on their edge and +2 on the complementary triangle; V = S_D T has V V^T = P0 + 9P8 and (V - (3/10)J)"
        "(V - (3/10)J)^T = P0, the source projector":
            T == 2 * J10 - 2 * K - I10 == -P0 - 7 * P3 + 3 * P8 and P8 == J10 / 10
            and {tuple(sorted(T[:, e])) for e in range(10)} == {(-3, 0, 0, 0, 0, 0, 0, 2, 2, 2)}
            and V * V.T == P0 + 9 * P8 and (V - 3 * J10 / 10) * (V - 3 * J10 / 10).T == P0,
        "the hub's orthogonal-feature encoder on t_c = (2c - 35)/35 with the native weights 1/(7 n): mu1 = 6/245, "
        "mu2 = 2971/8575, gamma = 3048/726635, nu1 = 20761/60025 and nu2 = 22555368816/218081329375, with weighted "
        "orthogonal, mean-zero features; the mod 13 labels 13 i mod 36 have moments 8401/490 and 39205/98 and raise the "
        "least consecutive Vandermonde determinant from 2 to 2990, where 13 and 23 tie as the best of the twelve units":
            (mu1, mu2, gam) == (sp.Rational(6, 245), sp.Rational(2971, 8575), sp.Rational(3048, 726635))
            and nu == (sp.Rational(20761, 60025), sp.Rational(22555368816, 218081329375))
            and sum(a * b * c for a, b, c in zip(w, f1, f2)) == 0 == sum(a * c for a, c in zip(w, f2))
            and (sum(a * b for a, b in zip(w, lab(13))), sum(a * b * b for a, b in zip(w, lab(13))))
            == (sp.Rational(8401, 490), sp.Rational(39205, 98))
            and (best[1], best[13], best[23]) == (2, 2990, 2990) and max(best.values()) == 2990,
        "the majority decoder's counts C(20, 3) = 1140 > C(18, 3) = 816 and 6 x 33 + 35 + 7 = 240 constraints; and the "
        "sibling's idempotent readings: the distance 241 is a unit, 25 mod 27 and 17 mod 32, with images 160, 945 and "
        "3456 summing to 241 + 4320; 2080 sends 120 to 3360, 3105 sends 120 and 240 to 1080 and 2160, 36^2 = 1296, and "
        "990 = 18 x 135 + 18 x 160 - 4320":
            (sp.binomial(20, 3), sp.binomial(18, 3)) == (1140, 816) and 6 * 33 + 35 + 7 == 240
            and gcd(241, N) == 1 and (241 % 27, 241 % 32, 241 % 5) == (25, 17, 1)
            and (ring(2080, 241), ring(3105, 241), ring(3456, 241)) == (160, 945, 3456) and 160 + 945 + 3456 == 241 + N
            and ring(2080, 120) == 3360 and (ring(3105, 120), ring(3105, 240)) == (1080, 2160) and 36 * 36 == 1296
            and 18 * 135 + 18 * 160 - N == 990 and 7 * 135 == 945 and ring(3105, 945) == 945,
    }


def notes_2253():
    """The hub's text (22:51) and the sibling's MODEL (22:26-22:51): the dark erasure court, the syndrome polynomial's
    spectrum, the cubic phase module and the arithmetic."""
    x = sp.Symbol("x")
    M = sp.Matrix(carrier.signless_incidence())
    K = M.T * M
    I10, J10 = sp.eye(10), sp.ones(10, 10)
    P0, P8 = (K - 3 * I10) * (K - 8 * I10) / 24, K * (K - 3 * I10) / 40
    SD = P0 + P8
    classes = {}
    for k in range(1, 7):
        for S in itertools.combinations(range(10), k):
            key = (k, tuple(sp.Poly(SD.extract(list(S), list(S)).charpoly(x).as_expr(), x).all_coeffs()))
            classes.setdefault(key, []).append(S)
    floor = {}
    for (k, co), Ss in classes.items():
        r = min(sp.Poly(co, x).real_roots())
        if k not in floor or r < floor[k][0]:
            floor[k] = [r, 0]
    for (k, co), Ss in classes.items():
        if min(sp.Poly(co, x).real_roots()) == floor[k][0]:
            floor[k][1] += len(Ss)
    want = {1: sp.Rational(3, 5), 2: sp.Rational(1, 3), 3: (17 - sp.sqrt(129)) / 30, 4: sp.Rational(1, 15),
            5: sp.Poly(135 * x ** 3 - 180 * x ** 2 + 54 * x - 2, x).real_roots()[0], 6: sp.Integer(0)}
    T = 2 * J10 - 2 * K - I10
    rng = np.random.default_rng(3)
    sym = lambda: (lambda X: sp.Matrix(X + X.T))(rng.integers(-3, 4, size=(5, 5)))
    A, B = sym(), sym()
    Z1 = lambda a, b: ((a + sp.I * b) * (a ** 2 + b ** 2)).trace() / 6
    Z3 = lambda a, b: ((a + sp.I * b) ** 3).trace() / 6
    c, s_ = sp.Rational(3, 5), sp.Rational(4, 5)
    quarter = sp.Matrix([[0, sp.Rational(3, 4), 0, sp.Rational(1, 4)], [0, 0, -1, 0], [0, 1, 0, 0], [-4, 0, 3, 0]])
    v = 2 * sp.Integer(252) ** 11 / 675
    return {
        "the hub's dark erasure court: over the 847 erased sets of 1 to 6 of the ten dark records, the least eigenvalue of "
        "S_D on the erased set is 3/5, 1/3, (17 - sqrt129)/30, 1/15, the least root of 135t^3 - 180t^2 + 54t - 2 and 0, "
        "attained by 10, 15, 30, 10, 60 and 25 sets: five dark losses stay recoverable and six can fail (the hub, 22:51)":
            sum(len(Ss) for Ss in classes.values()) == 847
            and all(sp.simplify(floor[k][0] - want[k]) == 0 for k in want)
            and [floor[k][1] for k in range(1, 7)] == [10, 15, 30, 10, 60, 25]
            and abs(float(want[5]) - 0.0430022) < 1e-6,
        "the sibling's reading of the syndrome polynomial: T = 2J - 2K - I has trace -30, sends the all-ones vector to 3 "
        "times itself and has characteristic polynomial (x - 3)(x + 7)^4 (x + 1)^5; S_D - I/15 has eigenvalues 14/15 six "
        "times and -1/15 four times, so the floor 1/15 holds only for errors on at most four edges, and each edge lies in "
        "four of the ten tight supports":
            T.trace() == -30 and T * sp.ones(10, 1) == 3 * sp.ones(10, 1)
            and sp.expand(T.charpoly(x).as_expr() - (x - 3) * (x + 7) ** 4 * (x + 1) ** 5) == 0
            and (SD - I10 / 15).eigenvals() == {sp.Rational(14, 15): 6, sp.Rational(-1, 15): 4}
            and all(sum(1 for f in range(10) if f == e or not set(carrier.edges()[e]) & set(carrier.edges()[f])) == 4
                    for e in range(10)),
        "the hub's cubic phase module: for symmetric A and B, eta = Tr(B^3)/6 = (3V - V3)/4 with Z1 = Tr[(A + iB)"
        "(A^2 + B^2)]/6 = U + iV and Z3 = Tr[(A + iB)^3]/6 = U3 + iV3, and a lane rotation multiplies Z1 and Z3 by "
        "e^(i theta) and e^(3i theta), so the cubics carry harmonic weights 1 and 3; its quarter-turn squares to -I":
            sp.simplify((B ** 3).trace() / 6 - (3 * sp.im(Z1(A, B)) - sp.im(Z3(A, B))) / 4) == 0
            and sp.simplify(Z1(c * A - s_ * B, s_ * A + c * B) - (c + sp.I * s_) * Z1(A, B)) == 0
            and sp.simplify(Z3(c * A - s_ * B, s_ * A + c * B) - (c + sp.I * s_) ** 3 * Z3(A, B)) == 0
            and quarter ** 2 == -sp.eye(4),
        "arithmetic: 2 x 252^11 / 675 = 7.711381184...e23 (the sibling's correction of 7.711381764) and times 1120 / "
        "10^28 it is 0.0863674692; the moment variances 54213 - 232^2 = 389 and 237985/4 - (975/4)^2 = 1315/16; the "
        "Singleton counts 252 - 12 + 1 = 241 and 32 - 12 + 1 = 21; 6240 = 26 x 240 = 39 x 160 sits on the clock as "
        "1920, a pure 27-component; and 1023 + 107 = 1130 with 1023 = 3 x 11 x 31 = 2^10 - 1":
            str(sp.N(v, 10)).startswith("7.711381184") and str(sp.N(v * 1120 / sp.Integer(10) ** 28, 9)) == "0.0863674693"
            and 54213 - 232 ** 2 == 389 and sp.Rational(237985, 4) - sp.Rational(975, 4) ** 2 == sp.Rational(1315, 16)
            and (252 - 12 + 1, 32 - 12 + 1) == (241, 21) and 26 * 240 == 39 * 160 == 6240 and 6240 % 4320 == 1920
            and (3105 * 1920) % 4320 == 0 == (3456 * 1920) % 4320 and 1023 + 107 == 1130 and 3 * 11 * 31 == 2 ** 10 - 1,
    }


def notes_2325():
    """The sibling's MODEL (23:07-23:22): the dark and Golden simplex Grams, the six Golden vectors' midpoints and
    triples, and the arithmetic."""
    N = 4320
    ring = lambda a, b: (a * b) % N
    h = [6 * sp.eye(6)[:, i] - sp.ones(6, 1) for i in range(6)]
    ip = lambda a, b: (a.T * b)[0] / 3
    pairs = list(itertools.combinations(range(6), 2))
    mids = [(h[i] + h[j]) / 2 for i, j in pairs]
    tri = [h[i] + h[j] + h[k] for i, j, k in itertools.combinations(range(6), 3) if 0 in (i, j, k)]
    frame = lambda vs: sum((v * v.T for v in vs), sp.zeros(6, 6)) / 3
    P = sp.eye(6) - sp.ones(6, 6) / 6
    dark = lambda n: 15 * sp.eye(n) - 3 * sp.ones(n, n)
    gold = lambda n: 12 * sp.eye(n) - 2 * sp.ones(n, n)
    return {
        "the dark simplex Gram 15I - 3J has eigenvalues 0 and 15^4, and deleting one vector leaves 15^3 and 3, condition 5; "
        "the Golden simplex Gram 12I - 2J, with one vector deleted, has 12^4 and 2, condition 6; and 10J - 4I on six has "
        "56 and (-4)^5, sending the alternating vector to -4 times itself":
            dark(5).eigenvals() == {15: 4, 0: 1} and dark(4).eigenvals() == {15: 3, 3: 1}
            and gold(5).eigenvals() == {12: 4, 2: 1}
            and (10 * sp.ones(6, 6) - 4 * sp.eye(6)).eigenvals() == {56: 1, -4: 5}
            and (10 * sp.ones(6, 6) - 4 * sp.eye(6)) * sp.Matrix([1, -1, 1, -1, 1, -1]) == -4 * sp.Matrix([1, -1, 1, -1, 1, -1]),
        "six vectors with Gram 12I - 2J (diagonal 10, off-diagonal -2) sum to 0; their fifteen edge midpoints have squared "
        "norm 4 and the half-differences 6, orthogonal to them; the midpoint frame equals the vertex frame 12; and the ten "
        "triple sums have squared norm 18, mutual inner products of absolute value 6 and frame 36, with nine of the "
        "fifteen midpoint readings vanishing on each":
            all(ip(h[i], h[j]) == (10 if i == j else -2) for i in range(6) for j in range(6))
            and sum(h, sp.zeros(6, 1)) == sp.zeros(6, 1) and {ip(m, m) for m in mids} == {4}
            and {ip((h[i] - h[j]) / 2, (h[i] - h[j]) / 2) for i, j in pairs} == {6}
            and all(ip(h[i] + h[j], h[i] - h[j]) == 0 for i, j in pairs)
            and frame(h) == 12 * P == frame(mids) and len(tri) == 10 and {ip(t, t) for t in tri} == {18}
            and {abs(ip(a, b)) for a, b in itertools.combinations(tri, 2)} == {6} and frame(tri) == 36 * P
            and {sum(1 for m in mids if ip(m, t) == 0) for t in tri} == {9},
        "arithmetic: the coefficients (-1)^k C(8, k) sum to 0 and their absolute values to 256; 61526 - 248^2 = 22, and "
        "61526 shares the 32-image 3510 = 26 x 135 with 22; 2160 = 16 x 135 is a pure 32-component and 960 = 6 x 160 a "
        "pure 27-component, 4/9 of 2160; 22080 = 23 x 960 has 27-image 480; 11! is 9240 circles; and a petal label and "
        "an address leave fibres of 720 and 120":
            sum((-1) ** k * sp.binomial(8, k) for k in range(9)) == 0 and sum(sp.binomial(8, k) for k in range(9)) == 256
            and 61526 - 248 ** 2 == 22 and ring(3105, 61526) == ring(3105, 22) == 3510 == 26 * 135
            and ring(3105, 2160) == 2160 == 16 * 135 and ring(2080, 960) == 960 == 6 * 160 and ring(3105, 960) == 0
            and ring(3456, 960) == 0 and sp.Rational(960, 2160) == sp.Rational(4, 9) and 22080 == 23 * 960
            and ring(2080, 22080) == 480 and factorial(11) == 9240 * N and (N // 6, N // 36) == (720, 120),
    }


def six_lines():
    """The hub's 23:38 text: the six lines of the tick's residue plane are an equitable, reducing partition of the
    root graph."""
    B, Binv, C, Cinv, R, RB = spine.frame()
    _, lines = cyclotomic.residue()
    pts = [cyclotomic.point(x) for x in RB]
    S = np.array([[int(pts[i] in L) for L in lines] for i in range(240)], dtype=np.int64)
    A = (RB @ C @ RB.T == 1).astype(np.int64)
    Q = 10 * np.ones((6, 6), dtype=np.int64) - 4 * np.eye(6, dtype=np.int64)
    spec = Counter(int(round(x)) for x in np.linalg.eigvalsh(A.astype(float)))
    finite = [int(np.trace(np.linalg.matrix_power(A, k))) // 240 for k in range(5)]
    P = sp.Matrix(Q.tolist()) / 56
    return {
        "with S the root-line incidence of the six lines (40 roots each), A S = S Q and S^T S = 40 I for Q = 10J - 4I: "
        "a root has 6 neighbours on its own line and 10 on each other, so the six A4 + A4 are an equitable partition "
        "of the root graph, with quotient spectrum 56 and (-4)^5 inside 56, 28^8, 8^35, (-2)^112, (-4)^84":
            np.array_equal(A @ S, S @ Q) and np.array_equal(S.T @ S, 40 * np.eye(6, dtype=np.int64))
            and spec == Counter({56: 1, 28: 8, 8: 35, -2: 112, -4: 84})
            and sp.Matrix(Q.tolist()).eigenvals() == {56: 1, -4: 5},
        "the split is reducing: A commutes with S S^T, so the finite graph's cross block between the six-dimensional "
        "line part and its 234-dimensional complement, and with it the Schur memory, is zero; the walks per root are "
        "1, 0, 56, 1512, 62160 against the lattice's 1, 0, 240, 13440, 1260720, so the finite graph is not the bath":
            np.array_equal(A @ S @ S.T, S @ S.T @ A) and sum(spec.values()) - 6 == 234
            and finite == [1, 0, 56, 1512, 62160] and recurrence.load_walks()[:5] == [1, 0, 240, 13440, 1260720],
        "the line chain Q/56 has diagonal 3/28 and off-diagonal 5/28 and eigenvalues 1 and (-1/14)^5, so one step is no "
        "real exponential while two steps are exp(log 196 (J/6 - I))":
            (P[0, 0], P[0, 1]) == (sp.Rational(3, 28), sp.Rational(5, 28))
            and P.eigenvals() == {1: 1, sp.Rational(-1, 14): 5}
            and P ** 2 == (sp.log(196) * (sp.ones(6, 6) / 6 - sp.eye(6))).exp().applyfunc(sp.nsimplify),
    }


def notes_2356():
    """The sibling's MODEL (23:26-00:00) and the hub's 23:38 text: the [15, 5, 6] midpoint code, the Dirac polynomial,
    the selected matrix over F5, the Klein fours, the printed moments' Jacobi chain, and the arithmetic."""
    N = 4320
    land = lambda n: (3456 * n) % N
    order = lambda s: N // gcd(s, N)
    h = [6 * np.eye(6, dtype=np.int64)[i] - 1 for i in range(6)]
    pairs = list(itertools.combinations(range(6), 2))
    U = np.array([(h[i] + h[j]) // 2 for i, j in pairs], dtype=float)
    rank = lambda rows: np.linalg.matrix_rank(U[list(rows)])
    ten = {rank(s) for s in itertools.combinations(range(15), 10)}
    fail = sorted(sorted(s) for s in itertools.combinations(range(15), 9) if rank(s) < 5)
    splits = [sum(h[i] for i in T) for T in itertools.combinations(range(6), 3) if 0 in T]
    zeros = sorted(sorted(k for k, (i, j) in enumerate(pairs) if int((h[i] + h[j]) @ x) == 0) for x in splits)
    E = list(itertools.combinations(range(5), 2))
    M = sp.Matrix(5, 10, lambda v, e: int(v in E[e]))
    K, I10 = M.T * M, sp.eye(10)
    Pk = {lam: sp.prod([(K - mu * I10) / (lam - mu) for mu in (0, 3, 8) if mu != lam]) for lam in (0, 3, 8)}
    TD = (K ** 2 - 7 * K - 2 * I10) / 2
    D, Cx = np.array([[1, 4], [1, 2]], dtype=np.int64), np.array([[0, 4], [1, 1]], dtype=np.int64)
    Dk = [np.eye(2, dtype=np.int64)]
    for _ in range(24):
        Dk.append((Dk[-1] @ D) % 5)
    scalar = lambda X: X[0, 1] == 0 and X[1, 0] == 0 and X[0, 0] == X[1, 1]
    line = lambda p: (0, 1) if p[0] % 5 == 0 else (1, int(p[1]) * pow(int(p[0]), -1, 5) % 5)
    proj = [(0, 1)] + [(1, b) for b in range(5)]

    def cycles(X):
        nxt = {p: line(tuple(int(t) for t in (X @ np.array(p)) % 5)) for p in proj}
        seen, out = set(), []
        for p in proj:
            n, q = 0, p
            while q not in seen:
                seen.add(q)
                q, n = nxt[q], n + 1
            if n:
                out.append(n)
        return sorted(out)
    k = cyclotomic.clocks()
    day, cp = cyclotomic.on_plane(k["day"]) % 5, cyclotomic.on_plane(k["c"]) % 5
    poly = lambda X: (int(np.trace(X)) % 5, int(round(np.linalg.det(X))) % 5)
    dpow = [np.eye(2, dtype=np.int64)]
    for _ in range(24):
        dpow.append((dpow[-1] @ day) % 5)
    klein = {frozenset({(a, b), (c, d)}) for om in range(5)
             for a, b, c, d in [tuple(v for v in range(5) if v != om)]
             for (a, b), (c, d) in [((a, b), (c, d)), ((a, c), (b, d)), ((a, d), (b, c))]}
    disjoint = {frozenset({e, f}) for e, f in itertools.combinations(E, 2) if not set(e) & set(f)}
    m = [1, 248, 61526, 15269016, 3790531010, 941278124080, 233807211090510]
    x = sp.Symbol("x")
    L = lambda p: sum(c * m[i] for i, c in enumerate(reversed(sp.Poly(sp.expand(p), x).all_coeffs())))
    p, a, b2 = [sp.Integer(1), x - 248], [sp.Integer(248)], []
    for n in (1, 2):
        a.append(L(x * p[n] ** 2) / L(p[n] ** 2))
        b2.append(L(p[n] ** 2) / L(p[n - 1] ** 2))
        p.append(sp.expand((x - a[n]) * p[n] - b2[-1] * p[n - 1]))
    b2.append(L(p[3] ** 2) / L(p[2] ** 2))

    def fmul(u, v):
        return (u[0] * v[0] - u[1] * v[1]) % 241, (u[0] * v[1] + u[1] * v[0] + 133 * u[1] * v[1]) % 241

    def fpow(u, n):
        y = (1, 0)
        while n:
            y, u, n = (fmul(y, u) if n & 1 else y), fmul(u, u), n >> 1
        return y
    w, t = sp.symbols("w t")
    series = sp.series(1 / (3 + 8 * w + 3 * w ** 2), w, 0, 3).removeO()
    c3 = [series.coeff(w, i) for i in range(3)]
    r5 = sp.sqrt(5)
    ca, cb, cc = sp.Rational(8, 5) + 4 * r5 / 25, sp.Rational(39, 50) + 47 * r5 / 250, sp.Rational(78, 625) + 6 * r5 / 125
    cubic = lambda X: X ** 3 - ca * X ** 2 + cb * X - cc
    ode = lambda y, f: (sp.simplify(sp.diff(y, t, 2) + 64 * y - f) == 0 and y.subs(t, 0) == 0
                        and sp.diff(y, t).subs(t, 0) == 0)
    band = lambda f: sp.nsimplify(sp.simplify(sum(sp.cos(2 * sp.pi * f * j / 5) ** 2 for j in range(5))))
    Gc, Gu, s = sp.symbols("G_c G_u s")
    marks = [{(0, 2), (0, 3), (1, 3), (1, 4), (2, 4)}, {(0, 2), (0, 4), (2, 3), (3, 4)}, {(0, 1), (0, 2), (0, 4), (1, 3)}]
    lo, hi, weyl = 435118836, 436266657, 2 ** 14 * 3 ** 5 * 5 ** 2 * 7
    return {
        "the fifteen midpoint readings of the six Golden vectors (Gram 12I - 2J) are a [15, 5, 6] code: all 3003 "
        "ten-reading sets span, and exactly 10 of the 5005 nine-reading sets fail, the zero sets of the ten 3 + 3 "
        "splits (the hub)":
            ten == {5} and fail == zeros and len(fail) == 10 and all(len(z) == 9 for z in zeros),
        "with K = M^T M, T = (K^2 - 7K - 2I)/2 = -P0 - 7P3 + 3P8 and (P0 + P8) T - (3/10) J = -P0 (the hub)":
            TD == -Pk[0] - 7 * Pk[3] + 3 * Pk[8] and (Pk[0] + Pk[8]) * TD - sp.Rational(3, 10) * sp.ones(10, 10) == -Pk[0],
        "the selected matrix D = [[1, 4], [1, 2]] over F5 squares to 3C with C of characteristic polynomial x^2 - x + 1, "
        "the Coxeter clock's on the residue plane; D^6 = 3I, D^12 = -I, D^24 = I and no power below 6 is scalar; on the "
        "six lines D, D^2 and D^3 have cycle types 6, 3 + 3 and 2 + 2 + 2; and D has the characteristic polynomial of "
        "the inverse day d^-1 = d^23 (and its Frobenius twin d^19), so it is conjugate to d^-1 in GL(2,5)":
            np.array_equal(Dk[2], np.array([[0, 2], [3, 3]])) and np.array_equal(Dk[2], (3 * Cx) % 5)
            and poly(Cx) == poly(cp) == (1, 1) and np.array_equal(Dk[6], 3 * np.eye(2, dtype=np.int64))
            and np.array_equal(Dk[12], 4 * np.eye(2, dtype=np.int64)) and np.array_equal(Dk[24], np.eye(2, dtype=np.int64))
            and not any(scalar(Dk[j]) for j in range(1, 6)) and [cycles(Dk[j]) for j in (1, 2, 3)] == [[6], [3, 3], [2, 2, 2]]
            and [j for j in range(1, 25) if poly(dpow[j]) == poly(D)] == [19, 23],
        "the five even Klein fours, one for each omitted vertex, have fifteen non-identity elements, exactly the "
        "fifteen disjoint edge pairs; a four-cycle squares to one of them; the quarter-turn squares to -I":
            klein == disjoint and len(disjoint) == 15 and (Permutation([1, 2, 3, 0, 4]) ** 2).cyclic_form == [[0, 2], [1, 3]]
            and sp.Matrix([[0, -1], [1, 0]]) ** 2 == -sp.eye(2),
        "if the printed moments 1, 248, 61526, ... are exact, their Hankel determinants are 22, 128724 and 540658207776, "
        "so no two atoms match five of them and no three all seven; the Jacobi diagonals are 248, 2556/11 and "
        "24755888/117997 and the off-diagonal squares 22, 32181/121 and 247801678564/345205587; the static resolvent "
        "bound 520089621/128932714232 lies between 124/30763 and 1/240, and the stated native enclosure above it":
            [sp.Matrix(n, n, lambda i, j: m[i + j]).det() for n in (2, 3, 4)] == [22, 128724, 540658207776]
            and a == [248, sp.Rational(2556, 11), sp.Rational(24755888, 117997)]
            and b2 == [22, sp.Rational(32181, 121), sp.Rational(247801678564, 345205587)]
            and sp.Rational(124, 30763) < sp.Rational(520089621, 128932714232) < sp.Rational(1, 240)
            and sp.Rational(lo, 10 ** 11) > sp.Rational(520089621, 128932714232),
        "mod 241, 94/75 = 133, and a root of t^2 - 133t + 1 (whose discriminant is a non-residue) has order 121 in "
        "F_241^2, its eleventh power not 1; the cleared Hankel has determinant 81; 1/(3 + 8w + 3w^2) begins 1/3, -8/9, "
        "55/27, which misses the carrier recurrence x^2 + 11x + 24 = (x + 3)(x + 8) by 7/27; the squared frequencies "
        "(4 +- sqrt7)/3 are positive":
            (133 * 75 - 94) % 241 == 0 and pow((133 * 133 - 4) % 241, 120, 241) == 240 and fpow((0, 1), 121) == (1, 0)
            and fpow((0, 1), 11) != (1, 0)
            and sp.Matrix([[0, 0, 0, 3], [0, 0, 3, 0], [0, 3, 0, -8], [3, 0, -8, 0]]).det() == 81
            and c3 == [sp.Rational(1, 3), sp.Rational(-8, 9), sp.Rational(55, 27)]
            and c3[2] + 11 * c3[1] + 24 * c3[0] == sp.Rational(7, 27)
            and all(r > 0 for r in sp.solve(3 * w ** 2 - 8 * w + 3, w)),
        "the cubic X^3 - (8/5 + 4 sqrt5/25) X^2 + (39/50 + 47 sqrt5/250) X - (78/625 + 6 sqrt5/125) is negative at 19/20 "
        "and positive at 957/1000 and its larger turning point is below 19/20, so its largest root leaves more than "
        "43/1000; sqrt(80/129) lies between 787/1000 and 788/1000, and 75/2 turns 43/1000 into 129/80":
            cubic(sp.Rational(19, 20)) < 0 < cubic(sp.Rational(957, 1000))
            and (ca + sp.sqrt(ca ** 2 - 3 * cb)) / 3 < sp.Rational(19, 20)
            and sp.Rational(787, 1000) < sp.sqrt(sp.Rational(80, 129)) < sp.Rational(788, 1000)
            and sp.Rational(43, 1000) * sp.Rational(75, 2) == sp.Rational(129, 80),
        "the fixture y'' + 64y = -cos 4t, -1 and -sin 4t from rest has the responses (cos 8t - cos 4t)/48, (cos 8t - 1)/64 "
        "and sin 8t/96 - sin 4t/48; the bands 4 and 8 on five samples both have squared norm 5/2; Phi_5(2) = 31 = 25 + 6":
            ode((sp.cos(8 * t) - sp.cos(4 * t)) / 48, -sp.cos(4 * t)) and ode((sp.cos(8 * t) - 1) / 64, -1)
            and ode(sp.sin(8 * t) / 96 - sp.sin(4 * t) / 48, -sp.sin(4 * t)) and band(4) == band(8) == sp.Rational(5, 2)
            and sp.cyclotomic_poly(5, 2) == 31 == 25 + 6,
        "arithmetic: (1440 + 5s) G_c + s G_u = 6 for every s gives G_c = 1/240 and G_u = -1/48; |W(E8)| = 2^14 3^5 5^2 7 is "
        "prime to 11; on the circle 3, 8, 24, 11, 48, 90, 242 and 20 have orders 1440, 540, 180, 4320, 90, 48, 2160 and "
        "216; the enclosure has width 1147821 and reciprocals in (229, 230); C(12, 5..7) = 792, 924, 792, "
        "C(12, 8..12) add to 794 and C(25, 5) = 53130; (25 - 1)/(5 - 1) = 6 and (81 - 1)/(9 - 1) = 10 count the lines "
        "of the hexad and the decad; 7! - 6! = 4320 = 12 x 360; the three exposures use 13 marks on 9 edges, missing 12 "
        "and sharing 02, with 80 one-erasure patterns; and the stated landings x -> 3456x hold":
            sp.solve(sp.Poly(sp.expand((1440 + 5 * s) * Gc + s * Gu - 6), s).coeffs(), [Gc, Gu])
            == {Gc: sp.Rational(1, 240), Gu: sp.Rational(-1, 48)} and weyl == 696729600 and weyl % 11 != 0
            and gcd(242, N) == 2 and [order(q) for q in (3, 8, 24, 11, 48, 90, 242, 20)]
            == [1440, 540, 180, 4320, 90, 48, 2160, 216] and hi - lo == 1147821
            and 229 < sp.Rational(10 ** 11, hi) and sp.Rational(10 ** 11, lo) < 230
            and [sp.binomial(12, q) for q in (5, 6, 7)] == [792, 924, 792]
            and sum(sp.binomial(12, q) for q in range(8, 13)) == 794 and sp.binomial(25, 5) == 53130
            and ((25 - 1) // (5 - 1), (81 - 1) // (9 - 1)) == (len(cyclotomic.residue()[1]), 10) == (6, 10)
            and factorial(7) - factorial(6) == N == 12 * 360 and gcd(36, 120) == 12
            and sum(map(len, marks)) == 13 and len(set.union(*marks)) == 9 and (1, 2) not in set.union(*marks)
            and set.intersection(*marks) == {(0, 2)} and len(marks[0]) * len(marks[1]) * len(marks[2]) == 80
            and [land(q) for q in (726, 125, 269, 13, 16, 79, 229, 313, 43, 129, 48, 234, 72, 216, 24, 7, 27, 242, 31)]
            == [3456, 0, 864, 1728, 3456, 864, 864, 1728, 1728, 864, 1728, 864, 2592, 3456, 864, 2592, 2592, 2592, 3456],
    }


@functools.lru_cache(maxsize=None)
def _wedge_moments():
    """The root-wedge port's moments m_n = t^T H^n t / t^T t through n = 8, from H^4 t on the lattice (t = column e01).
    H pushes 240 f(x) to x and -f(x) to the 240 neighbours x + r; the sums stay below 2^53, so float weights are exact."""
    R10, V, W, Bw, G, h, Hc = _wedge()
    R2 = np.asarray(R10, dtype=np.int64) // 5
    off, base = 64, 128
    w = base ** np.arange(8, dtype=np.int64)

    def push(keys, vals):
        pts = np.stack([(keys // base ** i) % base - off for i in range(8)], axis=1)
        nk = np.concatenate([keys, ((pts[:, None, :] + R2[None, :, :]).reshape(-1, 8) + off) @ w])
        nv = np.concatenate([240 * vals, np.repeat(-vals, 240)]).astype(float)
        u, inv = np.unique(nk, return_inverse=True)
        return u, np.bincount(inv, weights=nv)

    def apply_h(keys, vals, chunk=60000):
        parts = [push(keys[lo:lo + chunk], vals[lo:lo + chunk]) for lo in range(0, len(keys), chunk)]
        u, inv = np.unique(np.concatenate([k for k, _ in parts]), return_inverse=True)
        s = np.rint(np.bincount(inv, weights=np.concatenate([v for _, v in parts]))).astype(np.int64)
        return u[s != 0], s[s != 0]
    t = np.asarray(Bw[:, 0], dtype=np.int64)
    keys, vals = (R2[t != 0] + off) @ w, t[t != 0]
    order = np.argsort(keys)
    seq = [(keys[order], vals[order])]
    for _ in range(4):
        seq.append(apply_h(*seq[-1]))

    def dot(a, b):
        _, ia, ib = np.intersect1d(a[0], b[0], return_indices=True)
        return sum(int(x) * int(y) for x, y in zip(a[1][ia], b[1][ib]))
    raw = [dot(seq[i // 2], seq[(i + 1) // 2]) for i in range(9)]
    return [sp.Rational(r, raw[0]) for r in raw], [len(k) for k, _ in seq]


def petersen_sequence():
    """The hub's 00:25 text: the ten nonspecial synthemes meet the fifteen duads in the signless Petersen incidence."""
    H, sig, S5, sgn, U = _six_lines()
    E = carrier.edges()
    SY = _matchings(range(6))
    move = lambda p, m: frozenset(frozenset(sig[p][y] for y in pr) for pr in m)
    special = next(o for o in ({move(p, m) for p in S5} for m in SY) if len(o) == 5)
    v = {i: next(m for m in special if all(move(p, m) == m for p in S5 if p[i] == i)) for i in range(5)}
    edge = {tuple(i for i in range(5) if not v[i] & m): m for m in SY if m not in special}
    duads = [frozenset(d) for d in itertools.combinations(range(6), 2)]
    B = sp.Matrix(10, 15, lambda r, c: int(duads[c] in edge[E[r]]))
    M = sp.Matrix(carrier.signless_incidence())
    K, J, I = M.T * M, sp.ones(10, 10), sp.eye(10)
    BB = B * B.T
    P = (BB - I) * (6 * I - BB) / 6
    N = sp.Matrix(15, 15, lambda r, c: int(duads[r] in SY[c]))
    Ak = np.array([[int(not duads[i] & duads[j]) for j in range(15)] for i in range(15)])
    induced = sum(1 for a, b, c, d in itertools.permutations(range(15), 4)
                  if Ak[a, b] and Ak[b, c] and Ak[c, d] and Ak[d, a] and not Ak[a, c] and not Ak[b, d]) // 8
    Nn = np.array(N.tolist(), dtype=np.int64)
    Lv = np.block([[np.zeros((15, 15), dtype=np.int64), Nn], [Nn.T, np.zeros((15, 15), dtype=np.int64)]])
    deg = Lv.sum(axis=1)
    return {
        "B, the incidence of the ten nonspecial synthemes (in K5-edge order) with the fifteen duads, has three ones in "
        "each row and two in each column, and B B^T = 3I + A_Petersen = 4I + J - K for K = M^T M: two synthemes share a "
        "duad exactly when their K5 edges are disjoint, so B is the signless incidence of the Petersen graph, of rank 10":
            {sum(B.row(r)) for r in range(10)} == {3} and {sum(B.col(c)) for c in range(15)} == {2}
            and BB == 4 * I + J - K and B.rank() == 10,
        "the Petersen Gram has eigenvalues 4 on the source ker M, 1 on the charge part and 6 on the constant, so "
        "P_source = (BB^T - I)(6I - BB^T)/6 and (BB^T)^-1 = (I + K)/4 - (5/24) J":
            P * P == P and P.rank() == 5 and M * P == sp.zeros(5, 10) and BB.inv() == (I + K) / 4 - sp.Rational(5, 24) * J,
        "the full duad-syntheme incidence N has N N^T = 3I + A of the Kneser graph K(6,2), spectrum 9, 4^9, 0^5 and rank "
        "10; K(6,2) has exactly 90 induced four-cycles, while the Levi graph of N (30 vertices, 45 edges) has none":
            (N * N.T).eigenvals() == {9: 1, 4: 9, 0: 5} and N.rank() == 10 and induced == 90 and int(Lv.sum()) == 90
            and int(np.trace(np.linalg.matrix_power(Lv, 4))) == int(2 * (deg ** 2).sum() - deg.sum()),
    }


def notes_0032():
    """The hub's 00:25 text and the sibling's MODEL (00:04-00:38): the native moments through 6 from the lattice, the
    Hankel and Jacobi chain and the Galerkin bound on the static Green scalar, the reflection Casimir, the critical
    steps against the canon's subgroups, the Weyl vector's order, and the arithmetic."""
    N = 4320
    order = lambda s: N // gcd(s, N)
    sub = lambda s: {(s * k) % N for k in range(order(s))}
    land = lambda n: (3456 * n) % N
    m, supports = _wedge_moments()
    adj = [1, 8, 453, 27168, 2195296, 209077920, 22553934885]
    x = sp.Symbol("x")
    L = lambda p: sum(c * m[i] for i, c in enumerate(reversed(sp.Poly(sp.expand(p), x).all_coeffs())))
    p, a, b2 = [sp.Integer(1), x - m[1]], [m[1]], []
    for n in (1, 2):
        a.append(L(x * p[n] ** 2) / L(p[n] ** 2))
        b2.append(L(p[n] ** 2) / L(p[n - 1] ** 2))
        p.append(sp.expand((x - a[n]) * p[n] - b2[-1] * p[n - 1]))
    b2.append(L(p[3] ** 2) / L(p[2] ** 2))
    A3 = sp.Matrix(3, 3, lambda i, j: m[i + j + 1])
    c = A3.LUsolve(sp.Matrix(m[:3]))
    ell = sum(c[i] * m[i] for i in range(3))
    res = m[0] - 2 * sum(c[j] * m[j + 1] for j in range(3)) + sum(c[i] * c[j] * m[i + j + 2] for i in range(3)
                                                                   for j in range(3))
    R10, V, W, Bw, G, h, Hc = _wedge()
    R2 = np.asarray(R10, dtype=np.int64) // 5
    key = {tuple(r): i for i, r in enumerate(R2.tolist())}
    Bw = np.asarray(Bw, dtype=np.int64)
    casimir = sum(Bw - Bw[[key[tuple(y)] for y in (R2 - np.outer((R2 @ r) // 4, r)).tolist()]]
                  for r in R2 if tuple(r) > tuple(-r))
    crit = {864, 1728, 2592, 3456, 1080, 3240, 1440, 2880, 2160}   # layer 28's critical steps
    addr, prin, gold = sub(120), sub(144), sub(20)
    B, Binv, C, Cinv, R, RB = spine.frame()
    rho = principal.weyl_vector()[0]
    theta = RB[int(np.argmax(RB.sum(axis=1)))]
    phi121 = sp.Poly(sp.cyclotomic_poly(121, x), x, modulus=241)
    q = sp.Poly(x ** 2 - 133 * x + 1, x, modulus=241)
    facs = phi121.factor_list()[1]
    J6 = sp.ones(6, 6)
    return {
        "the root-wedge port's moments through order 6 recomputed on the lattice (H^3 on 897672 sites from the column "
        "e01) are 1, 232, 54213, 12740592, 3008062816, 712951229280 and 169533368834085: the hub's native m5 and m6 "
        "replay, and they are the binomial transform of its adjacency moments 1, 8, 453, ..., 22553934885":
            m[:7] == [1, 232, 54213, 12740592, 3008062816, 712951229280, 169533368834085] and supports[0] == 152
            and all(m[k] == sum(sp.binomial(k, j) * 240 ** (k - j) * (-1) ** j * adj[j] for j in range(k + 1))
                    for k in range(7)),
        "their 4 x 4 Hankel determinant is 275042684645559311, the new Jacobi coefficients are a2 = 14038040210424/"
        "85511499823 and b3^2 = 106991604327122571979/48322550088744649, and the Galerkin value of [m_(i+j+1)] c = [m_i] "
        "at n = 3 is l3 = 6446188211663/1481477624895392 <= s = <T, H^-1 T>; with the hub's congestion bound "
        "(n + 1)(n + 2)/48 (stated, not replayed) the upper end 114900908004970886996873523137/26337311436788301626627314003968 "
        "follows, so 0.00435118836 <= s <= 0.00436266657":
            sp.Matrix(4, 4, lambda i, j: m[i + j]).det() == 275042684645559311
            and a[2] == sp.Rational(14038040210424, 85511499823)
            and b2[2] == sp.Rational(106991604327122571979, 48322550088744649)
            and ell == sp.Rational(6446188211663, 1481477624895392) and res > 0
            and ell + sp.Rational(20, 48) * res == sp.Rational(114900908004970886996873523137,
                                                              26337311436788301626627314003968)
            and sp.Rational(435118836, 10 ** 11) <= ell and ell + sp.Rational(20, 48) * res <= sp.Rational(436266657, 10 ** 11),
        "the 120 root reflections give L_ref T = 48 T on all ten columns of the port (28800 root-reflection pairs), "
        "L_ref = sum (I - U_s)":
            np.array_equal(casimir, 48 * Bw),
        "the nine critical steps of layer 28 lie five in the address subgroup <120> (order 36), seven in the principal "
        "subgroup <144> (order 30) and three in both (1440, 2880, 2160); <120> and <144> meet in <720>, sit in the "
        "subgroup <20> of order 216 and the whole circle respectively, and generate <24> of order 180; <20> holds the "
        "five address-critical steps, none of the tick stations, and meets <144> in <720> (the sibling)":
            len(crit & addr) == 5 and len(crit & prin) == 7 and crit & addr & prin == {1440, 2880, 2160}
            and addr & prin == sub(720) and len(sub(720)) == 6 and addr <= gold and len(gold) == 216
            and crit & addr <= gold and not {864, 1728, 2592, 3456} & gold and gold & prin == sub(720)
            and len(sub(gcd(120, 144))) == 180 and N // 180 == 24,
        "correction: the Weyl vector's coordinates 46, 68, 91, 135, 110, 84, 57, 29 are in the Bourbaki order, the order "
        "in which the highest root is 2, 3, 4, 6, 5, 4, 3, 2 (Bourbaki's tables); their sum, 620, is |rho|^2":
            rho.tolist() == [46, 68, 91, 135, 110, 84, 57, 29] and theta.tolist() == [2, 3, 4, 6, 5, 4, 3, 2]
            and int(rho.sum()) == int(rho @ C @ rho) == 620 == 30 * 248 // 12,
        "mod 241: 241 = -1 mod 121, so Phi_121 splits into 55 quadratics, one of them t^2 - 133t + 1; (183I + 52J)(54I + "
        "25J) = I and 241I - J = -J for the six-site J; the steps 168, 55 and 133 generate the subgroups of order 180, "
        "864 and 4320":
            241 % 121 == 120 and phi121.rem(q).is_zero and len(facs) == 55
            and all(f.degree() == 2 and e == 1 for f, e in facs)
            and ((183 * sp.eye(6) + 52 * J6) * (54 * sp.eye(6) + 25 * J6)).applyfunc(lambda z: z % 241) == sp.eye(6)
            and [order(s) for s in (168, 55, 133)] == [180, 864, 4320],
        "arithmetic: the Petersen graph's power traces are 0, 30, 0, 150, 120, 990, with 12 pentagons and 10 hexagons; "
        "2420 = 121 x 20 generates <20> (order 216) and 132 the subgroup of order 360, meeting in order 72; 4(64 - 6) = "
        "232 and 4(64 + 6) = 280 add to 512; 27 x 47^2/400 = 59643/400; the energy enclosure [5.00015251952, "
        "5.00074396355] holds the older [5.00061970298, 5.00067938080], with 5.0001 below, 5.001 above and 5.0005 "
        "inside; the clock orders of 12, 15, 105, 95, 60, 30, 232, 64, 512, 17, 99, 1435, 54, 162 and the landings hold":
            _petersen_traces() == ([0, 30, 0, 150, 120, 990], 12, 10)
            and order(2420) == 216 and sub(2420) == sub(20) and order(132) == 360 and len(sub(20) & sub(12)) == 72
            and 4 * (64 - 6) == 232 and 4 * (64 + 6) == 280 and 232 + 280 == 512
            and sp.Rational(27 * 47 ** 2, 400) == sp.Rational(59643, 400)
            and 5.00015251952 < 5.00061970298 < 5.00067938080 < 5.00074396355 and 5.0001 < 5.00015251952
            and 5.00074396355 < 5.001 and 5.00015251952 < 5.0005 < 5.00074396355
            and [order(s) for s in (12, 15, 105, 95, 60, 30, 232, 64, 512, 17, 99, 1435, 54, 162)]
            == [360, 288, 288, 864, 72, 144, 540, 135, 135, 4320, 480, 864, 80, 80] and land(8) == land(1728) == 1728,
    }


def notes_0117():
    """The hub's 00:52 text (with the preserved 360/093 paper: the native moments through 8) and the sibling's MODEL
    (00:46-01:16): m7 and m8 on the lattice, the five-site port's sectors, the identity step (a correction), the
    pentagon metric and the arithmetic."""
    N = 4320
    order = lambda s: N // gcd(s, N)
    m, supports = _wedge_moments()
    adj = [1, 8, 453, 27168, 2195296, 209077920, 22553934885, 2673812041040, 341474102417616]
    dets = [sp.Matrix(k, k, lambda i, j: m[i + j]).det() for k in range(1, 6)]
    x = sp.Symbol("x")
    L = lambda p: sum(c * m[i] for i, c in enumerate(reversed(sp.Poly(sp.expand(p), x).all_coeffs())))
    p, a, b2 = [sp.Integer(1), x - m[1]], [m[1]], []
    for n in (1, 2, 3):
        a.append(L(x * p[n] ** 2) / L(p[n] ** 2))
        b2.append(L(p[n] ** 2) / L(p[n - 1] ** 2))
        p.append(sp.expand((x - a[n]) * p[n] - b2[-1] * p[n - 1]))
    b2.append(L(p[4] ** 2) / L(p[3] ** 2))
    R10 = _wedge()[0]
    Hn = _walk_entries()
    E = [Hn(np.zeros(8, dtype=np.int64), n) for n in range(4)]
    S = [Hn(np.asarray(R10[0], dtype=np.int64), n) for n in range(4)]
    uniform, contrast = [E[n] + 4 * S[n] for n in range(3)], [E[n] - S[n] for n in range(4)]
    rs = principal.weyl_vector()[1]
    Rst = spine.frame()[4]
    band0 = 240 - np.cos(2 * np.pi * (Rst @ (0 * rs))).sum()
    C5 = sp.Matrix(5, 5, lambda i, j: [4, 1, -2, -2, 1][(j - i) % 5])
    t = sp.Symbol("t")
    J6, J5 = sp.ones(6, 6), sp.ones(5, 5)
    E10 = list(itertools.combinations(range(5), 2))
    P4 = list(itertools.combinations(range(4), 2))

    def tree(es):
        parent = list(range(5))

        def find(u):
            while parent[u] != u:
                u = parent[u]
            return u
        for u, v in es:
            ru, rv = find(u), find(v)
            if ru == rv:
                return False
            parent[ru] = rv
        return True
    trees = sum(1 for es in itertools.combinations(E10, 4) if tree(es))
    phi = (1 + sp.sqrt(5)) / 2
    conv = [sp.Rational(sp.fibonacci(n + 1), sp.fibonacci(n)) for n in range(2, 8)]
    g = lambda z: z ** 2 - 1
    lo = sp.Rational(146357822798943902250, 84570222726627452591)
    return {
        "the root-wedge port's moments through order 8 on the lattice (H^4 on 4770696 sites from the column e01): m7 = "
        "40427488329573760 and m8 = 9664268760217668816, the hub's values, and all nine are the binomial transform of its "
        "adjacency moments 1, 8, 453, ..., 341474102417616":
            m[7:] == [40427488329573760, 9664268760217668816] and supports[4] == 4770696
            and all(m[k] == sum(sp.binomial(k, j) * 240 ** (k - j) * (-1) ** j * adj[j] for j in range(k + 1))
                    for k in range(9)),
        "the 5 x 5 Hankel determinant is 925993405224288478170979103007 > 0, the monic norms are 1, 389, 219823907/389, "
        "275042684645559311/219823907 and 925993405224288478170979103007/275042684645559311, and the next Jacobi entries "
        "are a3 = 9170078120306091261578543712/60460957530555757944248077 and b4^2 = "
        "203555488192637304566628840438354188349/75648478377036587574008272018794721":
            dets[4] == 925993405224288478170979103007
            and [dets[0]] + [dets[k] / dets[k - 1] for k in range(1, 5)]
            == [1, 389, sp.Rational(219823907, 389), sp.Rational(275042684645559311, 219823907),
                sp.Rational(925993405224288478170979103007, 275042684645559311)]
            and a[3] == sp.Rational(9170078120306091261578543712, 60460957530555757944248077)
            and b2[3] == sp.Rational(203555488192637304566628840438354188349, 75648478377036587574008272018794721),
        "five roots with pairwise products 1 carry the uniform moments 1, 236, 56144 (variance 448) and the contrast "
        "moments 1, 241, 58264, 14121093 (variance 183), the contrast being E_(k+1)/240; the next Lanczos coefficient is "
        "35366/183, and 58702 - 242^2 = 138":
            uniform == [1, 236, 56144] and contrast == [1, 241, 58264, 14121093] and uniform[2] - 236 ** 2 == 448
            and contrast[2] - 241 ** 2 == 183 and contrast[3] - 482 * contrast[2] + 241 ** 2 * contrast[1] == 35366
            and 58702 - 242 ** 2 == 138,
        "correction: at the identity step the band is 0, the minimum, not 240; the formula 248 - 8 mu(d)/phi(d) of layer "
        "28 holds for d > 1, since at d = 1 the 240 roots add 240 to the character":
            abs(band0) < 1e-12 and 248 - 8 * sp.mobius(1) // 1 == 240,
        "the pentagon metric [4, 1, -2, -2, 1] has characteristic polynomial (t - 2)(t^2 - 9t + 9)^2 and determinant "
        "162; det(I + J) = 6 and 162/6 = 27 is no square, so the two forms are not rationally isometric; mod 241, "
        "(183I + 58J)(54I + 182J) = I for the six-site J":
            sp.factor(C5.charpoly(t).as_expr()) == sp.factor((t - 2) * (t ** 2 - 9 * t + 9) ** 2) and C5.det() == 162
            and (sp.eye(5) + J5).det() == 6 and not sp.sqrt(27).is_rational
            and ((183 * sp.eye(6) + 58 * J6) * (54 * sp.eye(6) + 182 * J6)).applyfunc(lambda z: z % 241) == sp.eye(6),
        "the golden convergents 2/1, 3/2, 5/3, 8/5, 13/8, 21/13 end 1/104 apart with phi between the last two; x -> 1 + 1/x "
        "and z -> z^2 - 1 share the fixed-point equation and differ at 2 (3/2 against 3); the quadratic's multipliers "
        "1 +- sqrt5 multiply to -4 and both exceed 1 in size, and 0 <-> -1 is its superattracting 2-cycle":
            conv == [2, sp.Rational(3, 2), sp.Rational(5, 3), sp.Rational(8, 5), sp.Rational(13, 8), sp.Rational(21, 13)]
            and abs(conv[5] - conv[4]) == sp.Rational(1, 104) and conv[5] < phi < conv[4]
            and sp.simplify(1 + 1 / phi - phi) == 0 and sp.simplify(g(phi) - phi) == 0
            and (1 + sp.Rational(1, 2), g(2)) == (sp.Rational(3, 2), 3)
            and sp.expand((1 + sp.sqrt(5)) * (1 - sp.sqrt(5))) == -4 and (1 - sp.sqrt(5)) ** 2 > 1
            and (g(0), g(-1)) == (-1, 0) and 2 * 0 * 2 * (-1) == 0,
        "arithmetic: K5 has 125 spanning trees (Cayley) among C(10, 4) = 210 four-edge sets; 1 + 5 x 7 = 36; the "
        "compound of I4 + J4 has determinant 125 and det(12I5 - 2J5) = 41472 = 16^2 x 162; Lambda^2 diag(2, 1, 1, 1, 1) "
        "has eigenvalues 2^4 1^6; the Singleton bounds 21 - 17 + 1 = 5 and 25 - 12 + 1 = 14; C(21, 4) x 250 = 1496250; "
        "N33's sheets 3750 and 3705 follow 14 = 2 + 3 + 4 + 5 and three steps of 4, with claims 12 + 29 + 25 + 29 = 95; "
        "E4 < 7/4; the coordinates of rho have plain square sum 56492 against |rho|^2 = 620; and the clock orders hold":
            trees == 125 and sp.binomial(10, 4) - trees == 85 and 1 + 5 * 7 == 36
            and sp.Matrix(6, 6, lambda a, b: (sp.eye(4) + sp.ones(4, 4)).extract(list(P4[a]), list(P4[b])).det()).det() == 125
            and (12 * sp.eye(5) - 2 * J5).det() == 41472 == 16 ** 2 * 162
            and sp.Matrix(compound2(sp.diag(2, 1, 1, 1, 1))).eigenvals() == {2: 4, 1: 6}
            and (21 - 17 + 1, 25 - 12 + 1) == (5, 14) and sp.binomial(21, 4) * 250 == 1496250
            and 3738 - 3724 == 3693 - 3679 == 14 == 2 + 3 + 4 + 5 and 3738 + 12 == 3750 and 3693 + 12 == 3705
            and 12 + 29 + 25 + 29 == 95 and lo < sp.Rational(7, 4)
            and int((principal.weyl_vector()[0] ** 2).sum()) == 56492
            and [order(s) for s in (138, 236, 183, 56, 63, 125, 7, 14121093, 1260720)]
            == [720, 1080, 1440, 540, 480, 864, 4320, 1440, 6] and order(125) == order(5),
    }


def _petersen_traces():
    E = carrier.edges()
    A = np.array([[int(not set(e) & set(f)) for f in E] for e in E], dtype=np.int64)
    tr = [int(np.trace(np.linalg.matrix_power(A, k))) for k in range(1, 7)]
    cycles = lambda n: sum(1 for c in itertools.permutations(range(10), n) if c[0] == min(c) and c[1] < c[-1]
                           and all(A[c[i], c[(i + 1) % n]] for i in range(n)))
    return tr, cycles(5), cycles(6)


def notes_0844():
    """The sibling's MODEL of 08:22-08:44: the 01:21 certificate, the pentagon operator, the overlays, the N33
    workbooks and the sector sheet."""
    order = lambda s: N // gcd(s, N)
    I5, J5, s5 = sp.eye(5), sp.ones(5, 5), sp.sqrt(5)
    R = sp.Matrix(5, 5, lambda i, j: int(j == (i + 1) % 5))
    P = sp.Matrix(5, 5, lambda i, j: 0 if i == j else 1 if (j - i) % 5 in (1, 4) else -1)
    B = sp.Matrix(carrier.signed_incidence())
    Q = sp.Matrix.hstack(*[I5[:, i] - I5[:, 4] for i in range(4)])     # a basis of the sum-zero four
    on_four = lambda X: (Q.T * Q).inv() * Q.T * X * Q
    half = (I5 + P / s5) / 2
    roots = glue.roots()
    graph = sorted(Counter(np.rint(np.linalg.eigvalsh(np.isclose(roots @ roots.T, 1).astype(float))).astype(int)).items())
    m = [1, 242, 58702, 14267058]
    b1 = m[2] - m[1] ** 2
    left = m[3] - m[1] ** 3 - 2 * m[1] * b1
    return {
        "the 01:21 certificate: its ten exact-check counts sum to 393 and its regressions to 14 and 8; 500 + 56 = 556, "
        "135 - 115 = 20, 53130 = C(25, 5), 1496250 = C(21, 4) x 250, 63 = 2^6 - 1 and 15 = C(6, 2); on the circle 393, "
        "556, 56, 115, 506 and 67 have orders 1440, 1080, 540, 864, 2160 and 4320":
            sum([54, 80, 15, 24, 14, 27, 98, 67, 9, 5]) == 393 and 3 + 2 + 9 == 14 and 4 + 2 + 2 == 8
            and 500 + 56 == 556 and 135 - 115 == 20 and comb(25, 5) == 53130 and comb(21, 4) * 250 == 1496250
            and 2 ** 6 - 1 == 63 and comb(6, 2) == 15
            and [order(x) for x in (393, 556, 56, 115, 506, 67)] == [1440, 1080, 540, 864, 2160, 4320],
        "the pentagon operator, +1 on the pentagon steps and -1 on the pentagram steps, is the tick's Gauss sum "
        "R + R^4 - R^2 - R^3 = 2(I + R + R^4) - I - J on the vertices: P^2 = 5I - J = B B^T, the K5 Laplacian, P kills "
        "the constants and (sqrt5 I + P)(sqrt5 I - P) = J; so (I +- P/sqrt5)/2 are complementary projectors on the "
        "sum-zero four, where P has eigenvalues +-sqrt5 twice each, and not on R^5":
            P == R + R ** 4 - R ** 2 - R ** 3 == 2 * (I5 + R + R ** 4) - I5 - J5 and P * P == 5 * I5 - J5 == B * B.T
            and P * sp.ones(5, 1) == sp.zeros(5, 1)
            and sp.simplify((s5 * I5 + P) * (s5 * I5 - P) - J5) == sp.zeros(5)
            and sp.simplify(on_four(half) ** 2 - on_four(half)) == sp.zeros(4)
            and sp.simplify(half * half - half) != sp.zeros(5) and P.eigenvals() == {s5: 2, -s5: 2, 0: 1},
        "the 01:21 checkpoint's overlays: 52 + 56 + 70 + 142 = 320 new exact checks, 4 + 4 + 10 + 8 + 8 = 34 "
        "regressions and 24 + 108 + 103 + 132 + 125 + 528 = 1020 payloads; the step 6 has order 720 = 4320/6, 320 has "
        "order 27 and 1020 order 72":
            sum([52, 56, 70, 142]) == 320 and sum([4, 4, 10, 8, 8]) == 34
            and sum([24, 108, 103, 132, 125, 528]) == 1020 and order(6) == 720 == N // 6
            and order(320) == 27 and order(1020) == 72,
        "the N33 workbooks: 3750 - 3705 = 45 sheets; 6 + 6 + 18 + 210 = 240 with 6 + 6 + 18 = 30, six classes of 40; "
        "183 + 6 x 52 = 495; 241I - J has trace 1440 = 6 x 240 on six sites; 21 - 17 + 1 = 5 meets the Singleton "
        "bound; 125 = 5^3 and 5985 = C(21, 4)":
            3750 - 3705 == 45 and 6 + 6 + 18 + 210 == 240 and 6 + 6 + 18 == 30 and 240 // 6 == 40
            and 183 + 6 * 52 == 495 and (241 * sp.eye(6) - sp.ones(6, 6)).trace() == 1440 == 6 * 240
            and 21 - 17 + 1 == 5 and 5 ** 3 == 125 and comb(21, 4) == 5985,
        "the sector sheet: the root graph's eigenvalues besides its degree 56 are 28, 8, -2 and -4, which add to 30 and "
        "whose absolute values multiply to 1792 = 8 x 224; the sheet's moments 1, 242, 58702, 14267058 have variance "
        "138 and the next Jacobi coefficient 27778/138 = 13889/69, and differ from the contrast list 1, 241, 58264, "
        "14121093 by 1, 438 and 145965 and from the triangle port's 1, 242, 58691, 14259954 by 0, 11 and 7104; 30 and "
        "210 have order 144, 40 order 108, 125 order 864 and 29 order 4320":
            [e for e, _ in graph] == [-4, -2, 8, 28, 56] and 28 + 8 - 2 - 4 == 30 and 28 * 8 * 2 * 4 == 1792 == 8 * 224
            and b1 == 138 and left == 27778 and Fraction(left, b1) == Fraction(13889, 69) and left % b1
            and (242 - 241, 58702 - 58264, 14267058 - 14121093) == (1, 438, 145965)
            and (58702 - 58691, 14267058 - 14259954) == (11, 7104)
            and [order(x) for x in (30, 210, 40, 125, 29)] == [144, 144, 108, 864, 4320],
    }


def notes_0912():
    """The sibling's MODEL of 09:02-09:12, the separate model's continuation (08:53) and its note corrections (09:07)."""
    order = lambda s: N // gcd(s, N)
    sub = lambda s: set(spine.subgroup(s))
    I5, J5, s5 = sp.eye(5), sp.ones(5, 5), sp.sqrt(5)
    R = sp.Matrix(5, 5, lambda i, j: int(j == (i + 1) % 5))
    P = R + R ** 4 - R ** 2 - R ** 3
    t = sp.symbols("t")
    Q = sp.Matrix.hstack(*[I5[:, i] - I5[:, 4] for i in range(4)])
    on_four = lambda X: (Q.T * Q).inv() * Q.T * X * Q
    Jac = sp.Matrix([[242, 138], [1, sp.Rational(13889, 69)]])
    return {
        "the sibling's arithmetic: 138 and 438 have order 720; 3 x 12 + 3 x 8 + 3 x 6 + 2 = 80 = 5 x 16; "
        "943507 = 433 x 2179; 35366 = 183 x 193 + 47; the 08:54 certificate's packets 12 + 10 + 5 + 11 + 17 + 11 = 66 "
        "with 60 hashes, 151 - 150 = 1, 4052 + 28 = 4080, 556 + 18 = 574 and 288/625 in lowest terms; 1073 = 29 x 37":
            order(138) == order(438) == 720 and 3 * 12 + 3 * 8 + 3 * 6 + 2 == 80 == 5 * 16 and 433 * 2179 == 943507
            and 183 * 193 + 47 == 35366 and sum([12, 10, 5, 11, 17, 11]) == 66 and sum([11, 9, 4, 10, 16, 10]) == 60
            and 151 - 150 == 1 and 4052 + 28 == 4080 and 556 + 18 == 574 and gcd(288, 625) == 1
            and 288 == 32 * 9 and 625 == 5 ** 4 and 29 * 37 == 1073
            and [order(x) for x in (28, 150, 66, 41, 13, 1073)] == [1080, 144, 720, 4320, 4320, 4320],
        "the pentagon operator as the sibling replays it: P^3 = 5P, characteristic polynomial t (t^2 - 5)^2, rank 4, "
        "the four nonzero eigenvalues' squares multiply to 625, and tr P^0 = 5, tr P^(2m+1) = 0, tr P^(2m) = 4 x 5^m":
            P ** 3 == 5 * P and sp.expand(P.charpoly(t).as_expr() - t * (t ** 2 - 5) ** 2) == 0 and P.rank() == 4
            and 5 ** 4 == 625 and all((P ** k).trace() == (5 if k == 0 else 0 if k % 2 else 4 * 5 ** (k // 2))
                                      for k in range(9)),
        "the separate model's three corrections, replayed: the rational Jacobi matrix [[242, 138], [1, 13889/69]] "
        "gives the sheet's moments 1, 242, 58702, 14267058 exactly, so non-divisibility excludes only an integer "
        "diagonal; <125> = <5> is the miss set, of order 864, not the tick <864> of order 5, and the two meet in 0 and "
        "make the circle; the pentagon factors multiply to J on R^5 and to 0 on the sum-zero four":
            [(Jac ** k)[0, 0] for k in range(4)] == [1, 242, 58702, 14267058]
            and sub(125) == sub(5) and len(sub(125)) == 864 and len(sub(864)) == 5 and sub(125) & sub(864) == {0}
            and len({(a + b) % N for a in sub(864) for b in sub(5)}) == N
            and sp.simplify((s5 * I5 + P) * (s5 * I5 - P) - J5) == sp.zeros(5)
            and sp.simplify(on_four((s5 * I5 + P) * (s5 * I5 - P))) == sp.zeros(4),
        "a correction of the same kind: 1060 generates <20>, of order 216, while the golden orbit <216> has order 20; "
        "the two meet in the observer clock <1080>":
            sub(1060) == sub(20) and len(sub(20)) == 216 and len(sub(216)) == 20 and sub(20) & sub(216) == sub(1080)
            and len(sub(1080)) == 4,
    }


def _histories():
    """The sibling's two bivector histories on R^5 (09:38-09:51): the false e0 ^ (e1 + u e2 + u^2 e3) and the genuine
    (e0 + u e1) ^ (e2 + u e3), with the 25 Plucker equations on the 30 coefficients of a degree-two history."""
    u = sp.symbols("u")
    pairs, quads = list(itertools.combinations(range(5), 2)), list(itertools.combinations(range(5), 4))
    e = [sp.Matrix([int(i == k) for i in range(5)]) for k in range(5)]
    wedge = lambda a, b: [a[i] * b[j] - a[j] * b[i] for i, j in pairs]

    def square(X):                                                # X ^ X on the five four-sets
        out = []
        for q in quads:
            s = 0
            for i, j in itertools.combinations(q, 2):
                k, l = [x for x in q if x not in (i, j)]
                s += Permutation([q.index(x) for x in (i, j, k, l)]).signature() * X[pairs.index((i, j))] * X[pairs.index((k, l))]
            out.append(s)
        return out
    c = sp.symbols("c0:30")
    history = [c[k] + u * c[10 + k] + u ** 2 * c[20 + k] for k in range(10)]
    eqs = [sp.Poly(sp.expand(w), u).coeff_monomial(u ** d) for w in square(history) for d in range(5)]
    jac = sp.Matrix([[sp.diff(q, x) for x in c] for q in eqs])
    coeffs = lambda B: [sp.Poly(sp.expand(B[k]), u).coeff_monomial(u ** d) for d in range(3) for k in range(10)]
    false = wedge(e[0], e[1] + u * e[2] + u ** 2 * e[3])
    genuine = wedge(e[0] + u * e[1], e[2] + u * e[3])
    return u, pairs, e, wedge, square, c, eqs, jac, coeffs, false, genuine


def _syzygies(B, u, pairs):
    """The degree <= 1 vector polynomials v with v ^ B = 0: the rank of the map and its kernel."""
    a = sp.symbols("a0:10")
    v = [a[k] + u * a[5 + k] for k in range(5)]
    rows = []
    for i, j, k in itertools.combinations(range(5), 3):
        w = sp.Poly(sp.expand(v[i] * B[pairs.index((j, k))] - v[j] * B[pairs.index((i, k))] + v[k] * B[pairs.index((i, j))]), u)
        rows += [[sp.diff(w.coeff_monomial(u ** d), x) for x in a] for d in range(4)]
    M = sp.Matrix(rows)
    return M.rank(), [sp.Matrix([x[k] + u * x[5 + k] for k in range(5)]) for x in M.nullspace()]


def _rosebud():
    """The hub's Golden reference (09:23): the sum-zero four with an orthonormal basis, Lambda^2 of it, the six
    Sylow-five averages F_i and the selected channel Phi(X) = sum tr(F_i X / 2) (11 I - 5 F_i)/56."""
    Hb = np.linalg.qr(np.vstack([np.ones(5), np.eye(5)[:4]]).T)[0][:, 1:5]
    pm = lambda p: np.array([[float(p[j] == i) for j in range(5)] for i in range(5)])   # e_j -> e_p(j)
    rho4 = lambda p: Hb.T @ pm(p) @ Hb
    pairs = list(itertools.combinations(range(4), 2))
    wedge2 = lambda M: np.array([[M[i, k] * M[j, l] - M[i, l] * M[j, k] for k, l in pairs] for i, j in pairs])
    sign = lambda p: round(np.linalg.det(pm(p)))
    groups = []
    for p in itertools.permutations(range(5)):
        if [len(c) for c in _cycles(list(p))] == [5]:
            g, q = {tuple(range(5))}, p
            while q != tuple(range(5)):
                g.add(q)
                q = tuple(p[x] for x in q)
            if g not in groups:
                groups.append(g)
    F = [sum(wedge2(rho4(g)) for g in grp) / 5 for grp in groups]
    E, sig = [f / 2 for f in F], [(11 * np.eye(6) - 5 * f) / 56 for f in F]
    Phi = lambda X: sum(np.trace(E[i] @ X) * sig[i] for i in range(6))
    return rho4, wedge2, sign, F, E, sig, Phi


def notes_0951():
    """The sibling's MODEL of 09:38-09:51 (the source histories), the separate model's source-history completion
    (09:24) and the hub's text as revised at 09:23 (the Rosebud reference and the local arithmetic)."""
    u, pairs, e, wedge, square, c, eqs, jac, coeffs, false, genuine = _histories()
    at = lambda B: dict(zip(c, coeffs(B)))
    Jf, Jg = jac.subs(at(false)), jac.subs(at(genuine))
    rf, rg, rs = Jf.rank(), Jg.rank(), Jf.col_join(Jg).rank()
    sf, kf = _syzygies(false, u, pairs)
    sg, kg = _syzygies(genuine, u, pairs)

    def meet(B):                                                  # the line common to the planes B(0), ..., B(3)
        planes = []
        for x in range(4):
            M = sp.zeros(5, 5)
            for (i, j), val in zip(pairs, B):
                M[i, j], M[j, i] = sp.sympify(val).subs(u, x), -sp.sympify(val).subs(u, x)
            planes.append(sp.Matrix.hstack(*M.columnspace()))
        normals = sp.Matrix.vstack(*[sp.Matrix.hstack(*P.T.nullspace()).T for P in planes])
        return len(normals.nullspace())
    a0, b0 = e[0] + u * e[1], e[2] + u * e[3]
    scale = lambda M: {sp.simplify(x / y) for x, y in zip(wedge(M[0, 0] * a0 + M[0, 1] * b0, M[1, 0] * a0 + M[1, 1] * b0),
                                                          genuine) if y != 0}
    w4 = u * (u - 1) * (u - 2) * (u - 3)
    # the hub's Rosebud reference: six probes, the three-sector algebra, the Hom lines and the Golden channel
    B8, Binv, C, Cinv, R, RB = spine.frame()
    _, lines = cyclotomic.residue()
    line = [next(i for i, L in enumerate(lines) if cyclotomic.point(x) in L) for x in RB]
    Gr = RB @ C @ RB.T
    A2 = (Gr == 1).astype(int) @ (Gr == 1).astype(int)
    on = lambda l: [i for i in range(240) if line[i] == l]
    probes = next((a, c1, e1, b, d, f) for a in on(0) for b in on(3) if Gr[a, b] == -1
                  for c1 in on(1) if not Gr[a, c1] and not Gr[b, c1] for d in on(4) if Gr[c1, d] == -1 and not Gr[a, d]
                  and not Gr[b, d] for e1 in on(2) if not any(Gr[x, e1] for x in (a, b, c1, d)) for f in on(5)
                  if Gr[e1, f] == -1 and not any(Gr[x, f] for x in (a, b, c1, d)))
    V = A2[np.ix_(probes, probes)]
    I6, J6 = sp.eye(6), sp.ones(6, 6)
    H = sp.Matrix(6, 6, lambda i, j: int(abs(i - j) == 3))
    E0, Ep, Em = J6 / 6, (I6 + H) / 2 - J6 / 6, (I6 - H) / 2
    P, Vs = (10 * J6 - 4 * I6) / 56, 44 * I6 + 12 * J6 - 11 * H
    rho4, wedge2, sign, F, E, sig, Phi = _rosebud()

    def hom(gens):                                                # dim Hom_G(Lambda^2 A4, sign (x) A4)
        M = np.vstack([np.kron(wedge2(rho4(g)).T, np.eye(4)) - np.kron(np.eye(6), sign(g) * rho4(g)) for g in gens])
        return 24 - np.linalg.matrix_rank(M, tol=1e-9)
    c5, flip, dbl, swap = (1, 2, 3, 4, 0), (0, 4, 3, 2, 1), (0, 2, 4, 1, 3), (1, 0, 2, 3, 4)
    basis = [np.outer(np.eye(6)[i], np.eye(6)[j]) for i in range(6) for j in range(6)]
    S = np.array([Phi(X).ravel() for X in basis]).T
    spec = sorted(Counter(np.round(np.linalg.eigvals(S).real, 9) + 0).items())
    D = lambda X: np.trace(X) * np.eye(6) / 6
    X0 = np.arange(36.0).reshape(6, 6) % 7 - 3
    power = lambda X, n: X if n == 0 else power(Phi(X), n - 1)
    choi = lambda n: sum(np.kron(b, power(b, n)) for b in basis)
    lam1, lam2 = np.linalg.eigvalsh(choi(1)), np.linalg.eigvalsh(choi(2))
    Xw = F[0] - F[1]
    lanes = lambda W: [a for a in range(W) if gcd(a * (a + 2), W) == 1]
    omega = sp.Matrix([4, -1, -1, -1, -1]) / 5
    in_a4 = lambda x: all(t.is_integer for t in x) and sum(x) == 0
    shift = sp.Matrix(5, 5, lambda i, j: int(i == (j + 1) % 5))
    mask = sp.diag(*[int(a in lanes(5)) for a in range(5)])
    affine = [(a, b) for a in range(1, 5) for b in range(5)]
    return {
        "the source histories: the false e0 ^ (e1 + u e2 + u^2 e3) and the genuine (e0 + u e1) ^ (e2 + u e3) both pass "
        "all 25 Plucker equations on the 30 coefficients, which linearize to rank 13 at both (kernels of 17 meeting in "
        "8, row spaces in 4)": all(q.subs(at(false)) == 0 and q.subs(at(genuine)) == 0 for q in eqs) and len(eqs) == 25
        and (rf, rg, 30 - rs, rf + rg - rs) == (13, 13, 8, 4),
        "the syzygies separate them: both have rank 8 and nullity 2, the false kernel e0, u e0 wedges to 0, so no "
        "two-packet factorization exists, and the genuine kernel e0 + u e1, e2 + u e3 wedges back to the history; the "
        "false planes share the line e0, the genuine planes meet in 0; a determinant-1 change of the packets fixes the "
        "wedge and a determinant-2 one doubles it; u(u - 1)(u - 2)(u - 3) is 0 at four phases and 24 at the fifth":
            (sf, len(kf), sg, len(kg)) == (8, 2, 8, 2) and not any(sp.expand(x) for x in wedge(kf[0], kf[1]))
            and [sp.expand(x) for x in wedge(kg[0], kg[1])] == [sp.expand(x) for x in genuine]
            and (meet(false), meet(genuine)) == (1, 0) and scale(sp.Matrix([[2, 1], [3, 2]])) == {1}
            and scale(sp.Matrix([[2, 0], [0, 1]])) == {2} and [w4.subs(u, k) for k in range(5)] == [0, 0, 0, 0, 24],
        "the 09:24 certificate's counts: 4080 + 25 = 4105 artifacts, 574 + 13 = 587 relationships, 3 + 12 = 15 "
        "regressions, 68 files with 67 hashes; the 09:07 correction's 577 = 574 + 3 was not absorbed by its parent":
            4080 + 25 == 4105 and 574 + 13 == 587 and 3 + 12 == 15 and 68 - 67 == 1 and 574 + 3 == 577 != 587,
        "the hub's six root probes (09:23): one root on each of the six residue lines, in three orthogonal A2 pairs, "
        "have two-step return Gram A^2 = 44I + 12J - 11H on the root graph (56 on the diagonal, 1 in a pair, 12 "
        "between pairs), and with the six-line quotient's P = (10J - 4I)/56 = E0 - (E+ + E-)/14 and V = 105 E0 + "
        "33 E+ + 55 E- they give H = (244I + 336P - 5V)/55, E0 = (I + 14P)/15 and E- = (5V - 189I - 336P)/110":
            np.array_equal(V, 44 * np.eye(6, dtype=int) + 12 * np.ones((6, 6), dtype=int) - 11 * np.array(H, dtype=int))
            and len({line[i] for i in probes}) == 6 and P == E0 - (Ep + Em) / 14 and Vs == 105 * E0 + 33 * Ep + 55 * Em
            and H == (244 * I6 + 336 * P - 5 * Vs) / 55 and E0 == (I6 + 14 * P) / 15
            and Em == (5 * Vs - 189 * I6 - 336 * P) / 110 and all(X * X == X for X in (E0, Ep, Em)),
        "the bright six Lambda^2 A4 and the dark four sign (x) A4 have intertwiners of dimension 4, 2, 1 and 0 under "
        "C5, D10, F20 and S5: one F20 line, and none under S5":
            [hom(g) for g in ([c5], [c5, flip], [c5, dbl], [c5, swap])] == [4, 2, 1, 0],
        "the six Sylow-five averages on Lambda^2 A4 are rank-two projectors with sum 2I and tr F_i F_j = 2/5, and the "
        "selected channel Phi(X) = sum tr(F_i X / 2)(11I - 5F_i)/56 measures the six-line transition (10J - 4I)/56, "
        "has spectrum 1, (-1/14)^5, 0^30 and Phi^n = D + (-1/14)^(n-1)(Phi - D)":
            len(F) == 6 and all(round(np.trace(f)) == 2 and np.allclose(f @ f, f) for f in F)
            and np.allclose(sum(F), 2 * np.eye(6))
            and all(np.isclose(np.trace(F[i] @ F[j]), 0.4) for i in range(6) for j in range(6) if i != j)
            and np.allclose([[np.trace(E[i] @ sig[j]) for j in range(6)] for i in range(6)],
                            (10 * np.ones((6, 6)) - 4 * np.eye(6)) / 56)
            and spec == [(-0.071428571, 5), (0.0, 30), (1.0, 1)]
            and all(np.allclose(power(X0, n), D(X0) + (-1 / 14) ** (n - 1) * (Phi(X0) - D(X0))) for n in range(1, 6)),
        "its Choi spectrum is (3/28)^2, (1/7)^10, (9/56)^10, (11/56)^14 with trace 6, the second channel's is "
        "1/6 + (-1/14)(lambda - 1/6), and X = F0 - F1 has Tr X^2 = 16/5 and Phi(X) = -X/14, the witness of the hub's "
        "no-go for a closed finite unreset bath":
            sorted(Counter(np.round(lam1 * 56, 6) + 0).items()) == [(6.0, 2), (8.0, 10), (9.0, 10), (11.0, 14)]
            and np.isclose(lam1.sum(), 6) and np.allclose(np.sort(lam2), np.sort(1 / 6 - (lam1 - 1 / 6) / 14))
            and np.isclose(np.trace(Xw @ Xw), 16 / 5) and np.allclose(Phi(Xw), -Xw / 14),
        "the hub's local arithmetic: the twin lanes gcd(a(a + 2), W) = 1 are 1, 2, 4 mod 5, 36 mod 360 and 432 mod "
        "4320, and reduction mod 360 is 12 to 1 onto the 36; omega = (4, -1, -1, -1, -1)/5 generates A4*/A4 = Z/5 and "
        "every coordinate permutation fixes its class; (1 - 2/5)/(1 - 1/5)^2 = 15/16; the lane mask does not commute "
        "with the shift (commutator rank 4), and {0, 2} has a stabilizer of order 2 in AGL(1,5)":
            lanes(5) == [1, 2, 4] and len(lanes(360)) == 36 and len(lanes(4320)) == 432
            and Counter(a % 360 for a in lanes(4320)) == Counter({a: 12 for a in lanes(360)})
            and all(not in_a4(k * omega) for k in range(1, 5)) and in_a4(5 * omega)
            and all(in_a4(sp.Matrix([omega[p[i]] for i in range(5)]) - omega) for p in itertools.permutations(range(5)))
            and Fraction(3, 5) / Fraction(4, 5) ** 2 == Fraction(15, 16) and (mask * shift - shift * mask).rank() == 4
            and len([m for m in affine if {(m[0] * x + m[1]) % 5 for x in (0, 2)} == {0, 2}]) == 2,
    }


def notes_1004():
    """The hub's N33 reconciliation (09:54) and the separate model's unified connections (09:54)."""
    roots = glue.roots()
    A = np.isclose(roots @ roots.T, 1).astype(np.int64)
    closed = [int(np.trace(np.linalg.matrix_power(A, n))) // 240 for n in range(7)]
    W, _ = _walks()
    I6, J6 = sp.eye(6), sp.ones(6, 6)
    E = J6 / 6
    P = (10 * J6 - 4 * I6) / 56
    t = sp.log(196)
    nodes = [Fraction(2 * c - 35, 35) for c in range(36)]
    R = sp.Matrix(5, 5, lambda i, j: int(j == (i + 1) % 5))
    G5 = R + R ** 4 - R ** 2 - R ** 3
    M = sp.Matrix(carrier.signless_incidence())
    perm = lambda p: sp.Matrix(5, 5, lambda i, j: int(i == p[j]))
    fixed = [p for p in itertools.permutations(range(5)) if perm(p) * G5 * perm(p).T == G5]
    reversed_ = [p for p in itertools.permutations(range(5)) if perm(p) * G5 * perm(p).T == -G5]
    affine = {tuple((a * x + b) % 5 for x in range(5)) for a in range(1, 5) for b in range(5)}
    return {
        "the finite root graph's closed walks are 1, 0, 56, 1512, 62160, 2872800, 144606784 per root, from its spectrum "
        "56, 28^8, 8^35, (-2)^112, (-4)^84, while the infinite lattice's are W_2, W_3, W_4 = 240, 13440, 1260720: the "
        "two walk counts are different operators' (J04, J05)":
            closed == [1, 0, 56, 1512, 62160, 2872800, 144606784]
            and closed[6] * 240 == 56 ** 6 + 8 * 28 ** 6 + 35 * 8 ** 6 + 112 * 2 ** 6 + 84 * 4 ** 6
            and [int(x) for x in W[2:5]] == [240, 13440, 1260720],
        "the six-line transition P = (10J - 4I)/56 = E - (I - E)/14 has det (-1/14)^5 < 0, so it is e^B for no real B, "
        "while P^2 = E + (I - E)/196 = e^(log 196 (E - I)), a two-step Markov embedding (J06)":
            P == E - (I6 - E) / 14 and P.det() == sp.Rational(-1, 14) ** 5
            and P * P == E + (I6 - E) / 196 == E + sp.exp(-t) * (I6 - E),
        "the 36 contexts t_c = (2c - 35)/35 are distinct, so all C(36, 3) = 7140 Vandermonde minors of the quadratic "
        "evaluator are nonzero: an MDS [36, 3, 34] code over Q, correcting 33 erasures or 16 errors (J08)":
            len(set(nodes)) == 36 and comb(36, 3) == 7140 and 36 - 3 + 1 == 34 and (34 - 1, (34 - 1) // 2) == (33, 16),
        "the Golden Gauss operator G5 = R + R^-1 - R^2 - R^-2 has G5^2 = 5I - J, G5^3 = 5 G5 and M M^T + G5^2 = 8I with "
        "the signless incidence (J19); the permutations of the five vertices fix it for D10 (10 of them) and reverse it "
        "for the other 10 of AGL(1,5): x -> ax + b multiplies it by the Legendre symbol (a/5)":
            G5 * G5 == 5 * sp.eye(5) - sp.ones(5, 5) and G5 ** 3 == 5 * G5 and M * M.T + G5 * G5 == 8 * sp.eye(5)
            and len(fixed) == len(reversed_) == 10 and set(fixed) | set(reversed_) == affine
            and all(perm(tuple((a * x + b) % 5 for x in range(5))) * G5 * perm(tuple((a * x + b) % 5 for x in range(5))).T
                    == sp.jacobi_symbol(a, 5) * G5 for a in range(1, 5) for b in range(5)),
        "the 09:54 connections certificate: 40 + 12 + 61 + 21 = 134 new exact groups, 6 + 2 + 5 = 13 API regressions, "
        "4105 + 61 = 4166 artifacts, 587 + 20 + 3 = 610 relationships and 191 files with 190 hashes":
            40 + 12 + 61 + 21 == 134 and 6 + 2 + 5 == 13 and 4105 + 61 == 4166 and 587 + 20 + 3 == 610
            and 191 - 190 == 1,
    }


def notes_1411():
    """The canon's N34 release (14:04-14:11) and the sibling's MODEL of 14:06, replayed as arithmetic."""
    order = lambda s: N // gcd(s, N)
    tuple49 = [0, 2, 6, 8, 12, 20, 26, 30, 32, 36, 42, 48, 50, 56, 60, 68, 72, 78, 86, 92, 98, 102, 110, 116, 120, 126, 132,
               138, 140, 146, 152, 156, 158, 162, 168, 170, 176, 180, 182, 186, 188, 210, 212, 218, 222, 228, 230, 236, 240]
    omitted = {2: 1, 3: 1, 5: 4, 7: 3, 11: 7, 13: 5, 17: 11, 19: 14, 23: 16, 29: 18, 31: 4, 37: 7, 41: 11, 43: 1, 47: 7}
    m1, m2, d1 = 232, 54213, sp.Rational(975, 4)
    jets = lambda f1, f3, f5, a, b: (f1, f3 - a * f1, f5 - a * f3 + b * f1)         # y3, y5, y7 of y'' + Delta y = v f from rest
    roots = glue.roots()
    A = np.isclose(roots @ roots.T, 1).astype(np.int64)
    W, _ = _walks()
    I6, J6 = sp.eye(6), sp.ones(6, 6)
    Q = 10 * J6 - 4 * I6
    return {
        "the hub's 49-tuple: 49 distinct offsets with 0 and 2, diameter 240, and for every prime p <= 47 a residue it omits "
        "(the hub's listed residue among them), so it is admissible; for p > 49 the 49 offsets cannot fill p classes (N34-021)":
            len(set(tuple49)) == 49 and {0, 2} <= set(tuple49) and max(tuple49) - min(tuple49) == 240
            and all(a not in {h % p for h in tuple49} and len({h % p for h in tuple49}) < p for p, a in omitted.items())
            and sorted(omitted) == [p for p in range(2, 48) if all(p % q for q in range(2, p))],
        "the N34 jets: with the bright moments 232, 54213 and the dark first moment 975/4 held here, 248 = 232 + 16, "
        "58181 = 54213 + 16 x 232 + 16^2, 1039/4 = 975/4 + 16 and 47/4 = 975/4 - 232; these are the odd jets of "
        "y'' + Delta y = v f(t) from rest for a forcing with f' , f''', f^(5) = 1, -16, 256 (a harmonic forcing of frequency "
        "4): y3 = f1, y5 = f3 - m1 f1, y7 = f5 - m1 f3 + m2 f1; the canon's source q'' + 4q = 0 (frequency 2) would give "
        "y5 + 236 y3 = 0 and y7 - 55157 y3 = 0 (N34-012, N34-013)":
            248 == m1 + 16 and 58181 == m2 + 16 * m1 + 16 ** 2 and sp.Rational(1039, 4) == d1 + 16
            and d1 - m1 == sp.Rational(47, 4) and jets(1, -16, 256, m1, m2) == (1, -248, 58181)
            and jets(1, -16, 256, d1, sp.Rational(237985, 4))[1] == -sp.Rational(1039, 4)
            and jets(1, -4, 16, m1, m2) == (1, -236, 55157),
        "the N34 receipt: both workbooks grew by five tabs (3755 - 3750 = 3710 - 3705 = 5); 32 claims from 12 families; "
        "12 + 29 + 25 + 29 + 32 = 127 claims across N30-N34; no new matrix id and no gate change":
            3755 - 3750 == 5 == 3710 - 3705 and 12 + 29 + 25 + 29 + 32 == 127,
        "the sibling's 14:06 edition: the six-line quotient Q = 10J - 4I has Q^2 = 52 Q + 224 I ((x - 56)(x + 4) = x^2 - 52x "
        "- 224), with 224 the collar integer by coincidence; the root graph's minimal polynomial is (x - 56)(x - 28)(x - 8)"
        "(x + 2)(x + 4) and tr A^2 = 240 x 56 = 13440 = W_3, for a reason: both count the 240 x 56 ordered root pairs at "
        "inner product +-1, matched by r' -> -r'":
            Q * Q == 52 * Q + 224 * I6 and sp.expand((sp.Symbol("x") - 56) * (sp.Symbol("x") + 4)) == sp.expand(
                sp.Symbol("x") ** 2 - 52 * sp.Symbol("x") - 224)
            and not np.any(functools.reduce(np.matmul, [A - e * np.eye(240, dtype=np.int64) for e in (56, 28, 8, -2, -4)]))
            and int(np.trace(A @ A)) == 240 * 56 == int(W[3])
            and int(np.sum(np.isclose(roots @ roots.T, -1))) == 240 * 56,
        "the certificate's own counts, as the sibling reads them: 42 coordinate matrices + 16 aliases = 58, not the stated "
        "61 artifacts, and the listed typed relations 7 + 2 + 3 = 12, not the stated 20 joins; 587 + 20 + 3 = 610 holds; "
        "144606784 has order 135 on the circle, as 224 does":
            42 + 16 == 58 != 61 and 7 + 2 + 3 == 12 != 20 and 587 + 20 + 3 == 610
            and order(144606784) == order(224) == 135,
    }


# ------------------------------------------------------------------- joins of 30 Oct: every dot on THEOREM maps but two

def _cycles(perm):
    """The cycles of a permutation of range(n), each listed from its least point along the permutation."""
    cycles, seen = [], set()
    for s in range(len(perm)):
        if s not in seen:
            c = [s]
            while perm[c[-1]] != s:
                c.append(perm[c[-1]])
            seen |= set(c)
            cycles.append(c)
    return cycles


@functools.lru_cache(maxsize=1)
def _memory():
    """Layer 3's memory clock A as a permutation of its 120 states (A e_j = e_perm[j]), its cycles and its 90 powers."""
    _, _, _, A = spacetime.clock_quotient()
    perm = [int(np.argmax(A[:, j])) for j in range(120)]
    powers = [list(range(120))]
    for _ in range(89):
        powers.append([perm[x] for x in powers[-1]])
    return perm, _cycles(perm), powers


def memory_quotients():
    """The circle's maps onto the memory clock, without the selection: 24 of them, one orbit of the memory's symmetry."""
    perm, cycles, P = _memory()
    units = [u for u in range(90) if gcd(u, 90) == 1]

    def conjugator(u):                                      # pi(A^(uk) s) = A^k s on every cycle, so pi A^u = A pi
        pi = [0] * 120
        for c in cycles:
            x = c[0]
            for k in range(len(c)):
                pi[x], x = c[k], P[u][x]
        return pi
    conj = {u: conjugator(u) for u in units}
    nine = next(c for c in cycles if len(c) == 9)
    tens = [c for c in cycles if len(c) == 10]
    reads = lambda c, u, k: c.index(P[u * k % 90][c[0]])
    return {
        "the memory clock A permutes its 120 states with cycle type 10^11 9 1, so it has order 90":
            sorted(Counter(len(c) for c in cycles).items()) == [(1, 1), (9, 1), (10, 11)] and P[1] == perm,
        "every map of the circle onto <A> = Z/90 is k -> A^(uk) for one of the 24 units u mod 90, and each has kernel "
        "<90>, 48 points": len(units) == 24 and all(
            [k for k in range(N) if u * k % 90 == 0] == list(range(0, N, 90)) for u in units),
        "A^u has A's cycle type for every unit u, and a permutation of the 120 states conjugates it to A: the memory's "
        "normalizer in S_120 makes the 24 maps one orbit, so the canon's stepping k -> A^k is unique up to the memory's "
        "symmetry":
            all(sorted(pi) == list(range(120)) and all(pi[P[u][x]] == perm[pi[x]] for x in range(120))
                for u, pi in conj.items()),
        "for every one of them the 9-cycle reads x -> u x mod 9 and each 10-cycle x -> u x mod 10, and u is a power of "
        "2 mod 9 and mod 5 (2 is a primitive root of both): the vortex x mod 9 and the time coordinate x mod 5, up to "
        "the doubling":
            all(reads(nine, u, k) == u * k % 9 and all(reads(c, u, k) == u * k % 10 for c in tens)
                for u in units for k in range(1, 46))
            and {u % 9 for u in units} == {pow(2, j, 9) for j in range(6)}
            and {u % 5 for u in units} == {pow(2, j, 5) for j in range(4)},
    }


def massless_tower():
    """Layer 6 (conditional): every Kaluza-Klein tower of M4 x F starts on the five dark modes."""
    X = np.array([[1, -2, 0, 3], [2, 1, -1, 0], [0, 3, 1, -2], [-1, 0, 2, 1]])
    DM = np.block([[np.zeros((4, 4), dtype=int), X], [X.T, np.zeros((4, 4), dtype=int)]])   # an even stand-in for M4
    gam = np.diag([1] * 4 + [-1] * 4)
    DF = np.array(carrier.dirac(carrier.signless_incidence()), dtype=int)
    m = 2
    D = np.kron(DM, np.eye(15, dtype=int)) + np.kron(gam, m * DF)
    mu = np.linalg.eigvalsh((DM @ DM).astype(float))
    lam = np.rint(np.linalg.eigvalsh((DF @ DF).astype(float))).astype(int)
    spec = np.sort(np.linalg.eigvalsh((D @ D).astype(float)))
    ZF = lambda t: 5 + 8 * np.exp(-3 * m * m * t) + 2 * np.exp(-8 * m * m * t)
    kernel = sp.Matrix(DF).nullspace()
    return {
        "for D = D_M (x) 1 + gamma (x) m D_F, with gamma^2 = 1 anticommuting with D_M, the cross terms cancel: D^2 = "
        "D_M^2 (x) 1 + m^2 (1 (x) D_F^2), checked exactly on an even stand-in for M4's Dirac operator":
            np.array_equal(DM @ gam + gam @ DM, np.zeros((8, 8), dtype=int))
            and np.array_equal(D @ D, np.kron(DM @ DM, np.eye(15, dtype=int)) + m * m * np.kron(np.eye(8, dtype=int), DF @ DF)),
        "so spec D^2 = spec D_M^2 + m^2 {0, 3, 8}: over every level of M4 sits the tower 0, 3m^2, 8m^2 with "
        "multiplicities 5, 8 and 2, and the heat trace factorizes as Tr e^(-t D_M^2) (5 + 8 e^(-3 m^2 t) + 2 e^(-8 m^2 t))":
            sorted(Counter(lam.tolist()).items()) == [(0, 5), (3, 8), (8, 2)]
            and np.allclose(spec, np.sort((mu[:, None] + m * m * lam[None, :]).ravel()))
            and all(np.isclose(np.exp(-t * spec).sum(), np.exp(-t * mu).sum() * ZF(t)) for t in (0.05, 0.3, 1.0)),
        "the bottom of every tower is the five dark modes: ker D_F = 0 + ker M, so the massless sector of M4 x F is M4's "
        "levels times ker M, with the gap 3 m^2 = (h(D5) - h(A4)) m^2; M4 and m stay free":
            len(kernel) == 5 and all(v[i] == 0 for v in kernel for i in range(5))
            and len(sp.Matrix(carrier.signless_incidence()).nullspace()) == 5,
    }


def stiff_kernel():
    """Layer 7 (conditional): the stiff sector is the five dark modes, on every background."""
    U, sol, _ = _flrw()
    P0 = U.P[0]
    K = np.array(sp.Matrix.hstack(*sp.Matrix(carrier.signless_incidence()).nullspace()), dtype=float)
    momentum = np.array([np.exp(3 * sol.y[0, i]) * (P0 @ sol.y[17:, i]) for i in range(sol.y.shape[1])])
    return {
        "the kernel projector of D^2 is 0 + the projector onto ker M: the stiff sector is the five dark modes":
            np.allclose(P0[:5], 0) and np.allclose(P0[5:, 5:], K @ np.linalg.inv(K.T @ K) @ K.T)
            and round(float(np.trace(P0))) == 5,
        "P0 commutes with D^2, so psi'' + 3 H psi' + m^2 D^2 psi = 0 gives (a^3 P0 psi')' = 0: the dark modes' momentum "
        "a^3 P0 psi' is conserved whatever a(t) does, and their energy falls as a^-6 (checked along the flow, over which "
        "a grows 26-fold)":
            np.allclose(P0 @ U.K, U.K @ P0) and np.abs(momentum - momentum[0]).max() < 1e-8
            and np.exp(sol.y[0, -1]) > 20,
    }


def cosmos_calibration():
    """Layer 7 (conditional): a calibration acts on the cosmos's free inputs, and in the decoupling limit tau = 1/m."""
    U, _, (G, Lcc, m, psi0, v0) = _flrw()
    tau = 2.0
    gaps = []
    for lam in (Lcc, 0.3):
        s1 = cosmology.FLRW(G, lam, m).evolve(psi0, v0, 20.0, n=201)
        s2 = cosmology.FLRW(G, lam / tau ** 2, m / tau).evolve(psi0, v0 / tau, 20.0 * tau, n=201)
        gaps.append(max(np.abs(s1.y[2:17] - s2.y[2:17]).max(), np.abs(s1.y[0] - s2.y[0]).max(),
                        np.abs(s1.y[1] - tau * s2.y[1]).max(), np.abs(s1.y[17:] - tau * s2.y[17:]).max()))
    mu = 0.5
    s0 = cosmology.FLRW(0.0, 0.0, mu).evolve(psi0, mu * v0, 30.0, n=301)

    def native(u):                                             # psi'' + D^2 psi = 0 from (psi0, v0), in native time u
        out = U.P[0] @ (psi0 + u * v0)
        for lam, Pl in U.P.items():
            w = np.sqrt(float(lam))
            if w:
                out = out + Pl @ (np.cos(w * u) * psi0 + np.sin(w * u) / w * v0)
        return out
    return {
        "t -> tau t with m -> m/tau and Lambda_cc -> Lambda_cc/tau^2 carries the flow psi'' + 3 H psi' + m^2 D^2 psi = 0, "
        "H^2 = (8 pi G/3) rho + Lambda_cc/3 to a flow with the same a and psi, H and psi' divided by tau (checked at "
        "tau = 2 for Lambda_cc = 0 and 0.3): the conditional cosmos has no internal time unit either":
            max(gaps) < 1e-8,
        "in the decoupling limit G -> 0 with Lambda_cc tuned to 0, H stays 0 and the flow is the carrier's native flow "
        "in u = m t: the free mass scale is a calibration with tau = 1/m (checked at m = 1/2)":
            np.abs(s0.y[1]).max() == 0 and max(np.abs(s0.y[2:17, i] - native(mu * s0.t[i])).max()
                                                for i in range(len(s0.t))) < 1e-8,
    }


def day_units():
    """The day-Coxeter group modulo the tick is the unit group of the tick's residue field."""
    k = cyclotomic.clocks()
    c, d, g = (np.rint(k[n]).astype(np.int64) for n in ("c", "day", "g"))
    G = primes._matrix_group([c, d])
    key = lambda Q: tuple((np.asarray(Q) % 5).flatten().tolist())
    image = {key(cyclotomic.on_plane(x)) for x in G}
    Qc, Qd = cyclotomic.on_plane(c), cyclotomic.on_plane(d)
    days = {key(np.linalg.matrix_power(Qd, j)) for j in range(24)}
    field = {key(a * np.eye(2, dtype=np.int64) + b * Qc) for a in range(5) for b in range(5)}
    kernel = [x for x in G if key(cyclotomic.on_plane(x)) == (1, 0, 0, 1)]
    ticks = [spine.mpow(g, j) for j in range(5)]
    di = np.rint(np.linalg.inv(d)).astype(np.int64)
    return {
        "G120 = <c', d> has 120 elements, and each acts on the tick's residue plane E8/(1 - g)E8 as a multiplication "
        "a + b omega of the field F25 = F5[omega], omega the image of c'": len(G) == 120 and image <= field,
        "its image is all of F25^x, the 24 powers of the day, and its kernel is the tick <g>: G120 / <g> = F25^x, so "
        "G120 = <g> x| <d>, the day doubling the tick (d g d^-1 = g^2)":
            image == days and len(days) == 24 and len(kernel) == 5
            and all(any(np.array_equal(x, t) for t in ticks) for x in kernel)
            and np.array_equal(d @ g @ di, spine.mpow(g, 2)),
    }


def frame_a8():
    """The eight-root frame is an A8, the stabilizer of a census point of order 3."""
    e = lambda i: np.eye(8)[i]
    R = np.array([-e(0) - e(i) for i in range(1, 8)] + [-0.5 * np.ones(8)])
    roots = glue.roots()
    key = lambda v: tuple(np.rint(2 * v).astype(int))
    span = {key(x) for x in list(R) + list(-R) + [a - b for a, b in itertools.permutations(R, 2)]}
    W = np.linalg.inv(R).T                                      # the dual basis: <v_i, w_j> = delta_ij
    stab = lambda w: {key(r) for r in roots if abs(r @ w - round(r @ w)) < 1e-9}
    eps = lambda w: 240 - np.cos(2 * np.pi * roots @ w).sum()
    grad = lambda w: np.abs((np.sin(2 * np.pi * roots @ w)[:, None] * roots).sum(axis=0)).max()
    in_e8 = lambda v: (np.allclose(v, np.rint(v)) or np.allclose(v - 0.5, np.rint(v - 0.5))) and round(v.sum()) % 2 == 0
    census = {t: f for (_, t), f in handover.critical_census().items()}
    return {
        "the frame's 72 roots, +-v_i and v_i - v_j, are the roots of its span, an A8: Gram I + J is the A8 form in the "
        "basis e0 - e_i": len(span) == 72 and span <= {key(r) for r in roots},
        "each dual vector w_j is a point of order 3 of the momentum torus (3 w_j lies in E8, w_j does not) whose "
        "stabilizer is exactly the frame's A8":
            all(stab(w) == span and handover.stabiliser(roots, w)[0] == "A8" and in_e8(3 * w) and not in_e8(w) for w in W),
        "the band is critical there with eps = 252: the census's A8 family of 1920 = |W(E8)| / |W(A8)| points, the "
        "alcove's vertex of mark 3 and the principal steps 1440 and 2880":
            all(np.isclose(eps(w), 252) and grad(w) < 1e-9 for w in W) and round(240 - census["A8"]["lambda"]) == 252
            and census["A8"]["orbit"] == 1920 == 696729600 // factorial(9),
    }


def cube_frobenius():
    """AGL(1,5) on the four-cube's vertices, the cuts mod 2: the tick multiplies by zeta5, the doubling is Frobenius."""
    E = carrier.edges()
    star = lambda v: tuple(int(v in e) for e in E)
    plus = lambda a, b: tuple((x + y) % 2 for x, y in zip(a, b))
    cuts = {}
    for S in itertools.product(range(2), repeat=5):
        cuts.setdefault(functools.reduce(plus, (star(v) for v in range(5) if S[v]), (0,) * 10), S)

    def times_x(a):                                             # F16 = F2[x]/(x^4 + x^3 + x^2 + x + 1)
        return (a[3], (a[0] + a[3]) % 2, (a[1] + a[3]) % 2, (a[2] + a[3]) % 2)

    def mul(a, b):
        out = (0, 0, 0, 0)
        for i in range(4):
            if a[i]:
                out = plus(out, b)
            b = times_x(b)
        return out
    zeta = [(1, 0, 0, 0)]
    for _ in range(4):
        zeta.append(times_x(zeta[-1]))
    psi = lambda cut: functools.reduce(plus, (zeta[v] for v in range(5) if cuts[cut][v]), (0, 0, 0, 0))

    def act(f, cut):
        out = [0] * 10
        for k, (i, j) in enumerate(E):
            out[E.index(tuple(sorted((f(i), f(j)))))] = cut[k]
        return tuple(out)
    return {
        "delta({k}) -> zeta^k is a bijection from the sixteen cuts of K5 mod 2, the four-cube's vertices, onto F16 = "
        "F2[zeta5], well defined since the five vertex stars sum to 0 as the fifth roots of unity do":
            len(cuts) == 16 and len({psi(cut) for cut in cuts}) == 16
            and functools.reduce(plus, zeta, (0, 0, 0, 0)) == (0, 0, 0, 0),
        "the tick k -> k + 1 multiplies by zeta and the doubling k -> 2k is the Frobenius y -> y^2: AGL(1,5) acts on the "
        "cube's vertices as <zeta5> x| Gal(F16/F2) inside GammaL(1,16)":
            all(psi(act(lambda i: (i + 1) % 5, cut)) == mul(zeta[1], psi(cut))
                and psi(act(lambda i: 2 * i % 5, cut)) == mul(psi(cut), psi(cut)) for cut in cuts),
    }


def grain_steps():
    """The grain on the principal circle: the golden step times the sun's step, holding eleven regular steps."""
    reg = primes.regular()
    k = cyclotomic.clocks()
    held = [d for d in sorted(reg) if (N // d) % 72 == 0]
    return {
        "on the principal circle the grain <72> is the 60 points k rho/60, generated by the golden step 216 = rho/20 and "
        "the sun's step 1440 = rho/3, which carry the spectra of the golden clock and of the sun s = c'^10, the regular "
        "classes 20 and 3": gcd(216, 1440) == 72 and N // 20 == 216 and N // 3 == 1440
        and np.array_equal(reg[3], spine.mpow(k["c"], 10)) and np.array_equal(reg[20], k["golden"])
        and all(principal.regular_steps().values()),
        "it holds the step 4320/d of a regular order d exactly when d divides 60: the eleven regular orders 1, 2, 3, 4, "
        "5, 6, 10, 12, 15, 20 and 30, all but the day's 8 and 24":
            held == [d for d in sorted(reg) if 60 % d == 0] == [1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30],
    }


def plane_synthemes():
    """The secants through a point of PG(2,5) meet the conic in a syntheme: interior points are the ten, the
    exterior points' self-polar triangles the five."""
    points, conic, tangent, cross, on, sym2 = _plane()
    label = {x: c for c, x in conic.items()}
    count = {q: sum(on(L, q) for L in tangent.values()) for q in points}
    exterior = [q for q in points if q not in conic and count[q] == 2]
    interior = [q for q in points if q not in conic and count[q] == 0]
    secant = {frozenset(pr): cross(label[pr[0]], label[pr[1]]) for pr in itertools.combinations(range(6), 2)}
    through = lambda q: [pr for pr, L in secant.items() if on(L, q)]
    pole = {cross(tangent[label[a]], tangent[label[b]]): frozenset((a, b)) for a, b in itertools.combinations(range(6), 2)}
    syn = {q: frozenset(through(q)) for q in interior}
    syn.update({q: frozenset(through(q) + [pole[q]]) for q in exterior})
    perfect = lambda m: len(m) == 3 and len(set().union(*m)) == 6
    five = {syn[q] for q in exterior}
    triangles = [[q for q in exterior if syn[q] == m] for m in five]
    polar = lambda q: (-q[2] % 5, 2 * q[1] % 5, -q[0] % 5)          # the polar line of q for the conic y^2 = xz
    duads = [frozenset(dd) for dd in itertools.combinations(range(6), 2)]
    det = lambda m: (m[0] * m[3] - m[1] * m[2]) % 5
    pgl = {tuple(conic[sym2(m)(label[x])] for x in range(6)) for m in itertools.product(range(5), repeat=4) if det(m)}
    H, sig, S5, sgn, U = _six_lines()
    group = set(sig.values())
    f = next(f for f in itertools.permutations(range(6))
             if {tuple(f[s[f.index(x)]] for x in range(6)) for s in group} == pgl)
    move = lambda p, m: frozenset(frozenset(sig[p][y] for y in pr) for pr in m)
    special = {m for m in _matchings(range(6)) if len({move(p, m) for p in S5}) == 5}
    to_conic = lambda m: frozenset(frozenset(f[y] for y in pr) for pr in m)
    return {
        "the three secants through an interior point of PG(2,5) meet the conic in a syntheme of its six points, and the "
        "ten interior points give ten different synthemes": all(perfect(syn[q]) for q in interior)
        and len({syn[q] for q in interior}) == 10,
        "through an exterior point pass two secants, and with the duad of its two tangents they make a syntheme too: "
        "the fifteen exterior points give five synthemes, three times each, at the vertices of a self-polar triangle, "
        "and the five are a one-factorization, the other five of the fifteen":
            all(perfect(syn[q]) for q in exterior) and len(five) == 5 and all(len(t) == 3 for t in triangles)
            and all(on(polar(x), y) for t in triangles for x in t for y in t if x != y)
            and Counter(pr for m in five for pr in m) == Counter({dd: 1 for dd in duads})
            and five | {syn[q] for q in interior} == set(_matchings(range(6))),
        "a labelling of the conic by the six Sylow labels carries the hub's exceptional sigma onto PGL(2,5), and with "
        "it the five are the synthemes dot's special five, invariant under the exceptional S5, and the interior points "
        "its ten": len(pgl) == 120 and {to_conic(m) for m in special} == five,
    }


# ------------------------------------------------------------------- the diagram

DOTS = {
    "V": ("K5 vertices", "R^5, the five atoms", "1"),
    "E": ("K5 edges", "Lambda^2 R^5, the ten atoms", "1, 23"),
    "carrier": ("carrier", "R^15 with D^2 = M M^T + M^T M, spectrum 0^5 3^8 8^2", "1"),
    "kerM": ("zero modes", "ker M, the five dark modes", "1, 5"),
    "cycles": ("cycles", "ker B = Lambda^2 H, six", "22, 23"),
    "rotor": ("rotor plane", "the C5-fixed plane of the cycles", "22, 23"),
    "petersen": ("Petersen", "the graph on the ten edges", "1, 22"),
    "datum": ("datum", "(psi0, v0) with energy 34", "1, 22"),
    "source": ("source", "q'' + 4q = 0 on ker M + ker M", "4"),
    "A4": ("A4", "the 20 roots e_i - e_j", "11"),
    "D5": ("D5", "the 40 roots +-e_i +- e_j", "23"),
    "E8": ("E8", "the lattice and its 240 roots", "3, 11"),
    "L0": ("A4 + A4'", "index 5 in E8", "11, 23"),
    "bath": ("bath", "Delta = 240 - sum of root translations", "8, 22, 27"),
    "momenta": ("tick momenta", "the 25 fixed momenta of the tick", "23, 27"),
    "halfper": ("half-periods", "Lambda / 2 Lambda, 256", "22, 26, 27"),
    "pauli": ("Pauli algebra", "M16(R) with L", "22, 27"),
    "gksl": ("GKSL", "the semigroup e^-tL", "22, 27"),
    "triangle": ("triangle port", "the oriented triangle 0-1-2 on the lattice", "22, 23"),
    "sixsite": ("six-site port", "K5 coned off, an A5 simplex", "4, 22, 23"),
    "moments": ("moments", "the Stieltjes data of the ports", "22"),
    "walks": ("closed walks", "W_n on the lattice, each step a root; one operator of order 16, degree 58 mod primes", "3, 14"),
    "clocks": ("W(E8) clocks", "c', g = r r', d, v, m", "19, 21"),
    "G120": ("day-Coxeter group", "<c', d>, order 120", "21, 22"),
    "AGL": ("AGL(1,5)", "the affine group of the pentagon", "21"),
    "circle": ("circle", "Z/4320", "19, 28"),
    "time": ("time clock", "<864> = Z/5, the principal points of order 5 (rho/5)", "21, 22, 28"),
    "observer": ("observer clock", "<1080>, the principal points of order 4 (rho/4), the regular class 4 = d^6; inside the 2-clock <135>", "22, 23, 28"),
    "c27": ("27-clock", "<160>, the nakshatra", "20, 23, 28"),
    "atlas": ("atlas", "Z/36 = circle / <36>, the circle modulo its regular steps", "23, 28"),
    "golden": ("golden companion", "B = [[1, 1], [1, 0]]", "21, 22"),
    "stages": ("stages", "the fifteen indices", "22"),
    "cube": ("four-cube", "the 81-cell complex of [0, 1]^4", "21, 23"),
    "hodge": ("Hodge 70", "Lambda^4 R^8 = 35 + 35", "23"),
    "coil": ("coil", "<8>, the 540 multiples of 8: the grain plus the 27-clock", "23, 28"),
    "S5": ("S5", "the 120 vertex permutations, the cone point's stabilizer in S6", "1, 23"),
    "pgl": ("PGL(2,5)", "the transitive S5 in S6, on the projective line over F5", "23"),
    "grain": ("grain", "<72> = <216> x <1440>, the golden orbit times the sun: the 60 points k rho/60 the critical steps generate", "23, 28"),
    "vortex": ("vortex", "Z/9, the address mod 9: the 27-clock modulo the sun", "23, 28"),
    "miss": ("miss set", "<5>, the 864 points the tick does not see: the kernel of the time coordinate", "23, 28"),
    "frame": ("eight-root frame", "the origin and eight roots with pairwise products 1: a maximal 9-clique, index 3", "23"),
    "triple": ("spectral triple", "(A, H, D, gamma) on l2(V u E), dim 15, with D^2 = M M^T + M^T M", "2, 9"),
    "surface": ("surface", "RP^2: the hemi-icosahedron on the six axes and its complement, 1-skeleton K6", "3, 9"),
    "readout": ("readout", "the carrier as a control system x' = Ax, A = [[0, I], [-D^2, 0]], with named readouts", "5, 9"),
    "gravity": ("product geometry", "M4 x F and its spectral action, with M4, f, L and m free (conditional)", "6, 9"),
    "cosmology": ("FLRW", "the carrier field on a flat FLRW background (conditional)", "7"),
    "literal": ("literal operands", "the owner's native_source_matrices, SHA-256 73e07429...", "10"),
    "binding": ("binding", "the commutant of D and the anomaly-free content 5 + Lambda^2 5", "12"),
    "calibration": ("calibration", "t = tau u and the readout law omega = omega_hat / tau (TIME_BIND)", "13"),
    "measure": ("spectral measures", "the six-port's sector measures on [0, 256], with Gauss and Lobatto envelopes", "15"),
    "census": ("critical census", "the band's 11 critical families on the alcove, 243600 points", "16, 28"),
    "waves": ("sound and light", "the K5 edge Hodge complex: sound im d0, light ker d0^T, Curl = *d1", "17"),
    "torus": ("nine-torus", "T^9 of the nine positive critical frequencies, with a dense flow", "18"),
    "rootgraph": ("root graph", "the 240 roots, adjacent at inner product 1: a four-class association scheme", "3, 22, 23"),
    "cyclo": ("cyclotomic line", "E8 = Z[zeta30] with the trace form Tr(alpha x ybar), alpha = (2 + 2 eta + eta^2)/15, and c' = zeta30", "25"),
    "residue": ("residue plane", "E8/(1 - g)E8 = F25, the tick's 25 fixed momenta, and its six lines", "25"),
    "simplex": ("4-simplex", "the 31 faces of the simplex on the five vertices, its boundaries and the tick on every grade", "17, 23"),
    "air801": ("801 matrix", "AIR_801's [[108, 801], [106, 901]], mod 5 a Singer cycle of order 24", "23"),
    "pg25": ("PG(2,5)", "the projective plane over F5: the conic, 15 exterior and 10 interior points", "23"),
    "assignment": ("root assignment", "Standard-Model quantum numbers on the 240 roots under A4 + A4'", "24"),
    "goldenport": ("Golden port", "the hub's root-site cycle port T_G = F P_cycle on ten roots", "23"),
    "charges": ("five-site charges", "Q = Y + T3 = diag(-1/3, -1/3, -1/3, 1, 0), the removed shell's charges", "12, 23"),
    "memory": ("memory clock", "the 120-state quotient of layer 3's memory operator, of order 90", "3, 27"),
    "words": ("fifteen words", "the dihedral closure of 088, 086 and 980 under rotation and reversal, a D3-module of rank 15", "23"),
    "wedgeport": ("root-wedge port", "the hub's unmarked S5 port T_S x(rho) = <x, v ^ w>/sqrt24 on the 240 roots", "23"),
    "synthemes": ("synthemes", "the 15 perfect matchings of the six Sylow labels, 5 + 10 under the exceptional S5", "23"),
    "darkport": ("dark ports", "the hub's norm-four ports of the dark four: A on the 120 sites of the orbit of (-1, 0, 0, 1, 1, 0, 1, 0), and the triple wedge on 1200 sites", "23"),
    "parent": ("360 parent", "Q[A6] with the right action of r = (01234) and t = (23)(45), and the coset readers O90 and O36", "23, 26"),
    "regular": ("regular clocks", "the thirteen regular classes of W(E8), powers of c', d and v with characteristic polynomials Phi_d^(8/phi(d)) and centralizers of order prod_(d | d_i) d_i", "26"),
    "sun": ("sun's decad", "E8/(1 - s)E8 = F81 = F9^2 for the sun s = c'^10, with the form <x, (s - s^2) y> mod 3; its ten F9-lines pull back to ten 4A2 frames", "26, 27"),
    "principal": ("principal circle", "k -> k rho / 4320 in the momentum torus R^8 / E8, rho the Weyl vector; unique up to W(E8)", "28"),
}

# the levels of the model, from the integers up: (name, what lives there, its dots)
LEVELS = [
    ("number", "the circle and its clocks",
     ["circle", "time", "observer", "c27", "atlas", "coil", "grain", "vortex", "miss", "stages", "memory"]),
    ("symmetry", "groups, their actions and modules",
     ["clocks", "G120", "AGL", "S5", "pgl", "golden", "hodge", "air801", "words", "regular"]),
    ("combinatorics", "graphs, complexes and the cube",
     ["V", "E", "cycles", "rotor", "petersen", "cube", "surface", "simplex", "pg25", "synthemes"]),
    ("lattice", "roots, lattices and tori",
     ["A4", "D5", "E8", "L0", "frame", "momenta", "halfper", "census", "torus", "rootgraph", "cyclo", "residue", "sun",
      "principal"]),
    ("operator", "spaces with operators, ports and moments",
     ["carrier", "kerM", "datum", "source", "literal", "bath", "walks", "moments", "measure", "triangle", "sixsite",
      "pauli", "gksl", "goldenport", "wedgeport", "darkport", "parent"]),
    ("physics", "geometry, readout, waves, binding and the conditional cosmos",
     ["triple", "readout", "waves", "binding", "calibration", "gravity", "cosmology", "charges", "assignment"]),
]
LEVEL_OF = {dot: k for k, (_, _, dots) in enumerate(LEVELS) for dot in dots}

# (from, to, short label, the map, status, check)
JOINS = [
    ("E", "A4", "B", "the signed incidence: its columns are a positive system of A4", T, "k5_roots"),
    ("E", "D5", "B and M", "the two incidences: the twenty positive roots of D5", T, "k5_roots"),
    ("A4", "D5", "inclusion", "A4 is the sub-root-system e_i - e_j of D5", T, "k5_roots"),
    ("D5", "carrier", "Coxeter numbers", "M M^T = h(D5) I - h(A4) P: spec D^2 = {0, h(D5) - h(A4), h(D5)} = {0, 3, 8}", T,
     "k5_roots"),
    ("E", "V", "contraction", "B is contraction with u = (1, 1, 1, 1, 1) on Lambda^2 R^5", T, "exterior"),
    ("E", "kerM", "relations", "ker M is the space of relations among the roots e_i + e_j", T, "k5_roots"),
    ("E", "petersen", "orthogonality", "Petersen is the orthogonality graph of the roots e_i + e_j", T, "petersen_roots"),
    ("petersen", "carrier", "projectors", "the Petersen projectors are the carrier's edge projectors", T,
     "counts.petersen_projectors"),
    ("E", "cycles", "Lambda^2 H", "ker B = Lambda^2 of the sum-zero hyperplane; cuts u ^ H", T, "exterior"),
    ("cycles", "rotor", "area forms", "the C5-fixed plane, spanned by the invariant area forms", T, "exterior"),
    ("rotor", "E8", "Gram 10I", "the rotor pair of near and far roots, turned by a Weyl doubling", T,
     "counts.rotor_plane"),
    ("kerM", "datum", "v0", "the datum's velocity is the alternating 4-cycle in ker M", T, "counts.tick_tock"),
    ("datum", "carrier", "Legendre", "H = 1/2 |v|^2 + 1/2 psi D^2 psi = 34, the zero modes holding 2", T,
     "counts.tick_tock"),
    ("kerM", "source", "q = (a, b)", "the native source lives on ker M + ker M", T, "source_port"),
    ("source", "cycles", "W_AS", "a ^ b -> [A(a), A(b)], an oriented K5 cycle (rank 6, kernel 4)", T, "source_port"),
    ("source", "carrier", "no mode", "4 is not in spec D^2: the source is not a carrier mode", OB, "field"),
    ("source", "sixsite", "port", "the port metric and the boundary rotation of the native action", SR, "native_port"),
    ("A4", "E8", "embedding", "the first five coordinates: A4 and D5 roots are E8 roots", T, "embed"),
    ("D5", "E8", "embedding", "the first five coordinates", T, "embed"),
    ("A4", "L0", "A4 + A4'", "index 5, root cosets 40, 50, 50, 50, 50, glue x -> +-2x", T, "glue_cosets"),
    ("L0", "bath", "folding", "the bath on E8 / L0 = Z/5: 0, 250^4", T, "glue_cosets"),
    ("clocks", "momenta", "fixed points", "the 25 fixed momenta of the tick g", T, "tick_momenta"),
    ("momenta", "bath", "values", "the bath is 0 once and 250 at the other 24", T, "tick_momenta"),
    ("E8", "bath", "Delta", "240 - sum of the 240 root translations; frame 60 I", T, "triangle_port"),
    ("E8", "halfper", "mod 2", "Lambda -> Lambda / 2 Lambda; 120 root classes", T, "counts.folded_bath"),
    ("halfper", "pauli", "phi", "the Walsh-Hadamard conjugate of the folded bath is L in the Pauli basis", T,
     "counts.pauli_quotient"),
    ("pauli", "gksl", "GKSL", "-L(X) = 2 sum (A X A^T - X) over the 120 antisymmetric Paulis", T, "counts.pauli_quotient"),
    ("cycles", "triangle", "odd lift", "the triangle 0-1-2 lifted to its A4 roots", T, "triangle_port"),
    ("triangle", "moments", "Delta^n", "MOMENT_BIT's moments; heat t^-7 / (22394880000000 pi^4)", T, "triangle_port"),
    ("V", "sixsite", "cone", "the origin and the lifted vertices e_i + e_5: K5 coned off", T, "cone"),
    ("sixsite", "moments", "blocks", "241 I - J, 183 I + 52 J, 35366 I + 8134 J", T, "cone"),
    ("V", "clocks", "r", "r acts on the carrier's coordinates as the vertex rotation; g = r r' on A4", T, "clock_joins"),
    ("circle", "clocks", "k 144 -> c'^k", "the Coxeter subgroup <144> onto <c'>, 864 -> g", SR, "clock_joins"),
    ("circle", "time", "idempotent 3456", "the time part of the primary split", T, "primary_split"),
    ("circle", "observer", "idempotent 3105", "the 2-part; the observer clock is its order-4 subgroup", T, "primary_split"),
    ("circle", "c27", "idempotent 2080", "the 27-part, generated by the nakshatra 160", T, "primary_split"),
    ("time", "V", "kappa = 4x mod 5", "translation by 864 intertwined with the vertex rotor", T, "counts.two_clocks"),
    ("clocks", "G120", "c' and d", "the day-Coxeter group, order 120, derived group the tick", T, "clock_joins"),
    ("G120", "circle", "24 maps", "every homomorphism to the circle kills the commutator", T, "counts.circle_maps"),
    ("G120", "AGL", "day clocks", "G / centre on the five day clocks: the tick rotates, the day doubles", T,
     "clock_joins"),
    ("AGL", "carrier", "i -> a i + b", "the twenty affine maps of the vertices commute with D^2", T, "clock_joins"),
    ("circle", "atlas", "x mod 36", "onto Z/36 with kernel the seam <36>; doubling contracts it", T, "atlas"),
    ("golden", "circle", "B^k -> 216 k", "order 20 mod 5, the order of the golden step; 720 mod 4320", SR, "pisano"),
    ("golden", "atlas", "mod 36", "order 24, the tick in atlas steps", T, "pisano"),
    ("stages", "circle", "k -> k", "the fifteen indices as steps, with first landings", T, "counts.check_claims"),
    ("cube", "pauli", "4 - sum X_i", "the four-cube's vertices are four qubits", T, "four_cube"),
    ("carrier", "sixsite", "line graph of K6", "the 15 atoms are the bonds of K6 = K5 coned; D is the spoke-rim block of its line graph", T, "cone_line_graph"),
    ("E", "kerM", "paired response", "with the cyclic orientation [M; B] has rank 9; its kernel, near minus far, is the C5-fixed line of ker M", T, "paired_response"),
    ("E8", "bath", "7-design", "eps = 30|k|^2 - (3/2)|k|^4 + (1/24)|k|^6 + O(|k|^8)", T, "band_expansion"),
    ("bath", "walks", "return counts", "W_n = <delta_0, A^n delta_0> and E_n = <delta_0, Delta^n delta_0>", T, "walks_join"),
    ("walks", "moments", "binomial transform", "E_n, the one-site port's moments, is the binomial transform of W_n", T, "walks_join"),
    ("clocks", "hodge", "Lambda^4", "reflections swap the 35 + 35 halves, the clocks keep them", T, "hodge70"),
    ("coil", "circle", "gcd 8", "the tick, the observer and the nakshatra generate the 540 multiples of 8, index 8; the smear step 184 = 23 x 8 generates the same subgroup", T, "coil"),
    ("coil", "time", "x -> x mod 5", "onto the time coordinate with kernel the pada subgroup <40>: the tick misses its 108 points and meets the other 432", T, "coil"),
    ("c27", "atlas", "160 k -> 16 k mod 36", "the nakshatra walk: period 9, each stable address three times; the 27-coordinate is 25 k mod 27", T, "nakshatra_map"),
    ("atlas", "time", "Z/180 = Z/36 x Z/5", "36 = 1 mod 5: x = a + 36((t - a) mod 5), so every address carries all five time coordinates and the tick bit (t != 0) does not see the address", T, "address_lift"),
    ("golden", "time", "k -> 216 k mod 5", "the k-th golden point misses the tick iff 5 | k iff 5 | F_k; no trace L_n of a golden power is a multiple of 5", T, "golden_family"),
    ("S5", "carrier", "vertex permutations", "S5 acts on the 15 atoms and commutes with D; in S6 these are exactly the 120 permutations of K6 that keep D, and atoms and bonds are one S5-set", T, "cone_symmetry"),
    ("AGL", "S5", "F20 inside S5", "AGL(1,5) = F20, the twenty affine maps of the vertices, is where the cone S5 and PGL(2,5) meet in S6", T, "cone_symmetry"),
    ("AGL", "pgl", "x -> a x + b", "the stabilizer of infinity in PGL(2,5), and its only elements that keep D", T, "cone_symmetry"),
    ("pgl", "carrier", "not the carrier's S5", "on the 15 bonds PGL(2,5) has one orbit and involution character 3, the carrier's S5 two orbits and transposition character 7: equal on F20 and C5, not as S5-modules", OB, "cone_symmetry"),
    ("AGL", "sixsite", "the cone's rotation", "the 5-cycle with the cone point fixed, traces 1, 1, 1, 1, 6; a 6 x 6 block of order 5 with traces 1 (MPKG) is similar to it over Q", T, "mpkg_block"),
    ("grain", "coil", "index 9", "the multiples of 72 are the golden orbit <216> times the sun <1440>, a direct product of 60 points of index 9 in the coil; doubling doubles the golden index and inverts the sun", T, "grain"),
    ("grain", "c27", "j -> 9 j", "the 27-clock reads only the sun coordinate of a grain point, and time and the 2-clock read only its golden index", T, "grain"),
    ("atlas", "vortex", "x mod 9", "9 | 36, so the vortex coordinate is read off the address; doubling runs through its six units 2, 4, 8, 7, 5, 1", T, "vortex"),
    ("c27", "vortex", "kernel the sun", "Z/27 -> Z/9 has kernel 0, 9, 18, the sun's 27-coordinates: the vortex is the 27-clock without the sun", T, "vortex"),
    ("miss", "circle", "Z/4320 = <864> + <5>", "every point is a tick part plus a miss, uniquely; it misses exactly when its tick part is 0, and 864 copies of it give the pure tick with the opposite coordinate", T, "tick_miss"),
    ("observer", "miss", "inclusion", "the observer clock and the whole nakshatra clock lie in the miss set; in each golden loop the four misses are one observer coset", T, "tick_miss"),
    ("c27", "coil", "onto the golden cosets", "the nakshatra clock meets each of the coil's 27 golden cosets once, and doubling acts on both with cycles 18 + 6 + 2 + 1, the sun's swap among them", T, "doubling_orbits"),
    ("E8", "frame", "a maximal clique", "eight roots with pairwise inner product 1 and the origin: Gram I + J, index 3, no ninth root", T, "eight_roots"),
    ("frame", "sixsite", "six-point faces", "every six-point face of the frame is a six-port, with coupling Gram 183I + 52J", T, "eight_roots"),
    ("golden", "clocks", "B^k -> v^k", "B mod 5 and the golden clock v of W(E8) are both cyclic of order 20, and B^4 goes to v^4, the tick g", SR, "golden_clock"),
    ("cube", "E", "the cuts mod 2", "x -> the cut of {i : x_i = 1}: the sixteen vertices of the four-cube are the sixteen cuts of K5 over F2, a cube edge adds one vertex star, and the antipode is the fifth star", T, "cube_cuts"),
    ("E", "surface", "K5 inside K6", "the surface's 1-skeleton is K6, the ten K5 edges and five spokes, and D is the spoke-rim block of its line graph (J5)", T, "surface"),
    ("surface", "pgl", "PSL(2,5)", "on the projective line over F5 the hemi-icosahedron and its complement are the two PSL(2,5)-orbits of triangles; PGL(2,5) swaps them, and their links at infinity are the pentagram and the pentagon", T, "surface"),
    ("E8", "momenta", "the dual torus", "E8 is unimodular, so momenta live on R^8 / 2 pi E8, where the tick has |det(g - I)| = 25 fixed points", T, "dual_torus"),
    ("E8", "census", "the band on the alcove", "eps = 240 - sum cos(2 pi r.x) has 11 critical families on the alcove, 243600 points with Morse sum 0", T, "census"),
    ("momenta", "census", "fixed points are critical", "the tick's 25 fixed momenta are critical points of the band: the minimum and 24 points of the A4 + A4 family (eps 250, index 4)", T, "critical_momenta"),
    ("census", "torus", "nine frequencies", "the nine positive critical energies have distinct square-free parts, so their square roots are independent over Q and the flow is dense on T^9", T, "nine_torus"),
    ("census", "walks", "characteristic roots", "the 11 critical values are the in-band characteristic roots of the order-16 recurrence of W_n", T, "census_walks"),
    ("bath", "pauli", "periodic restriction", "on the 2-Lambda-periodic functions the bath, conjugated by Walsh-Hadamard, is the Pauli generator L", T, "counts.pauli_quotient"),
    ("literal", "source", "U", "the owner's operands give the same port up to U, a W_p-isometry commuting with the C5 rotation; their W_p is the reconstruction's exactly", T, "literal_port"),
    ("moments", "measure", "Hausdorff", "the true sector moments M_0..M_50 pass the Hausdorff test on [0, 256]: they are moments of measures, each with 25 Gauss nodes in the band", T, "measure"),
    ("carrier", "triple", "D", "the triple's Dirac operator is odd, with D^2 = M M^T + M^T M and moments 15, 40, 200, 1240, 8840", T, "triple"),
    ("kerM", "triple", "index", "ker D^2 lies on the edges and equals ker M; the Witten index is Tr(gamma on ker D^2) = -5 (J7)", T, "triple"),
    ("source", "readout", "hidden sector", "the hidden controllable sector of (edge force, D psi) is ker M + ker M, the native source's space (J6)", T, "readout"),
    ("carrier", "waves", "Hodge block", "on the cycle space, in the fundamental-cycle basis, Curl is -A, the carrier's Hodge block (6I - G) sigma", T, "sound_light"),
    ("E", "waves", "d0 = B^T", "the edge complex has d0 = B^T and d1 d0 = 0, ranks 4 + 6: sound is the cuts and light the cycles", T, "sound_light"),
    ("cycles", "waves", "helicities", "light = ker d0^T is the cycle space, split by Curl = *d1 into the helicities +-sqrt5, three each", T, "sound_light"),
    ("A4", "waves", "the sound Hessian", "the sound operator B B^T = 5I - J is half the A4 frame sum alpha alpha^T", T, "sound_light"),
    ("source", "binding", "Lambda^2 ker D", "the port lives on Lambda^2 ker D (10); with the five zero modes at the other chirality it makes the anomaly-free 5 + 10", T, "binding_joins"),
    ("triple", "readout", "first-order form", "the readout's generator A = [[0, I], [-D^2, 0]] is the triple's D^2 in first-order form: A^2 = -(D^2 + D^2)", T, "readout"),
    ("triple", "binding", "commutant", "the commutant of D is M5 + M4 + M4 + C + C (dimension 59), and its only atom-diagonal element is the phase", T, "binding_joins"),
    ("triple", "waves", "complement", "on the vertices the triple's D^2 and the sound operator add to 8: M M^T + B B^T = 8I", T, "sound_light"),
    ("readout", "calibration", "Salina-Prema", "a calibration t = tau u intertwines the native flow with the physical one: S U(u) = U_tau(tau u) S", T, "calibration"),
    ("circle", "calibration", "no internal clock", "calibrations tau and 2 tau give identical native records, so no internal number, the circle's ticks included, binds physical time", OB, "calibration"),
    ("triple", "gravity", "heat coefficients", "Tr D^0, D^2, D^4 = 15, 40, 200 give the M4 x F heat coefficients 60, -(160 m^2 + 5R), 400 m^4 + 40 m^2 R/3; G and Lambda_cc need f, L and m (J10)", gates.CONDITIONAL, "product_geometry"),
    ("gravity", "cosmology", "G and Lambda_cc", "the spectral action's G and Lambda_cc drive a flat FLRW flow; the Friedmann constraint holds, and the kernel sector, the datum's 2, scales exactly as a^-6", gates.CONDITIONAL, "friedmann"),
    ("E8", "rootgraph", "inner product 1", "the 240 roots with an edge at inner product 1: classes 1, 56, 126, 56, 1 around each root, an association scheme with eigenvalues 56, 28, 8, -2, -4", T, "root_scheme"),
    ("rootgraph", "walks", "pair sums", "W_3 = tr A^2 = 240 x 56, and W_4 = 1260720 is the sum of the squared pair-sum multiplicities (Canon K)", T, "root_scheme"),
    ("rootgraph", "frame", "eigenvalue 28", "the roots' Gram is 60 times the projector onto the eigenvalue-28 space, the coordinate space that the eight frame roots span", T, "root_scheme"),
    ("E", "simplex", "grade 2", "the ten edges are grade 2 of the 4-simplex; its boundaries have ranks 4, 6, 4, 1, the triangles fill the cycles, and the only homology is the point", T, "simplex_grades"),
    ("time", "simplex", "the tick on every grade", "the vertex rotation acts on every grade by copies of the five-clock's regular representation: (x - 1) Phi_5, then (x - 1)^2 Phi_5^2 twice, (x - 1) Phi_5 and x - 1", T, "simplex_grades"),
    ("golden", "E", "B -> -(T + T^-1)", "on the eight golden edge directions -(T + T^-1) satisfies the golden equation X^2 = X + I, so the golden companion acts there; Phi_5 splits over the golden field", T, "golden_split"),
    ("air801", "pgl", "the projective class", "mod 5 the matrix is [[3, 1], [1, 1]] of determinant 2, a non-square: in PGL(2,5) it lies outside PSL(2,5), has order 6 and turns the projective line in one 6-cycle, swapping the hemi-icosahedron and its complement", T, "air_801_joins"),
    ("surface", "pg25", "the Veronese conic", "v -> v^2 puts the six axes on the conic of PG(2,5); the 15 edges are the 15 exterior points, where two tangents meet, and the 10 faces of either triangulation are the 10 interior points, a face and its complementary face sharing their perspector", T, "projective_plane"),
    ("pgl", "pg25", "the symmetric square", "PGL(2,5) acts on the plane through the symmetric square, keeps the conic and is transitive on the conic, the exterior and the interior points", T, "projective_plane"),
    ("air801", "pg25", "orbits 1 + 3 + 3 + 6 + 6 + 6 + 6", "the matrix's symmetric square keeps the conic and splits the 31 points as conic 6, exterior 3 + 6 + 6 and interior 1 + 3 + 6", T, "air_801_joins"),
    ("census", "gksl", "the decay rates", "the 256 half-periods are the census's critical points of types E8 (1), E7 + A1 (120) and D8 (135), so e^-tL decays the Paulis at 0, 224 and 256", T, "gksl_census"),
    ("stages", "time", "first landings", "each stage prime to 5 lands first on a nonzero tick level, 864, 1728 or 2592; the stages 0, 5 and 10 never land", T, "stage_landings"),
    ("E8", "hodge", "Lambda^4 of the lattice", "Lambda^4 of the lattice's space is 70-dimensional, and the Hodge star splits it into halves of 35", T, "hodge70"),
    ("torus", "calibration", "the speed of the flow", "a calibration divides the nine frequencies together, so the flow's orbit on T^9 is the same for every calibration; no two frequencies have a rational ratio, so no calibration makes it periodic", T, "torus_calibration"),
    ("literal", "E", "the incidences", "the owner's file lists the edges in the carrier's order, and its H_signless and boundary_oriented are the carrier's M and B", T, "literal_incidences"),
    ("measure", "census", "the band", "the spectral measures live on [0, 256], from the census's minimum (type E8) to its maximum (type D8), with every Gauss node inside", T, "measure_band"),
    ("waves", "calibration", "invariant ratios", "a calibration divides every native frequency by tau, and light/sound = 1, port/source = 2, band top/source = 8 and carrier^2 + sound^2 = 8 stay as they are", T, "wave_calibration"),
    ("datum", "cosmology", "the stiff sector", "with the checked datum as initial value, the FLRW kernel sector holds the datum's 2 and scales exactly as a^-6", gates.CONDITIONAL, "friedmann"),
    ("momenta", "golden", "the Hessian", "at the tick's 24 fixed momenta of type A4 + A4, X = -(1/5) sum r r^T cos(2 pi r.x) satisfies X^2 = X + I: the band's Hessian there is -5 times a golden companion, det 5^8 (ENERGY_250)", T, "census_stabilizers"),
    ("sixsite", "golden", "twice the pentagon Laplacian", "the port metric is [2/5] + 4I + (2/5)J - 2(R + R^-1) (PORT_FORMULA); on the contrast X = -(R + R^-1) satisfies X^2 = X + I and the block is 4I + 2X, with golden eigenvalues 5 -+ sqrt5 of product 20, the golden step's order (GOLDEN_PORT)", T, "golden_port"),
    ("source", "readout", "the joint observer", "the wedge readout a ^ b of the source pair has rank 7, its fibre the SL(2) frame; with the probes a1, a2, b1 it is injective on a1 w12 != 0, with an explicit inverse (the hub's observer completion)", T, "observer_completion"),
    ("atlas", "circle", "the sideband lift", "the address and the residues mod 32, 27 and 5 (checksums mod 4 and 9) rebuild the tick, j = A + 36 t with t = 105 t8 + 40 t3 + 96 t5 mod 120; three sensors of largest alphabet 32 are optimal, one must read j itself", T, "clock_sidebands"),
    ("V", "charges", "a charge on the sites", "Q, Y and T3 are functions on the five sites; Q is kept by 3! = 6 permutations and Y by 12, and the 5-cycle keeps neither (TRIPLET)", T, "charges"),
    ("simplex", "charges", "q(S) on the faces", "on the even faces and on the odd ones sum q^2 = 16/3 = 2^(5-3) sum Q^2 (CHARGE_SHELL); the 16 even faces carry one generation's charges", T, "charges"),
    ("charges", "binding", "the anomaly", "the cubic charge sums over 5 and Lambda^2 5 are equal (5/36 for Y), so on B4's 5 + 10 at opposite chiralities the hypercharge anomaly cancels; on the zero modes alone it is 5/36", T, "charges"),
    ("charges", "kerM", "the dark U(5)", "through an identification of the five zero modes with the sites, Y acts on ker D inside B2's exact dark U(5) and commutes with D", SR, "charges"),
    ("charges", "carrier", "B1", "on the atoms no charge but the global phase commutes with D: the diagonal commutant of D has dimension 1", OB, "charges"),
    ("time", "halfper", "the tick on Lambda / 2 Lambda", "the time clock acts on the half-periods through the tick g = r r' (864 -> r by kappa): it fixes only the zero half-period and turns the other 255 in 51 five-cycles, 24 of type E7 + A1 and 27 of type D8, keeping the band", T, "tick_halfperiods"),
    ("time", "gksl", "a tick-equivariant semigroup", "L is diagonal on the 256 Pauli labels with the band values, constant on each tick orbit, so e^-tL commutes with the tick's permutation of the Paulis", T, "tick_halfperiods"),
    ("time", "waves", "the tick on sound and light", "the edge tick commutes with d0 and Curl; on each helicity it fixes one line and turns a golden plane, by 144 degrees on +sqrt5 and 72 on -sqrt5, with traces 1 - phi and phi", T, "light_symmetries"),
    ("golden", "waves", "B -> (I + Curl)/2", "Curl^2 = 5 on light, so X = (I + Curl)/2 satisfies X^2 = X + I there: the golden companion acts on light, as phi on helicity +sqrt5 and 1 - phi on -sqrt5", T, "light_symmetries"),
    ("AGL", "waves", "the helicity character", "x -> a x + b multiplies Curl by the Legendre symbol (a/5): the rotations and the reflection keep the helicities, the doubling exchanges them", T, "light_symmetries"),
    ("pgl", "S5", "the outer automorphism of S6", "S6 acting on its six synthematic totals is an outer automorphism, and it carries the cone's S5 onto a transitive S5 conjugate to PGL(2,5)", T, "outer_s6"),
    ("S5", "A4", "W(A4)", "the reflections in the roots e_i - e_j are the transpositions, and they generate the 120 vertex permutations: S5 = W(A4)", T, "s5_weyl"),
    ("S5", "binding", "the Weyl group of 5 + 10", "each reflection moves the weights e_i of the 5 and e_i + e_j of Lambda^2 5 as it moves the carrier's atoms, commuting with D (B5)", T, "s5_weyl"),
    ("air801", "surface", "the two triangulations", "x -> (3x + 1)/(x + 1) turns the six axes in one 6-cycle and maps the hemi-icosahedron's ten faces onto its complement's, and back", T, "air801_surface"),
    ("time", "cube", "a fifth root of unity in F16", "the vertex rotation moves the cuts mod 2 linearly, with Phi_5 irreducible over F2: the tick is a primitive fifth root of unity on F16, fixing the origin and turning the other fifteen vertices in three 5-cycles", T, "tick_cuts_f2"),
    ("grain", "time", "the golden index", "x -> 3456 x maps the grain onto the time clock with kernel <360>: it reads the golden index of x = 216 a + 1440 b", T, "small_joins"),
    ("miss", "time", "the kernel", "the miss set <5> is the kernel of the time coordinate x -> 3456 x", T, "small_joins"),
    ("stages", "miss", "the stages that never land", "the stages 0, 5 and 10, which never land, are exactly the stages in the miss set", T, "small_joins"),
    ("circle", "vortex", "x mod 9", "x -> x mod 9 maps the circle onto the vortex with kernel <9>, through the atlas and through the 27-clock", T, "small_joins"),
    ("rotor", "AGL", "a quarter turn", "the doubling i -> 2i turns the rotor plane by a quarter: pentagon to pentagram, pentagram to minus the pentagon", T, "small_joins"),
    ("triangle", "simplex", "a 2-face", "the triangle port's oriented triangle 0-1-2 is the boundary of the simplex's face 012", T, "small_joins"),
    ("hodge", "halfper", "the deck involution", "e_S = e_T mod 2 Lambda for four-sets S, T exactly when T = S or its complement: the Hodge star is the deck involution of S -> [e_S], onto 35 half-periods of type D8", T, "hodge_halfper"),
    ("halfper", "census", "three critical types", "the 256 half-periods are critical points of the band, of types E8 (1), E7 + A1 (120) and D8 (135), whole census orbits", T, "gksl_census"),
    ("L0", "momenta", "the characters of E8 / L0", "the tick momenta that are integral on A4 + A4' are the five characters of E8 / L0, with the folded values 0, 250^4", T, "tick_momenta"),
    ("literal", "sixsite", "W_p", "the owner's port metric in boundary order is the six-site port's W_p exactly", T, "literal_port"),
    ("measure", "sixsite", "the sector measures", "the measures are the six-port's contrast and uniform sector measures, with first moments 241 and 235, the six-site blocks' eigenvalues", T, "measure"),
    ("petersen", "D5", "orthogonality", "the Petersen graph is the orthogonality graph of the ten positive roots e_i + e_j of D5", T, "petersen_roots"),
    ("observer", "coil", "inclusion", "the observer clock <1080> lies in the coil <8> (1080 = 8 x 135), and with the tick and the nakshatra generates it", T, "coil"),
    ("torus", "bath", "the nine frequencies", "the torus's nine squared frequencies are the bath symbol's nine positive critical values, with distinct square-free parts", T, "nine_torus"),
    ("circle", "memory", "one step, one step", "k -> A^k is a homomorphism onto the memory clock's order-90 quotient (90 divides 4320), with kernel <90>: one circle step is one memory step, a selection", SR, "memory_clock"),
    ("memory", "vortex", "the 9-cycle", "on the memory clock's 9-cycle A^k moves by k mod 9, so its composite with the circle is the vortex x mod 9", SR, "memory_clock"),
    ("memory", "time", "the 10-cycles", "on each 10-cycle A^k moves by k mod 10, which carries the time coordinate k mod 5", SR, "memory_clock"),
    ("L0", "assignment", "the branching", "the 240 roots are (24,1) + (1,24) + (10,5) + (5b,10) + (10b,5b) + (5,10b): (10,5) is the carrier's ten duads times the twin's five sites, (5b,10) its five sites times the twin's ten duads, each pair once", T, "assignment.factors"),
    ("E8", "assignment", "the second moment", "10 I on A4 + A4', 15 P + 10 P' and 10 P + 15 P' on the mixed classes, 60 I in all: the band starts 30 |k|^2, and sum (T3.rho)^2 : sum (Q.rho)^2 = 3 : 8", T, "assignment.moments"),
    ("charges", "assignment", "charges on the roots", "Q = Y + T3 on the carrier factor gives every root its Standard-Model charge, and Q minus each colour coordinate is an integer on all 240 roots (the Z6); only the 20 family roots carry no Standard-Model charge", T, "assignment.standard_model"),
    ("E", "assignment", "the 10 of matter", "the carrier's ten duads are the weights of the 10 in (10,5): u^c on the colour duads, the quark doublet on the colour-weak ones, e^c on the weak duad 34", T, "assignment.standard_model"),
    ("AGL", "assignment", "the doubling on E8 / L0", "J (site_a -> mu_a, mu_a -> -site_a) lies in W(E8), J^2 = -1, and it cycles the four mixed classes, multiplying the grade in Z/5 by 2; the normalizer of A4 + A4' acts on them through the units of Z/5", T, "assignment.choices"),
    ("S5", "assignment", "one orbit of choices", "the ten colour triples are one orbit of S5 = W(A4), which keeps every twin weight; with J and -1 the factor, the orientation and the colour triple are all W(E8)-equivalent", T, "assignment.choices"),
    ("sixsite", "assignment", "the port's twin duad", "the six-site port's roots e_a + e_5 are the 5 at -(mu_3 + mu_4), the twin duad disjoint from the generation triangle, and the brackets of its 10's with its 5b's; its memory variance 183 I + 52 J counts bath neighbours", T, "assignment.six_site_port"),
    ("binding", "assignment", "three generations", "with the orientation and the bracket rule (the 5b's are the brackets of the 10's), anomaly freedom |S| = C(|S|, 2) forces a triangle of K5': 45 roots, three generations, every anomaly zero; B6 sharpened, not discharged", gates.CONDITIONAL, "assignment.generations"),
    ("rootgraph", "bath", "the bath between roots", "Delta^4 = (240 - A)^4 between two roots depends only on their inner product (3389062320, -40411056, 3317832, 222708, 228256 at 2 to -2), as do the walks of length 0 to 4; two roots fill 9361 points in five shells, 240, 56, 14, 2 and 1 deep (SHELLS, MEMORY, FOURTH)", T, "walks_by_angle"),
    ("walks", "sixsite", "the walks are the port", "the six-port's couplings 241, 183, 235 and 495 are walk moments; its leakage stays positive at the second step (55487966/183, 131183830/99), and its sector measures have positive Hankel determinants through size 11 (LEAK, RANK)", T, "port_leak"),
    ("clocks", "halfper", "two order-5 actions", "the coordinate five-cycle alone fixes 16 half-periods (1 + 10 + 5) and makes 48 band-keeping five-cycles; the tick g = r r' fixes only the origin (TICK, COXETER)", T, "two_ticks"),
    ("simplex", "cycles", "the cycles bound", "the filled 4-simplex has boundary ranks 4, 6, 4, 1 and interior Laplacians 5I, so the six cycles of K5 bound triangles; K = I + 2(T + T^-1) squares to 5 on the moving edges (HELICITY)", T, "filled_simplex"),
    ("charges", "E", "the charge on the edges", "the minimum-norm lift B^T Q / 5 of the charge has square 4/15 and lies in the cuts with zero cycle part; Y is 5/6 of the weak duad's 10-weight (MARKS, CHARGE_WEIGHT)", T, "charge_marks"),
    ("cycles", "goldenport", "the root-site isometry", "F sends the near edges to the roots e_i - e_(i+1) and the far edges to the glue roots site_i - (mu_i + mu_(i+1)), a signed isometry onto ten distinct roots, so T_G = F P_cycle has T_G* T_G = P_cycle (the hub's OES_Unified_Model)", T, "golden_root_port"),
    ("goldenport", "bath", "the Golden moments", "traces 1442, 347900, 84180666, 20416532280; means 239, 241, 481/2 -+ sqrt5/10; variances 371, 171, (1987 -+ 31 sqrt5)/10, MEMORY's stated block", T, "golden_root_port"),
    ("goldenport", "sixsite", "two windows on one bath", "with the hub's clique (six roots, differences roots) the Golden port shares two sites; the cross map has squared singular values 4/5 and 2/5, the joint span is 12 and the joint Krylov ranks are 12, 24, 36; the clique's 4 x 4 Hankels are positive", T, "shared_bath"),
    ("charges", "goldenport", "the marked charge map", "a fivefold order sends site i to its outgoing edge: L = P_cycle N P_A4 has rank 4 and L L^T = ((5I + K)/10) P_moving; a near and a far mark (squares 34/45 and 26/45) decode the two Golden densities with determinant 32 sqrt5/675, both nonnegative exactly in the window (49 -+ 12 sqrt5)/41 (the hub, 11:18)", T, "marked_charge"),
    ("S5", "cycles", "the twelve markings", "the ten transpositions sum to 0 on the cycles, so the S5-averaged marked map is 0 while its square averages to P_cycle/3; the 120 relabellings give 12 marked squares, ten times each, summing to 4 P_cycle, and only all twelve together are isotropic (the sibling's MODEL, 11:19)", T, "twelve_markings"),
    ("goldenport", "moments", "the infrared channels", "from the ten root sites, in units of 1/(1536 pi^4 30^4): plus 10 E^3 (1 - E^2/1080000), Golden (E^4/240)(1 + (1/100 -+ sqrt5/3000) E), minus E^5/36000; the near/far ratio (17/13)(1 - 2E/5525), the marked ensemble (E^4/360)(1 + 29E/3000) and the twirl (10/9) E^3 + E^4/540 + E^5/48600", T, "golden_infrared"),
    ("words", "surface", "the twisted duads", "the fifteen words are the oriented edges of K6 under c: i -> i + 2 and r: i -> -i with the reflection's sign twisted, isometrically over Q(sqrt2) (O = A + B/sqrt2) and over no smaller field (fixed Gram determinants 108 and 54), integrally with index 8 (T_Z = A + B, Smith 1^12 2^3) and never unimodularly (mod-2 coinvariants 3 and 4); the untwisted duads differ (reflection trace 3)", T, "word_duads"),
    ("words", "A4", "the Coxeter five-cycle", "D3 on J7 = 1 + 3 std has commutant Q + M3(Q) and no rational C5; the least extension with one is 9 = 1 + 4 std, where U9 = 1 + I2 x companion(Phi_5), and the companion is A4's Coxeter element on its simple roots", T, "words_c5"),
    ("words", "golden", "the extension's golden equation", "on the extension's eight moving directions -(U9 + U9^-1) satisfies X^2 = X + I, so the golden companion acts there as it does on the edges", T, "words_c5"),
    ("S5", "waves", "the parity contexts", "the six even and six odd contexts sum to 2 P_cycle -+ (2/sqrt5) J_H with J_H = Curl/sqrt5, so their difference is (4/5) Curl; every permutation acts on Curl through its sign, and S_even S_odd = (16/5) P_cycle (the hub, 11:58)", T, "hodge_contexts"),
    ("waves", "goldenport", "the Hodge defect", "Curl/sqrt5 commutes with the Golden port's response except on the fixed plane: ||[J_H, G]||^2 = (8/5)(g_+ - g_-)^2, 32/5 for the means and 64000 for the variances; four labelled context responses (determinant -64 sqrt5/625) recover the four channels and the defect, and from the computed densities R_C/R_D -> 2/3 and R_even/R_odd -> 3/2", T, "context_responses"),
    ("waves", "sixsite", "the Hodge-isotropic overlap", "the clique sees a 2-plane of the Golden port with C J_H C* = 0, so no orthogonal clique action extends the Hodge star (||AC - C J_H||^2 = 12/5 for every A), while the mixed involution K(x, y) = (x, J_H y + (J_H - I) C* x) keeps the joint Gram (det 3/25, condition 9 + 4 sqrt5); the residual clique S = I - CC* has S^-1 = I + 4 P_8 + (2/3) P_4", T, "overlap_hodge"),
    ("waves", "bath", "the Hodge repair", "two copies of the bath realize the Hodge-averaged response (G + J_H G J_H)/2 at every s; averaging after inversion is smaller by the factor (a - b)^2/(a^2 + 3ab + b^2); the memory pays M_odd^2 = (4/5) P_fix, the fixed means become 240 +- 1/sqrt5, and both Hodge lines start at E^3", T, "hodge_averaging"),
    ("words", "S5", "the six Sylow views", "c = (012) and r = (01)(34) act on the six Sylow five-cycle groups as i -> i + 2 and i -> -i on six points, so the words' twisted duads are duads of the Sylow views; as D3-modules the words are 3 + 2 sign + 5 std, the native V5 + E10 5 + 2 sign + 4 std and the cycles 2 sign + 2 std, so equivariant maps have rank at most 13 (attained), 5 and 4", T, "word_sylow"),
    ("words", "carrier", "no native Golden action", "D^2's eigenspaces 0, 3 and 8 carry D3 multiplicities (1, 0, 2), (2, 2, 2) and (2, 0, 0), all at most 2, so no rational operator of order five other than I commutes with both D^2 and the word D3", OB, "word_sylow"),
    ("circle", "E8", "the root address", "f(j) = R_diag^(2 floor(j/48)) r_(j mod 48) sends the 4320 frames onto the 240 roots, 18 each, through j mod 240, with f(j + 864) = R_diag f(j): the tick acts on addresses as the diagonal five-cycle; a chosen encoder, whose unit step is not an isometry (the hub, 11:58)", SR, "clock_root_address"),
    ("time", "L0", "the phase is not a glue class", "no permutation of the 240 roots advances every glue class by 1 (class 0 has 40 roots, the others 50), so the tick's phase 4j mod 5 is not the glue grade; R_diag keeps every class", OB, "clock_root_address"),
    ("AGL", "L0", "the carrier's doubling", "the doubling i -> 2i of AGL(1,5) on the carrier's sites, the twin fixed, permutes the 240 roots in 40 fixed, 10 two-cycles and 45 four-cycles; the 20 fixed beyond the twin copy are not a root system; every mixed root meets the two copies in the patterns (6, 8, 6) and (4, 12, 4) (the hub, 12:04)", T, "coordinate_bridge"),
    ("S5", "datum", "a regular orbit", "the 120 vertex permutations carry (psi0, v0) to 120 distinct data, all of energy 34: the datum's stabilizer in S5 is trivial, so its orbit labels S5, and the reflection 0 <-> 3, 1 <-> 2 that keeps the velocity's 4-cycle moves psi0", T, "datum_orbit"),
    ("charges", "cycles", "the charge map", "Q sends an oriented edge a -> a + d to q(a + 2d) - q(a + 4d): Q^T Q = 5 P_A4 onto the four moving cycles, the witness loop, commuting with the tick and the doubling; it is the only AGL(1,5)-map up to scale, no S5-map exists, and L = (U^2 - U^4) Q/5 (the sibling's MODEL, 12:24)", T, "witness_loop"),
    ("kerM", "cycles", "the midpoint", "the midpoint map (edge ab to the vertex 3(a + b)) takes ker M onto the trace-free sites with Gram (5/3) P_A4, killing only the near-minus-far line (square 10, fixed by the tick, negated by the doubling), and Q after it carries the other four zero modes onto the witness loop, whose seed (-3, 1, 2, 0, -1, 0, -2, 1, -1, 3) has rotates of strengths 25 phi^2 and 25 phi^-2", T, "witness_loop"),
    ("AGL", "circle", "the affine group on the frames", "j -> j + 864 (order 5) and j -> 3457 j (order 4, conjugating the tick to its square) generate AGL(1,5) on the 4320 frames, keeping the address j mod 36 and acting on the phase 4j mod 5 as x -> x + 1 and x -> 2x; every frame is 3105 (j mod 32) + 2080 (j mod 27) + 864 (4j mod 5) (the sibling's MODEL, 12:24)", T, "frame_affine"),
    ("time", "rootgraph", "free pentagons", "the time clock acts on the root graph through the tick g = r r', with no fixed root: the 240 roots fall in 48 five-cycles, each an extended A4 diagram (five roots summing to zero, products -1 around a pentagon, spanning an A4 root lattice), 24 in the order of g and 24 in the order of g^2, and each copy of A4 + A4' is 4 of them", T, "tick_actions"),
    ("time", "kerM", "one zero mode per character", "through kappa the time clock acts on the five zero modes with characteristic polynomial (x - 1) Phi_5, the regular representation: one zero mode for each character, the invariant one the near-minus-far line", T, "tick_actions"),
    ("time", "triple", "an automorphism of the triple", "the tick commutes with D and gamma and permutes the 15 atoms freely, so the time clock acts on the triple by automorphisms; each of its five characters has rank 3, with D^2 = 0, 8, 8 on the invariant one and 0, 3, 3 on each other (tr(P_lambda U^j) = 0, -2, 2 on the eigenvalues 0, 3, 8)", T, "tick_actions"),
    ("source", "waves", "the Agni-Soma light", "the source pair's commutator F_AS(a, b) = upper([A(a), A(b)]) is a circulation: rank 6 on Lambda^2 ker M, onto light, with kernel Lambda^3 A4 = std x sign; up to scale it is the only S5-map (F20 alone allows 4), the SO(2) rotating the two copies keeps it, and at the hub's witness ||F||^2 = 1392 and F^T J_H F = 96 sqrt5 (the hub, 12:29)", T, "agni_soma"),
    ("source", "charges", "the F20 factorization", "the whole commutator is F_AS(a, b) = L_out(Ra ^ Rb) - (2/5) C K_vertex [alpha(a) Rb - alpha(b) Ra]: the midpoint R carries the source pair to the trace-free sites, the charge map C carries them to the cycles, alpha(a) = <h, a>/10 reads the near-minus-far line, and L_out = [-P_fix + 3D P_fix + 2 P_moving]/5 is invertible but not orthogonal (the hub, 12:29)", T, "agni_factor"),
    ("source", "goldenport", "the E8 pullback", "through the Golden root-site port the witness's commutator has channel weights 288/5, 32/5 and 664 -+ (304/5) sqrt5, moments 1392, 334632 and 80732784, and memory variance form 1441112/5, above 171 x 1392 (the hub, 12:29)", T, "agni_pullback"),
    ("source", "readout", "the phase quadratures", "the ten native readings (six commutator coordinates, four quadratic contrasts) miss the SO(2) phase (rank 9); the phasor Z1 = Tr[(A + iB)(A^2 + B^2)]/6 turns as e^-i theta and reads the phase back on each orbit, and six coordinates, two contrasts and Re Z1, Im Z1 are ten readings with nonzero Jacobian at the witness (the hub, 12:29)", T, "source_phase"),
    ("pgl", "kerM", "the six Sylow sign lines", "each Sylow group's pentagon minus its pentagram is a zero mode of square 10; oriented, the six have products -2, sum to zero and frame ker M with factor 12, and S5 permutes them with signs through PGL(2,5), so ker M is the sign twist of PGL(2,5)'s 5; the triples' cubic traces are 16 and -16, ten each (the sibling's MODEL, 12:59)", T, "sylow_lines"),
    ("halfper", "bath", "the band edge", "sum_r cos(r.k) >= -16, so the bath's spectrum is exactly [0, 256]: Lambda = 4 e2(cos k) + 128 (prod cos(k_i/2) + prod sin(k_i/2)), a minimizer of the worst-sign bound takes at most three values (one cubic), and five 3-parameter families are certified by interval arithmetic; 256 is attained exactly at the 135 half-periods of type D8", T, "band.edge"),
    ("L0", "wedgeport", "the root wedge", "every root is (v, w) in A4 + A4' (site and twin coordinates, an isometry), and b_rho = v ^ w is a circulation, nonzero on the 200 mixed roots, with sum b b^T = 24 P_cycle: T_S x(rho) = <x, b_rho>/sqrt24 is an isometry of the cycles into the roots (the hub, 14:07)", T, "wedge_port"),
    ("cycles", "wedgeport", "an S5-isometry", "the diagonal S5 permutes the roots and T_S intertwines it with the signed edge action, with A T_S = 8 T_S on the root graph; its infrared is a uniform quadrupole, -sqrt6 <x, p ^ q>, so rho_S ~ C E^5/6000 and K_S ~ C t^-6/50 for every unit x", T, "wedge_port"),
    ("wedgeport", "bath", "scalar moments", "T_S* Delta^n T_S = m_n P_cycle with m = 1, 232, 54213, 12740592, 3008062816: variance 389, Hankel determinant 219823907, next Jacobi coefficient 219823907/151321; the two-block model misses m4 by 219823907/389", T, "wedge_port"),
    ("S5", "wedgeport", "no Lorentz form", "the cycles are real irreducible under S5, so every S5-invariant symmetric form on the port is Euclidean up to scale: a timelike line needs a smaller symmetry or another operator", OB, "wedge_port"),
    ("wedgeport", "goldenport", "three windows", "the root-wedge port meets the Golden port at squared cosines 1/24 and 1/120 (four times); with the clique the three ports span 18 dimensions, joint Gram determinant 35163473387/331776000000, joint Krylov ranks 18, 36, 54 and positive joint memory; ||[J_H, C*C]||^2 = 1/1440", T, "three_ports"),
    ("wedgeport", "sixsite", "the clique's view", "the clique meets the root-wedge port at squared cosines 1/30 and 1/60 (trace 1/20, pair determinant 1711/1800)", T, "three_ports"),
    ("rootgraph", "moments", "every order", "distinct roots meet at most at 1, so (Delta^n)_(r, (n + 1)s) = (-1)^n delta_rs and lower powers vanish there: a port family on one root shell has Krylov rank d(n + 1) at every order, positive definite block Hankels and a Jacobi chain that never ends (the clique, the Golden, root-wedge, triangle and six-site ports, and the joint 18)", T, "root_shell_krylov"),
    ("bath", "sixsite", "the Schur memory", "the clique's memory variance is 183 I + 52 J and, with the band edge, V/(s + 256) <= Sigma(s) <= V/s, the n-th boundary moment is at most 495 x 256^n, and Sigma is no finite sum of poles", T, "schur_memory"),
    ("A4", "waves", "the light is the A4 Hodge star", "on the cycles, Lambda^2 A4, f^T Curl f = 2 Pf(R^T C R) identically, so J_H = Curl/sqrt5 is the Hodge star of Lambda^2 A4, with orientation character sgn; the hub's quartic witness has Pfaffian 175 and f^T J_H f = 70 sqrt5", T, "hodge_star"),
    ("pgl", "synthemes", "the exceptional action", "on the six Sylow labels S5 acts sharply 3-transitively; the 15 synthemes split 5 + 10, the five a one-factorization", T, "syntheme_bridge"),
    ("synthemes", "carrier", "the syntheme Dirac operator", "vertex i -> the special syntheme its stabilizer fixes, edge jk -> the syntheme sharing no pair with v_j and v_k: Pi D Pi^T is the syntheme incidence operator, equivariantly for all 120; a transposition has trace 7 on both and 3 on the ordinary duads (the hub, 14:07)", T, "syntheme_bridge"),
    ("V", "synthemes", "vertices as synthemes", "each vertex's stabilizer fixes exactly one of the five special synthemes", T, "syntheme_bridge"),
    ("E", "synthemes", "edges as synthemes", "each of the ten other synthemes shares no pair with exactly two special ones, its endpoints", T, "syntheme_bridge"),
    ("pgl", "source", "the complex six-line frame", "A(h_i)^2 = 5 P_A4; any five lines read the complex source, two erasures do not; [A, B] = (1/144) sum Im(conj u_i u_j) [S_i, S_j]; Tr Z^3 and Tr Z^2 Z* are twenty-term frame cubics; a blind pair kills every invariant odd form; Hom(source, cycles) = 0 and W W^+ = (10/9) P_cycle (the hub, 14:07)", T, "sylow_frame"),
    ("words", "source", "the regular word lanes", "T, the D3-orbit of (1, -1, 2, -1, -1), intertwines the regular orbits of 980 and 086 with the source (rank 5); G = S S_g T + I - S T lifts the five-cycle rationally, one more generator lifts it integrally (G+^5 = I7), and at u = e0, v = e1 the 12 x 12 word Jacobian is -46080 (the hub, 14:07)", T, "word_source"),
    ("words", "source", "index 3 per lane", "T has Smith invariants 1, 1, 1, 1, 3 and every orbit matrix over F3 has rank at most 4: no D3-map from one regular orbit onto the integral source is surjective, and no integer G has T G = S_g T", OB, "word_source"),
    ("cycles", "sixsite", "no A5 map to the sites", "Hom_A5(cycles, site6) = 0, while Hom_C5 = 8 and Hom_D3 = 4: no linear map to the natural six sites carries both the word D3 and the five-cycle", OB, "word_source"),
    ("halfper", "wedgeport", "quadrupolar at the band top", "at each of the band's 135 top half-periods the roots split as a D8 of second moment 28 I and its half-spin weights; b_rho is quadratic in rho and even, so the root-wedge port's amplitude and its first order vanish there: a quadrupole at the top as at the bottom, density 39 (256 - E)^5/(655360 pi^4) against C E^5/6000, while the clique and the Golden port start (256 - E)^3 and the odd triangle port (256 - E)^4", T, "band_top"),
    ("pgl", "rotor", "six rotor planes", "the fixed planes of the six Sylow C5s in the cycles are equi-isoclinic: sum F_i = 2 P_cycle and F_i F_j F_i = F_i/5, and centred they have the Gram of the six lines (1 and -1/5) (the hub, 15:03)", T, "pair_frame"),
    ("pgl", "waves", "the pair frame's blind lines", "the fifteen pair commutators of the six lines are a 160-tight frame of the cycles (cut 5, bright 6, dark 4 on the pair space); any four erasures are tolerated, the twelve failing five-sets are the pentagons and pentagrams of the six C5s, and their blind lines sum to P_cycle +- Curl/5, so J_H = (sqrt5/2)(F+ - F-)", T, "pair_frame"),
    ("wedgeport", "triangle", "the parity pair", "the odd S5 port, the S5 orbit of the triangle port, has its moments 1, 242, 58691, 14259954, 3470101592; the bath keeps inversion, so it is spectrally orthogonal to the even root-wedge port, and the four root ports span 24 and grow by 24 at every order (the hub, 15:03)", T, "parity_ports"),
    ("L0", "darkport", "the norm-four shell", "the glue's 2160 norm-four sites carry the dark four (A4 x sign) 36 times and the 240 roots none; the free orbit of x0 = (-1, 0, 0, 1, 1, 0, 1, 0) carries the isometric dark port A/sqrt600 (the hub, 15:03)", T, "dark_port"),
    ("darkport", "bath", "the dark moments", "1, 975/4, 237985/4, 14539767, variance 1315/16; spectrally orthogonal to every root-supported port; its sites lie on one sphere, so it grows by 4 at every order, and the five ports by 28", T, "dark_port"),
    ("pgl", "darkport", "the dark intertwiner", "the Reynolds average K: R^15 -> A4 (entries -2, 0, 2) has K^T K = 60 P_dark and K K^T = 60 P_A4, so the two-shell port [T_S C/sqrt160; A K/sqrt36000] is an isometry of the pair space modulo its cuts", T, "dark_port"),
    ("L0", "darkport", "the triple wedge", "D2(x) = [X ^ Y ^ (5 X o Y - <X, Y> 1)]/625 on the label blocks of the norm-four sites is a second dark port: nonzero at 1200 sites, rank 4, Gram 7200 P, moments 1, 232, 54150, variance 326 (the hub, 16:11)", T, "two_dark"),
    ("darkport", "moments", "thirty-two at every order", "the two dark ports meet at four squared principal cosines 5/192, with mixed moments 232 C and 54150 C; every norm-four site meets a root at 2 and none above, so their eight columns grow by 8 at every order, and with the root 24, orthogonal to them, the ports grow by 32(n + 1)", T, "two_dark"),
    ("darkport", "rotor", "the six F20 views", "the F20-equivariant isometries X_i of the dark four onto the moving planes P_cycle - F_i (Reynolds averages, sum X_i = 0) have graph projectors with sum 2 P_bright + 3 P_dark; any four views recover the ten, with condition number phi^4, and the Woodbury cross response is -X_i/47 at a = 1/2, b = 1/3, q = 1/7 (the hub, 16:11)", T, "fusion_frame"),
    ("pgl", "words", "the Golden repair", "the six Sylow lines are V in primitive source coordinates (entries +-1, index 16) and the word adapter T has index 3, so V Z^6 + T Z^6 = Z^5 with an intersection of index 48, and each of the three lines outside T's image (a0 + 2a1 + 2a2 + a3 + 2a4 not 0 mod 3) repairs a lane (the hub, 16:11)", T, "source_coding"),
    ("source", "words", "the global decoder", "S = V^T G encodes the source (V S = 12 I, S^T S = 12 G); any five readings invert (|det| 2592), and with an anchor the twelve word coordinates of 980 and 086 have a global linear inverse of |det| 6^10 (the hub, 16:11)", T, "source_coding"),
    ("V", "darkport", "the five K4 planes", "deleting a vertex leaves a commuting 2-plane of source vectors on its K4; their bivectors lie in the commutator's kernel with Gram 15 I - 3 J, the vertex simplex of the dark four, and every golden line puts 2/5 of its square into each plane (the sibling's MODEL, 16:17)", T, "k4_planes"),
    ("bath", "measure", "absolutely continuous", "Fourier makes Delta multiplication by eps = 240 - Lambda, nonconstant with range [0, 256]; by the coarea formula and Sard every site vector's spectral measure is absolutely continuous, and a nonzero finitely supported one (a site, any port vector) has density positive almost everywhere on the whole band; both edges are nondegenerate, so the density of states vanishes as E^3 and (256 - E)^3", T, "free_chain"),
    ("walks", "measure", "the free chain", "so (Rakhmanov) every port measure's Jacobi chain tends to alpha = 128, beta = 64^2; from W_0..W_90 the return, contrast and uniform chains reach alpha_44 = 128.03, 128.13 and 128.03 with beta rising to 4080.2, 4073.2 and 4080.6, close to the weight (E(256 - E))^3 with the same edge exponents (beta_45 = 4080.4)", T, "free_chain"),
    ("V", "source", "the matching planes", "each vertex deletion leaves the 2-plane E_r of matching differences, the fixed source space of its Klein four group; the five G-projectors have sum 2 I and P_r P_s P_r = P_r/4 (all principal angles 60 degrees), and Tr(P_r R_j) = 2/5 against each of the six Golden lines (the hub, 16:47)", T, "k4_complete"),
    ("source", "darkport", "exactly five dark planes", "on the commutator's 4-dimensional kernel the Pluecker quadrics have exactly five projective solutions, all reduced, and they are the five planes: W_AS(a ^ b) = 0 only for collinear pairs or pairs spanning one E_r; each is a regular zero (tangent spectrum (2/3)^3 (10/9)^3), and the oriented bivectors, a 15-tight simplex of the dark four, are told apart by L = sum 2^r <p_r, .> (values 15 2^s - 93)", T, "k4_complete"),
    ("source", "readout", "two rotating branches", "the finite return parent keeps each matching plane, with an exact blind circular orbit (energy 32, charge 16); on its S2 x S3 line u (|u|^2 = 18, Tr A^3/6 = -16) it rotates on two branches, X = omega^2 = 6 and 32/3 at r = 1/2, both checked in the full equations (the hub, 16:47)", T, "dark_branches"),
    ("wedgeport", "darkport", "one-frequency tomography", "one complete retained response G^-1 = [[A, C], [C^T, D]] of the anchored F20 interaction gives back q = Tr CC^T/Tr(A - min A), X = C/q and both baselines (q = 1/7, a = 1/2, b = 1/3 for X0 + 2X1); the scalar determinant sees only four singular squares (a one-parameter isospectral family through X0 + 2X1 - X2 + 3X4), and the two-pole emulators have 0, 1, 3, 4 modes above the band at q = 1/7, 1, 2, 5 (the hub, 16:47)", T, "tomography"),
    ("E", "source", "the quadratic frames", "the ten edge projectors and the six Golden projectors split the source's fifteen quadratics as 1 + 9 + 5 (traces 1/9, 1/25, 1/5), with a closed inverse and Parseval identity; five edges complete them exactly when their source rows are a basis, 162 of the 252 five-sets and all unimodular, which is when the complementary five edges form a connected nonbipartite graph (the hub, 17:26)", T, "quadratic_frames"),
    ("darkport", "readout", "dark intensities", "matched intensities 1 and 1/16 name the five dark planes from any four sensors; intensities do not fix a dark vector (two of norm 40 share 225, 225, 100, 25, 25), but seven full-spark detectors recover any real dark vector up to sign, and eight survive one erasure (the hub, 17:26)", T, "dark_readout"),
    ("source", "cycles", "cubic-null triangles", "the transposition-odd planes are cubic-null and their ten commutators, twice the complementary triangles, give T T^T = 20 P_cycle; the equilateral K4 pair 2X - Y - Z, sqrt3 (Y - Z) is commutator-dark and cubic-null (energy 96, charge 48); E - 2 sigma Q is a sum of squares, and |W_AS| = sqrt10/3 (the hub, 17:26)", T, "cubic_null"),
    ("A4", "golden", "the Fibonacci bridge", "the marked K = A(h0) has K^2 = 5 on A4, so Phi = (1 + K)/2 has Phi^2 = Phi + 1, and a rational S carries Phi to two blocks B = [[1, 1], [1, 0]]; B^6 = [[13, 8], [8, 5]], entry sum 34 (the hub, 17:26)", T, "golden_bridge"),
    ("darkport", "readout", "the dark measurement", "the five dark planes have frame operator 15 I, so M_r = p_r p_r^T D/15 is a measurement: it reads a plane as itself with probability 4/5 and as each other plane with 1/20, carries exactly 6/5 bits under a uniform prior, and gives any two planes Bhattacharyya coefficient 11/20 (the sibling's MODEL, 18:00)", T, "dark_measurement"),
    ("source", "readout", "plane tomography", "every bivector of the source is tangent to its oriented planes, so a linear reading immerses them only with all ten channels, the bright six and the dark four; Gr+(2, 5) = Q3 has c = 1 + 3h + 4h^2 + 2h^3 and p = 1 + h^2, so a normal plane bundle in R^8 would need e^2 = -h^2, and a smooth reading needs at least nine (the sibling's MODEL, 18:00)", T, "plane_tomography"),
    ("darkport", "readout", "the seventh sensor", "the fixed probe h12 = (z0 + z1)/3, covector ell12 = (0, -3, 0, -1, 0, 3, 1, 0, 1, -1), responds (3, 3, -2, -2, -2) on the five dark rays, so the six bright readings and ell12 detect every plane, while six readings never do (G(2, 5) has odd degree 5); the nonblind margin is sqrt2 and the sharp label gap sqrt(15/46), from the 512 active-set cases and ell* = (-17, -5, -10, -2, -6, -15, -10, 15, -4, 16) (the hub, 18:22)", T, "seventh_sensor"),
    ("source", "darkport", "preparability", "a reconstructed exterior vector comes from one source pair exactly when its Pluecker quadrics vanish: in the native chart |w ^ w|^2 = 4 q^T H4 q = 2 (w^T H w)^2 - Tr[(K_w G)^4], the squared distances to the simple cone and to the unit planes are (s - sqrt(s^2 - t))/2 and s + 1 - 2 lambda_1, and z0 + z1 is dark but not simple (the hub, 18:22)", T, "preparability"),
    ("cycles", "darkport", "the exterior code", "fifteen bright Golden-pair readings (sum Q Q* = 144 I) and ten dark duad probes (sum h h* = 5 P_D) give a Parseval inverse on all ten exterior coordinates and a [25, 10, 5] code, [15, 6, 5] + [10, 4, 6], whose dark integer part has Smith invariants 1, 5, 5, 5 (the hub, 18:22)", T, "exterior_code"),
    ("source", "darkport", "two instruments", "the dark measurement names its plane with optimal success 4/5 and carries 6/5 = 8/5 - 2/5 bits (Holevo bound 2, KL divergence 3, eleven repeats for 1% error), while the source states P(E_r)/2 against the six Golden effects read 1/6 everywhere: two instruments, not one processed state (the hub, 18:22; the sibling's MODEL, 18:33)", T, "dark_information"),
    ("bath", "source", "causal records", "an ideal known-state boundary record y = -K * g of the native bath, with G_C = 183 P_contrast + 495 P_uniform, inverts the forcing g through a second-kind Volterra equation, with exact jets and the bound (1/183) cosh(sqrt(42240/61) T); the empty-bath pair X - Z, Y - Z (E = 8, Q = 4) is force-free yet has cubic phasor (-4/3, -4/3) (the hub, 18:22)", T, "causal_records"),
    ("parent", "source", "the Golden adapter", "marking point 5 reads the six Sylow cosets A5/D10 by their pentagons' Golden lines: B_G = H_G O36 has rank 5 and B_G B_G^T = 120 P_source, is A5-equivariant and fixed by r, so it keeps rank 5 where O90's r-history reaches 360 in five settings (90, 170, 250, 330, 360); the readers' joint ranks are 125, 165 and 230 (the hub, 18:22)", T, "parent_readers"),
    ("parent", "golden", "Golden30", "F30 = 6 P30 O36 (rank 30, F30 F30^T = 360 P30) and the involution t give A = F30 U_t F30^T/360, and 30 A has characteristic polynomial q^6 (q + 6)^5 (q - 6)^9 (q^2 + 3q - 99)^8; the Return I - A^2 exceeds 17/20, det[[I, A], [A, I]] = (24/25)^14 (7821/10000)^8, and on the 16-sector Phi16 = (I + J)/2 is eight Fibonacci blocks (the hub, 18:22)", T, "golden30"),
    ("A4", "parent", "the marked injection", "a rank-4 T with Phi16 T = T Phi4 carries A4's two Fibonacci blocks (Phi4 = (1 + K)/2, K = A(h0)) into the Golden30's eight: a marked operator injection, not an A6 map (the hub, 18:22)", T, "golden30"),
    ("parent", "readout", "the blind 126", "closing the F30 rows under r and t gives ranks 30, 60, 90, 145, 216, 225, 234; the blind 126 = 1 + 25 + 100 is the central projector of the trivial, chi5 and chi10 blocks; the fibre means reach 260, and one chi10 reader completes 360 (the hub, 18:22)", T, "parent_closure"),
    ("synthemes", "parent", "two 36s", "the coset 36 has orbits 6 + 30 and the six-label/duad/syntheme 36 has orbits 6 + 15 + 5 + 10 under the transitive A5, so no A5-module isomorphism identifies them: their common cardinality is not a map (the hub, 18:22)", OB, "two_36s"),
    ("E8", "cyclo", "the cyclotomic line", "every root generates E8 over Z[c'], so E8 is the ring Z[zeta30] with the trace form Tr(alpha x ybar), alpha = (2 + 2 eta + eta^2)/15, totally positive of norm 1/disc Q(zeta15); only the thirty roots of unity commute with c' (layer 25)", T, "cyclotomic_line"),
    ("cyclo", "clocks", "the clocks are Galois", "the normalizer of <c'> is the roots of unity times Gal(Q(zeta30)/Q) = <7> x <11>, 240 elements; the day is sigma7, the golden clock sigma11 and the mirror sigma29, each times a unit u with u ubar = sigma(alpha)/alpha (layer 25)", T, "galois_clocks"),
    ("clocks", "residue", "the residue plane", "the tick's 25 fixed momenta are E8/(1 - g)E8 = F25, the residue field of Q(zeta15) at 5, with c' a primitive sixth root of unity; the 240 roots lie ten over each of its 24 nonzero points (layer 25)", T, "residue_plane"),
    ("residue", "L0", "one residue line", "the six F5-lines pull back to six A4 + A4 sublattices whose root systems partition the 240 roots; the carrier's A4 + A4' is one of them, and its four glue classes are the parallel lines (layer 25)", T, "residue_plane"),
    ("residue", "pgl", "the tick's normalizer", "C_W(g) has 600 elements and acts on the plane as SL(2,5), the binary icosahedral group; with the day N_W(<g>) acts as GL(2,5), and on the six lines as PGL(2,5), the exceptional S5 (layer 25)", T, "tick_normalizer"),
    ("L0", "A4", "either factor", "the carrier line's stabilizer in N_W(<g>) has 400 elements, half of which exchange A4 and A4', so the carrier's A4 is either factor of any residue line, unique up to the tick's symmetry (layer 25)", T, "tick_normalizer"),
    ("residue", "surface", "the six axes", "C_W(g) acts on the six residue lines as PSL(2,5) = A5, transitively, as the icosahedral rotations act on the six axes: the hemi-icosahedron's vertices are the tick's six A4 + A4 (layer 25)", T, "tick_normalizer"),
    ("residue", "air801", "the Singer cycle", "on F25 the day is the Singer cycle 2 + 2 omega of order 24, turning the six lines in one 6-cycle, and AIR_801 mod 5 has the characteristic polynomial of minus the day, so the canon's 801 matrix is that Singer cycle (layer 25)", T, "clock_residues"),
    ("cyclo", "golden", "the Gauss sum", "Q(sqrt5) is the real quadratic field of Q(zeta5) inside Q(zeta30): the canon's A(h0) is the quadratic Gauss sum r + r^4 - r^2 - r^3, and on E8 the tick's Gauss sum squares to 5 (layer 25)", T, "golden_gauss"),
    ("L0", "carrier", "the shadows", "the mixed roots project onto the carrier's A4 as the five vertex and ten edge weights, and their Gram plus 2/5 is the signless incidence M, so D = [[0, M], [M^T, 0]] is the shadow incidence (layer 25)", T, "carrier_shadows"),
    ("pgl", "parent", "the hexad", "with the six residue lines labelled so that the carrier rotation is (01234) and the carrier line is 5, the hub's t = (23)(45) lies outside the tick's PSL(2,5) and the two generate A6: the 360 parent is the alternating group of the tick's hexad (layer 25)", T, "parent_hexad"),
    ("circle", "parent", "the address map", "address(j) = r^p c_q sends the 4320 circle onto the 360 parent's settings twelve to one, with address(j + 864) = r address(j); no address is equivariant for the natural doubling (the settings' F20 orbits are 5^4 10^2 20^16 against the clock's fives), so this is a selected scheduling convention (the hub, 19:39)", SR, "address_map"),
    ("clocks", "regular", "Springer", "the regular numbers of E8 are the divisors of the clocks' orders 30, 24 and 20; each regular class is a power of c', d or v with every eigenvalue a primitive d-th root, and its centralizer, counted from the images of a Z[w]-basis of roots, has the order the degrees give: 30, 24, 20, 288, 192, 600, 46080 and 155520 (layer 26)", T, "primes.regular_clocks"),
    ("regular", "cyclo", "three cyclotomic lines", "the clocks with cyclic centralizers make E8 a line over Z[zeta30], Z[zeta24] and Z[zeta20], each with a trace form of norm 1/disc (3^-4 5^-6, 2^-16 3^-4, 2^-8 5^-6) and a normalizer that realizes its Galois group (240, 192, 160) (layer 26)", T, "primes.cyclotomic_lines"),
    ("regular", "residue", "the centralizer of 5", "the regular class 5 is the tick, whose centralizer of order 20 x 30 = 600 acts on its residue plane F25 as SL(2,5) = Sp(2,5), the isometries of the plane's symplectic form (layer 26)", T, "primes.prime_residues"),
    ("regular", "sun", "the centralizer of 3", "the regular class 3 is the sun s = c'^10, whose centralizer of order 12 x 18 x 24 x 30 = 155520 acts on its 81 momenta as Sp(4,3), 155520/3 = 51840 isometries of <x, (s - s^2) y> mod 3, with kernel <s> (layer 26)", T, "primes.prime_residues"),
    ("regular", "halfper", "the centralizer of 2", "the regular class 2 is -1, the half-turn, whose centralizer is W(E8), of order 2 |GO8+(2)|; it keeps the half-period form q(x) = <x, x>/2 mod 2 (cited: W(E8)/<-1> = GO8+(2)) (layer 26)", T, "primes.prime_residues"),
    ("cyclo", "sun", "the prime over 3", "c' = (-1) s g, and the sun s = c'^10 fixes E8/(1 - s)E8 = F81 (Smith form 1^4 3^4), the residue field of Q(zeta15) at its prime over 3, on which c' has order 10; with the half-turn's F16 x F16 and the tick's F25 these are the residue rings of Z[zeta30] at 2, 3 and 5, and the roots lie 2, 3 and 10 over their points (layer 26)", T, "primes.prime_clocks"),
    ("sun", "rootgraph", "W(3)", "the sun's 40 projective points pull back to 40 A2 that partition the roots, two orthogonal exactly when their points are; the 40 totally isotropic lines are 40 frames 4A2 (the quadrangle W(3)), and the ten F9-lines, F9 = F3[phi] with phi = c' + c'^-1, are a spread of them: the decad (layer 26)", T, "primes.sun"),
    ("regular", "cyclo", "no fourth line", "Q(zeta16), the fourth cyclotomic field of degree 8, carries Z^8 and not E8: W(E8) has no element of order 16, since one would square to a conjugate of d^3 (cited: Springer) and C_W(d^3), 192 elements, has none (layer 26)", OB, "primes.no_sixteen"),
    ("cyclo", "halfper", "the primes over 2", "E8/2E8 = Z[zeta30]/2 = F16 x F16: the two primes over 2 are complementary totally singular subspaces, swapped by the mirror, on each of which c' is a Singer cycle of order 15; the 120 nonsingular half-periods carry the roots, two each (layer 26)", T, "primes.half_turn"),
    ("sun", "parent", "the decad", "the 2160 isometries that commute with the sun and with phi act on the ten F9-lines as PSL(2,9) with kernel <c'^5>, and an isomorphism from the hub's <r, t> sends r to the Coxeter clock: the 360 parent is the sun's A6 on its ten 4A2 frames (layer 26)", T, "primes.decad"),
    ("sun", "AGL", "the clocks on the decad", "on the ten frames c' and the tick act as one fixed-point-free 5-element and the day as its doubling, of order 4 and outside A6: the day-Coxeter group acts as AGL(1,5), and the isomorphism extends to S6 = PSigmaL(2,9) with the hub's doubling sent to the day (layer 26)", T, "primes.decad"),
    ("circle", "parent", "no homomorphism", "A6's elements have orders 1 to 5, all dividing 4320, so Z/4320 has exactly 360 homomorphisms to A6, each with a cyclic image of at most five elements: the address map's orbits add to 360, but no clock homomorphism covers A6, and the address map is not one (the owner, 20:22)", OB, "primes.parent_cover"),
    ("clocks", "parent", "solvable clocks", "every clock lies in the normalizer of <c'>, which is solvable (240 > 30 > 1), and A6 is perfect, so no clock group maps onto it; on the tick's hexad the seed acts through PGL(2,5), whose even part holds 60 of the 360 (layer 26)", OB, "primes.parent_cover"),
    ("sun", "bath", "243", "the bath is 240 + 3 = 243 at the sun's 80 nonzero fixed momenta: three roots lie over each nonzero residue point, so every nontrivial character of F81 sums to -3 over the roots (layer 27)", T, "places.band_at_places"),
    ("residue", "momenta", "Pontryagin duality", "the tick's 25 fixed momenta are the characters of its residue plane, and the bath there is 240 - sum_r chi(r): 0, and 250 on the 24 others, where ten roots lie over each nonzero point (layer 27)", T, "places.band_at_places"),
    ("halfper", "gksl", "the quadric sums", "the GKSL rates on the 256 Paulis are 240 - sum_r (-1)^<r, y>: 0, then 256 on the 135 singular and 224 on the 120 nonsingular half-periods, where the quadric's character sums are -16 and +16 (layer 27)", T, "places.band_at_places"),
    ("halfper", "pauli", "two stabilizers", "under the Pauli map the two primes over 2 are complementary stabilizer groups of 16 commuting symmetric real Paulis; Paulis commute exactly when their half-periods have even inner product; c' keeps both groups and the mirror swaps them (layer 27)", T, "places.qubit_primes"),
    ("sun", "golden", "F9 = F3[phi]", "the golden ratio Phi = 1 + g + g^4 generates the decad's field F9 on the sun's momenta, and B has Pisano period 8 mod 3: the golden field is inert at 3 (layer 27)", T, "places.golden_places"),
    ("halfper", "golden", "F4 = F2[phi]", "on the half-periods Phi is a cube root of unity keeping both primes over 2, F4 = F2[Phi], and B has Pisano period 3 mod 2: the golden field is inert at 2, while at 5 it is ramified (layer 27)", T, "places.golden_places"),
    ("memory", "clocks", "no clock of order 90", "an element of order n of GL8(Z) needs psi(n) <= 8, and the memory clock has order 90 with psi(90) = 10, so no lattice clock of the seed runs it (layer 27)", OB, "places.limits"),
    ("circle", "clocks", "no faithful circle", "psi(4320) = 38 > 8: the circle's images in GL8(Z) have order at most 60, and the element orders of W(E8) stop at 30 (cited), so only its part <144> acts, as the Coxeter clock (layer 27)", OB, "places.limits"),
    ("E8", "principal", "the Weyl vector", "rho = (46, 68, 91, 135, 110, 84, 57, 29) in the root basis is primitive, with <r, rho> = ht(r) on the roots, so t -> t rho is a circle of momenta in R^8 / E8 on which every step keeps its order (layer 28)", T, "principal.circle"),
    ("circle", "principal", "k -> k rho / 4320", "the canon's circle embeds in the momentum torus as the principal circle: no lattice clock runs it, but this circle of momenta does, and its step 144 is Kostant's principal element (layer 28)", T, "principal.circle"),
    ("principal", "clocks", "Kostant", "rho/30 acts on the adjoint representation with the spectrum of a lift of c': the clock's eigenvalues on the Cartan and eight copies of every 30th root from its free orbits on the roots; Kostant makes it conjugate to that lift (cited), so the step 144 is the Coxeter clock (layer 28)", T, "principal.regular_steps"),
    ("principal", "regular", "the regular steps", "for each of the thirteen regular numbers d the step 4320/d, rho/d, has the adjoint spectrum of a lift of the regular clock of order d, which turns the roots in 240/d free orbits; the steps 180 and 216 carry the day and the golden clock (layer 28)", T, "principal.regular_steps"),
    ("principal", "bath", "248 - chi", "on the principal circle the band is 248 minus the adjoint character, and at the regular step 4320/d the Ramanujan sum makes it 248 - 8 mu(d)/phi(d): 256 at the half-turn, the circle's top, down to 249 at the Coxeter step (layer 28)", T, "principal.band_on_circle"),
    ("principal", "census", "the critical steps", "the band is critical on the principal circle exactly at its nine elements of order 2 to 5, where the centralizer has full rank: the census's D8 (256), A8 (252), D5 + A3 (248) and A4 + A4 (250), the alcove's vertices of marks 2, 3, 4 and 5 (layer 28)", T, "principal.critical_steps"),
    ("time", "principal", "the A4 + A4 vertex", "the time clock's steps 864k are the principal points of order 5, whose centralizer has the carrier's root system A4 + A4: the family of the tick's 24 fixed momenta, at eps 250 (layer 28)", T, "principal.critical_steps"),
    ("observer", "principal", "the D5 + A3 vertex", "the observer clock's generators 1080 and 3240 are the principal points of order 4, of type D5 + A3 at eps 248, and its square 2160 is the D8 half-turn at the band's top 256 (layer 28)", T, "principal.critical_steps"),
    ("c27", "principal", "the A8 vertex", "the 27-clock meets the critical steps exactly in its order-3 steps 1440 and 2880, the principal points of type A8 at eps 252 (layer 28)", T, "principal.critical_steps"),
    ("synthemes", "petersen", "the syntheme incidence", "the ten nonspecial synthemes meet the fifteen duads in B with B B^T = 4I + J - K = 3I + A_Petersen: two synthemes share a duad exactly when their K5 edges are disjoint, so B is the signless Petersen incidence, of rank 10, and P_source = (B B^T - I)(6I - B B^T)/6 (the hub, 00:25)", T, "petersen_sequence"),
    ("residue", "rootgraph", "the six-line quotient", "A S = S Q with Q = 10J - 4I: a root has 6 neighbours on its own line and 10 on each other, so the six A4 + A4 are an equitable partition of the root graph, and a reducing one (A commutes with S S^T), so the finite graph has no Schur memory across it (the hub, 23:38)", T, "six_lines"),
    ("time", "pgl", "the phase on the Sylow labels", "sigma_g fixes one Sylow label; f(p) = sigma_g^p(anchor) has f(p(j + 864)) = sigma_g f(p(j)) and f(p(3457 j)) = sigma_d f(p(j)) on all 4320 frames, 864 per label (the hub, 14:07)", T, "clock_sylow"),
    ("assignment", "binding", "one root of every pair", "taking one of each pair +-rho as whole multiplets gives an odd SU(5) anomaly and 25 doublets (Witten's anomaly), every time", OB, "assignment.chirality"),
    ("circle", "memory", "24 maps, one orbit", "the circle maps onto the memory clock's group <A> = Z/90 in 24 ways, k -> A^(uk) for the units u, each with kernel <90>; A^u has A's cycle type 10^11 9 1, so the memory's normalizer in S_120 makes the 24 conjugate: the stepping is unique up to the memory's symmetry, without the selection (30 Oct)", T, "memory_quotients"),
    ("memory", "vortex", "up to doubling", "for every map of the circle onto the memory clock the 9-cycle reads x -> u x mod 9, and u mod 9 is a power of 2, a primitive root mod 9: the vortex up to its doubling (30 Oct)", T, "memory_quotients"),
    ("memory", "time", "up to doubling", "for every map of the circle onto the memory clock the 10-cycles read x -> u x mod 10, and u mod 5 is a power of 2, a primitive root mod 5: the time coordinate x mod 5 up to its doubling (30 Oct)", T, "memory_quotients"),
    ("kerM", "gravity", "the massless tower", "on M4 x F the cross terms cancel, D^2 = D_M^2 (x) 1 + m^2 (1 (x) D_F^2): over every level of M4 sits the tower 0, 3m^2, 8m^2 (multiplicities 5, 8, 2), whose bottom is the five dark modes ker M, and the heat trace factorizes; M4 and m stay free (30 Oct)", gates.CONDITIONAL, "massless_tower"),
    ("kerM", "cosmology", "the dark momentum", "the stiff sector is the five dark modes: the kernel projector 0 + P_kerM commutes with D^2, so a^3 P0 psi' is conserved on every flat FLRW background and the dark modes' energy falls as a^-6 (30 Oct)", gates.CONDITIONAL, "stiff_kernel"),
    ("cosmology", "calibration", "the mass scale", "a calibration t -> tau t acts on the cosmos's free inputs, m -> m/tau and Lambda_cc -> Lambda_cc/tau^2, with the same a and psi, so the cosmos has no internal time unit either; in the decoupling limit its flow is the native flow in u = m t, a calibration with tau = 1/m (30 Oct)", gates.CONDITIONAL, "cosmos_calibration"),
    ("G120", "residue", "the unit group", "G120 acts on the tick's residue field F25 by multiplication, with kernel the tick <g> and image all of F25^x, the day's 24 powers: G120 / <g> = F25^x and G120 = <g> x| <d>, the day doubling the tick (30 Oct)", T, "day_units"),
    ("frame", "census", "A8", "the frame's 72 roots are an A8, and each dual vector w_j is a point of order 3 whose stabilizer is exactly that A8: the band is critical there at 252, the census's A8 family of 1920 points, the alcove's vertex of mark 3 and the principal steps 1440 and 2880 (30 Oct)", T, "frame_a8"),
    ("AGL", "cube", "the Frobenius", "on the four-cube's vertices, the sixteen cuts of K5 mod 2 = F16 by delta({k}) -> zeta^k, the tick multiplies by a primitive fifth root of unity and the doubling is the Frobenius y -> y^2: AGL(1,5) acts as <zeta5> x| Gal(F16/F2) inside GammaL(1,16) (30 Oct)", T, "cube_frobenius"),
    ("grain", "principal", "the regular steps", "on the principal circle the grain is the 60 points k rho/60, the golden step 216 = rho/20 times the sun's step 1440 = rho/3, with the spectra of the golden clock and the sun; it holds the steps of the eleven regular orders dividing 60, all but the day's 8 and 24 (30 Oct)", T, "grain_steps"),
    ("pg25", "synthemes", "secants through a point", "the three secants through an interior point of PG(2,5) meet the conic in a syntheme: the ten interior points are the ten nonspecial synthemes, and the fifteen exterior points, in five self-polar triangles, give the special five, a one-factorization; a labelling that carries the exceptional sigma onto PGL(2,5) matches them with the Sylow labels' 10 + 5 (30 Oct)", T, "plane_synthemes"),
    ("E8", "principal", "unique up to W(E8)", "the Weyl vector is the half-sum of the positive roots and is regular, so it determines its positive system, and W(E8) permutes the positive systems transitively (cited) and keeps the band: the conjugate circles k -> k w rho / 4320 have the same band values, critical steps and types, so the principal circle is unique up to W(E8) (30 Oct)", T, "principal.principal_uniqueness"),
    ("principal", "grain", "the critical steps", "the band's nine nonzero critical steps are the union of <2160>, <1440>, <1080> and <864>, so they generate <72>, the grain, of order lcm(2, 3, 4, 5) = 60: the grain is the subgroup the band's critical points generate, and it is the seed's (30 Oct)", T, "principal.clock_lattice"),
    ("time", "observer", "the golden step", "the time clock and the observer clock meet in 0 and add to <216> = Z/20, the golden step's subgroup, Z/5 x Z/4: the golden step rho/20 is the sum of the two small clocks (30 Oct)", T, "principal.clock_lattice"),
    ("observer", "grain", "the three small clocks", "the grain is the sum <864> + <1080> + <1440> of the time clock, the observer clock and the sun's subgroup, lcm(5, 4, 3) = 60 points: the two small clocks and the sun generate the grain (30 Oct)", T, "principal.clock_lattice"),
    ("observer", "regular", "the regular class 4", "the observer clock's step 1080 = rho/4 has the adjoint spectrum of the regular clock of order 4, which is d^6, the day's sixth power, with d^12 = -1 the half-turn at the observer clock's square 2160 (30 Oct)", T, "principal.clock_lattice"),
    ("principal", "atlas", "modulo the regular steps", "the thirteen regular steps 4320/d are multiples of 36 and generate the seam <36> (as 144 and 180 already do; 216 = 6 x 36 adds nothing), of order lcm(30, 24, 20) = 120: the atlas Z/36 is the principal circle modulo the subgroup its regular steps generate, the largest quotient in which every step of regular order and every critical step vanishes; the quotient size 36 = 4320/120 is the canon's cofactor (30 Oct)", T, "principal.clock_lattice"),
    ("principal", "c27", "the Sylow 3-subgroup", "<160> is the unique subgroup of order 27 of the circle (4320 = 2^5 3^3 5), the points of order a power of 3; it holds the sun's step 1440 = rho/3, whose spectrum is the regular class 3, and the two A8 critical steps; the order 27 = 3^3 comes from the canon's 4320, not from the seed, whose regular orders carry one 3 (30 Oct)", T, "principal.clock_lattice"),
    ("grain", "coil", "plus the 27-clock", "the coil <8> is the sum <72> + <160> of the grain and the 27-clock, which meet in the sun's subgroup <1440>: 60 x 27 / 3 = 540 points, the kernel of x -> 540 x; it is also generated by the time, observer and 27-clocks (30 Oct)", T, "principal.clock_lattice"),
    ("principal", "miss", "the steps the tick does not see", "the miss set <5> is the kernel of the time coordinate, the points of order prime to 5, <135> + <160>; it holds every critical step but the time clock's four, and the atlas and the vortex hold none, every step of regular order and every critical step being 0 mod 36 (30 Oct)", T, "principal.clock_lattice"),
    ("principal", "vortex", "the 27-clock modulo the sun", "x -> x mod 9 maps the 27-clock <160> onto Z/9 with kernel the sun's subgroup <1440>, and the whole principal circle onto it with kernel <9> = <36> + <135>, the seam plus the 2-part, 480 points; the quotient size 9 = 27/3 is the canon's (30 Oct)", T, "principal.clock_lattice"),
    ("golden", "clocks", "the tick's cosine", "the tick's cosine g + g^-1 has minimal polynomial x^2 + x - 1, so X = -(g + g^-1) satisfies X^2 = X + I with characteristic polynomial (x^2 - x - 1)^4, and E8 has a Z-basis of four roots x_i and their images X x_i, ordered (X x_i, x_i), in which X is four blocks B: E8 = Z[phi]^4, the golden companion acting on the whole lattice through the tick; X = I - Phi for layer 27's Phi = 1 + g + g^4, and Z[g] = Z[zeta5] makes E8 a free module of rank 2 (30 Oct)", T, "golden_cosine"),
    ("golden", "G120", "the Galois conjugation", "the day conjugates the tick to its square and so carries X = -(g + g^-1) to I - X: it acts on Z[phi] as phi -> 1 - phi, the Galois conjugation of Q(sqrt5); c' commutes with X, so G120 acts on Z[X] through Gal(Q(sqrt5)/Q) = Z/2, 60 elements fixing X and 60 conjugating it, with kernel <g, d^2>; the embedding of Z[phi] into Z[X] is unique up to the day (30 Oct)", T, "golden_galois"),
    ("golden", "regular", "the cosine rings", "the cosine w + w^-1 of the regular clock of order d has characteristic polynomial Psi_d^(8/deg Psi_d), Psi_d the minimal polynomial of 2 cos(2 pi/d); the golden polynomial x^2 - x - 1 is Psi_10 = Psi_5(-x), the cosine of c'^3 = -g^3 is Phi, and the golden clock's cosine squares to Phi + 2; X lies in the cosine ring Z[w + w^-1] exactly for the five regular orders divisible by 5 (30 Oct)", T, "regular_cosines"),
    ("torus", "principal", "the critical steps", "the nine-torus's frequencies are exact: 240 - sum_k m_k cos(2 pi k/m_i) at the alcove's vertices, and 6800/27 and 4025/16 at the two Niven points on the lines R omega_2 and R omega_3; four of the nine, 256, 252, 248 and 250, are the band at the principal circle's critical steps of order 2, 3, 4 and 5 (30 Oct)", T, "torus_places"),
    ("torus", "halfper", "the half-periods", "two of the nine frequencies are the band at the 256 half-periods: 256 at the 135 of type D8 and 224 at the 120 of type E7 + A1; the half-turn 2160 is the half-period rho/2, of type D8 (30 Oct)", T, "torus_places"),
    ("torus", "sun", "the sun's momenta", "243 is the band at the sun's 80 nonzero fixed momenta, of type E6 + A2, every one a critical point of the band (30 Oct)", T, "torus_places"),
    ("torus", "momenta", "the tick's momenta", "250 is the band at the tick's 24 nonzero fixed momenta, of type A4 + A4; so six of the nine frequencies are placed through six of the eleven census families (E8 is the seventh type present, at the band's minimum 0), and sqrt 251, sqrt(4025/16) and sqrt(6800/27) (A5 + A2 + A1, A6 + A1, A7) are at no fixed momentum of a prime clock and at no critical step of the circle (30 Oct)", T, "torus_places"),
]

def notes_1504():
    """The sibling's MODEL editions of 14:49 and 15:04 (Names, Skew, Pulse) and the separate model's Matched History
    receipt (15:01), replayed as arithmetic."""
    order = lambda s: N // gcd(s, N)
    S = spine.subgroup
    R = np.rint(np.array(native.boundary_rotation(), dtype=float)).astype(np.int64)
    I6 = np.eye(6, dtype=np.int64)
    P = np.linalg.matrix_power
    Sk = R - R.T
    poly = P(Sk, 4) + 5 * P(Sk, 2) + 5 * I6
    rank = lambda M: np.linalg.matrix_rank(M.astype(float))
    W1, W2 = R - P(R, 4), P(R, 2) - P(R, 3)
    Jr = np.fliplr(I6)
    psi0, v0 = carrier.canon_initial_datum()
    E = carrier.edges()
    cyc = {E[i]: int(v0[5 + i]) for i in range(10) if v0[5 + i]}
    sw = {0: 3, 3: 0, 1: 2, 2: 1, 4: 4}
    img = {tuple(sorted((sw[a], sw[b]))): s for (a, b), s in cyc.items()}
    R5 = np.roll(np.eye(5, dtype=np.int64), 1, axis=0)
    L2 = np.zeros((10, 10), dtype=np.int64)
    for k, (i, j) in enumerate(E):
        a, b = int(np.argmax(R5[:, i])), int(np.argmax(R5[:, j]))
        L2[E.index(tuple(sorted((a, b)))), k] = 1 if a < b else -1
    B2 = np.array([[1, 1], [1, 0]], dtype=np.int64)
    K = np.array([[1, 1], [-5, -1]], dtype=np.int64)
    F = [0, 1]
    for _ in range(12):
        F.append(F[-1] + F[-2])
    comm = lambda A, Bm: A @ Bm - Bm @ A
    phi = (1 + sp.sqrt(5)) / 2
    cycles27 = sorted(len(c) for c in _cycles([2 * x % 27 for x in range(27)]))
    D5, T5 = (lambda x: 2 * x % 5), (lambda k: (lambda x: (x + k) % 5))
    return {
        "the six-site rotor R (order 5, fixing x0) has skew part S = R - R^T of rank 4, killed by S^4 + 5S^2 + 5I, which has "
        "rank 2: the polynomial is t^2 - 5t + 5 in t = -S^2, the relation of the golden pairs 2 + phi and 3 - phi (sum 5, "
        "product 5), and the five powers of R add to it, S^4 + 5S^2 + 5I = sum_k R^k = 5 P_fix, since ker S is the fixed "
        "space of R; the two windings R - R^4 and R^2 - R^3 have Frobenius Gram 10I":
            np.array_equal(P(R, 5), I6) and R[:, 0].tolist() == [1, 0, 0, 0, 0, 0] and rank(Sk) == 4 and not (Sk @ poly).any()
            and rank(poly) == 2 and np.array_equal(sum(P(R, k) for k in range(5)), poly)
            and all(sp.simplify(v ** 2 - 5 * v + 5) == 0 for v in (2 + phi, 3 - phi)) and sp.simplify((2 + phi) * (3 - phi)) == 5
            and [[int((A * Bm).sum()) for Bm in (W1, W2)] for A in (W1, W2)] == [[10, 0], [0, 10]],
        "the anti-diagonal reversal J squares to I but conjugates R neither to R^4 nor S to -S; the site swap (0 3)(1 2) "
        "exchanges the two positive edges of the datum's 4-cycle v0 and fixes its two negative ones; on Lambda^2 R^5, the "
        "exterior six of the sum-zero four plus u ^ (sum-zero), the five-cycle fixes a plane, inside the six":
            np.array_equal(Jr @ Jr, I6) and not np.array_equal(Jr @ R @ Jr, P(R, 4)) and not np.array_equal(Jr @ Sk @ Jr, -Sk)
            and cyc == {(0, 1): 1, (0, 3): -1, (1, 2): -1, (2, 3): 1}
            and {e for e, s in cyc.items() if s > 0} == {e for e, s in img.items() if s > 0}
            and all(img[e] == s for e, s in cyc.items() if s < 0) and 10 - rank(L2 - np.eye(10, dtype=np.int64)) == 2,
        "a Karma matrix: a traceless integer 2 x 2 K with K^2 = -4I (determinant 4) and det [K, B] = -29 exists, "
        "K = [[1, 1], [-5, -1]]; since B^n = F_n B + F_(n-1) I, [K, B^n] = F_n [K, B] has trace 0 and determinant -29 F_n^2 "
        "for every n (through the tenth, as the sibling reads); 29 = 2 + 3 + 4 + 6 + 5 + 4 + 3 + 2 is the highest root's "
        "marks without the leading 1, its height h - 1, and generates the circle; the sibling's own Karma operand is not "
        "stored here":
            np.array_equal(K @ K, -4 * np.eye(2, dtype=np.int64)) and round(np.linalg.det(K)) == 4 and np.trace(K) == 0
            and all(np.array_equal(comm(K, P(B2, n)), F[n] * comm(K, B2)) and np.trace(comm(K, P(B2, n))) == 0
                    and round(np.linalg.det(comm(K, P(B2, n)))) == -29 * F[n] ** 2 for n in range(1, 11))
            and sum([2, 3, 4, 6, 5, 4, 3, 2]) == 29 == int(principal.weyl_vector()[2].max()) and gcd(29, N) == 1,
        "the Names' clock readings: 36 x 120 = 4320 and 15 x 36 = 540, of order 8; 11 and 29 generate the circle; 108 = 3 "
        "mod 5, so 108 steps of the five-cycle are its third power; the yugas 1728 + 1296 + 864 + 432 = 4320; multiplication "
        "by 3 kills exactly 0, 1440, 2880, the nakshatra seam; doubling mod 27 has cycles 18, 6, 2, 1; the cut 736 has order "
        "135, the walk residues 480 and 3600 orders 9 and 6; 16 x 270 = 4320 with 16 meeting the tick and 270 not, and "
        "54 x 16 = 864 with both factors meeting it; the golden powers 0, 1, 4, 5, 20 land on 0, 216, 864, 1080, 0, and 1080 "
        "has order 4; the step 27 has order 160 and 160 order 27":
            36 * 120 == N and 15 * 36 == 540 and order(540) == 8 and gcd(11, N) == gcd(29, N) == 1 and 108 % 5 == 3
            and 1728 + 1296 + 864 + 432 == N and [x for x in range(N) if 3 * x % N == 0] == [0, 1440, 2880]
            and cycles27 == [1, 2, 6, 18] and (order(736), order(480), order(3600)) == (135, 9, 6) and 16 * 270 == N
            and (order(16), order(270)) == (270, 16) and 16 % 5 != 0 and 270 % 5 == 0 and 54 * 16 == 864 and 54 % 5 != 0
            and [216 * k % N for k in (0, 1, 4, 5, 20)] == [0, 216, 864, 1080, 0] and order(1080) == 4
            and (order(27), order(160)) == (160, 27),
        "the Skew's readings: 240 - 56 - 1 = 183 generates <3> and 4 x 183 + 2 x 127 = 986 generates <2>; 127 = 58691 - 242^2 "
        "and 131 = 3 x 64 + 8 x (-8) + 3 = 127 + 4; 16 + 20 = 36 and 16 - 20 = -4 (the sign census; its matrix is not stored "
        "here); and a correction: on the five points of <864>, doubling after a triple translation is one translation after "
        "doubling, 2(x + 3) = 2x + 1 mod 5, not two; two translations after doubling is doubling after one, 2(x + 1) = 2x + 2":
            240 - 56 - 1 == 183 and S(183) == S(3) and 4 * 183 + 2 * 127 == 986 and S(986) == S(2) and 58691 - 242 ** 2 == 127
            and 3 * 64 + 8 * (-8) + 3 == 131 == 127 + 4 and 16 + 20 == 36 and 16 - 20 == -4
            and all(D5(T5(3)(x)) == T5(1)(D5(x)) for x in range(5)) and not all(D5(T5(3)(x)) == T5(2)(D5(x)) for x in range(5))
            and all(D5(T5(1)(x)) == T5(2)(D5(x)) for x in range(5)),
        "the separate model's Matched History receipt (15:01): 36 payload files with 35 hashes (the manifest unhashed, as "
        "in the 14:25 record), 4170 artifacts preserved and combined, 620 + 4 typed joins = 624 relationships, 24 exact "
        "groups and 9 regressions, no new matrix; the Library pointer at N34, the Drive pointer at N33":
            36 - 35 == 1 and 620 + 4 == 624,
    }


# ------------------------------------------------------------------- unified at all levels (30 Oct): golden, torus

def golden_cosine():
    """The golden companion is the tick's negative cosine: E8 is Z[phi]^4 with phi = -(g + g^-1)."""
    x = sp.Symbol("x")
    I8 = np.eye(8, dtype=np.int64)
    B2 = np.array([[1, 1], [1, 0]], dtype=np.int64)
    g = cyclotomic.clocks()["g"]
    RB = spine.frame()[5]
    eta = g + spine.inverse(g)
    X = -eta
    Phi = I8 + g + spine.mpow(g, 4)
    char = lambda M: sp.Poly(sp.Matrix(M.tolist()).charpoly(x).as_expr(), x)
    cols = lambda idx: np.array([v for i in idx for v in (X @ RB[i], RB[i])], dtype=np.int64).T
    unimodular = lambda M: abs(round(np.linalg.det(M.astype(float)))) == 1
    rank = lambda M: np.linalg.matrix_rank(M.astype(float))
    idx = next(((a, b, c, d) for a in range(240) for b in range(a + 1, 240) if rank(cols((a, b))) == 4
                for c in range(b + 1, 240) if rank(cols((a, b, c))) == 6
                for d in range(c + 1, 240) if unimodular(cols((a, b, c, d)))), None)
    basis = cols(idx)
    binv = np.rint(np.linalg.inv(basis.astype(float))).astype(np.int64)
    Pg = [spine.mpow(g, j) for j in range(4)]
    x0 = RB[0]
    span = lambda y: np.array([Pg[j] @ x0 for j in range(4)] + [Pg[j] @ y for j in range(4)], dtype=np.int64).T
    pairs = [i for i, y in enumerate(RB) if unimodular(span(y))]
    _, lines = cyclotomic.residue()
    line0 = next(L for L in lines if cyclotomic.point(x0) in L)
    on_line = [i for i, y in enumerate(RB) if cyclotomic.point(y) in line0]
    return {
        "the tick's cosine g + g^-1 has minimal polynomial x^2 + x - 1 (the polynomial of 2 cos 72 degrees), so its "
        "negative X = -(g + g^-1) satisfies X^2 = X + I with characteristic polynomial (x^2 - x - 1)^4: the golden "
        "companion's polynomial, each of phi and 1 - phi with multiplicity 4; X = I - Phi for layer 27's "
        "Phi = 1 + g + g^4":
            not (eta @ eta + eta - I8).any() and (eta - eta[0, 0] * I8).any()
            and char(X) == sp.Poly((x ** 2 - x - 1) ** 4, x) and not (X @ X - X - I8).any()
            and np.array_equal(X, I8 - Phi),
        "E8 has a Z-basis of four roots x_i and their images X x_i, ordered (X x_i, x_i), in which X is four blocks "
        "B = [[1, 1], [1, 0]]: "
        "E8 is a free module of rank 4 over Z[phi] = Z[X], the golden companion acting on all of the lattice":
            idx is not None and np.array_equal(basis @ binv, I8)
            and np.array_equal(binv @ X @ basis, np.kron(np.eye(4, dtype=np.int64), B2)),
        "Z[g] = Z[zeta5] makes E8 a free module of rank 2: the Z-span of g^j x0 for one root x0 has rank 4, and "
        "{g^j x0, g^j y} is a Z-basis for 200 of the roots y, exactly those off the A4 + A4 of x0's residue line":
            rank(span(x0)[:, :4]) == 4 and len(pairs) == 200
            and sorted(set(range(240)) - set(pairs)) == on_line and len(on_line) == 40,
    }


def golden_galois():
    """The day conjugates the golden companion: G120 realizes Gal(Q(sqrt5)/Q) on the tick's cosine."""
    I8 = np.eye(8, dtype=np.int64)
    B2 = np.array([[1, 1], [1, 0]], dtype=np.int64)
    k = cyclotomic.clocks()
    g, d, c = k["g"], k["day"], k["c"]
    inv = spine.inverse
    X = -(g + inv(g))
    G = primes._matrix_group([c, d])
    conj = lambda W: W @ X @ inv(W)
    fix = [W for W in G if np.array_equal(conj(W), X)]
    flip = [W for W in G if np.array_equal(conj(W), I8 - X)]
    H = primes._matrix_group([g, d @ d])
    key = lambda M: tuple(M.flatten().tolist())
    J = np.array([[0, 1], [-1, 0]], dtype=np.int64)
    return {
        "the day conjugates the tick to its square, d g d^-1 = g^2, so it carries the cosine g + g^-1 to "
        "g^2 + g^-2 = -(g + g^-1) - I and X = -(g + g^-1) to I - X: the day acts on Z[phi] = Z[X] as the Galois "
        "conjugation phi -> 1 - phi = -1/phi":
            np.array_equal(d @ g @ inv(d), spine.mpow(g, 2))
            and np.array_equal(d @ (g + inv(g)) @ inv(d), -(g + inv(g)) - I8)
            and np.array_equal(d @ X @ inv(d), I8 - X),
        "c' commutes with X, so G120 = <c', d> acts on Z[X] through Gal(Q(sqrt5)/Q) = Z/2: 60 elements fix X and 60 "
        "carry it to I - X, and the kernel is <g, d^2>, the day's square conjugating the tick to its inverse":
            np.array_equal(c @ X @ inv(c), X) and len(G) == 120 and len(fix) == 60 and len(flip) == 60
            and {key(W) for W in fix} == {key(W) for W in H} and len(H) == 60
            and np.array_equal(d @ d @ g @ inv(d @ d), inv(g)),
        "the two roots of x^2 - x - 1 in the ring Z[X], X and I - X = Phi = I + g + g^4, are the two embeddings of Z[phi] "
        "into Z[X] (End(E8) has further roots, the conjugates s_i X s_i), and the quarter turn J = [[0, 1], [-1, 0]] in "
        "SL(2,Z) conjugates B to I - B: the embedding into Z[X] is unique up to the day":
            np.array_equal(J @ B2 @ np.rint(np.linalg.inv(J)).astype(np.int64), np.eye(2, dtype=np.int64) - B2)
            and round(np.linalg.det(J.astype(float))) == 1 and not ((I8 - X) @ (I8 - X) - (I8 - X) - I8).any()
            and np.array_equal(I8 - X, I8 + g + spine.mpow(g, 4)),
    }


def regular_cosines():
    """The cosines of the thirteen regular clocks, and which of them carry the golden companion."""
    x = sp.Symbol("x")
    I8 = np.eye(8, dtype=np.int64)
    g = cyclotomic.clocks()["g"]
    X = -(g + spine.inverse(g))
    Xv = sp.Matrix(X.flatten().tolist())
    reg = primes.regular()
    psi, charpolys, inside = {}, {}, {}
    for n, w in reg.items():
        eta = w + spine.inverse(w)
        psi[n] = sp.Poly(sp.minimal_polynomial(2 * sp.cos(2 * sp.pi / n), x), x)
        charpolys[n] = sp.Poly(sp.Matrix(eta.tolist()).charpoly(x).as_expr(), x) == psi[n] ** (8 // psi[n].degree())
        powers = [I8]
        for _ in range(psi[n].degree() - 1):
            powers.append(powers[-1] @ eta)
        sol = sp.linsolve((sp.Matrix([p.flatten().tolist() for p in powers]).T, Xv))
        inside[n] = None if sol == sp.EmptySet else tuple(next(iter(sol)))
    found = {n: s for n, s in inside.items() if s is not None}
    v, w10 = reg[20], reg[10]
    return {
        "the cosine w + w^-1 of the regular clock of order d has characteristic polynomial Psi_d^(8/deg Psi_d), Psi_d "
        "the minimal polynomial of 2 cos(2 pi/d): degree phi(d)/2 for d >= 3, so (x -+ 2)^8, (x + 1)^8, x^8, "
        "(x^2 + x - 1)^4, (x - 1)^8, (x^2 - 2)^4, (x^2 - x - 1)^4, (x^2 - 3)^4 and four quartics squared for "
        "d = 15, 20, 24, 30":
            all(charpolys.values()) and all(psi[n].degree() == primes._phi(n) // 2 for n in psi if n >= 3)
            and psi[5].as_expr() == x ** 2 + x - 1 and psi[10].as_expr() == x ** 2 - x - 1
            and psi[20].as_expr() == x ** 4 - 5 * x ** 2 + 5 and psi[24].as_expr() == x ** 4 - 4 * x ** 2 + 1,
        "the golden companion's polynomial x^2 - x - 1 is Psi_10 = Psi_5(-x): the regular clock of order 10, "
        "c'^3 = -g^3, has cosine Phi = 1 + g + g^4 and the tick has negative cosine X = 1 - Phi; the golden clock's "
        "cosine squares to Phi + 2, (v + v^-1)^2 - 2 = v^2 + v^-2 = Phi, as 2 cos 18 degrees squared is "
        "(5 + sqrt5)/2":
            np.array_equal(w10, -spine.mpow(g, 3)) and np.array_equal(w10 + spine.inverse(w10), I8 - X)
            and np.array_equal(spine.mpow(v, 2), w10)
            and np.array_equal(np.linalg.matrix_power(v + spine.inverse(v), 2) - 2 * I8, I8 - X),
        "X lies in the cosine ring Z[w + w^-1] exactly for the five regular orders divisible by 5, with integer "
        "coefficients: -eta (5), 1 - eta (10), 3 eta - eta^3 (15), 3 - eta^2 (20) and 1 + 3 eta - eta^3 (30); for "
        "the eight others it is not even in Q[w + w^-1], since Q(sqrt5) lies in Q(zeta_d) only when 5 | d":
            sorted(found) == [5, 10, 15, 20, 30]
            and found == {5: (0, -1), 10: (1, -1), 15: (0, 3, 0, -1), 20: (3, 0, -1, 0), 30: (1, 3, 0, -1)}
            and all(inside[n] is None for n in inside if n % 5),
    }


def torus_places():
    """The nine-torus at the four places: six of its nine squared frequencies are the band at the fixed momenta of the
    three prime clocks and at the principal circle's critical steps; the other three are at none of them."""
    B, Binv, C, Cinv, R, RB = spine.frame()
    k = cyclotomic.clocks()
    band = lambda x: 240 - np.cos(2 * np.pi * (R @ x)).sum()
    grad = lambda x: np.linalg.norm((np.sin(2 * np.pi * (R @ x))[:, None] * R).sum(axis=0))
    read = lambda xs: Counter((handover.stabiliser(R, x)[0], int(round(band(x)))) for x in xs if grad(x) < 1e-9)
    fam = {t: f for (_, t), f in _census().items()}
    eps = sorted({240 - v for v in _critical_values()} - {0})
    # on the line x = s omega_i the band is 240 - P_i(cos 2 pi s), P_i from the root counts on node i; the line's
    # stabilizer has rank 7, so the gradient lies along omega_i and the line's critical points are the band's
    c = sp.symbols("c")
    marks = [2, 3, 4, 6, 5, 4, 3, 2]
    P = [sum(m * sp.chebyshevt(abs(j), c) for j, m in Counter(int(v) for v in RB[:, i]).items()) for i in range(8)]
    vertex = {handover.stabiliser(R, B @ Cinv[:, i] / marks[i])[0]: 240 - sp.expand(P[i].subs(c, sp.cos(2 * sp.pi / marks[i])))
              for i in range(8)}
    turn = lambda i, r: float(sp.acos(r) / (2 * sp.pi)) * (B @ Cinv[:, i])
    off = {(i, r): (handover.stabiliser(R, turn(i, r))[0], 240 - P[i].subs(c, r), grad(turn(i, r)) < 1e-9)
           for i in (1, 2) for r in sp.roots(sp.Poly(sp.diff(P[i], c), c)) if r not in (0, sp.Rational(-1, 2))}
    torsion = {0, sp.Rational(1, 2), sp.Rational(-1, 2), sp.cos(2 * sp.pi / 5), sp.cos(4 * sp.pi / 5)}
    others = {(i, r) for i in range(8) for r in sp.roots(sp.Poly(sp.diff(P[i], c), c)) if abs(r) < 1 and r not in torsion}
    exact = {**vertex, **{t: e for t, e, _ in off.values()}, "E8": 0}
    close = all(abs(float(exact[t]) - (240 - f["lambda"])) < 1e-9 for t, f in fam.items())
    # the four places: the principal circle's critical steps and the fixed momenta of the half-turn, the sun and the tick
    rho, rs, _ = principal.weyl_vector()
    crit = [j for j in range(1, N) if grad(rs * j / N) < 1e-8]
    circle = {j: (handover.stabiliser(R, rs * j / N)[0], int(round(band(rs * j / N)))) for j in crit}
    half = read(np.array(y) @ B.T / 2 for y in itertools.product((0, 1), repeat=8))
    sun = read(places._fixed_momenta(spine.mpow(k["c"], 10), 81))
    tick = read(_tick_fixed_momenta()[1])
    at = list(circle.values()) + list(half) + list(sun) + list(tick)
    placed, types = {v for _, v in at} - {0}, {t for t, _ in at}
    return {
        "the nine squared frequencies are exact: at the vertex omega_i / m_i the band is 240 - sum_k m_k cos(2 pi k / m_i) "
        "for the root counts m_k on node i, giving 256, 252, 252, 251, 250, 248, 243 and 224 at D8, A8, A7 + A1, "
        "A5 + A2 + A1, A4 + A4, D5 + A3, E6 + A2 and E7 + A1; on the lines R omega_2 and R omega_3 it is "
        "240 - (64c^3 + 112c^2 + 64c) and 240 - (112c^4 + 112c^3 + 28c^2 - 12) in c = cos 2 pi s, critical off the "
        "torsion points at c = -2/3 and c = -1/4 (Niven), where it is 6800/27 (type A7) and 4025/16 (type A6 + A1), the "
        "only such points on the eight lines; the census's floats agree to 1e-9, and the nine square-free parts are distinct "
        "(nine_torus)":
            sp.expand(P[1]) == 64 * c ** 3 + 112 * c ** 2 + 64 * c and sp.expand(P[2]) == 112 * c ** 4 + 112 * c ** 3 + 28 * c ** 2 - 12
            and all(v.is_Rational for v in vertex.values())
            and vertex == {"D8": 256, "A8": 252, "A7+A1": 252, "A5+A2+A1": 251, "A4+A4": 250, "D5+A3": 248, "E6+A2": 243, "E7+A1": 224}
            and off == {(1, sp.Rational(-2, 3)): ("A7", sp.Rational(6800, 27), True), (2, sp.Rational(-1, 4)): ("A6+A1", sp.Rational(4025, 16), True)}
            and others == set(off) and close and sorted(set(exact.values()) - {0}) == eps and all(nine_torus().values()),
        "the principal circle's critical steps carry four of the nine: 256 at the half-turn 2160 (D8), 252 at 1440 and 2880 "
        "(A8), 248 at 1080 and 3240 (D5 + A3) and 250 at 864, 1728, 2592 and 3456 (A4 + A4), and the band is critical at "
        "no other nonzero step":
            circle == {2160: ("D8", 256), 1440: ("A8", 252), 2880: ("A8", 252), 1080: ("D5+A3", 248), 3240: ("D5+A3", 248),
                       864: ("A4+A4", 250), 1728: ("A4+A4", 250), 2592: ("A4+A4", 250), 3456: ("A4+A4", 250)}
            and min(grad(rs * j / N) for j in range(1, N) if j not in circle) > 1e-3,
        "the 256 half-periods carry two of the nine: 256 at the 135 of type D8 and 224 at the 120 of type E7 + A1, the whole "
        "census orbits of those types, and 0 at the origin; the half-turn 2160 is the half-period rho / 2, of type D8":
            half == Counter({("E8", 0): 1, ("D8", 256): 135, ("E7+A1", 224): 120})
            and (fam["D8"]["orbit"], fam["E7+A1"]["orbit"]) == (135, 120)
            and (rho % 2).tolist() == [0, 0, 1, 1, 0, 0, 1, 1] and handover.stabiliser(R, rs / 2)[0] == "D8",
        "the sun's 81 fixed momenta carry one of the nine, 243, at the 80 nonzero ones, of type E6 + A2; the tick's 25 carry "
        "250 at the 24 nonzero ones, of type A4 + A4; every one of these momenta is a critical point of the band":
            sun == Counter({("E8", 0): 1, ("E6+A2", 243): 80}) and tick == Counter({("E8", 0): 1, ("A4+A4", 250): 24}),
        "so six of the nine frequencies are placed, sqrt 224, 243, 248, 250, 252 and 256, through six of the eleven census "
        "families (D8, A8, D5 + A3, A4 + A4, E6 + A2, E7 + A1), with E8 the seventh type present, at the band's minimum 0; "
        "the three others, sqrt 251, sqrt(4025/16) and "
        "sqrt(6800/27), of types A5 + A2 + A1, A6 + A1 and A7, are at no fixed momentum of a prime clock and at no critical "
        "step of the principal circle, and the A7 + A1 family's 252 is placed only through A8":
            placed == {224, 243, 248, 250, 252, 256}
            and [e for e in eps if e not in placed] == [251, sp.Rational(4025, 16), sp.Rational(6800, 27)]
            and types == {"E8", "D8", "A8", "D5+A3", "A4+A4", "E6+A2", "E7+A1"} and len(types) == 7 == len(fam) - 4
            and set(fam) - types == {"A7+A1", "A5+A2+A1", "A6+A1", "A7"},
    }


def notes_1441():
    """The sibling's MODEL editions of 14:31 and 14:41, the separate model's provenance verification (14:25) and the hub's
    Canon_Position (14:20), replayed as arithmetic."""
    S = spine.subgroup
    order = lambda s: N // gcd(s, N)
    crit = [864, 1080, 1440, 1728, 2160, 2592, 2880, 3240, 3456]
    M = np.array(carrier.signless_incidence(), dtype=np.int64)
    R5 = np.roll(np.eye(5, dtype=np.int64), 1, axis=0)
    P = R5 + np.linalg.matrix_power(R5, 4) - np.linalg.matrix_power(R5, 2) - np.linalg.matrix_power(R5, 3)
    I5, J5, u = np.eye(5, dtype=np.int64), np.ones((5, 5), dtype=np.int64), np.ones(5, dtype=np.int64)
    zero_sum = [I5[i] - I5[0] for i in range(1, 5)]                      # a basis of the sum-zero four
    return {
        "the sibling's two readings of 120: lcm(30, 24, 20) = 120 is the order of the seam <36>, while the step 120 has "
        "order 36 (it generates the address subgroup); and the kernel of x -> 9x is <480>, of order 9, while the multiples "
        "of 9 are <9>, of order 480, the kernel of x -> x mod 9":
            lcm(30, 24, 20) == 120 == len(S(36)) and order(120) == 36 == len(S(120))
            and {x for x in range(N) if 9 * x % N == 0} == S(480) and len(S(480)) == 9
            and {x for x in range(N) if x % 9 == 0} == S(9) and len(S(9)) == 480,
        "the address subgroup <120> has order 36 and the principal subgroup <144> order 30; they meet in <720>, the unique "
        "subgroup of order 6; of the nine critical steps five lie in the address subgroup, seven in the principal subgroup "
        "and three in both (1440, 2160, 2880)":
            (len(S(120)), len(S(144))) == (36, 30) and S(120) & S(144) == S(720) and len(S(720)) == 6
            and [d for d in spine.divisors() if len(S(d)) == 6] == [720]
            and ([c for c in crit if c % 120 == 0], [c for c in crit if c % 144 == 0], [c for c in crit if c % 720 == 0])
            == ([1080, 1440, 2160, 2880, 3240], [864, 1440, 1728, 2160, 2592, 2880, 3456], [1440, 2160, 2880]),
        "the bridge's two splits: the signless Gram M M^T = 3I + J acts by 3 on the sum-zero four and by 8 on the all-ones "
        "line, and the Gauss square G5^2 = 5I - J by 5 and 0; both pairs add to 8, as M M^T + G5^2 = 8I":
            np.array_equal(M @ M.T, 3 * I5 + J5) and np.array_equal(P @ P, 5 * I5 - J5)
            and all(np.array_equal(M @ M.T @ v, 3 * v) and np.array_equal(P @ P @ v, 5 * v) for v in zero_sum)
            and np.array_equal(M @ M.T @ u, 8 * u) and not (P @ P @ u).any() and 3 + 5 == 8 + 0 == 8
            and np.array_equal(M @ M.T + P @ P, 8 * I5),
        "the receipts: 3755 - 5 = 3750 and 3710 - 5 = 3705 (the five tabs START, CLAIMS, SOURCES, OPEN, STATUS), so each N34 "
        "workbook is five sheets ahead of the publication pointer, which still names N33; the observer reconciliation takes "
        "4166 + 4 = 4170 artifacts and 610 + 10 = 620 relationships; the archive's 57 files have 56 hashes and the zip's 17 "
        "files 16, one manifest unhashed each; the workbooks' 31613408 + 30890062 = 62503470 bytes":
            3755 - 5 == 3750 and 3710 - 5 == 3705 and 4166 + 4 == 4170 and 610 + 10 == 620 and 57 - 56 == 1 == 17 - 16
            and 31613408 + 30890062 == 62503470,
        "readings, not joins: on the circle 4170 has order 144 and 620 order 216 (the Coxeter and golden orders), and "
        "144606784 and 224 have order 135; the 49-tuple's offsets 0, 2, 6 translated to 23 give 23, 25, 29, and 25 is "
        "composite: admissibility of the tuple says nothing about which translates are prime":
            (order(4170), order(620), order(144606784), order(224)) == (144, 216, 135, 135)
            and [23 + t for t in (0, 2, 6)] == [23, 25, 29] and 25 == 5 ** 2,
    }


# rows for docs/LEDGER.md: (join, the statement, the unified statement, status, layer)
LEDGER_ROWS = [
    ("the K5 incidences", "B B^T = 5I - J; signless + ordinary = 8I", "the Coxeter identities of A4 and D5: the carrier's spectrum {0, 3, 8} is {0, h(D5) - h(A4), h(D5)}", T, "23"),
    ("Petersen as roots", "A = J + I - M^T M", "the orthogonality graph of the ten roots e_i + e_j, whose Gram matrix is M^T M", T, "23"),
    ("the selected six-port (canon)", "moments 1, 242, 58691, 14259954; triangle-cycle heat t^-7 with 1/(22394880000000 pi^4)", "the oriented triangle 0-1-2 of K5 lifted to the lattice; its Fourier transform -8i sin(x/2) sin(y/2) sin(z/2) vanishes to third order, which gives the exponent and the coefficient", T, "23"),
    ("L0 (canon)", "A4 + A4' of index 5; root cosets 40/50/50/50/50; folded spectrum 0, 250^4", "replayed; the tick's 25 fixed momenta carry 0 and 250 (24 times), and E8 / L0 is five of them", T, "11, 23"),
    ("h81 (canon)", "chain counts 16/32/24/8/1; spectrum 0, 2^8, 4^24, 6^32, 8^16; dh + hd = I - P0, h^2 = 0, rank 40, norm 1/sqrt 2", "replayed on the 81-cell complex; its vertices are four qubits with Laplacian 4 - sum X_i; adjacent resistance 15/32", T, "21, 23"),
    ("Hodge 70 (canon)", "35 + 35 halves interchanged by a Weyl reflection", "replayed; the clocks of determinant 1 keep the halves", T, "23"),
    ("primary split (PRIMARY_SPLIT, DOUBLING_PARTS)", "3105 + 2080 + 3456 = 1; doubling kills the 2-part and returns the time and 27 parts after 4 and 18", "replayed; 36 = lcm(4, 18) returns the odd parts, and no doubling count returns all three", T, "20, 23"),
    ("the atlas (GOLDEN_ATLAS, ATLAS_801, ATLAS_CYCLE)", "addresses meet or miss the tick; 18 falls to the seam in two contractions; 16 does not move", "the atlas is the quotient Z/36, and the bit does not descend to it (96 meets and 24 misses at every address); 18 falls in one contraction; 16 is on the 6-cycle", T, "23"),
    ("the 801 matrix (AIR_801)", "order 24 in GL(2,5), projective order 6", "replayed: a Singer cycle mod 5", T, "23"),
    ("the bivector (CLOSURE_46)", "a change of pair scales a ^ b by its determinant; a cone of dimension 7; rank 6, kernel 4", "the native port W_AS: Lambda^2 ker M -> cycles of K5, rank 6 and kernel 4; the cone has dimension 7 = 10 - 3", T, "4, 23"),
    ("K6 and the carrier (synthesis)", "a 15-edge K6 carrier", "the 15 atoms are the bonds of K6 = K5 coned; D is the spoke-rim block of the line graph of K6, and KG(6,2) restricts to Petersen on the rim", T, "23"),
    ("K5-P9 (synthesis)", "paired regular-cyclic signless + signed response of rank 9 with a 1D residual line", "replayed: the residual line is near minus far, the C5-fixed line of ker M; the order orientation gives rank 7", T, "23"),
    ("band expansion (synthesis)", "30|k|^2 - (3/2)|k|^4 + (1/24)|k|^6", "replayed: the roots are a 7-design and not an 8-design", T, "23"),
    ("L11 (synthesis)", "an order-11, degree-5 operator L11(n, E_n) with 72 coefficients", "not a recurrence for W_n or E_n: full column rank 72 from n <= 90, and 84 < 85", OB, "14, 23"),
    ("801 orbits (joined paper)", "1 + 3 + 3 + 6 + 6 + 6 + 6 on 31 points", "replayed through the symmetric square on PG(2,5)", T, "23"),
    ("collar (synthesis)", "positivity up to E = 224 by mediant monotonicity", "not replayed; the collar stays open here", RP, "23"),
    ("the coil (SIBLING_540, CANON_CYCLE, COIL_DEEP)", "540 = 20 x 27 = 30 x 18 = 15 x 36; the smear step 184 generates 540 points; the pada unit is the part the tick cannot see", "the tick, the observer and the nakshatra generate <8> (index 8); inside it the tick misses exactly <40> (108 points) and meets the other 432; the cosets of <40> carry the time coordinates 0, 3, 1, 4, 2; x23 has order 36", T, "23"),
    ("the nakshatra map (NAKSHATRA_MAP)", "the 27 multiples of 160, coordinate 25k mod 27, period 9 on the atlas", "replayed; 'the address 16 meets as an address' is corrected by the note's own pair: 16 and 160 share address 16, and 160 misses", T, "23"),
    ("the golden family (GOLDEN_SYM, GOLDEN_PARENT, GOLDEN_HELIX, GOLDEN_MOVE)", "B^n = F_n B + F_(n-1) I; returns 6, 20, 12, 72, 48, 24; the first eight traces meet; 216 k misses iff 5 | F_k (to k = 40)", "replayed for every n: L_n mod 5 runs 2, 1, 3, 4, so no trace of a golden power misses the tick, and 5 | F_k iff 5 | k; the helix and 'doubling = x7' hold exactly where 5x = 0, the five tick points", T, "23"),
    ("the address bit (ADDRESS_TICK, BUILT_DOTS)", "a residue mod 36 does not meet or miss; x = a + 36((t - a) mod 5)", "adopted: the sibling now proves the 22:08 correction (36 = 1 mod 5); CANON_CYCLE, COIL_DEEP, GOLDEN_HELIX, NAKSHATRA_MAP, DEEP_H, LEVEL_DOTS and the 22:45 paper still used the address bit, and their own pairs 155/11, 160/16, 138/30 correct it", T, "23"),
    ("the shift and the doubling (MORE_DOTS; hub I_STATUS)", "the shift by one tick commutes with doubling", "corrected: D T = T^2 D = T^-1 D and D T != T D, while D^2 T = T D^2 (the hub's verifier agrees)", T, "23"),
    ("the K6 carrier and S5 (hub I_STATUS, REVIEW_CONFLICTS_I)", "C5 agreement does not prove an S5 identification; transposition characters 7 vs 3", "replayed: the cone S5, which is exactly the set of permutations of K6 that keep D, makes atoms and bonds one S5-set; the transitive S5 = PGL(2,5) gives another module (one orbit, character 3); the two meet in F20 = AGL(1,5)", T, "23"),
    ("MPKG and L4 (MPKG_L4, LEVEL_DOTS)", "four 6 x 6 blocks of order 5 with trace 1; levels 0, 6, 12, 18", "such a block is the C5 rotation of the cone's six sites up to similarity over Q (eigenvalues 1, 1 and the primitive fifth roots); doubling sends the levels to 0, 12, 24, 0; [[-1, 4], [6, 1]]^2 = 25 I", T, "23"),
    ("the 31-point clock (MORE_DOTS; hub I_STATUS)", "its characteristic polynomial was not recomputed; a rank bound 29 stays conditional", "for P31, the symmetric square's permutation: (x - 1)(x^3 - 1)^2 (x^6 - 1)^4, order 6, rank(P31 - I) = 24; the rank 29 belongs to the hub's order-30 clock on Z/31 and stays conditional", T, "23"),
    ("the four-cube faces (ADDRESS_TICK, BUILT_DOTS)", "16 + 32 + 24 + 8 + 1 = 81 words in {0, 1, *}", "replayed; the Hodge multiplicities 1, 8, 24, 32, 16 are the face counts read backwards (2k has C(4, k) 2^k = the number of (4 - k)-cells)", T, "23"),
    ("release H (RELEASE_H_RECEIPT, DEEP_H, CANON_JOIN)", "certificate integers; det T6 = 155, det Gram = 24025", "readings in layer 22; 155^2 = 24025 holds for any T with det 155, one being (2I - C) + [5]; the canon's T6 is not opened, and the archive's 5247252 bytes match Drive (SHA-256 not recomputed)", RP, "22, 23"),
    ("the grain (SUN_GRAIN, GRAIN_SPLIT, CLOCK_SPLIT, SEAM_HALF)", "<72> = golden orbit x sun; time reads the golden index, the 27-clock the sun", "replayed: a direct product of 60 points, index 9 in the coil; doubling doubles the golden index and inverts the sun; the other half of the seam falls in after one doubling", T, "23"),
    ("the shift law (SHIFT_LAW)", "D T = T^2 D for every shift; inversion only for the sun", "replayed: doubling inverts exactly the shifts with 3s = 0 (0, 1440, 2880 on the circle; 0, 12, 24 on the atlas, the 23:03 case)", T, "23"),
    ("the golden family, continued (DOUBLE_CHILD, KARMA_COMM, BASS_STOP, GOLDEN_REST)", "F(2n) = F(n) L(n) to n = 16; det [K, B^n] = -29 F(n)^2 to n = 10; B^10 is not an involution", "for every n, from the parent rule; mod 5, where B has order 20 like 216, B^10 = -I has order 2 like 2160", T, "23"),
    ("the vortex (VORTEX_JOIN, VORTEX_OFF, VORTEX_LIFT, LOOP_ALL)", "doubling mod 9 runs 2, 4, 8, 7, 5, 1; the 216 loops in 9 layers of 24", "replayed; the vortex reads the atlas (9 | 36) and is the 27-clock without the sun; 'order 1440, the sun' names the dual step: 3 has order 1440, the sun has order 3", T, "23"),
    ("the clock tower (ALL_RANKS)", "circle > seam > grain > golden orbit > ticks > observer > sun", "corrected: a chain down to the golden orbit; then the ticks and the observer are two subgroups meeting in 0, and the sun lies in the grain", T, "23"),
    ("doubling (DOUBLE_SPLIT, TWO_DOUBLES)", "nilpotent on the 2-part, a 36-cycle on the odd part; the atlas is that length", "replayed; the circle's doubling period 36 and the atlas modulus 36 are the same integer, not the same cycle (on the atlas the period is 6)", T, "23"),
    ("the 2-part of 216 (GOLDEN_EVERYWHERE)", "3456, the fourth tick, is the 2-part of one step", "corrected: 216 = 1080 (2-part) + 3456 (time part); the hub's release J agrees", T, "23"),
    ("BassForge and the 38-fiber (BASS_STOP, BASS_38, BASS_DEEP)", "GB-018 unformable; 38 = 7 x 4 + 4 x 2 + 2; rates 1/9, -1/3, 2/3, 0", "the arithmetic holds; the 117 checks, the view and the retraction are not stored here", RP, "23"),
    ("ticks and misses (TICK_MISS, COORD_LAW, FOUR_MISS, MISS_COSET, TWO_AGREE)", "the circle is the tick subgroup times the miss subgroup; four misses per loop", "replayed: Z/4320 = <864> + <5>; a point misses iff its tick part is 0; the four misses of a golden loop are an observer coset; two doublings and 864 copies agree exactly on <216>", T, "23"),
    ("doubling on the clocks (TICK_CYCLE, OBS_FALLS, NAKSHATRA_SPLIT, THREE_DOUBLES, GOLDEN_FATE)", "ticks cycle, the observer falls, the nakshatra splits 18 + 6 + 2 + 1", "replayed; the nakshatra clock maps onto the coil's 27 golden cosets with the same cycles, and doubling sorts the golden orbit by the tick bit", T, "23"),
    ("the relations receipt's corrections (23:50)", "the clock chain; the vortex points; the 36-cycle; p1; the fifth commutator", "agreed: two match the 23:44 corrections, and the other three are replayed (216 -> 432 moves; orbit lengths 1, 2, 4, 6, 12, 18, 36; [K, B^5] has entries divisible by 5, det by 25); the sibling adopted all five", T, "23"),
    ("towers (POWER_TOWER, SALINA_CONG, TOWERS, FROZEN_CLOCKS)", "threes freeze at 27, twos at 736, fives do not; mod 12: 3, 4, 5", "corrected: the fives freeze too, at 245 from height 3 (this layer had repeated 'do not' at 00:15 after checking one step); 736, 27 and 245 generate the points that are 0 on the 2-, 27- and time clocks", T, "23"),
    ("modules 8-11 (Locked Memory synthesis, 00:06)", "T12 non-semisimple; dA = 2 dx dy/(1 + r^2)^2; reader 2, 121, 241, 12; 57840", "replayed from the stated formulas; JOIN_MODULES's missing time-rotor map is the join kappa = 4x mod 5 of layer 22", T, "23"),
    ("N = 25 annihilator (Locked Memory synthesis)", "a Stieltjes-Jacobi annihilator of order 25 on W_0..W_50", "not an annihilator: the 26 x 26 Hankel determinant of W_0..W_50 is positive; a depth-25 Jacobi fit is not a recurrence", OB, "23"),
    ("the eight-root frame (ONE_MACHINE_29, FRAME_WALKS, DEEP_COURT)", "Gram I + J, det 9, index 3; quotient generator of squared length 8; no ninth root", "replayed: a maximal 9-clique of the lattice graph; the only vector meeting all eight has squared length 8/9; six times the duals is 6R - 2q; its six-point faces are six-ports", T, "23"),
    ("the symbol and the root graph (ONE_MACHINE_29, FRAME_WALKS)", "the D8 + half-spin formula; 240 and -16; closed walks 1, 0, 56, 1512, 62160", "replayed; the root graph's spectrum is 56, 28^8, 8^35, (-2)^112, (-4)^84 (the separate script's list, of trace -240, is not it); the collar witness has dispersion 220.635", T, "23"),
    ("protection (CLOSURE_092, LEVELS)", "a protected line cannot also be the coupling; the commutator court; the channel law", "replayed: [diag(1, 0), X] = 0 iff X has no coupling; rank 8 -> 9 with the anchor and Gram det 176173056; (1440 - 5z) G_c - z G_u = 6 with g0 cancelling", T, "23"),
    ("the grain, twice (GRAIN_SPLIT 00:19, OBS_SUN)", "the five ticks times the twelve multiples of 360, which are the observer times the sun", "replayed: the observer and the sun are the miss set's unique subgroups of orders 4 and 3", T, "23"),
    ("chart classes and the field prime (ONE_MACHINE_29, LEVELS)", "95, 98, 101 one class mod 30; the field prime meets the circle in 240", "corrected: one class mod 3 (mod 30 they are 5, 8, 11); 241 is prime to 4320, and 240 = 241 - 1 meets it in 240", T, "23"),
    ("the sibling's paper ONE_MACHINE_29 (00:20)", "the best closed model of 29 Oct; carrier unchanged; sigma in (231.7438, 231.7439); a rational Gauss-Manin matrix missing", "replayed where stated (carrier, ports, frame, symbol, walks, clocks); the sigma interval, the collar endpoints and the typeset .typ source were not", RP, "23"),
    ("the edge tick (CYCLE_TICK, CUT_TICK, DEEP36_LOOP)", "(x - 1)^2 Phi_5 on the cycles, Phi_5 on the cuts; the signed edge Gram squares to 5 times itself", "replayed: the second compound of the vertex 5-cycle; its fixed plane is the rotor plane, and on the cuts it has the time clock's polynomial (the join kappa = 4x mod 5)", T, "23"),
    ("the six-port moments (FOUR_ITEMS, REPAIR_AUDIT)", "contrast 241 and 183; uniform 235 and 495 once the factor 6 is restored", "replayed: F_k = E_k - E_(k+1)/240 because W(E8) is transitive on the roots; contrast E_(k+1)/240, uniform 6 E_k - 5 E_(k+1)/240; without the 6 the line gives -965", T, "23"),
    ("the script audits (FOUR_ITEMS, REPAIR_AUDIT, PASS2, MASTER_LEDGER, DEEP36_LOOP)", "4805 not a minor; 3/65 against 3/80; 74557/432 and -69373; Hessian 6.986, not 5.0708; two factorizations wrong", "replayed: 4805 = 24025/5 is the Gram over 5; the collar fractions are two different exact numbers; the shifted coefficient is -69373; the tangent Hessian is positive; the corrected squarefree parts are 3985 and 318; the collar stays open", T, "23"),
    ("the splits receipt's corrections (00:49)", "the tower of fives; 215 other loops; 4300 disagreement points; entry after two doublings", "replayed: all five hold", T, "23"),
    ("the spectral triple (J7)", "Witten index -5; moments 15, 40, 200", "joined: the triple's D squares to the carrier, and ker D^2 is ker M on the edges", T, "2, 9, 23"),
    ("the readout (J6)", "the hidden controllable sector is P5 + P5", "joined: the readout is the triple's D^2 in first-order form, and its hidden sector is the native source's space", T, "5, 9, 23"),
    ("the product geometry and FLRW (J10)", "heat coefficients 60, 160 m^2, 400 m^4; sectors a^-6 and a^-3", "joined conditionally: the coefficients are 4 Tr D^0, 4 Tr D^2 and 2 Tr D^4 for any M4, while G and Lambda_cc need f, L and m; the kernel sector, the datum's 2, scales exactly as a^-6", gates.CONDITIONAL, "6, 7, 23"),
    ("the surface (J5)", "RP^2 on the six icosahedral axes, 1-skeleton K6", "joined: on the projective line over F5 the hemi-icosahedron and its complement are the two PSL(2,5)-orbits of triangles, swapped by PGL(2,5), with links the pentagram and the pentagon", T, "3, 23"),
    ("the four-cube and the cuts", "four qubits, Laplacian 4 - sum X_i", "joined: the sixteen vertices are the sixteen cuts of K5 over F2, and a cube edge adds one vertex star", T, "23"),
    ("the critical census and the tick (layer 16)", "11 families, 243600 points, Morse sum 0", "joined: the tick's 25 fixed momenta are critical points, the minimum and 24 of the A4 + A4 family at eps 250; the 11 critical values are the recurrence's in-band roots", T, "16, 23"),
    ("the nine-torus (layer 18)", "square-free parts 14, 3, 62, 10, 251, 161, 51, 7, 1", "joined to the census: the nine frequencies are independent over Q and their flow is dense on T^9", T, "18, 23"),
    ("sound and light (layer 17)", "Curl = *d1 with helicities +-sqrt5; sound = cuts, light = cycles", "joined to the edges, the cycles, A4, the carrier's Hodge block and the triple (M M^T + B B^T = 8I)", T, "17, 23"),
    ("binding (layer 12)", "commutant 59; the anomaly-free 5 + 10", "joined to the triple (the commutant) and to the source (Lambda^2 ker D)", T, "12, 23"),
    ("calibration (layer 13)", "t = tau u; the Salina and Prema courts vanish", "joined to the readout by the intertwiner S U(u) = U_tau(tau u) S", T, "13, 23"),
    ("time from the circle (layer 13)", "countermodel A: tau and 2 tau give the same records", "an obstruction: no internal number, the circle's ticks included, binds physical time", OB, "13, 23"),
    ("the literal operands (layer 10)", "SHA-256 73e07429...; W_p exact; the adapters differ by a commutant element", "joined to the source by U, a W_p-isometry commuting with the C5 rotation", T, "10, 23"),
    ("the spectral measures (layer 15)", "M_0..M_50; Gauss and Lobatto envelopes", "joined to the moments by the Hausdorff test on [0, 256]", T, "15, 23"),
    ("the golden clock", "B mod 5 and v in W(E8), both of order 20", "joined by B^k -> v^k with B^4 -> the tick: a selected isomorphism of two cyclic groups", SR, "23"),
    ("the root graph (ROOT_SPECTRUM, GRAM_28, ORTHOGONAL_126, Canon K)", "classes 56, 126, 56, 1; intersection matrix; Gram = 60 P_28; W_3 and W_4 from pair sums", "replayed and joined: an association scheme with eigenvalues 56, 28, 8, -2, -4; the orthogonal 126 are E7, frame 36 P = 2 h(E7) P; W_4 = sum of squared pair-sum multiplicities", T, "23"),
    ("the 4-simplex (TRIANGLES, TETRAHEDRA, ALL_GRADES, FIVE_CLOCK_COPIES)", "ranks 4, 6, 4, 1; the rotation's polynomial on every grade", "replayed and joined: every grade is copies of the five-clock's regular representation, and the body is fixed", T, "23"),
    ("the tick split (TICK_SPLIT, GOLDEN_EIGENSPACES, GOLDEN_MATCH)", "pentagon and pentagram fixed; golden spaces 4 + 4, each 2 cycles + 2 cuts", "replayed; joined to the golden companion: -(T + T^-1) satisfies X^2 = X + I on the golden part", T, "23"),
    ("the frame's faces (INDEX_VECTOR, SIBLING_AGREEMENT)", "index vector classes 8, 28, 56, 56, 56, 28, 8; a face has three extensions", "replayed: each face has six common neighbours, a triangular prism, and lies in exactly two maximal 9-cliques", T, "23"),
    ("the monopole chain (GOLDEN_GRAVITY)", "no subgroup of order 120, 60, 30 or 10 contains a nonzero tick", "corrected: on the circle each of them contains the ticks, since 5 divides its order", T, "23"),
    ("the cumulant 495 (CUMULANT_183)", "183 + 6 x (56 - 4) with 4 the cut rank", "corrected reading: the 4 is the face's other four sites (56 common neighbours per pair, four inside)", T, "23"),
    ("the square-free certificate (HESSIAN_RECOMPUTE)", "the 256 subset products are distinct and square-free", "corrected: their square-free parts are distinct (the exponent matrix is invertible over F2), which is what independence needs; 196 products are not square-free", T, "23"),
    ("release K (hub, cutoff 01:06; Canon K, 01:49)", "71 Grand All Dots assertions; carry clock 36 x 120; observability descent; root-pair proof", "the bridges are replayed; the 71 assertions, the evidence package and the four workbook copies are recorded, not rerun", RP, "23"),
    ("the separate model's unified build (01:28)", "104 new check groups; three source corrections (CHERN_SPLIT twice, SPECTRA)", "the corrections are replayed; the build is not opened", RP, "23"),
    ("the 801 matrix and PG(2,5) (AIR_801; 02:20)", "a Singer cycle of order 24; orbits 1 + 3 + 3 + 6 + 6 + 6 + 6 on 31 points", "joined: in PGL(2,5) it lies outside PSL(2,5) and swaps the two triangulations; the Veronese conic carries the six axes, the 15 exterior points are the surface's edges and the 10 interior points its faces (perspectors); its orbits are conic 6, exterior 3 + 6 + 6, interior 1 + 3 + 6", T, "23"),
    ("the half-periods and the census", "1 + 120 + 135 half-period modes; GKSL rates 0, 224, 256", "joined: the 256 half-periods are the census's critical points of types E8, E7 + A1 and D8, whole orbits", T, "23"),
    ("the walk convolution (Canon K, W5/W6)", "c2 support 9361, c3 support 131041, c3(root) = 5253, c4(root) = 574224", "replayed: W_5 = 240 x 574224 and W_6 = sum c3^2 are layer 3's returns", T, "3, 23"),
    ("the 160 x 27 clock and the sidebands (WALKS_CLOCK, LEVELS_160, SUN_MOON_ORDERS; the observer completion)", "j = 2241 (j mod 160) + 2080 (j mod 27); t = 105 t8 + 40 t3 + 96 t5 mod 120", "joined: the sideband lift from the atlas to the circle; the tick sits in 2241 = 3105 + 3456 and the 27-clock is blind to it; three sensors of largest alphabet 32 are optimal", T, "23"),
    ("the joint observer (the hub's observer completion)", "wedge rank 7; a1, a2, b1 complete it to rank 10", "joined: the source to the readout, injective on a1 w12 != 0 with an explicit inverse; the rank-7 locus is a cone (Pluecker), not a linear 7-space", T, "23"),
    ("the six-site torsion (SEVEN_PAIRS, TORSION_FIVE, INVERSE_TWO)", "35366 G0 - 183 G1 = 350510 J; Smith form diag(1, 1, 1, 1, 1, 5); 57 masks", "replayed; the 5 is the 5 in 240, through the uniform moments", T, "22, 23"),
    ("the golden port (GOLDEN_PORT, PORT_FORMULA, CANON_BOARD, CAYLEY)", "W_p = [2/5] + 4I + (2/5)J - 2(R + R^-1); golden pair of product 20", "joined to the golden companion: on the contrast the block is 4I + 2X with X^2 = X + I; the canon's (5 +- sqrt5)/10 are the pentagon Laplacian's pseudo-inverse", T, "4, 23"),
    ("the census stabilizers and the class at 250 (CENSUS_STABILIZERS, ENERGY_250, CENSUS_CUBE)", "orbits 1 to 135, alternating sum 0; 14400 = 10 x 1440, 8640 = 10 x 864; det (-25)^4", "replayed: the stabilizers are the Weyl groups of the extended diagram's subsystems; joined: at the 24 A4 + A4 momenta the Hessian is -5 times a golden companion (det 5^8); corrected: 24 of the 25 momenta sit at 250, the 25th is the minimum", T, "16, 23"),
    ("the five-site charges (ALPHA_JOIN, CHARGE_SHELL, HYPERCHARGE, CUT, KERNEL, TRIPLET)", "Q = Y + T3; even and odd shells 16/3; sum Y^2 = 5/6", "joined as a dot: the shells are the simplex's even and odd faces, the hypercharge anomaly cancels on B4's 5 + 10, Y acts in the dark U(5) (a selection), and B1 forbids an atom-diagonal charge (OBSTRUCTION)", T, "12, 23"),
    ("the fine-structure board (BOARD_A, CANON_BOARD, ALPHA_JOIN)", "a = 0.0072973525664; r_2 = a/(2 pi); c = 1/(128 pi alpha)", "not joined: the digits invert to about 137.036 and are put in by hand; no e, hbar, c or length is stored", gates.UNFORMED, "23"),
    ("the frame's two cliques (CHECK_0154)", "no clique of nine roots; a face has three common neighbours, not a triangle", "both hold, in two graphs: the root graph's maximal 8-clique, and the lattice graph's 9-clique with the origin, all 84 of whose faces are prisms", T, "23"),
    ("the rotor firewall and the Bargmann repair (Canon K)", "C6 against C5 + I1; tr = 1 + i for raw dyads, (1 + i)/4 normalized", "replayed: every intertwiner has rank 1; the phase pi/4 is half the solid angle of the Pauli octant", T, "23"),
    ("releases K+ADDENDUM2 and K+ADDENDUM3 (hub, 02:31 and 02:41)", "W5/W6, the 160/27 clock, Bargmann, the rotor firewall, the joint observer, the sidebands, the sensor optimum, the anti-alias court", "every stated bridge is replayed; the verifiers and evidence zips are recorded, not run", RP, "23"),
    ("the critical value 224 (HALFPERIOD)", "224 not recomputed, not a certified critical value", "corrected: at x = r0/2 every r.x is in Z/2, so the gradient vanishes; eps = 240 - (128 - 112) = 224 exactly, with Hessian 12 P' - 52 P (index 1, nondegenerate): the E7 + A1 saddle; the collar near 224 stays open", T, "16, 23"),
    ("every pair of levels (layer 23)", "join all dots", "the six levels are joined pairwise by maps: number-lattice by the tick on the half-periods, number-operator by the tick-equivariant GKSL semigroup, number-physics by the tick on light, symmetry-physics by the golden companion and the affine group on light and by S5 on 5 + 10", T, "23"),
    ("no two maps (layer 23)", "join all dots", "every dot but the product geometry and FLRW lies on three maps, and removing any two maps leaves the diagram connected except for cutting off those conditional dots", T, "23"),
    ("the outer automorphism of S6", "the cone S5 and PGL(2,5) give different carrier modules", "joined: S6 on its six synthematic totals is outer and carries the cone's S5 onto PGL(2,5)", T, "23"),
    ("the tick on light", "light is the cycle space, helicities +-sqrt5", "joined: the edge tick commutes with d0 and Curl; one fixed line and a golden plane on each helicity (144 and 72 degrees); B -> (I + Curl)/2; x -> ax + b multiplies Curl by (a/5)", T, "17, 23"),
    ("the tick on the half-periods", "51 five-cycles on the nonzero half-periods", "joined: g fixes only 0 mod 2 Lambda and keeps the band on each orbit, so e^-tL is tick-equivariant", T, "22, 23"),
    ("the Hodge star mod 2", "Lambda^4 R^8 = 35 + 35", "joined: e_S = e_T mod 2 Lambda exactly for Hodge-dual four-sets, onto 35 D8 half-periods", T, "23"),
    ("the memory clock (layer 3)", "order-90 quotient of a 125-state operator", "joined by selection: one circle step is one memory step; its 9- and 10-cycles read the vortex and the time coordinate", SR, "3, 23"),
    ("no bridge (layer 23)", "join all dots", "every dot has at least two maps, and no single map holds the diagram together", T, "23"),
    ("every level (layer 23)", "join all dots at every level", f"{len(DOTS)} dots on six levels, number to physics: every layer 1-28 has a dot, each level is joined inside and to every other level, and THEOREM joins alone reach all but the product geometry, FLRW and the memory clock", T, "23"),
    ("SHELLS, CONVOLUTION, SEVENTH (08:43-08:58)", "two roots land on 9361 points in five shells; a root is a sum of three, four and six roots in 5253, 574224 and 9734696160 ways", "replayed: shells 240/56/14/2/1 deep on 1/240/2160/6720/240 points, and W_(k+1)/240 by transitivity", T, "23"),
    ("MEMORY, FOURTH (09:16, 09:19)", "four-step walks between roots 1260720, 574224, 253512, 107508, 43936 by inner product, with their fourth moments", "replayed against all 240 partners: the walks of length 0 to 4 depend only on the inner product, and the five fourth moments hold", T, "23"),
    ("MOMENTS, DEGREE (08:37, 08:40)", "241, 183, 235, 495 are walk moments; 183 = 240 - 56 - 1 and 495 = 183 + 6(56 - 4), the 4 the cut rank and the 6 the cycles", "replayed, with a correction: in G0 = X^T X the 4 counts the clique's other sites next to two sites and the 6 the port's sites; the cut rank and the cycle count are the same integers, not the same counts", T, "23, 24"),
    ("LEAK, RANK (08:50, 08:52)", "Hessian trace 480 - 2E; residual eigenvalues 55487966/183 and 131183830/99; nonzero Hankel windows, at least three frequencies", "replayed; both sector measures have positive Hankel determinants through size 11, so the six sites' Krylov space grows by 6 at every order through 10", T, "23"),
    ("TICK, COXETER (09:11, 09:15)", "the coordinate five-cycle fixes 16 half-periods and makes 48 five-cycles; Coxeter^6 fixes only zero and makes 51", "replayed: r alone fixes 1 + 10 + 5; g = r r' = c'^6 is free, and it is layer 23's tick", T, "23"),
    ("HELICITY (09:05)", "K = I + 2(U + U^-1): +-sqrt5 on the moving edges, K^2 = 5, det 625; the filled simplex; a free order-5 action not exhibited", "replayed; the free action is layer 23's tick g = r r', exhibited at 08:48", T, "23"),
    ("MARKS, CHARGE_WEIGHT (08:47, 09:08)", "Y is 5/6 of a duad's 10-weight; outer-product averages 5/24, 3/24, 1/3; the cut lift 4/15; t(t^2 - 25t + 155)^2", "replayed; Y is layer 24's hypercharge, and the 155 is a shared integer, not a map", T, "23, 24"),
    ("GLUE (09:07)", "classes (5, 10), (10, 5b), (10b, 5), (5b, 10b); frames (10,10), (10,15), (15,10), (15,10), (10,15); the 30 is in lattice units", "replayed in layer 24: the same classes with the twin's 5 renamed, (10,5) + (5b,10) and their conjugates; frames 10 I, 15 P + 10 P', 10 P + 15 P'", T, "24"),
    ("INFRARED (09:28)", "C = 1/(1536 pi^4 30^4); heat tails 6c, 24c, 120c; the fixed plane holds 17/10 of the all-ones vector, not 10", "replayed with a correction: both fixed vectors have square 5, so the value is 2 in the lexicographic orientation and exactly 10 in the cyclic one", T, "23"),
    ("CRITICAL (08:35)", "224 is critical, 24 + 1 tick momenta; the port is 2L + (2/5)J, not plus the scalar 2/5", "adopts layers 22-23; the port is W_p = [2/5] + (2 L_C5 + (2/5)J), which the code always checked and the prose now says", T, "23"),
    ("MEMORY's stated block (09:16)", "variances 171 and 371, golden variances above 171", "arithmetic replayed; the block is not stored here", gates.ARITHMETIC, "23"),
    ("ATLAS, SCRIPT (09:44, 10:04)", "twice the first-five sum mod 5 gives 40/50/50/50/50, integer/spinor 32/8, 10/40, 30/20, 30/20, 10/40; the zero filter returns 40, not 20", "replayed: the class is twice the A4*/A4 grade; the zero filter gives D5's 40 roots, of which A4 is the 20 with opposite signs; A4' is 12 integer roots and 8 spinors", T, "23, 24"),
    ("SYMBOL (10:05)", "the witness (28, 28, 6, 2, 1, 0, 0, 0)/10: 15.8548946233 + 3.5105736454, energy 220.6345317313; 12.54149 on the last three axes; least tangent eigenvalue 6.985582", "replayed, with the closed forms 2[(sum cos)^2 - sum cos^2] and 128(prod cos(x/2) + prod sin(x/2)); the least tangent eigenvalue is positive, computed by the projector and by a Householder basis", T, "23"),
    ("LEDGER, LEDGER48, MODEL (09:50-10:07)", "52 orbits; 171 = 271 - 100; 2 x 44 x 2 = 176; 4320 = 36 x 120 = 15 x 36 x 8; 9361 = 260 x 36 + 1", "arithmetic; the shared integers join nothing", gates.ARITHMETIC, "23"),
    ("the Golden root-site port (hub, 10:33)", "T_G = F P_cycle on ten roots; traces 1442, 347900, 84180666, 20416532280; means and variances with the floor 171", "replayed and joined as a dot: F is a signed isometry onto ten roots, the traces hold, and MEMORY's stated block is this port's fixed channels", T, "23"),
    ("the shared bath (hub, 10:33)", "clique and Golden ports: cross squared singular values 4/5 and 2/5, joint span 12, joint Krylov ranks 12, 24, 36; 4 x 4 clique Hankels 31566087163013649 and 1694632079790338625", "replayed", T, "23"),
    ("MODEL (10:09-10:38)", "charges, traces 30 and 80, 56 doublets by class, cubic charges, 13440 root triangles by class, transposition sums, the fivefold map, clock orders", "replayed; the fivefold map's rank 4 and Gram (2I - A_2)/5 hold on the trace-free sites, where charges live", T, "23"),
    ("PLANE (10:17)", "the square is 2; 17/10 was a miscount; 10 in the cyclic orientation", "adopts the 09:02 correction", T, "23"),
    ("the separate model's archives (08:35-09:13)", "completion, completion audit, critical port, connected model, glue-helicity", "recorded, not downloaded or run", RP, "23"),
    ("the mixed root classes (09:00)", "the 200 mixed roots are four classes of 50 with a (5, 10b) or (10, 5) weight structure; K5's five sites and ten duads meet E8's mixed classes at the level of representations", "replayed: (10,5) is the carrier's ten duads times the twin's five sites and (5b,10) its five sites times the twin's ten duads, each pair once; layer 11's (10, 5b') is (10,5) with the twin's 5 renamed", T, "11, 24"),
    ("the second moment (09:00)", "40 + 4 x 50 = 240; the weight-orbit covariances give sum rho rho^T = 60 I8, so the dispersion coefficient is 30", "replayed: 10 I on A4 + A4', 15 P + 10 P' on (10,5) and its conjugate, 10 P + 15 P' on (5b,10) and its conjugate, 60 I in all, and 30 = 60/2; the same moment gives T3 : Q = 3 : 8", T, "24"),
    ("the particle assignment (09:00)", "the construction does not by itself assign particles to E8 roots; work out the mathematics", "worked out (layer 24): Standard-Model quantum numbers on all 240 roots under a stated selection, unique up to W(E8); one root of every pair is always anomalous (OBSTRUCTION); three generations follow from the bracket rule and anomaly freedom (CONDITIONAL); the top coupling has no root realization (OBSTRUCTION); no Yukawa block is formed", SR, "24"),
    ("the K5 -> E8 reference port (09:00)", "a strictly positive six-channel memory variance: the visible sector cannot evolve without the bath", "replayed: M_2 - M_1^2 = X^T X = 183 I + 52 J counts the bath points next to two sites (235 and 52); its eigenvalues 183 and 495 are positive, so X = (1 - P) Delta P has no kernel", T, "22, 24"),
    ("the marked charge map (hub, 11:18; MODEL, 11:04)", "L = P_cycle N P_A4: rank 4, L L^T = ((5I + K)/10) P_moving; near and far marks 34/45 and 26/45; decoder determinant 32 sqrt5/675; window (49 -+ 12 sqrt5)/41; low-energy ratio 17/13", "replayed and joined (charges -> Golden port); the error constant 45(1 + sqrt5)/16 and the S5 twirls P_cycle/3 and P_cycle/9 hold", T, "23"),
    ("the twelve markings (MODEL, 11:19)", "12 marked squares, ten times each, summing to 4 P_cycle; of 66 pairs 6 of rank 4, 30 of condition 5, 30 of condition 5 + 2 sqrt5; centred rank 11; only all twelve isotropic", "replayed and joined (S5 -> cycles)", T, "23"),
    ("the Golden port's infrared channels (hub, 11:18)", "plus 10 C E^3, Golden (C/240) E^4, minus (C/36000) E^5; near/far (17/13)(1 - 2E/5525); marked (C/360) E^4 (1 + 29E/3000); twirl C[(10/9) E^3 + E^4/540 + E^5/48600]", "computed from the ten root sites (the roots are a 7-design) and joined (Golden port -> moments); the plus channel has no E^4 term because it has no dipole", T, "23"),
    ("the word-to-duad join (hub, 11:18)", "a sign-twisted rational intertwiner (det 6245535592857600); O = A + B/sqrt2 an exact isometry; no rational isometry (fixed Grams 108 and 54); T_Z = A + B of det -8, Smith 1^12 2^3; no unimodular intertwiner (coinvariants 3 and 4)", "replayed with its own A and B (det 8) and joined as a dot (words -> surface); the hub's own T stays in its receipt", T, "23"),
    ("J7 and the C5 extension (hub, 11:18)", "no rational C5 commutes with D3 on 1 + 3 std; the least extension is 9 = 1 + 4 std, with U9 = 1 + I2 x companion(Phi_5)", "replayed and joined (words -> A4: the companion is A4's Coxeter element; words -> golden)", T, "23"),
    ("the observation chain (hub, 11:18)", "rank(H9) = 9, rank([H9; L]) = 13, H13, anchors of determinant +-1, sums of +-9, the transported Return residues", "recorded, not replayed: the literal J7 matrix is in the receipts, not in the text", RP, "23"),
    ("MODEL (10:42-11:19)", "closed walks through 2872800; the wrong 220.6349198210; S5's orders and the cyclic fibre; condition 2 + sqrt5; the widths times 36", "replayed, the widths and factorizations as arithmetic; its four labelled responses at weight 1/sqrt5 are not defined in the notes and stay recorded", T, "23"),
    ("the twelve contexts and the Hodge star (hub, 11:58)", "S_even, S_odd = 2 P_cycle -+ (2/sqrt5) J_H; J_H = (sqrt5/4)(S_odd - S_even); sextet condition phi^2; pair overlaps 4/5, 12/25, 18/25", "replayed and joined (S5 -> sound and light): J_H is layer 17's Curl over sqrt5", T, "23"),
    ("the Hodge defect and the context responses (hub, 11:58)", "||[J_H, G]||^2 = (8/5)(g_+ - g_-)^2: 32/5 and 64000; R_A..R_D of determinant -64 sqrt5/625; D = (4/5)(g_+ - g_-) with error 46 eps; R_even/R_odd in [phi^-2, phi^2]; R_C/R_D -> 2/3", "replayed and joined (sound and light -> Golden port); the low-energy ratios now from the computed densities", T, "23"),
    ("the two-port Gram and the overlap (hub, 11:58)", "det Q = 3/25, condition 9 + 4 sqrt5; S^-1 = I + 4 P_8 + (2/3) P_4; C J_H C* = 0; ||AC - C J_H||^2 = 12/5; K_mix keeps Q", "replayed and joined (sound and light -> six-site port)", T, "23"),
    ("averaging and the causal repair (hub, 11:58, 12:04)", "E_H(G^-1)^-1 = (5ab/(a^2 + 3ab + b^2)) E_H(G); a - b = 2/s^2 - 760/s^3; the two-copy dilation; M_odd^2 = (4/5) P_fix; means 240 +- 1/sqrt5; Hodge lines (5 -+ sqrt5) C E^3", "replayed and joined (sound and light -> bath)", T, "23"),
    ("the word branch on the Sylow views (hub, 11:58)", "c = (012), r = (01)(34) on six Sylow views; D3 decompositions; ranks 13, 5, 4; native D^2 multiplicities (1,0,2), (2,2,2), (2,0,0); G8, K8 mod 5", "replayed and joined (words -> S5; an obstruction words -> carrier); the ranks 5 and 4 rest on J7's stated character", T, "23"),
    ("the clock-to-root address (hub, 11:58)", "R_diag and R_first: 0/20 fixed roots, 48/44 five-cycles, det 25/0; f(j + 864) = R_diag f(j), 18 frames per root; no permutation advances the glue classes", "replayed and joined (circle -> E8, a selection; an obstruction time -> A4 + A4')", SR, "23"),
    ("the coordinate bridge (hub, 12:04)", "y2 = M x5 with M^T M = (4/25) P; k_native = 2 k_glue; doubling census 40/10/45; angle patterns (6,8,6) and (4,12,4)", "replayed: layer 24's site/twin embedding is that bridge; joined (AGL(1,5) -> A4 + A4')", T, "23"),
    ("MODEL (11:36-12:07)", "yuga residues 2, 4, 1, 3; syntheme orbits 1, 2, 3, 3, 6; trace moments 15, 40, 200, 1240, 8840, 67480; the sixth cycle direction of square 30; S_even S_odd = 16/5", "replayed, with three corrections: the parity sums differ by (4/5) Curl, not J; S_even = (16/5) S_odd^-1, not 5/16; the yuga doubling is a residue-label action", T, "23"),
    ("the chain (MODEL, 12:24)", "Q: a -> a + d to q(a + 2d) - q(a + 4d); m: ab -> 3(a + b); seed (-3, 1, 2, 0, -1, 0, -2, 1, -1, 3); frames j -> j + 864 and j -> 3457 j", "replayed and joined (charges -> cycles, zero modes -> cycles, AGL(1,5) -> circle): Q^T Q = 5 P_A4 onto the moving cycles, the only AGL(1,5)-map up to scale; the midpoint kills only the near-minus-far line; the seed's rotates have strengths 25 phi^+-2; the frames carry AGL(1,5)", T, "23"),
    ("the Agni-Soma commutator (hub, 12:29)", "F_AS(a, b) = upper([A(a), A(b)]); W_AS rank 6, kernel Lambda^3 A4; F_AS = L_out(Ra ^ Rb) - (2/5) C K_vertex [alpha(a) Rb - alpha(b) Ra]; at the witness ||F||^2 = 1392, F^T J_H F = 96 sqrt5, parity readings 2592 and 2976", "replayed and joined (source -> sound and light, source -> charges): the only S5-map up to scale, where F20 allows 4", T, "23"),
    ("the source phase and the E8 pullback (hub, 12:29)", "Jacobian -64; native rank 9; eta_B = 144 at rate -256; Z1 = 424/3 + 200i, Z3 = -200 + 24i; six decoder determinants; channel weights 288/5, 32/5, 664 -+ (304/5) sqrt5; moments 1392, 334632, 80732784; variance form 1441112/5", "replayed and joined (source -> readout, source -> Golden port), with the hub's basis rebuilt as sympy's nullspace basis of M", T, "23"),
    ("the six Sylow sign lines (MODEL, 12:59)", "six lines of square 10 and products -2, frame factor 12, Gram 12I - 2J on any five; cubic traces +-16; squared cosines 1, 1, 1, 7/15, 1/5", "replayed and joined (PGL(2,5) -> zero modes): ker M is the sign twist of PGL(2,5)'s 5; the cubic traces are matrix traces (edge by edge they are +-4)", T, "23"),
    ("the root-wedge port (hub, 14:07)", "b_rho = v ^ w; sum b b^T = 24 P_cycle; moments 1, 232, 54213, 12740592, 3008062816; variance 389; Hankel 219823907; rho_S ~ C E^5/6000", "replayed from layer 24's site and twin coordinates and joined (A4 + A4' -> port -> bath)", T, "23"),
    ("three ports (hub, 14:07)", "squared cosines 1/24, 1/120 (x4) and 1/30, 1/60; joint Gram 35163473387/331776000000; ranks 18, 36, 54; positive memory; ||[J_H, C*C]||^2 = 1/1440", "replayed; the hub's first LDL pivot 8262212012399/35163473387 is reproduced", T, "23"),
    ("Krylov growth at every order (the hub: 'no all-order claim'; MODEL: 'not in the chain')", "ranks 18(n + 1) checked through degree 2", "proved at every order for any port family on one root shell: the point (n + 1)s carries (-1)^n p_n(s)", T, "23"),
    ("the Schur memory (hub, 11:18)", "V/(s + 256) <= Sigma(s) <= V/s, resting on the stated band bound", "proved with the band edge; the n-th boundary moment is at most 495 x 256^n (MODEL's conditional), and Sigma is no finite sum of poles", T, "23"),
    ("the band top through the ports (new)", "-", "the root-wedge port vanishes to second order at all 135 band tops (each a D8 of second moment 28 I), so it is a quadrupole at both band edges: 39 (256 - E)^5/(655360 pi^4) at the top, C E^5/6000 at the bottom; clique and Golden (256 - E)^3, triangle (256 - E)^4", T, "23"),
    ("the pair frame (hub, 15:03)", "C C^T = 160 P_cycle; projectors 5 + 6 + 4; 11-sets rank 6, 10-sets 2991 + 12; blind lines F+- = P_cycle +- eps/5; sum F_i = 2 P_cycle, F_i F_j F_i = F_i/5", "replayed and joined (PGL(2,5) -> rotor plane, -> sound and light): the frame's failures give the Hodge star", T, "23"),
    ("the parity pair and four root ports (hub, 15:03)", "odd moments 1, 242, 58691, 14259954, 3470101592; T_S* f(H) T_O = 0; rank 24; 24(n + 1) by 24 x 24 Weyl determinants 362979 and 983965", "replayed; 24(n + 1) follows from the root-shell theorem (the Weyl certificates are not rerun)", T, "23"),
    ("the norm-four dark port (hub, 15:03)", "2160 sites; dark multiplicities 0 and 36; A^T A = 600 P_A4; moments 1, 975/4, 237985/4, 14539767; K^T K = 60 P_dark; 28(n + 1)", "replayed (the hub's seed read through the twin's outer automorphism); the sphere version of the root-shell theorem gives 4(n + 1), orthogonality 28(n + 1)", T, "23"),
    ("the second dark port (hub, 16:11)", "1200 sites, rank 4, G2^2 = 7200 G2; moments 1, 232, 54150; principal cosines 5/192; mixed 232 C, 54150 C; residual 45640/187, 11152530/187; 32(n + 1) by Weyl determinants 117705 and 943098", "replayed and joined (A4 + A4' -> dark ports -> moments); 32(n + 1) follows from the norm-four shell argument (the Weyl certificates are not rerun)", T, "23"),
    ("the six F20 views (hub, 16:11)", "X_i^T X_i = P_A4, X_i X_i^* = P_cycle - F_i, Gram 24/5 delta - 4/5; sum Pi_i = 2 P_B + 3 P_D; tr Pi_i Pi_j = 6/5; ranks 4, 7, 9, 10, 10, 10; determinants 32, 2401/4, 5184; phi^4; Woodbury -X_i/47", "replayed and joined (dark ports -> rotor plane), the mixers built as Reynolds averages", T, "23"),
    ("the coherent encoder and the Golden repair (hub, 16:11)", "V S = 12 I, S^T S = 12 G; |det S_-j| = 2592; 7776 per lane, 6^10 for twelve; 2^20 3^16; V index 16, T index 3, intersection 48; intensities 5/6 and 1/30", "replayed and joined (PGL(2,5) -> words, source -> words)", T, "23"),
    ("the five K4 planes (MODEL, 16:17)", "Gram 15 on the dark four; 2/5 of every golden line in every plane", "replayed and joined (K5 vertices -> dark ports)", T, "23"),
    ("the bath's spectral measures (new)", "-", "proved: every site vector's measure is absolutely continuous, a port vector's density is positive almost everywhere on all of [0, 256], and its Jacobi chain tends to (128, 64^2) (Rakhmanov's theorem, cited); 45 exact levels from W_0..W_90", T, "23"),
    ("the five dark planes (hub, 16:47)", "sum P_r = 2 I, P_r P_s P_r = P_r/4; Tr(P_r R_j) = 2/5; five reduced Pluecker points; Gram 15 delta - 3; tangent spectrum (2/3)^3 (10/9)^3; ten inverse branches; tags -78, -63, -33, 27, 147", "replayed and joined (K5 vertices -> source -> dark ports)", T, "23"),
    ("the dark-plane energy court (hub, 16:47)", "word lattice of index 3 in each plane (det 108); minima 12 + 12 on two planes, 4 + 28 on three; prepared rotor energies 24 and 32, charges 12 and 16", "replayed (Lagrange reduction of the five plane lattices)", T, "23"),
    ("the finite parent's dark branches (hub, 16:47)", "E_r invariant (12-dimensional dark phase spaces); packet phi = (-4/3, -4/3), H = 20 rho^2 + (16/9) rho^6; blind circular orbit 32 and 16; branches X = 6 and 32/3 at r = 1/2 with H = 51/2, 134 and Q = (19/4) sqrt6, 18 sqrt6", "replayed in the full equations at three phases", T, "23"),
    ("one-frequency tomography and the scalar shift (hub, 16:47)", "q = Tr CC*/Tr R, X = C/q, a = 1/ell, b = 1/(m - q); Schur decrement; 84/5; (45/94, 15/47); quartic 25t^4 - 1300t^3 + ...; kernel (30595, -225, 55235, -6812, 41885); D = 55899556/4862025; -459567/245; emulator counts 0, 1, 3, 4", "replayed and joined (root-wedge port -> dark ports); the infinite E8 thresholds stay uncomputed", T, "23"),
    ("the quadratic frames and the matroid (hub, 17:26)", "sum E_e = 2 I, sum R_j = (6/5) I; 1/9, 1/25, 1/5; 1 + 9 + 5; closed inverse, Parseval; planes (1/2, -1/4); 162 complete and 90 incomplete five-edge sets, unimodular; connected nonbipartite complements", "replayed and joined (K5 edges -> source)", T, "23"),
    ("the dark readout (hub, 17:26)", "matched 1 and 1/16, four of five sensors; 225, 225, 100, 25, 25 at norm 40; full spark 35 and 70 minors, least 1", "replayed and joined (dark ports -> readout); the complement-property theorem is cited", T, "23"),
    ("cubic-null triangles and the double-dark pair (hub, 17:26)", "T T^T = 20 P_cycle; A0^2 + B0^2 = 16 P3; E = 96, Q = 48; ranks 6, 2, 8; E - 2 sigma Q a sum of squares; |W_AS| = sqrt10/3", "replayed and joined (source -> cycles)", T, "23"),
    ("the Fibonacci bridge (hub, 17:26)", "K^2 = 5, Phi^2 = Phi + 1, K S = S(2B - 1 + 2B - 1); B^6 sum 34", "replayed and joined (A4 -> golden companion)", T, "23"),
    ("the dark measurement (MODEL, 18:00)", "frame operator 15 I; 4/5 and 1/20; 6/5 bits; Bhattacharyya 11/20", "replayed and joined (dark ports -> readout)", T, "23"),
    ("plane tomography (MODEL, 18:00)", "every bivector tangent; 10 = 6 + 4; c = 1 + 3h + 4h^2 + 2h^3, p = 1 + h^2; Euler number 4 from four fixed planes; e^2 = -h^2 impossible", "replayed and joined (source -> readout); the skew normal form, Gr+(2, 5) = Q3 with its bundle formulas, and the Lefschetz theorem are cited", T, "23"),
    ("the seventh sensor (hub, 18:22)", "ell12: 3, 3, -2, -2, -2; G(2, 5) of degree 5; the rank-nine observer's tangent rank 5; margin sqrt2; 512 cases, 46, 105/2, 70, 85, 90, 190; ell* and the gap sqrt(15/46)", "replayed and joined (dark ports -> readout); the odd-degree section argument is cited", T, "23"),
    ("preparability (hub, 18:22)", "|w ^ w|^2 = 4 q^T H4 q = 2 s^2 - Tr (K_w G)^4; 1 and 2 at e01 + 2 e23, 10 with an error of 3; z0 + z1 not simple", "replayed and joined (source -> dark ports)", T, "23"),
    ("the exterior code (hub, 18:22)", "sum Q Q* = 144 I, sum h h* = 5 P_D, Parseval; [15, 6, 5], [10, 4, 6] (185 and 25), [25, 10, 5]; Smith 1, 5, 5, 5; rank 1 mod 5, 30 of 252 mod 2", "replayed and joined (cycles -> dark ports)", T, "23"),
    ("two instruments (hub, 18:22; MODEL, 18:33)", "success 4/5, optimal; 6/5 = 8/5 - 2/5 bits; Holevo 2, KL 3; 4 (11/20)^11 < 1%; 1/6 for the source states; 126 and 210 minors", "replayed and joined (source -> dark ports); the complement property is cited", T, "23"),
    ("causal records (hub, 18:22)", "G_C = 183 P_c + 495 P_u; jets through n = 10; 42240/61 and cosh; E = 8, Q = 4, phasor (-4/3, -4/3), wedge 12", "replayed and joined (bath -> source); the Volterra comparison is cited", T, "23"),
    ("the A6 readers and the Golden adapter (hub, 18:22)", "125, 165, 230; 90, 170, 250, 330, 360 and 357; B_G of rank 5, 120 P_source; 10 + 8 + 18 W4 against 18 + 18 W4", "replayed and joined (360 parent -> source); the 360 parent is a new dot", T, "23"),
    ("Golden30 (hub, 18:22)", "ranks 30 and 60; q^6 (q + 6)^5 (q - 6)^9 (q^2 + 3q - 99)^8; Return > 17/20; (24/25)^14 (7821/10000)^8; eight Fibonacci blocks; Phi16 T = T Phi4", "replayed and joined (360 parent -> golden companion, A4 -> 360 parent)", T, "23"),
    ("the blind 126 (hub, 18:22)", "30, 60, 90, 145, 216, 225, 234; trace 126 = 1 + 25 + 100; 260; the chi10 reader's 100; 360 and 37", "replayed and joined (360 parent -> readout)", T, "23"),
    ("two 36s (hub, 18:22)", "6 + 30 against 6 + 15 + 5 + 10", "replayed as an obstruction (synthemes -> 360 parent)", OB, "23"),
    ("the cyclotomic line (layer 25)", "every root generates E8 over Z[c']; alpha = (2 + 2 eta + eta^2)/15, N(alpha) = 1/1265625; C_W(c') = <c'>", "constructed and joined (E8 -> cyclotomic line)", T, "25"),
    ("the Galois clocks (layer 25)", "|N(<c'>)| = 240 = 30 x 8; the day sigma7, the golden clock sigma11, the mirror sigma29; u ubar = sigma(alpha)/alpha", "constructed and joined (cyclotomic line -> W(E8) clocks)", T, "25"),
    ("the residue plane (layer 25)", "SNF(1 - g) = 1^6 5^2; F25 with c' of order 6; 24 points of 10 roots; six A4 + A4", "constructed and joined (W(E8) clocks -> residue plane -> A4 + A4')", T, "25"),
    ("the tick's normalizer (layer 25)", "|C_W(g)| = 600 onto SL(2,5); |N| = 2400 onto GL(2,5), PGL(2,5) on the lines; stabilizer 400 with 200 swaps", "constructed and joined (residue plane -> PGL(2,5), surface; A4 + A4' -> A4)", T, "25"),
    ("the Singer cycle (layer 25)", "the day = 2 + 2 omega, order 24, a 6-cycle on the lines; AIR_801 mod 5 ~ -day (x^2 + x + 2)", "constructed and joined (residue plane -> 801 matrix)", T, "25"),
    ("the Gauss sum and the shadows (layer 25)", "A(h0) = r + r^4 - r^2 - r^3; (g + g^4 - g^2 - g^3)^2 = 5; shadow Gram + 2/5 = M", "constructed and joined (cyclotomic line -> golden companion; A4 + A4' -> carrier)", T, "25"),
    ("the hexad (layer 25)", "r = (01234) fixing the carrier line; t outside PSL(2,5); <PSL(2,5), t> = A6", "constructed and joined (PGL(2,5) -> 360 parent)", T, "25"),
    ("the address map (hub, 19:39)", "4320 -> 360 twelve to one, address(j + 864) = r address(j); orbits 5^4 10^2 20^16; 4200 mismatches", "replayed and joined as a selection (circle -> 360 parent)", SR, "23"),
    ("the regular clocks (layer 26)", "regular numbers = divisors of 30, 24, 20; charpoly Phi_d^(8/phi(d)); |C_W| = 30, 24, 20, 288, 192, 600, 46080, 155520", "constructed and joined (W(E8) clocks -> regular clocks -> cyclotomic line, residue plane, sun's decad, half-periods)", T, "26"),
    ("three cyclotomic lines (layer 26)", "Z[zeta30], Z[zeta24], Z[zeta20]; beta of norm 1/disc; |N| = 240, 192, 160; Q(zeta16) carries Z^8", "constructed and joined (regular clocks -> cyclotomic line); no element of order 16 (obstruction)", T, "26"),
    ("the prime clocks (layer 26)", "c' = (-1) s g; SNF 2^8, 1^4 3^4, 1^6 5^2; F16 x F16, F81, F25; roots 2 x 120, 3 x 80, 10 x 24", "constructed and joined (cyclotomic line -> half-periods, sun's decad)", T, "26"),
    ("the sun's decad (layer 26)", "C_W(s) onto Sp(4,3); F9 = F3[phi]; 40 A2, W(3), ten F9-lines = ten 4A2; F9-linear 2160 onto PSL(2,9) = A6, r -> c', doubling -> day", "constructed and joined (sun's decad -> 360 parent, AGL(1,5))", T, "26"),
    ("the four places (layer 27)", "the real place, 2, 3 and 5 carry the bath, the qubits, the parent and the carrier", "eps = 240 - sum_r chi(r): 250, 243, 224/256; the golden ratio ramified at 5, inert at 3 and 2; two stabilizers at 2", T, "27"),
    ("what the places cannot give (layer 27)", "the memory clock (order 90), the circle (4320), AIR_801 (det 12402)", "psi(90) = 10 and psi(4320) = 38 exceed 8; AIR_801 is no lattice clock", OB, "27"),
    ("the principal circle (layer 28)", "k -> k rho / 4320 in R^8 / E8; rho primitive with <r, rho> = ht(r)", "constructed and joined (E8 -> principal circle <- circle)", T, "28"),
    ("the regular steps (layer 28)", "rho/d has the adjoint spectrum of a lift of w_d; eps = 248 - 8 mu(d)/phi(d)", "constructed and joined (principal circle -> W(E8) clocks, regular clocks, bath); Kostant cited at d = 30", T, "28"),
    ("the critical steps (layer 28)", "the band on the circle is critical exactly at the steps of order 2 to 5: D8, A8, D5 + A3, A4 + A4", "constructed and joined (time, observer and 27-clocks -> principal circle -> critical census)", T, "28"),
    ("no clock covers A6 (owner, 20:22)", "Hom(Z/4320, A6) = 360, images <= 5; clocks solvable (240 > 30 > 1), A6 perfect; the hexad sees PSL(2,5) only", "obstruction (circle, W(E8) clocks -> 360 parent)", OB, "26"),
    ("the dark code (hub, 20:20)", "range P3 of K = M^T M; [10, 4, 6]; 25 failing four-edge sets", "replayed: K^2 = 3K + 4J, P0 + P3 + P8 = I, P3 = M^T P_A4 M/3, the code and its failures", T, "23"),
    ("the saddle quartic (monograph, 20:13)", "0 |y|^4 at the 224 saddle, from 18 + 18", "corrected: -rho^4/2, from 24 (E7) and 12 (oblique); the collar stays open", T, "23"),
    ("the norm 31 (monograph, 20:13)", "N(3 - zeta - zeta^4 + 2 zeta^2) = 31 and 5 x 31 = 155", "corrected: that element has norm 61; 2 + zeta - zeta^2 has norm 31", T, "23"),
    ("the line stabilizer (MODEL, 20:08-21:02)", "the 60 fixing the carrier line have the order of PSL(2,5)", "a point-stabilizer A5, not the tick's transitive PSL(2,5); they meet in 10", T, "23"),
    ("the landings (MODEL, 21:19-21:46)", "147 lands on 1728; 148 and 153 land on 2592", "as 864 x = 864 (x mod 5), yes; as the first tick level the multiples reach, not for 147, 148, 153 (3456, 1728, 1728); every unit and 328 non-units match", gates.ARITHMETIC, "23"),
    ("the dark erasure court (hub, 22:51)", "dark floors 3/5, 1/3, (17 - sqrt129)/30, 1/15, root of 135t^3 - 180t^2 + 54t - 2, 0", "replayed over all 847 erased sets, with attaining counts 10, 15, 30, 10, 60, 25", T, "23"),
    ("the dark syndrome floor (hub, 21:54)", "||S_D e||^2 >= ||e||^2/15 on four-sparse errors; T = (K^2 - 7K - 2I)/2", "replayed: 385 minors, ten tight supports, T = -P0 - 7P3 + 3P8, V V^T = P0 + 9P8", T, "23"),
    ("the circle as a ring (MODEL, 21:05-21:17; maps29.ts)", "idempotents 3105, 2080, 3456, 2241; mirrors 864, 2240, 1215; 864^2 = 3456; landings 864 r; depths 2592 + 1728", "replayed as arithmetic on Z/4320; the same integers are not the same operators", gates.ARITHMETIC, "23"),
    ("quartic chirality (hub, 14:07)", "Pf(R^T C R) = 175, ||f||^2 = 258, f^T eps f = 350, 70 sqrt5", "replayed; f^T Curl f = 2 Pf identically, so J_H is the Hodge star of Lambda^2 A4", T, "23"),
    ("the syntheme bridge (hub, 14:07)", "sharply 3-transitive six-label action; synthemes 5 + 10; D_syn = Pi D Pi^T; traces 7 against 3; 36 = 6 + 15 + 15 with orbits 6, 15, 5, 10", "replayed and joined (PGL(2,5) -> synthemes -> carrier)", T, "23"),
    ("the six-line frame (hub, 14:07)", "Gram 41472; two erasures blind; H R H^T/144; [A, B] from frame bilinears; cubics -1200 + 144i and 848 + 1200i; blind pair of edge-square 4; Hom dimensions 0, 1, 1; W W^+ = (10/9) P_cycle", "replayed; the twenty-term cubic formulas hold as polynomial identities", T, "23"),
    ("word lanes (hub, 14:07)", "T; Smith 1, 1, 1, 1, 3; F3 ranks <= 4; G^5 = I; the [T | e0] repair; W's Smith 1, 2, 2, 2, 2, 2; one dark Jordan block mod 5; Jacobians 5120 and -46080; Hom_C5, D3, A5 = 8, 4, 0; U of det -1", "replayed and joined (words -> source; index 3 and the A5 no-go are obstructions)", T, "23"),
    ("the clock on the Sylow labels (hub, 14:07)", "p = 4j mod 5 onto the five moving labels, 864 each", "replayed and joined (time clock -> PGL(2,5))", T, "23"),
    ("the comparator (MODEL, 13:02-14:18)", "moments 1, 242, 58691, 14259954, 3470101592; Hankel 15930273; last diagonal 200 or 210", "replayed: the triangle port's; not unique, and by the all-order theorem no finite comparator is exact", T, "23"),
    ("the THEOREM diagram", "-", f"THEOREM maps alone join {len(DOTS) - 2} of the {len(DOTS)} dots, no one or two of them hold it together, and they join every pair of levels at least twice; the datum's regular S5-orbit and the time clock's actions on the roots (48 extended A4 pentagons), the zero modes (one per character) and the triple close the last cuts", T, "23"),
    ("all dots", "-", f"{len(DOTS)} dots and {len(JOINS)} joins in one connected diagram (docs/DOTS.md)", T, "23"),
    ("the six-line quotient (hub, 23:38; MODEL, 23:26-00:00)", "A S = S Q, Q = 10J - 4I; spectrum 56, 28^8, 8^35, (-2)^112, (-4)^84; a reducing split with zero Schur memory", "replayed and joined (residue plane -> root graph)", T, "23"),
    ("the midpoint code (hub, 23:38)", "[15, 5, 6]: all 3003 ten-reading sets span, 10 of 5005 nine-reading sets fail", "replayed: the ten failures are the zero sets of the 3 + 3 splits", T, "23"),
    ("the selected matrix over F5 (MODEL, 23:26-00:00)", "D = [[1, 4], [1, 2]]: D^2 = 3C, D^6 = 3I, order 24, a 6-cycle on the lines", "replayed: D is conjugate in GL(2,5) to the inverse day d^-1", T, "23"),
    ("the native moments (hub, 00:25)", "m0..m6 = 1, 232, 54213, 12740592, 3008062816, 712951229280, 169533368834085; Hankel 275042684645559311; 0.00435118836 <= s <= 0.00436266657", "replayed: m5 and m6 recomputed on the lattice; the Hankel, Jacobi and Galerkin values hold; the congestion bound is stated", T, "23"),
    ("the native moments through 8 (hub, 00:52)", "m7 = 40427488329573760, m8 = 9664268760217668816; 5 x 5 Hankel 925993405224288478170979103007; a3, b4^2", "replayed: m7 and m8 recomputed on the lattice (H^4 on 4770696 sites)", T, "23"),
    ("the identity step (MODEL, 00:46-01:16)", "the band at the identity step is 240 = 248 - 8 mu(1)/phi(1)", "corrected: it is 0, the minimum; the formula holds for d > 1", T, "23"),
    ("the Petersen sequence (hub, 00:25)", "B B^T = 3I + A_Petersen = 4I + J - K, rank 10; P_source and (B B^T)^-1 as polynomials", "replayed and joined (synthemes -> Petersen)", T, "23"),
    ("the Weyl vector's order (MODEL, 00:04-00:38)", "46, 68, 91, 135, 110, 84, 57, 29 in a different order from Bourbaki's", "corrected: they are in the Bourbaki order, where the highest root is 2, 3, 4, 6, 5, 4, 3, 2", T, "23"),
    ("the clock tower, rooted (30 Oct)", "circle > seam > grain > golden orbit > ticks > observer > sun (the 23:27 chain)", "the chain is the principal circle's subgroup lattice: the seam <36> is generated by the regular steps, the grain <72> by the critical steps, the time and observer clocks are the critical steps of order 5 and 4 and add to the golden step's <216>, the sun's <1440> is the steps of order 3; the 27-clock is the Sylow 3-subgroup, the coil the grain plus the 27-clock, the miss set the kernel of the time coordinate, the vortex the 27-clock modulo the sun; the seed names the orders 5, 4, 60 and 120, so the time clock, the observer clock and the grain are derived, and the canon's cofactor 36 = 4320/120 names the rest", T, "23, 28"),
    ("the golden companion in the symmetry level (30 Oct)", "B = [[1, 1], [1, 0]] acts on E8 through the golden clock (a selection, B^k -> v^k)", "the golden companion is the tick's negative cosine X = -(g + g^-1): E8 = Z[phi]^4, the day is the Galois conjugation phi -> 1 - phi, and X lies in a regular clock's cosine ring exactly when 5 divides its order", T, "23"),
    ("the nine-torus placed (30 Oct)", "T^9 of the nine positive critical frequencies, joined to the census and the bath", "six of the nine are the band at the principal circle's critical steps (256, 252, 248, 250), at the half-periods (256, 224), at the sun's momenta (243) and at the tick's (250); 251, 4025/16 and 6800/27 are at none of them", T, "23, 28"),
    ("the principal circle's uniqueness (30 Oct)", "k -> k rho / 4320 for the Weyl vector rho", "unique up to W(E8): rho determines its positive system, W permutes the positive systems transitively (cited) and keeps the band, so every conjugate circle has the same band values, critical steps and types", T, "28"),
    ("the day and the golden clock (30 Oct)", "the stored day d (order 24, sigma_7) and golden clock v (order 20, sigma_11) in data/clocks.json", "each is one of two conjugacy classes of its normalizer <c', d, v> over its Galois automorphism (10 + 10, 12 + 12), with one characteristic polynomial, so conjugate in W(E8) but not relative to c'; the mirror's class is unique: a recorded selection", T, "25"),
    ("the sibling's clock corrections (MODEL, 14:41)", "lcm(30, 24, 20) = 120; the step 120 has order 36; the kernel of x -> 9x is <480>, of order 9, not the multiples of 9", "replayed: <36> has order 120 and the step 120 order 36; the multiples of 9 are <9>, of order 480, the kernel of x -> x mod 9", T, "23"),
    ("the address and principal subgroups (MODEL, 14:41)", "<120> (order 36) and <144> (order 30) meet in the subgroup of order 6; five, seven and three critical steps lie in them and in both", "replayed", T, "23"),
    ("the bridge's two splits (MODEL, 14:41)", "on the sum-zero four the signless Gram acts by 3 and the Gauss square by 5; on the all-ones line by 8 and 0", "replayed: M M^T = 3I + J and G5^2 = 5I - J, both pairs add to 8 (M M^T + G5^2 = 8I)", T, "23"),
    ("the six-site rotor's skew (MODEL, 15:04)", "S = R - R^T has rank 4 and is killed by S^4 + 5S^2 + 5I, of rank 2; the five powers of R add to it", "replayed: t^2 - 5t + 5 in t = -S^2, the relation of the golden pairs 2 + phi and 3 - phi; the sum of the powers is 5 P_fix; the windings R - R^4 and R^2 - R^3 have Gram 10I", T, "23"),
    ("Karma's commutators (MODEL, 15:04)", "K^2 = -4I, and [K, B^n] has trace 0 and determinant -29 F_n^2 through the tenth", "replayed with a witness K = [[1, 1], [-5, -1]]: [K, B^n] = F_n [K, B] for every n; 29 = h - 1 is the highest root's marks without the leading 1; the sibling's operand is not stored here", T, "23"),
    ("the Names' clock readings (MODEL, 14:49)", "540 of order 8; 11 and 29 generate; 108 = 3 mod 5; the yugas add to 4320; x3 kills the nakshatra seam; 736 of order 135; 3600 of order 6; the golden landings 0, 216, 864, 1080, 0", "replayed; readings, not joins", T, "23"),
    ("doubling after a triple translation (MODEL, 15:04)", "on <864>, doubling after a triple translation equals two translations", "corrected: 2(x + 3) = 2x + 1 mod 5, one translation after doubling; two translations after doubling is doubling after one", T, "23"),
    ("the memory clock's stepping (layer 3)", "one circle step is one memory step: k -> A^k onto the order-90 clock, a selection", "unique up to the memory's symmetry: the circle maps onto <A> in 24 ways, one orbit of its normalizer in S_120, and every one reads the vortex and the time coordinate up to the doubling (30 Oct)", T, "23"),
    ("the pentagon operator (MODEL, 08:22-08:44)", "+1 on the pentagon steps, -1 on the pentagram steps: P^2 = 5I - J, (sqrt5 I + P)(sqrt5 I - P) = J, complementary only on the sum-zero four", "replayed: P is the tick's Gauss sum R + R^4 - R^2 - R^3 = 2(I + R + R^4) - I - J on the vertices, and P^2 = B B^T, so P is a symmetric square root of the K5 Laplacian, the sound operator", T, "23"),
    ("the sheet's Jacobi step (MODEL, 08:44; separate model, 09:07)", "27778 is not divisible by 138, so the third moment does not continue that Jacobi step", "corrected (the separate model, replayed): only an integer diagonal is excluded; the rational Jacobi matrix [[242, 138], [1, 13889/69]] gives 1, 242, 58702, 14267058 exactly", T, "23"),
    ("the tick and the schedules (MODEL, 08:22-09:12; separate model, 09:07)", "the 125 schedules generate the order-864 tick", "corrected (the separate model, replayed): <125> = <5> is the miss set, of order 864; the tick <864> has order 5; they meet in 0 and make the circle", T, "23"),
    ("the golden subgroup (MODEL, 09:12)", "1060 generates the golden subgroup of order 216", "corrected: <1060> = <20> has order 216, while the golden orbit <216> has order 20; the two meet in the observer clock <1080>", T, "23"),
    ("the source histories (MODEL, 09:38-09:51; separate model, 09:24)", "the 25 Plucker equations are necessary and not sufficient: the false e0 ^ (e1 + u e2 + u^2 e3) passes them with no two-packet factorization", "replayed: both histories pass all 25, which linearize to rank 13 at both; the syzygies (rank 8, nullity 2) separate them: the false kernel e0, u e0 wedges to 0 and its planes share the line e0, the genuine kernel wedges back and its planes meet in 0", T, "23"),
    ("the six root probes (hub, 09:23)", "V = 44I + 12J - 11H on six root sites; H = (244I + 336P - 5V)/55", "replayed: one root on each residue line, in three orthogonal A2 pairs, has two-step return Gram V on the root graph; with the six-line quotient P = (10J - 4I)/56 it rebuilds the mirror and the three sectors", T, "23"),
    ("the F20 bright-dark line (hub, 09:23)", "Hom(Lambda^2 A4, sign (x) A4) has dimension 4, 2, 1, 0 under C5, D10, F20, S5", "replayed", T, "23"),
    ("the Golden channel (hub, 09:23)", "Phi(X) = sum tr(F_i X/2)(11I - 5F_i)/56: spectrum 1, (-1/14)^5, 0^30; Phi^n = D + (-1/14)^(n-1)(Phi - D); Choi (3/28)^2, (1/7)^10, (9/56)^10, (11/56)^14; no closed finite unreset dilation", "replayed through the six Sylow-five averages on Lambda^2 A4 (sum 2I, tr F_i F_j = 2/5); the no-go's witness F0 - F1 has Tr X^2 = 16/5 and Phi(X) = -X/14, and the proof is the hub's", T, "23"),
    ("the contrast Green identity (hub, 09:23)", "nu_J(dE) = E nu_origin(dE)/240, static return 1/240", "the measure form of the contrast moments E_(k+1)/240 already held: W(E8) is transitive on the roots, so (Delta^k)_(0r) = E_k - E_(k+1)/240 for every root r", T, "23"),
    ("the twin lanes and the A4 local factor (hub, 09:23)", "432 lanes mod 4320 onto 36 mod 360, 12 to 1; omega = (4, -1, -1, -1, -1)/5; 15/16", "replayed as arithmetic; the twin-prime programme itself is outside this model", T, "23"),
    ("two walk counts (hub, 09:54: J04, J05)", "the finite root graph closes 1, 0, 56, 1512, 62160, 2872800, 144606784 walks per root; the lattice has W_2..W_4 = 240, 13440, 1260720", "replayed: different operators, the finite graph from its spectrum and the lattice from its walks", T, "23"),
    ("the six-line transition (hub, 09:54: J06)", "det P = (-1/14)^5 < 0, so P is no e^B; P^2 = e^(log 196 (E - I))", "replayed", T, "23"),
    ("the Golden Gauss operator's symmetry (hub, 09:54: J19; separate model, 09:54)", "M M^T + G5^2 = 8I; stabilizer of order 10 and ten sign-reversing permutations", "replayed: x -> ax + b multiplies G5 by (a/5), so D10 fixes it and the rest of AGL(1,5) reverses it, and no other permutation sends it to +-G5", T, "23"),
    ("the N34 boundary jets (hub; canon N34-012, N34-013)", "y5 + 248 y3 = 0, y7 - 58181 y3 = 0 (bright, m1 = 232, m2 = 54213); y5 + (1039/4) y3 = 0 (dark, m1 = 975/4); separation 47/4", "replayed as arithmetic of the held moments: the odd jets of y'' + Delta y = v f from rest for a forcing with jets 1, -16, 256 (frequency 4); the canon's source q'' + 4q = 0 (frequency 2) would give 236 and 55157", T, "23"),
    ("the 49-tuple (hub, 09:23; canon N34-021)", "49 offsets of diameter 240 with 0 and 2, admissible for every prime", "replayed: a residue is omitted mod every prime p <= 47 and p > 49 is trivial; arithmetic about a tuple, nothing about primes", T, "23"),
    ("tr A^2 = W_3 (MODEL, 14:06)", "the root graph's tr A^2 = 13440 is the same integer as the lattice's W_3", "a reason, not a coincidence: both count the 240 x 56 ordered root pairs at inner product +-1, matched by r' -> -r'", T, "23"),
    ("separate model's joined model (22:02)", "158 check groups, 80 matrices, 63 typed relationships", "recorded, not rerun", RP, "23"),
]

NOT_JOINED = [
    ("the Yukawa sizes (layer 24)", "the roots give which couplings can be nonzero, not their sizes; "
                                    "no Yukawa block is formed, and masses and mixings stay removed", gates.UNFORMED),
    ("separate model's joined model (22:02)", "158 check groups, 12 review groups, 80 matrices, 63 typed relationships; "
                                              "sha256 b0c17731...", RP),
    ("canon SMEAR (184 / 481)", "a rank-6 port T and a rank-4 projector P with minor -512 alpha^4 / 25; the operands are "
                                "not stored here", RP),
    ("source-to-cube bridge", "rank 10 with an exact left decoder (canon); not stored here", RP),
    ("the hub's Z31 clock (I_STATUS)", "order 30 on 31 states, maximal rank 29 into the 45-point product; it rests on a "
                                       "supplied characteristic that is not stored here", gates.CONDITIONAL),
    ("the hub's R15 and F20 rows (I_STATUS)", "R15 with (t - 1)^3 (t^2 - 7t + 11)^6 and its F20 average 1^3, (7/2)^12; the "
                                              "operators are not stored here", RP),
    ("the separate model's release H (22:41)", "5247252 bytes, 168 check groups, 77 presentations, a finite Hilbert space "
                                               "of dimension 174108; not opened or rerun", RP),
    ("the separate model's IJ update (23:30)", "637057 bytes (matching Drive), 176 check groups, 60 presentations, a finite "
                                              "Hilbert space of dimension 176368; not opened or rerun", RP),
    ("BassForge (GB-018)", "the view and the retraction are absent in the canon and unformable; the 38-fiber's 117 "
                           "checks are not stored here", gates.UNFORMED),
    ("the source shape's witness (SHAPE_091)", "the squared lengths 20 and 24 and Omega^2 = 238/238 need the witness, "
                                               "which is not stored here", RP),
    ("the separate model's relations overlay (23:50)", "197642 bytes, 73 check groups, 32 matrix outputs; not opened or "
                                                       "rerun; its five source corrections are replayed", RP),
    ("modules 8-11, unreplayed parts", "the two-channel C and W, the Hankel realization and the [9, 3, 7] code over "
                                       "F11 need operands not stored here; the Bargmann projectors cannot be unit rank-one "
                                       "projections, since then |Tr P1 P2 P3| <= 1 < |1 + i| (the hub's review, replayed)", RP),
    ("the separate model's splits update (00:49)", "413793 bytes; 90 new check groups (grain 43, towers 17, module "
                                                   "relations 27, API 3) and 47 review groups; not opened or rerun; its "
                                                   "five source corrections are replayed", RP),
    ("the [9, 3, 7] code over F11 (layer 15)", "MDS and 3-error-correcting; nothing identifies it with H90 or with any "
                                               "dot", gates.UNFORMED),
    ("the separate model's unified build (01:25)", "43752185 bytes, 286 payloads, 104 new check groups (root graph 50, "
                                                   "simplex 26, K operators 20, API 8); not opened or rerun; its three "
                                                   "source corrections are replayed", RP),
    ("the hub's release-K packages (01:13, 01:53)", "OES_Canon_K_Evidence and OES_Canon_K_All_Dots_Exact (a Python verifier "
                                                    "and a JSON receipt): not downloaded and not run; their stated bridges "
                                                    "are replayed from the Google Doc", RP),
    ("air", "no air operator is stored, and none is formed", gates.UNFORMED),
    ("the board's fine-structure digits (BOARD_A, ALPHA_JOIN)", "a = 0.0072973525664 is written by hand; no e, hbar, c, "
                                                                "electron mass or length is stored, the canon removed "
                                                                "alpha = 1/137, and nothing here forms alpha or r_2",
     gates.UNFORMED),
    ("SEVEN_PAIRS's decoder", "D4 C4 = I3 and the reading ladder need operands not stored here", RP),
    ("the separate model's reconciled capsule (00:30)", "5032710 bytes, 189 new check groups and 887 matrix references, with "
                                                        "a source patch of 8240856 bytes; certificate read, nothing decoded "
                                                        "or run", RP),
    ("the separate model's connected capsule (01:21)", "8200616 bytes, 393 independent exact groups and 56 new typed "
                                                        "relationships (556 combined) over the N33 sources; its coverage "
                                                        "counts 53130 = C(25, 5), 1496250 = C(21, 4) x 250 and 63 = 2^6 - 1 "
                                                        "replay as arithmetic (notes_0117); certificate read, nothing decoded "
                                                        "or run", RP),
    ("the canon's N33 release (00:59-01:06)", "29 selected-reference source-graded claims from seven families in four new "
                                             "tabs (3750 and 3705 sheets), no new matrix ids and no gate changes; read "
                                             "from its receipt", RP),
    ("the canon's N32 release (00:04-00:13)", "25 source-graded claims from nine sources in four new tabs (3746 and 3701 "
                                             "sheets), no new matrix ids and no gate changes; read from its receipt", RP),
    ("the separate model's reviewed and extended capsules (21:46, 23:40)", "1692628 and 6462293 bytes; 72 and 271 new "
                                                                            "check groups, 26 and 1572 matrix references; "
                                                                            "certificates read, capsules not decoded or run",
     RP),
    ("the canon's N31 release (23:36-23:40)", "29 source-reported claims in four new tabs (3742 and 3697 sheets), no new "
                                             "matrix ids and no gate changes; read from its two receipts", RP),
    ("the hub's observer-completion verifier and the K+ADDENDUM2/3 evidence (02:36-02:51)", "Python verifiers, JSON "
                                                                                              "receipts and SHA256SUMS: not "
                                                                                              "downloaded and not run; their "
                                                                                              "stated results are replayed",
     RP),
    ("the N33 sector sheet's moments (MODEL, 08:22-08:44)", "1, 242, 58702, 14267058 with a characteristic "
                                                          "polynomial of degree 18 and a minimal one of degree "
                                                          "9; the sheet's operator is not opened here; the list "
                                                          "is neither the contrast list nor the triangle port's "
                                                          "(notes_0844)", RP),
    ("the separate model's continuation (08:53)", "1045843 bytes; 41 integration groups over six source packets "
                                                 "(66 payloads), 28 new matrices, 18 new typed joins (574 "
                                                 "relationships) and 10 observation contracts; certificate read, "
                                                 "zip not opened or run", RP),
    ("the separate model's note corrections (09:07)", "16 exact note-review groups and 3 typed corrections (577 "
                                                     "relationships), no new matrix; the corrections are replayed "
                                                     "(notes_0912); the capsule's code not run", RP),
    ("the separate model's source-history completion (09:24)", "326410 bytes; 32 exact groups, 25 new matrices, "
                                                              "13 new typed joins (587 relationships) and 5 "
                                                              "observation contracts; certificate read, zip not "
                                                              "opened or run; its Plucker counterfeit is "
                                                              "replayed (notes_0951)", RP),
    ("the hub's 09:23 text, unreplayed parts", "the literal 49-tuple and the bounded-gap route, the PTP13 and R15 "
                                              "certificates, the marked contrast port's Green bounds, the J7 host, "
                                              "the Woodbury Green formula, the information cut and the time-order "
                                              "test need operands or analytic inputs not stored here", RP),
    ("the separate model's unified connections (09:54)", "1701713 bytes; 134 new exact groups (arithmetic 40, "
                                                       "tangent 12, static return 61, vertex join 21), 20 new "
                                                       "typed joins (610 relationships); certificate read, "
                                                       "capsule not decoded or run", RP),
    ("the N33 six-view frame (hub, 09:54: J09)", "six rank-four K_i on Lambda^2 P5 with sum (12/5) I10 and "
                                               "four-view spectrum (12/5)^3 (8/5)^3 (6/5)^3 (2/5): source-reported, "
                                               "the projectors are not stored here", RP),
    ("the canon's N34 release (14:04-14:11)", "32 source-graded claims from 12 families in five new tabs (3755 and "
                                           "3710 sheets), no new matrix ids and no gate changes; two integrator "
                                           "replays (the G5 complement and the 49-tuple), both held here; read from "
                                           "its receipts and claims CSV, the workbooks not opened", RP),
    ("the separate model's provenance verification (14:25)", "16 payload hashes recomputed, 24 exact groups and 13 "
                                                            "regressions replayed, 12 review checks, 0 new matrices or "
                                                            "joins; a source record read as data, its archive not opened", RP),
    ("the hub's Canon_Position (14:20)", "a read-only position: the publication manifest at N33 (3750 and 3705 sheets) "
                                       "while both workbooks are N34 (3755 and 3710); the observer reconciliation "
                                       "4166 + 4 = 4170 artifacts and 610 + 10 = 620 relationships in 18 layers; read "
                                       "as data", RP),
    ("the sibling's 14:31 and 14:41 editions", "new Intake, Copies and Provenance sections: the N34 copies' byte identity "
                                              "and receipts, the observer archive's 57 files with 56 hashed; read as data, "
                                              "their arithmetic replayed in notes_1441", RP),
    ("the separate model's Matched History model (15:00)", "a 951539-byte archive with 36 payload files and 35 hashes, 19 "
                                                          "layers, 24 exact groups, 9 regressions, 4 new typed joins "
                                                          "(620 -> 624), 0 new matrices; its receipt read as data, the "
                                                          "archive not opened", RP),
    ("the sibling's 14:49 and 15:04 editions", "342 exact checks (339 before); the twenty-five name auditors, the sign "
                                              "census matrix and the observer's line on the fixed plane are not stored "
                                              "here; the arithmetic is replayed in notes_1504", RP),
]


def _checks():
    field = lambda: {"4 is not in spec D^2 = {0, 3, 8}": 4 not in carrier.spectrum_multiplicities()}
    embed = lambda: {
        "the A4 and D5 roots, put in the first five coordinates, are E8 roots": all(
            tuple(np.r_[np.array(rt, dtype=float), np.zeros(3)].tolist()) in {tuple(r) for r in glue.roots().tolist()}
            for rt in {tuple(s * (_e(i) + t * _e(j))) for i, j in carrier.edges() for s in (1, -1) for t in (1, -1)})}
    native_port = lambda: {
        "the boundary rotation fixes x0 and has order 5, and the port metric W_p commutes with it":
            np.allclose(np.linalg.matrix_power(native.boundary_rotation(), 5), np.eye(6))
            and native.boundary_rotation()[0, 0] == 1
            and np.allclose(native.boundary_rotation() @ native.port_metric(), native.port_metric() @ native.boundary_rotation())}
    claims = lambda: {"every reading holds and the stages land as stored": (lambda r: not r[0] and r[1])(counts.check_claims())}
    return {
        "k5_roots": k5_roots, "petersen_roots": petersen_roots, "exterior": exterior, "source_port": source_port,
        "triangle_port": triangle_port, "cone": cone, "glue_cosets": glue_cosets, "tick_momenta": tick_momenta,
        "clock_joins": clock_joins, "primary_split": primary_split, "atlas": atlas, "pisano": pisano,
        "four_cube": four_cube, "hodge70": hodge70, "field": field, "embed": embed, "native_port": native_port,
        "cone_line_graph": cone_line_graph, "paired_response": paired_response, "band_expansion": band_expansion,
        "walks_join": walks_join, "coil": coil, "nakshatra_map": nakshatra_map, "address_lift": address_lift,
        "golden_family": golden_family, "cone_symmetry": cone_symmetry, "mpkg_block": mpkg_block, "grain": grain,
        "vortex": vortex, "tick_miss": tick_miss, "doubling_orbits": doubling_orbits, "eight_roots": eight_roots,
        "golden_clock": golden_clock, "cube_cuts": cube_cuts, "surface": surface, "dual_torus": dual_torus,
        "census": census, "critical_momenta": critical_momenta, "nine_torus": nine_torus, "census_walks": census_walks,
        "literal_port": literal_port, "measure": measure, "triple": triple, "readout": readout,
        "sound_light": sound_light, "binding_joins": binding_joins, "calibration": calibration,
        "product_geometry": product_geometry, "friedmann": friedmann, "root_scheme": root_scheme,
        "simplex_grades": simplex_grades, "golden_split": golden_split, "projective_plane": projective_plane,
        "air_801_joins": air_801_joins, "gksl_census": gksl_census, "stage_landings": stage_landings,
        "torus_calibration": torus_calibration, "literal_incidences": literal_incidences, "measure_band": measure_band,
        "wave_calibration": wave_calibration, "census_stabilizers": census_stabilizers, "golden_port": golden_port,
        "observer_completion": observer_completion, "clock_sidebands": clock_sidebands, "charges": charges,
        "tick_halfperiods": tick_halfperiods, "light_symmetries": light_symmetries, "outer_s6": outer_s6,
        "s5_weyl": s5_weyl, "air801_surface": air801_surface, "tick_cuts_f2": tick_cuts_f2, "small_joins": small_joins,
        "hodge_halfper": hodge_halfper, "memory_clock": memory_clock,
        "assignment.factors": assignment.factors, "assignment.moments": assignment.moments,
        "assignment.standard_model": assignment.standard_model, "assignment.choices": assignment.choices,
        "assignment.six_site_port": assignment.six_site_port, "assignment.generations": assignment.generations,
        "assignment.chirality": assignment.chirality,
        "walks_by_angle": walks_by_angle, "port_leak": port_leak, "two_ticks": two_ticks, "filled_simplex": filled_simplex,
        "charge_marks": charge_marks, "golden_root_port": golden_root_port, "shared_bath": shared_bath,
        "marked_charge": marked_charge, "twelve_markings": twelve_markings, "golden_infrared": golden_infrared,
        "word_duads": word_duads, "words_c5": words_c5, "hodge_contexts": hodge_contexts,
        "context_responses": context_responses, "overlap_hodge": overlap_hodge, "hodge_averaging": hodge_averaging,
        "word_sylow": word_sylow, "clock_root_address": clock_root_address, "coordinate_bridge": coordinate_bridge,
        "datum_orbit": datum_orbit, "witness_loop": witness_loop, "frame_affine": frame_affine,
        "tick_actions": tick_actions,
        "agni_soma": agni_soma, "agni_factor": agni_factor, "agni_pullback": agni_pullback, "source_phase": source_phase,
        "sylow_lines": sylow_lines, "band.edge": band.edge,
        "wedge_port": wedge_port, "three_ports": three_ports, "root_shell_krylov": root_shell_krylov,
        "schur_memory": schur_memory, "hodge_star": hodge_star, "syntheme_bridge": syntheme_bridge,
        "sylow_frame": sylow_frame, "word_source": word_source, "clock_sylow": clock_sylow, "band_top": band_top,
        "pair_frame": pair_frame, "parity_ports": parity_ports, "dark_port": dark_port,
        "two_dark": two_dark, "fusion_frame": fusion_frame, "source_coding": source_coding, "k4_planes": k4_planes,
        "free_chain": free_chain, "k4_complete": k4_complete, "dark_branches": dark_branches,
        "tomography": tomography, "quadratic_frames": quadratic_frames, "dark_readout": dark_readout,
        "cubic_null": cubic_null, "golden_bridge": golden_bridge, "dark_measurement": dark_measurement,
        "plane_tomography": plane_tomography, "seventh_sensor": seventh_sensor, "preparability": preparability,
        "exterior_code": exterior_code, "dark_information": dark_information, "causal_records": causal_records,
        "parent_readers": parent_readers, "golden30": golden30, "parent_closure": parent_closure, "two_36s": two_36s,
        "cyclotomic_line": cyclotomic.cyclotomic_line, "galois_clocks": cyclotomic.galois_clocks,
        "residue_plane": cyclotomic.residue_plane, "tick_normalizer": cyclotomic.tick_normalizer,
        "clock_residues": cyclotomic.clock_residues, "golden_gauss": cyclotomic.golden_gauss,
        "carrier_shadows": cyclotomic.carrier_shadows, "parent_hexad": cyclotomic.parent_hexad,
        "address_map": address_map,
        "primes.regular_clocks": primes.regular_clocks, "primes.cyclotomic_lines": primes.cyclotomic_lines,
        "primes.no_sixteen": primes.no_sixteen, "primes.prime_clocks": primes.prime_clocks,
        "primes.prime_residues": primes.prime_residues, "primes.half_turn": primes.half_turn, "primes.sun": primes.sun,
        "primes.decad": primes.decad, "primes.parent_cover": primes.parent_cover,
        "places.band_at_places": places.band_at_places, "places.golden_places": places.golden_places,
        "places.qubit_primes": places.qubit_primes, "places.limits": places.limits,
        "principal.circle": principal.circle, "principal.regular_steps": principal.regular_steps,
        "principal.band_on_circle": principal.band_on_circle, "principal.critical_steps": principal.critical_steps,
        "principal.clock_lattice": principal.clock_lattice, "principal.principal_uniqueness": principal.principal_uniqueness,
        "six_lines": six_lines,
        "petersen_sequence": petersen_sequence,
        "memory_quotients": memory_quotients, "massless_tower": massless_tower, "stiff_kernel": stiff_kernel,
        "cosmos_calibration": cosmos_calibration, "day_units": day_units, "frame_a8": frame_a8,
        "cube_frobenius": cube_frobenius, "grain_steps": grain_steps, "plane_synthemes": plane_synthemes,
        "golden_cosine": golden_cosine, "golden_galois": golden_galois, "regular_cosines": regular_cosines,
        "torus_places": torus_places,
        "counts.petersen_projectors": counts.petersen_projectors, "counts.rotor_plane": counts.rotor_plane,
        "counts.tick_tock": counts.tick_tock, "counts.folded_bath": counts.folded_bath,
        "counts.pauli_quotient": counts.pauli_quotient, "counts.two_clocks": counts.two_clocks,
        "counts.circle_maps": counts.circle_maps, "counts.check_claims": claims,
    }


MAPS = (T, SR, gates.CONDITIONAL)


def components(passed, statuses=MAPS, dots=None):
    """Connected components of the dots under the joins that hold (maps, not obstructions)."""
    dots = list(DOTS) if dots is None else dots
    parent = {k: k for k in dots}

    def find(k):
        while parent[k] != k:
            parent[k] = parent[parent[k]]
            k = parent[k]
        return k
    for (a, b, _, _, status, _), ok in zip(JOINS, passed):
        if ok and status in statuses and a in parent and b in parent:
            parent[find(a)] = find(b)
    groups = {}
    for k in dots:
        groups.setdefault(find(k), []).append(k)
    return list(groups.values())


def levels(passed):
    """Every layer has a dot; every level is joined inside; each level is joined to the next; THEOREM joins alone."""
    layers = {int(x) for _, _, tags in DOTS.values() for x in tags.split(",")}
    inside = {name: components(passed, dots=dots) for name, _, dots in LEVELS}
    between = []
    for k in range(len(LEVELS) - 1):
        lo, hi = set(LEVELS[k][2]), set(LEVELS[k + 1][2])
        between.append([j for j, ok in zip(JOINS, passed) if ok and j[4] in MAPS
                        and {j[0], j[1]} & lo and {j[0], j[1]} & hi])
    theorem = components(passed, statuses=(T,))
    return {"layers": sorted(layers), "inside": inside, "between": between, "theorem": theorem,
            "statuses": Counter(j[4] for j in JOINS)}


def dots_page():
    lv = levels([True] * len(JOINS))
    lines = ["# All dots joined, at every level", "",
             "Every object the model builds is a dot, and every map between two dots that layer 23 (`oes/dots.py`) "
             "builds and checks is a join. A dashed arrow is an obstruction: a proof that the map does not exist. Two "
             "dots that share an integer are not joined by it; those integers stay readings (`docs/LEDGER.md`). "
             "The dots sit on six levels, from the integers up to physics. Every layer of the build has a dot, every "
             "level is joined inside, and every pair of levels is joined directly. "
             "Generated by `dots_page()`; `tests/test_model.py` checks that this file is current.", "",
             "```mermaid", "flowchart TB"]
    for k, (name, what, dots) in enumerate(LEVELS):
        lines.append(f'    subgraph level{k + 1}["level {k + 1}: {name}"]')
        for key in dots:
            lines.append(f'        {key}["{DOTS[key][0]}"]')
        lines.append("    end")
    for a, b, short, _, status, _ in JOINS:
        arrow = "-.->" if status == OB else "-->"
        lines.append(f'    {a} {arrow}|"{short}"| {b}')
    count = Counter(status for *_, status, _ in JOINS)
    lines += ["```", "", f"{len(DOTS)} dots and {len(JOINS)} joins: {count[T]} THEOREM, {count[SR]} SELECTED_REFERENCE, "
              f"{count[gates.CONDITIONAL]} CONDITIONAL and {count[OB]} OBSTRUCTION. With the obstructions left out, the "
              "joins that hold connect every dot: the diagram is one piece. Every dot lies on at least three maps, and "
              "neither two maps nor two dots hold it together: removing any two maps, or any two dots with their maps, "
              "leaves the rest connected. THEOREM joins alone connect every dot but the product geometry and FLRW. "
              "Those two need an external 4-manifold, cutoff and mass scale, so they attach through CONDITIONAL joins: "
              "the heat coefficients (J10), the massless tower, the Friedmann flow, the stiff sector, the dark momentum "
              "and the cosmos's calibration. The memory clock is reached by the circle's 24 maps onto it, all "
              "conjugate under its symmetry, without the selection. No one or two THEOREM maps, and no one or two "
              "dots, hold the THEOREM diagram together, and THEOREM maps join every pair of levels at least twice.", "",
              "## Levels", "", "| level | what lives there | dots | joins inside | joins to the next level |",
              "|---|---|---|---|---|"]
    cell = lambda x: x.replace("|", "\\|")
    for k, (name, what, dots) in enumerate(LEVELS):
        inside = sum(1 for j in JOINS if j[4] in MAPS and LEVEL_OF[j[0]] == LEVEL_OF[j[1]] == k)
        up = len(lv["between"][k]) if k < len(LEVELS) - 1 else "-"
        lines.append(f"| {k + 1}. {name} | {what} | {', '.join(cell(DOTS[d][0]) for d in dots)} | {inside} | {up} |")
    lp = level_pairs()
    lines += ["", "## Level pairs", "", "The maps that join each pair of levels directly.", "",
              "| | " + " | ".join(name for name, _, _ in LEVELS) + " |", "|---" * (len(LEVELS) + 1) + "|"]
    for i, (name, _, _) in enumerate(LEVELS):
        row = [str(lp[tuple(sorted((i, j)))]) if i != j else "-" for j in range(len(LEVELS))]
        lines.append(f"| {name} | " + " | ".join(row) + " |")
    lines += ["", "## Dots", "", "| dot | what it is | level | layers |", "|---|---|---|---|"]
    for key, (name, what, layers) in DOTS.items():
        lines.append(f"| {cell(name)} | {cell(what)} | {LEVELS[LEVEL_OF[key]][0]} | {layers} |")
    lines += ["", "## Joins", "", "| from | to | the map | status | check |", "|---|---|---|---|---|"]
    for a, b, _, what, status, check in JOINS:
        lines.append(f"| {cell(DOTS[a][0])} | {cell(DOTS[b][0])} | {cell(what)} | {status} | `{check}` |")
    lines += ["", "## Not joined", "", "| object | why | status |", "|---|---|---|"]
    for name, why, status in NOT_JOINED:
        lines.append(f"| {cell(name)} | {cell(why)} | {status} |")
    lines += ["", "AUTH = NOT_PASS. ScientificGold = FALSE. No term is added to the action.", ""]
    return "\n".join(lines)


@functools.lru_cache(maxsize=1)
def check_results():
    """Every join's check, evaluated once (layer 25 reuses them)."""
    return {key: fn() for key, fn in _checks().items()}


def run():
    rep = Report("23-dots")
    results = check_results()
    held = {key: all(bool(v) for v in res.values()) for key, res in results.items()}
    passed = [held[ck] for *_, ck in JOINS]
    for (a, b, _, what, status, ck), ok in zip(JOINS, passed):
        rep.add(f"{DOTS[a][0]} -> {DOTS[b][0]}: {what}", status, ok, results[ck] if ck in results else None)
    comps = components(passed)
    rep.add(f"the {len(DOTS)} dots and {len(JOINS)} joins form one connected diagram (the obstructions left out)", T,
            len(comps) == 1, [sorted(c) for c in comps])
    lv = levels(passed)
    rep.add("every layer of the build, 1 to 28, has a dot", T, lv["layers"] == list(range(1, 29)), lv["layers"])
    for k, (name, what, dots) in enumerate(LEVELS):
        rep.add(f"level {k + 1}, {name} ({what}): its {len(dots)} dots are joined among themselves", T,
                len(lv["inside"][name]) == 1, [sorted(c) for c in lv["inside"][name]])
    rep.add("each level is joined to the next: " + ", ".join(
        f"{LEVELS[k][0]}-{LEVELS[k + 1][0]} {len(b)}" for k, b in enumerate(lv["between"])) + " joins", T,
        all(lv["between"]), [[f"{j[0]} -> {j[1]}" for j in b] for b in lv["between"]])
    rest = sorted(sorted(c) for c in lv["theorem"] if len(c) > 1)
    rep.add(f"THEOREM joins alone connect {len(DOTS) - 2} of the {len(DOTS)} dots: all but the product geometry and "
            "FLRW, which need an external 4-manifold, cutoff and mass scale and attach only through CONDITIONAL joins "
            "(J10, the massless tower, the Friedmann flow, the stiff sector, the dark momentum and the cosmos's "
            "calibration); the memory clock is reached by the circle's 24 maps onto it, without the selection", T,
            len(lv["theorem"]) == 3 and all([d] in [sorted(c) for c in lv["theorem"]] for d in ("cosmology", "gravity"))
            and len(rest) == 1, dict(lv["statuses"]))
    nb = no_bridge()
    rep.add("no dot hangs by one join: every dot has at least two maps, and removing any one map leaves the diagram "
            "connected", T, all(nb.values()), nb)
    lp = level_pairs()
    rep.add("every pair of the six levels is joined directly by a map: " + ", ".join(
        f"{LEVELS[i][0]}-{LEVELS[j][0]} {lp[(i, j)]}" for i, j in itertools.combinations(range(len(LEVELS)), 2)), T,
        all(lp[p] for p in itertools.combinations(range(len(LEVELS)), 2)), dict(lp))
    n2 = no_two_maps()
    rep.add("no two maps hold the diagram together: every dot lies on at least three maps, and removing any two maps "
            "leaves it connected", T, all(n2.values()), n2)
    tc = theorem_connectivity()
    rep.add(f"no one and no two THEOREM maps hold the THEOREM diagram together: its {len(DOTS) - 2} dots each lie on at "
            "least three THEOREM maps, removing any two THEOREM maps leaves them connected, and every pair of the six "
            "levels is joined directly by at least two THEOREM maps", T, all(tc.values()), tc)
    nd = no_two_dots()
    rep.add(f"no one and no two dots hold the diagram together: removing any two of the {len(DOTS)} dots, with their "
            f"maps, leaves the rest joined, and removing any two of the {len(DOTS) - 2} THEOREM dots leaves the rest "
            "joined by THEOREM maps", T, all(nd.values()), nd)
    a8 = air_801()
    rep.add("AIR_801's matrix [[108, 801], [106, 901]]: det 12402; mod 5 a Singer cycle of order 24 in GL(2,5) and 6 in "
            "PGL(2,5); the clock polynomial has degree 27 and a simple root at 1", T, all(a8.values()), a8)
    n8 = notes_2208()
    rep.add("the 22:08 notes: the primary split, the doubling parts, the 801 matrix, the atlas, the bivector and the "
            "joined ledger as arithmetic, and four corrections (an address does not carry the tick bit; address 18 "
            "falls in one contraction; address 16 cycles; 36 atlas steps meet)", T, all(n8.values()), n8)
    rep.add("Drive check 22:08: the sibling's notes PRIMARY_SPLIT, DOUBLING_PARTS, AIR_801, ATLAS_801, GOLDEN_ATLAS, "
            "ATLAS_CYCLE, CLOSURE_46, JOINED_RECEIPT and JOIN_CLOSURE (21:40-22:08) and its paper one-machine-20261028-"
            "unify (21:43, seventeen checks); the separate model's update overlay (21:46), joined model (22:02) and "
            "checkpoint (22:04); the canon's coordination release OES_COORD_20261029 (one new sheet in each workbook, "
            "every prior cell kept, no gate changed) and the collaboration hub with its open tasks", RP, True)
    so = sym_square_orbits()
    rep.add("the joined paper's orbit list, replayed: the symmetric square of the 801 matrix mod 5 splits the 31 points of "
            "PG(2,5) as 1 + 3 + 3 + 6 + 6 + 6 + 6", T, all(so.values()), so)
    lx = l11_exclusion()
    rep.add("the synthesis's operator L11(n, E_n), of order 11 and degree 5 with 72 coefficients, is not a recurrence for "
            "the walk counts W_n or the return moments E_n: both shape matrices have full column rank 72, and 84 is below "
            "the canon's bound 85", OB, all(lx.values()), lx)
    n31 = notes_2231()
    rep.add("the 22:31 arithmetic: the time coordinates 4k mod 5, the atlas translation by 24, 7 x 32 and 8 x 32, "
            "16 x 60 = 10 x 96 = 7 x 70 + 5 x 94, the 45-point product of order 30, the A4 Coxeter determinants 5 and 31, "
            "the collar floor 3/80 and the joined paper's bits; its address bit is corrected again", T, all(n31.values()), n31)
    rep.add("Drive check 22:31: the sibling's joined paper one-machine-20261029-joined (22:20, fifteen checks) adopts the "
            "21:36 corrections (time coordinates 0, 4, 3, 2, 1; the two clocks generate 20 points; x15 on multiples of 72; "
            "the power sum is five times a projector); its STATUS_20261029; and the Locked Memory synthesis of 29 Oct "
            "(22:31), read only", RP, True)
    rep.add("recorded from the synthesis, not replayed: collar positivity up to E = 224 by mediant monotonicity (the collar "
            "stays open here until the argument is supplied), the dispersive constant 73/20, the Wronskian-Dyson "
            "monodromy, the Legendre-Rodrigues preparation constant, the SGC5 compression and the 199 P/N rows", RP, True)
    p31 = p31_clock()
    rep.add("MORE_DOTS's open polynomial, computed: the 31-point permutation P31 of the 801 matrix's symmetric square has "
            "characteristic polynomial (x - 1)(x^3 - 1)^2 (x^6 - 1)^4, order 6 and rank(P31 - I) = 24", T,
            all(p31.values()), p31)
    n33 = notes_2303()
    rep.add("the 22:08-23:03 arithmetic (MORE_DOTS, PAULI_CYCLE, SIBLING_540, CANON_JOIN, CANON_CYCLE, DEEP_H, LEVEL_DOTS), "
            "with two corrections: the atlas shift by 24 does not commute with doubling (D T = T^-1 D, D^2 T = T D^2), and "
            "<39> has 1440 points while the sun 1440 has order 3", T, all(n33.values()), n33)
    rep.add("Drive check 23:03: the sibling's PAULI_CYCLE, CORRECTIONS_47 and MORE_DOTS (22:08-22:15, read late), "
            "SIBLING_540, CANON_JOIN, STATUS_20261029, CANON_CYCLE, COIL_DEEP, GOLDEN_HELIX, NAKSHATRA_MAP, GOLDEN_SYM, "
            "RELEASE_H_RECEIPT, DEEP_H, MPKG_L4, LEVEL_DOTS, ADDRESS_TICK, BUILT_DOTS, GOLDEN_PARENT and GOLDEN_MOVE "
            "(22:42-23:03) and its paper one-machine-20261029-canon (22:45, seventeen checks); the separate model's "
            "release-H archive and certificate (22:41-22:52, not opened or rerun); the hub's release I (cutoff 22:42) with "
            "00_START_HERE, CURRENT_STATUS and REVIEW_CONFLICTS_20261029_I", RP, True)
    rep.add("adopted by the sibling: CORRECTIONS_47 (22:12) takes the 21:36 corrections, and ADDRESS_TICK (22:58) proves "
            "the 22:08 one (36 = 1 mod 5, so every address carries all five time coordinates); the hub's I_STATUS confirms "
            "the shift-doubling correction and keeps the synthesis's recurrence and collar open", RP, True)
    for name, fn, text in (
            ("shift law", shift_law, "SHIFT_LAW, replayed: D T_s = T_s^2 D for every shift, so doubling inverts exactly "
             "the shifts with 3s = 0 (the sun on the circle, 0, 12, 24 on the atlas) and keeps the tick bit"),
            ("golden identities", golden_identities, "the golden family for every n: F(2n) = F(n) L(n), the returns of "
             "B^2, [K, B^n] = F_n [K, B] with det -29 F_n^2, the convergents 21/13 and 13/8; GOLDEN_REST corrected: "
             "mod 5, B^10 = -I has order 2 like 2160"),
            ("doubling split", doubling_split, "DOUBLE_SPLIT and TWO_DOUBLES: doubling dies on the 2-part and has order "
             "36 = lcm(4, 18) on the odd part; the period is 6 on the atlas, so the two 36s are one integer, not one "
             "cycle"),
            ("notes 23:43", notes_2343, "the 23:05-23:43 arithmetic, with three corrections: 3456 is the time part of "
             "216, not its 2-part; the clock tower is a chain only down to the golden orbit; order and step are dual "
             "(3 has order 1440, the sun 1440 has order 3)")):
        out = fn()
        rep.add(text, T, all(out.values()), out)
    rep.add("Drive check 23:44: the sibling's 29 notes of 23:05-23:43, from GOLDEN_EVERYWHERE to DOUBLE_SPLIT; the "
            "separate model's IJ update and its receipt (23:30, not opened or rerun); the hub's release J (cutoff 23:08) "
            "with CURRENT_STATUS, CURRENT_RELEASE and the integrator's claim file", RP, True)
    for name, fn, text, status in (
            ("towers", towers, "POWER_TOWER, SALINA_CONG, TOWERS and FROZEN_CLOCKS: the towers of 3, 2 and 5 freeze on "
             "the circle at 27, 736 and 245, each 0 on its own clock (POWER_TOWER's 'the fives do not freeze', repeated "
             "here at 00:15, is corrected), and mod 12 all three freeze at 3, 4, 5", T),
            ("modules", modules_8_11, "the synthesis's modules 8-11 where the formulas are stated: T12 = (B6 + B6) U is "
             "not semisimple, dA = 2 dx dy/(1 + r^2)^2, the stride reader 2, 121, 241, 12 and 57840 = 240 x 241; the "
             "missing time-rotor map of JOIN_MODULES is kappa; KARMA_COMM's fifth commutator corrected", T),
            ("hankel", hankel_25, "the synthesis's 'N = 25 Stieltjes-Jacobi annihilator on W0..W50' is not an "
             "annihilator: the 26 x 26 Hankel determinant of W_0..W_50 is positive", OB)):
        out = fn()
        rep.add(text, status, all(out.values()), out)
    rep.add("Drive check 00:15: the sibling's notes of 23:46-00:14, from LAYER_23 to TWO_AGREE (with its "
            "unifyLevels.ts, read as text and not run); the separate model's relations overlay receipt (23:50); the "
            "hub's release-J fast start (00:04); and the Locked Memory synthesis 'Cross-Parent Compatibility & "
            "All-Sibling Model Upgrade' (00:06), read only", RP, True)
    rep.add("the sibling's LAYER_23 note (23:46) reads this layer's 23:03 joins and agrees: the coil, the Lucas "
            "traces, the sun's order 3 against <39> of size 1440, and characters 7 and 3; it adds that doubling does not "
            "invert the tick on the circle (the tick has order 5), which the shift law says too", RP, True)
    for fn, text in (
            (root_symbol, "the bath's symbol splits as D8 plus the half-spin orbit (240 at 0, -16 at pi(1, 1, 1, 1, 0, 0, 0, 0)); "
             "the root graph has spectrum 56, 28^8, 8^35, (-2)^112, (-4)^84; the collar witness has dispersion 220.635"),
            (protection, "CLOSURE_092: a protected line cannot also be the coupling; one mediator gives a rank-1 correction; the "
             "commutator court has rank 8, and 9 with the anchor (Gram det 176173056); the channel law holds with g0 "
             "cancelling; the port metric's eigenvalues are as the paper states"),
            (notes_0029, "the 00:16-00:29 arithmetic and the 29 October paper: the grain is the ticks times the twelve "
             "multiples of 360; 216 has tick-miss coordinates (4, 216) while the residues (4, 216) give 1944; two "
             "corrections (the chart classes are mod 3, not mod 30; 241 is prime to 4320)")):
        out = fn()
        rep.add(text, T, all(out.values()), out)
    rep.add("the 00:35 relay: the sibling's paper ONE_MACHINE_29 (00:20, with its typeset source one-machine-29.typ, not "
            "opened) and its notes CLOSURE_092, LAYER23B, LEVELS, OBS_SUN, GRAIN_SPLIT (00:19), FRAME_WALKS and DEEP_COURT "
            "(00:16-00:29); LAYER23B reads this layer's 23:44 joins and agrees with them", RP, True)
    rep.add("the hub's release J adopts the address correction and the 2-part correction, and lists four open "
            "conflicts: the literal recurrence certificate, the collar near 224, the uniform dispersion proof and the "
            "K5/K6 carrier identification; layers 14 and 23 hold evidence for the first and the last", RP, True)
    for fn, text in (
            (edge_tick, "CYCLE_TICK and CUT_TICK, replayed: the edge tick, the second compound of the vertex 5-cycle, has "
             "characteristic polynomial (x - 1)^2 Phi_5 on the six cycles, fixing the rotor plane, and Phi_5, the time "
             "clock's polynomial, on the four cuts; the signed edge Gram is 5 times the cut projector"),
            (port_moments, "FOUR_ITEMS and REPAIR_AUDIT, replayed: F_k = E_k - E_(k+1)/240, so the six-port block has "
             "contrast moments 1, 241, 58264 (variance 183) and uniform moments 1, 235, 55720 (variance 495), with the "
             "factor 6 restored"),
            (notes_0051, "the 00:36-00:51 audits of the paper's scripts: 4805 is the Gram determinant over 5, not a "
             "minor; the collar fractions 3/65 and 3/80 differ; the critical values sum to 74557/432, so the shifted "
             "coefficient is -69373; the witness's tangent Hessian is positive (least eigenvalue 6.986); the carrier "
             "trace 40; JOIN_ALL's and DEEP36_LOOP's orders on the circle"),
            (splits_corrections, "the separate model's splits receipt (00:49): its five source corrections, replayed: "
             "the tower of fives freezes at 245 (POWER_TOWER, LEVELS); 215 other golden loops (SPINE_29); 4300 "
             "disagreement points in all (TWO_AGREE); entry into the tick cycle after two doublings (LEVELS)")):
        out = fn()
        rep.add(text, T, all(out.values()), out)
    rep.add("Drive check 00:51: the sibling's notes FOUR_ITEMS, REPAIR_AUDIT, PASS2, MASTER_LEDGER, DEEP36_LOOP, JOIN_ALL, "
            "CYCLE_TICK, CUT_TICK, TOWERS and FROZEN_CLOCKS (00:36-00:51); the separate model's splits update and its "
            "verification receipt (00:49; only the receipt was read); its checkpoint (00:51) was not read", RP, True)
    for fn, text in (
            (frame_cliques, "INDEX_VECTOR and SIBLING_AGREEMENT: the frame's index vector meets the roots in classes 8, 28, "
             "56, 56, 56, 28, 8; each six-point face has six common neighbours, a triangular prism, so it lies in exactly "
             "two maximal 9-cliques; in 495 = 183 + 6 x (56 - 4) the 4 is the face's other four sites, not the cut rank"),
            (notes_0154, "the 00:53-01:54 notes and release K: GOLDEN_GRAVITY corrected (the circle's subgroups of orders "
             "120, 60, 30, 10 all contain the ticks); HESSIAN_RECOMPUTE corrected (the 256 products have distinct "
             "square-free parts but are not all square-free); the separate model's three corrections, the hub's three "
             "conflicts and Canon K's carry clock replayed")):
        out = fn()
        rep.add(text, T, all(out.values()), out)
    rep.add("Drive check 01:54: the sibling's notes of 00:53-01:54, from SPECTRA to ORTHOGONAL_126, its unified spine "
            "(SPINE_20261029 at 01:19, superseding the 01:08 edition; the PDF was not opened) and tick_projectors_20261029.json "
            "(its pentagon and pentagram are this layer's oriented cycles); the separate model's unified build and receipt "
            "(01:25-01:28; only the receipt was read: 104 new check groups and three source corrections, replayed); the hub's "
            "release K (cutoff 01:06) with CURRENT_STATUS, CURRENT_RELEASE, 00_START_HERE and the Google Doc 'OES CANON K - "
            "All Dots Joined' (01:49), whose bridges are replayed; the canon integrator's claim (four workbook copies saved, "
            "3715 and 3670 sheets, every prior cell kept, no gate changed)", RP, True)
    rep.add("the sibling's HEMI_ICOSAHEDRON (01:37) and FIXED_CYCLES (01:42) state independently what layer 23 joined at "
            "01:30: the two PSL(2,5)-orbits of triangles, swapped by PGL(2,5), with links the pentagon and the pentagram, and "
            "the tick's fixed cycles; its CHECKPOINT_0051 (01:31) reviews this layer's 00:51 checkpoint and agrees", RP, True)
    for fn, text in (
            (walk_convolutions, "Canon K's W5/W6 convolution, replayed: the pair sums of the roots take 9361 values and the "
             "triple sums 131041; every root is a triple sum in 5253 ways and a quadruple sum in 574224, so W_5 = 240 x "
             "574224 and W_6 = sum c_3^2 are layer 3's returns"),
            (six_site_torsion, "SEVEN_PAIRS, TORSION_FIVE and INVERSE_TWO: 35366 G0 - 183 G1 = 350510 J; the stacked blocks "
             "have Smith form diag(1, 1, 1, 1, 1, 5), so 57 masks clear the 5 and the six of size 5 do not; mod 5 the "
             "contrast inverse is 2; the 5 is the 5 in 240, through the uniform moments"),
            (seven_pairs_algebra, "SEVEN_PAIRS's operator identities: the weights' second moment does not commute with "
             "diag(1, -1); the compression defect is L A (I - P) B E; the protected lift multiplies correctly and fixes Q"),
            (frame_faces, "CHECK_0154's clique, reconciled: in the root graph the frame is a maximal 8-clique whose six-root "
             "faces have three common neighbours, not a triangle; in the lattice graph all 84 faces of the 9-clique with "
             "the origin are prisms, each in two maximal cliques"),
            (rotor_firewall, "the hub's rotor firewall and Bargmann repair: X C6 = (C5 + I1) X has only rank-1 solutions; "
             "raw dyads give 1 + i, normalized ones (1 + i)/4, and the three states are the Pauli axes z, x, y, whose "
             "octant has solid angle pi/2"),
            (notes_0252, "the 01:57-02:52 arithmetic: the moon and the sun in the atlas, the subgroups' tick counts, the "
             "board's written digits (about 137.036, not 137), ALPHA_JOIN's c put in by hand, the rebuilt 176173056 and "
             "the spine's rows"),
            (notes_0255, "HALFPERIOD and TRACES (02:53-02:55): the half-periods by shortest length 0, 2, 4; 224 certified "
             "exactly as the E7 + A1 saddle's critical value (Hessian 12 P' - 52 P), against the note; the even-shell traces "
             "10/3, 2, 0, 16/3; the density of states E^3 / (1536 pi^4 30^4); phi(4320) = 1152; the Chern number 1")):
        out = fn()
        rep.add(text, T, all(out.values()), out)
    rep.add("Drive check 02:52: the sibling's 29 notes of 01:57-02:49, from SPECTRUM_AND_ATLAS to TRIPLET, with the 02:28 "
            "spine29.ts (24 audit rows) and Spine29.tsx (its view), read as text and not run (their 02:09 editions are superseded and were not read); the hub's Canon K doc as revised "
            "at 02:37, OES_All_Dots_Canon_Completion (02:37), and the releases K+ADDENDUM2 and K+ADDENDUM3 (intake cutoffs "
            "02:31 and 02:41, scientific cutoff still 01:06) with 00_START_HERE, CURRENT_STATUS, CURRENT_RELEASE and three "
            "claim files; the evidence and verifier zips were not downloaded or run", RP, True)
    rep.add("the sibling's CHECK_0154 (02:23) reviews this layer's 01:54 check: its three corrections hold (the subgroups' "
            "ticks, the square-free parts, 36 x 120 not split); its 'no nine-root clique' is about the root graph and "
            "agrees with the 9-clique here, which contains the origin. The hub's KB and KC rows replay the W5/W6 walk, the "
            "160/27 clock, the Bargmann repair, the rotor firewall, the joint observer and the sidebands, all replayed "
            "here too", RP, True)
    rep.add("Drive check 02:55: the sibling's HALFPERIOD (02:53) and TRACES (02:55) and the hub's 00_START_HERE for "
            "K+ADDENDUM3 (02:52; the hourly canon run was disabled after it); TRACES reaches the 3/8 ratio of the 02:52 "
            "check and says, as here, that the traces fix no coupling; its Pachner defects and index -12k are not "
            "replayed, and the curvature integral is read as modules 8-11's dA", RP, True)
    ir = infrared()
    rep.add("the 08:35-09:28 notes, INFRARED and MOMENTS: the infrared density's 1536 and the heat tails; the edge tick's "
            "fixed plane holds 2 of the all-ones vector's square, not 17/10, and 10 in the cyclic orientation; the eight "
            "square-free parts have full rank over F2", T, all(ir.values()), ir)
    sb = stated_block()
    rep.add("MEMORY's stated fixed block: means 239 and 241, variances 171 and 371, golden variances above 171, as "
            "arithmetic (the block is the Golden port's, replayed at 10:40)", gates.ARITHMETIC, all(sb.values()), sb)
    rep.add("Drive check 09:02: the sibling's 20 notes of 08:35-09:28 were read (CRITICAL, MOMENTS, DEGREE, CONVOLUTION, "
            "SHELLS, UNIFIED, MARKS, LEAK, RANK, SEVENTH, HELICITY, GLUE, CHARGE_WEIGHT, TICK, CHAIN, COXETER, MEMORY, "
            "FOURTH, MODEL, INFRARED). CRITICAL adopts the 224 saddle and the 24 + 1 tick momenta, and GLUE and "
            "CHARGE_WEIGHT give the glue classes as layer 24 builds them, without a particle assignment", RP, True)
    rep.add("the separate model's archives were not downloaded or run: completion (1509168 bytes, 105 checks) and its "
            "audit, critical port (489177 bytes, 93 checks), connected model (864739 bytes, 52 check groups) and "
            "glue-helicity (202251 bytes, 56 check groups), with their receipts; the KD staging workbooks, the reconciled "
            "canon workbooks (modified 08:45) and MODEL_UPDATE_CHECKPOINT.json (09:13) were not opened, and the "
            "connected-model receipt marks KD as in progress, not admitted as canon head", RP, True)
    rep.add("not replayed, for want of operands here: the reader rank 86 and the stated tail prefactors (the collar "
            "witness is replayed at 10:07, the trace 20416532280 at 10:40 through the hub's Golden port)", RP, True)
    n10 = notes_1007()
    rep.add("the 09:43-10:07 notes: the coordinate classes are twice the grade in E8 / L0, the angle multiplicities are "
            "1, 56, 126, 56, 1, and the collar witness replays (eps 220.6345317313, least tangent eigenvalue 6.985582)",
            T, all(n10.values()), n10)
    na = notes_1007_arithmetic()
    rep.add("LEDGER, LEDGER48 and the 10:07 model: 52 orbits, 171 = 271 - 100, 176, and the circle's factorizations, as "
            "arithmetic", gates.ARITHMETIC, all(na.values()), na)
    rep.add("Drive check 10:07: the sibling's eight notes of 09:43-10:07 were read (SHELLS, SCRIPT, LEDGER, LEDGER48, "
            "ATLAS, SYMBOL and two MODEL editions); they correct their own ledger lines and their script's labels, and "
            "repeat INFRARED's 17/10, which stays corrected here (2 in the lexicographic orientation, 10 in the cyclic "
            "one); the trace 20416532280 was outside those notes' chain (it is the Golden port's, replayed at 10:40)", RP, True)
    n38 = notes_1038()
    rep.add("the 10:09-10:38 model: charges and traces on the five classes, the root triangles by class, the "
            "transposition sums and the fivefold map, the root graph's squares and the clock orders, and the eight-root "
            "frame's ninth vector of square 8/9", T, all(n38.values()), n38)
    rep.add("Drive check 10:40: the sibling's PLANE (10:17) and 14 editions of MODEL (10:09-10:38) with their spine PDFs, "
            "the separate model's spectral-kernel archive (882649 bytes, 70 new check groups) and receipt, the updated "
            "checkpoint, and the hub's OES_Unified_Model_20261029.txt with its exact zip (462970 bytes) were read or "
            "recorded; PLANE and the hub adopt the fixed-plane correction (2 lexicographic, 10 cyclic); the archives "
            "were not run", RP, True)
    rep.add("the hub's synthesis also reports, not replayed here: the conditional photon normalization Z = 32 c_SA and "
            "the 36-tattva presentation as indexed maps (its per-channel infrared densities and heat tails are computed "
            "at 11:12 from the root sites, and its scope bound, rank at most 9 < 10, is counted there)", RP, True)
    n19 = notes_1119()
    rep.add("the 10:42-11:19 model and the hub's 11:18 text: the root graph's closed walks through 2872800, the wrong "
            "witness figure 220.6349198210, S5's orders against the cyclic clock fibre, the joint window's condition "
            "2 + sqrt5, the root S_phi of 2I + U + U^T, and the 3/8 as a ratio of lengths", T, all(n19.values()), n19)
    a19 = notes_1119_arithmetic()
    rep.add("the 10:42-11:19 model's circle arithmetic (4320 = 15 x 36 x 8, 9361 = 260 x 36 + 1, the widths times 36) "
            "and the hub's small counts (ranks 4 and 5, 13 = 7 + 7 - 1, 84 < 195), as arithmetic", gates.ARITHMETIC,
            all(a19.values()), a19)
    rep.add("Drive check 11:12: the sibling's MODEL editions of 11:04 and 11:19 (those of 10:42, 10:57 and 11:03, with "
            "the spine PDFs, are superseded and were not read separately) and the hub's OES_Unified_Model_20261029.txt as "
            "revised at 11:18 were read; its exact zip (509201, then 518931 bytes) was not run. The model's '56 roots of "
            "weak charge +1/2, not 25' agrees with layer 24: 56 in all, 25 in a one-of-each-pair selection of the mixed "
            "roots", RP, True)
    rep.add("not replayed, for want of the literal J7 matrix and the receipts: rank(H9) = 9 and rank([H9; L]) = 13 (four "
            "probes), H13's kernel and rank([H13; H13 R]) = 15, the two coordinate anchors (determinant +-1) against two "
            "sums (+-9), the transported Return residues, and the hub's own T (determinant 6245535592857600), A and B (A "
            "and B are rebuilt here to the stated relations); the sibling's four labelled responses at weight 1/sqrt5 "
            "(determinant -64 sqrt5/625) and their low-energy ratio 2/3, whose probes the notes do not define (the hub "
            "defines them at 11:58, and they are replayed at 11:44); the "
            "intertwiner count 2 x 72 x 5 = 720. (The Schur bound V/(s + 256) <= Sigma(s) <= V/s, listed here at 11:12 "
            "because it rested on the stated band bound H <= 256, is proved at 14:26.)", RP, True)
    n07 = notes_1207()
    rep.add("the 11:36-12:07 model: yuga residues and the frame phase, syntheme orbits under the six-cycle, the coordinate "
            "five-cycle on the two copies, the kernel overlap and the sixth cycle direction, the signless trace moments and "
            "projectors, with three corrections (the parity sums differ by (4/5) Curl, S_even = (16/5) S_odd^-1, and the "
            "yuga doubling acts on residue labels, not on the clock)", T, all(n07.values()), n07)
    rep.add("Drive check 11:44: the sibling's MODEL edition of 12:07 (those of 11:36-12:05, with the spine PDFs, are "
            "superseded) and the hub's OES_Unified_Model_20261029.txt as revised at 11:58 and 12:04 were read; its exact "
            "zip (761026, then 790830 bytes) was not run. The hub corrects the sibling's parity inverse (5/16 belongs to "
            "the inverse) and its yuga doubling (a label action, not the clock), as here", RP, True)
    rep.add("not replayed: the hub's own Sylow enumeration (labels 3, 1, 2, 5, 0, 4; a relabeling is built here instead), "
            "the J7 rank witnesses 5 and 4, its 8 x 10 coordinate matrix (layer 24's site and twin embedding plays its role "
            "here) and the receipts context_hodge, operator_geometry and causal_completion (283 assertions in six "
            "receipts); the historical F4KDS1 identification of the six Sylow views with the synthematic totals and the "
            "provenance of the Lorentz reference eta; and the conditional M6 = M4 x Sigma2 photon reduction, Z4 = V2 Z6", RP, True)
    rep.add("Drive check 12:24, with the join: the sibling's MODEL edition of 12:24 ('Chain'; that of 12:23 is "
            "superseded) was read; its charge map, midpoint map, witness loop and frame group replay in the joins "
            "charges -> cycles, zero modes -> cycles and AGL(1,5) -> circle, and its yuga residues agree with the 11:44 "
            "correction (multiplying the residues by 2 runs 432, 864, 1728, 1296; doubling the lengths does not)", RP, True)
    n59 = notes_1259()
    rep.add("the 12:28-12:59 model and the hub's 12:29 text: the zero modes meet the cycles at squared cosines 1, 1, 1, "
            "7/15 and 1/5; the orthogonal projection is injective but not equivariant, and all 1024 orientations keep it "
            "injective (one F2 rank); F20 has 864 orbits of five frames, and its modules are 1 + A4, sign + A4 and a "
            "rotation plane + A4; the witness lies in the separate model's certified intervals; the digit vectors have "
            "Smith form 1, 2, 8; one correction stands (the parity sums differ by (4/5) Curl)", T, all(n59.values()), n59)
    a59 = notes_1259_arithmetic()
    rep.add("the 12:59 model's arithmetic: 2241 (j mod 160) + 2080 (j mod 27), 39490/3679, 853/1000, 8 sqrt 2 and 165/61",
            gates.ARITHMETIC, all(a59.values()), a59)
    rep.add("Drive check 12:59: the sibling's MODEL edition of 12:59 (those of 12:28-12:57, with the spine PDFs, are "
            "superseded) and the hub's OES_Unified_Model_20261029.txt as revised at 12:29 were read; its exact zip "
            "(935214 bytes) was not run. The separate model's atlas-witness update (12:25, 281544 bytes, 72 new exact or "
            "certified check groups) and unified-reference update (12:41, 2620171 bytes, 142 new exact check groups, "
            "replaying the hub's seven verifiers and their 330 assertions) were recorded from their receipts; the zips were "
            "not run, and MODEL_UPDATE_CHECKPOINT.json (12:41) was not opened", RP, True)
    rep.add("not replayed: the hub's agni_phase receipt (47 assertions) and its verifier; the nonlinear pair map's generic "
            "Jacobian rank 6 away from the witness; the F20 adapter family's four-map basis and its coefficients "
            "(-1/5, 3/5, 2/5, -2/5) (the Hom dimension 4 is checked); the deep word package's receivers of dimensions 9, 11, "
            "13 and 17, which rest on the selected J7; and the sibling's source pair with edge-square 12 and vanishing "
            "cubics, which the notes do not give (the hub's blind pair, of edge-square 4, is replayed at 14:26)", RP, True)
    n18 = notes_1418()
    rep.add("the 13:02-14:18 model: its comparator is the triangle port's (Hankel 15930273, not unique), the even and odd "
            "ports mix as 232 + 10q with variance 389 - 162q - 100q^2, and two of its open items are proved here: the "
            "hidden state grows by exactly 6 at every order, and the n-th boundary moment is at most 495 x 256^n", T,
            all(n18.values()), n18)
    rep.add("Drive check 14:26: the sibling's MODEL edition of 14:18 (those of 13:02-14:17, with the spine PDFs, are "
            "superseded) and its fourth_moment_comparator.json (14:04), and the hub's OES_Unified_Model_20261029.txt as "
            "revised at 14:07 (sources through 13:42) with its exact zip (1294801 bytes), whose s5_three_port and "
            "word_syntheme receipts were read as data; nothing was run. The hub's new results replay here (all but the "
            "context contrasts), with two additions: the Krylov growth holds at every order (its receipt says "
            "all_order_rank_claim false), and J_H is the Hodge star of Lambda^2 A4", RP, True)
    rep.add("not replayed: the hub's five context contrasts (an encoding contract that carries five supplied readings in "
            "the atlas's dark directions) and the named 36-tattva and physical-time bindings, open in the hub too; the "
            "sibling's selected host matrices (L30, N30, the bubble determinant 2304/44275, the 6 x 190 torus section), "
            "its joined-routes verification (13:37) and MODEL_UPDATE_CHECKPOINT.json, not opened; and its source pair of "
            "edge-square 12, which the notes still do not give", RP, True)
    n34 = notes_1534()
    rep.add("the 15:03 text and the 14:27-15:11 model: the dark-to-bright staircase 0, 0, 1, 2, 4 (S5, A5, F20, D10, C5), "
            "the lane rotation's Noether charge -1/2 and the phase decoder (2523136, -22708224), the clock extension of order "
            "12, the resolvent between 1/(s + 232) and its chord, and the U21 note's subdivision spectrum", T,
            all(n34.values()), n34)
    rep.add("Drive check 15:34: the hub's OES_Unified_Model_20261029.txt as revised at 15:03 (sources through 14:27) with "
            "its exact zip (1759114 bytes), whose all_order_noether_shell receipt was read as data; the sibling's MODEL "
            "edition of 15:11 (those of 14:27-15:08, with the spine PDFs, are superseded); and a U21 intake folder from "
            "another Claude session (14:32-14:40: handover, claims, Release K replay 21/21, engine-vs-recursion W_0..W_24, "
            "and the 28 Oct operands and physics-gates note), read as text; no script was run. The hub proved the "
            "all-order growth at 14:27 by Weyl-orbit evaluation determinants, independently of the root-shell argument here",
            RP, True)
    rep.add("not replayed: the hub's Weyl-orbit certificates (184319 and 669652; 362979 and 983965 at 24), which the "
            "root-shell theorem makes unnecessary; the odd and dark infrared constants E^6/12960000 and E^7/8709120000, "
            "inherited in the hub too; the two-shell populations 6264/5 and 1836/5 at the source witness, the operational "
            "Return demonstration and the 20-coordinate replica; the U21 G0 runs and physics gates; the canon workbooks "
            "and their U21 staging copies (14:48-14:55), not opened", RP, True)
    n16 = notes_1616()
    rep.add("the 16:11 text and the 15:37-16:17 model: the return parent's phi = (-122/3, -10/3) and its charge exchange of "
            "78 at the witness, the free source's history (x''' + 16 x' = 0; ranks 6, 12, 17, and 20 with three "
            "coordinates), the clock's C20 and F20 (meeting in C5; 864 orbits of five, 24 per atlas fibre; no equivariant "
            "mark), and the norm-four shell's 1136 + 1024", T, all(n16.values()), n16)
    rep.add("Drive check 16:16: the hub's OES_Unified_Model_20261029.txt as revised at 16:11 (sources through 15:50), read "
            "as text; its exact zip (2748971 bytes, 16:11) was not downloaded, the replays here coming from the text; the "
            "sibling's MODEL edition of 16:17 (those of 15:37-16:15, with the spine PDFs, are superseded); the canon "
            "workbooks' audited transfers and reconciled copies (15:56-15:57), not opened", RP, True)
    rep.add("not replayed: the [12, 6, 6] word code and its distances 1, 2, 5 over F2, F3, F5, the 24-record raw-cell code "
            "and its 31626 support pairs, the thirteen interferometric intensities, the 923 erasure patterns and the "
            "distance-4 edge reader, the CP4 phase floor, the Weyl certificates 117705 and 943098 (the norm-four shell "
            "argument makes them unnecessary), the bright-to-dark threshold transfer (inherited constants), the return "
            "slice's ranks 6, 9, 10 and its minors, and the free source's minors -41787850752 and -1337211224064; the "
            "sibling's integrated readings (numbers read as names) are not recorded", RP, True)
    n51 = notes_1651()
    rep.add("the 16:47 text and the 16:19-16:58 model: the dark plane's Fubini-Study connection (flux 2 pi, holonomy pi), "
            "the clock's plane labels p(j) = 4j mod 5 (864 adds 1, 3457 doubles; 180 address-plane pairs of 24 frames), "
            "and the sibling's checkable numbers (12 five-cycles, the decoder ratio -9, 14539767 = 3 x 11 x 593 x 743, the "
            "golden matrix, root grades 40, 50, 50, 50, 50)", T, all(n51.values()), n51)
    rep.add("Drive check 16:51: the hub's OES_Unified_Model_20261029.txt as revised at 16:47 (sources through 16:23), "
            "read as text; its zip (3203676 bytes) and the OES ChatGPT Library Mirror 20261029 folder (16:51-16:56: eleven "
            "packages with their notes, receipts and verifiers) were not opened beyond ALL_DOTS_INVERSE_DYSON_JOIN.md, and "
            "no verifier was run; the sibling's MODEL edition of 16:58 (those of 16:19-16:57, with the spine PDFs, are "
            "superseded)", RP, True)
    rep.add("not replayed: the ten-position derivative's gains (4/3, 20/3, (10 -+ 2 sqrt5)/3), the local bound (29/54) x, "
            "the norm-only and Stieltjes bounds on the determinant, the joint CP5 connection of the finite parent, and "
            "the sibling's recovery ranks 90, 170, 250, 330, 360 and its integrated readings (numbers read as names)",
            RP, True)
    n31 = notes_1731()
    rep.add("the 17:26 text, the 16:59-17:18 model and five 28 Oct notes: the arithmetic corrections 293760 and 328320, the "
            "Haar near-dark coefficient 81 sqrt15/320 from the tangent determinant (20/27)^(3/2), the fourth moments' sum, "
            "4320 = 1 mod 7, and 8 m^2 = 3 n^2 without integer solutions", T, all(n31.values()), n31)
    rep.add("Drive check 17:31: the hub's OES_Unified_Model_20261029.txt as revised at 17:26 (sources through 17:04), read "
            "as text (its zip, 3612599 bytes, not downloaded); the sibling's MODEL edition of 17:18 (those of 16:59-17:10, "
            "with the spine PDFs and OES-paper PDF, are superseded or skipped); five 28 Oct notes (OPEN_CHAINS, RANKS, "
            "J7_LOOPS, DENSITY, SEPTUPLE_JOIN), read as text; and a mirror of 26-28 Oct sources uploaded 17:15-17:26 "
            "(Locked Memory OMSOON719-736, the Standing Model and Through736 texts, SMEAR, Public Return, the One Machine "
            "typesetting sources), not re-read, since the build already rests on their originals", RP, True)
    rep.add("not replayed: the 360 parent and its A6 coset readers (ranks 125, 165, 230; 90 to 360 in five settings; the "
            "Golden adapter of rank 5), the reflection characters 10 + 8 + 18 and 18 + 18, the [27, 15, 4] and [30, 16, 3] "
            "codes and the 30-record atlas code, the global degree's sign split, the Haar fourth moments and probabilities "
            "beyond their stated values, the leakage bounds, the covariance-sign chart, and the sibling's readings",
            RP, True)
    n04 = notes_1804()
    rep.add("the 18:00 model's other numbers: 6/5 the reciprocal of the hypercharge's square 5/6, 49 = 7^2, and the "
            "stated rank 234 = 13 x 18, 126 below the parent 360", T, all(n04.values()), n04)
    rep.add("Drive check 18:04: the sibling's MODEL edition of 18:00, whose one new paragraph (its Observation) was read "
            "as text; the OES-paper PDF uploaded with it was skipped", RP, True)
    rep.add("not replayed: the exterior code of 25 readings in 10 coordinates at distance 5, the 49-record atlas, the "
            "mixed-history rank 234, the 6/5 bits read as a stored charge norm's reciprocal, the six fibre means and the "
            "Golden16 injection, and the sibling's readings", RP, True)
    n35 = notes_1835()
    rep.add("the 18:22 text's and the 18:33 model's other numbers: 6/5 = 8/5 - 2/5, W6 = 17141798400 as the "
            "repository's W_6, and the weighted 49-record atlas's 17 pairs per slot, 51 >= 49 records, 98 cells and 31626 "
            "two-cell locations", T, all(n35.values()), n35)
    rep.add("Drive check 18:35: the hub's OES_Unified_Model_20261029.txt as revised at 18:22 (sources through 17:26), read "
            "as text (its zip, 4262705 bytes, not downloaded); the sibling's MODEL edition of 18:33, read as text; the "
            "OES-paper PDF of 18:33 skipped", RP, True)
    rep.add("not replayed: the fixed seven-reading covariance quotient through the compound inverse, the weighted atlas's "
            "leak 2/245 and its placements (W36 E36 = I7, W36 K49 = 0, the two-error decodings), the 60-dimensional "
            "dilation's literal R and W, the Through736 reports (the 47-copy Gaussian reader, the determinant-155 adapter, "
            "the circle frequency 605.65), and the sibling's readings", RP, True)
    n09 = notes_1909()
    rep.add("the 19:00-19:15 model's exact claims: the dark detector's readings 4 and -1, the transposition traces 7 and "
            "3 of the two 15s, and the roots 30 +- 3 sqrt97", T, all(n09.values()), n09)
    rep.add("Drive check 19:09: the sibling's MODEL editions of 19:00-19:15, the latest (19:15) read as text; the "
            "spine29.ts editions and the OES-paper PDFs of 19:00-19:15 not read", RP, True)
    rep.add("not replayed: the sibling's integer readings of 19:00-19:15 (the twelve-mode bath's transfers, the rank "
            "ladders' minors, the moment band and the power-trace numerators)", RP, True)
    n50 = notes_1950()
    rep.add("the 19:39 text's and the 19:37-20:02 model's other claims: the Fibonacci no-go det(Phi4^5 - I) = 121, the "
            "37-channel reader's r-ranks 37 to 41, the weights 1, -3, 3, -1, A6's element orders and M^T M = 0^5 3^4 8^1",
            T, all(n50.values()), n50)
    rep.add("Drive check 19:50: the hub's OES_Unified_Model_20261029.txt as revised at 19:39 (sources through 19:12), read "
            "as text (its zip, 6685879 bytes, not downloaded); the sibling's MODEL editions of 19:37-20:02, the latest "
            "(20:02) read as text; the spine29.ts editions and the OES-paper PDFs not read", RP, True)
    rep.add("not replayed: the hub's record courts (R51 at raw distance 16, the balanced 56 layout, R50 at 14, the "
            "924-case word census), the source dyad from covariance and commutator, the hidden-wave aliases of an unknown "
            "bath, the local observation table at the double-dark source, the 37-channel reader's convolution inverse, "
            "condition number 3 and 13-setting erasures, the minimum 100-setting decoder, the changed fibre action, and "
            "the sibling's readings", RP, True)
    n33 = notes_2033()
    rep.add("the 20:20 text's, the 20:08-21:02 model's and the monograph's exact claims: A6's classes, the weighted "
            "contexts, the dark code [10, 4, 6] as a Dirac spectral subspace, the norm-31 element, the run-parity "
            "weights, the Golden15 stiffness and the S5 selection rule, with three corrections (the saddle quartic is "
            "-rho^4/2, the monograph's element has norm 61, and the line stabilizer is not the tick's PSL(2,5))",
            T, all(n33.values()), n33)
    rep.add("Drive check 20:33: the hub's OES_Unified_Model_20261029.txt as revised at 20:20 (sources through 19:56), read "
            "as text (its zip, 8710160 bytes, not downloaded); the sibling's MODEL editions of 20:08-21:02, the latest "
            "(21:02) read as text; the owner's monograph OES_Grand_Unified_Mathematical_Monograph_20261030 (20:13), read "
            "as text; the separate model's source continuation (20:40), current-model certificate (20:47) and update "
            "checkpoint (20:50), read as receipts; its 24173180-byte capsule (20:46), the spine29.ts editions and the "
            "OES-paper PDFs not opened", RP, True)
    rep.add("not replayed: the hub's checksum doublets and the [30, 12, 12] code, R53 and R55, the cyclic56 weight repair "
            "and its burst decoders, the polynomial encoder's decodings, the all-time dark families (dimensions 11, 8, 8; "
            "ranks 17, 9, 12, 12), the ten 3+2 dark marks and their pentagon frames, the run-parity decoder, the coherent "
            "phase lift, the noisy estimator's envelopes and its custody (958 groups in 30 receipts); the monograph's "
            "other remediations, its collar regimes and its master script (not run); the separate model's 114 and 237 "
            "independent groups and its two corrections (a mislabelled right inverse and the Fibonacci sum 34); and the "
            "canon's controlled workbooks, which gained additive appendices at 19:24, with two intake workbooks (19:21), "
            "not opened", RP, True)
    n17 = notes_2117()
    rep.add("the 21:05-21:17 model and maps29.ts: the circle as a ring (the CRT idempotents 3105, 2080, 3456 and 2241, "
            "their mirrors and their products on the tick levels), the levels that meet the tick, the unit landings and "
            "depths, the doubling cycle, the golden ticks' mirror, the petal and dark Grams and the seed", gates.ARITHMETIC,
            all(n17.values()), n17)
    rep.add("Drive check 21:18: the sibling's MODEL editions of 21:05-21:17, the latest (21:17) read as text, and its new "
            "maps29.ts (21:12), read as data and not run; the spine29.ts editions and the OES-paper PDFs not read", RP, True)
    n2150 = notes_2150()
    rep.add("the 21:19-21:46 model: the idempotents' images, the golden ticks as 1080 (k mod 4) + 3456 (k mod 5), the "
            "digit cycles, the traceless five, the companion values and the printed roots, with the landing read as "
            "864 x (the first tick level only for units)", gates.ARITHMETIC, all(n2150.values()), n2150)
    rep.add("Drive check 21:50: the sibling's MODEL editions of 21:19-21:46, the latest (21:46) read as text; the canon's "
            "release OES_N30_W3_D3_SELECTED_INTAKE_20261030 (three new N30 tabs in each controlled workbook, 3738 and 3693 "
            "sheets, every prior cell identical, no source check replayed, no gate changed), its release JSON and four-copy "
            "receipt read, the workbooks not opened; the spine29.ts editions and the OES-paper PDFs not read", RP, True)
    n2222 = notes_2222()
    rep.add("the 21:54 text and the 21:57-22:21 model: the landing count (units suffice, 328 non-units also match), the "
            "dark syndrome floor 1/15 with its ten tight supports, the Dirac polynomial T = -P0 - 7P3 + 3P8, the "
            "encoder variants' moments and Vandermonde minima, and the idempotent readings", T, all(n2222.values()), n2222)
    rep.add("Drive check 22:22: the hub's OES_Unified_Model_20261029.txt as revised at 21:54 (sources through 21:22), read "
            "as text (its zip, 10650481 bytes, not downloaded); the sibling's MODEL editions of 21:57-22:21, the latest "
            "(22:21) read as text; the spine29.ts editions and the OES-paper PDFs not read", RP, True)
    rep.add("not replayed: the hub's canonical exterior inverse (gain 1/5 against 149/720), the genuine [32, 12, 14] "
            "code, the bright floor (9 - sqrt37)/20, the source-power gate and the parent bound B >= ||w||/60, the "
            "feasibility routine, the six Golden references and the causal jets; and the sibling's N30 sheet gap (3724 "
            "and 3679 against 3735 and 3690 in the release's own previous entry) and its other readings", RP, True)
    n2253 = notes_2253()
    rep.add("the 22:51 text and the 22:26-22:51 model: the dark erasure court (floors 3/5, 1/3, (17 - sqrt129)/30, 1/15, a "
            "cubic root and 0, attained 10, 15, 30, 10, 60, 25 times), the spectrum of T, the cubic phase module of weights "
            "1 and 3, and the arithmetic", T, all(n2253.values()), n2253)
    rep.add("Drive check 22:53: the hub's OES_Unified_Model_20261029.txt as revised at 22:51 (sources through 22:28; 1198 "
            "groups in 42 receipts), read as text (its zip, 15946002 bytes, not downloaded); the sibling's MODEL editions of "
            "22:26-22:51, the latest (22:51) read as text; the spine29.ts editions and the OES-paper PDFs not read", RP, True)
    rep.add("not replayed: the hub's temporal rank ladder 17 -> 19 -> 20, the two-context branches, the global signed-wedge "
            "completion, the gain bound 10^28, the continuum of dark E8 embeddings, the feedback inverse and its 5320/6240-"
            "site baths, the 277-entry admission court, the Golden-setting trades, the bright erasure rows, the two "
            "replacement codes and the reacting root-port jets", RP, True)
    n2325 = notes_2325()
    rep.add("the 23:07-23:22 model: the dark and Golden simplex Grams and their deletion conditions 5 and 6, the six Golden "
            "vectors' midpoints, differences and triple sums with their frames 12 and 36, and the arithmetic",
            gates.ARITHMETIC, all(n2325.values()), n2325)
    rep.add("Drive check 23:25: the sibling's MODEL editions of 23:07-23:22, the latest (23:22) read as text; the hub's text "
            "unchanged since 22:51; the spine29.ts editions and the OES-paper PDFs not read; not replayed: the jet-rank "
            "increments and the degree-five kernel 23, the generating function's eighth derivative, the 4188 rows, the "
            "120-site bath and the reported 67, 37, 96 and 939 checks", RP, True)
    n2356 = notes_2356()
    rep.add("the 23:38 text and the 23:26-00:00 model: the [15, 5, 6] midpoint code and its ten failing nine-sets, the "
            "Dirac polynomial, the selected matrix over F5 (conjugate to the inverse day), the Klein fours, the printed "
            "moments' Hankel and Jacobi chain, the closure field F_241^2, the cubic over Q(sqrt5), the fixture and the "
            "arithmetic", T, all(n2356.values()), n2356)
    rep.add("Drive check 23:56: the sibling's MODEL editions of 23:26-00:00, the latest (00:00) read as text, with its "
            "spine29.ts (00:01) read as data, not run; the hub's OES_Unified_Model_20261029.txt as revised at 23:38 "
            "(sources through 23:15; 1336 groups in 48 receipts) read as text, its zip (20969993 bytes) not downloaded; "
            "the canon's N31 release read from its receipts; the separate model's capsules recorded from their "
            "certificates; the OES-paper PDFs not read", RP, True)
    rep.add("not replayed: the static Schur completion energies 13/27 and 16/27 (the operator is not given), the six "
            "petals' POVM, the minimum-energy bath and its Green scalar, the encoder value; the hub's marked and quadratic "
            "rosebud bridges (det B = 4/125, Jacobian -256), the [22, 10, 6] exterior code, the 36 norm-four dark copies' "
            "jet ranks, the 24 Cauchy moments, the invisible sector and the energy caps", RP, True)
    n0032 = notes_0032()
    rep.add("the 00:25 text and the 00:04-00:38 model: the native moments through 6 recomputed on the lattice, their "
            "Hankel and Jacobi chain and the Galerkin bound on the static Green scalar, the reflection Casimir 48, the "
            "critical steps against the canon's subgroups, the Weyl vector's Bourbaki order (a correction) and the "
            "arithmetic", T, all(n0032.values()), n0032)
    rep.add("Drive check 00:32: the sibling's MODEL editions of 00:04-00:38, the latest (00:38) read as text, with its "
            "spine29.ts (00:38) read as data, not run; the hub's OES_Unified_Model_20261029.txt as revised at 00:25 "
            "(sources through 23:54; 1435 groups in 53 receipts) read as text, its zip (26691563 bytes) not downloaded; "
            "the canon's N32 release read from its receipt; the separate model's reconciled capsule recorded from its "
            "certificate; the OES-paper PDFs not read", RP, True)
    rep.add("not replayed: the hub's operator tomography on 36 Hermitian directions, the active13 and three-exposure "
            "erasure costs, the 119 five-cell erasure orbits, the attained energy minimum and its 106040-site interval, "
            "the J7 clock quotients and the delayed-Return cutset, the congestion bound itself, and the sibling's "
            "minimum-energy caps, defect formulas and rank ladders (their arithmetic replays)", RP, True)
    n0117 = notes_0117()
    rep.add("the 00:52 text and the 00:46-01:16 model: the native moments m7 and m8 on the lattice with the 5 x 5 Hankel "
            "and the next Jacobi entries, the five-site port's sectors, the identity step's band 0 (a correction), the "
            "pentagon metric, the golden convergents and the arithmetic", T, all(n0117.values()), n0117)
    rep.add("Drive check 01:17: the sibling's MODEL editions of 00:46-01:16, the latest (01:16) read as text, with its "
            "spine29.ts (01:16) read as data, not run; the hub's OES_Unified_Model_20261029.txt as revised at 00:52 (a "
            "new opening chapter over the preserved v23 paper, the 360/093 paper v14 and three source appendices) read "
            "as text; the canon's N33 release read from its receipt; the OES-paper PDFs not read", RP, True)
    rep.add("not replayed: the hub's F20 bridge and positive operator family, the source pullback action, the two causal "
            "input contracts and their five-time codes, the electrical-flow Green certificates and the sibling's "
            "rounded lower Green values, source determinants and noise constant", RP, True)
    n0844 = notes_0844()
    rep.add("the 08:22-08:44 model: the 01:21 certificate's counts and circle orders, the pentagon operator as the "
            "tick's Gauss sum (a symmetric square root of the K5 Laplacian), the overlays, the N33 workbooks and the "
            "sector sheet", T, all(n0844.values()), n0844)
    rep.add("Drive check 08:51: the sibling's MODEL editions of 08:22-08:44, the latest (08:44) read as text, with its "
            "spine29.ts (08:44) read as data, not run; nothing else on Drive is newer than 01:29; the OES-paper PDFs "
            "not read", RP, True)
    rep.add("not replayed: the N33 sector sheet's moments 58702 and 14267058 and its polynomials of degrees 18 and "
            "9 (the sheet's operator is not opened here), and the overlays' 33083 base instances", RP, True)
    n0912 = notes_0912()
    rep.add("the 09:02-09:12 model and the separate model's 09:07 corrections: the sibling's arithmetic and its "
            "replay of the pentagon operator (P^3 = 5P, t (t^2 - 5)^2), the rational Jacobi reference, the miss "
            "set <125> = <5> against the tick, and <1060> = <20> against the golden orbit", T, all(n0912.values()), n0912)
    rep.add("Drive check 09:22: the sibling's MODEL editions of 09:02-09:12, the latest (09:12) read as text, with its "
            "spine29.ts (09:12) read as data, not run; the separate model's continuation (08:53) recorded from its "
            "certificate (08:54) and its checkpoint (08:57); its note-correction capsule (09:07) read in memory as "
            "data, its code not run, with its certificate and checkpoint recovery (09:15); the OES-paper PDFs not "
            "read", RP, True)
    n0951 = notes_0951()
    rep.add("the 09:23 text and the 09:38-09:51 model: the source histories (the Plucker counterfeit and its "
            "syzygies), the six root probes and the three-sector algebra, the F20 bright-dark line, the Golden "
            "projectors and channel, and the hub's local arithmetic", T, all(n0951.values()), n0951)
    rep.add("Drive check 09:51: the hub's OES_Unified_Model_20261029.txt as revised at 09:23 read as text; the "
            "separate model's source-history completion (09:24) recorded from its certificate (09:25) and "
            "checkpoint (09:27); the sibling's MODEL editions of 09:38-09:51, the latest read as text, with its "
            "spine29.ts read as data, not run; the OES-paper PDFs not read", RP, True)
    n1004 = notes_1004()
    rep.add("the hub's N33 reconciliation and the 09:54 connections: the finite and infinite walk counts, the "
            "six-line transition's missing logarithm and its two-step embedding, the MDS context code and the Gauss "
            "operator's AGL(1,5) sign rule", T, all(n1004.values()), n1004)
    rep.add("Drive check 10:26: the hub's OES_All_Dots_N33_Reconciliation_20261030.txt (09:54) read as text, its "
            "handover zip not opened; the separate model's unified connections (09:54) recorded from its "
            "certificate (10:02), with its checkpoint recovery (10:04)", RP, True)
    n1411 = notes_1411()
    rep.add("the canon's N34 release and the 14:06 model: the hub's 49-tuple is admissible, the N34 boundary jets are "
            "the odd jets of the held moments under a frequency-4 forcing, the receipt's counts add up, Q^2 = 52Q + 224I, "
            "and tr A^2 = 13440 = W_3 for a reason", T, all(n1411.values()), n1411)
    rep.add("Drive check 14:11: the canon's N34 release (the four-copy receipt, the claims CSV, the current-release "
            "manifests and the Locked Memory handover note read as data, the workbooks not opened); the sibling's MODEL "
            "edition of 14:06 read as text with its spine29.ts read as data, not run; the OES-paper PDF not read", RP, True)
    for name, why, status in NOT_JOINED:
        rep.add(f"not joined: {name}: {why}", status, True)
    return rep
