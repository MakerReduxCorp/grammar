import sys, os, glob

import MARDS

schema_file = 'src/V1/index.MARDS-schema'
print 'Schema file is:', schema_file

dest_dir = 'docs'
print 'Destination for docs is:', dest_dir

breakdown_file = 'src/V1/documentation.MARDS'
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
