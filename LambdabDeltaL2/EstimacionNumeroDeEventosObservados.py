#from matplotlib.pyplot import figure, show
import matplotlib.pyplot as plt
import numpy as np

#XS_LambdaBX_7TeV = 2.36e9 #fb
#Delta_XS_LambdaBX_7TeV = np.sqrt( ((np.sqrt((0.06**2)+(0.12**2))/1.16)**2) + ((2.3/4.7)**2) + ((4.6/19.7)**2) )*1e9 #fb

XS_LambdaBX_7TeV = 1.06e09
Delta_XS_LambdaBX_7TeV = 3.88701e08

#XS_LambdaBX_13TeV = XS_LambdaBX_7TeV*(13./7) #fb
#Delta_XS_LambdaBX_13TeV = Delta_XS_LambdaBX_7TeV*(13./7)

XS_LambdaBX_13TeV = 1.96857e09
Delta_XS_LambdaBX_13TeV = 7.21873e08

XS_LambdaBX2s_13TeV = (1.96857e09)*(6.35/100)
Delta_XS_LambdaBX2s_13TeV = XS_LambdaBX2s_13TeV*np.sqrt(((7.21873e08/1.96857e09)**2)+((0.33/6.35)**2))

print "The 7 TeV xs=", XS_LambdaBX_7TeV, "fb", "+-", (Delta_XS_LambdaBX_7TeV/XS_LambdaBX_7TeV)*100, "%"
print "The 13TeV xs=", XS_LambdaBX_13TeV, "fb", "+-", (Delta_XS_LambdaBX_13TeV/XS_LambdaBX_13TeV)*100, "%"

Luminosity=np.linspace(1,300,1000) #fb-1

Branching_LambdaB_p_pi_mu_mu = np.logspace(-10,-6,100)

MuEff=0.9
TrEff=0.9

TotalAnaEffppimumu = 0.73/100
Delta_TotalAnaEffppimumu = 0.074/100
TotalAnaEffppipipimumu = 0.73*(TrEff**2)/100
Delta_TotalAnaEffppipipimumu = 0.074*(TrEff**2)/100

FixedBR=1e-8
BR1=1e-6
BR2=1e-7
BR3=1e-8
#LambdaB -> p pi mu mu

#ExpectedEvents = XS_LambdaBX_13TeV*(MuEff**2)*(TrEff**2)*np.outer(Luminosity, Branching_LambdaB_p_pi_mu_mu)
ExpectedEvents = XS_LambdaBX_13TeV*(TotalAnaEffppimumu)*np.outer(Luminosity, Branching_LambdaB_p_pi_mu_mu)
Delta_ExpectedEvents = ExpectedEvents*np.sqrt(((Delta_TotalAnaEffppimumu/TotalAnaEffppimumu)**2)+((Delta_XS_LambdaBX_13TeV/XS_LambdaBX_13TeV)**2))

