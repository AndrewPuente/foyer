from foyer.atomtyper import (
    Element, NeighborCount, NeighborsAtLeast, NeighborsExactly, Whitelist,
    Blacklist, check_atom, InWhitelist)
from foyer.chemical_groups import benzene, dioxolane13


# -------------- #
# House of rules #
# -------------- #

@Element('O')
@NeighborCount(2)
@NeighborsExactly('H', 2)
@Whitelist(111)
def opls_111(atom):
    """O TIP3P Water """
    return True


@Element('H')
@NeighborCount(1)
@NeighborsExactly(111, 1)
@Whitelist(112)
def opls_112(atom):
    """H TIP3P Water """
    return True


@Element('C')
@NeighborCount(4)
@NeighborsExactly('C', 1)
@NeighborsExactly('H', 3)
#@NeighborsExactly('Si', 1)
@Whitelist(135)
def opls_135(atom):
    """alkane CH3 """
    return True


@Element('C')
@NeighborCount(4)
@NeighborsExactly('C', 2)
@NeighborsExactly('H', 2)
@Whitelist(136)
def opls_136(atom):
    """alkane CH2 """
    return True


@Element('C')
@NeighborCount(4)
@NeighborsExactly('C', 3)
@NeighborsExactly('H', 1)
@Whitelist(137)
def opls_137(atom):
    """alkane CH """
    return True


@Element('C')
@NeighborCount(4)
@NeighborsExactly('H', 4)
@Whitelist(138)
def opls_138(atom):
    """alkane CH4 """
    return True


@Element('C')
@NeighborCount(4)
@NeighborsExactly('C', 4)
@Whitelist(139)
def opls_139(atom):
    """alkane C """
    return True


@Element('H')
@NeighborCount(1)
@NeighborsExactly('C', 1)
@Whitelist(140)
def opls_140(atom):
    """alkane H """
    return True


@Element('C')
@NeighborCount(3)
@NeighborsExactly('C', 3)
@Whitelist(141)
def opls_141(atom):
    """alkene C (R2-C=) """
    return True


@Element('C')
@NeighborCount(3)
@NeighborsExactly('C', 2)
@NeighborsExactly('H', 1)
@Whitelist(142)
def opls_142(atom):
    """alkene C (RH-C=) """
    return True


@Element('C')
@NeighborCount(3)
@NeighborsExactly('C', 1)
@NeighborsExactly('H', 2)
@Whitelist(143)
def opls_143(atom):
    """alkene C (H2-C=) """
    return True


@Element('H')
@NeighborCount(1)
@NeighborsExactly('C', 1)
@Whitelist(144)
@Blacklist(140)
def opls_144(atom):
    """alkene H (H-C=) """
    # Make sure that the carbon is an alkene carbon.
    rule_ids = [141, 142, 143]
    return check_atom(atom.bond_partners[0], rule_ids)


@Element('C')
@NeighborCount(3)
@NeighborsAtLeast('C', 2)
@Whitelist(145)
@Blacklist([141, 142])
def opls_145(atom):
    """Benzene C - 12 site JACS,112,4768-90. Use #145B for biphenyl """
    return benzene(atom)


@Element('C')
@NeighborCount(3)
@NeighborsExactly('C', 3)
@NeighborsExactly('145', 3)
@Whitelist('145B')
@Blacklist([145])
def opls_145B(atom):
    """Biphenyl C1 """
    return True


@Element('H')
@NeighborCount(1)
@NeighborsExactly('C', 1)
@NeighborsExactly(145, 1)
@Whitelist(146)
@Blacklist([140, 144])
def opls_146(atom):
    """Benzene H - 12 site. """
    return True


@Element('C')
@NeighborCount(4)
@NeighborsExactly('C', 1)
@NeighborsExactly(145, 1)
@NeighborsExactly('H', 3)
@Whitelist(148)
@Blacklist(135)
def opls_148(atom):
    """C: CH3, toluene """
    return True


@Element('C')
@NeighborCount(4)
@NeighborsExactly('C', 2)
@NeighborsExactly(145, 1)
@NeighborsExactly('H', 2)
@Whitelist(149)
@Blacklist(136)
def opls_149(atom):
    """C: CH2, ethyl benzene """
    return True


@Element('O')
@NeighborCount(2)
@NeighborsExactly('H', 1)
@Whitelist(154)
def opls_154(atom):
    """all-atom O: mono alcohols """
    return True


