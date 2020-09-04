#from matplotlib.pyplot import figure, show
import matplotlib
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42
matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt
import numpy as np

XS_Bs_7TeV = 6.45e09
Delta_XS_Bs_7TeV = 9.28e08

XS_Bs_13TeV = 1.20e10
Delta_XS_Bs_13TeV = 1.72e09

#Ds decay Br
Ds_k_pi_pi = 1.49*0.6920
Ds_k_pi_pi_E = Ds_k_pi_pi*np.sqrt(((0.08/1.49)**2)+((0.05/69.20)**2))
Ds_k_k_pi_1 = 5.50
Ds_k_k_pi_1_E = 0.27
Ds_k_k_pi_2 = 2.32
Ds_k_k_pi_2_E = 0.14
Ds_k_k_pi_3 = 2.60
Ds_k_k_pi_3_E = 0.15
Ds_k_k_pi_4 = 1.55
Ds_k_k_pi_4_E = 0.16
Ds_3tracks = Ds_k_pi_pi+Ds_k_k_pi_1+Ds_k_k_pi_2+Ds_k_k_pi_3+Ds_k_k_pi_4
Ds_3tracks_E = Ds_3tracks*np.sqrt(((Ds_k_pi_pi_E/Ds_k_pi_pi)**2)+((Ds_k_k_pi_1_E/Ds_k_k_pi_1)**2)+((Ds_k_k_pi_2_E/Ds_k_k_pi_2)**2)+((Ds_k_k_pi_3_E/Ds_k_k_pi_3)**2)+((Ds_k_k_pi_4_E/Ds_k_k_pi_4)**2))
#Ds_3tracks =  5.50 #Caso de Diego
#Ds_3tracks_E = 0.27 #Caso de Diego
 
print "Total braching ratio of Ds into three charged tracks:", Ds_3tracks, "+/-", Ds_3tracks_E

XS_Bs2s_13TeV = (XS_Bs_13TeV)*(Ds_3tracks/100)
Delta_XS_Bs2s_13TeV = XS_Bs2s_13TeV*np.sqrt(((Delta_XS_Bs_13TeV/XS_Bs_13TeV)**2)+((Ds_3tracks_E/Ds_3tracks)**2))

print "Cross sections for signal 1"
print "The 7 TeV xs=", XS_Bs_7TeV, "fb", "+-", (Delta_XS_Bs_7TeV/XS_Bs_7TeV)*100, "%"
print "The 13TeV xs=", XS_Bs_13TeV, "fb", "+-", (Delta_XS_Bs_13TeV/XS_Bs_13TeV)*100, "%"

print "Cross sections for signal 2"
#print "The 7 TeV xs=", XS_Bs2s_7TeV, "fb", "+-", (Delta_XS_Bs2s_7TeV/XS_Bs2s_7TeV)*100, "%"
print "The 13TeV xs=", XS_Bs2s_13TeV, "fb", "+-", (Delta_XS_Bs2s_13TeV/XS_Bs2s_13TeV)*100, "%"

#Luminosity=np.linspace(1,300,1000) #fb-1

Branching_Bs_k_pi_mu_mu = np.logspace(-10,-6,100)

TrEff=0.9

TotalAnaEff1s = 1.56/100
Delta_TotalAnaEff1s = 0.05/100
TotalAnaEff2s = 1.56*(TrEff**2)/100
Delta_TotalAnaEff2s = 0.05*(TrEff**2)/100

print "The Bs->Ds pi mu mu efficiency is=", TotalAnaEff2s*100, "+-", (Delta_TotalAnaEff2s)*100, "%"

FixedBR=1e-8
BR1=1e-6
BR2=1e-7
BR3=1e-8

#Bs -> k pi mu mu

#ExpectedEvents = XS_Bs_13TeV*(TotalAnaEff1s)*np.outer(Luminosity, Branching_Bs_k_pi_mu_mu)
#Delta_ExpectedEvents = ExpectedEvents*np.sqrt(((Delta_TotalAnaEff1s/TotalAnaEff1s)**2)+((Delta_XS_Bs_13TeV/XS_Bs_13TeV)**2))

