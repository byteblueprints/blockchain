import bitwise_ops.shr_n as shr_n   
import bitwise_ops.rotr_n as rotr_n
import bitwise_ops.xor_n as xor_n
import bitwise_ops.add_n as add_n

def main():
    print("SHR Example:")
    shr_n.shr_n(3454, 5)
    print("\nROTR Example:")
    rotr_n.rotr_n(3454, 5)
    print("\nXOR Example:")
    xor_n.xor_n(3454, 1234)
    print("\nADD Example:")
    add_n.add_n(3454, 1234)


if __name__ == "__main__":
    main()
