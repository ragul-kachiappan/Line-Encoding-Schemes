"""Visualization functions for line encoding schemes."""

import matplotlib.pyplot as plt
from typing import List

from ..encoders.base import (
    unipolar,
    nrz_l,
    nrz_i,
    polar_rz,
    biphase_manchester,
    diff_manchester,
    ami,
    pseudo,
)


def plot_all(c: List[int], b: List[int], bout: List[int]) -> None:
    """Plot all encoding techniques.
    
    Args:
        c: Clock signal
        b: Input binary sequence
        bout: Extended input sequence
    """
    plt.subplot(5, 2, 1)
    plt.ylabel("Clock")
    plt.plot(c, color='black', drawstyle='steps-post', marker='>')
    plt.grid()
    
    plt.subplot(5, 2, 2)
    plt.ylabel("Input")
    plt.plot(bout, color='red', drawstyle='steps-post', marker='>')
    plt.grid()
    
    plt.subplot(5, 2, 3)
    plt.ylabel("Unipolar-NRZ")
    plt.plot(unipolar(b), color='red', drawstyle='steps-post', marker='>')
    plt.grid()
    
    plt.subplot(5, 2, 4)
    plt.ylabel("P-NRZ-L")
    plt.plot(nrz_l(b), color='red', drawstyle='steps-post', marker='>')
    plt.grid()
    
    plt.subplot(5, 2, 5)
    plt.ylabel("P-NRZ-I")
    plt.plot(nrz_i(b), color='red', drawstyle='steps-post', marker='>')
    plt.grid()
    
    plt.subplot(5, 2, 6)
    plt.ylabel("Polar-RZ")
    plt.plot(polar_rz(b), color='red', drawstyle='steps-post', marker='>')
    plt.grid()
    
    plt.subplot(5, 2, 7)
    plt.ylabel("B_Man")
    plt.plot(biphase_manchester(b), color='red', drawstyle='steps-post', marker='>')
    plt.grid()
    
    plt.subplot(5, 2, 8)
    plt.ylabel("Dif_Man")
    plt.plot(diff_manchester(b), color='red', drawstyle='steps-post', marker='>')
    plt.grid()
    
    plt.subplot(5, 2, 9)
    plt.ylabel("Bipolar_AMI")
    plt.plot(ami(b), color='red', drawstyle='steps-post', marker='>')
    plt.grid()
    
    plt.subplot(5, 2, 10)
    plt.ylabel("Bipolar_pseudoternary")
    plt.plot(pseudo(b), color='red', drawstyle='steps-post', marker='>')
    plt.grid()
    
    plt.show()


def plot_single(c: List[int], b: List[int], bout: List[int], encoding_type: str) -> None:
    """Plot a single encoding technique.
    
    Args:
        c: Clock signal
        b: Input binary sequence
        bout: Extended input sequence
        encoding_type: Type of encoding to plot
    """
    plt.subplot(3, 1, 1)
    plt.ylabel("Clock")
    plt.plot(c, color='black', drawstyle='steps-post', marker='>')
    plt.grid()
    
    plt.subplot(3, 1, 2)
    plt.ylabel("Input data")
    plt.plot(bout, color='red', drawstyle='steps-post', marker='>')
    plt.grid()
    
    plt.subplot(3, 1, 3)
    
    if encoding_type == "unipolar":
        plt.ylabel("Unipolar-NRZ")
        plt.plot(unipolar(b), color='red', drawstyle='steps-post', marker='>')
    elif encoding_type == "nrz_l":
        plt.ylabel("polar-NRZ-L")
        plt.plot(nrz_l(b), color='red', drawstyle='steps-post', marker='>')
    elif encoding_type == "nrz_i":
        plt.ylabel("polar-NRZ-I")
        plt.plot(nrz_i(b), color='red', drawstyle='steps-post', marker='>')
    elif encoding_type == "polar_rz":
        plt.ylabel("polar-RZ")
        plt.plot(polar_rz(b), color='red', drawstyle='steps-post', marker='>')
    elif encoding_type == "manchester":
        plt.ylabel("Biphase Manchester")
        plt.plot(biphase_manchester(b), color='red', drawstyle='steps-post', marker='>')
    elif encoding_type == "diff_manchester":
        plt.ylabel("Differential-Manchester")
        plt.plot(diff_manchester(b), color='red', drawstyle='steps-post', marker='>')
    elif encoding_type == "ami":
        plt.ylabel("Bipolar_AMI")
        plt.plot(ami(b), color='red', drawstyle='steps-post', marker='>')
    elif encoding_type == "pseudo":
        plt.ylabel("Bipolar_pseudoternary")
        plt.plot(pseudo(b), color='red', drawstyle='steps-post', marker='>')
    
    plt.grid()
    plt.show() 