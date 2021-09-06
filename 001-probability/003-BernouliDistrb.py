# -*- coding: utf-8 -*-
#author : Amitava Chakraborty

#Bernoulli distribution - a special case of the Binomial distribution 
#where a single experiment is conducted so that the number of observation is 1, (n=1)
#Hence Bernoulli distribution describes events having exactly two outcomes -  1 (success) and 0 (failure), 
#and a single trial, for example, a coin toss. 
#So the random variable X which has a Bernoulli distribution can take value 1 with the probability of success, p, 
#and the value 0 with the probability of failure, q or 1−p. 
#The probabilities of success and failure need not be equally likely. 



from scipy.stats import bernoulli
import seaborn as sb

#A bernouli distribution data 
#We generate a bernoulli distributed discrete random variable using scipy.stats module's bernoulli.rvs() 
#p (probability of success) is a shape parameter. 
#To shift distribution use the loc parameter. 
#size decides the number of times to repeat the trials. 
#To maintain reproducibility, include a random_state argument assigned to a number.
data = bernoulli.rvs(size=1000,p=0.6)

print(data)
ax = sb.distplot(data,
                  kde=True,
                  color='blue',
                  hist_kws={"linewidth": 25,'alpha':1})
ax.set(xlabel='Bernouli', ylabel='Frequency')

#%% 
p=0.531
rv = bernoulli(p)
print (rv)
#%%
x = np.arange(0, np.minimum(rv.dist.b, 3))
h = plt.vlines(x, 0, rv.pmf(x), lw=2)
#Here, rv.dist.b is the right endpoint of the support of rv.dist.
#%%
#Check accuracy of cdf and ppf
prb = bernoulli.cdf(x, p)
h = plt.semilogy(np.abs(x - bernoulli.ppf(prb, p)) + 1e-20)
#%%- Random number generation
R = bernoulli.rvs(p, size=100)
print (R)