#ExpectedEvents301s = XS_LambdaBX_13TeV*(MuEff**2)*(TrEff**2)*30.*Branching_LambdaB_p_pi_mu_mu
#ExpectedEvents30p1s = 1.35*(XS_LambdaBX_13TeV*(MuEff**2)*(TrEff**2)*30.*Branching_LambdaB_p_pi_mu_mu)
#ExpectedEvents30m1s = 0.65*(XS_LambdaBX_13TeV*(MuEff**2)*(TrEff**2)*30.*Branching_LambdaB_p_pi_mu_mu)
ExpectedEvents301s = XS_LambdaBX_13TeV*(TotalAnaEffppimumu)*30.*Branching_LambdaB_p_pi_mu_mu
Delta_ExpectedEvents301s = ExpectedEvents301s*np.sqrt(((Delta_TotalAnaEffppimumu/TotalAnaEffppimumu)**2)+((Delta_XS_LambdaBX_13TeV/XS_LambdaBX_13TeV)**2))
Relative_Error_1s = Delta_ExpectedEvents301s[0]/ExpectedEvents301s[0]
print "Relative error on expected events for the first signal =", Relative_Error_1s*100, "%" 
EventsBR1 = XS_LambdaBX_13TeV*(TotalAnaEffppimumu)*30.*BR1
EventsBR2 = XS_LambdaBX_13TeV*(TotalAnaEffppimumu)*30.*BR2
EventsBR3 = XS_LambdaBX_13TeV*(TotalAnaEffppimumu)*30.*BR3
print "For BR=1e-6 with signal 1, Expected events =", EventsBR1, "+-", EventsBR1*Relative_Error_1s
print "For BR=1e-7 with signal 1, Expected events =", EventsBR2, "+-", EventsBR2*Relative_Error_1s
print "For BR=1e-8 with signal 1, Expected events =", EventsBR3, "+-", EventsBR3*Relative_Error_1s
#ExpectedEvents30p1s = 1.35*(XS_LambdaBX_13TeV*(TotalAnaEffppimumu)*30.*Branching_LambdaB_p_pi_mu_mu)
#ExpectedEvents30m1s = 0.65*(XS_LambdaBX_13TeV*(TotalAnaEffppimumu)*30.*Branching_LambdaB_p_pi_mu_mu)
ExpectedEvents30p1s = (1.+Relative_Error_1s)*(XS_LambdaBX_13TeV*(TotalAnaEffppimumu)*30.*Branching_LambdaB_p_pi_mu_mu)
ExpectedEvents30m1s = (1-Relative_Error_1s)*(XS_LambdaBX_13TeV*(TotalAnaEffppimumu)*30.*Branching_LambdaB_p_pi_mu_mu)

#ExpectedEvents3001s = XS_LambdaBX_13TeV*(MuEff**2)*(TrEff**2)*300.*Branching_LambdaB_p_pi_mu_mu
#ExpectedEvents300p1s = 1.35*(XS_LambdaBX_13TeV*(MuEff**2)*(TrEff**2)*300.*Branching_LambdaB_p_pi_mu_mu)
#ExpectedEvents300m1s = 0.65*(XS_LambdaBX_13TeV*(MuEff**2)*(TrEff**2)*300.*Branching_LambdaB_p_pi_mu_mu)
#ExpectedEvents3001s = XS_LambdaBX_13TeV*(TotalAnaEffppimumu)*300.*Branching_LambdaB_p_pi_mu_mu
#ExpectedEvents300p1s = 1.35*(XS_LambdaBX_13TeV*(TotalAnaEffppimumu)*300.*Branching_LambdaB_p_pi_mu_mu)
#ExpectedEvents300m1s = 0.65*(XS_LambdaBX_13TeV*(TotalAnaEffppimumu)*300.*Branching_LambdaB_p_pi_mu_mu)
ExpectedEvents3001s = XS_LambdaBX_13TeV*(TotalAnaEffppimumu)*300.*Branching_LambdaB_p_pi_mu_mu
Delta_ExpectedEvents3001s = ExpectedEvents301s*np.sqrt(((Delta_TotalAnaEffppimumu/TotalAnaEffppimumu)**2)+((Delta_XS_LambdaBX_13TeV/XS_LambdaBX_13TeV)**2))
ExpectedEvents300p1s = (1.+Relative_Error_1s)*(XS_LambdaBX_13TeV*(TotalAnaEffppimumu)*300.*Branching_LambdaB_p_pi_mu_mu)
ExpectedEvents300m1s = (1-Relative_Error_1s)*(XS_LambdaBX_13TeV*(TotalAnaEffppimumu)*300.*Branching_LambdaB_p_pi_mu_mu)

ExpectedEvents30001s = XS_LambdaBX_13TeV*(TotalAnaEffppimumu)*3000.*Branching_LambdaB_p_pi_mu_mu
Delta_ExpectedEvents30001s = ExpectedEvents301s*np.sqrt(((Delta_TotalAnaEffppimumu/TotalAnaEffppimumu)**2)+((Delta_XS_LambdaBX_13TeV/XS_LambdaBX_13TeV)**2))
ExpectedEvents3000p1s = (1.+Relative_Error_1s)*(XS_LambdaBX_13TeV*(TotalAnaEffppimumu)*3000.*Branching_LambdaB_p_pi_mu_mu)
ExpectedEvents3000m1s = (1-Relative_Error_1s)*(XS_LambdaBX_13TeV*(TotalAnaEffppimumu)*3000.*Branching_LambdaB_p_pi_mu_mu)