@Element('H')
@NeighborCount(1)
@NeighborsExactly('O', 1)
@NeighborsExactly(154, 1)
@Whitelist(155)
def opls_155(atom):
    """all-atom H(O): mono alcohols, OP(=O)2 """
    return True


@Element('O')
@NeighborCount(2)
@NeighborsExactly('C', 2)
@NeighborsExactly(145, 1)
@Whitelist(179)
@Blacklist(180)
def opls_179(atom):
    """O: anisole """
    return True


@Element('O')
@NeighborCount(2)
@NeighborsExactly('C', 2)
@Whitelist(180)
def opls_180(atom):
    """O: dialkyl ether """
    return True


@Element('C')
@NeighborCount(4)
@NeighborsExactly('H', 3)
@NeighborsExactly('O', 1)
@Whitelist(181)
def opls_181(atom):
    """C(H3OR): methyl ether """
    return True


@Element('C')
@NeighborCount(4)
@NeighborsExactly('H', 2)
@NeighborsExactly(180, 1)
@NeighborsExactly('C', 1)
@Whitelist(182)
def opls_182(atom):
    """C(H2OR): ethyl ether """
    return True


@Element('C')
@NeighborCount(3)
@NeighborsExactly('H', 1)
@NeighborsExactly(180, 1)
@NeighborsExactly('C', 1)
@Whitelist(183)
def opls_183(atom):
    """C(HOR): i-PR ether, allose"""
    return True


@Element('C')
@NeighborCount(2)
@NeighborsExactly('O', 1)
@NeighborsExactly('C', 1)
@Whitelist(184)
def opls_184(atom):
    """C(OR): t-Bu ether """
    return True


@Element('H')
@NeighborCount(1)
@NeighborsExactly('C', 1)
@Whitelist(185)
@Blacklist([140, 144])
def opls_185(atom):
    """H(COR): alpha H ether """
    rule_ids = [181, 182, 183]
    return check_atom(atom.bond_partners[0], rule_ids)


@Element('C')
@NeighborCount(3)
@NeighborsExactly('C', 2)
@NeighborsExactly(145, 2)
@NeighborsExactly('O', 1)
@Whitelist(199)
@Blacklist(145)
def opls_199(atom):
    """C(O,Me): anisole """
    return True


@Element('C')
@NeighborCount(4)
@NeighborsExactly('O', 1)
@NeighborsExactly(154, 1)
@NeighborsExactly('C', 1)
@NeighborsExactly(145, 1)
@NeighborsExactly('H', 2)
@Whitelist(218)
@Blacklist(182)
def opls_218(atom):
    """C in CH2OH - benzyl alcohols """
    return True


@Element('C')
@NeighborCount(3)
@NeighborsExactly('C', 3)
@NeighborsExactly(218, 1)
@NeighborsExactly(145, 2)
@Whitelist(221)
@Blacklist([145, '145B'])
def opls_221(atom):
    """C(CH2OH)   - benzyl alcohols """
    return True


@Element('C')
@NeighborCount(3)
@NeighborsExactly('C', 1)
@NeighborsExactly(145, 1)
@NeighborsExactly('H', 1)
@NeighborsExactly('O', 1)
@NeighborsExactly(278, 1)
@Whitelist(232)
@Blacklist(277)
def opls_232(atom):
    """C: C=0 in benzaldehyde, acetophenone (CH) """
    return True


@Element('C')
@NeighborCount(3)
@NeighborsExactly('C', 2)
@NeighborsExactly(145, 1)
@NeighborsExactly('O', 1)
@NeighborsExactly(278, 1)
@Whitelist(233)
@Blacklist(145)
def opls_233(atom):
    """C: C=0 in acetophenone (CMe) """
    return True


@Element('C')
@InWhitelist(145)
@NeighborCount(3)
@NeighborsExactly('C', 2)
@NeighborsExactly('CL', 1)
@Whitelist(263)
@Blacklist(145)
def opls_263(atom):
    """C(Cl) chlorobenzene """
    return True


@Element('CL')
@NeighborCount(1)
@NeighborsExactly('C', 1)
@Whitelist(264)
def opls_264(atom):
    """Cl chlorobenzene """
    return benzene(atom.bond_partners[0])


@Element('C')
@NeighborCount(3)
@NeighborsExactly('O', 1)
@NeighborsExactly('H', 1)
@Whitelist(277)
def opls_277(atom):
    """AA C: aldehyde """
    return True


