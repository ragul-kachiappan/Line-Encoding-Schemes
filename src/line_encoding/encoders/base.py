"""Base encoding functions for line encoding schemes."""

from typing import List


def unipolar(b: List[int]) -> List[int]:
    """Unipolar encoding.
    
    Args:
        b: List of binary input bits
        
    Returns:
        List of encoded values
    """
    e = list(b)
    e.append(e[-1])  # appending the last element again to display a continuous step function graph
    return e


def nrz_l(b: List[int]) -> List[int]:
    """NRZ-L (Non-Return-to-Zero Level) encoding.
    
    Args:
        b: List of binary input bits
        
    Returns:
        List of encoded values (-1 for 0, 1 for 1)
    """
    e = list(b)
    e = [-1 if i == 0 else 1 for i in e]  # assigns -1 if the binary input is 0, 1 for binary input 1
    e.append(e[-1])
    return e


def nrz_i(b: List[int]) -> List[int]:
    """NRZ-I (Non-Return-to-Zero Inverted) encoding.
    
    Args:
        b: List of binary input bits
        
    Returns:
        List of encoded values
    """
    e = list(b)
    
    for i in range(len(b)):
        if i == 0:  # assuming that the signal was "high" before receiving binary input
            if b[i] == 1:
                e[i] = -1
                continue
            else:
                e[i] = 1
                continue
        if b[i] == 1 and i != 0:
            if e[i-1] == -1:
                e[i] = 1
                continue
            else:
                e[i] = -1
                continue
        else:
            e[i] = e[i-1]
    e.append(e[-1])
    
    return e


def polar_rz(b: List[int]) -> List[int]:
    """Polar Return-to-Zero encoding.
    
    Args:
        b: List of binary input bits
        
    Returns:
        List of encoded values
    """
    li = list(b)
    li = [-1 if i == 0 else 1 for i in b]
    e = []
    for i in range(len(b)):
        e.append(li[i])
        e.append(0)  # for appending '0s' between elements for mid-transition
    e.append(e[-1])
    return e


def biphase_manchester(b: List[int]) -> List[int]:
    """Biphase Manchester encoding.
    
    Args:
        b: List of binary input bits
        
    Returns:
        List of encoded values
    """
    e = []
    for i in range(len(b)):
        if b[i] == 1:  # -1 to 1 to denote signal 1
            e.append(-1)
            e.append(1)
        else:
            e.append(1)  # 1 to -1 to denote signal 0
            e.append(-1)
    e.append(e[-1])
    return e


def diff_manchester(b: List[int]) -> List[int]:
    """Differential Manchester encoding.
    
    Args:
        b: List of binary input bits
        
    Returns:
        List of encoded values
    """
    e = []
    for i in range(len(b)):
        if i == 0:  # assuming that the signal was high before receiving binary input
            if b[i] == 0:
                e.append(-1)
                e.append(1)
            else:
                e.append(1)
                e.append(-1)
        else:
            if b[i] == 1:
                e.append(e[-1])
                if e[-1] == 1:
                    e.append(-1)
                else:
                    e.append(1)
            else:
                if e[-1] == -1:
                    e.append(1)
                    e.append(-1)
                else:
                    e.append(-1)
                    e.append(1)
    e.append(e[-1])
    return e


def ami(b: List[int]) -> List[int]:
    """Alternate Mark Inversion (AMI) encoding.
    
    Args:
        b: List of binary input bits
        
    Returns:
        List of encoded values
    """
    e = []
    first = 1
    flag = 0
    for i in range(len(b)):
        if b[i] == 0:
            e.append(0)
        else:
            if first:
                e.append(1)
                flag = 1
                first = 0
            else:
                if flag == 1:
                    e.append(-1)
                    flag = 0
                else:
                    e.append(1)
                    flag = 1
    e.append(-1)
    return e


def pseudo(b: List[int]) -> List[int]:
    """Pseudoternary encoding.
    
    Args:
        b: List of binary input bits
        
    Returns:
        List of encoded values
    """
    e = []
    first = 1
    flag = 0
    for i in range(len(b)):
        if b[i] == 1:
            e.append(0)
        else:
            if first:
                e.append(1)
                flag = 1
                first = 0
            else:
                if flag == 1:
                    e.append(-1)
                    flag = 0
                else:
                    e.append(1)
                    flag = 1
    e.append(-1)
    return e 