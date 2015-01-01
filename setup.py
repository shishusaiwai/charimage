from setuptools import setup, find_packages
setup(name='charimage',
      version="0.3",
      description="convert black-white image to string which can be displayed in terminal.",
      author="cong liu",
      author_email="shishusaiwai@vip.qq.com",
      license="GPL",
      packages=find_packages(),
      entry_points={"console_scripts": ["charimage = charimage.main:main"]})