#ExpectedEvents1sFixedBr = XS_LambdaBX_13TeV*(MuEff**2)*(TrEff**2)*Luminosity*(10e-10)
#ExpectedEventsp1sFixedBr = 1.35*XS_LambdaBX_13TeV*(MuEff**2)*(TrEff**2)*Luminosity*(10e-10)
#ExpectedEventsm1sFixedBr = 0.65*XS_LambdaBX_13TeV*(MuEff**2)*(TrEff**2)*Luminosity*(10e-10)
ExpectedEvents1sFixedBr = XS_LambdaBX_13TeV*(TotalAnaEffppimumu)*Luminosity*(FixedBR)
ExpectedEventsp1sFixedBr = 1.35*XS_LambdaBX_13TeV*(TotalAnaEffppimumu)*Luminosity*(FixedBR)
ExpectedEventsm1sFixedBr = 0.65*XS_LambdaBX_13TeV*(TotalAnaEffppimumu)*Luminosity*(FixedBR)

#LambdaB -> p pi pi mu mu

#ExpectedEvents302s = XS_LambdaBX_13TeV*(MuEff**2)*(TrEff**3)*30.*Branching_LambdaB_p_pi_mu_mu
#ExpectedEvents30p2s = 1.35*(XS_LambdaBX_13TeV*(MuEff**2)*(TrEff**3)*30.*Branching_LambdaB_p_pi_mu_mu)
#ExpectedEvents30m2s = 0.65*(XS_LambdaBX_13TeV*(MuEff**2)*(TrEff**3)*30.*Branching_LambdaB_p_pi_mu_mu)
ExpectedEvents302s = XS_LambdaBX2s_13TeV*(TotalAnaEffppipipimumu)*30.*Branching_LambdaB_p_pi_mu_mu
Delta_ExpectedEvents302s = ExpectedEvents302s*np.sqrt(((Delta_TotalAnaEffppipipimumu/TotalAnaEffppipipimumu)**2)+((Delta_XS_LambdaBX2s_13TeV/XS_LambdaBX2s_13TeV)**2))
Relative_Error_2s = Delta_ExpectedEvents302s[0]/ExpectedEvents302s[0]
print "Relative error on expected events for the second signal =", Relative_Error_2s*100, "%" 
EventsBR1 = XS_LambdaBX2s_13TeV*(TotalAnaEffppimumu)*30.*BR1
EventsBR2 = XS_LambdaBX2s_13TeV*(TotalAnaEffppimumu)*30.*BR2
EventsBR3 = XS_LambdaBX2s_13TeV*(TotalAnaEffppimumu)*30.*BR3
print "For BR=1e-6 with signal 2, Expected events =", EventsBR1, "+-", EventsBR1*Relative_Error_1s
print "For BR=1e-7 with signal 2, Expected events =", EventsBR2, "+-", EventsBR2*Relative_Error_1s
print "For BR=1e-8 with signal 2, Expected events =", EventsBR3, "+-", EventsBR3*Relative_Error_1s
#ExpectedEvents30p2s = 1.35*(XS_LambdaBX_13TeV*(TotalAnaEffppipipimumu)*30.*Branching_LambdaB_p_pi_mu_mu)
#ExpectedEvents30m2s = 0.65*(XS_LambdaBX_13TeV*(TotalAnaEffppipipimumu)*30.*Branching_LambdaB_p_pi_mu_mu)
ExpectedEvents30p2s = (1.+Relative_Error_2s)*(XS_LambdaBX2s_13TeV*(TotalAnaEffppipipimumu)*30.*Branching_LambdaB_p_pi_mu_mu)
ExpectedEvents30m2s = (1-Relative_Error_2s)*(XS_LambdaBX2s_13TeV*(TotalAnaEffppipipimumu)*30.*Branching_LambdaB_p_pi_mu_mu)

