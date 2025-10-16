vip_users = {"ali", "reza", "sara", "hadi"}
normal_users = {"nima", "sara", "hadi", "mahdi"}

set_vip = set(vip_users)
set_normal = set(normal_users)
finally_user = set_vip.symmetric_difference(set_normal)
print(finally_user)