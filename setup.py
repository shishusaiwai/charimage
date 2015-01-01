from setuptools import setup, find_packages
setup(name='charimage',
      version="0.2",
      description="convert black-white image to string which can be displayed in terminal.",
      author="cong liu",
      author_email="shishusaiwai@vip.qq.com",
      license="GPL",
      packages=find_packages(),
      use_2to3=True,
      entry_points={"console_scripts": ["charimage = charimage.main:main"]})
