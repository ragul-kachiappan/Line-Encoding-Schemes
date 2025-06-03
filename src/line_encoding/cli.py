"""Command-line interface for line encoding visualization."""

from typing import List

from .visualization.plotter import plot_all, plot_single


def get_binary_input() -> List[int]:
    """Get binary input from user.
    
    Returns:
        List of binary digits
    """
    print("Enter the number of bits in encoded data: ")
    size = int(input())
    b = []
    print(f'Enter the binary bits sequence of length {size} bits: \n')
    for i in range(size):
        print(f'Enter element {i+1}:')
        b.append(int(input()))
    return b


def generate_clock_signal(size: int) -> List[int]:
    """Generate clock signal based on input size.
    
    Args:
        size: Number of bits
        
    Returns:
        List of clock signal values
    """
    c = []
    for i in range(2 * size + 1):
        if i % 2 == 0:
            c.append(1)
        else:
            c.append(0)
    return c


def main() -> None:
    """Main entry point for the CLI."""
    b = get_binary_input()
    bout = list(b)
    bout.append(bout[-1])
    c = generate_clock_signal(len(b))
    
    while True:
        print("\nWhich type of encoding do you want to perform: ")
        print("         1->UNIPOLAR:")
        print("         2->NRZ-L:")
        print("         3->NRZ-I:")
        print("         4->POLAR RZ:")
        print("         5->MANCHESTER:")
        print("         6->Differential Manchester:")
        print("         7->Bipolar AMI:")
        print("         8->Bipolar pseudoternary:")
        print("         9->ALL:")
        print("Enter your choice (1-9): ", end="")
        y = int(input())
        
        encoding_map = {
            1: "unipolar",
            2: "nrz_l",
            3: "nrz_i",
            4: "polar_rz",
            5: "manchester",
            6: "diff_manchester",
            7: "ami",
            8: "pseudo",
        }
        
        if y == 9:
            plot_all(c, b, bout)
        elif y in encoding_map:
            plot_single(c, b, bout, encoding_map[y])
        else:
            print("INVALID CHOICE, TRY AGAIN!!!")
        
        print("Do you want to try again? (y/n) : ", end="")
        choice = input().lower()
        if choice != 'y':
            break


if __name__ == '__main__':
    main() 