ExpectedEvents301s = XS_Bs_13TeV*(TotalAnaEff1s)*30.*Branching_Bs_k_pi_mu_mu
Delta_ExpectedEvents301s = ExpectedEvents301s*np.sqrt(((Delta_TotalAnaEff1s/TotalAnaEff1s)**2)+((Delta_XS_Bs_13TeV/XS_Bs_13TeV)**2))
Relative_Error_1s = Delta_ExpectedEvents301s[0]/ExpectedEvents301s[0]
print "Relative error on expected events for the first signal =", Relative_Error_1s*100, "%" 
EventsBR1 = XS_Bs_13TeV*(TotalAnaEff1s)*30.*BR1
EventsBR2 = XS_Bs_13TeV*(TotalAnaEff1s)*30.*BR2
EventsBR3 = XS_Bs_13TeV*(TotalAnaEff1s)*30.*BR3
print "For BR=1e-6 with signal 1, Expected events =", EventsBR1, "+-", EventsBR1*Relative_Error_1s
print "For BR=1e-7 with signal 1, Expected events =", EventsBR2, "+-", EventsBR2*Relative_Error_1s
print "For BR=1e-8 with signal 1, Expected events =", EventsBR3, "+-", EventsBR3*Relative_Error_1s
ExpectedEvents30p1s = (1.+Relative_Error_1s)*(XS_Bs_13TeV*(TotalAnaEff1s)*30.*Branching_Bs_k_pi_mu_mu)
ExpectedEvents30m1s = (1-Relative_Error_1s)*(XS_Bs_13TeV*(TotalAnaEff1s)*30.*Branching_Bs_k_pi_mu_mu)

ExpectedEvents3001s = XS_Bs_13TeV*(TotalAnaEff1s)*300.*Branching_Bs_k_pi_mu_mu
Delta_ExpectedEvents3001s = ExpectedEvents301s*np.sqrt(((Delta_TotalAnaEff1s/TotalAnaEff1s)**2)+((Delta_XS_Bs_13TeV/XS_Bs_13TeV)**2))
ExpectedEvents300p1s = (1.+Relative_Error_1s)*(XS_Bs_13TeV*(TotalAnaEff1s)*300.*Branching_Bs_k_pi_mu_mu)
ExpectedEvents300m1s = (1-Relative_Error_1s)*(XS_Bs_13TeV*(TotalAnaEff1s)*300.*Branching_Bs_k_pi_mu_mu)

ExpectedEvents30001s = XS_Bs_13TeV*(TotalAnaEff1s)*3000.*Branching_Bs_k_pi_mu_mu
Delta_ExpectedEvents30001s = ExpectedEvents301s*np.sqrt(((Delta_TotalAnaEff1s/TotalAnaEff1s)**2)+((Delta_XS_Bs_13TeV/XS_Bs_13TeV)**2))
ExpectedEvents3000p1s = (1.+Relative_Error_1s)*(XS_Bs_13TeV*(TotalAnaEff1s)*3000.*Branching_Bs_k_pi_mu_mu)
ExpectedEvents3000m1s = (1-Relative_Error_1s)*(XS_Bs_13TeV*(TotalAnaEff1s)*3000.*Branching_Bs_k_pi_mu_mu)

#ExpectedEvents1sFixedBr = XS_LambdaBX_13TeV*(TotalAnaEffppimumu)*Luminosity*(FixedBR)
#ExpectedEventsp1sFixedBr = 1.35*XS_LambdaBX_13TeV*(TotalAnaEffppimumu)*Luminosity*(FixedBR)
#ExpectedEventsm1sFixedBr = 0.65*XS_LambdaBX_13TeV*(TotalAnaEffppimumu)*Luminosity*(FixedBR)

#Bs -> Ds pi mu mu

ExpectedEvents302s = XS_Bs2s_13TeV*(TotalAnaEff2s)*30.*Branching_Bs_k_pi_mu_mu
Delta_ExpectedEvents302s = ExpectedEvents302s*np.sqrt(((Delta_TotalAnaEff2s/TotalAnaEff2s)**2)+((Delta_XS_Bs2s_13TeV/XS_Bs2s_13TeV)**2))
Relative_Error_2s = Delta_ExpectedEvents302s[0]/ExpectedEvents302s[0]
print "Relative error on expected events for the second signal =", Relative_Error_2s*100, "%" 
EventsBR1 = XS_Bs2s_13TeV*(TotalAnaEff2s)*30.*BR1
EventsBR2 = XS_Bs2s_13TeV*(TotalAnaEff2s)*30.*BR2
EventsBR3 = XS_Bs2s_13TeV*(TotalAnaEff2s)*30.*BR3
print "For BR=1e-6 with signal 2, Expected events =", EventsBR1, "+-", EventsBR1*Relative_Error_1s
print "For BR=1e-7 with signal 2, Expected events =", EventsBR2, "+-", EventsBR2*Relative_Error_1s
print "For BR=1e-8 with signal 2, Expected events =", EventsBR3, "+-", EventsBR3*Relative_Error_1s
ExpectedEvents30p2s = (1.+Relative_Error_2s)*(XS_Bs2s_13TeV*(TotalAnaEff2s)*30.*Branching_Bs_k_pi_mu_mu)
ExpectedEvents30m2s = (1-Relative_Error_2s)*(XS_Bs2s_13TeV*(TotalAnaEff2s)*30.*Branching_Bs_k_pi_mu_mu)

