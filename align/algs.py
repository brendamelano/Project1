
class PairwiseAligner:
  #score matrix
    # M = score matrix - records the score of optimal preceding sub_alignment
    # T = traceback matrix - records the "decision"" of which sub-alignment precedes the current sub-alignment
  # recursive rule
  # traceback rule
    # add a gapped alignment state with 2 decisions: extend or match
      # requires two additional matrices 
        # I_a and I_b which record scores for opening and extending a gap in A or B
  # Gap rules
    # Linear Gap = cost of gap scales with length of gap
      # Y = n*D_gap (where D_gap is negative)
    # Affine Gap penalty
      # cost of gap = cost of opening a gap (high) and cost of extension (low)
        # Y = D_open + (n-1)D_extend * ( D_open = 12, D_extend)
      # M(i,j) gives you the best score of subalignment given that A_i is aligned to B_j
        # pay a cost (D_open) when you enter a gap state from M to I_a and an extension cost (D_extend) when you stay in I_a because you stay there
      # I_a(i,j) = gives you the best score given alignmennt up to A_i terminates in a gap
      # I_a(i,j) = gives you the best score given alignmennt up to A_i terminates in a gap
	pass
	def __init__(string  A, string B, init a, init b):
    self.name = name
    self.color = color
    self.weight = weight
  # add self to every method within the class
  def LCS(self, string  A, string B, init a, init b, lookup):
    
    # return 0 if the length of either sequence is 0
    if a == 0 or b == 0:
      return 0;
      
    # creating a unique dict key
    key = (a, b)
    
    # determing whether the dict was seen and stored in a dict
    if key not in lookup:
    
      # if the last character matches
      if A[a -1] == B[b -  1]:
        return LCS(A, B, a-1, b-1) + 1
      
      # if the last characters do not match

# Local Alignment
class SmithWaterman(PairwiseAligner): 
  pass
	
# Global Alignment
class NeedlemanWunsch(PairwiseAligner):
	pass


# is the extend penatly dependent on the length of the sequence?