@Element('O')
@NeighborCount(1)
@NeighborsExactly('C', 1)
@Whitelist(278)
def opls_278(atom):
    """AA O: aldehyde """
    return True


@Element('H')
@NeighborCount(1)
@NeighborsExactly('C', 1)
@Whitelist(279)
@Blacklist([140, 185])
def opls_279(atom):
    """AA H-alpha in aldehyde & formamide """
    return check_atom(atom.bond_partners[0], [232, 277])


@Element('O')
@NeighborCount(1)
@NeighborsExactly('C', 1)
@NeighborsExactly(233, 1)
@Whitelist(281)
@Blacklist(278)
def opls_281(atom):
    """AA O: ketone """
    return True


@Element('N')
@NeighborCount(4)
@Whitelist(288)
def opls_288(atom):
    """N (R4N+)  JPC,90,2174 (1986) """
    return True


@Element('C')
@NeighborCount(4)
@NeighborsExactly('N', 1)
@NeighborsExactly('H', 3)
@Whitelist(291)
def opls_291(atom):
    """C in CH3NH3+ """
    return True


@Element('C')
@NeighborCount(4)
@NeighborsExactly('N', 1)
@NeighborsExactly('C', 1)
@NeighborsExactly('H', 2)
@Whitelist(292)
def opls_292(atom):
    """C in RCH2NH3+ """
    return True


@Element('P')
@NeighborCount(4)
@NeighborsExactly('O', 4)
@Whitelist(440)
def opls_440(atom):
    """P in Me2PO4-, Me2PO4H """
    carbons_two_bonds_away = 0
    for neighbor in atom.bond_partners:
        for neighbors_neighbor in neighbor.bond_partners:
            if neighbors_neighbor.element_name == 'C':
                carbons_two_bonds_away += 1

    if carbons_two_bonds_away >= 2:
        return True


@Element('O')
@NeighborCount(1)
@NeighborsExactly(440, 1)
@Whitelist(441)
def opls_441(atom):
    """O= in Me2PO4-, Me2PO4H """
    return True


@Element('O')
@NeighborCount(2)
@NeighborsExactly(440, 1)
@NeighborsExactly('C', 1)
@Whitelist(442)
def opls_442(atom):
    """OMe in Me2PO4-, Me2PO4H   dimethylphosphate """
    return True


@Element('C')
@NeighborCount(4)
@NeighborsExactly('O', 1)
@NeighborsExactly(442, 1)
@NeighborsAtLeast('H', 2)
@Whitelist(443)
@Blacklist(182)
def opls_443(atom):
    """C in Me2PO4-, Me2PO4H   dimethylphosphate """
    return True


@Element('H')
@NeighborCount(1)
@NeighborsExactly(443, 1)
@Whitelist(444)
@Blacklist([140, 144, 185])
def opls_444(atom):
    """H in Me2PO4-, Me2PO4H   6-31+G* CHELPG """
    return True


@Element('P')
@NeighborCount(4)
@NeighborsExactly('O', 4)
@Whitelist(445)
def opls_445(atom):
    """P in MeOPO3-, MeOPO3H2"""
    carbons_two_bonds_away = 0
    for neighbor in atom.bond_partners:
        for neighbors_neighbor in neighbor.bond_partners:
            if neighbors_neighbor.element_name == 'C':
                carbons_two_bonds_away += 1

    if carbons_two_bonds_away == 1:
        return True


@Element('O')
@NeighborCount(1)
@NeighborsExactly(445, 1)
@Whitelist(446)
def opls_446(atom):
    """O= in MeOPO3-, MeOPO3H """
    return True


@Element('O')
@NeighborCount(2)
@NeighborsExactly(445, 1)
@NeighborsExactly('C', 1)
@Whitelist(447)
def opls_447(atom):
    """OMe in MeOPO3-, MeOPO3H   dimethylphosphate """
    return True


@Element('C')
@NeighborCount(4)
@NeighborsExactly('O', 1)
@NeighborsExactly(447, 1)
@NeighborsAtLeast('H', 2)
@Whitelist(448)
@Blacklist(182)
def opls_448(atom):
    """C in MeOPO3-, MeOPO3H """
    return True


@Element('H')
@NeighborCount(1)
@NeighborsExactly(448, 1)
@Whitelist(449)
@Blacklist([140, 144, 185])
def opls_449(atom):
    """H in MeOPO3-, MeOPO3H """
    return True


