"""
Author: DracoY

The main program to run all resources.
"""

import lib as geo

def main():
    A = geo.locate(1, 0, 0)
    B = geo.locate(0, 1, 0)
    O = geo.ORIGIN

    print(A.distance(B))
    print(O.distance(A))

    x = A.mid_pt(B)
    x = geo.to_locate(x)
    print(x)
    print(x.distance(A))

    print(A.section(B, 1, 1))


if __name__ == "__main__":
    main()
