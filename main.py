
import sys
import json
import urllib3

  if __name__ == "__main__":
    query_file = sys.argv[1]
    query_index = 0
    with open(query_file, 'r') as fp:
      for line in fp:
        query = line.rstrip()
        query_index = query_index + 1
        query_gbk = query
        query = query.decode('gbk', 'ignore').encode('utf8', 'ignore')
        url = 'http://10.42.141.12:8089/adrender?query=%s&ad_num=3&srcid=101'\
           '&ip=172.22.182.55&baiduid=61ABB404320C72436EB6B8352DFBB388:FG=1' % (query)
        req = urllib3.urlopen(url)
        page = req.read()
        ddict = json.loads(page)
        expid = ddict['expid']
        sid = ddict['sid']
        ad_num = ddict['response_adnum']
        for i in range(0, ad_num):
          output_html = '%s-%d.html' % (query_gbk, i)
          output = open(output_html, 'w')
          ad = ddict['response_ads'][i].encode('utf8', 'ignore')

          output.write("%s" % (ad))


          output.close()