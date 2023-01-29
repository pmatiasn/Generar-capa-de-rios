import arcpy
from arcpy.sa import *

# Establecer el entorno de trabajo
arcpy.env.workspace = r"<espacio de trabajo>"

# Asignar la entrada de raster
inRaster = "<dem>"
    
# Ejecutar el proceso Fill
outFill = Fill(inRaster)
   
# Ejecutar el proceso FlowDirection
outFlow = FlowDirection(outFill)

# Ejecutar el proceso FlowAccumulation
outAccum = FlowAccumulation(outFlow)
    
# Utilizar la Calculadora de Raster para aplicar la expresión lógica
outLog = Log10(outAccum)
  
# Utilizar la Calculadora de Raster para aplicar la expresión Con
outCon = Con(outLog > 3, outLog)

# Ejecutar la herramienta Stream Link
outStreamLink = StreamLink(outCon, outFlow)

# Ejecutar la herramienta Stream Order
outStreamOrder = StreamOrder(outStreamLink, outFlow)
    
# Ejecutar la herramienta Stream to Feature
outStreamFeature = StreamToFeature(outStreamOrder, outFlow, "<capa de salida>")
