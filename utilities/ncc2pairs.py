"""
---- COPYRIGHT ----------------------------------------------------------------
Copyright (C) 2020
Connor Horton (Harvard University)

---- LICENSE ------------------------------------------------------------------
This file is part of GiniQC.

GiniQC is free software: you can redistribute it and/or modify it under the
terms of the GNU Lesser General Public License as published by the Free
Software Foundation, either version 3 of the License, or (at your option) any
later version.

GiniQC is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
details. 

You should have received a copy of the GNU Lesser General Public License along
with this software.  If not, see <http://www.gnu.org/licenses/>.
"""

#pairs columns: readID chr1 pos1 chr2 pos2 strand1 strand2
#ncc columns: chr_a start_a end_a re1_a_start re1_a_end strand_a chr_b start_b end_b re1_b_start re1_b_end strand_b ambig_group pair_id swap_pair
import sys

def main():
	infile = open(sys.argv[1], 'r')
	outfile = open(sys.argv[2], 'a')

	for i, line in enumerate(infile):
		chr_a, start_a, end_a, re1_a_start, re1_a_end, strand_a, chr_b, start_b, end_b, re1_b_start, re1_b_end, strand_b, ambig_group, pair_id, swap_pair = line.strip().split(' ')
		out = [pair_id]
		if strand_a == "+":
			out.extend([chr_a, start_a])
		else:
			out.extend([chr_a, end_a])
		if strand_b == "+":
			out.extend([chr_b, start_b])
		else:
			out.extend([chr_b, end_b])
		out.extend([strand_a, strand_b])
		outfile.write("\t".join(out)+"\n")

	infile.close()
	outfile.close()


if __name__ == '__main__':
	main()