#ExpectedEvents3002s = XS_LambdaBX_13TeV*(MuEff**2)*(TrEff**3)*300.*Branching_LambdaB_p_pi_mu_mu
#ExpectedEvents300p2s = 1.35*(XS_LambdaBX_13TeV*(MuEff**2)*(TrEff**3)*300.*Branching_LambdaB_p_pi_mu_mu)
#ExpectedEvents300m2s = 0.65*(XS_LambdaBX_13TeV*(MuEff**2)*(TrEff**3)*300.*Branching_LambdaB_p_pi_mu_mu)
#ExpectedEvents3002s = XS_LambdaBX_13TeV*(TotalAnaEffppipipimumu)*300.*Branching_LambdaB_p_pi_mu_mu
#ExpectedEvents300p2s = 1.35*(XS_LambdaBX_13TeV*(TotalAnaEffppipipimumu)*300.*Branching_LambdaB_p_pi_mu_mu)
#ExpectedEvents300m2s = 0.65*(XS_LambdaBX_13TeV*(TotalAnaEffppipipimumu)*300.*Branching_LambdaB_p_pi_mu_mu)
ExpectedEvents3002s = XS_LambdaBX2s_13TeV*(TotalAnaEffppipipimumu)*300.*Branching_LambdaB_p_pi_mu_mu
ExpectedEvents300p2s = (1.+Relative_Error_2s)*(XS_LambdaBX2s_13TeV*(TotalAnaEffppipipimumu)*300.*Branching_LambdaB_p_pi_mu_mu)
ExpectedEvents300m2s = (1-Relative_Error_2s)*(XS_LambdaBX2s_13TeV*(TotalAnaEffppipipimumu)*300.*Branching_LambdaB_p_pi_mu_mu)

ExpectedEvents30002s = XS_LambdaBX2s_13TeV*(TotalAnaEffppipipimumu)*3000.*Branching_LambdaB_p_pi_mu_mu
ExpectedEvents3000p2s = (1.+Relative_Error_2s)*(XS_LambdaBX2s_13TeV*(TotalAnaEffppipipimumu)*3000.*Branching_LambdaB_p_pi_mu_mu)
ExpectedEvents3000m2s = (1-Relative_Error_2s)*(XS_LambdaBX2s_13TeV*(TotalAnaEffppipipimumu)*3000.*Branching_LambdaB_p_pi_mu_mu)

#ExpectedEvents2sFixedBr = XS_LambdaBX_13TeV*(MuEff**2)*(TrEff**3)*Luminosity*(10e-10)
#ExpectedEventsp2sFixedBr = 1.35*XS_LambdaBX_13TeV*(MuEff**2)*(TrEff**3)*Luminosity*(10e-10)
#ExpectedEventsm2sFixedBr = 0.65*XS_LambdaBX_13TeV*(MuEff**2)*(TrEff**3)*Luminosity*(10e-10)
ExpectedEvents2sFixedBr = XS_LambdaBX2s_13TeV*(TotalAnaEffppipipimumu)*Luminosity*(FixedBR)
ExpectedEventsp2sFixedBr = 1.35*XS_LambdaBX2s_13TeV*(TotalAnaEffppipipimumu)*Luminosity*(FixedBR)
ExpectedEventsm2sFixedBr = 0.65*XS_LambdaBX2s_13TeV*(TotalAnaEffppipipimumu)*Luminosity*(FixedBR)

#OLD PLOT
#fig = plt.figure()
#ax = fig.add_subplot(111)
#
#ColorMap=np.linspace(0.1,1.0,len(ExpectedEvents))
#
#for i in xrange(len(ExpectedEvents)):
#    ax.plot(Branching_LambdaB_p_pi_mu_mu,ExpectedEvents[i],color=str(ColorMap[i]),linestyle='solid')
#
#ax.set_xscale('log')
#ax.set_yscale('log')
#ax.set_xlabel('$Br(\Lambda_{b}\longrightarrow p\pi^{+}\mu^{-}\mu^{-})$')
#ax.set_ylabel('Number of events')
######ax.axhline(y=1.0, xmin=Branching_LambdaB_p_pi_mu_mu[0], xmax=Branching_LambdaB_p_pi_mu_mu[-1], linewidth=5, color = 'g')
#ax.plot((Branching_LambdaB_p_pi_mu_mu[0],Branching_LambdaB_p_pi_mu_mu[-1]),(1.0,1.0),linewidth=3,color="green",linestyle='solid')

