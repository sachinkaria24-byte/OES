"""Layer 17. Sound, light, frequency and phase on the K5 edges.

The ten edges of K5 carry one Hodge complex. With the gradient d0 = B^T
(vertices -> edges), the curl Curl = *d1 (edges -> the ten triangles -> edges by
the Hodge star of the 4-simplex) and the canon's orientation (boundary_oriented):

* sound = im d0, the 4 longitudinal edge modes. They are the velocity fields of
  the acoustic system p' = -d0^T u, u' = d0 p, whose frequencies are the vertex
  Laplacian B B^T = 5I - J = (1/2) sum over A4 roots alpha alpha^T. That is the
  long-wave Hessian of the carrier's own root lattice;
* light = ker d0^T, the 6 transverse edge modes. This is the cycle space L6, the
  native port space. Curl is symmetric with Curl^2 = d1^T d1, eigenvalues
  +-sqrt5 (3 each) on light and 0 on sound. In the canon's fundamental-cycle
  basis it is -A, where A = (6I - G) sigma is the Hodge block of layer 1;
* frequency: d0 d0^T + Curl^2 = 5 I_10, so sound and light are isochronous at
  omega = sqrt5. The carrier's vertex frequencies are the complements,
  M M^T + B B^T = 8I;
* phase: the order-5 edge tick fixes both sectors. Sound carries the C5 phases
  +-72 and +-144 degrees and no phase 0. The two curl eigenspaces (helicities)
  are swapped by odd permutations. Under the rotation group A5 they are the two
  icosahedral 3-dim irreps (5-cycle characters phi and 1 - phi), and sound is
  the A5 4. So no S5- or A5-symmetric medium converts sound into light; the C5
  clock allows 4 real phase-matched parameters, and each helicity's phase-0
  mode stays dark to sound.

The native port joins them. A source at frequency 2 drives the light sector
only at frequencies 0 and 4, with doubled phase; the port's kernel is the A5 4.
The adapter carries light to the boundary, where the E8 bath takes it as sound:
its speed^2 on the carrier's plane is 30 = 5 (A4) + 25 (the mixed roots), and
the port frequency lies in the smooth acoustic part of the band.

"Sound" and "light" name the longitudinal and transverse sectors. Making them
physical sound and light needs DYN_BIND and TIME_BIND, so that step is CONDITIONAL.
"""

import itertools

import numpy as np
import sympy as sp
from scipy.optimize import brentq
from sympy.combinatorics import Permutation

from . import carrier, gates, handover, literal
from .record import Report

PHI = (1 + 5 ** 0.5) / 2


def complex_ops():
    """Exact d0 (10x5), d1 (triangles x edges), Hodge star (edges x triangles), Curl = star d1."""
    E = carrier.edges()
    idx = {e: k for k, e in enumerate(E)}
    tris = list(itertools.combinations(range(5), 3))
    tidx = {t: k for k, t in enumerate(tris)}
    d1 = sp.zeros(10, 10)
    for t, (i, j, k) in enumerate(tris):
        for (a, b), s in (((i, j), 1), ((j, k), 1), ((i, k), -1)):
            d1[t, idx[(a, b)]] = s
    star = sp.zeros(10, 10)
    for e, (i, j) in enumerate(E):
        k, l, m = sorted(set(range(5)) - {i, j})
        star[e, tidx[(k, l, m)]] = Permutation([i, j, k, l, m]).signature()
    d0 = carrier.signed_incidence().T
    return d0, d1, star, star * d1


def edge_action(p, signed=True):
    """Vertex permutation p carried to edges, with the orientation sign if signed."""
    E = carrier.edges()
    idx = {e: k for k, e in enumerate(E)}
    U = np.zeros((10, 10))
    for k, (i, j) in enumerate(E):
        a, b = p[i], p[j]
        U[idx[tuple(sorted((a, b)))], k] = (1 if a < b else -1) if signed else 1
    return U


def projectors():
    d0, _, _, curl = complex_ops()
    d0 = np.array(d0, float)
    C = np.array(curl, float)
    Ps = d0 @ np.linalg.pinv(d0)
    Pl = np.eye(10) - Ps
    return Ps, Pl, (Pl + C / 5 ** 0.5) / 2, (Pl - C / 5 ** 0.5) / 2, C


