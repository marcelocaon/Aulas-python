#!/usr/bin/env python

import os
import urllib2
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Image

filename = './python-logo.png'

def get_python_image():
    """ Get a python logo image for this example """
    if not os.path.exists(filename):
        response = urllib2.urlopen(
            'http://www.python.org/community/logos/python-logo.png')
        f = open(filename, 'w')
        f.write(response.read())
        f.close()

get_python_image()

doc = SimpleDocTemplate("image.pdf", pagesize=letter)
parts = []
parts.append(Image(filename))
doc.build(parts)




Writing images to a canvas is easy, but has one gotcha.

#!/usr/bin/env python

import os
import urllib2
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas

filename = './python-logo.png'

def get_python_image():
    """ Get a python logo image for this example """
    if not os.path.exists(filename):
        response = urllib2.urlopen(
            'http://www.python.org/community/logos/python-logo.png')
        f = open(filename, 'w')
        f.write(response.read())
        f.close()

get_python_image()

c = canvas.Canvas('imageabs.pdf', pagesize=letter)
width, height = letter
c.drawImage(filename, inch, height - 2 * inch) # Who needs consistency?
c.showPage()
c.save()