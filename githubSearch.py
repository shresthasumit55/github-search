from github import Github

print("Enter the authentication token")
ACCESS_TOKEN = input()

file = open('myfile.txt', 'w')
g = Github(ACCESS_TOKEN)
 
def search_github(keyword):
    rate_limit = g.get_rate_limit()
    rate = rate_limit.search
    if rate.remaining == 0:
        print(f'You have 0/{rate.limit} API calls remaining. Reset time: {rate.reset}')
        return
    else:
        print(f'You have {rate.remaining}/{rate.limit} API calls remaining')
 
    query = keyword+ "in:file"
    result = g.search_code(query, order='desc')
 
    max_size = 100
    print(f'Found {result.totalCount} file(s)')
    if result.totalCount > max_size:
        result = result[:max_size]

    output = []

    for file in result:
        output.append(file.html_url + "\n")

    return output
 
if __name__ == '__main__':

    keywords = ["changeitematkey","isonheap","getsubmissiontime","invertexrange","currentsystemtime",
    "rebalancepathtoroot","removeminitem","singlerotateleft","singlerotateright","submissiontime",
    "isendlocation","iterationadvance","endlocation","getnumitems","iterationbegin","iterationdone",
    "validlocationcount","verifybalance","iterationcurrent","doublecapacity","getstartlocation",
    "isvalidlocation","iterationmode","requiredtime","validlocations","encryptiontree","nextletter",
    "indextochange","avltree","printpreorder","locationstack","verifysearchorder","datatoheap","arrayqueue",
    "locationstacknode","numitems","bstnode","arrayheap","avlnode","heapandfreestack"]
    
    for keyword in keywords:
        file.write(keyword+"\n")
        file.writelines(search_github(keyword))
        file.write("\n")