def hom_dim(Pa, Pb, gens):
    """dim {X = Pb X Pa : T_g X = X T_g for g in gens} (maps sector a -> sector b)."""
    ba, bb = _basis(Pa), _basis(Pb)
    rows = []
    for T in gens:
        Ta, Tb = ba.T @ T @ ba, bb.T @ T @ bb
        rows.append(np.kron(np.eye(len(Ta)), Tb) - np.kron(Ta.T, np.eye(len(Tb))))
    L = np.vstack(rows)
    return ba.shape[1] * bb.shape[1] - np.linalg.matrix_rank(L, tol=1e-9)


def _basis(P):
    w, V = np.linalg.eigh((P + P.T) / 2)
    return V[:, w > 0.5]


def a5():
    return [p for p in itertools.permutations(range(5)) if Permutation(list(p)).is_even]


def character(P, perms):
    return np.array([np.trace(edge_action(p) @ P) for p in perms])


def conversion(kappa=0.05, t_end=None):
    """Sound and light coupled by a C5-equivariant X; start in one sound phase class."""
    Ps, Pl, Hp, Hm, _ = projectors()
    T5 = edge_action((1, 2, 3, 4, 0))
    bs, bl = _basis(Ps), _basis(Pl)
    # basis of Hom_C5(sound, light)
    Ta, Tb = bs.T @ T5 @ bs, bl.T @ T5 @ bl
    L = np.kron(np.eye(4), Tb) - np.kron(Ta.T, np.eye(6))
    _, s, Vt = np.linalg.svd(L)
    homs = Vt[-4:]
    rng = np.random.default_rng(7)
    Xc = (rng.standard_normal(4) @ homs).reshape(4, 6).T          # 6 x 4 (light x sound), column-major vec
    X = bl @ Xc @ bs.T
    # initial state: a sound mode in the rho_1 (72 degree) class
    ev, U = np.linalg.eig(bs.T @ T5 @ bs)
    k = int(np.argmin(np.abs(ev - np.exp(2j * np.pi / 5))))
    u = np.real(bs @ U[:, k])
    u /= np.linalg.norm(u)
    X /= np.linalg.norm(X @ u)                       # unit coupling on this phase class
    K = 5 * np.eye(10) + kappa * (X + X.T)
    w, V = np.linalg.eigh(K)
    t_end = t_end or 2 * np.pi / (np.sqrt(5 + kappa) - np.sqrt(5 - kappa))
    ts = np.linspace(0, t_end, 2001)
    c = V.T @ u
    xs = np.array([V @ (np.cos(np.sqrt(w) * t) * c) for t in ts])
    vs = np.array([V @ (-np.sqrt(w) * np.sin(np.sqrt(w) * t) * c) for t in ts])

    def energy(P):
        return 0.5 * np.einsum("ti,ij,tj->t", vs, P, vs) + 2.5 * np.einsum("ti,ij,tj->t", xs, P, xs)

    tot = 0.5 * np.einsum("ti,ti->t", vs, vs) + 0.5 * np.einsum("ti,ij,tj->t", xs, K, xs)
    phase0 = bl @ _basis_phase0(bl, T5)
    P0 = phase0 @ phase0.T
    # the helicity that carries rho_1
    hel = Hp if abs(np.trace(T5 @ Hp) - PHI) < 1e-9 else Hm
    other = Hm if hel is Hp else Hp
    return {"max_light_fraction": float(np.max(energy(hel) / energy(np.eye(10)))),
            "max_other_helicity": float(np.max(energy(other))),
            "max_phase0": float(np.max(energy(P0))),
            "energy_drift": float(np.max(np.abs(tot - tot[0])))}


def _basis_phase0(bl, T5):
    Tl = bl.T @ T5 @ bl
    w, V = np.linalg.eig(Tl)
    v = np.real(V[:, np.abs(w - 1) < 1e-9])
    q, _ = np.linalg.qr(v)
    return q


