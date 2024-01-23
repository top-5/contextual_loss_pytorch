from setuptools import setup, find_packages

setup(
    name='contextual_loss_pytorch',
    version='1.0',
    description='Contextual Loss w/ PyTorch',
    packages=find_packages(exclude=('tests', 'doc')),
    author='So Uchida',
    author_email='s.aiueo32@gmail.com',
    install_requires=["torch", "torchvision"],
    url='https://github.com/top-5/contextual_loss_pytorch',
)