@Element('C')
@NeighborCount(3)
@NeighborsExactly('O', 2)
@NeighborsExactly('C', 1)
@Whitelist(465)
def opls_465(atom):
    """AA C: esters - for R on C=O use #280-#282 """
    return True


@Element('O')
@NeighborCount(1)
@NeighborsExactly('C', 1)
@NeighborsExactly(465, 1)
@Whitelist(466)
@Blacklist(278)
def opls_466(atom):
    """AA =O: esters """
    return True


@Element('O')
@NeighborCount(2)
@NeighborsExactly('C', 2)
@NeighborsAtLeast(465, 1)
@Whitelist(467)
@Blacklist([179, 180])
def opls_467(atom):
    """AA -OR: ester """
    return True


@Element('C')
@NeighborCount(4)
@NeighborsExactly('H', 3)
@NeighborsExactly('O', 1)
@NeighborsAtLeast(467, 1)
@Whitelist(468)
def opls_468(atom):
    """methoxy C in esters - see also #490-#492 """
    return True


@Element('H')
@NeighborCount(1)
@NeighborsExactly('C', 1)
@NeighborsExactly(490, 1)
@Whitelist(469)
@Blacklist([140, 185])
def opls_469(atom):
    """methoxy Hs in esters """
    return True


@Element('C')
@NeighborCount(4)
@NeighborsExactly('C', 1)
@NeighborsExactly('O', 1)
@NeighborsExactly(467, 1)
@NeighborsExactly('H', 2)
@Whitelist(490)
@Blacklist(182)
def opls_490(atom):
    """C(H2OS) ethyl ester """
    return True


@Element('C')
@NeighborCount(4)
@NeighborsExactly('C', 3)
@NeighborsExactly(145, 1)
@NeighborsExactly('H', 1)
@Whitelist(515)
@Blacklist(137)
def opls_515(atom):
    """all-atom C: CH, isopropyl benzene """
    return True


@Element('C')
@InWhitelist('145')
@NeighborCount(3)
@NeighborsExactly('C', 3)
@NeighborsExactly('725', 1)
@Whitelist(724)
@Blacklist([145, 221])
def opls_724(atom):
    """C(CF3) trifluoromethylbenzene """
    return True


@Element('C')
@NeighborCount(4)
@NeighborsExactly('C', 1)
@NeighborsExactly('145', 1)
@NeighborsExactly('F', 3)
@Whitelist(725)
def opls_725(atom):
    """CF3 trifluoromethylbenzene """
    return True


@Element('F')
@NeighborCount(1)
@NeighborsExactly('C', 1)
@NeighborsExactly('725', 1)
@Whitelist(726)
def opls_726(atom):
    """F trifluoromethylbenzene """
    return True


@Element('N')
@NeighborCount(3)
@NeighborsExactly('O', 2)
@NeighborsExactly('C', 1)
@Whitelist(760)
def opls_760(atom):
    """N in nitro R-NO2 """
    return True


@Element('O')
@NeighborCount(1)
@NeighborsExactly('N', 1)
@Whitelist(761)
def opls_761(atom):
    """O in nitro R-NO2 """
    return True


@Element('C')
@InWhitelist('145')
@NeighborCount(3)
@NeighborsExactly('C', 2)
@NeighborsExactly('N', 1)
@NeighborsExactly('760', 1)
@Whitelist(768)
@Blacklist(145)
def opls_768(atom):
    """C(NO2) nitrobenzene """
    return True


@Element('O')
@NeighborCount(1)
@NeighborsExactly('C', 1)
@Whitelist(771)
@Blacklist(278)
def opls_771(atom):
    """propylene carbonate O """
    if dioxolane13(atom.bond_partners[0]):
        for neighbors_neighbor in atom.bond_partners[0].bond_partners:
            if neighbors_neighbor.name != 'O':
                return False
        else:
            return True
    return False


@Element('C')
@NeighborCount(3)
@NeighborsExactly('O', 3)
@Whitelist(772)
def opls_772(atom):
    """propylene carbonate C=O """
    return dioxolane13(atom)


@Element('O')
@NeighborCount(2)
@NeighborsExactly('C', 2)
@Whitelist(773)
@Blacklist([467, 180])
def opls_773(atom):
    """propylene carbonate OS """
    return dioxolane13(atom)


