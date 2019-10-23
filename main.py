#!/usr/bin/env python


def main():
    import segyio
    import numpy as np

    filename = 'BO_Kapuni-3D.sgy'
    with segyio.open(filename, 'r', ignore_geometry=True) as f:
        len(f.trace)
        print(f)


if __name__ == '__main__':
    main()
