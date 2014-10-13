import sys, os, glob

import MARDS
fh = open("version.txt", 'r')
text = fh.read()
fh.close()
dict_schema = {}
for line in text.split("\n"):
    if not line:
       continue
    print 'processing:', line + '\n'
    t, ver = line.split(" ", 1)

    if t != "#":

        schema_file = 'src/'+ver+'/index.MARDS-schema'
        print 'Schema file is:', schema_file

        dest_dir = 'docs'
        if ver != 'latest':
            dest_dir += '/'+ver
        print 'Destination for docs is:', dest_dir

        breakdown_file = 'src/'+ver+'/documentation.MARDS'
        print 'Breakdown MARDS for doc is:', breakdown_file


        print
        print "Creating docs..."

        print "  Erasing previous content..."
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
        else:
            files = glob.glob(dest_dir+"/*.rst")
            for f in files:
                os.remove(f)
        print "    done."
        print

        print "  Compiling Schema..."
        with open(schema_file, "r") as fh:
            schema_text = fh.read()
            schema_dir = os.path.dirname(os.path.realpath(schema_file))
        schema,e = MARDS.ml.SCHEMA_to_rolne(doc=schema_text, schema_dir=schema_dir)
        print "    compile errors:"
        print "     ",repr(e)
        print "    done."
        print

        print "  Compiling Breakdown..."
        with open(breakdown_file, "r") as fh:
            breakdown_text = fh.read()
        breakdown, e = MARDS.string_to_rolne(breakdown_text)
        print "    compile errors:"
        print "     ",repr(e)
        print "    done."
        print

        print "  Creating RST files..."
        MARDS.doc.generate_rst_files(schema, breakdown, dest_dir)
        print "    done."
        print

        print "done."