#LambdaB -> p pi mu mu

fig1 = plt.figure()
ax1 = fig1.add_subplot(111)

ax1.plot(Branching_LambdaB_p_pi_mu_mu,ExpectedEvents301s,color='g',linestyle='solid', label=r'$\mathcal{L}$ = 30 fb$^{-1}$')
ax1.plot(Branching_LambdaB_p_pi_mu_mu,ExpectedEvents3001s,color='b',linestyle='solid', label=r'$\mathcal{L}$ = 300 fb$^{-1}$')
ax1.plot(Branching_LambdaB_p_pi_mu_mu,ExpectedEvents30001s,color='k',linestyle='solid', label=r'$\mathcal{L}$ = 3000 fb$^{-1}$')
ax1.fill_between(Branching_LambdaB_p_pi_mu_mu, ExpectedEvents30p1s, ExpectedEvents30m1s, color='green', alpha=0.3)
ax1.fill_between(Branching_LambdaB_p_pi_mu_mu, ExpectedEvents300p1s, ExpectedEvents300m1s, color='blue', alpha=0.3)
ax1.fill_between(Branching_LambdaB_p_pi_mu_mu, ExpectedEvents3000p1s, ExpectedEvents3000m1s, color='black', alpha=0.3)

ax1.set_xscale('log')
ax1.set_yscale('log')
ax1.set_xlabel('$BR(\Lambda_{b}^{0}\longrightarrow p\pi^{+}\mu^{-}\mu^{-})$', fontsize=16)
ax1.set_ylabel('Expected events at CMS experiment', fontsize=16)
ax1.plot((Branching_LambdaB_p_pi_mu_mu[0],Branching_LambdaB_p_pi_mu_mu[-1]),(1.0,1.0),linewidth=3,color="black",linestyle='solid')

legend1 = ax1.legend(loc='upper left', shadow=False)

fig12 = plt.figure()
ax12 = fig12.add_subplot(111)

ax12.plot(Luminosity,ExpectedEvents1sFixedBr,color='k',linestyle='solid')#, label='30 fb$^{-1}$')
ax12.fill_between(Luminosity, ExpectedEventsp1sFixedBr, ExpectedEventsm1sFixedBr, color='red', alpha=0.3)

ax12.text( 50, 110, '$BR(\Lambda_{b}^{0}\longrightarrow p\pi^{+}\mu^{-}\mu^{-})=10^{-8}$', fontsize=20)
ax12.set_xlabel('Integrated luminosity [fb$^{-1}$]', fontsize=16)
ax12.set_ylabel('Expected events at CMS', fontsize=16)

#LambdaB -> p pi pi mu mu

fig2 = plt.figure()
ax2 = fig2.add_subplot(111)

ax2.plot(Branching_LambdaB_p_pi_mu_mu,ExpectedEvents302s,color='g',linestyle='solid', label=r'$\mathcal{L}$ = 30 fb$^{-1}$')
ax2.plot(Branching_LambdaB_p_pi_mu_mu,ExpectedEvents3002s,color='b',linestyle='solid', label=r'$\mathcal{L}$ = 300 fb$^{-1}$')
ax2.plot(Branching_LambdaB_p_pi_mu_mu,ExpectedEvents30002s,color='k',linestyle='solid', label=r'$\mathcal{L}$ = 3000 fb$^{-1}$')
ax2.fill_between(Branching_LambdaB_p_pi_mu_mu, ExpectedEvents30p2s, ExpectedEvents30m2s, color='green', alpha=0.3)
ax2.fill_between(Branching_LambdaB_p_pi_mu_mu, ExpectedEvents300p2s, ExpectedEvents300m2s, color='blue', alpha=0.3)
ax2.fill_between(Branching_LambdaB_p_pi_mu_mu, ExpectedEvents3000p2s, ExpectedEvents3000m2s, color='black', alpha=0.3)

