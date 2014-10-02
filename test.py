import sys, os, getopt

import MARDS

def main(argv):
   inputfile = 'examples/bling.MARDS'
   sfile = 'compiled/V1/index.MARDS-schema'
   debug = False
   try:
      opts, args = getopt.getopt(argv,"hdi:s:",["ifile=","sfile=","debug"])
   except getopt.GetoptError:
      print 'test.py -i <docfile> -s <schemafile>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'test.py -i <ifile> -s <sfile> (default = mr recipe.MARDS-schema> -d <debug>'
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-s", "--sfile"):
         sfile = arg
      elif opt in ("-d", "--debug"):
         debug = True

   print 'docfile is: ', inputfile
   print 'Schema file is: ', sfile
   with open(inputfile, 'r') as docfile:
      doc = docfile.read()
   with open(sfile, 'r') as schemafile:
      schema = schemafile.read()

   if debug == True:
      x,e = MARDS.ml.SCHEMA_to_rolne(schema)
   else:
      x,e = MARDS.string_to_rolne(doc, schema_file=sfile)
   
   print "FINAL:\n"
   print x._explicit()
   print "ERRORS:\n"
   for err in e:
        print repr(err)

if __name__ == "__main__":
   main(sys.argv[1:])