ExpectedEvents3002s = XS_Bs2s_13TeV*(TotalAnaEff2s)*300.*Branching_Bs_k_pi_mu_mu
ExpectedEvents300p2s = (1.+Relative_Error_2s)*(XS_Bs2s_13TeV*(TotalAnaEff2s)*300.*Branching_Bs_k_pi_mu_mu)
ExpectedEvents300m2s = (1-Relative_Error_2s)*(XS_Bs2s_13TeV*(TotalAnaEff2s)*300.*Branching_Bs_k_pi_mu_mu)

ExpectedEvents30002s = XS_Bs2s_13TeV*(TotalAnaEff2s)*3000.*Branching_Bs_k_pi_mu_mu
ExpectedEvents3000p2s = (1.+Relative_Error_2s)*(XS_Bs2s_13TeV*(TotalAnaEff2s)*3000.*Branching_Bs_k_pi_mu_mu)
ExpectedEvents3000m2s = (1-Relative_Error_2s)*(XS_Bs2s_13TeV*(TotalAnaEff2s)*3000.*Branching_Bs_k_pi_mu_mu)

#ExpectedEvents2sFixedBr = XS_Bs2s_13TeV*(TotalAnaEff2s)*Luminosity*(FixedBR)
#ExpectedEventsp2sFixedBr = 1.35*XS_Bs2s_13TeV*(TotalAnaEffppipipimumu)*Luminosity*(FixedBR)
#ExpectedEventsm2sFixedBr = 0.65*XS_Bs2s_13TeV*(TotalAnaEffppipipimumu)*Luminosity*(FixedBR)


#Bs -> k pi mu mu

fig1 = plt.figure()
ax1 = fig1.add_subplot(111)

ax1.plot(Branching_Bs_k_pi_mu_mu,ExpectedEvents301s,color='g',linestyle='solid', label=r'$\mathcal{L}$ = 30 fb$^{-1}$')
ax1.plot(Branching_Bs_k_pi_mu_mu,ExpectedEvents3001s,color='b',linestyle='solid', label=r'$\mathcal{L}$ = 300 fb$^{-1}$')
ax1.plot(Branching_Bs_k_pi_mu_mu,ExpectedEvents30001s,color='k',linestyle='solid', label=r'$\mathcal{L}$ = 3000 fb$^{-1}$')
ax1.fill_between(Branching_Bs_k_pi_mu_mu, ExpectedEvents30p1s, ExpectedEvents30m1s, color='green', alpha=0.3)
ax1.fill_between(Branching_Bs_k_pi_mu_mu, ExpectedEvents300p1s, ExpectedEvents300m1s, color='blue', alpha=0.3)
ax1.fill_between(Branching_Bs_k_pi_mu_mu, ExpectedEvents3000p1s, ExpectedEvents3000m1s, color='black', alpha=0.3)

ax1.set_xscale('log')
ax1.set_yscale('log')
ax1.set_xlabel('$BR(B_{s}^{0}\longrightarrow K^{-}\pi^{-}\mu^{+}\mu^{+})$', fontsize=16)
ax1.set_ylabel('Expected events at CMS experiment', fontsize=16)
ax1.plot((Branching_Bs_k_pi_mu_mu[0],Branching_Bs_k_pi_mu_mu[-1]),(1.0,1.0),linewidth=3,color="black",linestyle='solid')

legend1 = ax1.legend(loc='upper left', shadow=False)

#fig12 = plt.figure()
#ax12 = fig12.add_subplot(111)
#
#ax12.plot(Luminosity,ExpectedEvents1sFixedBr,color='k',linestyle='solid')#, label='30 fb$^{-1}$')
#ax12.fill_between(Luminosity, ExpectedEventsp1sFixedBr, ExpectedEventsm1sFixedBr, color='red', alpha=0.3)

#ax12.text( 50, 110, '$BR(\Lambda_{b}^{0}\longrightarrow p\pi^{+}\mu^{-}\mu^{-})=10^{-8}$', fontsize=20)
#ax12.set_xlabel('Integrated luminosity [fb$^{-1}$]', fontsize=16)
#ax12.set_ylabel('Expected events at CMS', fontsize=16)

#Bs -> Ds pi mu mu

fig2 = plt.figure()
ax2 = fig2.add_subplot(111)

ax2.plot(Branching_Bs_k_pi_mu_mu,ExpectedEvents302s,color='g',linestyle='solid', label=r'$\mathcal{L}$ = 30 fb$^{-1}$')
ax2.plot(Branching_Bs_k_pi_mu_mu,ExpectedEvents3002s,color='b',linestyle='solid', label=r'$\mathcal{L}$ = 300 fb$^{-1}$')
ax2.plot(Branching_Bs_k_pi_mu_mu,ExpectedEvents30002s,color='k',linestyle='solid', label=r'$\mathcal{L}$ = 3000 fb$^{-1}$')
ax2.fill_between(Branching_Bs_k_pi_mu_mu, ExpectedEvents30p2s, ExpectedEvents30m2s, color='green', alpha=0.3)
ax2.fill_between(Branching_Bs_k_pi_mu_mu, ExpectedEvents300p2s, ExpectedEvents300m2s, color='blue', alpha=0.3)
ax2.fill_between(Branching_Bs_k_pi_mu_mu, ExpectedEvents3000p2s, ExpectedEvents3000m2s, color='black', alpha=0.3)