ax2.set_xscale('log')
ax2.set_yscale('log')
#ax2.set_xlabel('$Br(\Lambda_{b}\longrightarrow p\pi^{+}\pi^{-}\pi^{+}\mu^{-}\mu^{-})$', fontsize=16)
ax2.set_xlabel('$BR(\Lambda_{b}^{0}\longrightarrow \Lambda_{c}^{+}\pi^{+}\mu^{-}\mu^{-})$', fontsize=16)
ax2.set_ylabel('Expected events at CMS experiment', fontsize=16)
ax2.plot((Branching_LambdaB_p_pi_mu_mu[0],Branching_LambdaB_p_pi_mu_mu[-1]),(1.0,1.0),linewidth=3,color="black",linestyle='solid')

legend2 = ax2.legend(loc='upper left', shadow=False)

fig22 = plt.figure()
ax22 = fig22.add_subplot(111)

ax22.plot(Luminosity,ExpectedEvents2sFixedBr,color='k',linestyle='solid')#, label='30 fb$^{-1}$')
ax22.fill_between(Luminosity, ExpectedEventsp2sFixedBr, ExpectedEventsm2sFixedBr, color='red', alpha=0.3)

ax22.text( 50, 100, '$BR(\Lambda_{b}^{0}\longrightarrow \Lambda_{c}^{+}\pi^{+}\mu^{-}\mu^{-})=10^{-8}$', fontsize=20)
ax22.set_xlabel('Integrated luminosity [fb$^{-1}$]', fontsize=16)
ax22.set_ylabel('Expected events at CMS', fontsize=16)

####################################################
##########PLOTS FROM DIEGO##########################
####################################################

figD1 = plt.figure()
axD1 = figD1.add_subplot(111)

XD1=np.array([1e-10,1e-8,1e-6])
YD1=np.array([9.81/100,9.81,981.])
YD1m=(1-0.45)*YD1
YD1p=(1+0.45)*YD1
YD2=np.array([53./100,53.,5300.])
YD2m=(1-0.45)*YD2
YD2p=(1+0.45)*YD2

axD1.plot(XD1,YD1,color='r',linestyle='solid', label=r'$\mathcal{L}$ = 10 fb$^{-1}$')
axD1.plot(XD1,YD2,color='m',linestyle='solid', label=r'$\mathcal{L}$ = 50 fb$^{-1}$')
axD1.fill_between(XD1, YD1p, YD1m, color='red', alpha=0.3)
axD1.fill_between(XD1, YD2p, YD2m, color='magenta', alpha=0.3)

axD1.set_xscale('log')
axD1.set_yscale('log')
axD1.set_xlabel('$BR(\Lambda_{b}^{0}\longrightarrow p\pi^{+}\mu^{-}\mu^{-})$', fontsize=16)
axD1.set_ylabel('Expected events at LHCb experiment', fontsize=16)
axD1.plot((XD1[0],XD1[-1]),(1.0,1.0),linewidth=3,color="black",linestyle='solid')

legendD1 = axD1.legend(loc='upper left', shadow=False)


figD2 = plt.figure()
axD2 = figD2.add_subplot(111)

XD21=np.array([1e-10,1e-8,1e-6])
YD21=np.array([0.5/100,0.5,50.])
YD21m=(1-0.45)*YD21
YD21p=(1+0.45)*YD21
YD22=np.array([2.7/100,2.7,272.])
YD22m=(1-0.45)*YD22
YD22p=(1+0.45)*YD22

axD2.plot(XD21,YD21,color='r',linestyle='solid', label=r'$\mathcal{L}$ = 10 fb$^{-1}$')
axD2.plot(XD21,YD22,color='m',linestyle='solid', label=r'$\mathcal{L}$ = 50 fb$^{-1}$')
axD2.fill_between(XD21, YD21p, YD21m, color='red', alpha=0.3)
axD2.fill_between(XD21, YD22p, YD22m, color='magenta', alpha=0.3)

axD2.set_xscale('log')
axD2.set_yscale('log')
axD2.set_xlabel('$BR(\Lambda_{b}^{0}\longrightarrow \Lambda_{c}^{+}\pi^{+}\mu^{-}\mu^{-})$', fontsize=16)
axD2.set_ylabel('Expected events at LHCb experiment', fontsize=16)
axD2.plot((XD21[0],XD21[-1]),(1.0,1.0),linewidth=3,color="black",linestyle='solid')

legendD2 = axD2.legend(loc='upper left', shadow=False)

plt.show()
