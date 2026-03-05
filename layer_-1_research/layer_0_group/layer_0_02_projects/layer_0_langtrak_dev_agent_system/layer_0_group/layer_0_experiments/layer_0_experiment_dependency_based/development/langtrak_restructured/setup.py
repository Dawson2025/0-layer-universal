# resource_id: "1b05c522-1541-41c9-af5c-8236bb4c38c4"
# resource_type: "document"
# resource_name: "setup"
from setuptools import setup
from make_sphinx_documentation import BuildDocsCommand

BuildDocsCommand.sourcedir = "docs"

setup(
    cmdclass={
        'build_docs': BuildDocsCommand, # Run to build the documentation
    },
    
    include_package_data=True
)
