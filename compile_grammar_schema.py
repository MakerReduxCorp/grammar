import sys, os, glob

import MARDS

schema_file = 'src/V1/index.MARDS-schema'
print 'Schema file is:', schema_file

compile_dir = 'compiled/V1'
print 'Destination for compiled MARDS-schema is:', compile_dir

print
print "Creating compiled version..."

print "  Erasing previous content..."
if not os.path.exists(compile_dir):
    os.makedirs(compile_dir)
else:
    files = glob.glob(compile_dir+"/*.MARDS-schema")
    for f in files:
        os.remove(f)
print "    done."
print

print "  Compiling MARDS-schema..."
with open(schema_file, "r") as fh:
    schema_text = fh.read()
    schema_dir = os.path.dirname(os.path.realpath(schema_file))
schema,e = MARDS.ml.SCHEMA_to_rolne(doc=schema_text, schema_dir=schema_dir)
print "    compile errors:"
print "     ",repr(e)
print "    done."
print



print "  Creating files..."
print "    text..."
new_schema_text = MARDS.rolne_to_string(schema)
new_workstep_text = MARDS.rolne_to_string(schema.only(("name", "workstep")))
new_part_text = MARDS.rolne_to_string(schema.only(("name", "part")))
new_parameter_text = MARDS.rolne_to_string(schema.only(("name", "parameter")))
del schema["name", "maker"]["required"]
new_maker_text = MARDS.rolne_to_string(schema.only(("name", "maker")))
print "    index file..."
with open(compile_dir+"/index.MARDS-schema", "w") as fh:
    fh.write(new_schema_text)
    fh.close()
print "    workstep file..."
with open(compile_dir+"/workstep.MARDS-schema", "w") as fh:
    fh.write(new_workstep_text)
    fh.close()
print "    part file..."
with open(compile_dir+"/part.MARDS-schema", "w") as fh:
    fh.write(new_part_text)
    fh.close()
print "    parameter file..."
with open(compile_dir+"/parameter.MARDS-schema", "w") as fh:
    fh.write(new_parameter_text)
    fh.close()
print "    maker file..."
with open(compile_dir+"/maker.MARDS-schema", "w") as fh:
    fh.write(new_maker_text)
    fh.close()
print "    done."
print

print "done."