def bath_sound(eps=16.0):
    """Wavenumber, phase and group velocity of bath sound at eps along two directions."""
    R = handover.e8_roots()

    def along(u):
        f = lambda s: 240 - np.cos(R @ (s * u)).sum() - eps
        s0 = brentq(f, 1e-6, 2.0)
        h = 1e-6
        de = (f(s0 + h) - f(s0 - h)) / (2 * h)
        w = np.sqrt(eps)
        return {"k": float(s0), "v_phase/sqrt30": float(w / s0 / 30 ** 0.5),
                "v_group/sqrt30": float(de / (2 * w) / 30 ** 0.5)}

    root = R[0] / np.linalg.norm(R[0])
    vert = np.array([1, 1, 1, 1, 0, 0, 0, 0]) / 2
    return {"root direction": along(root), "band-vertex direction": along(vert)}


def run():
    rep = Report("17-waves")
    T, AR, CD = gates.THEOREM, gates.ARITHMETIC, gates.CONDITIONAL
    d0, d1, star, curl = complex_ops()
    B = carrier.signed_incidence()
    lit = literal.load()
    rep.add("K5 edge complex: the canon's oriented boundary is the signed incidence; "
            "d1 d0 = 0 and rank d0 + rank d1 = 4 + 6 = 10 (exact, H^1 = 0)", T,
            lit["boundary_oriented"] == B and d1 * d0 == sp.zeros(10, 5)
            and d0.rank() == 4 and d1.rank() == 6)
    rep.add("Hodge Laplacian d0 d0^T + Curl^2 = 5 I_10: sound and light are isochronous "
            "at omega = sqrt5", T, d0 * d0.T + curl * curl == 5 * sp.eye(10)
            and curl * curl == d1.T * d1)
    Ps, Pl, Hp, Hm, C = projectors()
    F = np.array(lit["Fedge_native_inverse"], float)
    Bn = np.array(B, float)
    rep.add("Hodge split: sound = im d0 (4 longitudinal modes), light = ker d0^T (6 transverse "
            "modes) = the cycle space L6 = the native port space", T,
            np.isclose(np.trace(Ps), 4) and np.isclose(np.trace(Pl), 6)
            and np.allclose(Bn @ F, 0) and np.linalg.matrix_rank(F) == 6)
    E5 = sp.eye(5)
    A4 = [E5[:, i] - E5[:, j] for i in range(5) for j in range(5) if i != j]
    half = sum((a * a.T for a in A4), sp.zeros(5, 5)) / 2
    rep.add("sound: the acoustic system p' = -d0^T u, u' = d0 p has omega^2 in {0, 5^4}; its "
            "operator B B^T = 5I - J = (1/2) sum_A4 alpha alpha^T, the long-wave Hessian of the "
            "carrier's root lattice", T,
            B * B.T == 5 * sp.eye(5) - sp.ones(5, 5) == half)
    G, S, A = carrier.hodge_block()
    Cf, _ = carrier.fundamental_cycles()
    X = (Cf * Cf.T).inv() * Cf * curl * Cf.T
    ev = curl.eigenvals()
    rep.add("light: Curl = *d1 is symmetric with spectrum {+sqrt5^3, -sqrt5^3, 0^4}; on the "
            "cycle space, in the canon's fundamental-cycle basis, it is -A, the Hodge block "
            "A = (6I - G) sigma of layer 1", T,
            curl == curl.T and ev == {sp.sqrt(5): 3, -sp.sqrt(5): 3, 0: 4}
            and curl * Cf.T == Cf.T * X and X == -A)
    perms = a5()
    chi_p, chi_m, chi_s = (character(P, perms) for P in (Hp, Hm, Ps))
    norm = lambda a, b: float(a @ b / 60)
    tau = edge_action((1, 0, 2, 3, 4))
    T5 = edge_action((1, 2, 3, 4, 0))
    rep.add("helicity: odd permutations swap the two curl eigenspaces, even ones keep them; "
            "under A5 they are the two icosahedral 3-dim irreps and sound is the A5 4", T,
            np.allclose(tau @ Hp @ tau.T, Hm) and np.allclose(T5 @ Hp @ T5.T, Hp)
            and np.isclose(norm(chi_p, chi_p), 1) and np.isclose(norm(chi_m, chi_m), 1)
            and np.isclose(norm(chi_p, chi_m), 0) and np.isclose(norm(chi_s, chi_s), 1)
            and np.isclose(chi_p[0], 3) and np.isclose(chi_s[0], 4),
            {"<chi+,chi+>": norm(chi_p, chi_p), "<chi+,chi->": norm(chi_p, chi_m),
             "<chi_sound,chi_sound>": norm(chi_s, chi_s)})
    tr = {"sound": float(np.trace(T5 @ Ps)), "helicity+": float(np.trace(T5 @ Hp)),
          "helicity-": float(np.trace(T5 @ Hm))}
    rep.add("phase: the edge tick (order 5) fixes both sectors; Tr on sound = -1 (phases +-72, "
            "+-144 degrees, none at 0); Tr on the helicities = phi and 1 - phi (each = one "
            "phase-0 mode + one of the 72 / 144 degree pairs)", T,
            np.allclose(T5 @ Ps, Ps @ T5) and np.isclose(tr["sound"], -1)
            and sorted([round(tr["helicity+"], 9), round(tr["helicity-"], 9)])
            == sorted([round(PHI, 9), round(1 - PHI, 9)]), tr)
    s5_gens = [T5, tau]
    a5_gens = [T5, edge_action((1, 2, 0, 3, 4))]
    dims = {"S5": int(hom_dim(Ps, Pl, s5_gens)), "A5": int(hom_dim(Ps, Pl, a5_gens)),
            "C5": int(hom_dim(Ps, Pl, [T5]))}
    rep.add("conversion selection rules: no S5- or A5-equivariant map takes sound to light; "
            "the C5 clock allows exactly 4 real phase-matched parameters, and the two phase-0 "
            "light modes stay dark to sound", T, dims == {"S5": 0, "A5": 0, "C5": 4}, dims)
    conv = conversion()
    rep.add("resonant conversion: with any C5-equivariant coupling, a sound mode of the 72-degree "
            "class converts completely into the helicity that carries that class; the other "
            "helicity and the phase-0 modes stay empty", CD,
            conv["max_light_fraction"] > 0.999 and conv["max_other_helicity"] < 1e-12
            and conv["max_phase0"] < 1e-12 and conv["energy_drift"] < 1e-10, conv,
            note="isochronous sectors make the transfer complete; the coupling itself is not a "
                 "canon operand")
    M = carrier.signless_incidence()
    rep.add("carrier complement: M M^T + B B^T = 8I, so on every vertex mode omega_carrier^2 + "
            "omega_sound^2 = 8 (uniform 8 + 0, contrast 3 + 5)", T, M * M.T + B * B.T == 8 * sp.eye(5))
    K = np.array(M.T * M, float)
    rep.add("matter and sound/light carry two C5 actions on the same edges: the carrier's edge "
            "operator M^T M commutes with the unsigned tick, not with the signed one", T,
            np.allclose(K @ np.abs(T5), np.abs(T5) @ K) and not np.allclose(K @ T5, T5 @ K))
    pairs = [tuple(p) for p in lit["source_wedge_order"]]
    N = np.array(lit["N_source"], float)
    Phi = F @ np.array(lit["WAS_native"], float)
    ok = True
    for p in ((1, 2, 3, 4, 0), (1, 0, 2, 3, 4)):
        Sg = np.linalg.pinv(N) @ edge_action(p, signed=False) @ N
        L2 = np.array(literal.lambda2(sp.Matrix(Sg), pairs), float)
        ok &= np.allclose(Phi @ L2, edge_action(p) @ Phi)
    _, sv, Vt = np.linalg.svd(Phi)
    kern = Vt[6:].T
    chi_k = []
    for p in perms:
        Sg = np.linalg.pinv(N) @ edge_action(p, signed=False) @ N
        L2 = np.array(literal.lambda2(sp.Matrix(Sg), pairs), float)
        chi_k.append(np.trace(np.linalg.pinv(kern) @ L2 @ kern))
    chi_k = np.array(chi_k)
    rep.add("the literal port (source wedges -> light) is S5-equivariant, drives each helicity "
            "with rank 3, and its 4-dim kernel is the A5 4 (the sound type)", T,
            ok and np.linalg.matrix_rank(Hp @ Phi, 1e-9) == 3
            and np.linalg.matrix_rank(Hm @ Phi, 1e-9) == 3 and np.allclose(chi_k, chi_s))
    src = literal.LiteralSource()
    rng = np.random.default_rng(11)
    a0, b0, ph = rng.standard_normal(5), rng.standard_normal(5), 0.37
    ts = rng.uniform(0, 7, 9)
    g = lambda t: src.g(np.r_[a0 * np.cos(2 * t + ph), b0 * np.sin(2 * t + ph)])
    gab = src.g(np.r_[a0, b0])
    circ = all(np.allclose(g(t), 0.5 * np.sin(4 * t + 2 * ph) * gab) for t in ts)
    a1, b1 = rng.standard_normal(5), rng.standard_normal(5)
    gen = lambda t: src.g(np.r_[a0 * np.cos(2 * t) + a1 * np.sin(2 * t),
                                b0 * np.cos(2 * t) + b1 * np.sin(2 * t)])
    basis = lambda t: np.array([1, np.cos(4 * t), np.sin(4 * t)])
    t5 = np.linspace(0.1, 1.3, 3)
    coef = np.linalg.solve(np.array([basis(t) for t in t5]), np.array([gen(t) for t in t5]))
    fits = all(np.allclose(basis(t) @ coef, gen(t)) for t in ts)
    rep.add("frequency and phase at the port: a source at frequency 2 drives light only at "
            "frequencies 0 and 4; a circular source gives pure frequency 4 with phase 2 phi", T,
            circ and fits, note="the port is quadratic: a ^ b doubles frequency and phase")
    Rr = handover.e8_roots()
    P = np.zeros((8, 8))
    P[:5, :5] = np.eye(5) - np.ones((5, 5)) / 5
    on_plane = lambda rs: P @ (0.5 * sum(np.outer(r, r) for r in rs)) @ P
    A4r = np.array([r for r in Rr if np.allclose(r[5:], 0) and np.isclose(r[:5].sum(), 0)])
    A4p = np.array([r for r in Rr if np.allclose(A4r @ r, 0)])
    mixed = np.array([r for r in Rr if not np.allclose(A4r @ r, 0)
                      and not (np.allclose(r[5:], 0) and np.isclose(r[:5].sum(), 0))])
    rep.add("sound speed^2 through the layers: K5 / A4 gives 5; the E8 bath on the carrier's "
            "4-plane gives 30 = 5 (A4) + 0 (A4') + 25 (the 200 mixed roots), isotropically", T,
            len(mixed) == 200 and np.allclose(on_plane(Rr), 30 * P)
            and np.allclose(on_plane(A4r), 5 * P) and np.allclose(on_plane(A4p), 0)
            and np.allclose(on_plane(mixed), 25 * P))
    fam = handover.critical_census()
    eps_crit = sorted(240 - f["lambda"] for f in fam.values())
    rep.add("acoustic window: the band has no critical value in (0, 224), so the port frequency "
            "4 (eps = 16) radiates into the smooth acoustic part of the bath", T,
            np.isclose(eps_crit[0], 0) and np.isclose(eps_crit[1], 224))
    bs = bath_sound()
    rep.add("bath sound at the port frequency: wavenumber, phase and group velocity (lattice "
            "units, as ratios to the long-wave speed sqrt30)", AR, True,
            {k: {kk: round(vv, 6) for kk, vv in v.items()} for k, v in bs.items()},
            note="the two directions differ only at order k^8 (E8 roots are a 7-design)")
    ladder = [("dark (ker D)", 0.0), ("carrier contrast", 3 ** 0.5), ("source", 2.0),
              ("K5 sound = light", 5 ** 0.5), ("carrier uniform", 8 ** 0.5), ("port", 4.0),
              ("bath saddle (eps 224)", 224 ** 0.5), ("bath band top", 16.0)]
    rep.add("frequency ladder in native units: 0 < sqrt3 < 2 < sqrt5 < 2 sqrt2 < 4 < sqrt224 < 16",
            AR, all(a[1] < b[1] for a, b in zip(ladder, ladder[1:])),
            {name: round(w, 6) for name, w in ladder})
    rep.add("physical sound and light", CD, True,
            note="naming the longitudinal and transverse sectors as physical sound and light needs "
                 "DYN_BIND, and absolute frequencies need TIME_BIND; the invariant content is "
                 "the ratios: light/sound 1, carrier^2 + sound^2 = 8, port/source 2, bath/K5 "
                 "speed^2 6")
    return rep
