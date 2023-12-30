"""置き石の座標。
"""
from typing import List


handicap_coordinate_map = {
    9 : {
        2 : ["G7", "C3",],
        3 : ["C7", "G7", "C3"],
        4 : ["C7", "G7", "C3", "G3"],
        5 : ["C7", "G7", "E5", "C3", "G3"],
        6 : ["C7", "G7", "C5", "G5", "C3", "G3"],
        7 : ["C7", "G7", "C5", "E5", "G5", "C3", "G3"],
        8 : ["C7", "E7", "G7", "C5", "G5", "C3", "E3", "G3"],
        9 : ["C7", "E7", "G7", "C5", "E5", "G5", "C3", "E3", "G3"],
    },
    11 : {
        2 : ["J9", "C3"],
        3 : ["C9", "J9", "C3"],
        4 : ["C9", "J9", "C3", "J3"],
        5 : ["C9", "J9", "F6", "C3", "J3"],
        6 : ["C9", "J9", "C6", "J6", "C3", "J3"],
        7 : ["C9", "J9", "C6", "F6", "J6", "C3", "J3"],
        8 : ["C9", "F9", "J9", "C6", "J6", "C3", "F3", "J3"],
        9 : ["C9", "F9", "J9", "C6", "F6", "J6", "C3", "F3", "J3"],
    },
    13 : {
        2 : ["K10", "D4"],
        3 : ["D10", "K10", "D4"],
        4 : ["D10", "K10", "D4", "K4"],
        5 : ["D10", "K10", "G7", "D4", "K4"],
        6 : ["D10", "K10", "D7", "K7", "D4", "K4"],
        7 : ["D10", "K10", "D7", "G7", "K7", "D4", "K4"],
        8 : ["D10", "G10", "K10", "D7", "K7", "D4", "G4", "K4"],
        9 : ["D10", "G10", "K10", "D7", "G7", "K7", "D4", "G4", "K4"],
    },
    15 : {
        2 : ["M12", "D4"],
        3 : ["D12", "M12", "D4"],
        4 : ["D12", "M12", "D4", "M4"],
        5 : ["D12", "M12", "H8", "D4", "M4"],
        6 : ["D12", "M12", "D8", "M8", "D4", "M4"],
        7 : ["D12", "M12", "D8", "H8", "M8", "D4", "M4"],
        8 : ["D12", "H12", "M12", "D8", "M8", "D4", "H4", "M4"],
        9 : ["D12", "H12", "M12", "D8", "H8", "M8", "D4", "H4", "M4"],
    },
    17 : {
        2 : ["O14", "D4"],
        3 : ["D14", "O14", "D4"],
        4 : ["D14", "O14", "D4", "O4"],
        5 : ["D14", "O14", "J9", "D4", "O4"],
        6 : ["D14", "O14", "D9", "O9", "D4", "O4"],
        7 : ["D14", "O14", "D9", "J9", "O9", "D4", "O4"],
        8 : ["D14", "J14", "O14", "D9", "O9", "D4", "J4", "O4"],
        9 : ["D14", "J14", "O14", "D9", "J9", "O9", "D4", "J4", "O4"],
    },
    19 : {
        2 : ["Q16", "D4"],
        3 : ["D16", "Q16", "D4"],
        4 : ["D16", "Q16", "D4", "Q4"],
        5 : ["D16", "Q16", "K10", "D4", "Q4"],
        6 : ["D16", "Q16", "D10", "Q10", "D4", "Q4"],
        7 : ["D16", "Q16", "D10", "K10", "Q10", "D4", "Q4"],
        8 : ["D16", "K16", "Q16", "D10", "Q10", "D4", "K4", "Q4"],
        9 : ["D16", "K16", "Q16", "D10", "K10", "Q10", "D4", "K4", "Q4"],
    },
}


def get_handicap_coordinates(size: int, handicaps: int) -> List[int]:
    """置き石の座標リストを取得する。

    Args:
        size (int): 碁盤のサイズ。
        handicaps (int): 置き石の数。

    Returns:
        List[int]: 置き石の座標リスト。
    """
    if size in handicap_coordinate_map and \
       handicaps in handicap_coordinate_map[size]:
        return handicap_coordinate_map[size][handicaps]
    return None
