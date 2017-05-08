import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cm as cm

def ed2cen(ed):
    cen = .5*(ed[1:]+ed[:-1])
    return cen

data = np.loadtxt('raw.dat')

stars = data[:,0]
approval_ratio = data[:,1]/data[:,2]


bins = [i+.5 for i in range(0,11)]
H, ed = np.histogram(stars, bins=bins)#, density=True)

mean_confidence=np.empty(10)
mean_weight=np.empty(10)
for i in range(1,11):
    mask=data[:,0]==int(i)
    mean_confidence[i-1] = np.mean(approval_ratio[mask])
    mean_weight[i-1] = np.mean(data[:,2][mask])

print(np.min(mean_weight), np.max(mean_weight))

#fig, (ax,ax2) = plt.subplots(2,1)
##l1 = ax.plot(ed2cen(ed), H, 'o', label="1")
#l1 = ax.bar(ed2cen(ed), H,facecolor='#9999ff', edgecolor='white', label="1")
##ax2 = ax.twinx()
#l2 = ax2.scatter(ed2cen(ed), mean_confidence, marker='s', s=mean_weight,
#                 color='r', label='2')

fig, ax = plt.subplots(1,1)
l1 = ax.bar(ed2cen(ed), H,facecolor='#9999ff', edgecolor='white', label="Reviews")
#plt.legend(bbox_to_anchor=(0., 1.0), loc=3, mode="expand", borderaxespad=0.,
#           frameon=False)
plt.legend(bbox_to_anchor=(1.1, 0.9), loc=4, mode="expand", borderaxespad=0.,
           frameon=False)
ax2 = ax.twinx()
l2 = ax2.scatter(ed2cen(ed), mean_confidence, marker='s', s=mean_weight,
                 color='r', label='Approval')
#plt.legend(bbox_to_anchor=(0.3, 1.0), loc=3,  mode="expand", borderaxespad=0.,
#           frameon=False)
plt.legend(bbox_to_anchor=(1.1, 0.8), loc=4,  mode="expand", borderaxespad=0.,
           frameon=False)


#ax2.fill_between(ed2cen(ed),mean_confidence)
ax2.set_ylabel("Approval")
ax2.set_xlabel("Stars")
ax2.text(0.65,.4,"Approval := Usefulness/Total\nSize := Total")
ax.set_ylabel("#Reviews")
fig.suptitle("Star Wars - The Force Awakens IMDB Reviews")
#plt.legend()
#ax2.plot(ed2cen(ed), mean_weight, 'g^')
#ax.set_label("1")
#ax2.set_label("2", )


mask=data[:,0]<6
bad = len(data[mask])
mask=data[:,0]>6
good = len(data[mask])
mask=data[:,0]==6
even = len(data[mask])
print("TOTAL = ", bad+good+even)
print("bad = %i, even = %i, good = %i" % (bad, even, good))

average=0
for i in range(1,11): average+=i*H[i-1]
print("average = %f" % (average/(bad+good+even)) )

fig2, ax3 = plt.subplots(1,1)
J, st_ed, ap_ed = np.histogram2d(stars,approval_ratio )
X, Y = np.meshgrid(st_ed, ap_ed)
M = ax3.pcolormesh(X, Y, J)
ax3.set_xlabel("Stars")
ax3.set_ylabel("Approval")
cb = plt.colorbar(M)
cb.set_label("Reviews")
plt.title("Stars vs Approval review distribution")


plt.show()
