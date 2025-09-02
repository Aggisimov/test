import math

tp = 2
fp=2
fn=11
tn=985

acc = (tp+tn)/(tp+fp+fn+tn)

print(f"{acc*100} %" )  