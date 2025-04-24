def main():
    import pandas as pd 
    cars=int(input("Enter no. of cars:"))
    asking_price=input("Enter asking prices: ")
    values=list(map(int,asking_price.split()))
    asking_prices=pd.Series(values)
    fair_price=input("Enter fair prices: ")
    values=list(map(int,fair_price.split()))
    fair_prices=pd.Series(values)
    good_deals=asking_prices<=fair_prices 
    good_deals_indices=good_deals[good_deals].index.tolist() 
    print("Indice of good deals:", good_deals_indices) 
if __name__=='__main__':
    main()