def rgb_to_hls(r,g,b):

  # Convert the RGB values to the range 0-1, this can be done by dividing the value by 255 for 8-bit colour depth

  r = r/255
  g = g/255
  b = b/255
  

  #Find the minimum and maximum values of R, G and B. 

  minimum = min([r,g,b])
  maximum = max([r,g,b])
  
  l = (maximum + minimum)/2
 
  # If the min and max value are the same, it means that there is no saturation. 
  if minimum == maximum:
    s = 0
    hue = 0
  
  else: 
    hue = 1
    if l < 0.5:
      s = (maximum - minimum)/(maximum + minimum)
    else:
      (maximum - minimum)/(2.0 - maximum - minimum)
  
  if hue != 0:

    if r == maximum:
      h = (g-b)/(maximum - minimum)
    elif g == maximum:
      h = 2.0 + (b-r)/(maximum-minimum)
    elif b == maximum:
      h = 4.0 + (r-g)/(maximum-minimum)

  else:
    print("good")
    h = 0
    
  h = h*60
  
  if h < 0:
    h = h + 360
    
  h = round(h)
  l = (round(l*100))
  s = (round(s*100))
  
  return h,s,l
    
print(rgb_to_hls(24,98,118))