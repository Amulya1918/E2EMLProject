from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    const = '-e .'
    '''
    This function returns the list of the requirements
    '''
    with open(file_path) as fileobj:
        requirements = fileobj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if const in requirements:
            requirements.remove(const)
    return requirements

# Get requirements from the requirements.txt file
install_requires = get_requirements(r'D:\\DataAmulyaWorking\AIMLGenAILearning\\MLE2EProject\\requirements.txt')

# Print the requirements to check them
print(install_requires)

# Setup the package
setup(
    name="End to End ML Project",
    version='0.0.1',
    author='Amulya',
    author_email='amulya16505@gmail.com',
    install_requires=install_requires,
    packages=find_packages()  # Assuming you want to find the packages automatically
)
