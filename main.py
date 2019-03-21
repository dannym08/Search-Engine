from Index import Index
from Query import Query
        

if __name__ == '__main__':
    ''' '''
    
    ##path = '/Users/Danny/Desktop/cs121hw3/WEBPAGES_RAW' #Mac Path
    path = r'C:\Users\Danny\Desktop\cs121hw3\WEBPAGES_RAW' ##windows path
    index = Index(path)
    index.create_index()
    index.save_index()
    print("danny")
    #json_data = get_url()
    #path_test ='/Users/Danny/Desktop/cs121hw3/Test'
    #index = loop_urls(path, json_data)
    #save_index(index)
    #print(numOfPages)
    
    # Index loading and query
    #index = load_index()
    ##print(len(index.keys()))
    ##input()
    #print(sorted(index.keys()))
    
    #Q = Query()
    #Q.load_index()
    #count = 1;
    #while True:
    #    query = Q.get_query()
    #    pQuery = Q.process_query(query)
    #    results = Q.process_results(pQuery)
    #    Q.results_to_file(results)
    #    count += 1
