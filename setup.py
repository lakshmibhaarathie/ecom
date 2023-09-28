from setuptools import setup,find_packages

__version__ = "0.0.0"
REPO_NAME = "ECommerce-API"
AUTHOR_USER_NAME = "lakshmibhaarathi"
API_REPO = "ecommerce_api"
AUTHOR_EMAIL = "lakshmibhaarathiofcl@gmail.com"

setup(
    name=API_REPO,
    version=__version__,
    author= AUTHOR_USER_NAME,
    description="An Ecommerce API",
    long_description_content='text\markdown',
    url=f'https://github.com/{AUTHOR_USER_NAME}/{API_REPO}',
    project_urls={
        "Bug Tracker" : f'https"//github.com/{AUTHOR_USER_NAME}/{API_REPO}/issues',
    },
    packages=find_packages()
)   