import csv
import json

import pandas as pd
import graphlab

#u_cols = ['user_id', 'user_name']
#users = pd.read_csv('users.csv', sep=',', names=u_cols, header=0)

#r_cols = ['user_id', 'product_id','rating']
#ratings = pd.read_csv('user-prod.csv', sep=',', names=r_cols, header=0)

#Reading items file:
#i_cols = ['url@6pm','sku@6pm','brand@6pm','imp_desc@6pm','title@6pm','gender@6pm','img@6pm','now_price@6pm','orig_price@6pm','color@6pm','url@eastbay','gender@eastbay','imp_desc@eastbay','description@eastbay','sku@eastbay','orig_price@eastbay','now_price@eastbay','img@eastbay','Confidence@6pm_ebay_jw_90','url@zappos','imp_desc@zappos','sku@zappos','brand@zappos','description@zappos','rating@zappos','img@zappos','now_price@zappos','orig_price@zappos','Confidence','product_id']
#items = pd.read_csv('prod.csv', sep=',', names=i_cols, header=0)


r_cols = ['user_id', 'product_id', 'rating']
ratings_base = pd.read_csv('user-prod.csv', sep=',', names=r_cols, header=0)
#ratings_test = pd.read_csv('ua.test', sep='\t', names=r_cols, encoding='latin-1')


train_data = graphlab.SFrame(ratings_base)
#test_data = graphlab.SFrame(ratings_test)

popularity_model = graphlab.popularity_recommender.create(train_data,user_id='user_id',item_id='product_id', target='rating')

popularity_recomm = popularity_model.recommend(users=range(1,998), k=5)

csvwriter = csv.writer(open('recommed_new.csv','wb'))
csvwriter.writerow(['user_id','product_id','score','rank'])
for items in popularity_recomm:
    csvwriter.writerow([items['user_id'],items['product_id'],items['score'],items['rank']])
#popularity_recomm.print_rows(num_rows=100000)

#model_performance = graphlab.compare(test_data, [popularity_model])
#graphlab.show_comparison(model_performance,[popularity_model])
