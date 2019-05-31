import numpy as np

lon_min = 0
lon_max = 30
#lat_min = 100
#lat_max = 180
lat_min = 260
lat_max = 340
mon_min = 5
mon_max = 11

lead_times = ['6', '12', '24', '48']
for lt in lead_times:
	pos_x     = np.loadtxt("positive_global_MCS_TC_GP_features_"+lt+"hours.txt")
	neg_x     = np.loadtxt("negative_global_MCS_TC_GP_features.txt")

	pos_len  = pos_x.shape[0]
	neg_len  = neg_x.shape[0]

	f_pos = open("positive_NA_MCS_TC_GP_features_"+lt+"hours.txt", "w")
	f_neg = open("negative_NA_MCS_TC_GP_features.txt", "w")


	f_pos_sup = open("positive_NA_MCS_TC_GP_features_"+lt+"hours_sup.txt", "w")
	f_neg_sup = open("negative_NA_MCS_TC_GP_features_sup.txt", "w")

	for pi in range(pos_len):
		if pos_x[pi,0] > lon_min and pos_x[pi,0] < lon_max:
			if pos_x[pi,1] > lat_min and pos_x[pi,1] < lat_max:
				if pos_x[pi,2] > mon_min and pos_x[pi,2] < mon_max:
					np.savetxt(f_pos, (pos_x[pi,:]), newline=" ")
					f_pos.write("\n")
				else:
					np.savetxt(f_pos_sup, (pos_x[pi,:]), newline=" ")
					f_pos_sup.write("\n")
			else:
				np.savetxt(f_pos_sup, (pos_x[pi,:]), newline=" ")
				f_pos_sup.write("\n")
		else:
			np.savetxt(f_pos_sup, (pos_x[pi,:]), newline=" ")
			f_pos_sup.write("\n")

	for ni in range(neg_len):
		if neg_x[ni,0] > lon_min and neg_x[ni,0] < lon_max:
			if neg_x[ni,1] > lat_min and neg_x[ni,1] < lat_max:
				if neg_x[ni,2] > mon_min and neg_x[ni,2] < mon_max:
					np.savetxt(f_neg, (neg_x[ni,:]), newline=" ")
					f_neg.write("\n")
				else:
					np.savetxt(f_neg_sup, (neg_x[ni,:]), newline=" ")
					f_neg_sup.write("\n")
			else:
				np.savetxt(f_neg_sup, (neg_x[ni,:]), newline=" ")
				f_neg_sup.write("\n")
		else:
			np.savetxt(f_neg_sup, (neg_x[ni,:]), newline=" ")
			f_neg_sup.write("\n")
			

	f_pos.close()
	f_neg.close()
	f_pos_sup.close()
	f_neg_sup.close()