@Element('C')
@NeighborCount(4)
@NeighborsExactly('C', 1)
@NeighborsExactly('O', 1)
@NeighborsExactly('H', 2)
@Whitelist(774)
@Blacklist([182, 218, 490])
def opls_774(atom):
    """propylene carbonate C in CH2 """
    return dioxolane13(atom)


@Element('H')
@NeighborCount(1)
@NeighborsExactly('C', 1)
@NeighborsExactly('774', 1)
@Whitelist(777)
@Blacklist([140, 185])
def opls_777(atom):
    """propylene carbonate H in CH2 """
    return True


@Element('C')
@InWhitelist(145)
@NeighborCount(3)
@NeighborsExactly('C', 2)
@NeighborsExactly('N', 1)
@Whitelist(916)
@Blacklist(145)
def opls_916(atom):
    """C(NH2) aniline """
    return True


@Element('O')
@NeighborCount(2)
@NeighborsExactly('Si', 2)
@Whitelist(1001)
def opls_1001(atom):
    """Bulk silica oxygen """
    return True


@Element('Si')
@NeighborCount(4)
@NeighborsExactly('O', 4)
@Whitelist(1002)
def opls_1002(atom):
    """Bulk silica silicon """
    return True


@Element('Si')
@NeighborCount(3)
@NeighborsExactly('O', 3)
@Whitelist(1003)
def opls_1003(atom):
    """Bulk silica silicon """
    return True


@Element('Si')
@NeighborCount(4)
@NeighborsExactly('C', 1)
@NeighborsExactly('O', 3)
@Whitelist(1004)
def opls_1004(atom):
    """Silane silicon """
    return True


@Element('C')
@NeighborCount(4)
@NeighborsExactly('C', 1)
@NeighborsExactly('Si', 1)
@NeighborsExactly('H', 2)
@Whitelist(1005)
def opls_1005(atom):
    """Alkane carbon bound to silane """
    return True


@Element('O')
@NeighborCount(2)
@NeighborsExactly('Si', 2)
@Whitelist(1006)
@Blacklist([1001,1011])
def opls_1006(atom):
    """Silica surface oxygen bound to silane """
    for neighbor in atom.bond_partners:
        for neighbors_neighbor in neighbor.bond_partners:
            if neighbors_neighbor.element_name != 'O':
                return True


@Element('O')
@NeighborCount(2)
@NeighborsExactly('Si', 1)
@NeighborsExactly('H', 1)
@Whitelist(1007)
@Blacklist(154)
def opls_1007(atom):
    """Silica surface hydroxyl oxygen """
    for neighbor in atom.bond_partners:
        if check_atom(neighbor, [1002,1003,1009,1010,1012]):
            return True


@Element('H')
@NeighborCount(1)
@NeighborsExactly(1007, 1)
@Whitelist(1008)
@Blacklist(155)
def opls_1008(atom):
    """Silica surface hydroxyl hydrogen """
    return True


@Element('Si')
@NeighborCount(5)
@NeighborsExactly('O', 5)
@Whitelist(1009)
def opls_1009(atom):
    """Bulk silica silicon, overcoordinated """
    return True

@Element('Si')
@NeighborCount(2)
@NeighborsExactly('O', 2)
@Whitelist(1010)
def opls_1010(atom):
    """Bulk silica silicon, undercoordinated """
    return True

@Element('O')
@NeighborCount(1)
@NeighborsExactly('Si', 1)
@Whitelist(1011)
def opls_1011(atom):
    """Bulk silica silicon, undercoordinated """
    return True

@Element('Si')
@NeighborCount(1)
@NeighborsExactly('O', 1)
@Whitelist(1012)
def opls_1012(atom):
    """Bulk silica silicon, undercoordinated """
    return True

# @Element('O')
# @NeighborCount(2)
# @NeighborsExactly('Si', 1)
# @NeighborsExactly('H', 1)
# @Whitelist(1011)
# @Blacklist(154)
# def opls_1011(atom):
#     rule_ids = [1002]
#     check = check_atom(atom.bond_partners[0], rule_ids)
#     if not check:
#         check = check_atom(atom.bond_partners[1], rule_ids)
#     return check


# @Element('O')
# @NeighborCount(2)
# @NeighborsExactly('Si', 2)
# @Whitelist(1009)
# @Blacklist(1001)
# def opls_1009(atom):
#     rule_ids = [1004]
#     check = check_atom(atom.bond_partners[0], rule_ids)
#     if not check:
#         check = check_atom(atom.bond_partners[1], rule_ids)
#     return check


