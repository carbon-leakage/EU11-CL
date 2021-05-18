import pandas as pd
import pypsa

def co2_price_update(network,co2_price,alpha):
    gdp_per_capita=co2_price_distribution(network,co2_price,alpha)
    
    for i,generator in network.generators.iterrows():
        marginal = network.carriers.loc[network.generators.loc[i]['carrier']]['marginal']
        co2_emissions = network.carriers.loc[network.generators.loc[i]['carrier']]['co2_emissions']
        co2_price = gdp_per_capita.loc[network.generators.loc[i]['bus']]['co2_prices']
        network.generators.loc[i,'marginal_cost']=marginal+co2_emissions*co2_price
    return network

def co2_price_distribution(network,co2_price,alpha):
    gdp_per_capita = pd.read_csv('gdp_per_capita.csv',index_col=0)
    gdp_per_capita['co2_prices'] = 0.0
    
    avg_gdp = 0.
    for i,bus in gdp_per_capita.iterrows():
        avg_gdp += network.loads_t.p_set.sum().loc[i]*gdp_per_capita.loc[i]['GDP per capita']
    avg_gdp=avg_gdp/network.loads_t.p_set.sum().sum()
    
    for i,bus in gdp_per_capita.iterrows():
        co2_price_n = alpha*co2_price*gdp_per_capita.loc[i]['GDP per capita']/avg_gdp+co2_price-alpha*co2_price
        if co2_price_n < 0.:
            co2_price_n=0.
        gdp_per_capita.loc[i,'co2_prices']=co2_price_n  
    return gdp_per_capita