ax2.set_xscale('log')
ax2.set_yscale('log')
ax2.set_xlabel('$BR(B_{s}^{0}\longrightarrow D_{s}^{-}\pi^{-}\mu^{+}\mu^{+})$', fontsize=16)
ax2.set_ylabel('Expected events at CMS experiment', fontsize=16)
ax2.plot((Branching_Bs_k_pi_mu_mu[0],Branching_Bs_k_pi_mu_mu[-1]),(1.0,1.0),linewidth=3,color="black",linestyle='solid')

legend2 = ax2.legend(loc='upper left', shadow=False)

#fig22 = plt.figure()
#ax22 = fig22.add_subplot(111)
#
#ax22.plot(Luminosity,ExpectedEvents2sFixedBr,color='k',linestyle='solid')#, label='30 fb$^{-1}$')
#ax22.fill_between(Luminosity, ExpectedEventsp2sFixedBr, ExpectedEventsm2sFixedBr, color='red', alpha=0.3)
#
#ax22.text( 50, 100, '$BR(\Lambda_{b}^{0}\longrightarrow \Lambda_{c}^{+}\pi^{+}\mu^{-}\mu^{-})=10^{-8}$', fontsize=20)
#ax22.set_xlabel('Integrated luminosity [fb$^{-1}$]', fontsize=16)
#ax22.set_ylabel('Expected events at CMS', fontsize=16)

####################################################
##########PLOTS FROM DIEGO##########################
####################################################
figD1 = plt.figure()
axD1 = figD1.add_subplot(111)

XD1=np.array([1e-10,1e-9,1e-8,1e-7,1e-6])
YD1=np.array([0.158,1.58,15.8,158.,1580.])
YD1m=(1-(51./158))*YD1
YD1p=(1+(51./158))*YD1
YD2=np.array([0.852,8.52,85.2,852.,8520.])
YD2m=(1-(273./852))*YD2
YD2p=(1+(273./852))*YD2

axD1.plot(XD1,YD1,color='r',linestyle='solid', label=r'$\mathcal{L}$ = 10 fb$^{-1}$')
axD1.plot(XD1,YD2,color='m',linestyle='solid', label=r'$\mathcal{L}$ = 50 fb$^{-1}$')
axD1.fill_between(XD1, YD1p, YD1m, color='red', alpha=0.3)
axD1.fill_between(XD1, YD2p, YD2m, color='magenta', alpha=0.3)

axD1.set_xscale('log')
axD1.set_yscale('log')
axD1.set_xlabel('$BR(B_{s}^{0}\longrightarrow K^{-}\pi^{-}\mu^{+}\mu^{+})$', fontsize=16)
axD1.set_ylabel('Expected events at LHCb experiment', fontsize=16)
axD1.plot((XD1[0],XD1[-1]),(1.0,1.0),linewidth=3,color="black",linestyle='solid')

legendD1 = axD1.legend(loc='upper left', shadow=False)


figD2 = plt.figure()
axD2 = figD2.add_subplot(111)

XD21=np.array([1e-10,1e-7,1e-6])
YD21=np.array([7./1000,7.,70.])
YD21m=(1-(22./70))*YD21
YD21p=(1+(22./70))*YD21
YD22=np.array([37.6/1000,37.6,376.])
YD22m=(1-(120./376))*YD22
YD22p=(1+(120./376))*YD22

axD2.plot(XD21,YD21,color='r',linestyle='solid', label=r'$\mathcal{L}$ = 10 fb$^{-1}$')
axD2.plot(XD21,YD22,color='m',linestyle='solid', label=r'$\mathcal{L}$ = 50 fb$^{-1}$')
axD2.fill_between(XD21, YD21p, YD21m, color='red', alpha=0.3)
axD2.fill_between(XD21, YD22p, YD22m, color='magenta', alpha=0.3)

axD2.set_xscale('log')
axD2.set_yscale('log')
axD2.set_xlabel('$BR(B_{s}^{0}\longrightarrow D_{s}^{-}\pi^{-}\mu^{+}\mu^{+})$', fontsize=16)
axD2.set_ylabel('Expected events at LHCb experiment', fontsize=16)
axD2.plot((XD21[0],XD21[-1]),(1.0,1.0),linewidth=3,color="black",linestyle='solid')

legendD2 = axD2.legend(loc='upper left', shadow=False)

plt.show()
