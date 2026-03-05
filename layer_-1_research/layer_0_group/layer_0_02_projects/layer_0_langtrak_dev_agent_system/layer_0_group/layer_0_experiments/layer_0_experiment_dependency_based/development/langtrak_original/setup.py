# resource_id: "f5361780-a742-4c16-8e51-09b5dac01767"
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
