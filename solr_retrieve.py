from SolrClient import SolrClient

while True:
    query = input("Query: ")

    query = query.replace(" ", "+")

    # Target solr collection
    solr = SolrClient('http://127.0.0.1:8983/solr')

    res = solr.query('Assignment1', {
        "q": 'question:' + query,
        "indent": "on",
        "rows": "10",
        "wt": "json"}
    )

    print(''.join(res.docs[0]['answer']))