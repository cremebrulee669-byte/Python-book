# If a is True and B is False, then from (not(a and b) and (a or b)) or ((a and b) or not (a or b))
# The value will always become True, because on the left side, one of a or b is True and the other is False.
# This means that on the left, (not(a and b)), will be true, because a and b will be False, but it is Not, so it is opposite,
# and the other part of it is a or b, which means atleast one value must be true to make the whole true, making it True and True ending up in True,
# and since the whole thing is something or something, and one side is True and the entire this has an or in the middle, the one true makes the entire expression True.
a = True
b = False
print(not(a and b) and (a or b)) or ((a and b) or not (a or b))